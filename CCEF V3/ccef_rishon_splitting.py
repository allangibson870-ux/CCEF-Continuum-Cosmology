#!/usr/bin/env python3
"""
ccef_rishon_splitting.py  --  can sub-structural relation bundling ('rishon splitting') rescue the finite-volume /
dark-energy prediction that failed in the audit (CCEF_prediction_audit.md)?

Idea: a relation is a bundle of n sub-grains (rishons; n ~ 25-37 from the force strengths, CCEF_nonabelian.md).
Gravity's G is set by the FIELDS on the junction lattice (spacing l = 5.1 l_P, N_eff ~ 495), but the everpresent-
Lambda 4-volume count (rho_L ~ 1/Delta V4, Delta V4 = Poisson noise of the element count) should count the finest
independent elements: sub-grains, or their elementary update events.
  1. STATISTICS: when does finer counting actually shrink Delta V4?  (Monte Carlo)
       (a) bundles appear Poisson-randomly, each with exactly n sub-grains (rigid bundles)
       (b) bundles Poisson, sub-grain occupancy also Poisson (compound)
       (c) bundle lattice is a CRYSTAL (fixed count, as the seed growth produces), sub-grain events Poisson
  2. HOW MANY independent elements per l^4 are needed:  L_max(median) = 0.072 n4^(1/3) D_LSS
  3. WHERE they could come from: n4 = (sub-grains per l^3) x (events per sub-grain per light-crossing time l/c)
       = 1.3 n x R,  with R = J_zz / J_ring = (J_zz/J_pm)^3 / 12 in quantum spin ice (light = slow ring exchange)
  4. SIDE EFFECT on the axion: the gauge-singlet nu^c string can spread over sub-grains too -> Lambda* up by
     (1.3 n)^(1/3)
"""

import math

import numpy as np

rng = np.random.default_rng(42)

# ---------------------------------------------------------------- 1. statistics
print("1. DOES COUNTING SUB-GRAINS SHRINK THE 4-VOLUME NOISE?  (relative noise of the volume estimate, 20,000 trials)")
Nb, n = 4000, 30
trials = 20000
cases = {}
nb = rng.poisson(Nb, trials)
cases["(a) random bundles, rigid (n each)"] = nb * n
cases["(b) random bundles, random occupancy"] = np.array([rng.poisson(n * k) for k in nb])
cases["(c) crystal of bundles, random sub-events"] = rng.poisson(n * Nb, trials)
for k, Ns in cases.items():
    print(f"   {k:44s} sigma(V4)/V4 = {Ns.std() / Ns.mean():.2e}")
print(f"   reference: 1/sqrt(bundles) = {1 / math.sqrt(Nb):.2e};  1/sqrt(sub-grains) = {1 / math.sqrt(n * Nb):.2e}")
print("   -> finer counting helps ONLY if the bundle (junction) count does not itself fluctuate: a crystal, which is")
print("      what one-seed growth produces (hyperuniform: count noise only from the boundary).  Then Lambda gains sqrt(n4).\n")

# ---------------------------------------------------------------- 2. requirement
NEFF = 495
pref = 1.04 * (9 / NEFF) ** (2 / 3)          # L_max(median) = pref * n4^(1/3)
print("2. REQUIREMENT  (frozen formula with counting length l_c^2 = l^2 / sqrt(n4), n4 = independent elements per l^4)")
print(f"   median L_max = {pref:.4f} x n4^(1/3) D_LSS")
for target in (1.0, 1.04, 1.5):
    print(f"   L_max = {target:4.2f} D_LSS needs n4 = {(target / pref) ** 3:6.0f}")
print(f"   (exact restoration of the frozen numbers: n4 = (N_eff/9)^2 = {(NEFF / 9) ** 2:.0f})\n")

# ---------------------------------------------------------------- 3. sources
print("3. SOURCES OF ELEMENTS:  n4 = 1.3 n (sub-grains per l^3; 0.65 junctions x 2 relations x n)  x  R (events per crossing)")
for nn in (25, 31, 37):
    s = 1.3 * nn
    print(f"   n = {nn}: spatial bundling alone (R = 1): n4 = {s:4.0f} -> median L_max = {pref * s ** (1 / 3):.2f} D_LSS"
          f"  (still excluded)")
print("   with microscopic events: quantum spin ice light is the slow 3rd-order ring exchange, so each grain is updated")
print("   R = J_zz/J_ring = (J_zz/J_pm)^3/12 times per light-crossing time.  Then  L_max ~ 0.072 (1.3 n/12)^(1/3) (J_zz/J_pm) D_LSS")
print(f"   {'J_pm/J_zz':>10s} {'R':>7s}   median L_max (D_LSS) for n = 25 / 31 / 37")
for jr in (0.03, 0.05, 0.08, 0.10, 0.15, 0.20):
    R = (1 / jr) ** 3 / 12
    Ls = [pref * (1.3 * nn * R) ** (1 / 3) for nn in (25, 31, 37)]
    print(f"   {jr:10.2f} {R:7.0f}   " + " / ".join(f"{x:5.2f}" for x in Ls))
print("   quantum spin ice's Coulomb (photon) phase needs small J_pm/J_zz (reported edge ~0.05-0.2; quoted from memory)")
print("   -> for J_pm/J_zz <~ 0.1 (deep in the photon phase) the universe comes out ~1-3.5 D_LSS: the frozen finite-volume")
print("      range is RESTORED; for 0.15-0.2 it stays too small.  The cosmic size becomes tied to the light sector's")
print("      coupling ratio: L ~ 0.1 (J_zz/J_pm) D_LSS\n")

# ---------------------------------------------------------------- 4. axion side effect
print("4. SIDE EFFECT: AXION.  Dirac dilution y = (cells' worth of grains)^(-1/2); if the gauge-singlet nu^c spreads over")
print("   sub-grains, grains per crossover cell = 1.3 n (M/Lambda*)^3  ->  Lambda* = M y^(2/3) (1.3 n)^(1/3)")
M, y = 2.38e18, 2.9e-13
for nn in (1 / 1.3, 25, 31, 37):
    L = M * y ** (2 / 3) * (1.3 * nn) ** (1 / 3)
    ma = 5.691e-6 * 1e12 / L * 1e6
    lab = "no sub-grains (audit)" if nn < 1 else f"n = {nn}"
    print(f"   {lab:22s} Lambda* = {L:.2e} GeV -> m_a = {ma:4.0f} micro-eV ({ma * 0.2418:.0f} GHz)"
          f"{'   inside frozen 14-400 band' if 14 <= ma <= 400 else ''}")
print("\n5. UNCHANGED: N_eff (fields still live on the junction lattice) and M = 2.4e18 GeV; Branch L3 Lorentz bound.")
