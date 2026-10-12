#!/usr/bin/env python3
"""
ccef_ripples.py  --  can the grain framework produce the primordial ripples (no inflation)?  Order-of-magnitude tests.

Targets: A_s = 2.1e-9 (zeta), n_s = 0.9649 +- 0.0042, running ~0, Gaussian (f_NL ~ 0 +- 5), statistically isotropic,
super-horizon (phase-coherent acoustic peaks), r < 0.036.
CCEF ingredients: grain length ell = 1/M, M = 1.77e19 GeV; G = ell^2/(4 eta), eta = N_eff/(24 pi), N_eff = 9;
pre-geometric (non-local) tangle -> correlations on all scales before space exists; crystallisation reheats to
T_RH ~ 0.3 - 1.9 M (CCEF_reheat.md); one-seed growth front; matter switch-on Lambda*.
"""

import math

M = 1.767e19
eta = 9 / (24 * math.pi)
AS = 2.1e-9
DPHI = (4 / 9) * AS                     # radiation era: zeta = (3/2) Phi

print(f"targets: A_s = {AS:.1e} (-> Delta^2_Phi = {DPHI:.1e}), n_s = 0.965, r < 0.036\n")

# ------------------------------------------------------------------ M1 Poisson grain-count noise
print("M1. Poisson (random) fluctuations in the number of grains (causal-set / everpresent-Lambda style)")
for Rl in (1e10, 1e30, 1e60):
    d = Rl ** -1.5
    print(f"   region of {Rl:.0e} grain lengths: delta N / N ~ {d:.0e}")
print("   -> spectrum Delta^2 ~ k^3 (white noise, n_s = 4): wrong shape, and negligible on cosmic scales  [FAILS]\n")

# ------------------------------------------------------------------ M2 area-law (holographic) thermal fluctuations
print("M2. Area-law ('holographic') thermal fluctuations frozen when non-locality ends")
print("   if the heat capacity of a region scales with its AREA (the same entanglement area law that gives gravity),")
print("   dM^2 = T^2 c (R/ell)^2 and Phi = G dM / R  ->  Phi^2 = c (T/M)^2 / (16 eta^2): INDEPENDENT of R (scale-invariant)")
print(f"   amplitude: Delta^2_Phi = {1 / (16 * eta ** 2):.2f} c (T_f/M)^2;  needed {DPHI:.1e}")
Tf = math.sqrt(DPHI * 16 * eta ** 2) * M
print(f"   -> freeze-out temperature T_f = {Tf:.1e} GeV / sqrt(c)   (c = O(1) area-law coefficient)")
for lab, T in (("crystallisation, T_RH ~ 0.5 M", 0.5 * M), ("Branch L3 switch-on, Lambda* = 7.7e10", 7.7e10),
               ("Branch M switch-on, Lambda* >= 4e15", 4e15)):
    A = (1 / (16 * eta ** 2)) * (T / M) ** 2 * 9 / 4
    print(f"   if frozen at {lab:40s}: A_s ~ {A:.0e} x c   ({'too big' if A > 10 * AS else 'too small' if A < AS / 10 else 'about right'})")
for c in (1, 0.1, 0.01):
    print(f"   c = {c:5.2f}: needed T_f = {Tf / math.sqrt(c):.1e} GeV")
print("   tilt: exactly scale-invariant at leading order. A red tilt needs larger scales to freeze slightly hotter, e.g.")
for q in (2.0, 2.5):
    L = math.log(1 / (0.05 * 1.97e-14 / 1.0) * 1.6e-35 ** -1 * 1e-60) if False else 140.0
    ns1 = -2 * q / L
    print(f"     T_f proportional to [ln(R/ell)]^{q}:  n_s - 1 = -2q/ln(R/ell) = {ns1:+.3f},  running = {-(ns1 ** 2) / (2 * q):+.1e}"
          "   (form assumed, not derived)")
print("   status: right SHAPE naturally; amplitude fixes the freeze-out scale; tilt not derived  [PARTIAL]\n")

# ------------------------------------------------------------------ M3 growth-front roughness
print("M3. Roughness of the crystallisation front (arrival-time delays, zeta = H dt)")
print("   2-D front in 3-D space: Edwards-Wilkinson growth -> log-rough -> scale-invariant (!);")
print("   KPZ growth (the generic case) -> roughness exponent ~0.39 -> n_s - 1 ~ -0.78 (far too red); KPZ is also non-Gaussian")
for v_over_nu in (1.0,):
    lam_cmb = 1e60
    print(f"   anisotropy: a mode of transverse size L stays correlated over a distance ~ v L^2/nu along the growth direction;")
    print(f"   for cosmic L ~ {lam_cmb:.0e} ell that is ~{lam_cmb:.0e} times longer than wide -> extreme statistical anisotropy")
print("   amplitude: H ~ M at crystallisation, so zeta = H dt ~ 1 unless the front is smoother than ~5e-5 Planck times per scale")
print("   status: shape possible (EW), but anisotropy and non-Gaussianity rule out a single propagating front  [FAILS]\n")

# ------------------------------------------------------------------ requirements met by M2
print("SUPER-HORIZON COHERENCE: correlations must exist before the hot phase on scales far beyond c*t.")
print("   CCEF: the pre-geometric tangle is non-local (everything a few links from everything) -> satisfied by M1-M3 setups.")
print("TENSORS: thermal area-law mechanisms (string-gas precedent) predict a slightly BLUE tensor tilt (n_t ~ -(n_s-1) > 0),")
print("   unlike inflation's red tilt; a distinctive test if r is ever measured.")
