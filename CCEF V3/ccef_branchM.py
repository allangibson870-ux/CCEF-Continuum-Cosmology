#!/usr/bin/env python3
"""
ccef_branchM.py  --  rebuild CCEF Branch M (minimal string-net rules: no Z3 lepton triality) as one package and test it.

Branch M: proton decays via local dimension-6 junctions at Lambda*; Majorana nu^c masses allowed (seesaw / Weinberg
operator at Lambda*); standard thermal leptogenesis available.  Inputs carried over: reheating T_RH ~ 1e19 GeV
(CCEF_reheat.md), area-law ripples A_s = (9/4) 4.39 c (T_f/M)^2 with T_f = Lambda* (CCEF_ripples.md).
"""

import math

import numpy as np

M, v = 1.767e19, 174.0
dm21, dm31, dm32IO = 7.42e-5, 2.51e-3, 2.49e-3
TAU_SK, TAU_HK = 2.4e34, 8e34                      # Super-K limit; Hyper-K ~20-yr 3-sigma reach (approx.)
m3 = math.sqrt(dm31)

print("1. NEUTRINO MASS SETS THE CROSSOVER: Weinberg operator / seesaw at Lambda*, m3 = k v^2 / Lambda*")
rows = []
for k in (0.3, 1.0, 3.0):
    L = k * v ** 2 / (m3 * 1e-9)
    rows.append((k, L))
    print(f"   k = {k:3.1f}: Lambda* = {L:.1e} GeV")
L0 = v ** 2 / (m3 * 1e-9)

print("\n2. PROTON DECAY  tau = 8.7e35 yr (Lambda*/1e16)^4 / C^2   (C = junction coefficient)")
for k, L in rows:
    Cmax = math.sqrt(8.7e35 * (L / 1e16) ** 4 / TAU_SK)
    Chk = math.sqrt(8.7e35 * (L / 1e16) ** 4 / TAU_HK)
    print(f"   Lambda* = {L:.1e}: Super-K needs C <= {Cmax:.3f}; Hyper-K discovers it if C >= {Chk:.3f}"
          f"  -> window {Chk:.3f} < C < {Cmax:.3f}")

print("\n3. PRIMORDIAL RIPPLES (area-law, frozen at T_f = Lambda*):  A_s = 9.9 c (Lambda*/M)^2 = 2.1e-9")
for k, L in rows:
    c = 2.1e-9 / (9.88 * (L / M) ** 2)
    print(f"   Lambda* = {L:.1e}: needs c = {c:.3f}")

print("\n4. LORENTZ PROTECTION (Mechanism A): gamma >= 23 / log10(M / Lambda*)")
for k, L in rows:
    print(f"   Lambda* = {L:.1e}: gamma >= {23 / math.log10(M / L):.2f}")

print("\n5. MATTER-ANTIMATTER: thermal leptogenesis (Majorana nu^c, M1 ~ 0.1-1 Lambda*, T_RH ~ 1e19 >> M1)")
for frac in (0.1, 1.0):
    M1 = frac * L0
    eps_max = 3 / (16 * math.pi) * M1 * (m3 * 1e-9) / v ** 2
    K = 0.05 / 1.08e-3
    kappa = 0.02 / K ** 1.1 if K > 1 else 1
    etaB = 0.96e-2 * eps_max * kappa
    print(f"   M1 = {M1:.1e} GeV: Davidson-Ibarra eps_max = {eps_max:.2f}; washout K ~ {K:.0f} -> efficiency ~{kappa:.0e};"
          f" max eta_B ~ {etaB:.0e} (needed 6e-10) -> {'WORKS' if etaB > 6e-10 else 'fails'}")

print("\n6. NEUTRINOS: Majorana anarchy (flavour-blind grains), 4e6 random complex-symmetric mass matrices")
rng = np.random.default_rng(3)
NO, IO = [], []
for _ in range(8):
    n = 500_000
    A = (rng.standard_normal((n, 3, 3)) + 1j * rng.standard_normal((n, 3, 3))) / math.sqrt(2)
    Mm = (A + np.transpose(A, (0, 2, 1))) / 2
    s = np.sort(np.linalg.svd(Mm, compute_uv=False), axis=1)
    s2 = s ** 2
    rNO = (s2[:, 1] - s2[:, 0]) / (s2[:, 2] - s2[:, 0])
    rIO = (s2[:, 2] - s2[:, 1]) / (s2[:, 2] - s2[:, 0])
    r = dm21 / dm31
    mNO = np.abs(np.log(rNO / r)) < 0.15
    mIO = np.abs(np.log(rIO / r)) < 0.15
    NO.append(np.c_[s[mNO], np.abs(Mm[mNO, 0, 0])])
    IO.append(np.c_[s[mIO], np.abs(Mm[mIO, 0, 0])])
NO, IO = np.concatenate(NO), np.concatenate(IO)
print(f"   ordering odds normal : inverted = {len(NO) / max(len(IO), 1):.1f} : 1")
eps = np.sqrt(dm31 / (NO[:, 2] ** 2 - NO[:, 0] ** 2))
sumNO = eps * NO[:, :3].sum(1)
mbb = eps * NO[:, 3]
q = lambda x: np.percentile(x, [16, 50, 84])
print(f"   normal ordering: sum m_nu = {q(sumNO * 1e3).round(1)} meV (16/50/84%); lightest {q(eps * NO[:, 0] * 1e3).round(1)} meV")
print(f"   neutrinoless double-beta m_bb = {q(mbb * 1e3).round(1)} meV;  P(m_bb > 10 meV) = {np.mean(mbb > 0.010):.2f},"
      f"  P(m_bb > 20 meV) = {np.mean(mbb > 0.020):.2f}  (LEGEND-1000 / nEXO reach ~10-20 meV)")
epsI = np.sqrt(dm32IO / (IO[:, 2] ** 2 - IO[:, 0] ** 2))
print(f"   inverted ordering (less likely): m_bb median {np.median(epsI * IO[:, 3]) * 1e3:.0f} meV")

print("\n7. DARK MATTER AND STRONG CP")
for k, L in rows:
    over = (L / 1.4e11) ** 1.165
    print(f"   axion with f_a = Lambda* = {L:.1e} (post-inflation, forced by T_RH >> f_a): overproduces dark matter ~x{over:.0e}")
print("   -> Branch M cannot use f_a = Lambda*: needs a separate PQ scale ~1e10-1e11 GeV (unexplained) or another DM")
print("   heavy right-handed neutrino DM (Boyle-Finn-Turok style, ~5e8 GeV): thermalised at T_RH ~ M, cannot annihilate -> overcloses")

print("\n8. RELIC RADIATION: nu^c are heavy (Majorana) -> no nu^c contribution; thermal gravitons Delta N_eff ~ 0.05")

print("\n9. BOTH BRANCHES - Planck-mass black-hole remnants after a Planck-hot start:")
for frac in (0.3, 0.5):
    d = frac ** 1.5
    beta = math.erfc(0.45 / d)
    print(f"   T_RH = {frac} M: grain-count fluctuations delta ~ {d:.2f} -> formation fraction ~{beta:.0e} (DM allows ~1e-28)")
print("   -> if Planck-scale black holes leave STABLE remnants, a Planck-hot start overcloses the universe by ~1e26:")
print("      CCEF needs complete evaporation (no stable remnants); the 'remnant dark matter' option is excluded in both branches")
