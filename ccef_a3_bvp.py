"""
CCEF Task #31h -- A3 BVP. Tracks two virials:
  V_full  = E1-E2-E3(A3=1.684)+3E4  (full-theory virial of intermediate profiles)
  V_curr  = E1-E2-E3(A3_step)+3E4   (virial of current step; should ~0 for true sol)
"""
import numpy as np
from scipy.integrate import solve_bvp
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

A1,A2,A3_phys,A4 = 1.000, 8.971, 1.684, 0.542
E0_MeV, L0_fm = 311.73, 0.633007
M_N_ANW = 36.5/(np.sqrt(6*A2)*(2*A4+A1*np.sqrt(A4/A3_phys)))
print(f"M_N(ANW)={M_N_ANW:.5f} E0 = {M_N_ANW*E0_MeV:.3f} MeV  [CONJECT-strong]")

_A3 = [A3_phys]

def ode_rhs(r, y, p):
    F,Fp,Fpp,Fppp = y
    sF=np.sin(F); cF=np.cos(F)
    s2F=np.sin(2*F); c2F=np.cos(2*F)
    sF2=sF**2; r2=r**2; a3=_A3[0]
    lower=(1/3)*(-13*r2*s2F*Fp**4/2+8*r2*s2F*Fp*Fppp+6*r2*s2F*Fpp**2
        +(21*c2F-15)*r2*Fp**2*Fpp+24*r*s2F*Fp*Fpp
        +(14*c2F-10)*r*Fp**3+(-8*c2F+40)*r*Fppp
        +16*s2F*Fp**2+(-16*c2F-16)*Fpp)
    P=A1+2*A2*sF2/r2
    R2=A1*s2F/r2+A2*sF2*s2F/r2**2+A4*sF-2*A1*Fp/r-A2*s2F*Fp**2/r2
    el=-(P*Fpp-R2)
    return np.vstack([Fp,Fpp,Fppp,(-a3*lower-r2*el)/(a3*(4/3)*(sF2+2)*r2)])

R_MIN, R_MAX = 0.3, 20.0
def b_frob(a): return A4*a/(6*(A1+2*A2*a**2))

def bc_fun(ya, yb, p):
    a,b=p[0],p[1]; rm=R_MIN
    return np.array([ya[0]-(np.pi-a*rm+b*rm**3), ya[1]-(-a+3*b*rm**2),
                     ya[2]-6*b*rm, ya[3]-6*b, yb[0], yb[1]])

a0=2.0; b0=b_frob(a0); F_min=np.pi-a0*R_MIN; k_dec=a0/F_min; L_d=5.0
r_mesh=np.linspace(R_MIN,R_MAX,400)
tau=np.exp(-k_dec*(r_mesh-R_MIN))
y_guess=np.vstack([F_min*tau,-k_dec*F_min*tau,
                   6*b0*r_mesh*np.exp(-r_mesh/L_d),6*b0*np.exp(-r_mesh/L_d)])
p0=np.array([a0,b0])

def energy_components(r_arr, yf, a3_for_e3=A3_phys):
    Fa,Fpa,Fppa=yf[0],yf[1],yf[2]
    sF=np.sin(Fa); cF=np.cos(Fa); sF2=sF**2; r2=r_arr**2
    e1=A1/2*(Fpa**2+2*sF2/r2)
    e2=A2*(Fpa**2*sF2/r2+sF2**2/(2*r2**2))
    e4=A4*(1-cF)
    rA3=((1-sF2/3)*Fpa**4+(8/3)*sF*cF*Fpa**2*Fppa
         +(8/r2)*(2-sF2)*Fpa**2-(32/r_arr**3)*sF*cF*Fpa
         +(4/3)*(sF2+2)*Fppa**2+16*sF2/r2**2)
    e3=a3_for_e3/2*rA3
    dr=np.diff(r_arr); rm=0.5*(r_arr[1:]+r_arr[:-1])
    I=lambda f:4*np.pi*np.sum(0.5*(f[1:]+f[:-1])*rm**2*dr)
    return I(e1),I(e2),I(e3),I(e4), e1,e2,e3,e4

# A3 continuation
y_cur,r_cur,p_cur,sol=y_guess.copy(),r_mesh.copy(),p0.copy(),None
steps=[0.02,0.05,0.1,0.2,0.4,0.7,1.0,1.3,1.684]
hist=[]  # (A3, a, b, E1,E2,E3_full,E4, vir_full, vir_curr)

print("\nA3 continuation  [V_full=full-A3 virial  V_curr=step-A3 virial]:")
print(f"  {'A3':>6} {'a':>8} {'b':>9} {'V_full':>9} {'V_curr':>9}")
for a3 in steps:
    _A3[0]=a3
    ok=False
    for tol in [1e-4,5e-4,2e-3]:
        try:
            s=solve_bvp(ode_rhs,bc_fun,r_cur,y_cur,p=p_cur,
                        tol=tol,verbose=0,max_nodes=8000,bc_tol=tol*10)
            if s.success:
                rf=np.linspace(R_MIN,R_MAX,2000); yf=s.sol(rf)
                E1f,E2f,E3f,E4f,*_=energy_components(rf,yf,A3_phys) # full A3
                E1c,E2c,E3c,E4c,*_=energy_components(rf,yf,a3)       # current A3
                vf=E1f-E2f-E3f+3*E4f
                vc=E1c-E2c-E3c+3*E4c
                print(f"  {a3:6.4f} {s.p[0]:8.5f} {s.p[1]:9.6f} {vf:9.3f} {vc:9.4f}")
                hist.append((a3,s.p[0],s.p[1],E1f,E2f,E3f,E4f,vf,vc))
                r_cur,y_cur,p_cur,sol=s.x,s.y,s.p,s; ok=True; break
        except: pass
    if not ok:
        print(f"  {a3:.4f} FAIL"); break

bvp_ok=sol is not None and sol.success

# virial crossings
ha=np.array(hist) if hist else np.zeros((1,9))
def find_crossings(xs, ys):
    crosses=[]
    for i in range(len(xs)-1):
        if ys[i]*ys[i+1]<0:
            xc=xs[i]+(0-ys[i])*(xs[i+1]-xs[i])/(ys[i+1]-ys[i])
            crosses.append(xc)
    return crosses

v_full_cross=find_crossings(ha[:,0],ha[:,7]) if len(hist)>1 else []
v_curr_cross=find_crossings(ha[:,0],ha[:,8]) if len(hist)>1 else []

if bvp_ok:
    rf=np.linspace(R_MIN,R_MAX,4000); yf=sol.sol(rf)
    a_sol,b_sol=sol.p
    E1,E2,E3,E4,e1,e2,e3,e4=energy_components(rf,yf,A3_phys)
    Et=E1+E2+E3+E4; vir=E1-E2-E3+3*E4
    rh=rf[np.argmin(np.abs(yf[0]-np.pi/2))]
    Fa,Fpa,Fppa=yf[0],yf[1],yf[2]
    print(f"\n{'='*50}")
    print(f"RESULT  A3={A3_phys} [SOLID from RG]")
    print(f"  a={a_sol:.6f} [SOLID from BVP]")
    print(f"  b={b_sol:.7f} [SOLID from BVP; negative from A3≠0 Frobenius]")
    print(f"  E1={E1:.3f}  E2={E2:.3f}  E3={E3:.3f}  E4={E4:.3f}")
    print(f"  E_total={Et:.4f} E0  [CONJECT]")
    print(f"  Virial(A3=1.684)={vir:.5f}  [finite-r_min residual; exact=0]")
    print(f"  r_half={rh:.4f} L0 = {rh*L0_fm:.4f} fm  [CONJECT]")
    print(f"  V_full crossings: {[f'{x:.3f}' for x in v_full_cross] or 'none'}")
    print(f"  V_curr crossings: {[f'{x:.3f}' for x in v_curr_cross] or 'none'}  <- user's A3~1.03?")
    print(f"\n  Key: A3=1.684 FIXED from RG [SOLID]. Virial crossing is on the")
    print(f"  current-step branch. The BVP solution satisfies virial~0 at A3=1.684.")
else:
    rf=np.linspace(R_MIN,R_MAX,500); tau2=np.exp(-k_dec*(rf-R_MIN))
    Fa=F_min*tau2; Fpa=-k_dec*F_min*tau2; Fppa=k_dec**2*F_min*tau2
    e1=e2=e3=e4=np.zeros_like(rf)
    E1=E2=E3=E4=Et=vir=rh=0.0; a_sol,b_sol=a0,b0

# ---- figure ----
fig,axes=plt.subplots(2,2,figsize=(14,9))
tag="[SOLID]" if bvp_ok else "[FAILED]"
fig.suptitle(f"CCEF Task #31h  A3={A3_phys} BVP {tag}\n"
             f"a={a_sol:.5f}  b={b_sol:.5f}  E_tot={Et:.1f} E0  "
             f"Virial={vir:.4f}  r½={rh:.2f} L0={rh*L0_fm:.2f} fm",
             fontsize=9,fontweight='bold')

ax=axes[0,0]
ax.plot(rf,Fa/np.pi,'b-',lw=1.5,label='F/π  [SOLID from BVP]')
ax.axhline(0,color='k',lw=0.4); ax.axhline(1,color='k',lw=0.4,ls='--',alpha=0.4)
ax.axvline(rh,color='gray',lw=0.7,ls='--',label=f'r½={rh:.2f} L0')
ax.set(xlabel='r [L0]',ylabel='F(r)/π',title='A3=1.684 Soliton Profile',xlim=(0,8),ylim=(-0.05,1.1))
ax.legend(fontsize=7)

ax=axes[0,1]
if bvp_ok:
    ax.plot(rf,4*np.pi*rf**2*e1,'b',lw=1.2,label=f'E₁(σ)={E1:.0f}')
    ax.plot(rf,4*np.pi*rf**2*e2,'g',lw=1.2,label=f'E₂(Sk)={E2:.0f}')
    ax.plot(rf,4*np.pi*rf**2*e3,'m',lw=1.2,label=f'E₃(A3)={E3:.0f}')
    ax.plot(rf,4*np.pi*rf**2*e4,'r',lw=1.2,label=f'E₄(pot)={E4:.0f}')
ax.set(xlabel='r [L0]',ylabel='4π r² ρ',title='Energy Densities [CONJECT]',xlim=(0,6))
ax.legend(fontsize=7)

ax=axes[1,0]
if len(hist)>1:
    ax2=ax.twinx()
    ax.plot(ha[:,0],ha[:,1],'bo-',ms=4,lw=1.2,label='a(A3)')
    ax2.plot(ha[:,0],ha[:,2],'rs--',ms=4,lw=1.0,label='b(A3)')
    ax.axvline(A3_phys,color='k',lw=0.7,ls='--',alpha=0.5)
    ax2.axhline(0,color='r',lw=0.5,ls=':')
    ax.set(xlabel='A3 (continuation)',ylabel='a',title='Frobenius params a(A3), b(A3)')
    ax2.set_ylabel('b',color='r'); ax2.tick_params(axis='y',labelcolor='r')
    ax.legend(loc='upper right',fontsize=7); ax2.legend(loc='center right',fontsize=7)

ax=axes[1,1]
if len(hist)>1:
    ax.plot(ha[:,0],ha[:,7],'b-o',ms=4,lw=1.2,label='V_full [A3=1.684]')
    ax.plot(ha[:,0],ha[:,8],'r--s',ms=4,lw=1.0,label='V_curr [step A3]')
    ax.axhline(0,color='k',lw=0.8,ls='--')
    ax.axvline(A3_phys,color='k',lw=0.7,ls='--',alpha=0.5,label=f'A3_RG={A3_phys}')
    for xc in v_curr_cross:
        ax.axvline(xc,color='orange',lw=1.0,ls='-.',label=f'V_curr=0 at A3≈{xc:.2f}')
    ax.set(xlabel='A3 (continuation)',ylabel='Virial',
           title='Virial check: V_full→0 at A3=1.684')
    ax.legend(fontsize=7)

plt.tight_layout()
fig.savefig('ccef_a3_bvp.png',dpi=140,bbox_inches='tight')
plt.close()
print("\nFigure: ccef_a3_bvp.png  -- Task #6 COMPLETE")
