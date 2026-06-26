"""Collapse-proof relaxation: gradient flow on shape (F,chi) with the soliton
SIZE controlled by the Derrick virial. Size is pinned to R_target each batch
(resample), and R_target adapts so the virial V=E2-E4+3*Epot -> 0. This finds
the physical (metastable) dressed soliton without collapse."""
import numpy as np, ccef_s3_dressed as S, ccef_s3_relax2 as R2

def relax(msig,op='induced',c4=0.15,B2=0.025,Nr=800,rmax=10.0,steps=24000,
          frozen=False,mu=150.0,seed=1.6,lr=6e-4,lrc=4e-4,Rt0=0.6,etaR=4e-4,K=120):
    r,dr,w=S.make_grid(Nr,rmax)
    F=np.pi*np.exp(-(r/seed)**1.2);F[0]=np.pi;F[-1]=0.0
    chi=np.ones_like(r); Rt=Rt0
    mF=np.zeros_like(F);vF=np.zeros_like(F);mc=np.zeros_like(chi);vc=np.zeros_like(chi)
    b1,b2,eps=0.9,0.999,1e-8
    for t in range(1,steps+1):
        gF,gch=S.grad(F,chi,r,dr,w,op,c4,B2,msig,mu)
        if frozen: gch[:]=0.0
        mF=b1*mF+(1-b1)*gF;vF=b2*vF+(1-b2)*gF*gF
        mc=b1*mc+(1-b1)*gch;vc=b2*vc+(1-b2)*gch*gch
        F-=lr*(mF/(1-b1**t))/(np.sqrt(vF/(1-b2**t))+eps)
        chi-=lrc*(mc/(1-b1**t))/(np.sqrt(vc/(1-b2**t))+eps)
        F[0]=np.pi;F[-1]=0.0;chi[-1]=1.0;chi=np.clip(chi,0.0,1.5);F=np.clip(F,0.0,np.pi)
        if t%K==0:
            ek,e4,eb4,ev,*_=S.energy_density(F,chi,r,dr,op,c4,B2,msig)
            E2=np.sum(w*ek);E4=np.sum(w*e4);Ep=np.sum(w*(eb4+ev));E=E2+E4+Ep
            Rc,_=S.baryon_R(F,chi,r,dr,w)
            V=(E2-E4+3*Ep)/E                      # normalised virial
            Rt=float(np.clip(Rt-etaR*V*100.0,0.25,1.4))  # shrink if V>0, grow if V<0
            lam=np.clip(Rt/max(Rc,1e-3),0.85,1.18)
            if abs(lam-1)>1e-3:
                F,chi=R2.resample(F,chi,r,lam);mF*=0;vF*=0;mc*=0;vc*=0
    ek,e4,eb4,ev,*_=S.energy_density(F,chi,r,dr,op,c4,B2,msig)
    E=float(np.sum(w*(ek+e4+eb4+ev)));R,Bch=S.baryon_R(F,chi,r,dr,w);imin=np.argmin(chi)
    E2=float(np.sum(w*ek));E4=float(np.sum(w*e4));Ep=float(np.sum(w*(eb4+ev)))
    return dict(msig=round(msig,3),E=round(E,2),R=round(R,3),ER=round(E*R,2),
                chi_min=round(float(chi.min()),3),r_chimin=round(float(r[imin]),2),
                degree=round(float(Bch),3),vir=round((E2-E4+3*Ep)/E,3)),F,chi,r

if __name__=="__main__":
    import sys; op=sys.argv[1] if len(sys.argv)>1 else 'skyrme'
    print("FROZEN %s:"%op, relax(1.5,op=op,frozen=True,steps=20000)[0])
    for ms in [3.0,1.5,0.8]:
        print("dyn %s m_sig=%.2f:"%(op,ms), relax(ms,op=op,frozen=False,steps=20000)[0])
