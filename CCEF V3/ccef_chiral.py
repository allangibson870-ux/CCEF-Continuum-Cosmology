#!/usr/bin/env python3
"""
ccef_chiral.py  --  toward a one-handed (chiral) weak force from grains: the mirror-gapping route.

Grains (any lattice) give fermions in left+right pairs (Nielsen-Ninomiya).  A chiral force needs the 'mirror' partners
gapped WITHOUT bilinear masses (which would pair L with R): symmetric mass generation (SMG).  SMG is possible only if
the mirror sector has no anomaly in the symmetries it must keep.

1. Anomaly bookkeeping for one Standard-Model generation (left-handed Weyl basis), with / without nu^c:
   perturbative gauge anomalies, Witten SU(2), and the Z16 count for the spin-Z4 symmetry X = 5(B-L) - 4Y.
2. Proof-of-principle SMG by exact diagonalisation: n Majorana fermions with a time-reversal symmetry that forbids every
   bilinear mass; random T-symmetric quartic interactions; is there a UNIQUE gapped ground state?  (Fidkowski-Kitaev:
   only when n is a multiple of 8 - the 0+1-d analogue of the 4-d 'multiple of 16' rule.)
"""

import itertools
from fractions import Fraction as F

import numpy as np

# ------------------------------------------------------------------ 1. anomalies
# (name, multiplicity = colours x isospin components, SU3 rep dim, SU2 rep dim, Y, B, L)
fields = [("Q", 6, 3, 2, F(1, 6), F(1, 3), 0), ("u^c", 3, 3, 1, F(-2, 3), F(-1, 3), 0),
          ("d^c", 3, 3, 1, F(1, 3), F(-1, 3), 0), ("L", 2, 1, 2, F(-1, 2), 0, 1),
          ("e^c", 1, 1, 1, F(1, 1), 0, -1), ("nu^c", 1, 1, 1, F(0), 0, -1)]
T3 = {1: 0, 3: F(1, 2)}            # SU(3) Dynkin index of the fundamental
A3 = {1: 0, 3: 1}                  # SU(3) cubic anomaly coefficient (3bar counted with sign via conjugation below)


def anomalies(include_nuc):
    fs = [f for f in fields if include_nuc or f[0] != "nu^c"]
    out = {}
    out["U(1)_Y^3"] = sum(m * Y ** 3 for _, m, _, _, Y, _, _ in fs)
    out["grav^2 U(1)_Y"] = sum(m * Y for _, m, _, _, Y, _, _ in fs)
    out["SU(2)^2 U(1)_Y"] = sum((m // 2) * Y for n, m, c, w, Y, _, _ in fs if w == 2)
    out["SU(3)^2 U(1)_Y"] = sum((m // 3) * Y for n, m, c, w, Y, _, _ in fs if c == 3)
    sign = {"Q": 1, "u^c": -1, "d^c": -1}
    out["SU(3)^3"] = sum((m // 3) * sign[n] for n, m, c, w, Y, _, _ in fs if c == 3)
    out["Witten SU(2) (doublets mod 2)"] = sum(m // 2 for n, m, c, w, Y, _, _ in fs if w == 2) % 2
    X = [(5 * (B - Lq) - 4 * Y) for _, m, _, _, Y, B, Lq in fs for _ in range(m)]
    out["X = 5(B-L)-4Y mod 4 (each Weyl)"] = sorted(set(int(x % 4) for x in X))
    out["Z16: Weyl count mod 16"] = len(X) % 16
    return out


print("1. ANOMALIES OF ONE GENERATION (the mirror copy has the same, sign-flipped)")
for inc in (False, True):
    a = anomalies(inc)
    print(f"   {'with' if inc else 'WITHOUT'} right-handed neutrino ({sum(f[1] for f in fields if inc or f[0] != 'nu^c')} Weyl fermions):")
    for k, v in a.items():
        print(f"      {k:34s} {v}")
print("   -> all perturbative gauge anomalies cancel either way, but the Z16 count (spin-Z4 symmetry X) is 15 without nu^c")
print("      and 0 with it: a mirror generation can be gapped symmetrically (keeping X) ONLY if it has 16 Weyl fermions.\n")

# ------------------------------------------------------------------ 2. SMG by exact diagonalisation


def majoranas(n):
    m = n // 2
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]])
    sz = np.diag([1.0, -1.0]).astype(complex)
    I = np.eye(2)
    ops = []
    for j in range(m):
        for s in (sx, sy):
            mats = [sz] * j + [s] + [I] * (m - j - 1)
            o = mats[0]
            for x in mats[1:]:
                o = np.kron(o, x)
            ops.append(o)
    return ops


rng = np.random.default_rng(5)
print("2. SYMMETRIC MASS GENERATION, exact: n Majoranas, T forbids all bilinear masses, random T-symmetric quartic terms")
for n in (4, 8, 12, 16):
    g = majoranas(n)
    quads = list(itertools.combinations(range(n), 4))
    T_even_real = True
    uniq, gaps = 0, []
    trials = 40 if n < 16 else 12
    for _ in range(trials):
        sel = quads if len(quads) <= 300 else [quads[i] for i in rng.choice(len(quads), 300, replace=False)]
        H = np.zeros_like(g[0])
        for (a, b, c, d) in sel:
            H = H + rng.normal() * (g[a] @ g[b] @ g[c] @ g[d])
        # time reversal T': gamma_i -> gamma_i (all), i -> -i.  Every quartic product with a REAL coefficient is
        # T'-even (all allowed); every bilinear i gamma_a gamma_b is T'-odd (all forbidden).  H is Hermitian as built.
        e = np.linalg.eigvalsh(H)
        deg = int(np.sum(np.abs(e - e[0]) < 1e-9))
        uniq += deg == 1
        gaps.append(e[deg] - e[0])
    print(f"   n = {n:2d} Majoranas ({n // 2} complex fermions): unique gapped ground state in {uniq}/{trials} random cases;"
          f" typical gap {np.median(gaps):.2f}")
print("   -> interactions alone (no bilinear masses) give a unique gapped state only for n = 8, 16 (multiples of 8):")
print("      the Fidkowski-Kitaev 'mod 8' rule, the low-dimensional analogue of '16 Weyl per generation' in 3+1-d.")
