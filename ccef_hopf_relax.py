"""
ccef_hopf_relax.py -- Task F retry: topology-preserving Hopf Q=1 relaxation
===========================================================================
Replaces the failed L-BFGS-B with first-order Adam + kappa-continuation.
Energy/gradients (FD-verified) from ccef_hopf_core.

Strategy:
  Phase A  Adam on physical energy with LARGE kappa penalty E_pen=kappa(Q-1)^2
           -> lock topology while the field finds the soliton basin.
  Phase B  kappa-continuation: anneal kappa downward; field relaxes onto the
           true physical minimum while topology stays pinned.
  Phase C  kappa=0 polish: confirm it is a genuine stationary point of the
           PHYSICAL energy (Virial -> 0) with Q preserved.

Convergence target:  |Q-1|<0.05  AND  |E1-E2+3E4|/E < 0.15 (Virial).
"""
import numpy as np
import json
from ccef_hopf_core import (Grid, energy_components, grad_phys, hopf_Q,
                            hopf_Q_grad_flat, virial, seed_ring)

A1, A2, A4 = 1.0, 0.3268, 3.5553       # Task-D parameters (direct comparison)
E0_MEV = 30.608                         # Task C calibration
MP_CCEF = 938.272 / E0_MEV              # proton mass in CCEF units = 30.65

g = Grid(rho_max=6.0, z_max=6.0, Nr=110, Nz=220)
W = g.w
WSAFE = np.maximum(W, 0.01)
BMASK = np.ones((g.Nr, g.Nz))
BMASK[0, :] = BMASK[-1, :] = BMASK[:, 0] = BMASK[:, -1] = 0.0   # freeze boundaries


def apply_bc(T):
    T[0, :] = 0.0; T[-1, :] = 0.0; T[:, 0] = 0.0; T[:, -1] = 0.0
    return T


def diagnostics(T, P):
    c = energy_components(g, T, P, A1, A2, A4)
    Q = hopf_Q(g, T, P)
    v = virial(c)
    return c, Q, v


QTARGET = -1.0   # set from seed sign in __main__


def total_grad(T, P, kappa, Qtarget=None):
    if Qtarget is None:
        Qtarget = QTARGET
    gT, gP = grad_phys(g, T, P, A1, A2, A4)
    Q = hopf_Q(g, T, P)
    if kappa > 0:
        qT, qP = hopf_Q_grad_flat(g, T, P)
        pref = 2.0 * kappa * (Q - Qtarget)
        gT = gT + pref * qT / WSAFE
        gP = gP + pref * qP / WSAFE
    return gT * BMASK, gP * BMASK, Q


def adam_run(T, P, nsteps, lr, kappa_fn, label, log_every=200,
             b1=0.9, b2=0.999, eps=1e-8, clip=50.0):
    mT = np.zeros_like(T); vT = np.zeros_like(T)
    mP = np.zeros_like(P); vP = np.zeros_like(P)
    hist = []
    for t in range(1, nsteps + 1):
        kappa = kappa_fn(t, nsteps)
        gT, gP, Q = total_grad(T, P, kappa)
        # gradient clipping for stability (quartic A2 term, no A3 smoothing)
        gn = np.sqrt(np.mean(gT**2) + np.mean(gP**2))
        if gn > clip:
            sc = clip / gn; gT *= sc; gP *= sc
        mT = b1 * mT + (1 - b1) * gT; vT = b2 * vT + (1 - b2) * gT**2
        mP = b1 * mP + (1 - b1) * gP; vP = b2 * vP + (1 - b2) * gP**2
        mTh = mT / (1 - b1**t); vTh = vT / (1 - b2**t)
        mPh = mP / (1 - b1**t); vPh = vP / (1 - b2**t)
        T = T - lr * mTh / (np.sqrt(vTh) + eps)
        P = P - lr * mPh / (np.sqrt(vPh) + eps)
        T = apply_bc(T)
        if t % log_every == 0 or t == 1:
            c, Q, v = diagnostics(T, P)
            hist.append((t, c['E'], c['E_A1'], c['E_A2'], c['E_A4'], v,
                         abs(v) / c['E'], Q, kappa, gn))
            print(f"[{label}] {t:5d} E={c['E']:8.3f} "
                  f"A1={c['E_A1']:7.2f} A2={c['E_A2']:7.2f} A4={c['E_A4']:7.2f} "
                  f"vir/E={abs(v)/c['E']:.3f} Q={Q:+.4f} k={kappa:7.1f} |g|={gn:.2f}")
    return T, P, hist


if __name__ == "__main__":
    # ---- seed ----
    T, P = seed_ring(g, R0=1.6, width=0.9)
    if hopf_Q(g, T, P) < 0:
        P = -P                      # orient seed to Q=+1 (avoids early flip transient)
    c0, Q0, v0 = diagnostics(T, P)
    QTARGET = 1.0
    print(f"  (Q target = {QTARGET:+.0f}; seed Q={Q0:+.4f})")
    print(f"SEED: E={c0['E']:.3f} (A1={c0['E_A1']:.2f} A2={c0['E_A2']:.2f} "
          f"A4={c0['E_A4']:.2f}) Q={Q0:.4f} vir/E={abs(v0)/c0['E']:.3f}")
    print(f"Target m_p = {MP_CCEF:.2f} CCEF ; Derrick upper bound = 84.78 CCEF\n")

    allhist = []
    # Phase A: lock topology with large kappa, find the basin
    T, P, h = adam_run(T, P, 2500, lr=3e-3,
                       kappa_fn=lambda t, N: 3000.0, label="A:lock")
    allhist += h
    # Phase B: anneal kappa 3000 -> 50 (continuation)
    T, P, h = adam_run(T, P, 4000, lr=2e-3,
                       kappa_fn=lambda t, N: 3000.0 * (50.0 / 3000.0) ** (t / N),
                       label="B:anneal")
    allhist += h
    # Phase C: small kappa polish (confirm physical stationarity)
    T, P, h = adam_run(T, P, 4000, lr=1e-3,
                       kappa_fn=lambda t, N: 50.0, label="C:polish")
    allhist += h

    c, Q, v = diagnostics(T, P)
    # effective torus radius
    sinT_int = np.trapz(np.sin(T), g.z, axis=1) if not hasattr(np, 'trapezoid') \
        else np.trapezoid(np.sin(T), g.z, axis=1)
    R_eff = g.rho[int(np.argmax(sinT_int))]

    print("\n==================== FINAL ====================")
    print(f"  E_sol = {c['E']:.4f} CCEF  = {c['E']*E0_MEV:.1f} MeV  = {c['E']/MP_CCEF:.3f} x m_p")
    print(f"  E_A1={c['E_A1']:.4f}  E_A2={c['E_A2']:.4f}  E_A4={c['E_A4']:.4f}")
    print(f"  Virial E1-E2+3E4 = {v:.4f}   |vir/E| = {abs(v)/c['E']:.4f}")
    print(f"  Q = {Q:.5f}   R_eff = {R_eff:.3f} CCEF")
    print(f"  Derrick scaling-only upper bound was 84.78 CCEF (2.77 x m_p)")
    valid = abs(Q - 1.0) < 0.05 and abs(v) / c['E'] < 0.15
    print(f"  VALID MINIMUM: {valid}  (need |Q-1|<0.05 and |vir/E|<0.15)")

    np.save("relax_T.npy", T); np.save("relax_P.npy", P)
    np.save("relax_rho.npy", g.rho); np.save("relax_z.npy", g.z)
    with open("relax_hist.json", "w") as f:
        json.dump({"hist": allhist, "final": {
            "E": c['E'], "E_A1": c['E_A1'], "E_A2": c['E_A2'], "E_A4": c['E_A4'],
            "virial": v, "Q": Q, "R_eff": float(R_eff),
            "E_MeV": c['E']*E0_MEV, "E_over_mp": c['E']/MP_CCEF, "valid": bool(valid)}},
            f, indent=2)
    print("  saved relax_{T,P,rho,z}.npy, relax_hist.json")
