"""#4 FRG/heat-kernel B2(chi)  and  #5 UV re-pin scan.
Induced positive Skyrme term (CC694B a2) is built from d_phi -> scales chi^4,
times a log whose IR cutoff is the LOCAL gap. In the broken phase the gap ~ chi
(mass proportional to amplitude), so the log grows as chi->0:
   B2_eff(chi) = B2_0 * chi^4 * (L0 - ln chi)/L0    (FRG-motivated, non-power-law)
L0 = ln(k_UV/gap) ~ 5-6  (CC694B: log set by B3~1e-6).
Compare to bare powers chi^q. Analytic gradient (verified)."""
import numpy as np, ccef_s3_dressed as S, ccef_s3_relax2 as R2
B1,B4=S.B1,S.B4; LAM=S.LAM

def B2eff(chi,B2_0,mode,q,L0):
    if mode=='power': return B2_0*chi**q
    c=np.clip(chi,1e-4,None)
    return B2_0*c**4*(L0-np.log(c))/L0          # FRG form
def dB2eff(chi,B2_0,mode,q,L0):
    if mode=='power': return B2_0*q*chi**(q-1)
    c=np.clip(chi,1e-4,None)
    return B2_0*c**3/L0*(4*(L0-np.log(c))-1)

def en(F,chi,r,dr,B2_0,msig,mode,q,L0):
    s=np.sin(F);c=np.cos(F);Fp,chp=S._derivs(F,chi,dr);u=s*s/r**2
    ek=0.5*B1*(chp**2+chi**2*(Fp**2+2*u))
    Sinv=Fp**2+2*u;TrT2=Fp**4+2*u**2;K4=(2/3)*Sinv**2+(1/3)*TrT2   # induced 2:1 shape
    Be=B2eff(chi,B2_0,mode,q,L0); e4=Be*K4
    e_an=0.5*B4*chi**2*s**2; e_v=(msig**2/8.0)*(chi**2-1)**2
    return ek,e4,e_an,e_v,Fp,chp,s,c,u,K4,Be
def energy(F,chi,r,dr,w,B2_0,msig,mode,q,L0,mu):
    ek,e4,e_an,e_v,*_=en(F,chi,r,dr,B2_0,msig,mode,q,L0)
    return float(np.sum(w*(ek+e4+e_an+e_v)))+mu*(S.baryon_charge(F,dr)-1)**2
def grad(F,chi,r,dr,w,B2_0,msig,mode,q,L0,mu):
    ek,e4,e_an,e_v,Fp,chp,s,c,u,K4,Be=en(F,chi,r,dr,B2_0,msig,mode,q,L0)
    dK4dFp=(2/3)*2*(Fp**2+2*u)*2*Fp+(1/3)*4*Fp**3
    dK4du =(2/3)*2*(Fp**2+2*u)*2+(1/3)*4*u
    dudF=2*s*c/r**2
    dEdFp=B1*chi**2*Fp+Be*dK4dFp; dEdchp=B1*chp
    P=w*dEdFp;Q=w*dEdchp
    deF=B1*chi**2*dudF+Be*dK4du*dudF+B4*chi**2*s*c
    dBe=dB2eff(chi,B2_0,mode,q,L0)
    dech=(B1*chi*(Fp**2+2*u)+dBe*K4+B4*chi*s**2+0.5*msig**2*chi*(chi**2-1))
    gF=w*deF;gch=w*dech
    gF[1:-1]+=(P[:-2]-P[2:])/(2*dr); gch[1:-1]+=(Q[:-2]-Q[2:])/(2*dr)
    B=S.baryon_charge(F,dr);dB=np.zeros_like(F)
    dB[1:-1]=-(1/np.pi)*(2*s[1:-1]*c[1:-1]*(F[2:]-F[:-2])+s[:-2]**2-s[2:]**2)
    gF+=2*mu*(B-1)*dB; gF[0]=gF[-1]=0;gch[-1]=0
    return gF,gch
def ermsR(F,chi,r,dr,w,B2_0,msig,mode,q,L0):
    ek,e4,e_an,e_v,*_=en(F,chi,r,dr,B2_0,msig,mode,q,L0);e=ek+e4+e_an+e_v
    return np.sqrt(np.sum(w*r**2*e)/np.sum(w*e))
def relax(B2_0,msig,mode='frg',q=4.0,L0=5.5,Nr=700,rmax=11.0,steps=16000,frozen=False,
          mu=300.0,seed=1.6,lr=6e-4,lrc=3e-4,Rt0=0.5,etaR=3e-4,K=120):
    r,dr,w=S.make_grid(Nr,rmax)
    F=np.pi*np.exp(-(r/seed)**1.2);F[0]=np.pi;F[-1]=0;chi=np.ones_like(r);Rt=Rt0
    mF=np.zeros_like(F);vF=np.zeros_like(F);mc=np.zeros_like(chi);vc=np.zeros_like(chi)
    b1,b2,eps=0.9,0.999,1e-8
    for t in range(1,steps+1):
        gF,gch=grad(F,chi,r,dr,w,B2_0,msig,mode,q,L0,mu)
        if frozen: gch[:]=0
        mF=b1*mF+(1-b1)*gF;vF=b2*vF+(1-b2)*gF*gF;mc=b1*mc+(1-b1)*gch;vc=b2*vc+(1-b2)*gch*gch
        F-=lr*(mF/(1-b1**t))/(np.sqrt(vF/(1-b2**t))+eps)
        chi-=lrc*(mc/(1-b1**t))/(np.sqrt(vc/(1-b2**t))+eps)
        F[0]=np.pi;F[-1]=0;chi[-1]=1;chi=np.clip(chi,1e-3,1.5);F=np.clip(F,0,np.pi)
        if t%K==0:
            ek,e4,e_an,e_v,*_=en(F,chi,r,dr,B2_0,msig,mode,q,L0)
            E2=np.sum(w*ek);E4=np.sum(w*e4);Ep=np.sum(w*(e_an+e_v));E=E2+E4+Ep
            Rc,_=S.baryon_R(F,chi,r,dr,w);V=(E2-E4+3*Ep)/E
            Rt=float(np.clip(Rt-etaR*V*100,0.25,1.4));lam=np.clip(Rt/max(Rc,1e-3),0.88,1.14)
            if abs(lam-1)>1e-3:F,chi=R2.resample(F,chi,r,lam);mF*=0;vF*=0;mc*=0;vc*=0
    ek,e4,e_an,e_v,*_=en(F,chi,r,dr,B2_0,msig,mode,q,L0)
    E=float(np.sum(w*(ek+e4+e_an+e_v)));Re=ermsR(F,chi,r,dr,w,B2_0,msig,mode,q,L0)
    _,B=S.baryon_R(F,chi,r,dr,w);E2=np.sum(w*ek);E4=np.sum(w*e4);Ep=np.sum(w*(e_an+e_v))
    return dict(E=round(E,2),R=round(float(Re),3),ER=round(E*Re,2),
                chi_min=round(float(chi.min()),3),degree=round(float(B),3),
                vir=round((E2-E4+3*Ep)/E,3))
if __name__=="__main__":
    r,dr,w=S.make_grid(120,11.0);rng=np.random.default_rng(4)
    F=np.pi*np.exp(-(r/1.2))+0.04*rng.standard_normal(len(r));F[0]=np.pi;F[-1]=0
    chi=1-0.6*np.exp(-(r/0.6)**2)+0.02*rng.standard_normal(len(r));chi[-1]=1
    A=(0.025,1.0,'frg',4.0,5.5,300.0)
    gF,gch=grad(F,chi,r,dr,w,*A);h=1e-6;ngF=np.zeros_like(F);ngc=np.zeros_like(chi)
    for j in range(1,len(r)-1):
        a=F.copy();a[j]+=h;b=F.copy();b[j]-=h
        ngF[j]=(energy(a,chi,r,dr,w,*A)-energy(b,chi,r,dr,w,*A))/(2*h)
        a=chi.copy();a[j]+=h;b=chi.copy();b[j]-=h
        ngc[j]=(energy(F,a,r,dr,w,*A)-energy(F,b,r,dr,w,*A))/(2*h)
    print("grad check F:%.1e chi:%.1e"%(np.max(np.abs(gF[1:-1]-ngF[1:-1]))/(np.max(np.abs(ngF[1:-1]))+1e-12),
                                        np.max(np.abs(gch[1:-1]-ngc[1:-1]))/(np.max(np.abs(ngc[1:-1]))+1e-12)))
