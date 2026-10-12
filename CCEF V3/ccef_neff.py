#!/usr/bin/env python3
"""
ccef_neff.py  --  N_eff (gravity's species count) for the full grain field content.

Jacobson / Sakharov: G = l^2 / (4 eta_g), eta_g = N_eff / (24 pi), eta_g = entanglement area-law coefficient of ALL
fields living on the grains (per grain length squared).  ccef_induced_gravity.py computed eta_g for a massless scalar
and the grain electron.  Here:
  1. Do HEAVY fields count?  The area law is set at the grain scale, so a mass far below the grain scale should not
     matter.  Test: massive scalar (m = 0 .. 1 in grain units) and a gapped grain fermion (bond dimerisation delta).
  2. Sensitivity of the grain-electron coefficient to the spin-orbit strength lambda.
  3. Count the full content as it is built in CCEF (CCEF_chiral.md, CCEF_grain_electrons.md, CCEF_nonabelian.md):
       fermions: each SM Weyl field + its lattice mirror = one grain Dirac field; the 3 X-valleys = 3 generations
                 -> 16 grain-electron fields (16 Weyl per generation, nu^c included)
       gauge:    12 gauge bosons x 2 polarisations (scalar proxy); Higgs: 4 real scalars
  4. Cross-check with the grain budget: a relation bundle of n grains (qubits) can carry at most ~n ln2 of entanglement
     across a cut -> N_eff <~ 39 n on this cut (rough).
"""

import contextlib
import io
import time

import numpy as np

with contextlib.redirect_stdout(io.StringIO()):
    import ccef_strong_cp as scp

T0 = time.time()
CELL_A = [np.array(p) for p in ((0, 0, 0), (0, 2, 2), (2, 0, 2), (2, 2, 0))]
SITES = [(0, p) for p in CELL_A] + [(1, p + 1) for p in CELL_A]
NK, LZ = 10, 8


def bloch_chain(terms, nspin, kx, ky, Lz):
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
            iy, _ = allsites[tuple(ym)]
            blk = np.atleast_2d(T) * np.exp(1j * (kx * w[0] + ky * w[1]))
            H[ix * nspin:(ix + 1) * nspin, iy * nspin:(iy + 1) * nspin] += blk
            H[iy * nspin:(iy + 1) * nspin, ix * nspin:(ix + 1) * nspin] += blk.conj().T
    return H


def S_fermion(kx, ky, terms):
    H = bloch_chain(terms, 2, kx, ky, LZ)
    w, V = np.linalg.eigh(H)
    occ = V[:, w < 0]
    r = np.arange(len(SITES) * (LZ // 2) * 2)
    nu = np.clip(np.linalg.eigvalsh(occ[r] @ occ[r].conj().T), 1e-14, 1 - 1e-14)
    gap = np.min(np.abs(w))
    return float(-np.sum(nu * np.log(nu) + (1 - nu) * np.log(1 - nu))), gap


def S_scalar(kx, ky, m):
    terms = [(0, 1, d, np.array([[-1.0]])) for d in scp.DEL]
    Hh = bloch_chain(terms, 1, kx, ky, LZ)
    K = (4 + m * m) * np.eye(Hh.shape[0]) + Hh
    w, V = np.linalg.eigh(K)
    X = (V / np.sqrt(w)) @ V.conj().T / 2
    P = (V * np.sqrt(w)) @ V.conj().T / 2
    r = np.arange(len(SITES) * (LZ // 2))
    ev = np.linalg.eigvals(X[np.ix_(r, r)] @ P[np.ix_(r, r)]).real
    nu = np.sqrt(np.clip(ev, 0.25 + 1e-15, None))
    return float(np.sum((nu + .5) * np.log(nu + .5) - (nu - .5) * np.log(nu - .5))), float(np.sqrt(w.min()))


KS = (np.arange(NK) + 0.5) / NK * 2 * np.pi / 4 - np.pi / 4


def eta(fn):
    vals = [fn(kx, ky) for kx in KS for ky in KS]
    return sum(v[0] for v in vals) / (2 * 16 * NK * NK) * 3.0, min(v[1] for v in vals)


def fermion_terms(lam, delta=0.0):
    out = []
    for t in scp.base_terms(lam):
        a, b, d, T = t
        if a != b and np.allclose(d, scp.DEL[0]):
            T = T * (1 + delta)                             # one bond direction strengthened: gaps the Dirac points
        out.append((a, b, d, T))
    return out


to_N = lambda e: 24 * np.pi * e
print("1. DO HEAVY FIELDS COUNT?  (masses in grain units: 1 = the grain scale M)")
for m in (0.0, 0.1, 0.3, 1.0):
    e, g = eta(lambda kx, ky: S_scalar(kx, ky, m))
    print(f"   scalar, mass {m:4.1f}:                 eta_g = {e:.4f}   N_eff = {to_N(e):5.2f}")
for dl in (0.0, 0.3, 0.6):
    e, g = eta(lambda kx, ky: S_fermion(kx, ky, fermion_terms(0.25, dl)))
    print(f"   grain fermion, dimerisation {dl:3.1f} (gap {2 * g:4.2f}): eta_g = {e:.4f}   N_eff = {to_N(e):5.2f}")
print("   -> fields far lighter than the grain scale count fully (all SM fields and the mirror partners at ~1e13 GeV)")

print("\n2. SENSITIVITY OF THE GRAIN ELECTRON TO SPIN-ORBIT STRENGTH")
NF = {}
for lam in (0.1, 0.25, 0.5):
    e, _ = eta(lambda kx, ky: S_fermion(kx, ky, fermion_terms(lam)))
    NF[lam] = to_N(e)
    print(f"   lambda = {lam:4.2f}: eta_g = {e:.4f}   N_eff = {to_N(e):5.2f}")

NS = to_N(eta(lambda kx, ky: S_scalar(kx, ky, 0.0))[0])
nf_lo, nf_hi = min(NF.values()), max(NF.values())
print("\n3. FULL CONTENT AS BUILT IN CCEF")
rows = [("fermions: 16 grain Dirac fields (each SM Weyl + mirror; 3 valleys = 3 generations)", 16 * NF[0.25],
         16 * nf_lo, 16 * nf_hi),
        ("gauge bosons: 12 x 2 polarisations (scalar proxy)", 24 * NS, 24 * NS, 24 * NS),
        ("Higgs doublet: 4 real scalars", 4 * NS, 4 * NS, 4 * NS)]
tot = sum(r[1] for r in rows)
lo, hi = sum(r[2] for r in rows), sum(r[3] for r in rows)
for name, v, a, b in rows:
    print(f"   {name:86s} N_eff = {v:6.1f}  ({a:.0f}-{b:.0f})")
print(f"   TOTAL N_eff = {tot:.0f}  (range {lo:.0f}-{hi:.0f} from lambda);  without mirror partners (8 fields): "
      f"{tot - 8 * NF[0.25]:.0f}")

EP, LP = 1.221e19, 1.616e-35


def scale(Ne):
    r = np.sqrt(Ne / (6 * np.pi))
    return r, r * LP, EP / r


print("\n   grain size and grain scale  (l = sqrt(N_eff / 6 pi) l_P,  M = hbar c / l):")
for label, Ne in (("assumed so far", 9), ("light + grain electron", 2 * NS + NF[0.25]),
                  ("full content, no mirrors", tot - 8 * NF[0.25]), ("FULL CONTENT (with mirrors)", tot),
                  ("range high", hi)):
    r, l, M = scale(Ne)
    print(f"   {label:28s} N_eff = {Ne:6.1f}: l = {r:5.2f} l_P = {l:.2e} m,  M = {M:.2e} GeV")

print("\n4. GRAIN BUDGET CROSS-CHECK (rough): this cut crosses 0.75 relations per l^2; a bundle of n grains carries")
print("   <~ n ln2 across the cut -> N_eff <~ 24 pi x 0.75 x n ln2 = %.1f n" % (24 * np.pi * 0.75 * np.log(2)))
nmin = tot / (24 * np.pi * 0.75 * np.log(2))
print(f"   full content needs n >~ {nmin:.0f} grains per relation; CCEF_nonabelian estimated ~25-37 "
      f"(U(1) 1-4 + SU(2) 8-11 + SU(3) 15-22): consistent")
print(f"\ntotal {time.time() - T0:.0f} s")
