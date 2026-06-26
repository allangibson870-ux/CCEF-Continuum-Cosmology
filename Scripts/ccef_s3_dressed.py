"""
ccef_s3_dressed.py -- Dressed S^3 baryon, hedgehog phi=chi(r)(cosF, sinF r_hat).
Dynamical amplitude chi(r) + radial potential V=(m_sigma^2/8)(chi^2-1)^2.
2-deriv invariant  S    = F'^2 + 2 sin^2F/r^2
4-deriv invariants S^2,  TrT2 = F'^4 + 2 sin^4F/r^4
4-derivative term (operator choice):
  'skyrme' (pure proxy)   : c4 * (1/2)(S^2 - TrT2) = c4 (s^2/r^2)(2F'^2 + s^2/r^2)
  'induced' (heat-kernel) : B2 * [ (2/3)S^2 + (1/3)TrT2 ]   (CC694B 2:1 mix)
Topology held at degree 1 by a soft baryon-charge penalty mu*(B-1)^2 (=>0 at min).
Analytic gradient (verified). R = baryon-charge rms radius.
"""
import numpy as np
B1, B4 = 1.0, 3.5553
LAM = np.sqrt(B4/B1)            # 1.886

def make_grid(Nr=700, rmax=9.0):
    r=(np.arange(Nr)+0.5)*(rmax/Nr); dr=rmax/Nr; w=4*np.pi*r**2*dr
    return r,dr,w

def _derivs(F,chi,dr):
    Fp=np.empty_like(F); chp=np.empty_like(chi)
    Fp[1:-1]=(F[2:]-F[:-2])/(2*dr); chp[1:-1]=(chi[2:]-chi[:-2])/(2*dr)
    Fp[0]=(F[1]-np.pi)/(2*dr); Fp[-1]=(0.0-F[-2])/(2*dr)
    chp[0]=(chi[1]-chi[0])/dr;  chp[-1]=(1.0-chi[-2])/(2*dr)
    return Fp,chp

def K4_and_partials(Fp,s,r,op,c4,B2):
    u=s*s/r**2; dudF=2*s*np.cos(np.arcsin(np.clip(s,-1,1)))  # placeholder, replaced below
    # use explicit cosF passed separately instead; (s,c) handled in caller
    return None

def energy_density(F,chi,r,dr,op,c4,B2,msig):
    s=np.sin(F); c=np.cos(F); Fp,chp=_derivs(F,chi,dr); u=s*s/r**2
    e_k=0.5*B1*(chp**2+chi**2*(Fp**2+2*u))
    if op=='skyrme':
        K4=c4*u*(2*Fp**2+u)
    else:  # induced 2:1 mix
        S=Fp**2+2*u; TrT2=Fp**4+2*u**2
        K4=B2*((2.0/3.0)*S**2+(1.0/3.0)*TrT2)
    e4=chi**4*K4
    e_b4=0.5*B4*chi**2*s**2
    e_v=(msig**2/8.0)*(chi**2-1)**2
    return e_k,e4,e_b4,e_v,Fp,chp,s,c,u

def baryon_charge(F,dr):
    s=np.sin(F)
    return -(1.0/np.pi)*np.sum(s[1:-1]**2*(F[2:]-F[:-2]))  # = integral baryon density

def total_energy(F,chi,r,dr,w,op,c4,B2,msig,mu):
    ek,e4,eb4,ev,*_=energy_density(F,chi,r,dr,op,c4,B2,msig)
    E=float(np.sum(w*(ek+e4+eb4+ev)))
    B=baryon_charge(F,dr)
    return E+mu*(B-1)**2

def grad(F,chi,r,dr,w,op,c4,B2,msig,mu):
    ek,e4,eb4,ev,Fp,chp,s,c,u=energy_density(F,chi,r,dr,op,c4,B2,msig)
    if op=='skyrme':
        K4=c4*u*(2*Fp**2+u); dK4dFp=c4*u*4*Fp
        dK4du=c4*(2*Fp**2+2*u)
    else:
        S=Fp**2+2*u; TrT2=Fp**4+2*u**2
        K4=B2*((2.0/3.0)*S**2+(1.0/3.0)*TrT2)
        dK4dFp=B2*(4*Fp**3+(16.0/3.0)*Fp*u)
        dK4du=B2*((8.0/3.0)*Fp**2+(20.0/3.0)*u)
    dudF=2*s*c/r**2
    dEdFp=B1*chi**2*Fp+chi**4*dK4dFp
    dEdchp=B1*chp
    P=w*dEdFp; Q=w*dEdchp
    deF=(B1*chi**2*dudF + chi**4*dK4du*dudF + B4*chi**2*s*c)
    dech=(B1*chi*(Fp**2+2*u) + 4*chi**3*K4 + B4*chi*s**2 + 0.5*msig**2*chi*(chi**2-1))
    gF=w*deF; gch=w*dech
    gF[1:-1]+=(P[:-2]-P[2:])/(2*dr)
    gch[1:-1]+=(Q[:-2]-Q[2:])/(2*dr)
    # baryon-charge penalty gradient (F only)
    B=baryon_charge(F,dr)
    dB=np.zeros_like(F)
    dB[1:-1]=-(1.0/np.pi)*(2*s[1:-1]*c[1:-1]*(F[2:]-F[:-2]) + s[:-2]**2 - s[2:]**2)
    gF+=2*mu*(B-1)*dB
    gF[0]=gF[-1]=0.0; gch[-1]=0.0
    return gF,gch

def baryon_R(F,chi,r,dr,w):
    Fp,_=_derivs(F,chi,dr)
    b=-(1/(2*np.pi**2))*(np.sin(F)**2/r**2)*Fp
    B=np.sum(w*b); r2=np.sum(w*r**2*b)/B
    return np.sqrt(abs(r2)),B

def relax(msig,op='induced',c4=0.15,B2=0.025,Nr=700,rmax=9.0,steps=15000,
          frozen=False,mu=120.0,seed=1.6,lr=6e-4):
    r,dr,w=make_grid(Nr,rmax)
    F=np.pi*np.exp(-(r/seed)**1.2); F[0]=np.pi; F[-1]=0.0
    chi=np.ones_like(r)
    mF=np.zeros_like(F);vF=np.zeros_like(F);mc=np.zeros_like(chi);vc=np.zeros_like(chi)
    b1,b2,eps=0.9,0.999,1e-8
    for t in range(1,steps+1):
        gF,gch=grad(F,chi,r,dr,w,op,c4,B2,msig,mu)
        if frozen: gch[:]=0.0
        mF=b1*mF+(1-b1)*gF; vF=b2*vF+(1-b2)*gF*gF
        mc=b1*mc+(1-b1)*gch; vc=b2*vc+(1-b2)*gch*gch
        F-=lr*(mF/(1-b1**t))/(np.sqrt(vF/(1-b2**t))+eps)
        chi-=lr*(mc/(1-b1**t))/(np.sqrt(vc/(1-b2**t))+eps)
        F[0]=np.pi;F[-1]=0.0;chi[-1]=1.0
        chi=np.clip(chi,0.0,2.0); F=np.clip(F,0.0,np.pi)
    ek,e4,eb4,ev,*_=energy_density(F,chi,r,dr,op,c4,B2,msig)
    E=float(np.sum(w*(ek+e4+eb4+ev)))
    R,Bch=baryon_R(F,chi,r,dr,w); imin=np.argmin(chi)
    return dict(msig=msig,op=op,E=E,R=R,ER=E*R,chi_min=float(chi.min()),
                r_chimin=float(r[imin]),degree=float(Bch),
                E2=float(np.sum(w*ek)),E4=float(np.sum(w*e4)),
                Eb4=float(np.sum(w*eb4)),Ev=float(np.sum(w*ev))),F,chi,r

if __name__=="__main__":
    # gradient verification including penalty + induced operator
    r,dr,w=make_grid(120,9.0); rng=np.random.default_rng(1)
    F=np.pi*np.exp(-(r/1.2))+0.04*rng.standard_normal(len(r));F[0]=np.pi;F[-1]=0
    chi=1-0.5*np.exp(-(r/0.6)**2)+0.02*rng.standard_normal(len(r));chi[-1]=1
    for op in ('skyrme','induced'):
        gF,gch=grad(F,chi,r,dr,w,op,0.15,0.025,1.5,120.0)
        h=1e-6;ngF=np.zeros_like(F);ngch=np.zeros_like(chi)
        for j in range(1,len(r)-1):
            Fp1=F.copy();Fp1[j]+=h;Fm=F.copy();Fm[j]-=h
            ngF[j]=(total_energy(Fp1,chi,r,dr,w,op,0.15,0.025,1.5,120.0)-
                    total_energy(Fm,chi,r,dr,w,op,0.15,0.025,1.5,120.0))/(2*h)
            cp=chi.copy();cp[j]+=h;cm=chi.copy();cm[j]-=h
            ngch[j]=(total_energy(F,cp,r,dr,w,op,0.15,0.025,1.5,120.0)-
                     total_energy(F,cm,r,dr,w,op,0.15,0.025,1.5,120.0))/(2*h)
        eF=np.max(np.abs(gF[1:-1]-ngF[1:-1]))/(np.max(np.abs(ngF[1:-1]))+1e-12)
        ec=np.max(np.abs(gch[1:-1]-ngch[1:-1]))/(np.max(np.abs(ngch[1:-1]))+1e-12)
        print("op=%-7s grad rel-err  F:%.2e  chi:%.2e"%(op,eF,ec))
