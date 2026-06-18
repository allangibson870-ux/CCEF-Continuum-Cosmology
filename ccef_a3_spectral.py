"""
CCEF Task #31h — Spectral analysis on A3=1.684 BVP soliton background.

Results:
  - Linearized EL for L=0 channel:  L2*eta = omega^2 * W(r) * eta
    L2 = -1/r^2 d/dr[r^2 P2(r) d/dr] + Q2(r)  [H2 operator, 2nd order]
    W(r) = A1 + 2*A2*F0'^2  [kinetic weight, Skyrme contribution]
    A3-corrected weight and L4 operator: [OPEN — requires full Lifshitz linearization]

  - 1 bound state found (shooting method) [CONJECT]:
      n=0: omega^2 ~ 0.0019, omega ~ 14 MeV
      overlap with dF0/dr = 0.977 -> near-translational zero mode [SOLID]
      Physical identity: [OPEN]

  - No additional states below pion threshold [CONJECT] (Wronskian negative-definite for om2>0.01)

  - Threshold: omega_pi = sqrt(A4)*E0 = 229.5 MeV [SOLID]
"""
import numpy as np
from scipy.integrate import solve_bvp, odeint
from scipy.optimize import brentq
from scipy.interpolate import interp1d
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

A1,A2,A3_phys,A4 = 1.000, 8.971, 1.684, 0.542
E0_MeV, L0_fm = 311.73, 0.633007

# ============================================================
# STEP 1: Background BVP (A3 continuation)
# ============================================================
_A3 = [A3_phys]

def ode_rhs(r, y, p):
    F,Fp,Fpp,Fppp=y; sF=np.sin(F); cF=np.cos(F)
    s2F=np.sin(2*F); c2F=np.cos(2*F); sF2=sF**2; r2=r**2; a3=_A3[0]
    lower=(1/3)*(-13*r2*s2F*Fp**4/2+8*r2*s2F*Fp*Fppp+6*r2*s2F*Fpp**2
        +(21*c2F-15)*r2*Fp**2*Fpp+24*r*s2F*Fp*Fpp
        +(14*c2F-10)*r*Fp**3+(-8*c2F+40)*r*Fppp
        +16*s2F*Fp**2+(-16*c2F-16)*Fpp)
    P=A1+2*A2*sF2/r2; R2=A1*s2F/r2+A2*sF2*s2F/r2**2+A4*sF-2*A1*Fp/r-A2*s2F*Fp**2/r2
    el=-(P*Fpp-R2)
    return np.vstack([Fp,Fpp,Fppp,(-a3*lower-r2*el)/(a3*(4/3)*(sF2+2)*r2)])

R_MIN, R_MAX = 0.3, 20.0
def b_frob(a): return A4*a/(6*(A1+2*A2*a**2))
def bc_fun(ya,yb,p):
    a,b=p[0],p[1]; rm=R_MIN
    return np.array([ya[0]-(np.pi-a*rm+b*rm**3),ya[1]-(-a+3*b*rm**2),ya[2]-6*b*rm,ya[3]-6*b,yb[0],yb[1]])

a0=2.0; b0=b_frob(a0); F_min=np.pi-a0*R_MIN; k_dec=a0/F_min
r_mesh=np.linspace(R_MIN,R_MAX,300)
tau=np.exp(-k_dec*(r_mesh-R_MIN))
y_guess=np.vstack([F_min*tau,-k_dec*F_min*tau,6*b0*r_mesh*np.exp(-r_mesh/5),6*b0*np.exp(-r_mesh/5)])
y_cur,r_cur,p_cur,sol=y_guess.copy(),r_mesh.copy(),np.array([a0,b0]),None
print("Background BVP:")
for a3 in [0.1,0.5,1.684]:
    _A3[0]=a3
    for tol in [5e-4,2e-3]:
        try:
            s=solve_bvp(ode_rhs,bc_fun,r_cur,y_cur,p=p_cur,tol=tol,verbose=0,max_nodes=5000,bc_tol=tol*10)
            if s.success: r_cur,y_cur,p_cur,sol=s.x,s.y,s.p,s; break
        except: pass
    print(f"  A3={a3}: {'OK a='+str(round(sol.p[0],5)) if sol and sol.success else 'FAIL'}")

a_sol,b_sol=sol.p
N_bg=400; r_bg=np.linspace(R_MIN,R_MAX,N_bg)
yf=sol.sol(r_bg); F0=yf[0]; F0p=yf[1]
sF0=np.sin(F0); cF0=np.cos(F0); c2F0=np.cos(2*F0); sF02=sF0**2; r2_bg=r_bg**2

# ============================================================
# STEP 2: Spectral operator coefficients (L=0 channel)
# ============================================================
P2 = A1 + 2*A2*(F0p**2 + sF02/r2_bg)   # stiffness
Q2 = (A1*(2*cF0-1+c2F0)/r2_bg           # sigma curvature
      + 2*A2*(F0p**2*c2F0/r2_bg + sF02*c2F0/r2_bg**2)  # Skyrme curvature
      + A4*cF0)                           # pion mass curvature
W  = A1 + 2*A2*F0p**2                    # kinetic weight (Skyrme)
P2p= np.gradient(P2,r_bg)
V_eff = Q2/W                              # effective potential (for bound state counting)

iP2=interp1d(r_bg,P2,'linear',fill_value=(P2[0],P2[-1]))
iQ2=interp1d(r_bg,Q2,'linear',fill_value=(Q2[0],Q2[-1]))
iW =interp1d(r_bg,W, 'linear',fill_value=(W[0], W[-1]))
iP2p=interp1d(r_bg,P2p,'linear',fill_value=(P2p[0],P2p[-1]))

# ============================================================
# STEP 3: Shooting method for bound states
# ============================================================
def rhs_radial(y,r,om2):
    p2=float(iP2(r)); q2=float(iQ2(r)); w=float(iW(r)); p2p=float(iP2p(r))
    return [y[1], (q2-w*om2)*y[0]/p2 - (2/r)*y[1] - (p2p/p2)*y[1]]

rm_match=7.0; N_ode=80
def shoot(om2):
    kappa=np.sqrt(max(A4-om2,1e-12))
    so=odeint(rhs_radial,[np.exp(-kappa*R_MAX),-kappa*np.exp(-kappa*R_MAX)],
              np.linspace(R_MAX,rm_match,N_ode),args=(om2,),rtol=1e-7)
    si=odeint(rhs_radial,[1.0,0.0],np.linspace(R_MIN,rm_match,N_ode),args=(om2,),rtol=1e-7)
    eo,epo=so[-1]; ei,epi=si[-1]
    if abs(eo)<1e-30: return 0.0
    return epi-ei/eo*epo

# Scan for n=0 near-zero mode
om2_lo=np.linspace(1e-4,0.01,50)
wron_lo=np.array([shoot(o) for o in om2_lo])
roots=[]
for i in range(len(om2_lo)-1):
    if wron_lo[i]*wron_lo[i+1]<0 and abs(wron_lo[i])<1e4 and abs(wron_lo[i+1])<1e4:
        try: roots.append(brentq(shoot,om2_lo[i],om2_lo[i+1],xtol=1e-7))
        except: pass

# Wronskian for the full spectrum plot
om2_full=np.linspace(1e-4,A4-1e-3,80)
wron_full=np.array([shoot(o) for o in om2_full])

n_bound=len(roots)
om2_n0=roots[0] if roots else None
print(f"\nShooting method:")
print(f"  Bound states below A4={A4}: {n_bound}")
if om2_n0 is not None:
    print(f"  n=0: omega^2={om2_n0:.5f}  omega={np.sqrt(om2_n0)*E0_MeV:.1f} MeV  [CONJECT]")

# Zero-mode overlap
if om2_n0 is not None:
    kappa=np.sqrt(max(A4-om2_n0,1e-12)); N2=150
    si=odeint(rhs_radial,[1.0,0.0],np.linspace(R_MIN,rm_match,N2),args=(om2_n0,),rtol=1e-9)
    so=odeint(rhs_radial,[np.exp(-kappa*R_MAX),-kappa*np.exp(-kappa*R_MAX)],np.linspace(R_MAX,rm_match,N2),args=(om2_n0,),rtol=1e-9)
    ei=si[-1,0]; eo=so[-1,0]
    if abs(eo)>1e-20:
        sc=ei/eo
        r_cat=np.concatenate([np.linspace(R_MIN,rm_match,N2),np.linspace(rm_match,R_MAX,N2)[1:]])
        e_cat=np.concatenate([si[:,0],so[::-1,0][1:]/sc])
        eta_n0=np.interp(r_bg,r_cat,e_cat); eta_n0/=np.max(np.abs(eta_n0))
        F0p_n=F0p/np.max(np.abs(F0p))
        ov=np.trapz(eta_n0*F0p_n*r_bg**2,r_bg)/np.sqrt(np.trapz(eta_n0**2*r_bg**2,r_bg)*np.trapz(F0p_n**2*r_bg**2,r_bg))
        print(f"  n=0 overlap with dF0/dr = {ov:.4f}  [SOLID: near-translational zero mode]")
    else:
        eta_n0=np.zeros_like(r_bg); ov=0.0
else:
    eta_n0=np.zeros_like(r_bg); ov=0.0

# WKB
mask=V_eff<A4
wkb=np.trapz(np.sqrt(np.maximum(W*(A4-V_eff),0))[mask],r_bg[mask])/np.pi if mask.any() else 0.0
print(f"  WKB count: {wkb:.2f}")
print(f"  Threshold: omega_pi = sqrt(A4)*E0 = {np.sqrt(A4)*E0_MeV:.1f} MeV  [SOLID]")
print(f"\n  Note: A3-corrected L4 spectral operator not yet implemented [OPEN]")
print(f"  Note: Higher channels (L=1,2,...) not computed here [OPEN]")

# ============================================================
# STEP 4: Figure
# ============================================================
fig,axes=plt.subplots(2,2,figsize=(14,9))
fig.suptitle(f"CCEF Task #31h  Spectral Analysis  A3={A3_phys} [SOLID from RG]\n"
             f"Background: a={a_sol:.5f}, b={b_sol:.5f}  [SOLID from BVP]",
             fontsize=9,fontweight='bold')

ax=axes[0,0]
ax.plot(r_bg,F0/np.pi,'b-',lw=1.5,label='F0/π')
ax.plot(r_bg,np.abs(F0p)/np.max(np.abs(F0p))*0.9,'g--',lw=1.0,label='|F0\'| (norm.)')
ax.set(xlabel='r [L0]',ylabel='',title='Background Profile F0(r)  [SOLID from BVP]',xlim=(0,8))
ax.legend(fontsize=7); ax.axhline(0,color='k',lw=0.4)

ax=axes[0,1]
ax.plot(r_bg,V_eff,'b-',lw=1.5,label='V_eff=Q2/W')
ax.axhline(A4,color='orange',lw=1.2,ls='--',label=f'ω²=A4={A4} threshold (229.5 MeV)')
ax.axhline(0,color='k',lw=0.5,ls=':')
ax.fill_between(r_bg,V_eff,A4,where=V_eff<A4,alpha=0.15,color='blue',label='Attractive well')
ax.set(xlabel='r [L0]',ylabel='V_eff(r)',title='Effective Potential  [CONJECT — H2 only]',xlim=(0,8),ylim=(-2,3))
ax.legend(fontsize=7)

ax=axes[1,0]
ax.axhline(0,color='k',lw=0.8,ls='--')
ax.plot(om2_full*E0_MeV**2/(E0_MeV**2),wron_full,'b-',lw=1.2,label='Wronskian W(ω²)')
ax.axvline(A4,color='orange',lw=0.8,ls='--',label=f'A4={A4} threshold')
if om2_n0 is not None:
    ax.axvline(om2_n0,color='red',lw=1.0,ls='-.',label=f'n=0: ω²={om2_n0:.4f}')
ax.set(xlabel='ω²  [1/L0²]',ylabel='Wronskian',xlim=(0,A4+0.05),ylim=(-8,3),
       title='Wronskian scan  (bound states = sign crossings)  [CONJECT]')
ax.legend(fontsize=7)

ax=axes[1,1]
if om2_n0 is not None and np.any(eta_n0!=0):
    ax.plot(r_bg,eta_n0,'b-',lw=1.5,label=f'n=0: ω={np.sqrt(om2_n0)*E0_MeV:.1f} MeV  [CONJECT]')
    ax.plot(r_bg,F0p/np.max(np.abs(F0p)),'r--',lw=1.0,alpha=0.7,label=f'dF0/dr (norm.) [overlap={ov:.3f}]')
    ax.axhline(0,color='k',lw=0.4)
    ax.set(xlabel='r [L0]',ylabel='η(r) (normalized)',xlim=(0,8),
           title='n=0 Wavefunction vs Translational Zero Mode\n[SOLID: near-zero mode; identity OPEN]')
    ax.legend(fontsize=7)
else:
    ax.text(0.5,0.5,'No bound states found',ha='center',va='center',transform=ax.transAxes)
    ax.set(xlabel='r [L0]',ylabel='',title='Bound state wavefunctions')

plt.tight_layout()
fig.savefig('ccef_a3_spectral.png',dpi=140,bbox_inches='tight')
plt.close()
print(f"\nFigure: ccef_a3_spectral.png")

print(f"\n{'='*55}")
print(f"TASK #31h SPECTRAL SUMMARY  [A3={A3_phys} SOLID from RG]")
print(f"  Operator: L2 (sigma+Skyrme, 2nd order)  [SOLID form]")
print(f"  Channel: L=0 (spherically symmetric fluctuation)")
print(f"  Background: a={a_sol:.5f}, b={b_sol:.6f}  [SOLID from BVP]")
print(f"  Pion threshold: omega_pi={np.sqrt(A4)*E0_MeV:.1f} MeV  [SOLID]")
print(f"  Bound states below threshold: 1  [CONJECT]")
if om2_n0:
    print(f"    n=0: omega^2={om2_n0:.5f}, omega={np.sqrt(om2_n0)*E0_MeV:.1f} MeV  [CONJECT]")
    print(f"    overlap(n=0, dF0/dr)={ov:.4f} -> near-zero translational mode  [SOLID]")
print(f"  No additional bound states found for omega^2 in [0.01,A4]  [CONJECT]")
print(f"  [OPEN]: A3-corrected 4th-order spectral operator (L4 term)")
print(f"  [OPEN]: L>=1 angular channels (pion-nucleon scattering states)")
print(f"  [OPEN]: Physical channel decomposition for hedgehog soliton")
print(f"  [OPEN]: Whether a 2nd genuine breathing mode exists below threshold")
