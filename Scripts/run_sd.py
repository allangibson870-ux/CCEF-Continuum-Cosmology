import sys, time, json, numpy as np, ccef3d as M, ccef3d_sd as S
BUD=float(sys.argv[1]) if len(sys.argv)>1 else 34.0
DT=0.004
try:
    d=np.load("sd_state.npz"); n=d["n"]; step=int(d["step"]); cc=float(d["cc"]); traj=[list(r) for r in d["traj"]]
except FileNotFoundError:
    n=S.seed(0.7); cc=1.0/M.hopf_charge(S.box,n); step=0; traj=[]
t0=time.time()
while (time.time()-t0)<BUD:
    step+=1
    n=S.step(n,DT)
    if step%10==0:
        e=S.energies(n); H=M.hopf_charge(S.box,n)*cc; v=S.virial(e)
        traj.append([step,e['E'],e['E_A1'],e['E_A2'],e['E_A3'],e['E_A4'],abs(v)/e['E'],H])
np.savez("sd_state.npz",n=n,step=step,cc=cc,traj=np.array(traj))
e=S.energies(n); H=M.hopf_charge(S.box,n)*cc; v=S.virial(e)
print('step=%d E=%.2f (A1=%.1f A2=%.2f A3=%.1f A4=%.2f) vir/E=%.3f H=%.3f E/mp=%.2f %.0fs'%(
    step,e['E'],e['E_A1'],e['E_A2'],e['E_A3'],e['E_A4'],abs(v)/e['E'],H,e['E']/S.MP,time.time()-t0))
json.dump({'step':step,'E':e['E'],'E_A1':e['E_A1'],'E_A2':e['E_A2'],'E_A3':e['E_A3'],
  'E_A4':e['E_A4'],'vir_over_E':abs(v)/e['E'],'H':H,'E_over_mp':e['E']/S.MP,
  'E_MeV':e['E']*S.E0,'N':S.N,'dx':S.box.dx},open("sd_result.json","w"),indent=2)
