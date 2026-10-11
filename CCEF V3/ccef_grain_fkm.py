#!/usr/bin/env python3
"""
ccef_grain_fkm.py  --  spin-1/2 junction fermions on the 3-D grain (diamond) graph: relativistic electrons?

Each relation is a PAIR of grains -> two fermion modes per junction (spin up/down, via the dressed-hop encoding).
Fu-Kane-Mele hopping:  H = -sum_<ij> t_ij c_i^+ c_j  +  i (8 lambda / a^2) sum_<<ij>> c_i^+ s.(d1 x d2) c_j
(second term = spin-orbit hop through the shared neighbour; d1, d2 the two bonds).  Units a = 4 (bond = (1,1,1)).
Tests:
  1. lambda = 0 -> nodal lines (spinless no-go persists);  lambda != 0 -> isolated 4-fold Dirac points?  where, how many?
  2. cone speeds at a Dirac point (parallel / perpendicular): is there an isotropic (Lorentz-like) choice of lambda/t?
  3. masses: unequal bond strengths t_1..t_4 (junction anisotropy) -> gaps at each Dirac point.
"""

import itertools

import numpy as np
from scipy.optimize import minimize

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2)
DEL = np.array([(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)], dtype=float)       # A -> B bonds
FCC = [np.array(v, dtype=float) for v in itertools.product((-2, 0, 2), repeat=3)
       if sorted(np.abs(v)) == [0, 2, 2]]                                              # 12 second neighbours


def soc_terms():
    """for each sublattice (A: bonds +DEL, B: bonds -DEL) and each fcc vector R: s.(d1 x d2) via the shared neighbour"""
    out = {}
    for sub, sign in (("A", 1), ("B", -1)):
        lst = []
        for R in FCC:
            for d1 in sign * DEL:
                d2 = R - d1
                if any(np.allclose(d2, -sign * d) for d in DEL):
                    c = np.cross(d1, d2)
                    lst.append((R, c[0] * SX + c[1] * SY + c[2] * SZ))
                    break
        out[sub] = lst
    return out


SOC = soc_terms()


def H(k, t=(1, 1, 1, 1), lam=0.1):
    hAB = -sum(ti * np.exp(1j * k @ d) for ti, d in zip(t, DEL)) * I2
    hAA = sum(1j * (8 * lam / 16) * np.exp(1j * k @ R) * M for R, M in SOC["A"])
    hBB = sum(1j * (8 * lam / 16) * np.exp(1j * k @ R) * M for R, M in SOC["B"])
    Hm = np.zeros((4, 4), dtype=complex)
    Hm[:2, :2], Hm[2:, 2:], Hm[:2, 2:], Hm[2:, :2] = hAA, hBB, hAB, hAB.conj().T
    assert np.allclose(Hm, Hm.conj().T)
    return Hm


def emin(k, **kw):
    return np.min(np.abs(np.linalg.eigvalsh(H(np.asarray(k), **kw))))


G = 2 * np.pi / 4 * 2                                     # cubic reciprocal unit (2pi/a with a=4) times 2 covers the BZ
rng = np.random.default_rng(0)
X = {"X_x": np.array([np.pi / 2, 0, 0]), "X_y": np.array([0, np.pi / 2, 0]), "X_z": np.array([0, 0, np.pi / 2])}

print("1. NODES")
for lam in (0.0, 0.1):
    zeros = []
    for _ in range(150):
        r = minimize(lambda kk: emin(kk, lam=lam), rng.uniform(-np.pi, np.pi, 3), method="Nelder-Mead",
                     options={"xatol": 1e-10, "fatol": 1e-12, "maxiter": 4000})
        if r.fun < 1e-6:
            zeros.append(r.x)
    # fold into the BZ using the fcc reciprocal lattice (b vectors (pi/2)(-1,1,1) etc. with a = 4)
    B = np.array([(-1, 1, 1), (1, -1, 1), (1, 1, -1)]) * np.pi / 2
    def fold(k):
        best = k
        for n in itertools.product(range(-2, 3), repeat=3):
            q = k + np.array(n) @ B
            if np.linalg.norm(q) < np.linalg.norm(best) - 1e-9:
                best = q
        return best
    zf = [fold(z) for z in zeros]
    distinct = []
    for z in zf:
        if all(min(np.linalg.norm(z - d), np.linalg.norm(z + d)) > 1e-3 for d in distinct):
            distinct.append(z)
    print(f"   lambda/t = {lam}: {len(zeros)}/150 searches hit E = 0; distinct zero locations (up to k -> -k): {len(distinct)}")
    if lam > 0:
        for z in distinct:
            mult = int(np.sum(np.abs(np.linalg.eigvalsh(H(z, lam=lam))) < 1e-5))
            print(f"      k = {np.round(z / (np.pi / 2), 4)} x (2pi/a): E=0 multiplicity {mult}")

print("\n2. CONE SPEEDS at X_x (units t x a/4), as a function of lambda/t")
for lam in (0.05, 0.1, 0.2, 0.25, 0.3, 0.4):
    h = 1e-5
    vs = []
    for d in np.eye(3):
        e = np.sort(np.abs(np.linalg.eigvalsh(H(X["X_x"] + h * d, lam=lam))))[0]
        vs.append(e / h)
    print(f"   lambda/t = {lam:4.2f}: v_x = {vs[0]:.3f}, v_y = {vs[1]:.3f}, v_z = {vs[2]:.3f}   (anisotropy {max(vs) / min(vs):.2f})")
from scipy.optimize import brentq
f = lambda lam: (np.sort(np.abs(np.linalg.eigvalsh(H(X["X_x"] + 1e-5 * np.eye(3)[0], lam=lam))))[0]
                 - np.sort(np.abs(np.linalg.eigvalsh(H(X["X_x"] + 1e-5 * np.eye(3)[1], lam=lam))))[0])
try:
    lam_iso = brentq(f, 0.01, 1.0)
    print(f"   isotropic (Lorentz-like) cone at lambda/t = {lam_iso:.4f}")
except ValueError:
    print("   no isotropic point found in 0.01-1")

print("\n3. MASSES from junction anisotropy (bond strengths t1..t4 = 1 + eps_i), lambda/t = 0.1")
for eps in ((0.01, 0, 0, 0), (0.02, -0.01, 0.005, 0.0), (0.0, 0.001, 0.0, 0.0)):
    t = tuple(1 + e for e in eps)
    gaps = {n: np.min(np.abs(np.linalg.eigvalsh(H(x, t=t, lam=0.1)))) for n, x in X.items()}
    e1, e2, e3, e4 = eps
    pred = {"X_x": abs(e1 + e2 - e3 - e4), "X_y": abs(e1 - e2 + e3 - e4), "X_z": abs(e1 - e2 - e3 + e4)}
    print(f"   eps = {eps}: half-gaps " + ", ".join(f"{n} {gaps[n]:.5f} (|Klein combo| {pred[n]:.5f})" for n in X))

