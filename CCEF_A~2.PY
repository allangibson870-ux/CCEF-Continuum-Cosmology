import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

A1=1.000; A2=8.971; A3=1.684; E0=311.73
r_min=0.3; r_max=20.0

print("=== CCEF A4 Sensitivity Scan — solve_bvp per A4 ===")

try:
    data=np.load('F0.npy')
    r_grid,F0,dF0=data[0],data[1],data[2]
    idx=np.argsort(r_grid); r_grid,F0,dF0=r_grid[idx],F0[idx],dF0[idx]
    print("Loaded BVP profile.")
except Exception:
    print("Frobenius fallback.")
    r_grid=np.linspace(r_min,r_max,2000)
    a,b=0.836548,-0.018511
    F0=np.pi-a*r_grid+b*r_grid**3*np.exp(-0.8*r_grid)
    dF0=np.gradient(F0,r_grid)
    np.save('F0.npy',np.column_stack((r_grid,F0,dF0)))

F_sp =make_interp_spline(r_grid,F0, k=3,bc_type='natural')
dF_sp=make_interp_spline(r_grid,dF0,k=3,bc_type='natural')

# Gaussian initial guess (same shape as nominal BVP run)
x0=np.linspace(r_min,r_max,300)
mu,sig=2.0,1.5
g  =np.exp(-(x0-mu)**2/(2*sig**2))
dg =-(x0-mu)/sig**2*g
d2g=((x0-mu)**2/sig**4-1/sig**2)*g
d3g=-(x0-mu)/sig**2*((x0-mu)**2/sig**4-3/sig**2)*g
y0_guess=np.vstack([g,dg,d2g,d3g])

def find_mode_bvp(A4v):
    """Run solve_bvp with omega2 free, A4=A4v in the operator."""
    def ode(r,y,p):
        omega2=p[0]
        eta,de,d2e,d3e=y
        F=F_sp(r); Fp=dF_sp(r)
        sF=np.sin(F); cF=np.cos(F); r2=r**2; sF2=sF**2; cF2=cF**2
        Q=(A1*(2*cF-1+np.cos(2*F))/r2
           +2*A2*(Fp**2*(cF2-sF2)+sF2*(1-sF2)/r**4)
           +A4v*cF)          # A4v here
        W=A1+2*A2*Fp**2; lap=d2e+2*de/r
        d4=-(4/r)*d3e+(1/A3)*(A1*lap-Q*eta+omega2*W*eta)
        c=(2*A2/A3)*(Fp**2*lap-sF2*eta/r**4)
        d4+=np.where(np.isfinite(c), c, 0.0)
        return np.vstack([de,d2e,d3e,d4])

    def bc(ya,yb,p):
        # Even-parity regularity + decay + normalisation
        return np.array([ya[1],ya[3],yb[0],yb[1],ya[0]-1.0])

    p_guess=[A4v-0.002]   # initial guess: just below pion threshold
    sol=solve_bvp(ode,bc,x0.copy(),y0_guess.copy(),
                  p=p_guess,tol=1e-6,max_nodes=50000,verbose=0)
    if sol.success:
        return sol.p[0], np.sqrt(abs(sol.p[0]))*E0
    return None, None

# ── A4 scan ───────────────────────────────────────────────────────────────────
A4_scan=[0.490,0.500,0.510,0.520,0.530,0.542,0.550,0.560,0.570,0.580,0.590]

print(f"\n{'A4':>6} {'ω_π (MeV)':>11} {'ω_mode (MeV)':>13} "
      f"{'Δω (MeV)':>10} {'Ratio':>8}  Status")
print("-"*68)

results=[]
for A4v in A4_scan:
    wpi=np.sqrt(A4v)*E0
    o2,wm=find_mode_bvp(A4v)
    if wm is None:
        print(f"{A4v:6.3f} {wpi:11.2f} {'NOT FOUND':>13} "
              f"{'---':>10} {'---':>8}  FAIL")
        results.append((A4v,wpi,None,None,None))
    else:
        dw=wpi-wm; ratio=wm/wpi
        status="bound" if dw>0 else "above"
        print(f"{A4v:6.3f} {wpi:11.2f} {wm:13.2f} {dw:10.2f} {ratio:8.4f}  {status}")
        results.append((A4v,wpi,o2,wm,ratio))

# ── Verdict ───────────────────────────────────────────────────────────────────
valid=[r for r in results if r[3] is not None]
if len(valid)>=3:
    ratios=np.array([r[4] for r in valid])
    mu_r,sg=ratios.mean(),ratios.std()
    print(f"\nTracking ratio:  mean={mu_r:.4f},  std={sg:.4f}")
    if sg<0.005:
        print("→ THRESHOLD RESONANCE — tracks ω_π tightly  [CONJECT]")
    elif sg<0.02:
        print("→ MIXED — threshold + internal structure  [CONJECT]")
    else:
        print("→ GENUINE INTERNAL MODE — sigma analog or dilaton  [CONJECT]")

    A4v_=[r[0] for r in valid]; wpi_=[r[1] for r in valid]
    wm_ =[r[3] for r in valid]; rt_ =list(ratios)

    fig,ax=plt.subplots(1,2,figsize=(12,5))
    ax[0].plot(A4v_,wpi_,'g--o',ms=5,label='ω_π')
    ax[0].plot(A4v_,wm_, 'r-o', ms=5,label='ω_mode')
    ax[0].set_xlabel('A4'); ax[0].set_ylabel('ω (MeV)')
    ax[0].set_title('Breathing mode vs pion threshold')
    ax[0].legend(); ax[0].grid(True)

    ax[1].plot(A4v_,rt_,'b-o',ms=5)
    ax[1].axhline(1.0,color='gray',ls='--',label='perfect tracking')
    ax[1].axhline(mu_r+sg,color='r',ls=':',alpha=0.6)
    ax[1].axhline(mu_r-sg,color='r',ls=':',alpha=0.6,label='±1σ')
    ax[1].set_xlabel('A4'); ax[1].set_ylabel('ω_mode/ω_π')
    ax[1].set_title(f'Track ratio  (std={sg:.4f})')
    ax[1].legend(); ax[1].grid(True)

    plt.suptitle('CCEF A4 Sensitivity: Physical Identity of Breathing Mode')
    plt.tight_layout()
    plt.savefig('ccef_A4_sensitivity.png',dpi=200)
    print("Figure saved: ccef_A4_sensitivity.png")
else:
    print("\nToo few successes. If BVP still fails, share which A4 values converge.")
print("\nA4 sensitivity scan COMPLETE.")
