#!/usr/bin/env python3
"""
ccef_parity_breaking.py  --  how and where does the grain world's left<->right (inversion) symmetry break?

1. GEOMETRIC ('breathing') breaking: make the two junction types inequivalent (A != B):
     (i)  staggered on-site energy  +V on A, -V on B
     (ii) different spin-orbit strength on A and B junctions (lambda_A != lambda_B)
   Both break inversion (P) but keep time reversal (T).  Effect on the grain Dirac fermion at X:
   which mass type appears (scalar P-even / pseudoscalar 'theta-type' P-odd T-odd), or does the Dirac point split into
   Weyl points (left- and right-handed parts moved apart in momentum)?
2. WHERE: the left-right breaking scale v_R allowed by neutrino masses (seesaw), domain walls + theta_bar,
   cosmic strings (if B-L breaks to a Z2), LHC (W_R).
"""

import contextlib
import io

import numpy as np
from scipy.optimize import minimize

with contextlib.redirect_stdout(io.StringIO()):
    import ccef_strong_cp as scp

X = scp.X
base = scp.base_terms()


def onsite(V):
    return [(0, 0, np.zeros(3), 0.5 * V * scp.I2), (1, 1, np.zeros(3), -0.5 * V * scp.I2)]


def soc_breathing(dl):
    out = []
    for sub, key, s in ((0, "A", +1), (1, "B", -1)):
        for R, Mm in scp.SOC[key]:
            out.append((sub, sub, R, 0.5 * 1j * (8 * (s * dl) / 16) * Mm))
    return out


def analyse(pert, label):
    terms = base + pert
    dH = scp.H_of_k(pert, X)
    m1 = np.trace(dH @ scp.B1).real / 4
    m2 = np.trace(dH @ scp.B2).real / 4
    emin = lambda k: np.min(np.abs(np.linalg.eigvalsh(scp.H_of_k(terms, np.asarray(k)))))
    nodes = []
    rng = np.random.default_rng(0)
    for _ in range(40):
        r = minimize(emin, X + rng.normal(scale=0.08, size=3), method="Nelder-Mead",
                     options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": 4000})
        if r.fun < 1e-6 and np.linalg.norm(r.x - X) < 0.5:
            if all(np.linalg.norm(r.x - n) > 1e-4 for n in nodes):
                nodes.append(r.x)
    gap = min(emin(X + d) for d in [np.zeros(3)] + [rng.normal(scale=0.05, size=3) for _ in range(200)])
    mult = [int(np.sum(np.abs(np.linalg.eigvalsh(scp.H_of_k(terms, n))) < 1e-5)) for n in nodes]
    sep = max((np.linalg.norm(a - b) for a in nodes for b in nodes), default=0.0)
    print(f"   {label:38s}: scalar mass {m1:+.1e}, theta-type mass {m2:+.1e};  zero-energy points near X: {len(nodes)}"
          f" (multiplicity {sorted(set(mult))}), max separation {sep:.3f};  min |E| sampled {gap:.1e}")


print("1. GEOMETRIC (breathing) INVERSION BREAKING on the grain Dirac fermion at X")
analyse([], "no breaking")
for V in (0.02, 0.05):
    analyse(onsite(V), f"staggered on-site V = {V}")
for dl in (0.02, 0.05):
    analyse(soc_breathing(dl), f"spin-orbit breathing dlambda = {dl}")
print("   reading: breathing breaks P but not T, so it cannot create the theta-type mass (which is P- AND T-odd).")
print("   Instead each 4-fold Dirac point splits into 2-fold WEYL points: the left- and right-handed halves are pulled")
print("   apart in momentum - the first step toward a chiral (left/right-distinguishing) low-energy world.\n")

print("2. WHERE: the left-right breaking scale v_R")
MP, v = 1.22e19, 174.0
mnu = 5e-11
print(f"   {'v_R (GeV)':>10s} {'seesaw y^2/f':>13s} {'walls: eps >=':>14s} {'theta ok if kappa <=':>21s} {'Z2-string G mu':>15s}")
for vR in (1e4, 1e10, 1e12, 1e13, 1e14, 1e15):
    yy = mnu * vR / v ** 2
    eps = (vR / MP) ** 2
    print(f"   {vR:10.0e} {yy:13.1e} {eps:14.0e} {1e-10 / eps:21.0e} {eps:15.0e}")
print("   LHC: W_R heavier than ~6 TeV.  Pulsar timing limits stable strings to G mu <~ 1e-10 (if B-L breaks to Z2).")
print("   Natural window: v_R ~ 1e13 - 1e14 GeV  (seesaw couplings ~0.02-0.2; walls removable with theta_bar ~ 1e-12-1e-10;")
print("   strings G mu ~ 7e-13 - 7e-11, below the pulsar limit and inside LISA / future-detector reach).")
