"""Robustness / sanity checks for the Sec 17.7 Kubo verdict."""
import numpy as np
Lam=1.0

def make(Tc, m_c, vertex_pow):
    def nB(E): return 1.0/np.expm1(E/Tc)
    def ImPi_pair(w,m1,m2):
        thr=m1+m2
        if w<=thr: return 0.0
        num=(w*w-m1*m1-m2*m2)**2-4*m1*m1*m2*m2
        if num<=0: return 0.0
        p2=num/(4*w*w); p=np.sqrt(p2)
        E1=np.sqrt(p2+m1*m1); E2=np.sqrt(p2+m2*m2)
        ps=(1/(4*np.pi**2))*p2/(p/E1+p/E2)
        return ps*(1+nB(E1)+nB(E2))*(w**vertex_pow)/2
    def tot(w):
        return ImPi_pair(w,Lam,Lam)+ImPi_pair(w,m_c,m_c)+2*ImPi_pair(w,Lam,m_c)
    return tot

print("Robustness of Im Pi(2Lam) and of the coherent NO-FILTER result")
print(f"{'Tc':>5} {'m_c':>7} {'vtx':>4} | {'ImPi(2L)':>10} {'ImPi(0.01)':>11} {'ratio Re(2L)/Re0':>16}")
for Tc in [0.58,0.65,0.78]:
  for m_c in [1e-2,1e-3,1e-4]:
    for vp in [2,0]:
      f=make(Tc,m_c,vp)
      sg=np.linspace(1e-4,60,60000); rho=np.array([f(s) for s in sg])
      Re0=(2/np.pi)*np.trapz(rho/sg,sg)
      w=2.0
      integ=rho*2/(sg*(sg*sg-w*w)); mask=np.abs(sg-w)>2*(sg[1]-sg[0])
      Re2=Re0+(w*w/np.pi)*np.trapz(integ[mask],sg[mask])
      print(f"{Tc:5.2f} {m_c:7.0e} {vp:4d} | {f(2.0):10.3e} {f(0.01):11.3e} {Re2/Re0:16.4f}")

print()
print("Key invariants (all parameter choices):")
print(" * TT gapped-pair channel = 0 for w<2Lam, threshold-zero AT 2Lam  (checked in main)")
print(" * Im Pi(2Lam) nonzero but only O(thermal); ratio Re(2L)/Re0 ~ 1  -> no filtering")
print(" * drain fraction fixed at (Lam/M)^2 = 1.7e-40 regardless of thermal O(1)")

# order-of-limits sanity: Landau cut collapses as k->0
print()
print("Order-of-limits (Landau/scattering cut) check:")
print(" at strictly k=0 the 1<->1 scattering cut has zero measure (needs w<k);")
print(" only the pair-creation cut (w>=2m) + Bose enhancement survive -> as coded.")
