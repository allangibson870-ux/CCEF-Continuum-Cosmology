#!/usr/bin/env python3
"""
ccef_induced_gravity.py  --  coarse-graining the geometry events: where does Einstein gravity's stiffness come from?

B1. COORDINATE FREEDOM AT LARGE SCALE: slip a whole plane of space by a lattice vector (every grain crossing the
    plane is rewired) -> energy change?  (a relational universe should not care: it is a relabelling)
B2. NO ELASTICITY: two geometry defects (flux-allowed switches) at graph distance d -> interaction energy
    E12 - E1 - E2 + E0.  In a crystal of atoms, defects interact through long-range strain (~1/d^3); a relational graph
    has no positions, so any interaction must be contact-only.
    => the bare geometry energy coarse-grains to (core energy) x (number of defects): no Fierz-Pauli (Einstein) term.
B3. STIFFNESS FROM THE FIELDS ON THE GRAINS (Sakharov / Jacobson): entanglement area law S = eta_g A / l^2 of
    (i) a massless scalar on the junctions (proxy for one photon polarisation),
    (ii) the grain electron (spin-1/2 Fu-Kane-Mele, three 4-component Dirac cones at X),
    computed exactly for Gaussian states on the diamond lattice (slab cut, transverse momenta, two cuts).
    Jacobson: area law + local equilibrium -> Einstein's equations with G = l^2 / (4 eta_g).  CCEF assumed
    eta_g = N_eff / (24 pi) with N_eff ~ 9 (eta_g = 0.119).  Compare.
"""

import contextlib
import io
import itertools
import time

import numpy as np

from ccef_geo_dynamics import Graph2
from ccef_grain_hamiltonian_mc import diamond

T0 = time.time()

# ================================================================ geometry part (angle-rule energy K=1, U=8, W=4)
L = 3
N, EDGES = diamond(L)
BOX = 4 * L
n = N // 2
A_POS = [(x, y, z) for x in range(0, BOX, 2) for y in range(0, BOX, 2) for z in range(0, BOX, 2) if (x + y + z) % 4 == 0]
POS = A_POS + [tuple((c + 1) % BOX for c in p) for p in A_POS]
IDX = {p: i for i, p in enumerate(POS)}


def energy(edges):
    g = Graph2(N, edges, 1, 8, 4)
    perf = sum(g.full_stats(v) == (0, 12, 0, 0) for v in range(N))
    return g.E, perf


E0, P0 = energy(EDGES)
print(f"diamond universe {N} junctions, {len(EDGES)} grains: E/N = {E0 / N:+.3f}, perfect junctions {P0}/{N}\n")

# ---------------------------------------------------------------- B1: slip a plane
b = np.array([2, 2, 0])
new = []
moved = 0
for a, bb in EDGES:
    pa, pb = POS[a], POS[bb]
    if pa[2] == 4 and pb[2] == 5:                          # A below the plane, B above: move the upper end by +b
        q = tuple((np.array(pb) + b) % BOX)
        new.append((a, IDX[q]))
        moved += 1
    elif pa[2] == 5 and pb[2] == 4:                        # A above, B below: equivalently move the lower end by -b
        q = tuple((np.array(pb) - b) % BOX)
        new.append((a, IDX[q]))
        moved += 1
    else:
        new.append((a, bb))
E1, P1 = energy(new)
deg = np.bincount([x for e in new for x in e], minlength=N)
print("B1. SLIP A WHOLE PLANE OF SPACE by a lattice vector (2,2,0)")
print(f"    grains rewired: {moved} ({100 * moved / len(EDGES):.0f}% of all grains); every junction still has 4: "
      f"{bool(np.all(deg == 4))}")
print(f"    energy change {E1 - E0:+.3f}; perfect junctions {P1}/{N}")
print("    -> a large rewiring with zero cost: it is a change of coordinates (a large diffeomorphism), not physics\n")

# ---------------------------------------------------------------- B2: defect-defect interaction
adj0 = [set() for _ in range(N)]
for a, bb in EDGES:
    adj0[a].add(bb)
    adj0[bb].add(a)
eid = {e: k for k, e in enumerate(EDGES)}
cands = set()
for a in range(n):
    for e in adj0[a]:
        for c in adj0[e]:
            if c == a:
                continue
            for bb in adj0[a] - {e}:
                for d in adj0[c] - {e}:
                    cands.add(tuple(sorted((eid[(a, bb)], eid[(c, d)]))))
cands = sorted(cands)


def switched(edges, pairs):
    ed = list(edges)
    for i, j in pairs:
        (a, bb), (c, d) = ed[i], ed[j]
        ed[i], ed[j] = (a, d), (c, bb)
    return ed


def bfs(src):
    dist = {s: 0 for s in src}
    fr = list(src)
    while fr:
        nx = []
        for x in fr:
            for y in adj0[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1
                    nx.append(y)
        fr = nx
    return dist


def anchors(p):
    return {x for k in p for x in EDGES[k]}


rng = np.random.default_rng(3)
s1 = cands[0]
d1 = bfs(anchors(s1))
Es1 = energy(switched(EDGES, [s1]))[0] - E0
byd = {}
for s2 in [cands[i] for i in rng.permutation(len(cands))[:900]]:
    if set(s2) & set(s1):
        continue
    dd = min(d1[x] for x in anchors(s2))
    if len(byd.get(dd, [])) >= 12:
        continue
    ed12 = switched(EDGES, [s1, s2])
    if len(set(ed12)) < len(ed12):
        continue                                           # would create a double link
    E2 = energy(switched(EDGES, [s2]))[0] - E0
    E12 = energy(ed12)[0] - E0
    byd.setdefault(dd, []).append(E12 - Es1 - E2)
print("B2. DO GEOMETRY DEFECTS FEEL EACH OTHER AT A DISTANCE?")
print(f"    one switch defect costs {Es1:+.1f} (geometry units)")
for dd in sorted(byd):
    v = np.array(byd[dd])
    print(f"    defects {dd} steps apart: {len(v):2d} pairs, interaction energy  max |I| = {np.abs(v).max():.2f}"
          f"  (mean {v.mean():+.2f})")
print("    -> contact interaction only, nothing beyond a few steps: the bare geometry has NO elasticity, so it cannot")
print("       produce the long-range (Einstein / Fierz-Pauli) stiffness by itself\n")

# ================================================================ B3: entanglement area law of fields on the grains
with contextlib.redirect_stdout(io.StringIO()):
    import ccef_strong_cp as scp
CELL_A = [np.array(p) for p in ((0, 0, 0), (0, 2, 2), (2, 0, 2), (2, 2, 0))]
SITES = [(0, p) for p in CELL_A] + [(1, p + 1) for p in CELL_A]          # (sublattice, position) in a cube of side 4


def bloch_chain(terms, nspin, kx, ky, Lz):
    """H for a column of Lz conventional cells (periodic in z), Bloch phases kx, ky across the x, y faces"""
    ns = len(SITES)
    box = np.array([4, 4, 4 * Lz])
    allsites = {}
    for cz in range(Lz):
        for s, (sub, p) in enumerate(SITES):
            allsites[tuple((p + np.array([0, 0, 4 * cz])) % box)] = (cz * ns + s, sub)
    dim = ns * Lz * nspin
    H = np.zeros((dim, dim), dtype=complex)
    for x, (ix, sub) in allsites.items():
        for a, bsub, d, T in terms:
            if a != sub:
                continue
            y = np.array(x) + d
            ym = y % box
            w = y - ym
            iy, suby = allsites[tuple(ym)]
            assert suby == bsub
            ph = np.exp(1j * (kx * w[0] + ky * w[1]))
            blk = np.atleast_2d(T) * ph
            H[ix * nspin:(ix + 1) * nspin, iy * nspin:(iy + 1) * nspin] += blk
            H[iy * nspin:(iy + 1) * nspin, ix * nspin:(ix + 1) * nspin] += blk.conj().T
    return H


def region_idx(Lz, nspin):
    ns = len(SITES)
    return np.arange(ns * (Lz // 2) * nspin)


def S_fermion(kx, ky, Lz, terms):
    H = bloch_chain(terms, 2, kx, ky, Lz)
    w, V = np.linalg.eigh(H)
    occ = V[:, w < 0]
    r = region_idx(Lz, 2)
    C = occ[r] @ occ[r].conj().T
    nu = np.clip(np.linalg.eigvalsh(C), 1e-14, 1 - 1e-14)
    return float(-np.sum(nu * np.log(nu) + (1 - nu) * np.log(1 - nu))), int(np.sum(w < 0)), H.shape[0]


SCALAR_TERMS = [(0, 1, d, np.array([[-1.0]])) for d in scp.DEL]


def S_scalar(kx, ky, Lz):
    Hhop = bloch_chain(SCALAR_TERMS, 1, kx, ky, Lz)
    K = 4 * np.eye(Hhop.shape[0]) + Hhop                   # graph Laplacian (4 - adjacency) as the spring matrix
    w, V = np.linalg.eigh(K)
    X = (V / np.sqrt(w)) @ V.conj().T / 2
    P = (V * np.sqrt(w)) @ V.conj().T / 2
    r = region_idx(Lz, 1)
    ev = np.linalg.eigvals(X[np.ix_(r, r)] @ P[np.ix_(r, r)]).real
    nu = np.sqrt(np.clip(ev, 0.25 + 1e-15, None))
    return float(np.sum((nu + .5) * np.log(nu + .5) - (nu - .5) * np.log(nu - .5)))


def eta(fn, nk, Lz):
    ks = (np.arange(nk) + 0.5) / nk * 2 * np.pi / 4 - np.pi / 4  # conventional-cell zone, offset grid
    tot = sum(fn(kx, ky, Lz) for kx in ks for ky in ks)
    area = 2 * 16 * nk * nk                                 # two cuts, transverse area 16 per k-point
    return tot / area * 3.0                                 # per grain length squared (l^2 = 3)


terms_e = scp.base_terms(0.25)
_, nocc, dim = S_fermion(0.1, 0.2, 4, terms_e)
print("B3. ENTANGLEMENT AREA LAW of the fields living on the grains (slab cut; exact Gaussian states)")
print(f"    grain electron chain check: {nocc} of {dim} states filled (half filling)")
for nk, Lz in ((6, 6), (10, 8), (14, 10)):
    es = eta(S_scalar, nk, Lz)
    ef = eta(lambda kx, ky, Lz: S_fermion(kx, ky, Lz, terms_e)[0], nk, Lz)
    print(f"    transverse {nk}x{nk} cells, depth {Lz}: eta_g(scalar) = {es:.4f}   eta_g(grain electron) = {ef:.4f}")
NEFF_S, NEFF_F = 24 * np.pi * es, 24 * np.pi * ef
print(f"    as N_eff = 24 pi eta_g:  one scalar (one photon polarisation) {NEFF_S:.2f};  grain electron {NEFF_F:.2f}")
print(f"    CCEF assumed N_eff ~ 9 (eta_g = 0.119)")
print(f"    photon (2 polarisations) + grain electron: N_eff = {2 * NEFF_S + NEFF_F:.2f}")
print(f"\ntotal {time.time() - T0:.0f} s")
