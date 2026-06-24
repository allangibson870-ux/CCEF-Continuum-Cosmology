import sys, time, json, numpy as np, ccef3d as M
A1,A2,A4=1.0,0.3268,3.5553
E0=30.608; MP=938.272/E0
L,N=2.6,96
box=M.Box(L=L,N=N)
BUD=float(sys.argv[1]) if len(sys.argv)>1 else 36.0
def seed(scale):
    x,y,z=box.X/scale,box.Y/scale,box.Z/scale; r2=x*x+y*y+z*z
    den=2*z+1j*(r2-1.0); den=den+1e-9*(np.abs(den)<1e-9)
    w=2*(x+1j*y)/den; aw2=np.abs(w)**2; dd=aw2+1.0
    return M.renorm(np.stack([2*np.real(w)/dd,2*np.imag(w)/dd,(aw2-1.0)/dd]))
try:
    d=np.load("r96_state.npz"); n=d["n"]; step=int(d["step"]); cc=float(d["cc"]); traj=list(d["traj"])
except FileNotFoundError:
    n=seed(1.1); cc=1.0/M.hopf_charge(box,n); step=0; traj=[]
def lr(s): return 1.2e-3 if s<1500 else (8e-4 if s<3500 else 5e-4)
t0=time.time()
while (time.time()-t0)<BUD:
    step+=1
    g=-M.proj_force(box,n,A1,A2,A4)
    gn=np.sqrt(np.mean(g**2))
    if gn>10: g*=10/gn
    n=M.renorm(n-lr(step)*g)
    if step%25==0:
        e=M.energies(box,n,A1,A2,A4); v=M.virial(e); H=M.hopf_charge(box,n)*cc
        traj.append([step,e['E'],e['E_A1'],e['E_A2'],e['E_A4'],abs(v)/e['E'],H])
np.savez("r96_state.npz",n=n,step=step,cc=cc,traj=np.array(traj))
e=M.energies(box,n,A1,A2,A4); v=M.virial(e); H=M.hopf_charge(box,n)*cc
E1,E2,E4=e['E_A1'],e['E_A2'],e['E_A4']
u=(-E1+(E1*E1+12*E2*E4)**0.5)/(6*E4); lam=u**0.5
Eder=lam*E1+E2/lam+lam**3*E4
print("step=%d E=%.2f vir/E=%.3f Hcal=%.3f | Derrick: lam*=%.3f E_sol=%.2f =%.2fxmp %.0fs"%(
    step,e['E'],abs(v)/e['E'],H,lam,Eder,Eder/MP,time.time()-t0))
json.dump({"step":step,"E":e['E'],"E_A1":e['E_A1'],"E_A2":e['E_A2'],"E_A4":e['E_A4'],
    "vir_over_E":abs(v)/e['E'],"Hcal":H,"E_over_mp":e['E']/MP,"E_MeV":e['E']*E0,
    "N":N,"L":L,"dx":box.dx,"E_derrick":Eder,"lam":lam,"Eder_over_mp":Eder/MP},open("r96_result.json","w"),indent=2)
