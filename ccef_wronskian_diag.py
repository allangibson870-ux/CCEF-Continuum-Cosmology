import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import make_interp_spline
import warnings; warnings.filterwarnings('ignore')

A1=1.000; A2=8.971; A3=1.684; A4=0.542; E0=311.73
r_min=0.3; r_max=20.0

data = np.load('F0.npy')
r_grid,F0,dF0 = data[0],data[1],data[2]
idx=np.argsort(r_grid); r_grid,F0,dF0=r_grid[idx],F0[idx],dF0[idx]
F_sp  = make_interp_spline(r_grid,F0, k=3,bc_type='natural')
dF_sp = make_interp_spline(r_grid,dF0,k=3,bc_type='natural')

def rhs(r,y,omega2):
    eta,de,d2e,d3e=y
    F=F_sp(r); Fp=dF_sp(r)
    sF=np.sin(F); cF=np.cos(F); r2=r**2; sF2=sF**2; cF2=cF**2
    Q=(A1*(2*cF-1+np.cos(2*F))/r2
       +2*A2*(Fp**2*(cF2-sF2)+sF2*(1-sF2)/r**4)+A4*cF)
    W=A1+2*A2*Fp**2; lap=d2e+2*de/r
    d4=-(4/r)*d3e+(1/A3)*(A1*lap-Q*eta+omega2*W*eta)
    c=(2*A2/A3)*(Fp**2*lap-sF2*eta/r**4)
    d4+=c if np.isfinite(c) else 0.0
    return [de,d2e,d3e,d4]

omega2=0.541
disc=A1**2-4*A3*(A4-omega2); sd=np.sqrt(max(disc,0))
k1=np.sqrt((A1+sd)/(2*A3)); k2=np.sqrt(max((A1-sd)/(2*A3),0))
print(f"omega2={omega2}, k1={k1:.4f}, k2={k2:.6f}")

r_match=12.0

# Test each integration individually
print("\n--- Forward u1 [1,0,0,0] ---")
s=solve_ivp(lambda r,y:rhs(r,y,omega2),[r_min,r_match],[1,0,0,0],
            method='LSODA',rtol=1e-7,atol=1e-7,max_step=0.05)
print(f"  success={s.success}, t_end={s.t[-1]:.2f}, y={s.y[:,-1]}")

print("\n--- Forward u2 [0,0,1,0] ---")
s=solve_ivp(lambda r,y:rhs(r,y,omega2),[r_min,r_match],[0,0,1,0],
            method='LSODA',rtol=1e-7,atol=1e-7,max_step=0.05)
print(f"  success={s.success}, t_end={s.t[-1]:.2f}, y={s.y[:,-1]}")

print("\n--- Backward v1 from r_max with k1 ---")
ic1=[1,-k1,k1**2,-k1**3]
print(f"  IC={[f'{x:.4f}' for x in ic1]}")
s=solve_ivp(lambda r,y:rhs(r,y,omega2),[r_max,r_match],ic1,
            method='LSODA',rtol=1e-7,atol=1e-7,max_step=0.05)
print(f"  success={s.success}, t_end={s.t[-1]:.2f}, y={s.y[:,-1]}")

print("\n--- Backward v2 from r_max with k2 ---")
ic2=[1,-k2,k2**2,-k2**3]
print(f"  IC={[f'{x:.6f}' for x in ic2]}")
s=solve_ivp(lambda r,y:rhs(r,y,omega2),[r_max,r_match],ic2,
            method='LSODA',rtol=1e-7,atol=1e-7,max_step=0.05)
print(f"  success={s.success}, t_end={s.t[-1]:.2f}, y={s.y[:,-1]}")

# Now scan det values
print("\n--- Det scan (A4=0.542) ---")
def shoot4(ic,t0,t1,o2):
    s=solve_ivp(lambda r,y:rhs(r,y,o2),[t0,t1],ic,
                method='LSODA',rtol=1e-7,atol=1e-7,max_step=0.05)
    return s.y[:,-1] if s.success else None

for o2 in np.linspace(0.528,0.542,15):
    disc=A1**2-4*A3*(A4-o2); sd=np.sqrt(max(disc,0))
    k1_=np.sqrt((A1+sd)/(2*A3)); k2_=np.sqrt(max((A1-sd)/(2*A3),0))
    u1=shoot4([1,0,0,0],r_min,r_match,o2)
    u2=shoot4([0,0,1,0],r_min,r_match,o2)
    v1=shoot4([1,-k1_,k1_**2,-k1_**3],r_max,r_match,o2)
    ic2=[1,-k2_,k2_**2,-k2_**3] if k2_>1e-6 else [0,1,-k1_,k1_**2]
    v2=shoot4(ic2,r_max,r_match,o2)
    if any(x is None for x in [u1,u2,v1,v2]):
        print(f"  o2={o2:.4f}: INTEGRATION FAILED")
        continue
    M=np.vstack([u1,u2,v1,v2])
    norms=np.linalg.norm(M,axis=1,keepdims=True); norms[norms<1e-20]=1
    d=np.linalg.det(M/norms)
    print(f"  o2={o2:.5f}  det={d:+.4e}  k1={k1_:.4f} k2={k2_:.5f}")
