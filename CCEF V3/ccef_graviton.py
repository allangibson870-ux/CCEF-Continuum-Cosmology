#!/usr/bin/env python3
"""
ccef_graviton.py  --  which emergent tensor field on the grains gives exactly a graviton?

Field: symmetric spatial tensor h_ij (6 components) with conjugate 'electric' tensor E_ij, lattice energy
H = sum E_ij^2 / 2 + V[h] (positive kinetic term, as any grain model has).  Gauge redundancies = Gauss laws on E.
For a plane wave of wavevector K: physical modes = orthogonal complement of the gauge directions; omega^2 = eigenvalues
of V there.  General first-derivative (relativistic-candidate) potential:
   V = a K^2 (h.h) + b |K.h|^2 + c (K.h.K) tr h + d K^2 (tr h)^2
Candidate symmetries:
   DIFF  : h -> h + K xi + xi K   (all 3 xi)        -> linearised GR (Fierz-Pauli) family
   TDIFF+WEYL : transverse xi (K.xi = 0) plus Weyl h -> h + phi*1   (unimodular / WTDiff: volume fixed)
   DIFF+WEYL  : both
For each: invariant potentials, physical modes, helicity (spin about K), stability (omega^2 > 0), dispersion.
"""

import itertools

import numpy as np

rng = np.random.default_rng(2)


def sym_basis():
    B = []
    for i in range(3):
        M = np.zeros((3, 3)); M[i, i] = 1; B.append(M)
    for i, j in ((0, 1), (0, 2), (1, 2)):
        M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1 / np.sqrt(2); B.append(M)
    return B


BAS = sym_basis()


def terms(h, K):
    Kh = K @ h
    return np.array([K @ K * np.sum(h * h), Kh @ Kh, (K @ h @ K) * np.trace(h), K @ K * np.trace(h) ** 2])


def gauge_dirs(K, kind):
    dirs = []
    if kind in ("DIFF", "DIFF+WEYL"):
        for e in np.eye(3):
            dirs.append(np.outer(K, e) + np.outer(e, K))
    if kind == "TDIFF+WEYL":
        n = K / np.linalg.norm(K)
        t1 = np.cross(n, [1, 0, 0] if abs(n[0]) < 0.9 else [0, 1, 0]); t1 /= np.linalg.norm(t1)
        t2 = np.cross(n, t1)
        for e in (t1, t2):
            dirs.append(np.outer(K, e) + np.outer(e, K))
    if "WEYL" in kind:
        dirs.append(np.eye(3))
    return dirs


def invariant_potentials(kind):
    """coefficient vectors (a,b,c,d) with V(h + g) = V(h) for all h and gauge g (quadratic form: cross term = 0)"""
    rows = []
    for _ in range(30):
        K = rng.normal(size=3)
        h = sum(rng.normal() * b for b in BAS)
        for g in gauge_dirs(K, kind):
            # V is quadratic: V(h+g) - V(h) - V(g) = 2 B(h, g) must vanish and V(g) must vanish
            cross = (terms(h + g, K) - terms(h, K) - terms(g, K))
            rows.append(cross)
            rows.append(terms(g, K))
    _, s, vt = np.linalg.svd(np.array(rows))
    null = vt[np.sum(s > 1e-9 * s[0]):]
    return null


def quad_matrix(coef, K):
    n = len(BAS)
    Q = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            vi = terms(BAS[i] + BAS[j], K) - terms(BAS[i], K) - terms(BAS[j], K)
            Q[i, j] = 0.5 * coef @ vi if i != j else coef @ terms(BAS[i], K)
    return Q


def modes(coef, K, kind):
    G = np.array([[np.sum(g * b) for b in BAS] for g in gauge_dirs(K, kind)])
    _, s, vt = np.linalg.svd(G)
    phys = vt[np.sum(s > 1e-10):]                     # orthonormal physical subspace (components in BAS)
    Q = quad_matrix(coef, K)
    w2, vecs = np.linalg.eigh(phys @ Q @ phys.T)
    out = []
    n = K / np.linalg.norm(K)
    for k in range(len(w2)):
        hk = sum(c * b for c, b in zip(phys.T @ vecs[:, k], BAS))
        # helicity: rotate about K by angle phi; amplitude picks up cos(s phi). Measure |s| via overlap after rotation
        phi = 0.3
        ax = n
        Kx = np.array([[0, -ax[2], ax[1]], [ax[2], 0, -ax[0]], [-ax[1], ax[0], 0]])
        R = np.eye(3) + np.sin(phi) * Kx + (1 - np.cos(phi)) * Kx @ Kx
        hr = R @ hk @ R.T
        ov = np.sum(hr * hk) / np.sum(hk * hk)
        s = min((0, 1, 2), key=lambda s: abs(np.cos(s * phi) - ov))
        out.append((w2[k], s))
    return out


print("Physical (freely moving) modes of an emergent symmetric tensor on the grains, plane wave K, |K| = 1 and 2")
for kind in ("DIFF", "TDIFF+WEYL", "DIFF+WEYL"):
    null = invariant_potentials(kind)
    print(f"\n{kind}: {len(null)} independent first-derivative potentials invariant under it")
    if len(null) == 0:
        print("   none -> no relativistic (k^2) energy exists; only higher-derivative (non-relativistic) dynamics")
        continue
    for v in null:
        v = v / v[np.argmax(np.abs(v))] * (0.25 if v[0] != 0 else 1)
        if abs(v[0]) > 1e-9:
            v = v / v[0] * 0.25
        print(f"   potential (a, b, c, d) = {np.round(v, 4)}")
        K = rng.normal(size=3); K /= np.linalg.norm(K)
        m1 = modes(v, K, kind)
        m2 = modes(v, 2 * K, kind)
        for (w, s), (w2_, _) in zip(m1, m2):
            disp = "static (omega = 0: a constraint, not a wave)" if abs(w) < 1e-9 else \
                ("UNSTABLE (omega^2 < 0)" if w < 0 else f"wave, omega^2 grows x{w2_ / w:.0f} when k doubles -> omega ~ k")
            print(f"      helicity {s}: omega^2 = {w:+.3f}  -> {disp}")
