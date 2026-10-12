#!/usr/bin/env python3
"""
ccef_nent.py  --  derive the entanglement number N_ent (formerly 'N_eff') from the current grain theory alone.

Definitions (grain theory only):  Jacobson: G = l^2 / (4 eta_g), eta_g = entanglement across a surface per grain area
l^2 (l = grain length = junction spacing).  N_ent = 24 pi eta_g is only a conventional label (renamed from N_eff to
avoid confusion with the cosmological Delta N_eff).  No number from earlier CCEF versions is used.

Three contributions, each from the current construction:
  A. FIELDS on the junction lattice (distillable entanglement, exact Gaussian states):
     per-field coefficients for a scalar and for the grain Dirac fermion, now averaged over cut ORIENTATIONS
     ((001), and (111) through both of its inequivalent gaps) - a horizon is a coarse surface, not one lattice plane.
  B. FIELD CONTENT the current theory puts on the grains:
     light (spin-ice U(1), 2 polarisations); SU(2), SU(3) rishon links (6 + 16 polarisations, free-field proxy);
     fermions: every Standard-Model Weyl field + the lattice-forced mirror = one grain Dirac field; 16 per generation
     (nu^c required by the anomaly argument); the 3 X-valleys = 3 generations (minimal) or not (x3);
     Higgs: not yet built in the grain theory (0, or 4 real scalars if added).
  C. EDGE (Gauss-law) entanglement of the grains themselves: the boundary electric-flux configuration is a classical
     label shared by both sides.  Computed for the spin-ice U(1) by Monte Carlo of the ice manifold (entropy per cut
     grain); for SU(2)/SU(3) bundles only bounds (0 .. n ln2 per cut relation).
"""

import contextlib
import io
import math
import random
import time
from collections import Counter

import numpy as np

with contextlib.redirect_stdout(io.StringIO()):
    import ccef_strong_cp as scp
from ccef_grain_hamiltonian_mc import diamond

T0 = time.time()


# ================================================================ A. per-field coefficients, several cuts
def make_hops(avecs, rB, terms):
    Am = np.array(avecs, dtype=float).T
    Ai = np.linalg.inv(Am)
    rs = {0: np.zeros(3), 1: np.array(rB, dtype=float)}
    hops, cross = [], 0
    for sub in (0, 1):
        for a, b, d, T in terms:
            if a != sub:
                continue
            c = Ai @ (rs[sub] + np.array(d, dtype=float) - rs[b])
            ci = np.round(c).astype(int)
            assert np.allclose(c, ci)
            hops.append((sub, b, ci, np.atleast_2d(T)))
            if a != b and ci[2] != 0:
                cross += 1
    return hops, cross, np.linalg.norm(np.cross(avecs[0], avecs[1]))


def H_slab(hops, nspin, kap, Lz):
    dim = 2 * Lz * nspin
    H = np.zeros((dim, dim), dtype=complex)
    for m in range(Lz):
        for sub, b, ci, T in hops:
            m2 = (m + ci[2]) % Lz
            blk = T * np.exp(2j * np.pi * (kap[0] * ci[0] + kap[1] * ci[1]))
            i0, j0 = (2 * m + sub) * nspin, (2 * m2 + b) * nspin
            H[i0:i0 + nspin, j0:j0 + nspin] += blk
            H[j0:j0 + nspin, i0:i0 + nspin] += blk.conj().T
    return H


def S_ferm(H, nreg):
    w, V = np.linalg.eigh(H)
    occ = V[:, w < 0]
    nu = np.clip(np.linalg.eigvalsh(occ[:nreg] @ occ[:nreg].conj().T), 1e-14, 1 - 1e-14)
    return float(-np.sum(nu * np.log(nu) + (1 - nu) * np.log(1 - nu)))


def S_bos(Hhop, nreg):
    K = 4 * np.eye(Hhop.shape[0]) + Hhop
    w, V = np.linalg.eigh(K)
    X = (V / np.sqrt(w)) @ V.conj().T / 2
    P = (V * np.sqrt(w)) @ V.conj().T / 2
    ev = np.linalg.eigvals(X[:nreg, :nreg] @ P[:nreg, :nreg]).real
    nu = np.sqrt(np.clip(ev, 0.25 + 1e-15, None))
    return float(np.sum((nu + .5) * np.log(nu + .5) - (nu - .5) * np.log(nu - .5)))


CUTS = {"(001)": ([(2, 2, 0), (2, -2, 0), (0, 2, 2)], (1, 1, 1)),
        "(110)": ([(2, -2, 0), (0, 0, 4), (2, 0, 2)], (-1, 1, -1)),
        "(111) narrow gap (3 grains/site)": ([(2, -2, 0), (0, 2, -2), (2, 2, 0)], (1, 1, 1)),
        "(111) wide gap (1 grain/site)": ([(2, -2, 0), (0, 2, -2), (2, 2, 0)], (-1, -1, 1))}
FTERMS = scp.base_terms(0.25)
STERMS = [(0, 1, d, np.array([[-1.0]])) for d in scp.DEL]
NK, LZ = 12, 16
kgrid = [((i + .5) / NK, (j + .5) / NK) for i in range(NK) for j in range(NK)]
print("A. PER-FIELD AREA-LAW COEFFICIENTS eta_g (per grain area l^2 = 3), exact Gaussian states, two cuts per slab")
coef = {}
for name, (av, rB) in CUTS.items():
    hs, cross, area = make_hops(av, rB, STERMS)
    hf, _, _ = make_hops(av, rB, FTERMS)
    es = np.mean([S_bos(H_slab(hs, 1, k, LZ), LZ) for k in kgrid]) / (2 * area) * 3
    ef = np.mean([S_ferm(H_slab(hf, 2, k, LZ), LZ * 2) for k in kgrid]) / (2 * area) * 3
    gpl = cross / area * 3
    coef[name] = (es, ef, gpl)
    print(f"   {name:34s} grains cut per l^2 = {gpl:.3f}:  scalar {es:.4f} ({es / gpl:.4f} per cut grain)   "
          f"grain Dirac fermion {ef:.4f} ({ef / gpl:.3f} per cut grain)")
# a plane at a random position along [111] falls in the wide gap 3/4 of the time (gap widths sqrt3 vs sqrt3/3)
c111 = [0.25 * a + 0.75 * b for a, b in zip(coef["(111) narrow gap (3 grains/site)"], coef["(111) wide gap (1 grain/site)"])]
fam = {"(001)": (coef["(001)"], 3), "(110)": (coef["(110)"], 6), "(111)": (c111, 4)}   # weights: equivalent planes
wsum = sum(w for _, w in fam.values())
ES = sum(c[0] * w for c, w in fam.values()) / wsum
EF = sum(c[1] * w for c, w in fam.values()) / wsum
GPL = sum(c[2] * w for c, w in fam.values()) / wsum
print(f"   (111) position-weighted: scalar {c111[0]:.4f}, fermion {c111[1]:.4f}, grains cut {c111[2]:.3f}/l^2")
print(f"   orientation-averaged (weights 3:6:4 for the plane families): grains cut {GPL:.3f}/l^2 "
      f"(isotropic geometric value 0.650)")
print(f"   -> scalar eta = {ES:.4f} (N_ent {24 * math.pi * ES:.2f});  grain Dirac fermion eta = {EF:.4f} "
      f"(N_ent {24 * math.pi * EF:.2f})")
lo = min(c[1] for c, _ in fam.values())
hi = max(c[1] for c, _ in fam.values())
print(f"   fermion spread over orientations: {lo:.3f}-{hi:.3f} ({(hi - lo) / EF * 100:.0f}%)\n")

# ================================================================ C. spin-ice edge entropy per cut grain
print("C. EDGE ENTROPY OF THE GRAINS' OWN GAUSS LAW (spin-ice U(1)): Monte Carlo of the ice manifold")
L = 4
N, E = diamond(L)
nA = N // 2
box = 4 * L
Apos = [(x, y, z) for x in range(0, box, 2) for y in range(0, box, 2) for z in range(0, box, 2) if (x + y + z) % 4 == 0]
pos = Apos + [tuple((c + 1) % box for c in p) for p in Apos]
inc = [[] for _ in range(N)]
for k, (a, b) in enumerate(E):
    inc[a].append(k)
    inc[b].append(k)
spin = [0] * len(E)
used = [False] * len(E)
for st in range(N):
    while any(not used[k] for k in inc[st]):
        v = st
        while True:
            ks = [k for k in inc[v] if not used[k]]
            if not ks:
                break
            k = ks[0]
            used[k] = True
            spin[k] = 1 if v < nA else -1
            v = E[k][1] if v == E[k][0] else E[k][0]
rng = random.Random(3)


def loop_flip():
    v, path, seen = rng.randrange(N), [], {}
    while v not in seen:
        seen[v] = len(path)
        outs = [k for k in inc[v] if spin[k] == (1 if v < nA else -1)]
        k = outs[rng.randrange(len(outs))]
        path.append(k)
        v = E[k][1] if v == E[k][0] else E[k][0]
    for k in path[seen[v]:]:
        spin[k] = -spin[k]


cut = [k for k, (a, b) in enumerate(E) if {pos[a][2], pos[b][2]} == {7, 8}]
mid = {k: ((pos[E[k][0]][0] + pos[E[k][1]][0]) / 2 % box, (pos[E[k][0]][1] + pos[E[k][1]][1]) / 2 % box) for k in cut}


def pdist(p, q):
    dx = min(abs(p[0] - q[0]), box - abs(p[0] - q[0]))
    dy = min(abs(p[1] - q[1]), box - abs(p[1] - q[1]))
    return dx * dx + dy * dy


KMAX = 12
refs = cut[:16]
windows = {r: sorted(cut, key=lambda k: pdist(mid[k], mid[r]))[:KMAX] for r in refs}
for _ in range(20000):
    loop_flip()
NS = 30000
samples = []
for _ in range(NS):
    for _ in range(3):
        loop_flip()
    samples.append([spin[k] for k in cut])
S = (np.array(samples) > 0).astype(np.int64)
col = {k: i for i, k in enumerate(cut)}
Hk = []
for kk in range(1, KMAX + 1):
    hs = []
    for r in refs:
        idx = [col[k] for k in windows[r][:kk]]
        codes = S[:, idx] @ (1 << np.arange(kk))
        cnt = np.array(list(Counter(codes.tolist()).values()), dtype=float)
        p = cnt / NS
        hs.append(-np.sum(p * np.log(p)) + (len(cnt) - 1) / (2 * NS))     # Miller-Madow
    Hk.append(np.mean(hs))
Hk = np.array(Hk)
slope = np.polyfit(np.arange(6, KMAX + 1), Hk[5:], 1)[0]
print(f"   {len(cut)} grains cross a (001) plane of the 1,024-grain ice; {NS} ice states (loop algorithm)")
print("   block entropy H(k) of k neighbouring cut grains: " + ", ".join(f"{h:.2f}" for h in Hk[[0, 3, 7, 11]])
      + f"  (k = 1, 4, 8, 12)")
print(f"   entropy per cut grain: single grain {Hk[0]:.3f} (ln2 = {math.log(2):.3f}); large-block slope {slope:.3f}")
H_EDGE = slope
print(f"   -> each U(1) grain crossing a surface carries ~{H_EDGE:.2f} nats of shared flux label\n")

# ================================================================ B + totals
print("B. FIELD CONTENT OF THE CURRENT GRAIN THEORY and the resulting N_ent = 24 pi eta_g")
nf_min, nf_max = 16, 48
pol = 2 + 6 + 16
rows = {
    "fermions, valleys = generations (16 grain Dirac fields)": nf_min * EF,
    "gauge bosons: light 2 + SU(2) 6 + SU(3) 16 polarisations": pol * ES,
}
fields_min = sum(rows.values())
for k, v in rows.items():
    print(f"   {k:58s} eta = {v:6.3f}   N_ent = {24 * math.pi * v:6.1f}")
print(f"   {'(Higgs, if added: 4 real scalars)':58s} eta = {4 * ES:6.3f}   N_ent = {24 * math.pi * 4 * ES:6.1f}")
print(f"   {'(if valleys are NOT generations: 48 grain Dirac fields)':58s} eta = {nf_max * EF:6.3f}   "
      f"N_ent = {24 * math.pi * nf_max * EF:6.1f}")
edge_u1 = [GPL * n * H_EDGE for n in (1, 4)]
edge_na = [0.0, GPL * 37 * math.log(2)]
print(f"   edge, U(1) grains (1-4 per relation, computed per grain): eta = {edge_u1[0]:.2f}-{edge_u1[1]:.2f}  "
      f"N_ent = {24 * math.pi * edge_u1[0]:.0f}-{24 * math.pi * edge_u1[1]:.0f}")
print(f"   edge, SU(2)+SU(3) bundles (bounds 0 .. n ln2, n <= 37):   eta = 0-{edge_na[1]:.1f}  "
      f"N_ent = 0-{24 * math.pi * edge_na[1]:.0f}")

MP, LP = 1.2209e19, 1.616255e-35


def scale(eta):
    r = math.sqrt(4 * eta)                                   # l = sqrt(4 eta) l_P
    return r, MP / r


print("\nRESULT  (l = sqrt(4 eta_g) l_P,  M = hbar c / l)")
cases = [("fields only (minimal content)", fields_min),
         ("fields + U(1) edge (computed)", fields_min + edge_u1[0]),
         ("fields + U(1) edge (4 U(1) grains)", fields_min + edge_u1[1]),
         ("fields + all edges (upper bound)", fields_min + edge_u1[1] + edge_na[1]),
         ("non-minimal fermions + U(1) edge", nf_max * EF + pol * ES + edge_u1[0])]
for lab, eta in cases:
    r, M = scale(eta)
    print(f"   {lab:38s} eta_g = {eta:6.2f}  N_ent = {24 * math.pi * eta:6.0f}:  l = {r:5.2f} l_P,  M = {M:.2e} GeV")
print(f"\ntotal {time.time() - T0:.0f} s")
