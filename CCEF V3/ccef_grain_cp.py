#!/usr/bin/env python3
"""
ccef_grain_cp.py  --  can grains carry CP violation?

Grain-level symmetries (quantum-spin-ice sector of the grain Hamiltonian):
  C  = prod sigma^x   (electric field sigma^z -> -sigma^z, charge Q -> -Q)
  T  = complex conjugation in the sigma^z basis (antiunitary)
  P  = an improper geometric map; at a single 4-grain junction: a mirror swapping two grains
Emergent Lorentz invariance + locality -> CPT, so CP violation <=> T violation.

1. Audit: the junction Hamiltonian H = (Jzz/2) Q^2 - Jpm sum_{i<j} (e^{i phi_ij} s+_i s-_j + h.c.)
   commutes with C, T, P for real couplings (phi = 0).  Phases phi_ij that are not 'pure gauge' (net flux through a
   triangle of grains) break T and P.
2. Spontaneous route: for the frustrated sign of the exchange (Jpm < 0) the junction ground state is a 2-fold doublet;
   is it labelled by the scalar spin chirality chi = S1.(S2 x S3)  (C-even, P-odd, T-odd -> CP-odd)?
3. Explicit route: a small flux through the junction's triangles splits the doublet and picks a chirality sign.
4. Phase counting: CP phases in the junction (Yukawa) amplitudes for N generations; the Delta B = 2 junction.
"""

import itertools

import numpy as np

sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.array([[1, 0], [0, -1]], dtype=complex)
sp = np.array([[0, 1], [0, 0]], dtype=complex)
I2 = np.eye(2)
n = 4


def op(o, i):
    mats = [I2] * n
    mats[i] = o
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


S = [[0.5 * op(s, i) for s in (sx, sy, sz)] for i in range(n)]
SP = [op(sp, i) for i in range(n)]
Q = sum(op(sz, i) for i in range(n)) / 2


def H(Jzz=1.0, Jpm=0.05, phi=None):
    h = 0.5 * Jzz * Q @ Q
    for i, j in itertools.combinations(range(n), 2):
        ph = np.exp(1j * (phi.get((i, j), 0.0) if phi else 0.0))
        h = h - Jpm * (ph * SP[i] @ SP[j].conj().T + np.conj(ph) * SP[j] @ SP[i].conj().T)
    return h


def chi(i, j, k):
    a, b, c = S[i], S[j], S[k]
    cross = [b[1] @ c[2] - b[2] @ c[1], b[2] @ c[0] - b[0] @ c[2], b[0] @ c[1] - b[1] @ c[0]]
    return sum(a[m] @ cross[m] for m in range(3))


# total junction chirality: sum over the 4 triangles of the tetrahedron, consistently oriented
CHI = chi(0, 1, 2) - chi(0, 1, 3) + chi(0, 2, 3) - chi(1, 2, 3)
C_op = np.eye(1)
for i in range(n):
    C_op = np.kron(C_op, sx)
# mirror swapping grains 2 and 3
P_op = np.zeros((16, 16))
for s in range(16):
    bits = [(s >> (n - 1 - i)) & 1 for i in range(n)]
    bits[2], bits[3] = bits[3], bits[2]
    P_op[sum(b << (n - 1 - i) for i, b in enumerate(bits)), s] = 1


def fluxes(phi):
    f = {}
    g = lambda i, j: (phi.get((i, j), 0.0) if i < j else -phi.get((j, i), 0.0))
    for i, j, k in itertools.combinations(range(n), 3):
        f[(i, j, k)] = round((g(i, j) + g(j, k) + g(k, i) + np.pi) % (2 * np.pi) - np.pi, 6)
    return f


def audit(phi, label):
    h = H(Jpm=-0.05, phi=phi)
    e, v = np.linalg.eigh(h)
    f = fluxes(phi or {})
    t_ok = all(abs(x) < 1e-9 or abs(abs(x) - np.pi) < 1e-9 for x in f.values())
    c_ok = np.allclose(C_op @ h @ C_op.T, h) or not any(abs(x) > 1e-9 for x in f.values())
    print(f"   {label:46s} triangle fluxes {list(f.values())}  -> physical T (and CP) {'conserved' if t_ok else 'VIOLATED'}")


print("1. SYMMETRY AUDIT of the 4-grain junction (quantum-spin-ice sector). Only gauge-invariant data count:")
print("   the flux through each triangle of grains (edge phases that are pure gauge can be removed by rephasing grains)")
audit(None, "real couplings (grain Hamiltonian v1)")
alpha = (0.0, 0.3, 0.1, -0.2)
audit({(i, j): alpha[i] - alpha[j] for i, j in itertools.combinations(range(n), 2)}, "pure-gauge phases (phi_ij = a_i - a_j)")
audit({(0, 1): 0.2, (1, 2): 0.2, (0, 2): -0.0}, "phases with net flux through triangles")
print("   real Hamiltonian: C =", np.allclose(C_op @ H() @ C_op.T, H()), ", P =", np.allclose(P_op @ H() @ P_op.T, H()),
      ", T =", np.allclose(H().conj(), H()), " -> v1 conserves C, P, T separately")
print("   CHI (junction scalar chirality): C-even:", np.allclose(C_op @ CHI @ C_op.T, CHI), " T-odd:", np.allclose(CHI.conj(), -CHI),
      " P-odd:", np.allclose(P_op @ CHI @ P_op.T, -CHI), " -> CHI is CP-odd")
print("   note: the 4 faces of a junction form a closed surface, so edge-phase fluxes through them sum to zero:")
print("   edge phases can bias a single face's chirality but NOT the junction's total chirality CHI")

print("\n2. SPONTANEOUS ROUTE: ground states of one junction, Jzz = 1")
for Jpm in (+0.05, -0.05):
    e, v = np.linalg.eigh(H(Jpm=Jpm))
    deg = int(np.sum(np.abs(e - e[0]) < 1e-9))
    G = v[:, :deg]
    chis = np.linalg.eigvalsh(G.conj().T @ CHI @ G) if deg > 1 else [float(np.real(G[:, 0].conj() @ CHI @ G[:, 0]))]
    print(f"   Jpm = {Jpm:+.2f} ({'unfrustrated' if Jpm > 0 else 'frustrated'}): ground energy {e[0]:+.4f}, degeneracy {deg}, "
          f"gap {e[deg] - e[0]:.4f}; chirality values in ground space {np.round(chis, 4)}")

print("\n3. EXPLICIT ROUTE: a three-grain chiral coupling  H' = lambda * CHI  (T-odd, P-odd, CP-odd) on the frustrated junction")
for lam in (0.0, 1e-4, 1e-3, -1e-3):
    e, v = np.linalg.eigh(H(Jpm=-0.05) + lam * CHI)
    g = v[:, 0]
    print(f"   lambda = {lam:+.0e}: doublet splitting {e[1] - e[0]:.2e}, ground-state chirality <CHI> = {np.real(g.conj() @ CHI @ g):+.3f}")
print("   -> any CP-odd coupling, however small, picks one handedness for every junction (linear splitting)")

print("\n4. WHERE IRREMOVABLE PHASES CAN LIVE")
for N in (1, 2, 3, 4):
    print(f"   {N} generation(s): CP phases in the quark junction (Yukawa) amplitudes = (N-1)(N-2)/2 = {(N - 1) * (N - 2) // 2}")
print("   -> Branch L3's anomaly condition forces N = 3: exactly the minimum for one Kobayashi-Maskawa phase.")
print("   Delta B = 2 six-quark junction (u d d)(u d d) with 3 generations: many independent complex flavour coefficients;")
print("   only one overall phase can be removed (baryon-number rephasing) -> new CP phases at Lambda* are allowed, unconstrained.")
