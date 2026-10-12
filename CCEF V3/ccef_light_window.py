#!/usr/bin/env python3
"""
ccef_light_window.py  --  is the light sector's coupling ratio x = J_pm/J_zz consistent with everything that needs it?

1. LIGHT EXISTS only inside quantum spin ice's Coulomb (photon) phase: |x| < x_c ~ 0.052 in J_pm units (Kato & Onoda, QMC, PRL 115,
   077202 (2015): |J_perp|/J < 0.104 with J_pm = -J_perp/2; unfrustrated sign).  Rishon splitting (CCEF_rishon_splitting.md) needs x <~ 0.1 to rescue
   the finite universe.  -> the photon's existence alone implies the rescue condition?
2. ELECTRONS in the current construction are the spin-ice charges themselves (fermionic string ends; Gauss parity =
   fermion parity, CCEF_grain_electrons.md).  In spin ice a charge hops at first order (~J_pm) while light is third order
   (J_ring = 12 J_pm^3 / J_zz^2), and charges cost ~J_zz.  Two consequences checked:
   (a) speed mismatch: charge hopping / light scale = J_pm / J_ring = 1 / (12 x^2)
   (b) Mott instability of the spin-1/2 grain electron (Fu-Kane-Mele on diamond): mean-field critical on-site
       repulsion U_c (staggered and uniform magnetic channels, all spin axes) vs U/t ~ J_zz / J_pm = 1/x.
"""

import contextlib
import io
import math

import numpy as np

with contextlib.redirect_stdout(io.StringIO()):
    import ccef_strong_cp as scp

XC = 0.052   # Kato-Onoda |J_perp|/J = 0.104 with J_pm = -J_perp/2 (HFB convention, J_ring = 12 J_pm^3/J_zz^2)

# ---------------------------------------------------------------- 1. photon window vs rescue
print("1. LIGHT EXISTS ONLY FOR x = J_pm/J_zz < x_c ~ 0.052 (quantum spin ice Coulomb phase, QMC; |J_perp|/J < 0.104)")
pref = 1.04 * (9 / 495) ** (2 / 3)
for x in (XC, 0.04, 0.03, 0.02):
    R = (1 / x) ** 3 / 12
    Ls = [pref * (1.3 * n * R) ** (1 / 3) for n in (25, 31, 37)]
    tag = "  <- edge of the photon phase" if x == XC else ""
    print(f"   x = {x:5.3f}: R = J_zz/J_ring = {R:6.0f};  median L_max = {Ls[0]:.2f} / {Ls[1]:.2f} / {Ls[2]:.2f} D_LSS"
          f" (n = 25 / 31 / 37){tag}")
print("   -> wherever light exists, the rishon-splitting universe is >~ 1 D_LSS: the rescue condition is the photon's own")
print("      existence condition, not an extra tuning.  Prediction (N_ent = 495): L ~ 2.1 (x_c / x) D_LSS; with N_ent")
print("      880-1080 (CCEF_valleys_edges.md) the edge value is 1.2-1.4 D_LSS: still >~ 1 D_LSS wherever light exists\n")

# ---------------------------------------------------------------- 2a. speed mismatch
print("2a. SPEED: charges hop at first order (J_pm), light is third-order ring exchange (J_ring = 12 J_pm^3/J_zz^2)")
for x in (XC, 0.03):
    print(f"    x = {x:5.3f}: charge hopping / light scale = 1/(12 x^2) = {1 / (12 * x * x):5.1f}")
print("    -> spin-ice charges are generically FASTER than spin-ice light (they Cherenkov-radiate; known in the QSI")
print("       literature).  Electrons that are bare spin-ice charges would break the one-light-cone requirement.\n")

# ---------------------------------------------------------------- 2b. Mott instability (mean field)
base = scp.base_terms(0.25)
A = np.array([[0, 2, 2], [2, 0, 2], [2, 2, 0]], dtype=float)            # FCC primitive vectors (rows)
B = 2 * np.pi * np.linalg.inv(A).T
NK = 32
g = (np.arange(NK) + 0.5) / NK
K = np.array([[a, b, c] for a in g for b in g for c in g]) @ B
H = np.array([scp.H_of_k(base, k) for k in K])
E, V = np.linalg.eigh(H)
occ = E < 0
print(f"2b. MOTT: grain electron (spin-1/2 FKM, lambda = 1/4, t = 1), {len(K)} k-points; half filling check: "
      f"{occ.sum() / len(K):.2f} filled bands of 4")
SIG = {"x": scp.SX, "y": scp.SY, "z": scp.SZ}
res = []
for pat, eps in (("staggered (A up, B down)", (1, -1)), ("uniform (ferro)", (1, 1))):
    for ax, s in SIG.items():
        O = np.kron(np.diag(eps), s)                                    # per-cell operator, 2 sites
        Ok = np.einsum("kia,ij,kjb->kab", V.conj(), O, V)
        dE = E[:, None, :] - E[:, :, None]                               # E_m - E_n  [k, n, m]
        mask = occ[:, :, None] & ~occ[:, None, :]
        chi = 2 * np.sum(np.where(mask, np.abs(Ok) ** 2 / np.where(mask, dE, 1), 0)) / (len(K) * 2)
        Uc = 2 / chi
        res.append((Uc, pat, ax))
        print(f"    {pat:26s} sigma_{ax}: chi = {chi:.3f} per site -> mean-field U_c = {Uc:5.2f} t")
Ucmin = min(r[0] for r in res)
print(f"    lowest mean-field U_c = {Ucmin:.2f} t (mean field underestimates U_c; true value likely 1.5-2x larger)")
print("    the charge cost in spin ice (J_zz Q^2/2) acts as an on-site repulsion U ~ J_zz between two charges on one")
print("    junction (O(1) factor depends on the spin-1/2 encoding); charge hopping t ~ J_pm:")
for x in (XC, 0.03):
    print(f"    x = {x:5.3f}: U/t ~ 1/x = {1 / x:5.1f}  vs U_c ~ {Ucmin:.1f}-{2 * Ucmin:.1f}  ->"
          f" {'MOTT INSULATOR (electrons gapped)' if 1 / x > 2 * Ucmin else 'borderline'}")
print("    with one light cone imposed (t matched to light, t ~ J_ring): U/t ~ J_zz/J_ring = R >~ 590 -> deeper still\n")

print("VERDICT: the photon phase automatically delivers the rishon-splitting rescue (good), but in that same phase")
print("electrons built as bare spin-ice charges are too fast AND Mott-gapped (bad).  The electron construction must change:")
print("matter as separate constituents of the relation bundle, with the Gauss law div E = rho (no on-site J_zz penalty)")
print("and a gauge-covariant hop whose speed matches light.")
