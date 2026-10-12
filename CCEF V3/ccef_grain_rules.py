#!/usr/bin/env python3
"""
ccef_grain_rules.py  --  the grain rules rewritten as LOCAL UPDATE EVENTS (a quantum causal structure).

Tests on real grain systems:
 1. LIGHT event (spin-ice ring update on a 6-grain ring, U = exp(-i e J (O_h + O_h^dag)), O_h = s+ s- s+ s- s+ s-):
    conserves the Gauss charge Q_v at every junction exactly.
 2. CAUSAL INVARIANCE with these real light events on a 16-grain diamond patch (2^16 states): overlapping rings do NOT
    commute (order matters), disjoint ones do; every cause-and-effect-respecting order gives the same state.
 3. ELECTRON events: the grain Dirac fermion (spin-1/2 Fu-Kane-Mele, CCEF_grain_electrons.md) evolved by layers of
    local hops - the 4 bond directions of the diamond are 4 natural layers (each a perfect matching: every junction
    updates exactly one bond per layer) plus spin-orbit layers.  Does the electron stay massless (Dirac point at X)
    when time comes in discrete steps of size eps?  Sequential vs symmetric (palindromic) update order.
"""

import contextlib
import io
import itertools

import numpy as np
from scipy.linalg import expm

from ccef_grain_lattice import build

# ================================================================ 1 + 2: light events
N, edges, inc, hexes = build(1)                       # 8 junctions, 16 grains
nA = N // 2
print(f"diamond patch: {N} junctions, {len(edges)} grains, {len(hexes)} six-rings")


def ring_flip_pattern(h):
    """order the ring's grains around the hexagon and alternate s+ / s- so every junction's charge is unchanged"""
    es = list(h)
    adj = {}
    for e in es:
        a, b = edges[e]
        adj.setdefault(a, []).append(e)
        adj.setdefault(b, []).append(e)
    order, cur_e, cur_v = [es[0]], es[0], edges[es[0]][0]
    while len(order) < 6:
        v = edges[cur_e][1] if edges[cur_e][0] == cur_v else edges[cur_e][0]
        nxt = [e for e in adj[v] if e != cur_e][0]
        order.append(nxt)
        cur_v, cur_e = v, nxt
    signs, s = {}, +1
    # s+ raises sigma^z: Q_A += 2, Q_B -= 2  (Q_v = sum eta sigma^z, eta = +1 at the A end, -1 at the B end)
    v = edges[order[0]][0]
    for e in order:
        a, b = edges[e]
        signs[e] = s
        s = -s
    return order, signs


sp_ = np.array([[0, 1], [0, 0]], dtype=complex)
sm_ = sp_.T.copy()
L = len(edges)


def local_ring_op(order, signs):
    m = np.ones((1, 1), dtype=complex)
    for e in order:
        m = np.kron(m, sp_ if signs[e] > 0 else sm_)
    return m


def apply_local(psi, U, sites):
    k = len(sites)
    psi = psi.reshape([2] * L)
    psi = np.moveaxis(psi, sites, list(range(k))).reshape(2 ** k, -1)
    psi = (U @ psi).reshape([2] * k + [2] * (L - k))
    return np.moveaxis(psi, list(range(k)), sites).reshape(-1)


# Gauss-law check on the full 16-grain space for each ring event (diagonal Q_v)
bits = ((np.arange(2 ** L)[:, None] >> (L - 1 - np.arange(L))) & 1)
sz = 1 - 2 * bits                                       # sigma^z eigenvalue per grain
Qv = np.zeros((2 ** L, N))
for e, (a, b) in enumerate(edges):
    Qv[:, a] += sz[:, e]
    Qv[:, b] -= sz[:, e]
rng = np.random.default_rng(1)
events = []
viol = 0.0
for h in hexes:
    order, signs = ring_flip_pattern(h)
    O = local_ring_op(order, signs)
    U = expm(-1j * 0.4 * (O + O.conj().T))
    events.append((order, U))
    psi = rng.normal(size=2 ** L) + 1j * rng.normal(size=2 ** L)
    psi /= np.linalg.norm(psi)
    for v in range(N):
        # [U, Q_v] = 0  <=>  U preserves each Q_v eigenspace: compare U(Q psi) with Q(U psi)
        lhs = apply_local(Qv[:, v] * psi, U, order)
        rhs = Qv[:, v] * apply_local(psi, U, order)
        viol = max(viol, np.abs(lhs - rhs).max())
print(f"1. LIGHT events: {len(events)} ring updates; max violation of the Gauss law at any junction = {viol:.1e}")

# causal structure: events that share a grain must be ordered.  Pick ring events including disjoint pairs.
sel = [events[0]]
for ev in events[1:]:
    if len(sel) >= 8:
        break
    if any(not (set(ev[0]) & set(s[0])) for s in sel) or len(sel) % 2:
        sel.append(ev)
share = [[bool(set(a[0]) & set(b[0])) for b in sel] for a in sel]
npair = len(sel) * (len(sel) - 1) // 2
ncomm = sum(1 for i, j in itertools.combinations(range(len(sel)), 2) if not share[i][j])
print(f"   {len(sel)} ring events: {ncomm} disjoint pairs (commute), {npair - ncomm} overlapping pairs (order matters)")
psi0 = rng.normal(size=2 ** L) + 1j * rng.normal(size=2 ** L)
psi0 /= np.linalg.norm(psi0)


def run(order_idx):
    psi = psi0.copy()
    for i in order_idx:
        psi = apply_local(psi, sel[i][1], sel[i][0])
    return psi


ref_order = list(range(len(sel)))
ref = run(ref_order)


def random_causal(rng):
    done, out = set(), []
    while len(out) < len(sel):
        ready = [i for i in range(len(sel)) if i not in done and all(j in done for j in range(i) if share[i][j])]
        i = ready[rng.integers(len(ready))]
        done.add(i)
        out.append(i)
    return out


orders = {tuple(random_causal(rng)) for _ in range(400)}
dmax = max(np.linalg.norm(run(list(o)) - ref) for o in orders)
swaps = []
for i, j in itertools.combinations(range(len(sel)), 2):
    if share[i][j]:
        o = ref_order.copy()
        o[i], o[j] = o[j], o[i]
        swaps.append(np.linalg.norm(run(o) - ref))
swaps = np.array(swaps)
print(f"2. CAUSAL INVARIANCE with real light events: {len(orders)} distinct causal orders -> max state difference {dmax:.1e};")
print(f"   reversing two overlapping events (violating cause-and-effect): {np.sum(swaps > 1e-9)} of {len(swaps)} swaps "
      f"change the state (largest difference {swaps.max():.2f})")

# ================================================================ 3: electron events
with contextlib.redirect_stdout(io.StringIO()):
    import ccef_strong_cp as scp
base = scp.base_terms(0.25)
X = scp.X
nn_layers = [[t] for t in base if t[0] != t[1]]                          # 4 bond directions (perfect matchings)
soc_terms = [t for t in base if t[0] == t[1]]
soc_dirs = {}
for t in soc_terms:
    key = tuple(np.round(np.abs(t[2]) * np.sign(t[2][np.nonzero(t[2])[0][0]]), 6))
    soc_dirs.setdefault(key, []).append(t)
soc_layers = list(soc_dirs.values())
layers = nn_layers + soc_layers


def floquet(k, eps, symmetric):
    seq = layers if not symmetric else layers
    W = np.eye(4, dtype=complex)
    if symmetric:
        half = [expm(-1j * eps / 2 * scp.H_of_k(l, k)) for l in layers]
        for U in half:
            W = U @ W
        for U in reversed(half):
            W = U @ W
    else:
        for l in layers:
            W = expm(-1j * eps * scp.H_of_k(l, k)) @ W
    return W


def quasi(k, eps, symmetric):
    w = np.linalg.eigvals(floquet(k, eps, symmetric))
    return np.sort(np.abs(np.angle(w)) / eps)


from scipy.linalg import logm


def heff_random(k, eps, n_orders=120, seed=3):
    """average effective Hamiltonian (i/eps) log W over random update orders of the layers"""
    r = np.random.default_rng(seed)
    acc = np.zeros((4, 4), dtype=complex)
    for _ in range(n_orders):
        W = np.eye(4, dtype=complex)
        for li in r.permutation(len(layers)):
            W = expm(-1j * eps * scp.H_of_k(layers[li], k)) @ W
        acc += 1j * logm(W) / eps
    return acc / n_orders


def speeds_random(eps):
    h = 1e-4
    e0 = np.min(np.abs(np.linalg.eigvalsh((heff_random(X, eps) + heff_random(X, eps).conj().T) / 2)))
    vs = []
    for d in np.eye(3)[:2]:
        Hm = heff_random(X + h * d, eps)
        vs.append((np.min(np.abs(np.linalg.eigvalsh((Hm + Hm.conj().T) / 2))) - e0) / h)
    return e0, vs


print(f"3. ELECTRON events: {len(nn_layers)} bond-direction layers (each junction updates one bond per layer) + "
      f"{len(soc_layers)} spin-orbit layers")
print("   continuous time: 4-fold zero (massless Dirac) at X")
for eps in (0.05, 0.1, 0.2, 0.4):
    for sym in (False, True):
        e0 = quasi(X, eps, sym)
        # search a small neighbourhood for the node (it may move)
        best = min(np.min(quasi(X + d, eps, sym)) for d in np.r_[[np.zeros(3)], 0.02 * np.random.default_rng(0).normal(size=(300, 3))])
        h = 1e-4
        vx = (np.min(quasi(X + h * np.array([1, 0, 0]), eps, sym)) - e0[0]) / h
        vy = (np.min(quasi(X + h * np.array([0, 1, 0]), eps, sym)) - e0[0]) / h
        print(f"   step eps = {eps:4.2f} {'symmetric ' if sym else 'sequential'}: lowest |quasi-energy| at X = {e0[0]:.1e}"
              f" (x{int(np.sum(e0 < 1e-6))} zero), min nearby {best:.1e}; cone speeds v_x {vx:.2f}, v_y {vy:.2f}"
              f"  (anisotropy {abs(1 - vx / vy):.4f})")
    e0r, (vxr, vyr) = speeds_random(eps)
    print(f"   step eps = {eps:4.2f} RANDOM order : gap {e0r:.1e}; cone speeds v_x {vxr:.2f}, v_y {vyr:.2f}"
          f"  (anisotropy {abs(1 - vxr / vyr):.4f})")
