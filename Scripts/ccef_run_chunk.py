"""
ccef_run_chunk.py -- checkpointed driver for the Hopf relaxation.
Resumes from relax_state.npz, runs steps until a wall-time budget, saves state.
Global-step schedule (total 10500):
  0-2500    : lock     kappa=3000, lr=3e-3
  2500-6500 : anneal   kappa 3000->50 (geometric), lr=2e-3
  6500-10500: polish   kappa=50,   lr=1e-3
"""
import sys, time, json, numpy as np
import ccef_hopf_relax as R

g = R.g
TOTAL = 10500
BUDGET = float(sys.argv[1]) if len(sys.argv) > 1 else 38.0
R.QTARGET = 1.0


def sched(step):
    if step < 2500:
        return 3000.0, 3e-3
    if step < 6500:
        f = (step - 2500) / 4000.0
        return 3000.0 * (50.0 / 3000.0) ** f, 2e-3
    return 50.0, 1e-3


def load():
    try:
        d = np.load("relax_state.npz")
        return (d["T"], d["P"], d["mT"], d["vT"], d["mP"], d["vP"], int(d["step"]))
    except FileNotFoundError:
        T, P = R.seed_ring(g, R0=1.6, width=0.9)
        if R.hopf_Q(g, T, P) < 0:
            P = -P
        z = np.zeros_like(T)
        return (T, P, z.copy(), z.copy(), z.copy(), z.copy(), 0)


def main():
    T, P, mT, vT, mP, vP, step = load()
    b1, b2, eps, clip = 0.9, 0.999, 1e-8, 50.0
    t0 = time.time()
    logf = open("relax_run.log", "a")
    while step < TOTAL and (time.time() - t0) < BUDGET:
        step += 1
        kappa, lr = sched(step)
        gT, gP, Q = R.total_grad(T, P, kappa, Qtarget=1.0)
        gn = np.sqrt(np.mean(gT**2) + np.mean(gP**2))
        if gn > clip:
            s = clip / gn; gT *= s; gP *= s
        mT = b1*mT + (1-b1)*gT; vT = b2*vT + (1-b2)*gT**2
        mP = b1*mP + (1-b1)*gP; vP = b2*vP + (1-b2)*gP**2
        c1 = 1-b1**step; c2 = 1-b2**step
        T = T - lr*(mT/c1)/(np.sqrt(vT/c2)+eps)
        P = P - lr*(mP/c1)/(np.sqrt(vP/c2)+eps)
        R.apply_bc(T)
        if step % 250 == 0:
            c, Q, v = R.diagnostics(T, P)
            line = (f"{step:5d} E={c['E']:8.3f} A1={c['E_A1']:7.2f} A2={c['E_A2']:7.2f} "
                    f"A4={c['E_A4']:7.2f} vir/E={abs(v)/c['E']:.4f} Q={Q:+.4f} "
                    f"k={kappa:7.1f} |g|={gn:.2f}")
            print(line); logf.write(line+"\n"); logf.flush()
    np.savez("relax_state.npz", T=T, P=P, mT=mT, vT=vT, mP=mP, vP=vP, step=step)
    c, Q, v = R.diagnostics(T, P)
    print(f"--- chunk end: step={step}/{TOTAL} E={c['E']:.3f} vir/E={abs(v)/c['E']:.4f} "
          f"Q={Q:+.4f} elapsed={time.time()-t0:.1f}s")
    logf.close()
    if step >= TOTAL:
        sinT_int = (np.trapezoid if hasattr(np,'trapezoid') else np.trapz)(np.sin(T), g.z, axis=1)
        R_eff = float(g.rho[int(np.argmax(sinT_int))])
        E0 = 30.608; MP = 938.272/E0
        valid = abs(Q-1.0) < 0.05 and abs(v)/c['E'] < 0.15
        np.save("relax_T.npy", T); np.save("relax_P.npy", P)
        np.save("relax_rho.npy", g.rho); np.save("relax_z.npy", g.z)
        res = {"E": c['E'], "E_A1": c['E_A1'], "E_A2": c['E_A2'], "E_A4": c['E_A4'],
               "virial": v, "vir_over_E": abs(v)/c['E'], "Q": Q, "R_eff": R_eff,
               "E_MeV": c['E']*E0, "E_over_mp": c['E']/MP, "valid": bool(valid)}
        json.dump(res, open("relax_result.json", "w"), indent=2)
        print("=== DONE ===", json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
