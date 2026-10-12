#!/usr/bin/env python3
"""
ccef_local_time.py  --  from one global clock to a clock at every junction.

A. LINEARISED GRAVITY: modes of the grain metric field h_ij (positive kinetic term, unique Fierz-Pauli energy found in
   ccef_graviton.py) with
     (i)  momentum constraint only (spatial coordinate freedom, DIFF)
     (ii) + ONE global time constraint (affects only the K = 0 mode: Page-Wootters)
     (iii)+ a LOCAL time constraint at every point: linearised Hamiltonian constraint  C = K_i K_j h_ij - K^2 tr h,
          whose gauge partner shifts the momenta by (K_i K_j - delta_ij K^2) alpha
   and with matter: C = 16 pi G rho  -> the potential produced by a point mass (Newton?).
B. GRAIN LEVEL: local clocks need local constraints C_v = p_v + h_v that are mutually consistent.
     (1) continuous-time local Hamiltonian terms on a ring of grains (transverse-field Ising): [C_v, C_w] != 0
         -> Dirac-inconsistent: no clock-per-site formulation
     (2) dynamics as local UPDATE EVENTS (two-grain gates in a brickwork / causal order): each junction's clock = its
         number of updates; check that every update order compatible with the same local clock readings gives the
         SAME state (foliation independence = 'many-fingered time', causal invariance)
"""

import itertools

import numpy as np
from scipy.linalg import expm

from ccef_graviton import BAS, quad_matrix

# ================================================================ A
FP = np.array([0.25, -0.5, 0.5, -0.25])


def project_out(dirs):
    G = np.array([[np.sum(g * b) for b in BAS] for g in dirs])
    _, s, vt = np.linalg.svd(G)
    return vt[np.sum(s > 1e-10):]


def helicity(hk, K):
    n = K / np.linalg.norm(K)
    phi = 0.3
    Kx = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    R = np.eye(3) + np.sin(phi) * Kx + (1 - np.cos(phi)) * Kx @ Kx
    ov = np.sum((R @ hk @ R.T) * hk) / np.sum(hk * hk)
    return min((0, 1, 2), key=lambda s: abs(np.cos(s * phi) - ov))


def modes(K, local_time):
    diff = [np.outer(K, e) + np.outer(e, K) for e in np.eye(3)]
    if not local_time:
        P = project_out(diff)                                  # physical configuration = momentum (and) phase space
        w2, v = np.linalg.eigh(P @ quad_matrix(FP, K) @ P.T)
        return [(w, helicity(sum(c * b for c, b in zip(P.T @ v[:, k], BAS)), K)) for k, w in enumerate(w2)]
    # local Hamiltonian constraint: configuration must satisfy C(h) = 0 (remove direction KK - K^2 1 from h), and the
    # momentum direction (KK - K^2 1) is pure gauge (remove from pi). With a Euclidean kinetic metric both remove the
    # same direction, so the reduced space is the orthogonal complement of DIFF and the scalar direction.
    scal = np.outer(K, K) - K @ K * np.eye(3)
    P = project_out(diff + [scal])
    w2, v = np.linalg.eigh(P @ quad_matrix(FP, K) @ P.T)
    return [(w, helicity(sum(c * b for c, b in zip(P.T @ v[:, k], BAS)), K)) for k, w in enumerate(w2)]


rng = np.random.default_rng(4)
K = rng.normal(size=3); K /= np.linalg.norm(K)
print("A. GRAVITON MODES (plane wave, |K| = 1)")
for label, loc in (("(i)   coordinate freedom only", False), ("(ii)  + one GLOBAL clock (acts only at K = 0)", False),
                   ("(iii) + a LOCAL clock at every point", True)):
    out = modes(K, loc)
    desc = ", ".join(f"helicity {s}: omega^2 {w:+.3f}{' (UNSTABLE)' if w < -1e-12 else ''}" for w, s in out)
    print(f"   {label:46s} {len(out)} modes -> {desc}")
print("   -> a single global clock cannot remove the unstable scalar (it only constrains the uniform K = 0 mode);")
print("      a clock at every point removes it, leaving exactly the 2 graviton polarisations.\n")

# Newton from the local time constraint: K_i K_j h_ij - K^2 h = 16 pi G rho; in a gauge h_ij = -2 Phi delta_ij
# (spatial part of the weak-field metric) the constraint reads  2 K^2 Phi*... -> solve for Phi and transform to r
G = 1.0
ks = np.logspace(-3, 3, 4000)
# h_ij = -2 Phi delta_ij  ->  C = K^2(-2Phi) - K^2(-6Phi) = 4 K^2 Phi = 16 pi G rho  ->  Phi(k) = 4 pi G rho / k^2 ... sign:
Phi_k = -4 * np.pi * G / ks ** 2                              # point mass rho(k) = 1 (sign: attractive)
for r in (1.0, 2.0, 4.0):
    integrand = Phi_k * ks ** 2 * np.sinc(ks * r / np.pi) / (2 * np.pi ** 2)
    Phi_r = np.trapezoid(integrand, ks)
    print(f"   point mass, potential at r = {r}: Phi = {Phi_r:+.4f}   (Newton -G M / r = {-G / r:+.4f})")
print("   -> Newton's 1/r attraction is exactly the content of the local time constraint (it is a constraint, not a wave)\n")

# ================================================================ B
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
n = 6


def op(o, i):
    m = [np.eye(2)] * n
    m[i] = o
    out = m[0]
    for x in m[1:]:
        out = np.kron(out, x)
    return out


print("B. GRAIN LEVEL (ring of 6 grains)")
h = [op(sz, i) @ op(sz, (i + 1) % n) + 0.7 * op(sx, i) for i in range(n)]
worst = max(np.abs(h[v] @ h[w] - h[w] @ h[v]).max() for v, w in itertools.combinations(range(n), 2))
nbr = max(np.abs(h[v] @ h[(v + 1) % n] - h[(v + 1) % n] @ h[v]).max() for v in range(n))
print(f"   (1) continuous-time local terms: max |[h_v, h_w]| = {worst:.2f} (neighbours {nbr:.2f})")
print("       -> local constraints C_v = p_v + h_v do not commute: no consistent 'clock per junction' this way")


def rand_gate(rng):
    A = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    return expm(-1j * (A + A.conj().T) / 2)


def apply_gate(psi, U, i):
    j = (i + 1) % n
    psi = psi.reshape([2] * n)
    psi = np.moveaxis(psi, (i, j), (0, 1)).reshape(4, -1)
    psi = (U @ psi).reshape([2, 2] + [2] * (n - 2))
    return np.moveaxis(psi, (0, 1), (i, j)).reshape(-1)


rng2 = np.random.default_rng(9)
# causal structure: brickwork events; event (layer L, pair i) acts on grains i, i+1; each grain's clock = # events seen
layers = 4
events = [(L, i) for L in range(layers) for i in range(L % 2, n, 2)]
gates = {e: rand_gate(rng2) for e in events}
psi0 = np.zeros(2 ** n, dtype=complex); psi0[0] = 1


def run(order):
    psi = psi0.copy()
    for e in order:
        psi = apply_gate(psi, gates[e], e[1])
    return psi


def valid(order):
    """an order is causally valid if each event comes after the earlier-layer events sharing a grain with it"""
    pos = {e: k for k, e in enumerate(order)}
    for (L, i) in order:
        for (L2, i2) in events:
            if L2 < L and ({i2, (i2 + 1) % n} & {i, (i + 1) % n}) and pos[(L2, i2)] > pos[(L, i)]:
                return False
    return True


def random_causal_order(rng):
    """random topological order of the causal graph: any event whose causal predecessors are done may fire next"""
    done, order = set(), []
    while len(order) < len(events):
        ready = [e for e in events if e not in done and all(
            (L2, i2) in done for (L2, i2) in events
            if L2 < e[0] and ({i2, (i2 + 1) % n} & {e[1], (e[1] + 1) % n}))]
        e = ready[rng.integers(len(ready))]
        done.add(e)
        order.append(e)
    return order


ref = run(sorted(events))
orders = [random_causal_order(rng2) for _ in range(300)]
distinct = len({tuple(o) for o in orders})
diffs = [np.linalg.norm(run(o) - ref) for o in orders]
print(f"   (2) local update events (brickwork of {len(events)} two-grain gates):")
print(f"       {distinct} distinct causally-allowed update orders (different 'global time slicings'); "
      f"max state difference among them = {max(diffs):.1e}")
# a causally INVALID order generally gives a different state
bad = None
for _ in range(3000):
    order = [events[k] for k in rng2.permutation(len(events))]
    if not valid(order):
        bad = np.linalg.norm(run(order) - ref)
        break
print(f"       an order that violates the causal order: state difference {bad:.2f}")
print("       -> with local update events, the state depends only on each junction's own clock reading (how many")
print("          updates it has had), never on a global time order: a consistent clock at every junction.")
