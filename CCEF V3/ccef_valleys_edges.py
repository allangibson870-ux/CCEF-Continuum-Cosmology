#!/usr/bin/env python3
"""
ccef_valleys_edges.py  --  two checks before rebuilding the electron.

PART 1. ARE THE 3 X-VALLEYS THE 3 GENERATIONS?
  Generations need (i) identical gauge charges (automatic: one lattice field), (ii) independent masses, (iii) mixing
  (CKM/PMNS) with a CP phase, ideally (iv) without spoiling the strong-CP parity solution (Hermitian mass matrices).
  The valleys sit at different crystal momenta, so they mix only if the vacuum breaks the FCC translations down to the
  simple-cubic (conventional, 8-site) cell.  In that cell all three valleys fold to k = 0 -> 12 zero modes.
  Compute: the space of Dirac mass terms for 3 flavours (expect 18 = 9 P-even 'A' + 9 P-odd 'B'), and which part of it
  local grain perturbations reach:
     (a) FCC-periodic bond distortions (the old 'Klein-four' masses)
     (b) cell-periodic, inversion-symmetric, time-reversal-symmetric
     (c) cell-periodic, inversion-symmetric, all (incl. T-breaking, i.e. complex couplings)
     (d) cell-periodic, everything
  and whether they mix valleys.
PART 2. EDGE ENTANGLEMENT OF THE SU(2) / SU(3) BUNDLES (replacing the crude n ln2 bound)
  Electric fluctuations of a free lattice gauge field on the diamond (hexagon plaquettes, exact Gaussian vacuum):
  <E^2> per colour component = c_E / g^2.  Flux-representation probabilities on a cut link p_R ~ dim(R)^2 exp(-tau C2(R))
  fixed by <C2> = dim(G) c_E / g^2, truncated to the link Hilbert space the forces need (CCEF_nonabelian.md).
  Edge entropy per cut link = H(p) + <ln dim R>  (Donnelly; Donnelly-Wall).
"""

import contextlib
import io
import itertools
import math

import numpy as np
from scipy.linalg import sqrtm

with contextlib.redirect_stdout(io.StringIO()):
    import ccef_strong_cp as scp
from ccef_grain_lattice import build

SX, SY, SZ, I2 = scp.SX, scp.SY, scp.SZ, scp.I2
CELL_A = [np.array(p) for p in ((0, 0, 0), (0, 2, 2), (2, 0, 2), (2, 2, 0))]
SITES = [(0, p) for p in CELL_A] + [(1, (p + 1) % 4) for p in CELL_A]
IDX = {tuple(p): i for i, (_, p) in enumerate(SITES)}


def H_conv(k, terms):
    H = np.zeros((16, 16), dtype=complex)
    for i, (sub, p) in enumerate(SITES):
        for a, b, d, T in terms:
            if a != sub:
                continue
            y = p + np.array(d)
            ym = y % 4
            j = IDX[tuple(ym)]
            blk = T * np.exp(1j * np.dot(k, y - ym))
            H[2 * i:2 * i + 2, 2 * j:2 * j + 2] += blk
            H[2 * j:2 * j + 2, 2 * i:2 * i + 2] += blk.conj().T
    return H


terms = scp.base_terms(0.25)
H0 = H_conv(np.zeros(3), terms)
w, V = np.linalg.eigh(H0)
Z = V[:, np.abs(w) < 1e-9]
print("PART 1. VALLEYS AS GENERATIONS")
print(f"   conventional 8-site cell at k = 0: {Z.shape[1]} zero modes (3 valleys x 4 Dirac components)")
h = 1e-6
Vel = [Z.conj().T @ ((H_conv(h * e, terms) - H_conv(-h * e, terms)) / (2 * h)) @ Z for e in np.eye(3)]


def perm_op(shift):
    P = np.zeros((16, 16))
    for i, (_, p) in enumerate(SITES):
        j = IDX[tuple((p + np.array(shift)) % 4)]
        P[2 * j:2 * j + 2, 2 * i:2 * i + 2] = np.eye(2)
    return P


T1, T2 = (Z.conj().T @ perm_op(s) @ Z for s in ((0, 2, 2), (2, 0, 2)))
ev, U = np.linalg.eig(T1 + 2 * T2)                             # joint eigenbasis of two commuting translations
lab = {}
for val in np.round(ev.real, 6):
    lab.setdefault(val, 0)
groups = {}
for idx, val in enumerate(np.round(ev.real, 6)):
    groups.setdefault(val, []).append(idx)
proj = []
for val, ids in groups.items():
    Q, _ = np.linalg.qr(U[:, ids])
    proj.append(Q @ Q.conj().T)
print(f"   primitive translations split them into {len(proj)} valleys of sizes {[int(round(np.trace(P).real)) for P in proj]}")
# inversion (bond-centred: r -> (1,1,1) - r, A <-> B, spin unchanged)
Pinv = np.zeros((16, 16))
for i, (_, p) in enumerate(SITES):
    j = IDX[tuple((np.array([1, 1, 1]) - p) % 4)]
    Pinv[2 * j:2 * j + 2, 2 * i:2 * i + 2] = np.eye(2)
assert np.allclose(Pinv @ H0 @ Pinv.T, H0)
Iz = Z.conj().T @ Pinv @ Z

# Hermitian 12x12 basis and the mass space {X : {X, v_a} = 0}
n = 12
herm = []
for i in range(n):
    for j in range(i, n):
        E = np.zeros((n, n), dtype=complex)
        E[i, j] = E[j, i] = 1
        herm.append(E / np.linalg.norm(E))
        if i != j:
            E = np.zeros((n, n), dtype=complex)
            E[i, j], E[j, i] = 1j, -1j
            herm.append(E / np.linalg.norm(E))
blocks = []
for Va in Vel:
    cols = []
    for X in herm:
        ac = Va @ X + X @ Va
        cols.append(np.r_[ac.real.ravel(), ac.imag.ravel()])
    blocks.append(np.array(cols).T)                       # (288, 144): linear map c -> {V_a, sum c_i X_i}
Amat = np.vstack(blocks)
_, s, vt = np.linalg.svd(Amat)
null = vt[np.sum(s > 1e-8):]
mass_basis = [sum(c * X for c, X in zip(vec, herm)) for vec in null]
print(f"   Dirac mass terms for 3 flavours: {len(mass_basis)} (expected 18 = 9 P-even + 9 P-odd)")
# split by inversion parity
Mpar = np.array([[np.trace(Mi.conj().T @ Iz @ Mj @ Iz.conj().T).real for Mj in mass_basis] for Mi in mass_basis])
pw, pv = np.linalg.eigh((Mpar + Mpar.T) / 2)
Pe = [sum(c * M for c, M in zip(pv[:, k], mass_basis)) for k in range(len(pw)) if pw[k] > 0]
Po = [sum(c * M for c, M in zip(pv[:, k], mass_basis)) for k in range(len(pw)) if pw[k] < 0]
print(f"   inversion-even (P-even, 'A') masses: {len(Pe)};  inversion-odd ('B', the theta-bar direction): {len(Po)}")


def coords(X, basis):
    return np.array([np.trace(B.conj().T @ X).real for B in basis])


# perturbation generators in the 8-site cell
GEN = []                                               # (name, T-class, 16x16 Hermitian)
BONDS_T = {}
ops_bond = [("t", "even", I2), ("i t", "odd", 1j * I2)] + [(f"i s{a}", "even", 1j * S) for a, S in zip("xyz", (SX, SY, SZ))] \
           + [(f"s{a}", "odd", S) for a, S in zip("xyz", (SX, SY, SZ))]
for i, (sub, p) in enumerate(SITES[:4]):
    for d in scp.DEL:
        j = IDX[tuple((p + d) % 4)]
        for nm, tc, T in ops_bond:
            M = np.zeros((16, 16), dtype=complex)
            M[2 * i:2 * i + 2, 2 * j:2 * j + 2] += T
            M[2 * j:2 * j + 2, 2 * i:2 * i + 2] += T.conj().T
            GEN.append((f"bond {nm}", tc, M))
            if nm == "t":
                BONDS_T.setdefault(tuple(int(x) for x in d), []).append(M)
for i in range(8):
    for nm, tc, T in (("mu", "even", I2), ("hx", "odd", SX), ("hy", "odd", SY), ("hz", "odd", SZ)):
        M = np.zeros((16, 16), dtype=complex)
        M[2 * i:2 * i + 2, 2 * i:2 * i + 2] = T
        GEN.append((f"site {i} {nm}", tc, M))


def analyse(mats):
    C = np.array([coords(Z.conj().T @ M @ Z, mass_basis) for M in mats])
    rk = np.linalg.matrix_rank(C, tol=1e-8) if len(C) else 0
    Ce = np.array([coords(Z.conj().T @ M @ Z, Pe) for M in mats])
    Co = np.array([coords(Z.conj().T @ M @ Z, Po) for M in mats])
    re = np.linalg.matrix_rank(Ce, tol=1e-8)
    ro = np.linalg.matrix_rank(Co, tol=1e-8)
    offd = 0.0
    for M in mats:
        X = Z.conj().T @ M @ Z
        Xm = sum(c * B for c, B in zip(coords(X, mass_basis), mass_basis))
        offd = max(offd, sum(np.linalg.norm(Pa @ Xm @ Pb) for a, Pa in enumerate(proj) for b, Pb in enumerate(proj) if a != b))
    return rk, re, ro, offd


# (a) FCC-periodic bond-direction distortions
fcc = [sum(ms) for ms in BONDS_T.values()]
sym = lambda M: M + Pinv @ M @ Pinv.T
inv_all = [sym(M) for _, _, M in GEN]
inv_T = [sym(M) for _, tc, M in GEN if tc == "even"]
for label, mats in (("(a) uniform bond-direction distortions (FCC-periodic)", fcc),
                    ("(b) 8-site-periodic, inversion- and T-symmetric", inv_T),
                    ("(c) 8-site-periodic, inversion-symmetric, incl. complex (T-odd)", inv_all),
                    ("(d) 8-site-periodic, everything", [M for _, _, M in GEN])):
    rk, re, ro, offd = analyse(mats)
    print(f"   {label:62s} mass span {rk:2d}/18 (P-even {re}/9, P-odd {ro}/9); "
          f"valley mixing {'YES' if offd > 1e-8 else 'no'}")
print("   reading: P-even span 9/9 = a general HERMITIAN 3x3 flavour matrix (3 masses + 3 angles + phases) with")
print("   theta-bar = arg det M = 0 automatically when the P-odd part is absent (the strong-CP parity solution)\n")

# ================================================================ PART 2: non-abelian edge entropy
print("PART 2. EDGE ENTANGLEMENT OF THE SU(2) AND SU(3) RELATION BUNDLES")


def cE_of(L):
    N, edges, inc, hexes = build(L)
    d1 = np.zeros((len(hexes), len(edges)))
    for hi, hx in enumerate(hexes):
        es = list(hx)
        adj = {}
        for e in es:
            for v in edges[e]:
                adj.setdefault(v, []).append(e)
        cur = es[0]
        v = edges[cur][0]
        for _ in range(6):
            a, b = edges[cur]
            d1[hi, cur] = 1 if v == a else -1                    # traversed A->B : +1
            v = b if v == a else a
            cur = [e for e in adj[v] if e != cur][0]
    K = d1.T @ d1
    wK, VK = np.linalg.eigh(K)
    sq = (VK * np.sqrt(np.clip(wK, 0, None))) @ VK.T
    return 0.5 * np.mean(np.diag(sq))


cE3, cE4 = cE_of(3), cE_of(4)
cE = cE4
print(f"   free lattice gauge field on the diamond (hexagon plaquettes): c_E = <Pi^2> per link = {cE3:.4f} (L=3), "
      f"{cE4:.4f} (L=4)")


def reps_su2(cap):
    out, tot = [], 0
    for twoj in range(0, 400):
        dim = twoj + 1
        if tot + dim * dim > cap:
            break
        tot += dim * dim
        out.append((dim, twoj / 2 * (twoj / 2 + 1)))
    return out


def reps_su3(cap):
    allr = []
    for p in range(0, 60):
        for q in range(0, 60):
            dim = (p + 1) * (q + 1) * (p + q + 2) // 2
            C2 = (p * p + q * q + p * q + 3 * p + 3 * q) / 3
            allr.append((C2, dim))
    allr.sort()
    out, tot = [], 0
    for C2, dim in allr:
        if tot + dim * dim > cap:
            break
        tot += dim * dim
        out.append((dim, C2))
    return out


def edge_S(reps, target):
    dims = np.array([r[0] for r in reps], float)
    C2 = np.array([r[1] for r in reps], float)

    def dist(tau):
        lw = 2 * np.log(dims) - tau * C2
        p = np.exp(lw - lw.max())
        return p / p.sum()
    lo, hi = 0.0, 50.0
    if np.sum(dist(0.0) * C2) < target:                   # truncation caps the fluctuations
        p = dist(0.0)
    else:
        for _ in range(200):
            mid = (lo + hi) / 2
            if np.sum(dist(mid) * C2) > target:
                lo = mid
            else:
                hi = mid
        p = dist((lo + hi) / 2)
    nz = p > 0
    return float(-np.sum(p[nz] * np.log(p[nz]))), float(np.sum(p * np.log(dims))), float(np.sum(p * C2))


GPL = 0.618
print(f"   {'group':6s} {'g^2':>5s} {'link states':>12s}   H(p)   <ln dim R>   edge/link   <C2> reached")
res = {}
for G, dimG, caps, reps_f in (("SU(2)", 3, (200, 1500), reps_su2), ("SU(3)", 8, (3e4, 6e6), reps_su3)):
    for g2 in (0.25, 0.40):
        for cap in caps:
            Hp, lnd, c2 = edge_S(reps_f(cap), dimG * cE / g2)
            res[(G, g2, cap)] = Hp + lnd
            print(f"   {G:6s} {g2:5.2f} {cap:12.0e}   {Hp:5.2f}   {lnd:8.2f}    {Hp + lnd:7.2f}     "
                  f"{c2:6.1f} / {dimG * cE / g2:5.1f}")
S2 = [res[k] for k in res if k[0] == "SU(2)"]
S3 = [res[k] for k in res if k[0] == "SU(3)"]
lo_e, hi_e = min(S2) + min(S3), max(S2) + max(S3)
# neighbouring cut links are correlated (spin-ice U(1): 0.60 vs 0.69 -> x0.87)
corr = 0.603 / 0.692
eta_lo, eta_hi = GPL * lo_e * corr, GPL * hi_e
print(f"   per cut relation: SU(2)+SU(3) edge {lo_e:.1f}-{hi_e:.1f} nats (crude bound was up to {37 * math.log(2):.1f})")
print(f"   -> eta_g(edge, non-abelian) = {eta_lo:.2f}-{eta_hi:.2f}  (N_ent {24 * math.pi * eta_lo:.0f}-{24 * math.pi * eta_hi:.0f};"
      f" correlation factor 0.87 applied at the low end)")

base_eta = 6.41                                              # CCEF_nent.md central (fields + U(1) edge)
MP = 1.2209e19
print("\nUPDATED N_ent (valleys = generations; fields + U(1) edge + non-abelian edge):")
for lab, eta in (("low", base_eta + eta_lo), ("high", base_eta + eta_hi)):
    r = math.sqrt(4 * eta)
    print(f"   {lab:5s}: eta_g = {eta:5.2f}  N_ent = {24 * math.pi * eta:5.0f}  l = {r:4.2f} l_P  M = {MP / r:.2e} GeV")
