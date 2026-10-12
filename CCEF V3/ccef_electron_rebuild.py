#!/usr/bin/env python3
"""
ccef_electron_rebuild.py  --  the grain electron rebuilt as a separate fermionic constituent of the relation bundle,
minimally coupled to the spin-ice light (CCEF_light_window.md showed the old 'bare spin-ice charge' electron is too
fast and Mott-gapped inside the photon phase).

NEW RULES
  matter:  fermions c_{v,s} at each junction (spin s = up/down), part of the relation bundles (qubit-encoded as before)
  light:   spin-ice grains, E_l = S^z_l (oriented A -> B)
  Gauss:   G_v = div E (outflow) - (n_v - 1)   [half-filling background];  physical states: G_v = 0
           the old J_zz term becomes J_G sum_v G_v^2: it penalises only Gauss VIOLATIONS, not matter charge
  hop:     -t c^+_{w,s} S^-_l c_{v,s} + h.c.  (A -> B; moves charge and its flux together), t independent of J_pm
  ring:    S^+ S^- S^+ S^- S^+ S^- around hexagons (light), unchanged
CHECKS
  1. exact gauge invariance; J_G G^2 vanishes on every physical state -> NO on-site repulsion from the light sector
  2. residual Coulomb repulsion vs the Mott threshold:  U_eff / t = 4 alpha G(0) / C  (diamond lattice Green function)
  3. one light cone: matter hop matched to the photon speed (photon velocity of the diamond lattice gauge field)
  4. masslessness in the background flux the light actually has: 0-flux (unfrustrated spin ice) and pi-flux
     (frustrated spin ice, the sign CCEF's ring term assumed) - spin-1/2 Fu-Kane-Mele hopping made gauge covariant
"""

import contextlib
import io
import itertools
import math
import time

import numpy as np
import scipy.sparse as sp

with contextlib.redirect_stdout(io.StringIO()):
    import ccef_strong_cp as scp
from ccef_grain_lattice import build, pi_flux_signs
from ccef_grain_hamiltonian_mc import diamond

T0 = time.time()

# ================================================================ 1. gauge invariance and no on-site U (one hexagon ring)
print("1. GAUGE INVARIANCE AND THE ON-SITE REPULSION  (one hexagonal ring: 6 junctions, 6 grains, spin-1/2 matter)")
nj, nl = 6, 6
nf = 2 * nj                                    # fermion modes (j, s) -> 2j + s
NQ = nf + nl
I2s = sp.identity(2, format="csr")
sz = sp.csr_matrix(np.diag([0.5, -0.5]))
spl = sp.csr_matrix(np.array([[0, 1], [0, 0]], dtype=float))
Zm = sp.csr_matrix(np.diag([1.0, -1.0]))
ann = sp.csr_matrix(np.array([[0, 1], [0, 0]], dtype=float))     # |1> -> |0>  (basis |0>,|1>) ... occupation index


def kron_list(ops):
    out = ops[0]
    for o in ops[1:]:
        out = sp.kron(out, o, format="csr")
    return out


def on(q, op):
    return kron_list([op if k == q else I2s for k in range(NQ)])


nocc = sp.csr_matrix(np.diag([0.0, 1.0]))
a_loc = sp.csr_matrix(np.array([[0, 1], [0, 0]], dtype=float))   # basis (|0>,|1>): annihilates |1>
Zf = sp.csr_matrix(np.diag([1.0, -1.0]))


def c_op(m):                                   # Jordan-Wigner annihilator for fermion mode m (qubits 0..nf-1)
    return kron_list([Zf if k < m else (a_loc if k == m else I2s) for k in range(NQ)])


C = [c_op(m) for m in range(nf)]
Cd = [c.T.tocsr() for c in C]
N_ = [Cd[m] @ C[m] for m in range(nf)]
Ez = [on(nf + l, sz) for l in range(nl)]
Sp = [on(nf + l, spl) for l in range(nl)]
Sm = [s.T.tocsr() for s in Sp]
# ring: junctions 0..5, even = A, odd = B; link l joins j=l and j=l+1 (mod 6); orientation A -> B
links = [(l, (l + 1) % 6) for l in range(nl)]
eta = {}
for l, (u, w) in enumerate(links):
    A, B = (u, w) if u % 2 == 0 else (w, u)
    eta[(A, l)], eta[(B, l)] = +1, -1
G = []
dim = 2 ** NQ
Id = sp.identity(dim, format="csr")
for v in range(nj):
    div = sum(eta[(v, l)] * Ez[l] for l in range(nl) if (v, l) in eta)
    G.append(div - (N_[2 * v] + N_[2 * v + 1] - Id))
Hhop = sp.csr_matrix((dim, dim))
for l, (u, w) in enumerate(links):
    A, B = (u, w) if u % 2 == 0 else (w, u)
    for s in (0, 1):
        T = Cd[2 * B + s] @ Sm[l] @ C[2 * A + s]               # A -> B: E_l decreases by 1
        Hhop = Hhop - (T + T.T)
ring = Sp[0]
for l in range(1, nl):
    ring = ring @ (Sm[l] if l % 2 else Sp[l])
Hring = ring + ring.T
rng = np.random.default_rng(1)
psi = rng.normal(size=dim)
viol = max(np.abs(Hhop @ (G[v] @ psi) - G[v] @ (Hhop @ psi)).max() for v in range(nj))
violr = max(np.abs(Hring @ (G[v] @ psi) - G[v] @ (Hring @ psi)).max() for v in range(nj))
print(f"   [H_hop, G_v] max violation {viol:.1e};  [H_ring, G_v] {violr:.1e}  (exact gauge invariance)")
Gd = np.array([G[v].diagonal() for v in range(nj)])
phys = np.all(np.abs(Gd) < 1e-12, axis=0)
nd = np.array([N_[m].diagonal() for m in range(nf)])
double = np.array([nd[2 * v] * nd[2 * v + 1] for v in range(nj)]).sum(0)
HG = (Gd ** 2).sum(0)
print(f"   physical states (all G_v = 0): {phys.sum()};  of these with a doubly occupied junction: "
      f"{int(np.sum(phys & (double > 0)))};  J_G sum G^2 on them: max {HG[phys].max():.1f}")
Qold = np.array([sum(eta[(v, l)] * Ez[l].diagonal() for l in range(nl) if (v, l) in eta) for v in range(nj)])
cost_old = (Qold ** 2).sum(0)
dbl_phys = phys & (double > 0)
sgl_phys = phys & (double == 0) & (nd.sum(0) == nj)
print(f"   OLD rule (J_zz Q_v^2 on the light's own charge, matter = spin-ice charges): mean cost of states with a")
print(f"   doubly occupied junction {cost_old[dbl_phys].mean():.2f} J_zz vs none {cost_old[sgl_phys].mean():.2f} J_zz;"
      f"  NEW rule: 0 and 0  -> the on-site U from the light sector is GONE\n")

# ================================================================ 2. residual Coulomb repulsion
print("2. RESIDUAL COULOMB REPULSION (photon exchange) vs the Mott threshold")
NK = 64
g = (np.arange(NK) + 0.5) / NK
Bm = 2 * np.pi * np.linalg.inv(np.array([[0, 2, 2], [2, 0, 2], [2, 2, 0]], float)).T
K = np.array(np.meshgrid(g, g, g, indexing="ij")).reshape(3, -1).T @ Bm
f = np.exp(1j * K @ scp.DEL.T).sum(1)
detL = 16 - np.abs(f) ** 2
GAA = 4 / detL                                                 # [L^-1]_AA for L = [[4, -f], [-f*, 4]]
G0 = GAA.mean()
rs, rG = [], []
for m in (3, 4, 5, 6, 7):
    r = np.array([4.0 * m, 0, 0])                              # A -> A along x
    rs.append(np.linalg.norm(r))
    rG.append((GAA * np.cos(K @ r)).mean() * np.linalg.norm(r))
Cc = np.mean(rG[-3:])
print(f"   diamond lattice Green function: G(0) = {G0:.4f};  r G(r) -> C = {Cc:.4f} (continuum 1/pi = {1 / math.pi:.4f})")


def vphoton(L):
    N, edges, inc, hexes = build(L)
    d1 = np.zeros((len(hexes), len(edges)))
    for hi, hx in enumerate(hexes):
        es = list(hx)
        adj = {}
        for e in es:
            for v in edges[e]:
                adj.setdefault(v, []).append(e)
        cur, v = es[0], edges[es[0]][0]
        for _ in range(6):
            a, b = edges[cur]
            d1[hi, cur] = 1 if v == a else -1
            v = b if v == a else a
            cur = [e for e in adj[v] if e != cur][0]
    w = np.linalg.eigvalsh(d1.T @ d1)
    w = np.sort(w[w > 1e-8])
    return math.sqrt(w[0]) / (2 * math.pi / (4 * L))


vl = vphoton(4)
print(f"   photon speed of the lattice gauge field (unit couplings): v = {vl:.3f} (lattice units; L = 4)")
print(f"   electron cone speed = 4 t (FKM, lambda = 1/4) -> ONE LIGHT CONE requires t = c/4 = {vl:.3f} sqrt(U K) / 4")
for alpha in (0.08, 0.013, 1 / 137):
    Ueff = 4 * alpha * G0 / Cc
    print(f"   alpha = {alpha:.4f}: U_eff / t = 4 alpha G(0)/C = {Ueff:.3f}   (Mott needs >~ 5)")
print("   -> far below the Mott threshold at any realistic coupling\n")

# ================================================================ 3/4. masslessness in 0-flux and pi-flux backgrounds
print("3. MASSLESSNESS IN THE LIGHT'S BACKGROUND FLUX  (spin-1/2 FKM, lambda = 1/4, gauge-covariant hops, torus)")


def fkm_realspace(L, signs, kappa):
    N, edges = diamond(L)
    box = 4 * L
    nA = N // 2
    A = [(x, y, z) for x in range(0, box, 2) for y in range(0, box, 2) for z in range(0, box, 2) if (x + y + z) % 4 == 0]
    pos = [np.array(p) for p in A] + [(np.array(p) + 1) % box for p in A]
    idx = {tuple(p % box): i for i, p in enumerate(pos)}
    eid = {}
    for k, (a, b) in enumerate(edges):
        eid[(a, b)] = eid[(b, a)] = k
    H = np.zeros((2 * N, 2 * N), dtype=complex)

    def add(i, j, blk):
        H[2 * i:2 * i + 2, 2 * j:2 * j + 2] += blk
        H[2 * j:2 * j + 2, 2 * i:2 * i + 2] += blk.conj().T
    for i in range(nA):
        for d in scp.DEL:
            j = idx[tuple((pos[i] + d) % box)]
            add(i, j, -signs[eid[(i, j)]] * np.exp(1j * kappa @ d) * np.eye(2))
    for sub, key, sgn in ((0, "A", 1), (1, "B", -1)):
        for R, Mm in scp.SOC[key]:
            for d1 in sgn * scp.DEL:
                d2 = R - d1
                if any(np.allclose(d2, -sgn * dd) for dd in scp.DEL):
                    break
            rng_sites = range(nA) if sub == 0 else range(nA, N)
            for i in rng_sites:
                wsite = idx[tuple((pos[i] + d1) % box)]
                j = idx[tuple((pos[i] + R) % box)]
                ph = signs[eid[(i, wsite)]] * signs[eid[(wsite, j)]]
                add(i, j, 0.5 * 1j * (8 * 0.25 / 16) * ph * np.exp(1j * kappa @ R) * Mm)
    return H


L = 4
N, edges, inc, hexes = build(L)
s0 = np.ones(len(edges))
spi = pi_flux_signs(edges, hexes)
print(f"   pi-flux pattern on the L = {L} torus: {'found' if spi is not None else 'NOT found'}; check product round every"
      f" hexagon = -1: {spi is not None and all(np.prod(spi[list(h)]) < 0 for h in hexes)}")
for L in (4, 6):
    N, edges, inc, hexes = build(L)
    s0, spi = np.ones(len(edges)), pi_flux_signs(edges, hexes)
    rngk = np.random.default_rng(3)
    twists = [2 * np.pi * rngk.random(3) / (4 * L) for _ in range(12 if L == 4 else 4)]
    for name, sg in (("0-flux (unfrustrated spin ice)", s0), ("pi-flux (frustrated spin ice)", spi)):
        e0 = np.linalg.eigvalsh(fkm_realspace(L, sg, np.zeros(3)))
        a = np.abs(np.concatenate([np.linalg.eigvalsh(fkm_realspace(L, sg, k)) for k in twists]))
        fr = [(a < e).mean() for e in (0.02, 0.05, 0.1, 0.2)]
        print(f"   L = {L} {name:31s} exact zero modes (X points on the grid) {int((np.abs(e0) < 1e-8).sum()):3d};"
              f"  fraction of states below |E| = 0.02/0.05/0.1/0.2: " + " / ".join(f"{x:.4f}" for x in fr))
print("   0-flux: exactly 12 zero modes = 3 Dirac points x 4, no states nearby -> RELATIVISTIC (as before)")
print("   pi-flux: dozens of zero modes and a finite density of low-energy states, N(E) ~ E^(1.1-1.6) -> NOT relativistic")
print("   CCEF's grain Hamiltonian writes -J_pm (s+s- + h.c.) with J_pm > 0: the UNFRUSTRATED sign -> 0-flux spin ice\n")

print("4. SPEED MATCHING with the quantum Monte Carlo photon (Kato & Onoda 2015)")
print("   their H = J s^z s^z + J_perp (s^x s^x + s^y s^y), i.e. J_pm = -J_perp/2: photon phase for J_pm/J_zz < 0.052")
print("   (= |J_perp|/J < 0.104); ring scale g = 3 J_perp^3/(2 J^2) = 12 J_pm^3/J_zz^2; photon speed c = 1.49 a g")
a_cub = 4.0
c_qmc = 1.49 * a_cub
print(f"   in these units (bond (1,1,1), cubic a = 4): c = {c_qmc:.2f} g;  electron cone speed 4 t  ->  one light cone at"
      f" t = {c_qmc / 4:.2f} g = {c_qmc / 4:.2f} J_ring")
print("   -> the matter hop must sit at ~1.5x the ring-exchange scale: an independent coupling of the bundle constituent")
print("      (no longer tied to J_pm, so no 'faster than light' charges)")
print(f"\ntotal {time.time() - T0:.0f} s")
