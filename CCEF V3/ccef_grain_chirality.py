#!/usr/bin/env python3
"""
ccef_grain_chirality.py  --  do the grain junctions spontaneously pick ONE handedness (spontaneous CP violation)
as the network cools through the light/matter switch-on?

Model: the grains' light sector = spin-1/2 XXZ on the pyrochlore lattice (grains = bonds of the diamond junction
graph), H = Jzz sum Sz Sz - Jpm sum (S+ S- + h.c.) over pairs of grains sharing a junction (equivalent to the
Gauss-law + exchange terms of the grain Hamiltonian).  16-grain periodic cluster (8 junctions), Sz = 0 sector.
Jpm > 0: unfrustrated (0-flux quantum spin ice);  Jpm < 0: frustrated (pi-flux); Jpm = -0.5: Heisenberg antiferromagnet.

Observable: junction chirality chi_t = sum over the 4 faces of S_i.(S_j x S_k), faces oriented by outward normals
(C-even, P-odd, T-odd = CP-odd).  Chiral structure factor  S_chi = <X^2> / (N_t <chi_t^2>),  X = sum_t chi_t:
  ~1 -> junction handedness uncorrelated (no spontaneous CP violation);  -> N_t = 8 -> all junctions share a handedness.
Ground state: exact (Lanczos).  Temperature: microcanonical thermal pure quantum states (mTPQ), 6 random vectors.
"""

import itertools
import sys
import time
from multiprocessing import Pool

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

DELTAS = np.array([(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)])
BOX = 4


def cluster():
    A = [np.array(r) for r in [(0, 0, 0), (0, 2, 2), (2, 0, 2), (2, 2, 0)]]
    grains, pos = [], []
    junA = {k: [] for k in range(4)}
    junB = {}
    for a, r in enumerate(A):
        for d in DELTAS:
            g = len(grains)
            b = tuple((r + d) % BOX)
            grains.append((a, b))
            pos.append(r + d / 2.0)                    # bond midpoint (unwrapped from its A end)
            junA[a].append(g)
            junB.setdefault(b, []).append(g)
    juns = [(np.array(A[a], float), gs) for a, gs in junA.items()] + \
           [(np.array(b, float), gs) for b, gs in junB.items()]
    return len(grains), np.array(pos), juns


N, POS, JUNS = cluster()
DIM = 2 ** N
sx = sp.csr_matrix(np.array([[0, 1], [1, 0]], dtype=complex))
sy = sp.csr_matrix(np.array([[0, -1j], [1j, 0]]))
sz = sp.csr_matrix(np.array([[1, 0], [0, -1]], dtype=complex))


def site_op(o, i):
    return sp.kron(sp.kron(sp.identity(2 ** i, format="csr"), o), sp.identity(2 ** (N - 1 - i), format="csr"), format="csr")


Sx = [0.5 * site_op(sx, i) for i in range(N)]
Sy = [0.5 * site_op(sy, i) for i in range(N)]
Sz = [0.5 * site_op(sz, i) for i in range(N)]
popcount = np.array([bin(s).count("1") for s in range(DIM)])
SECTOR = np.nonzero(popcount == N // 2)[0]


def restrict(M):
    return M[SECTOR][:, SECTOR].tocsr()


def min_image(d):
    return (d + BOX / 2) % BOX - BOX / 2


def junction_chirality(center, gs):
    out = None
    for f in itertools.combinations(gs, 3):
        i, j, k = f
        ri, rj, rk = (center + min_image(POS[x] - center) for x in f)
        nrm = np.cross(rj - ri, rk - ri)
        if np.dot(nrm, (ri + rj + rk) / 3 - center) < 0:
            j, k = k, j
        a = (Sx[i], Sy[i], Sz[i])
        b = (Sx[j], Sy[j], Sz[j])
        c = (Sx[k], Sy[k], Sz[k])
        term = a[0] @ (b[1] @ c[2] - b[2] @ c[1]) + a[1] @ (b[2] @ c[0] - b[0] @ c[2]) + a[2] @ (b[0] @ c[1] - b[1] @ c[0])
        out = term if out is None else out + term
    return restrict(out)


CHI = [junction_chirality(c, gs) for c, gs in JUNS]
X = sum(CHI)
X2 = (X @ X).tocsr()
# staggered: A-type (up) junctions minus B-type (down).  Inversion maps A<->B and flips chi, so a staggered pattern
# (chi_A = -chi_B) is P-EVEN and T-odd -> CP-even: it does not bias matter vs antimatter.
Y = sum(CHI[:4]) - sum(CHI[4:])
Y2 = (Y @ Y).tocsr()
CHI2 = sum((c @ c) for c in CHI).tocsr() / len(CHI)
PAIRS = [(i, j) for (c, gs) in JUNS for i, j in itertools.combinations(gs, 2)]


def hamiltonian(Jpm, Jzz=1.0):
    H = None
    for i, j in PAIRS:
        t = Jzz * Sz[i] @ Sz[j] - Jpm * 2 * (Sx[i] @ Sx[j] + Sy[i] @ Sy[j])     # S+S- + h.c. = 2(SxSx + SySy)
        H = t if H is None else H + t
    return restrict(H)


def run(Jpm):
    t0 = time.time()
    H = hamiltonian(Jpm)
    e, v = eigsh(H, k=8, which="SA")
    order = np.argsort(e)
    e, v = e[order], v[:, order]
    deg = int(np.sum(e - e[0] < 1e-8))
    G = v[:, :deg]
    chi2_g = np.real(np.trace(G.conj().T @ (CHI2 @ G))) / deg
    X2_g = np.real(np.trace(G.conj().T @ (X2 @ G))) / deg
    Y2_g = np.real(np.trace(G.conj().T @ (Y2 @ G))) / deg
    Xeig = np.linalg.eigvalsh(G.conj().T @ (X @ G)) if deg > 1 else np.array([np.real(G[:, 0].conj() @ (X @ G[:, 0]))])
    # mTPQ: |k+1> = (l - H/N)|k>, temperature from energy density
    rng = np.random.default_rng(1)
    lmax = abs(e[0]) / N * 4 + 1.0
    curves = []
    for _ in range(6):
        psi = rng.normal(size=H.shape[0]) + 1j * rng.normal(size=H.shape[0])
        psi /= np.linalg.norm(psi)
        pts = []
        for k in range(1, 1201):
            psi = lmax * psi - (H @ psi) / N
            psi /= np.linalg.norm(psi)
            if k % 10 == 0:
                u = np.real(psi.conj() @ (H @ psi)) / N
                pts.append((k, u, np.real(psi.conj() @ (X2 @ psi)), np.real(psi.conj() @ (CHI2 @ psi)),
                            np.real(psi.conj() @ (Y2 @ psi))))
        curves.append(pts)
    rows = []
    for idx in range(len(curves[0])):
        k = curves[0][idx][0]
        u = np.mean([c[idx][1] for c in curves])
        x2 = np.mean([c[idx][2] for c in curves])
        c2 = np.mean([c[idx][3] for c in curves])
        y2 = np.mean([c[idx][4] for c in curves])
        T = N * (lmax - u) / (2 * k) if k > 0 else np.inf
        rows.append((T, u, x2 / (len(CHI) * c2), y2 / (len(CHI) * c2)))
    return Jpm, e[:6], deg, (X2_g / (len(CHI) * chi2_g), Y2_g / (len(CHI) * chi2_g), chi2_g), Xeig, rows, time.time() - t0


if __name__ == "__main__":
    vals = [float(x) for x in sys.argv[1:]] or [0.05, -0.05, -0.15, -0.5]
    print(f"cluster: {N} grains, {len(JUNS)} junctions, Sz=0 sector dim {len(SECTOR)}")
    with Pool(min(4, len(vals))) as pool:
        res = pool.map(run, vals)
    for Jpm, e, deg, Sg, Xeig, rows, dt in res:
        Jring = 12 * abs(Jpm) ** 3
        print(f"\nJpm = {Jpm:+.2f} (ring scale ~ {Jring:.1e})  [{dt:.0f}s]")
        print(f"   lowest energies {np.round(e, 4)}; ground degeneracy {deg}")
        SU, SS, c2 = Sg
        print(f"   ground state: <chi_t^2> = {c2:.3f}; UNIFORM (CP-odd) S = {SU:.2f}; STAGGERED (CP-even) S = {SS:.2f}"
              f"   (1 = uncorrelated, 8 = all junctions locked)")
        print(f"   uniform chirality X within ground space: {np.round(Xeig, 3)}")
        sel = [r for r in rows if np.isfinite(r[0])]
        for target in (2.0, 0.5, 0.2, 0.1, 0.05, 0.02):
            r = min(sel, key=lambda r: abs(np.log(r[0] / target)))
            print(f"   T ~ {r[0]:.3f}: uniform S = {r[2]:.2f}, staggered S = {r[3]:.2f}")
