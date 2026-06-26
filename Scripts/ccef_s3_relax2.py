"""Derrick-rescaled relaxation of the dressed S^3 hedgehog (prevents collapse).
E(lambda)=E2*lam + E4/lam + Epot*lam^3 ; resample to virial-optimal lam each batch.
"""
import numpy as np, ccef_s3_dressed as S

def derrick_lambda(E2,E4,Epot):
    a,b,d=E2,E4,max(Epot,1e-12)
    lam2=(-a+np.sqrt(a*a+12*b*d))/(6*d)
    return float(np.sqrt(max(lam2,1e-6)))

def resample(F,chi,r,lam):
    # new profile of size lam*current: field_new(r)=field_old(r/lam)
    rq=r/lam
    Fn=np.interp(rq,r,F,left=np.pi,right=0.0)
    cn=np.interp(rq,r,chi,left=chi[0],right=1.0)
    Fn[0]=np.pi; Fn[-1]=0.0; cn[-1]=1.0
    return Fn,cn

def relax(msig,op='induced',c4=0.15,B2=0.025,Nr=700,rmax=9.0,
          steps=20000,frozen=False,mu=200.0,seed=1.6,lr=6e-4,resample_every=150):
    r,dr,w=S.make_grid(Nr,rmax)
    F=np.pi*np.exp(-(r/seed)**1.2); F[0]=np.pi; F[-1]=0.0
    chi=np.ones_like(r)
    mF=np.zeros_like(F);vF=np.zeros_like(F);mc=np.zeros_like(chi);vc=np.zeros_like(chi)
    b1,b2,eps=0.9,0.999,1e-8
    for t in range(1,steps+1):
        gF,gch=S.grad(F,chi,r,dr,w,op,c4,B2,msig,mu)
        if frozen: gch[:]=0.0
        mF=b1*mF+(1-b1)*gF; vF=b2*vF+(1-b2)*gF*gF
        mc=b1*mc+(1-b1)*gch; vc=b2*vc+(1-b2)*gch*gch
        F-=lr*(mF/(1-b1**t))/(np.sqrt(vF/(1-b2**t))+eps)
        chi-=lr*(mc/(1-b1**t))/(np.sqrt(vc/(1-b2**t))+eps)
        F[0]=np.pi;F[-1]=0.0;chi[-1]=1.0
        chi=np.clip(chi,0.0,2.0);F=np.clip(F,0.0,np.pi)
        if t%resample_every==0:
            ek,e4,eb4,ev,*_=S.energy_density(F,chi,r,dr,op,c4,B2,msig)
            E2=np.sum(w*ek);E4=np.sum(w*e4);Ep=np.sum(w*(eb4+ev))
            lam=derrick_lambda(E2,E4,Ep)
            lam=np.clip(lam,0.8,1.25)            # gentle rescaling
            if abs(lam-1)>1e-3:
                F,chi=resample(F,chi,r,lam)
                mF*=0;vF*=0;mc*=0;vc*=0
    ek,e4,eb4,ev,*_=S.energy_density(F,chi,r,dr,op,c4,B2,msig)
    E=float(np.sum(w*(ek+e4+eb4+ev)))
    R,Bch=S.baryon_R(F,chi,r,dr,w); imin=np.argmin(chi)
    E2=float(np.sum(w*ek));E4=float(np.sum(w*e4));Ep=float(np.sum(w*(eb4+ev)))
    vir=(E2-E4+3*Ep)/E
    return dict(msig=round(msig,3),E=round(E,2),R=round(R,3),ER=round(E*R,2),
                chi_min=round(float(chi.min()),3),r_chimin=round(float(r[imin]),2),
                degree=round(float(Bch),3),vir=round(vir,3)),F,chi,r

if __name__=="__main__":
    import sys
    op=sys.argv[1] if len(sys.argv)>1 else 'skyrme'
    print("FROZEN %s:"%op, relax(1.5,op=op,frozen=True,steps=18000)[0])
    for ms in [3.0,1.5,0.8]:
        print("dyn %s m_sig=%.2f:"%(op,ms), relax(ms,op=op,frozen=False,steps=18000)[0])
