#!/usr/bin/env python3
"""
ccef_hybrid.py  --  CCEF hybrid = Branch M early universe + a dark string-net sector for dark matter.

Branch M (CCEF_branchM.md): Lambda* ~ 1e15 GeV; proton decay (Hyper-K window); Majorana nu, leptogenesis; ripples.
Dark sector = extra string LABELS on the same grains (P7 kept): a vector-like dark fermion chi charged under a dark
U(1)_D (or dark SU(N)), SM-neutral.  Stability of the lightest dark-charged string end: dark Gauss law (exact).
Constraint from the Planck-hot start (T_RH ~ 1e19 GeV): every sector is thermalised at ~M; a stable relic must be able to
annihilate (gravitational-only relics overclose).  Two versions:
  H1 secluded thermal relic: chi chi-bar -> dark photons (massive, decaying to SM via tiny kinetic mixing)
  H2 asymmetric DM: a portal junction at Lambda* shares the B-L asymmetry from leptogenesis with chi.
"""

import math

GEVM2_TO_CM3S = 1.17e-17                  # (GeV^-2) -> cm^3/s
SIGV_TH = 2.2e-26                         # cm^3/s for Omega h^2 = 0.12 (standard thermal relic)
OMEGA_RATIO = 0.120 / 0.0224              # Omega_DM / Omega_b = 5.36
M_P = 1.2209e19
LSTAR = 1e15

print("DARK SECTOR TEMPERATURE: SM and dark sector share T at ~M, decouple when portal junctions (dim-6 at Lambda*) freeze")
T_dec = (LSTAR ** 4 * 1.66 * math.sqrt(112) / M_P) ** (1 / 3)
print(f"   portal freeze-out T ~ (Lambda*^4 H-factor / M_P)^(1/3) ~ {T_dec:.0e} GeV (all SM species still relativistic)")
xi0 = (3.91 / 106.75) ** (1 / 3)
print(f"   later SM entropy dumps cool the dark sector relative to photons: T_D/T_gamma ~ {xi0:.2f} (x self-heating factors)\n")

print("H1. SECLUDED THERMAL RELIC (chi chi-bar -> A'A', sigma v = pi alpha_D^2 / m^2)")
for xi in (1.0, 0.45):
    sig_needed = SIGV_TH * xi                    # hidden-sector freeze-out at lower temperature needs ~xi less annihilation
    for aD in (0.003, 0.01, 0.03, 0.1):
        m = math.sqrt(math.pi * aD ** 2 / (sig_needed / GEVM2_TO_CM3S))
        print(f"   xi = {xi:.2f}, alpha_D = {aD:5.3f}: m_chi ~ {m / 1e3:6.2f} TeV")
print("   ('WIMPless miracle': m/alpha_D fixed; any alpha_D works, mass not predicted)")
for mA in (0.01, 0.1, 1.0):            # GeV
    eps_min = math.sqrt(1 / (1.0 * (1 / 137) * mA * 1.52e24 / 3))    # tau = 3/(alpha eps^2 m) < 1 s (BBN)
    print(f"   massive dark photon m_A' = {mA * 1e3:5.0f} MeV must decay before BBN (<1 s): kinetic mixing eps >~ {eps_min:.0e}")
print("   massless dark photon instead -> dark radiation:")
dN_dp = (8 / 7) * (11 / 4) ** (4 / 3) * xi0 ** 4 * (5.5 / 2) ** (4 / 3)
print(f"      Delta N_eff(dark photon, heated by chi annihilation) ~ {dN_dp:.2f}  (+ gravitons 0.05 -> ~{dN_dp + 0.05:.2f}: disfavoured by CMB)")
print("   -> H1 prefers a MASSIVE dark photon (secluded / Pospelov-Ritz-Voloshin type)\n")

print("H2. ASYMMETRIC DARK MATTER (portal junction shares B-L from leptogenesis with chi, then freezes)")
for r in (0.5, 1.0, 2.0):             # n_chi / n_B after sharing (set by chemical-equilibrium coefficients)
    m = OMEGA_RATIO * 0.938 / r
    print(f"   n_chi/n_B = {r:3.1f}:  m_chi = (Omega_DM/Omega_b) m_p / ratio = {m:4.1f} GeV")
sig_min = SIGV_TH * 3 / GEVM2_TO_CM3S
for m in (2.5, 5.0):
    aD = math.sqrt(sig_min * m ** 2 / math.pi)
    print(f"   symmetric part must annihilate away: m = {m} GeV needs alpha_D >~ {aD:.0e} (easy)")
print("   -> explains why dark matter and ordinary matter have similar densities (both from the same leptogenesis);")
print("      the dark mass ~2-10 GeV itself is not predicted (could be a dark-confinement scale)\n")

print("BOTH: relic radiation Delta N_eff ~ 0.05 (gravitons; massive dark photon); Branch M package otherwise unchanged.")
print("STRONG CP: no axion at Lambda* (it would overproduce); an axion with f_a ~ 1e9-1e11 (sub-dominant DM) or another")
print("   solution is still needed - open.")
