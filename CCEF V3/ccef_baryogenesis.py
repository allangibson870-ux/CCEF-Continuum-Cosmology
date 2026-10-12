#!/usr/bin/env python3
"""
ccef_baryogenesis.py  --  can the grain framework (Branch L3, and Branch M for comparison) make the observed
matter-antimatter asymmetry?  Order-of-magnitude estimates against Sakharov's conditions.

Inputs (CCEF): Lambda* = 7.7e10 GeV (1.4e10 - 4.2e11); T_max <~ 0.95 Lambda* (monopoles); Dirac Yukawa
y = 2.9e-13 from grain dilution of nu^c (which dilutes EVERY vertex containing nu^c); Z3 lepton triality: forbids
Delta L = 1, 2; allows Delta L = 3, sphalerons (Delta B = Delta L = 3), and Delta B = 2, Delta L = 0 (uddudd).
Target: eta_B = 6.1e-10  ->  Y_B = n_B / s = 8.7e-11.
"""

import math

MPL, LSTAR, GSTAR = 1.2209e19, 7.7e10, 106.75
YB = 8.7e-11
T_SPH = 131.7                      # sphaleron freeze-out (GeV)
C_SPH = 28 / 79                    # B = (28/79)(B-L) in the SM with sphalerons
y_nu = 2.9e-13
H = lambda T, g=GSTAR: 1.66 * math.sqrt(g) * T * T / MPL

print(f"TARGET: eta_B = 6.1e-10, Y_B = {YB:.1e}\n")

# ---------------------------------------------------------------- A. Majorana leptogenesis
print("A. Standard (Majorana) thermal leptogenesis")
print("   Branch L3: needs Delta L = 2 (Majorana nu^c) -> FORBIDDEN by Z3 lepton triality.")
print("   Branch M : allowed; Davidson-Ibarra needs M_N >~ 1e9 GeV <= T_max -> WORKS in the standard way (not CCEF-specific)\n")

# ---------------------------------------------------------------- B. Dirac leptogenesis
print("B. Dirac leptogenesis (Dick-Lindner-Ratz-Wright; Murayama-Pierce)")
G_eq = y_nu ** 2 / (16 * math.pi) * T_SPH
print(f"   hiding condition: nu_R must not equilibrate before sphalerons stop: y <~ 1e-8 (lit.);  CCEF y = {y_nu:.1e}  -> SATISFIED"
      f" (y^2 T/16pi / H at T_sph = {G_eq / H(T_SPH):.0e})")
Yeq_phi = 0.278 * 4 / GSTAR                      # complex doublet parent, relativistic equilibrium abundance
for g_other in (1.0, 0.1):
    BR = y_nu ** 2 / g_other ** 2               # the parent's nu^c vertex is diluted like every nu^c vertex
    print(f"   parent's other couplings ~{g_other}: branching into L nu^c <= {BR:.0e}; CP asymmetry eps <= BR -> "
          f"Y_B <= {C_SPH * Yeq_phi * BR:.0e}  (needed {YB:.0e}) -> FAILS by 1e{math.log10(YB / (C_SPH * Yeq_phi * BR)):.0f}")
print("   (the dilution that makes Dirac neutrinos light also starves every nu^c channel)")
tau = 1 / (y_nu ** 2 * LSTAR / (8 * math.pi)) * 6.582e-25
Gam = 6.582e-25 / tau
Td = math.sqrt(Gam * MPL / (1.66 * math.sqrt(86.25)))
print(f"   heavy grain modes of nu^c as parent: lifetime {tau:.0e} s -> decay at T ~ {Td:.0f} GeV < T_sph = {T_SPH} GeV"
      f" -> too late for sphalerons -> FAILS\n")

# ---------------------------------------------------------------- C. electroweak baryogenesis
print("C. Electroweak baryogenesis: needs a first-order EW transition (m_H <~ 70 GeV in the SM); m_H = 125 GeV gives a")
print("   smooth crossover and SM CP violation is ~1e-20 too small; CCEF adds nothing at the EW scale -> FAILS\n")

# ---------------------------------------------------------------- D. Delta B = 2 (allowed by Z3)
print("D. Delta B = 2 baryon violation (6-quark uddudd junction at Lambda*), allowed in Branch L3")
print("   thermal washout: rate ~ c T^11 / Lambda*^10 (c = unknown phase-space/coupling factor); in equilibrium above T_f:")
for c in (1, 1e-2, 1e-4, 1e-6, 1e-8):
    r = (1.66 * math.sqrt(GSTAR) * LSTAR / (c * MPL)) ** (1 / 11)
    print(f"      c = {c:7.0e}: T_f = {r:.2f} Lambda*" + ("   (never in equilibrium below Lambda*: no washout)" if r >= 1 else ""))
print("   -> an asymmetry made at T_after survives if T_after < T_f; sphalerons then share it between B and L (B-L conserved by them)")
L_QCD6 = 0.25 ** 6
tau_nn = 6.582e-25 / (L_QCD6 / LSTAR ** 5) / 3.156e7
print(f"   neutron-antineutron oscillation: tau ~ hbar Lambda*^5 / Lambda_QCD^6 ~ {tau_nn:.0e} yr (limit ~ 3 yr): untestable\n")

# ---------------------------------------------------------------- E. the growth front
print("E. Front-driven baryogenesis at geometrogenesis (Sakharov 3 = the advancing crystal front)")
for frac in (0.2, 0.5, 0.95):
    T = frac * LSTAR
    n_cells_over_s = 1 / (0.4386 * GSTAR * frac ** 3)          # one Lambda*-cell per (1/Lambda*)^3 volume
    need = YB / n_cells_over_s
    print(f"   T just behind the front = {frac:.2f} Lambda*: needs (Delta B = 2 events per cell) x (CP bias) ~ {need:.0e}")
print("   -> a tiny CP bias per event suffices, IF grain-level CP violation exists (unknown) and T behind the front < T_f.")
print("   One seed -> one sign of asymmetry everywhere: no matter/antimatter domains (required: none seen out to ~Gpc,")
print("   and the CCEF universe is only ~1 CMB diameter across).")

print("\nSUMMARY (Branch L3):  Majorana leptogenesis forbidden | Dirac leptogenesis starved by dilution (fails by ~1e16) |")
print("  EW baryogenesis fails | Delta B = 2 front mechanism ALLOWED but needs an unknown grain-level CP source.")
print("Branch M: standard Majorana leptogenesis available.")
