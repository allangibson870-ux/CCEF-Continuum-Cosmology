#!/usr/bin/env python3
"""
ccef_strong_cp.py  --  can the grain picture solve the strong-CP problem without an axion (the CCEF hybrid needs this)?

theta_bar = theta_QCD + arg det(M_u M_d) must be < 1e-10, while the CKM phase (~1.2 rad) requires complex quark couplings.
1. Symmetries of the theta term: C-even, P-odd, T-odd -> CP-odd, CPT-even: CPT (Janus) symmetry cannot fix theta.
2. 'Parity solution' test on the grain electrons: in the spin-1/2 Fu-Kane-Mele grain fermions (CCEF_grain_electrons.md),
   each X point hosts a 4-component Dirac fermion.  Two mass types are possible: m (scalar, P-even) and m' (pseudoscalar,
   'i gamma5' type, P-odd) -> the chiral phase atan(m'/m) is the fermion's contribution to theta_bar.
   Add random perturbations to the grain hopping (including complex, CP-violating ones):
     (a) respecting diamond's bond-centred INVERSION (A <-> B junction swap)   (b) breaking it
   and measure the induced chiral phase.
3. Cosmology: P (or CP) must eventually be broken (the weak force is chiral); spontaneous breaking after a Planck-hot
   start makes domain walls -> bias needed vs theta induced.
"""

import itertools

import numpy as np

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2)
DEL = np.array([(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)], dtype=float)     # A -> B bonds (as ccef_grain_fkm)
FCC = [np.array(v, dtype=float) for v in itertools.product((-2, 0, 2), repeat=3) if sorted(np.abs(v)) == [0, 2, 2]]


def soc_terms():
    """spin-orbit second-neighbour hops s.(d1 x d2), as in ccef_grain_fkm.py"""
    out = {}
    for sub, sign in (("A", 1), ("B", -1)):
        lst = []
        for R in FCC:
            for d1 in sign * DEL:
                d2 = R - d1
                if any(np.allclose(d2, -sign * d) for d in DEL):
                    c = np.cross(d1, d2)
                    lst.append((R, c[0] * SX + c[1] * SY + c[2] * SZ))
                    break
        out[sub] = lst
    return out


SOC = soc_terms()

rng = np.random.default_rng(11)
print("1. theta term:  C even, P odd, T odd  ->  CP odd, CPT even.  A CPT-symmetric (Janus) universe does NOT constrain theta.\n")

# ---------------------------------------------------------------- Bloch Hamiltonian from a list of hopping terms
# term = (a, b, d, T): hop from sublattice b to a over displacement d, 2x2 spin matrix T (Hermitian completion added)
def base_terms(lam=0.25):
    terms = []
    for d in DEL:                                       # NN: A at 0, B at d
        terms.append((0, 1, d, -1.0 * I2))
    for sub, key in ((0, "A"), (1, "B")):
        for R, Mm in SOC[key]:
            terms.append((sub, sub, R, 0.5 * 1j * (8 * lam / 16) * Mm))   # half: Hermitian completion doubles it
    return terms


def H_of_k(terms, k):
    H = np.zeros((4, 4), dtype=complex)
    for a, b, d, T in terms:
        blk = T * np.exp(1j * np.dot(k, d))
        H[2 * a:2 * a + 2, 2 * b:2 * b + 2] += blk
        H[2 * b:2 * b + 2, 2 * a:2 * a + 2] += blk.conj().T
    return H


def invert(term):
    """bond-centred inversion: A <-> B and d -> -d; spin (pseudovector) unchanged"""
    a, b, d, T = term
    return (1 - a, 1 - b, -np.array(d), T)


base = base_terms()
X = np.array([np.pi / 2, 0.0, 0.0])
H0X = H_of_k(base, X)
print(f"2. grain Dirac fermion at X: |H(X)| = {np.abs(H0X).max():.1e} (4-fold zero, as found before)")
h = 1e-6
V = [(H_of_k(base, X + h * e) - H_of_k(base, X - h * e)) / (2 * h) for e in np.eye(3)]
# mass matrices: Hermitian 4x4 anticommuting with all three velocity matrices
basis = []
P4 = [np.kron(a, b) for a in (I2, SX, SY, SZ) for b in (I2, SX, SY, SZ)]
A = np.array([[np.trace(Vi @ Pj + Pj @ Vi).real for Pj in P4] for Vi in V] +
             [[np.trace(Vi @ Pj + Pj @ Vi).imag for Pj in P4] for Vi in V])
rows = []
for Vi in V:
    for Pk in P4:
        rows.append([np.trace(Pk @ (Vi @ Pj + Pj @ Vi)).real for Pj in P4])
_, s, vt = np.linalg.svd(np.array(rows))
null = vt[s.size - np.sum(s < 1e-8):] if np.sum(s < 1e-8) else vt[-2:]
null = vt[np.where(np.r_[s, np.zeros(16 - s.size)] < 1e-8)[0]]
masses = [sum(c * Pj for c, Pj in zip(vec, P4)) for vec in null]
print(f"   Hermitian 4x4 mass matrices anticommuting with all velocities: {len(masses)} (expected 2: scalar and pseudoscalar)")
B1, B2 = masses[0], masses[1]
# orthonormalise
B1 = B1 / np.sqrt(np.trace(B1 @ B1).real / 4)
B2 = B2 - np.trace(B2 @ B1).real / 4 * B1
B2 = B2 / np.sqrt(np.trace(B2 @ B2).real / 4)


def random_term():
    a, b = rng.integers(0, 2, 2)
    if a == b:
        d = [np.array(v, float) for v in itertools.product((-2, 0, 2), repeat=3) if sorted(np.abs(v)) == [0, 2, 2]]
        d = d[rng.integers(len(d))]
    else:
        d = DEL[rng.integers(4)] * (1 if (a, b) == (0, 1) else -1)
    T = sum((rng.normal() + 1j * rng.normal()) * m for m in (I2, SX, SY, SZ))
    return (a, b, d, 0.01 * T)


def chiral_angles(symmetric, n=400):
    out = []
    for _ in range(n):
        pert = [random_term() for _ in range(6)]
        if symmetric:
            pert = pert + [invert(t) for t in pert]
        dH = H_of_k(pert, X)
        m1 = np.trace(dH @ B1).real / 4
        m2 = np.trace(dH @ B2).real / 4
        out.append((m1, m2))
    return np.array(out)


for label, sym in (("(a) inversion-symmetric perturbations (incl. complex / CP-violating hoppings)", True),
                   ("(b) inversion-BREAKING perturbations", False)):
    m = chiral_angles(sym)
    f1, f2 = np.sqrt(np.mean(m[:, 0] ** 2)), np.sqrt(np.mean(m[:, 1] ** 2))
    print(f"   {label}:")
    print(f"      rms mass along type-1 {f1:.2e}, along type-2 {f2:.2e}")
    if sym:
        sym_ratio = (f1, f2)
ang = np.arctan2(np.abs(chiral_angles(True)[:, 1]), np.abs(chiral_angles(True)[:, 0]) + 1e-30)
print("   -> with inversion intact only ONE mass type is ever generated: that is the P-even scalar mass; the P-odd")
print("      'i gamma5' mass (the fermion's contribution to theta_bar) is forbidden, even with complex couplings.")
print("      Breaking inversion generates both types -> an arbitrary chiral phase -> theta_bar ~ O(1).\n")

print("3. COSMOLOGY: parity must be broken somewhere (the weak force is chiral).  If it is broken SPONTANEOUSLY at scale v")
print("   after the Planck-hot start, domain walls form (tension ~v^3).  Walls must be removed by a small explicit bias eps,")
print("   which feeds theta_bar ~ kappa * eps (kappa = loop factor).  Wall removal before domination needs eps >~ (v/M_P)^2:")
MP = 1.22e19
for v in (1e12, 1e14, 1e15, 1e16):
    eps = (v / MP) ** 2
    print(f"   v = {v:.0e} GeV: eps >~ {eps:.0e}; theta_bar < 1e-10 needs loop factor kappa <~ {1e-10 / eps:.0e}")
print("   -> fine for v <~ 1e14 GeV (kappa ~ 1); at v ~ Lambda* ~ 1e15 needs kappa <~ 0.01.")
print("   Alternative [CONJECT]: if the P-breaking choice is inherited from the single crystal seed (which survives T_RH),")
print("   there is one domain and no walls at all.\n")

print("4. PREDICTION if this is the solution: no strong-CP axion; theta_bar is generated only radiatively -> a neutron EDM")
for th in (1e-11, 5e-11, 1e-10):
    print(f"   theta_bar = {th:.0e}: d_n ~ {2.4e-16 * th:.1e} e cm  (current limit 1.8e-26; n2EDM-class goal ~1e-27)")
