"""
ccef3d_relax.py -- checkpointed 3D Hopf relaxation (Adam gradient flow).
Pure energy gradient flow (no penalty); |n|=1 renormalised each step.
Topology monitored via Whitehead charge (relative drift => unwinding).
"""
import sys, time, json, numpy as np
import ccef3d as M

A1, A2, A4 = 1.0, 0.3268, 3.5553
E0_MEV = 30.608
MP = 938.272 / E0_MEV          # 30.65 CCEF
L, N = 2.5, 64
TOTAL = int(sys.argv[2]) if len(sys.argv) > 2 else 6000
BUDGET = float(sys.argv[1]) if len(sys.argv) > 1 else 38.0
box = M.Box(L=L, N=N)


def exact_seed(b, scale):
    x, y, z = b.X/scale, b.Y/scale, b.Z/scale
    r2 = x*x+y*y+z*z
    den = 2*z+1j*(r2-1.0)
    den = den+1e-9*(np.abs(den) < 1e-9)
    w = 2*(x+1j*y)/den
    aw2 = np.abs(w)**2
    dd = aw2+1.0
    return M.renorm(np.stack([2*np.real(w)/dd, 2*np.imag(w)/dd, (aw2-1.0)/dd]))


def load():
    try:
        d = np.load("r3d_state.npz")
        return d["n"], d["mn"], d["vn"], int(d["step"]), float(d["H0"])
    except FileNotFoundError:
        n = exact_seed(box, scale=0.7)
        H0 = M.hopf_charge(box, n)
        z = np.zeros_like(n)
        return n, z.copy(), z.copy(), 0, H0


def lr_of(step):
    # conservative: aggressive Adam overshoots and unwinds the topology
    if step < 3000:
        return 1.5e-3
    if step < 7000:
        return 1.0e-3
    return 6e-4


def main():
    n, mn, vn, step, H0 = load()
    mom = 0.0                        # PURE gradient flow (momentum unwinds this shallow min)
    t0 = time.time()
    logf = open("r3d_run.log", "a")
    while step < TOTAL and (time.time()-t0) < BUDGET:
        step += 1
        g = -M.proj_force(box, n, A1, A2, A4)    # projected dE/dn
        gn = np.sqrt(np.mean(g**2))
        if gn > 10:
            g *= 10/gn
        mn = mom*mn - lr_of(step)*g              # velocity (heavy-ball)
        n = M.renorm(n + mn)
        if step % 200 == 0:
            e = M.energies(box, n, A1, A2, A4)
            v = M.virial(e)
            H = M.hopf_charge(box, n)
            line = (f"{step:5d} E={e['E']:8.3f} A1={e['E_A1']:7.2f} A2={e['E_A2']:7.2f} "
                    f"A4={e['E_A4']:7.2f} vir/E={abs(v)/e['E']:.4f} H={H:.4f}(H0={H0:.4f}) "
                    f"|g|={gn:.2f}")
            print(line); logf.write(line+"\n"); logf.flush()
    np.savez("r3d_state.npz", n=n, mn=mn, vn=vn, step=step, H0=H0)
    e = M.energies(box, n, A1, A2, A4); v = M.virial(e); H = M.hopf_charge(box, n)
    print(f"--- chunk end step={step}/{TOTAL} E={e['E']:.3f} vir/E={abs(v)/e['E']:.4f} "
          f"H={H:.4f}/H0={H0:.4f} elapsed={time.time()-t0:.1f}s")
    logf.close()
    if step >= TOTAL:
        # topology-charge calibration: c so that exact seed reads 1
        cn = exact_seed(box, 0.7)
        c = 1.0/M.hopf_charge(box, cn)
        res = dict(E=e['E'], E_A1=e['E_A1'], E_A2=e['E_A2'], E_A4=e['E_A4'],
                   virial=v, vir_over_E=abs(v)/e['E'], H_raw=H, H_cal=H*c,
                   E_MeV=e['E']*E0_MEV, E_over_mp=e['E']/MP,
                   L=L, N=N, dx=box.dx)
        json.dump(res, open("r3d_result.json", "w"), indent=2)
        np.save("r3d_n.npy", n)
        print("=== DONE ===")
        print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
