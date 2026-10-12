#!/usr/bin/env python3
"""
ccef_reheat.py  --  how hot does crystallisation (geometrogenesis) make the universe?

Latent heat: energy per junction released when tangle -> diamond crystal (from our own simulations, angle rule on).
Junction density: diamond with bond length = grain length ell = 1/M  ->  n_J = 8 / (4 ell / sqrt3)^3 = 0.65 / ell^3.
Energy scale of the geometry coupling K = kappa * M.  Unit consistency (quantum spin ice): light speed c ~ J_ring * a,
so with a = ell the ring-exchange (and ring-reward K) scale is ~ hbar c / ell = M  ->  natural kappa ~ 1.
If the heat thermalises into radiation with g* degrees of freedom:  rho = n_J dE K = (pi^2/30) g* T^4.
Self-consistency: in the simulations diamond survives up to T ~ 2.7 K (it never melted); if T_RH / K exceeds that,
the released heat would re-melt space.
"""

import math
import random

from ccef_geo_dynamics import Graph2
from ccef_grain_hamiltonian_mc import random_bipartite

M = 1.767e19
LSTAR = 7.7e10
nJ = 8 / (4 / math.sqrt(3)) ** 3          # junctions per ell^3

g = Graph2(1728, random_bipartite(864, 4, random.Random(4)), 1, 8, 4)
E_tangle = g.E / g.N
E_glass, E_crys = -8.4, -12.0
print(f"latent heat per junction (units of K): random tangle {E_tangle:+.2f} -> crystal -12: dE = {E_tangle - E_crys:.1f};"
      f"  relaxed glass -8.4 -> -12: dE = {E_glass - E_crys:.1f}")
print(f"junction density n_J = {nJ:.2f} / ell^3\n")


def T_rh(dE, kappa, gstar):
    rho = nJ * dE * kappa                 # in units of M^4
    return (30 * rho / (math.pi ** 2 * gstar)) ** 0.25 * M


print(f"{'kappa = K/M':>12s} {'g*':>6s}   T_RH (GeV), dE = 3.6 .. {E_tangle - E_crys:.0f}     T_RH / Lambda*      T_RH / K  (melts space if >~ 2.7)")
for kappa in (1.0, 0.1, 4.4e-9, 1e-20, 1e-32):
    for gstar in (2, 106.75, 1000):
        lo, hi = T_rh(3.6, kappa, gstar), T_rh(E_tangle - E_crys, kappa, gstar)
        print(f"{kappa:12.1e} {gstar:6.0f}   {lo:9.1e} .. {hi:9.1e}       {lo / LSTAR:9.1e} .. {hi / LSTAR:9.1e}   "
              f"{lo / (kappa * M):9.1e} .. {hi / (kappa * M):9.1e}")
k_crit = math.pi ** 2 * 106.75 / 30 * (LSTAR / M) ** 4 / (nJ * (E_tangle - E_crys))
print(f"\nT_RH would stay below Lambda* only if kappa < {k_crit:.0e} (K < {k_crit * M:.0e} GeV per junction)")
for gstar in (106.75, 1000):
    # T_RH/K = (30 nJ dE/(pi^2 g*))^(1/4) kappa^(-3/4) <= 2.7
    kmin = ((30 * nJ * (E_tangle - E_crys) / (math.pi ** 2 * gstar)) ** 0.25 / 2.7) ** (4 / 3)
    print(f"no re-melting (T_RH <= 2.7 K) requires kappa >= {kmin:.2f}  (g* = {gstar:.0f})")
print("\nConsequences if kappa ~ 1 (natural): T_RH ~ 0.3 - 0.9 M ~ 1e18 - 1e19 GeV (~1e31 - 1e32 K)")
for name, g_x, gdec in (("right-handed neutrinos (3 Weyl)", 3 * 7 / 8 * 2, 106.75), ("gravitons (2 bosonic)", 2, 106.75)):
    if "neutrino" in name:
        dN = 3 * (10.75 / gdec) ** (4 / 3)
    else:
        dN = (4 / 7) * g_x * (10.75 / gdec) ** (4 / 3)
    print(f"   {name:32s} thermalised then decoupled above Lambda*: Delta N_eff = {dN:.3f}")
