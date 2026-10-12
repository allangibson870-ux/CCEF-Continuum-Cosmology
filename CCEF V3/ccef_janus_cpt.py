#!/usr/bin/env python3
"""
ccef_janus_cpt.py  --  matter and antimatter in a CPT-symmetric (Janus-point) universe.

1. GRAIN CHECK: adding the CP-odd junction-chirality coupling lambda*chi breaks C, P, T separately but keeps CPT
   (needed for a CPT-symmetric Janus universe).
2. JANUS TOY: a quantum 'universe' with sectors B = +1 (matter, dim m), B = -1 (antimatter, dim m), B = 0 (neutral, dim m0).
   C swaps the B = +1 and B = -1 sectors; T = complex conjugation; CPT = Theta = C K.
   H(t) = H0 + g(t) V:  H0 block-diagonal (B conserved);  V couples B = 0 <-> B = +-1 (baryon violation).
   CPT invariance:  V(0,-) = V(0,+)^*,  A(-,-) = A(+,+)^*.   CP-symmetric laws: all real.
   g(t) = g0 exp(-(t/tau)^2): baryon violation active only near the Janus point, off as the universe cools away from it
   (on BOTH sides).  The universal state is CPT-invariant at t = 0 (Theta psi0 = psi0, so <B>(0) = 0 exactly).
   Evolve forward and backward from t = 0; report the frozen asymmetry <B>(+inf) and <B>(-inf).
   Cases: (a) CP-symmetric laws and state; (b) CP-symmetric laws, CP-odd phase in the Janus state;
          (c) CP-violating laws, CP-symmetric state; (d) as (b) but baryon violation never switches off.
"""

import itertools

import numpy as np
from scipy.linalg import expm

# ------------------------------------------------------------------ 1. grain CPT check (single junction)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.array([[1, 0], [0, -1]], dtype=complex)
sp = np.array([[0, 1], [0, 0]], dtype=complex)
n = 4


def op(o, i):
    m = [np.eye(2)] * n
    m[i] = o
    out = m[0]
    for x in m[1:]:
        out = np.kron(out, x)
    return out


S = [[0.5 * op(s, i) for s in (sx, sy, sz)] for i in range(n)]


def chi(i, j, k):
    a, b, c = S[i], S[j], S[k]
    cr = [b[1] @ c[2] - b[2] @ c[1], b[2] @ c[0] - b[0] @ c[2], b[0] @ c[1] - b[1] @ c[0]]
    return sum(a[m] @ cr[m] for m in range(3))


CHI = chi(0, 1, 2) - chi(0, 1, 3) + chi(0, 2, 3) - chi(1, 2, 3)
Q = sum(op(sz, i) for i in range(n)) / 2
SP = [op(sp, i) for i in range(n)]
H = 0.5 * Q @ Q
for i, j in itertools.combinations(range(n), 2):
    H = H + 0.05 * (SP[i] @ SP[j].conj().T + SP[j] @ SP[i].conj().T)
H = H + 0.01 * CHI
C = np.eye(1)
for i in range(n):
    C = np.kron(C, sx)
P = np.zeros((16, 16))
for s in range(16):
    b = [(s >> (n - 1 - i)) & 1 for i in range(n)]
    b[2], b[3] = b[3], b[2]
    P[sum(x << (n - 1 - i) for i, x in enumerate(b)), s] = 1
U = C @ P                                     # unitary part of CPT; CPT acts as  H -> U H^* U^T
print("1. GRAIN CHECK: junction Hamiltonian + 0.01 * chirality (CP-odd coupling)")
print(f"   C: {np.allclose(C @ H @ C.T, H)}   P: {np.allclose(P @ H @ P.T, H)}   T: {np.allclose(H.conj(), H)}   "
      f"CP: {np.allclose(U @ H @ U.T, H)}   CPT: {np.allclose(U @ H.conj() @ U.T, H)}")
print("   -> CP and T are broken, CPT holds: a CP-violating grain universe can still be CPT-symmetric about a Janus point\n")

# ------------------------------------------------------------------ 2. Janus toy
rng = np.random.default_rng(7)
m, m0 = 40, 40
D = 2 * m + m0
Bop = np.diag([1.0] * m + [-1.0] * m + [0.0] * m0)


def sym(M):
    return (M + M.T) / 2


A_real = sym(rng.normal(size=(m, m)))
A_cpv = A_real + 0.0 * 1j
D0 = sym(rng.normal(size=(m0, m0)))
W_real = rng.normal(size=(m0, m)) / np.sqrt(m)
W_phase = W_real * np.exp(1j * rng.uniform(-0.6, 0.6, size=(m0, m)))


def build(A, W):
    H0 = np.zeros((D, D), dtype=complex)
    H0[:m, :m] = A
    H0[m:2 * m, m:2 * m] = A.conj()                # CPT: A(-,-) = A(+,+)^*
    H0[2 * m:, 2 * m:] = D0
    V = np.zeros((D, D), dtype=complex)
    V[2 * m:, :m] = W                              # B = 0 <-> B = +1
    V[2 * m:, m:2 * m] = W.conj()                  # CPT: V(0,-) = V(0,+)^*
    V = V + V.conj().T
    return H0, V


Cm = np.zeros((D, D))
Cm[:m, m:2 * m] = np.eye(m)
Cm[m:2 * m, :m] = np.eye(m)
Cm[2 * m:, 2 * m:] = np.eye(m0)


def cpt_check(H0, V):
    return np.allclose(Cm @ H0.conj() @ Cm.T, H0) and np.allclose(Cm @ V.conj() @ Cm.T, V)


def cpt_state(phi):
    """Theta psi = psi with Theta = C K: psi_- = psi_+^*, psi_0 real.  phi = CP-odd phase of the matter components."""
    base = rng.normal(size=m) / np.sqrt(m)
    psi = np.zeros(D, dtype=complex)
    psi[:m] = 0.3 * base * np.exp(1j * phi)
    psi[m:2 * m] = np.conj(psi[:m])
    psi[2 * m:] = rng.normal(size=m0)
    return psi / np.linalg.norm(psi)


def evolve(H0, V, psi0, g0=0.8, tau=6.0, tmax=40.0, dt=0.1, always_on=False):
    out = {}
    for sgn in (+1, -1):
        psi = psi0.copy()
        ts, bs = [0.0], [np.real(psi.conj() @ Bop @ psi)]
        t = 0.0
        while t < tmax - 1e-9:
            tm = t + dt / 2
            g = g0 if always_on else g0 * np.exp(-(tm / tau) ** 2)
            psi = expm(-1j * sgn * dt * (H0 + g * V)) @ psi
            t += dt
            ts.append(sgn * t)
            bs.append(np.real(psi.conj() @ Bop @ psi))
        out[sgn] = (np.array(ts), np.array(bs))
    return out


cases = []
Hs, Vs = build(A_real, W_real)
Hc, Vc = build(A_cpv, W_phase)
s_sym = cpt_state(0.0)
rng = np.random.default_rng(7)
s_cpodd = cpt_state(0.5)
print("2. JANUS TOY (CPT-invariant laws and CPT-invariant state at t = 0)")
print(f"   CPT invariance of the laws: CP-symmetric {cpt_check(Hs, Vs)}, CP-violating {cpt_check(Hc, Vc)}")
for label, H0, V, psi, on in (("(a) CP-symmetric laws, CP-symmetric Janus state", Hs, Vs, s_sym, False),
                              ("(b) CP-symmetric laws, CP-odd phase in Janus state", Hs, Vs, s_cpodd, False),
                              ("(c) CP-violating laws, CP-symmetric Janus state", Hc, Vc, s_sym, False),
                              ("(d) as (b), baryon violation NEVER switches off", Hs, Vs, s_cpodd, True)):
    r = evolve(H0, V, psi, always_on=on)
    Bp, Bm = r[+1][1], r[-1][1]
    late = slice(-100, None)
    print(f"   {label:52s} <B>(0) = {Bp[0]:+.1e};  our side late <B> = {Bp[late].mean():+.4f} "
          f"(spread {Bp[late].std():.4f});  mirror side late <B> = {Bm[late].mean():+.4f}")
    cases.append((label, Bp, Bm))
print("   (in (d) the 'late' value is a time average while baryon violation stays on)")

# erasure in the long run: diagonal-ensemble value of B for the always-on Hamiltonian
e, v = np.linalg.eigh(Hs + 0.8 * Vs)
cn = v.conj().T @ s_cpodd
diagB = np.real(np.sum(np.abs(cn) ** 2 * np.einsum("ij,ij->j", v.conj(), Bop @ v)))
print(f"   long-time (diagonal-ensemble) <B> with baryon violation always on: {diagB:+.1e}  (CPT forces eigenstates to have <B> = 0)")
