#!/usr/bin/env python3
"""
ccef_nonabelian.py  --  the weak (SU(2)) and strong (SU(3)) forces from grains: rishon quantum-link construction.

Chain: grains -> fermions (Bravyi-Kitaev / Jordan-Wigner, CCEF_grain_electrons.md) -> RISHONS: N 'colour' fermion
modes at each end of every relation (link).  Link field U^{ab}_{xy} = c_{x,a} c_{y,b}^dagger (Chandrasekharan-Wiese
quantum links).  Gauss-law generators at a junction x:  G^a_x = sum_{rishon ends and matter at x} c^dagger T^a c.
Checks (exact, sparse matrices):
  1. Lie algebra at a junction: [G^a, G^b] = i f^{abc} G^c  for SU(2) and SU(3)
  2. gauge invariance: matter hopping  psi_x^dag U_xy psi_y + h.c.  and the plaquette  tr(U12 U23 U34 U41) + h.c.
     commute with every G^a_x
  3. SU(2) plaquette: gauge-invariant sector (fixed rishon number per link, colour singlet at every junction),
     spectrum of  H = -J (tr U_p + h.c.)
  4. grains per relation needed to reach the real weak/strong couplings (heuristic truncation estimate)
"""

import itertools
import math
import time

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

t0 = time.time()


def fermion_ops(M):
    """Jordan-Wigner annihilation operators for M modes (sparse)"""
    Z = sp.csr_matrix(np.diag([1.0, -1.0]))
    a = sp.csr_matrix(np.array([[0.0, 1.0], [0.0, 0.0]]))
    I = sp.identity(2, format="csr")
    ops = []
    for k in range(M):
        mats = [Z] * k + [a] + [I] * (M - k - 1)
        o = mats[0]
        for m in mats[1:]:
            o = sp.kron(o, m, format="csr")
        ops.append(o)
    return ops


def gens(N):
    if N == 2:
        s = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
        return [x / 2 for x in s]
    l = np.zeros((8, 3, 3), dtype=complex)
    l[0][0, 1] = l[0][1, 0] = 1
    l[1][0, 1], l[1][1, 0] = -1j, 1j
    l[2][0, 0], l[2][1, 1] = 1, -1
    l[3][0, 2] = l[3][2, 0] = 1
    l[4][0, 2], l[4][2, 0] = -1j, 1j
    l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2], l[6][2, 1] = -1j, 1j
    l[7] = np.diag([1, 1, -2]) / math.sqrt(3)
    return [x / 2 for x in l]


def bilinear(c, idx, T):
    """sum_ab c^dag_{idx[a]} T_ab c_{idx[b]}"""
    out = None
    for a in range(len(idx)):
        for b in range(len(idx)):
            if abs(T[a, b]) > 1e-14:
                term = T[a, b] * (c[idx[a]].getH() @ c[idx[b]])
                out = term if out is None else out + term
    return out


def comm_norm(A, B):
    C = A @ B - B @ A
    return 0.0 if C.nnz == 0 else float(np.abs(C.data).max())


# ---------------------------------------------------------------- 1 + 2a: one link between two junctions, with matter
for N in (2, 3):
    T = gens(N)
    # modes: matter at x (N), rishons at x-end (N), rishons at y-end (N), matter at y (N)
    M = 4 * N
    c = fermion_ops(M)
    mx, rx, ry, my = [list(range(k * N, (k + 1) * N)) for k in range(4)]
    Gx = [bilinear(c, mx, t) + bilinear(c, rx, t) for t in T]
    Gy = [bilinear(c, my, t) + bilinear(c, ry, t) for t in T]
    # structure constants via the matrices
    f_err = 0.0
    for a, b in itertools.combinations(range(len(T)), 2):
        cm = T[a] @ T[b] - T[b] @ T[a]
        coeffs = [2 * np.trace(cm @ T[k]) for k in range(len(T))]          # [T^a,T^b] = sum_k coeffs_k T^k
        lhs = Gx[a] @ Gx[b] - Gx[b] @ Gx[a]
        rhs = sum(coeffs[k] * Gx[k] for k in range(len(T)) if abs(coeffs[k]) > 1e-12)
        f_err = max(f_err, float(np.abs((lhs - rhs).data).max()) if (lhs - rhs).nnz else 0.0)
    hop = None
    for a in range(N):
        for b in range(N):
            # psi_x^dag U^{ab} psi_y with U^{ab} = c_{x,a} c_{y,b}^dag  -> colour-singlet at each junction
            pass
    hop = sum(c[mx[a]].getH() @ c[rx[a]] for a in range(N)) @ sum(c[ry[b]].getH() @ c[my[b]] for b in range(N))
    hop = hop + hop.getH()
    gi = max(max(comm_norm(hop, g) for g in Gx), max(comm_norm(hop, g) for g in Gy))
    print(f"SU({N}): one relation + 2 junctions ({M} fermion modes = {M} grains' worth of qubits):")
    print(f"   Lie algebra at a junction [G^a,G^b] = i f^abc G^c : max error {f_err:.1e}  ({len(T)} generators)")
    print(f"   matter hopping psi^dag U psi gauge-invariant: max |[H, G^a]| = {gi:.1e}")

# ---------------------------------------------------------------- 2b + 3: SU(2) plaquette
N = 2
T = gens(2)
links = [(0, 1), (1, 2), (2, 3), (3, 0)]
M = len(links) * 2 * N                                      # 16 rishon modes
c = fermion_ops(M)
end = {}
k = 0
for li, (x, y) in enumerate(links):
    end[(li, x)] = list(range(k, k + N)); k += N
    end[(li, y)] = list(range(k, k + N)); k += N
Gs = {x: [sum(bilinear(c, end[(li, xx)], t) for li, (a, b) in enumerate(links) for xx in (a, b) if xx == x)
          for t in T] for x in range(4)}


def U(li, a, b):
    x, y = links[li]
    return c[end[(li, x)][a]] @ c[end[(li, y)][b]].getH()


plaq = None
for a, b, cc, d in itertools.product(range(N), repeat=4):
    term = U(0, a, b) @ U(1, b, cc) @ U(2, cc, d) @ U(3, d, a)
    plaq = term if plaq is None else plaq + term
H = -(plaq + plaq.getH())
gi = max(comm_norm(H, g) for x in range(4) for g in Gs[x])
print(f"\nSU(2) plaquette (4 relations, 16 rishon modes): plaquette term gauge-invariant: max |[H, G^a_x]| = {gi:.1e}")
# gauge-invariant sector: rishon number 2 per link (one fundamental 'string' per link), singlet at every junction
num = [sum(c[m].getH() @ c[m] for m in end[(li, links[li][0])] + end[(li, links[li][1])]) for li in range(4)]
diag = np.array([np.round(nl.diagonal().real).astype(int) for nl in num])
sector = np.nonzero(np.all(diag == 2, axis=0))[0]
cas = sum(g @ g for x in range(4) for g in Gs[x])
Cs = cas[sector][:, sector].toarray()
w, v = np.linalg.eigh(Cs)
phys = v[:, w < 1e-9]
Hs = phys.conj().T @ H[sector][:, sector].toarray() @ phys
e = np.linalg.eigvalsh(Hs)
print(f"   sector with 2 rishons per relation: {len(sector)} states; colour-singlet at all 4 junctions: {phys.shape[1]} physical states")
print(f"   spectrum of -J(tr U_p + h.c.) in the physical sector: {np.round(e, 3)}")
print(f"   ({time.time() - t0:.0f}s so far)")

# ---------------------------------------------------------------- 4. grains per relation at the real couplings
MZ = 91.19
ainv = np.array([59.01, 29.59, 8.47])
b = np.array([41 / 10, -19 / 6, -7.0])
for mu in (7.7e10, 1e15):
    ai = ainv - b / (2 * math.pi) * math.log(mu / MZ)
    g2, g3 = math.sqrt(4 * math.pi / ai[1]), math.sqrt(4 * math.pi / ai[2])
    print(f"\nGRAINS PER RELATION at mu = {mu:.0e} GeV (one-loop SM couplings g2^2 = {g2 ** 2:.2f}, g3^2 = {g3 ** 2:.2f}):")
    for name, g, N_ in (("SU(2) weak", g2, 2), ("SU(3) strong", g3, 3)):
        for factor in (2, 4):
            jmax = factor / g                                    # electric flux needed ~ few / g at weak coupling
            if N_ == 2:
                dim = sum((2 * j + 1) ** 2 for j in np.arange(0, jmax + 0.25, 0.5))
            else:
                P = int(2 * jmax)
                dim = sum(((p + 1) * (q + 1) * (p + q + 2) // 2) ** 2 for p in range(P + 1) for q in range(P + 1) if p + q <= P)
            print(f"   {name:12s} truncation ~{factor}/g (j_max ~ {jmax:.1f}): link states ~{dim:,.0f} -> ~{math.log2(dim):.0f} qubits (grains)")
print("   + U(1) hypercharge (spin-ice grain, ~1-4 qubits)  ->  a relation is a bundle of roughly 20-50 grains")
print(f"\n(total {time.time() - t0:.0f}s)")
