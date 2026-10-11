#!/usr/bin/env python3
"""
ccef_grain_fermion_fluxsearch.py  --  which 0/pi flux patterns (periodic with one conventional cube, 8 junctions)
give the junction fermions isolated relativistic Dirac points instead of nodal lines?

All 2^16 sign patterns on the 16 grains of the cell; gauge-equivalent ones (sign flips on junctions) share a spectrum,
so one representative per class is classified.  Classifier on k-grids of n = 16 and 32 per side:
   count k-points with min|E| < 2.5 * (grid spacing) * t*bond-scale:  points -> count ~ const; lines -> ~ n; gap -> 0
then the promising classes are refined: exact zeros by minimisation, multiplicity, shape (Hessian), cone speeds.
"""

import itertools
import os
from multiprocessing import Pool

import numpy as np
from scipy.optimize import minimize

from ccef_grain_fermion_nodes import DELTAS, cell, bloch_factory

P = 4
A = cell(P)
nA = len(A)
idx = {tuple(r): i for i, r in enumerate(A)}
EDGE_B = [nA + idx[tuple((r + d - 1) % P)] for r in A for d in DELTAS]
EDGE_A = [i for i in range(nA) for _ in range(4)]
G = 2 * np.pi / P


def canonical(bits):
    """gauge-fix: flip junction signs so that a spanning set of edges is +; return a class key"""
    s = np.array(bits)
    best = None
    for flips in itertools.product((0, 1), repeat=2 * nA - 1):
        f = np.r_[0, flips]
        t = s ^ f[EDGE_A] ^ f[EDGE_B]
        key = tuple(t)
        if best is None or key < best:
            best = key
    return best


DVEC = np.array([d for r in A for d in DELTAS], dtype=float)


def batch_min_abs_E(s, K):
    """min |E| at each k in K (vectorised Bloch Hamiltonians)"""
    Hb = np.zeros((len(K), 2 * nA, 2 * nA), dtype=complex)
    ph = np.exp(1j * K @ DVEC.T)                           # (nk, 16)
    for e in range(16):
        i, j = EDGE_A[e], EDGE_B[e]
        Hb[:, i, j] += -s[e] * ph[:, e]
        Hb[:, j, i] += -s[e] * np.conj(ph[:, e])
    return np.min(np.abs(np.linalg.eigvalsh(Hb)), axis=1)


def classify(bits):
    s = np.where(np.array(bits) == 1, -1.0, 1.0)
    res = {}
    for n in (16, 32):
        g = np.linspace(0, G, n, endpoint=False) + G / (2 * n)
        K = np.array(list(itertools.product(g, g, g)))
        res[n] = int(np.sum(batch_min_abs_E(s, K) < 2.5 * G / n))
    return bits, res


if __name__ == "__main__":
    os.environ["OMP_NUM_THREADS"] = "1"
    # gauge classes: enumerate patterns, keep those whose canonical form is themselves (cheap: use flux signature instead)
    # flux signature = product of signs around each independent cycle; classes <-> signatures
    import ccef_grain_fermion_nodes as nd
    reps = {}
    for bits in itertools.product((0, 1), repeat=16):
        b = np.array(bits)
        # gauge fix quickly: force signs on a spanning tree (A0 to all its 4 B's, and each B to one A) to be +
        f = np.zeros(2 * nA, dtype=int)
        order = [0]
        seen = {0}
        # BFS over the cell graph setting junction flips to make tree edges +
        nbr = {}
        for e, (a, bb) in enumerate(zip(EDGE_A, EDGE_B)):
            nbr.setdefault(a, []).append((bb, e))
            nbr.setdefault(bb, []).append((a, e))
        while order:
            u = order.pop(0)
            for w, e in nbr[u]:
                if w not in seen:
                    seen.add(w)
                    f[w] = f[u] ^ b[e]
                    order.append(w)
        key = tuple(b ^ f[np.array(EDGE_A)] ^ f[np.array(EDGE_B)])
        reps.setdefault(key, bits)
    print(f"{len(reps)} gauge classes of 0/pi flux patterns on the 8-junction cell", flush=True)
    with Pool(4) as pool:
        out = pool.map(classify, list(reps.values()), chunksize=8)
    kinds = {"gapped": [], "points": [], "lines/surfaces": []}
    for bits, r in out:
        if r[32] == 0:
            kinds["gapped"].append(bits)
        elif r[32] <= 1.5 * r[16]:
            kinds["points"].append((bits, r))
        else:
            kinds["lines/surfaces"].append(bits)
    print(f"classification: gapped {len(kinds['gapped'])}, point-like {len(kinds['points'])}, "
          f"line/surface {len(kinds['lines/surfaces'])}")
    rng = np.random.default_rng(3)
    shown = 0
    for bits, r in kinds["points"]:
        s = np.where(np.array(bits) == 1, -1.0, 1.0)
        H = bloch_factory(P, s, A)
        emin = lambda kv: np.min(np.abs(np.linalg.eigvalsh(H(np.asarray(kv)))))
        zeros = []
        for _ in range(60):
            rr = minimize(emin, rng.uniform(0, G, 3), method="Nelder-Mead",
                          options={"xatol": 1e-10, "fatol": 1e-12, "maxiter": 4000})
            if rr.fun < 1e-5:
                k = np.mod(rr.x, G)
                if all(np.linalg.norm(np.angle(np.exp(1j * (k - z) * P))) > 1e-3 for z in zeros):
                    zeros.append(k)
        desc = []
        for k in zeros:
            mult = int(np.sum(np.abs(np.linalg.eigvalsh(H(k))) < 1e-4))
            h = 1e-4
            f2 = lambda x: emin(x) ** 2
            Hs = np.array([[(f2(k + h * a + h * b) - f2(k + h * a - h * b) - f2(k - h * a + h * b) + f2(k - h * a - h * b))
                            / (4 * h * h) for b in np.eye(3)] for a in np.eye(3)])
            hev = np.sort(np.linalg.eigvalsh(Hs))
            desc.append((np.round(k / G, 3), mult, np.round(np.sqrt(np.maximum(hev, 0)) / np.sqrt(3), 3)))
        nflux = int(np.sum(np.array(bits)))
        print(f"\n point-node class (minus signs on {nflux}/16 grains; grid counts {r}): {len(zeros)} zero points")
        for k, mult, v in desc:
            print(f"   k = {k} (cell-BZ units): E=0 multiplicity {mult}, cone speeds v/(t*bond) = {v}")
        shown += 1
        if shown >= 4:
            break
