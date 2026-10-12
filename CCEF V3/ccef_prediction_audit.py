#!/usr/bin/env python3
"""
ccef_prediction_audit.py  --  audit of the frozen CCEF predictions after the computed N_eff (CCEF_neff.md).

The framework had assumed N_eff = 9 (grain length l = 0.69 l_P, grain scale M = 1.77e19 GeV).  The lattice computation
gives N_eff ~ 495 for the content CCEF builds (278 without mirror partners): l = sqrt(N_eff / 6 pi) l_P.
For every frozen prediction this script (0) checks the frozen files still match their recorded SHA-256 hashes,
(1) identifies whether the prediction depends on l / M / N_eff, (2) recomputes the dependent numbers with the SAME
formulas as the frozen code.  Frozen files are not modified.
"""

import hashlib
import math
import os
import re

MP, LP = 1.2209e19, 1.616255e-35
v, Y_NU = 174.0, 2.9e-13
CASES = (("assumed (frozen)", 9), ("computed, no mirrors", 278), ("computed, full content", 495))


def grain(Ne):
    r = math.sqrt(Ne / (6 * math.pi))
    return r * LP, MP / r


# ---------------------------------------------------------------- 0. hash integrity of the freeze records
print("0. FREEZE-RECORD INTEGRITY (recorded SHA-256 vs files on disk)")
for rec in sorted(f for f in os.listdir(".") if f.endswith("_prereg_hash.txt")):
    lines = open(rec, encoding="utf-8", errors="replace").read().splitlines()
    voided = any("VOIDED" in l for l in lines)
    entries = []
    for i, l in enumerate(lines):
        h = re.findall(r"\b[0-9A-Fa-f]{64}\b", l)
        f = re.findall(r"[\w.]+\.(?:py|md|json|txt)", l)
        if h and f:
            entries.append((i, f[0], h[0].lower()))
    if voided:                                   # keep only hashes recorded after the VOID line
        cut = max(i for i, l in enumerate(lines) if "VOIDED" in l)
        entries = [e for e in entries if e[0] > cut] or entries
    res = []
    for _, f, h in entries:
        if not os.path.exists(f):
            res.append(f"{f}: MISSING")
            continue
        ok = hashlib.sha256(open(f, "rb").read()).hexdigest() == h
        res.append(f"{f}: {'ok' if ok else 'CHANGED'}")
    print(f"   {rec:40s} " + "; ".join(res))

# ---------------------------------------------------------------- 1. grain scale
print("\n1. GRAIN SCALE  (l = sqrt(N_eff/6 pi) l_P, M = hbar c / l)")
for lab, Ne in CASES:
    l, M = grain(Ne)
    print(f"   {lab:24s} N_eff = {Ne:3d}: l = {l:.2e} m, M = {M:.2e} GeV")
M0 = grain(9)[1]

# ---------------------------------------------------------------- 2. Branch L3 crossover and axion (frozen 17:14:09)
print("\n2. BRANCH L3: crossover Lambda* = M y^(2/3) (Dirac dilution, p = 3/2, c = 1)  ->  axion f_a = Lambda*")
LST0 = (1.43e10, 7.70e10, 4.16e11)
for lab, Ne in CASES:
    M = grain(Ne)[1]
    out = []
    for L in (x * M / M0 for x in LST0):
        ma = 5.691e-6 * 1e12 / L
        out.append((L, ma * 1e6, ma * 1e6 * 0.2418, 0.12 * (28e-6 / ma) ** 1.165))
    (Ll, ml, fl, _), (Lb, mb, fb, om), (Lh, mh, fh, _) = out
    print(f"   {lab:24s} Lambda* = {Lb:.1e} GeV ({Ll:.0e}-{Lh:.0e});  m_a = {mb:5.0f} micro-eV ({mh:.0f}-{ml:.0f}),"
          f" {fb:4.0f} GHz ({fh:.0f}-{fl:.0f});  misalignment Omega h^2 = {om:.4f} (strings x{0.12 / om:.0f})")
print("   frozen: m_a = 74 micro-eV (14-400), 3.4-100 GHz.  Post-inflation DM windows quoted in the frozen code:")
print("   40-180 (Buschmann+22), 95-450 (Saikawa+24), >~500 micro-eV (Gorghetto+21)")
print("   Lorentz gamma_min = 23/log10(M/Lambda*) is unchanged (M/Lambda* = y^(-2/3) is fixed)")

# ---------------------------------------------------------------- 3. reheating, gravitons, remnants
print("\n3. REHEATING AND RELIC RADIATION")
T_eq_grav = (1.66 * math.sqrt(106.75)) ** (1 / 3) * MP          # Gamma ~ T^5/MP^2 = H ~ 1.66 sqrt(g*) T^2/MP
for lab, Ne in CASES:
    M = grain(Ne)[1]
    lo, hi = 0.3 * M, 1.9 * M
    print(f"   {lab:24s} T_RH ~ {lo:.1e} - {hi:.1e} GeV;  gravitons thermalise only above ~{T_eq_grav:.1e} GeV"
          f" -> {'marginal' if hi > 0.3 * T_eq_grav else 'NO'};  black-hole remnant mass ~ M = {M * 1.783e-24 * 1e6:.1f} micro-g")
print("   nu^c Delta N_eff = 0.14 needs only T_RH >> Lambda* (ratio unchanged) -> UNCHANGED; the '+0.05 thermal")
print("   graviton' increment (0.14 -> 0.19) becomes doubtful")

# ---------------------------------------------------------------- 4. Branch M ripples and Lorentz
print("\n4. BRANCH M (Lambda* fixed by neutrino masses = v^2/m3, independent of M)")
L0 = v ** 2 / (math.sqrt(2.51e-3) * 1e-9)
for lab, Ne in CASES:
    l, M = grain(Ne)
    eta = Ne / (24 * math.pi)
    c_need = 2.1e-9 / ((9 / 4) * (1 / (16 * eta ** 2)) * (L0 / M) ** 2)
    print(f"   {lab:24s} ripples A_s = (9/4) c (Lambda*/M)^2/(16 eta^2) needs area-law coefficient c = {c_need:.3f};"
          f"  Lorentz gamma >= {23 / math.log10(M / L0):.2f}")
print("   proton decay (tau depends on Lambda* only), Majorana anarchy, m_bb, leptogenesis: UNCHANGED")

# ---------------------------------------------------------------- 5. proton-decay freeze (12:50:31)
print("\n5. PROTON-DECAY FREEZE ROWS (tau = 8.7e35 yr (Lambda*/1e16)^4, C = 1; Super-K limit 2.4e34 yr)")
for lab, Ne in CASES:
    M = grain(Ne)[1]
    rows = (("gamma = 3", M * 10 ** (-23 / 3)), ("gamma = 5", M * 10 ** (-23 / 5)), ("neutrino link", 6.06e14),
            ("SM at grain scale", M))
    txt = ", ".join(f"{n}: {8.689e35 * (L / 1e16) ** 4:.0e} yr" for n, L in rows)
    print(f"   {lab:24s} {txt}")
print("   verdicts unchanged: Mechanism-A rows excluded either way; grain-scale row unobservable either way")

# ---------------------------------------------------------------- 6. finite volume and everpresent Lambda
print("\n6. FINITE VOLUME / DARK-ENERGY MAGNITUDE  (rho_L ~ beta / (l^2 sqrt V4); L_max = A(N) beta^(2/3) D_LSS)")
for lab, Ne in CASES:
    A = 2.15 * (9 / Ne) ** (2 / 3)                               # A = 2.15 (N=9), 3.18 (N=5): A ~ N^(-2/3)
    med = A * (0.6745 / 2) ** (2 / 3)
    b_need = (1 / A) ** 1.5
    P = math.erfc(math.sqrt(2) * b_need)                         # beta = |x|/2, x ~ N(0,1)
    lam_ratio = 0.6745 / 2 * (grain(9)[0] / grain(Ne)[0]) ** 2 / (0.6745 / 2)
    print(f"   {lab:24s} median L_max = {med:.3f} D_LSS;  P(L_max >= 1 D_LSS) = {P:.2e};  rho_L for a fixed"
          f" 4-volume x{lam_ratio:.3f} of the frozen value")
print("   frozen: 'finite volume ~(1-1.5 D_LSS)^3'.  With N_eff ~ 500 the same formula forces a universe ~0.07 D_LSS")
print("   across, which existing CMB topology searches exclude; equivalently the everpresent-Lambda magnitude falls")
print("   ~55x short for an observed-size universe.")

# ---------------------------------------------------------------- 7. length noise (12:36:16)
print("\n7. LENGTH NOISE")
for chi in (0.24, 1 / 3):
    r = (grain(495)[0] / grain(9)[0]) ** (1 - chi)
    print(f"   Channel A (KPZ paths, dL ~ l (L/l)^chi, chi = {chi:.2f}): amplitude x{r:.1f} - still far below any test")
print("   Channel B (Verlinde-Zurek, <dL^2> = c_B l_P L): uses the Planck length, not l -> UNCHANGED (GQuEST row)")

print("\n8. INDEPENDENT OF l / M / N_eff (no change): no phantom crossing and the recruitment w(z) locus; f sigma8;")
print("   S8; Branch L3 no proton decay / no 0nubb / normal ordering; sum m_nu = 72 meV, m_beta = 12.5 meV;")
print("   Delta N_eff = 0.14 (nu^c); hybrid asymmetric dark matter 2.5-10 GeV")
