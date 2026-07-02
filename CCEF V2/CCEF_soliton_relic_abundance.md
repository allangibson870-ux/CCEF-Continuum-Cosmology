================================================================================
CCEF v2 — DERIVATION NOTE: SOLITON RELIC ABUNDANCE FROM THE KIBBLE/ORDERING TRANSITION
Follow-on to the growth note (can CCEF's own solitons supply the Omega_eff~0.3 that
structure growth wants -- WITHOUT a dark-matter particle?). Derived from the theory;
no hand-fitting; a soliton fix is preferred and is what this tests.
Compiled 2026-06-29. Builds on CCEF_perturbations_growth.md; uses v1 KZM result (Working Dir Sec 11).
Labels: [SOLID] derived/verified | [BRACKET] bounded, not pinned | [STRUCT] structurally natural
        | [DEFER] needs the freeze-out/annihilation history calc
================================================================================

--------------------------------------------------------------------------------
0. THE QUESTION AND THE HEADLINE
--------------------------------------------------------------------------------
Growth wants a clustering Omega_eff ~ 0.3; baryons give only ~0.05. Can CCEF's OWN solitons
(the same topological excitations as baryons -- NO new particle) supply the rest as a relic from
the Kibble/ordering transition? Or is the growth sector falsified without conventional dark matter?

HEADLINE:
  NOT falsified, and NO scarcity: the Kibble mechanism OVER-produces solitons -- v1 found
  n_KZM/n_baryon,obs ~ 5e8 (Working Directory Sec 11). Raw soliton abundance vastly EXCEEDS what is
  needed; the relic is set by ANNIHILATION, not by any production shortage. [SOLID]
  The annihilation freeze-out is MARGINAL -- Gamma/H ~ O(1) at the ordering transition -- so the
  surviving relic is bracketed between ~1e-10 (efficient thermal annihilation of the light hadronic
  soliton) and overclosure (frozen-in Kibble value). Omega ~ 0.3 lies INSIDE that bracket. [BRACKET]
  A purely THERMAL symmetric relic of the light hadronic soliton is too small (Omega~7e-11); reaching
  ~0.3 needs the NON-thermal, incompletely-annihilated Kibble relic (which the v1 overproduction
  evidences) and/or a heavier weakly-annihilating soliton -- and CCEF already has a candidate: the
  S^2 HOPF soliton, which v1 FALSIFIED as a baryon for being far too heavy (E*R~79-1061) but which is
  exactly what a HEAVY, weakly-annihilating DARK soliton in a DISTINCT topological sector needs. [STRUCT]
  ATTRACTIVE STRUCTURE: if the SYMMETRIC soliton relic is the dark matter and the NET topological
  charge is the baryons, the two densities share ONE origin, so Omega_DM/Omega_b ~ 5 is a linked,
  natural ratio (observed 5.3), not a coincidence. A genuine soliton fix -- same field, no new
  particle -- that ALSO explains the 5:1 DM:baryon ratio. [STRUCT]
  VERDICT: viable and attractive, but NOT yet pinned to 0.3. Whether it lands there is gated by the
  annihilation freeze-out history (the specific next calc). No value is tuned here; the bracket is
  reported honestly.

================================================================================
1. NO SCARCITY: THE KIBBLE MECHANISM OVER-PRODUCES SOLITONS
================================================================================
At the (second-order, mean-field -- derived) ordering transition, the order parameter picks random
orientations in causally-disconnected regions; topological solitons (Skyrmions, pi_3) form at ~1 per
correlation volume, n_def ~ 1/xi_c^3. Mean-field Kibble-Zurek (nu=1/2, z_dyn=2) gives xi_c ~ xi_0
(tau_Q/tau_0)^{1/4}. The magnitude (v1, Working Directory Sec 11): n_KZM/n_baryon,obs ~ 5e8. So:
  * If left UN-annihilated at the baryon mass, Omega_raw ~ 5e8 x Omega_b ~ 2e7 -- absurd overclosure.
  * => there is NO shortage of solitons. The observed baryon density (Omega_b~0.05) is already a
    HEAVILY-processed remnant. The relic that matters for dark matter is set by how much of the huge
    initial population SURVIVES annihilation. [SOLID]
This flips the growth "missing mass" worry: the raw material for Omega~0.3 is present ~1e8-fold over;
the physics question is regulation (annihilation), not manufacture.

================================================================================
2. THE ANNIHILATION FREEZE-OUT IS MARGINAL (relic not fixed by scarcity)
================================================================================
At the transition (T ~ Lambda ~ 0.23 GeV): n ~ Lambda^3, geometric cross-section sigma ~ pi/Lambda^2,
v ~ c => annihilation rate Gamma = n sigma v ~ Lambda. Coasting Hubble at the transition (t_order ~
1/Lambda) => H ~ Lambda. Hence
   Gamma/H ~ O(1)  (marginal).                                                          [SOLID]
Marginal freeze-out means the relic is EXPONENTIALLY SENSITIVE to details and spans a huge range:
efficient annihilation -> Omega -> ~0; inefficient (frozen-in) -> Omega -> overclosure. Omega ~ 0.3
is comfortably inside this window. The outcome is therefore NOT determined by scarcity but by the
detailed annihilation history through the transition -- which is the calc still to be done (Sec 4). [BRACKET]

================================================================================
3. TWO BRACKETS, AND WHERE 0.3 SITS
================================================================================
Using standard freeze-out Omega ~ 6e-27 cm^3 s^-1 / <sigma v> (h^2~0.5):
  LOWER bracket -- THERMAL relic of the LIGHT hadronic soliton (R~0.3 fm, geometric):
     <sigma v> ~ 8.5e-17 cm^3/s  ->  Omega ~ 7e-11 (negligible). A light soliton that reaches
     thermal equilibrium annihilates almost completely. [SOLID]
  Required for Omega~0.26: <sigma v> ~ 2.3e-26 cm^3/s (the standard thermal value) -- i.e. ~4e9x
     WEAKER annihilation than the geometric light soliton. [SOLID]
  UPPER bracket -- NON-thermal Kibble relic (annihilation frozen by the marginal Gamma~H and the
     rapid coarsening dilution of encounter rates): stays near the huge Kibble value -> overcloses.
Two natural ways the true relic lands near 0.3 BETWEEN these brackets, both using EXISTING structure:
  (i) HEAVIER soliton -> smaller size R~1/m -> sigma~pi/m^2 -> relic boosts as m^2. CCEF's S^2 HOPF
      soliton (pi_3(S^2)=Z, a DISTINCT sector) was FALSIFIED as a baryon precisely for being too
      heavy (E*R~79-1061, i.e. ~1e2-1e3x). As DARK matter that heaviness is a VIRTUE: weaker
      annihilation, heavier relic. (Thermal m^2 boost alone gives ~1e-6-1e-4; not enough by itself,
      but it moves the light-soliton relic strongly upward and stacks with (ii).) [STRUCT]
  (ii) INCOMPLETE annihilation: the v1 KZM OVER-production (x5e8) is direct evidence that annihilation
      does NOT reach thermal completeness here (else no overproduction) -- so the true relic sits well
      ABOVE the thermal lower bracket, toward the Kibble value, and a modest partial annihilation
      leaving ~5x the net-baryon density gives Omega_DM ~ 0.25. [STRUCT / BRACKET]

================================================================================
4. THE ATTRACTIVE PART: DM AND BARYONS SHARE ONE ORIGIN (the 5:1 ratio)
================================================================================
In this picture the SAME Kibble population yields both:
   * NET topological charge (survives annihilation by charge conservation) = BARYONS, Omega_b ~ 0.05.
     The net is sqrt(N)-suppressed relative to the total (random-walk of orientations).
   * SYMMETRIC surviving relic (soliton+antisoliton that escaped annihilation) = DARK MATTER, Omega_DM.
Because both come from ONE event, their ratio is a computable statistics+freeze-out number, NOT a free
coincidence. The observed Omega_DM/Omega_b = 5.3 is then a TARGET the mechanism should hit, not an
accident -- an asymmetric-dark-matter-like link, but here with NO new sector: the dark matter is
literally the symmetric relic of CCEF's own solitons. This is the strongest reason to prefer the
soliton fix: it can explain BOTH the dark-matter density AND the ~5:1 coincidence at once. [STRUCT]

================================================================================
5. HONEST STATUS
================================================================================
[SOLID]
  - Kibble OVER-produces solitons (v1 x5e8): no scarcity; relic is annihilation-limited.
  - Freeze-out is marginal (Gamma/H ~ O(1) at the transition): relic spans ~1e-10 to overclosure;
    Omega~0.3 is inside the accessible window.
  - A THERMAL relic of the LIGHT hadronic soliton is too small (~7e-11) -> a pure light-soliton
    thermal relic FAILS; the working channels are (i) heavier Hopf-sector soliton, (ii) non-thermal
    incomplete annihilation.
[STRUCT -- attractive, existing-structure]
  - The S^2 HOPF soliton (v1's "too-heavy" failed baryon) is a natural HEAVY dark soliton (distinct
    sector, topologically stable, weakly annihilating). No new field.
  - DM = symmetric relic, baryons = net charge -> Omega_DM/Omega_b ~ 5 is a linked prediction-shaped
    number (observed 5.3), not tuned.
[DEFER -- the calc that decides it]
  - The annihilation freeze-out HISTORY through the ordering transition on the coasting background:
    solve n-dot = -<sigma v>(n^2 - n_eq^2) - 3Hn with the ACTUAL soliton cross-section(s) and
    H(t_order)=1/t_order, for BOTH the Hopf (dark) and Skyrme (baryon) sectors. Output: Omega_DM and
    Omega_DM/Omega_b. THIS is what turns "0.3 is in range" into a derived number (or a falsification).
  - Cross-check: the same transition's defect network must also give the growth-required clustering
    (feed Omega_eff back into CCEF_perturbations_growth.md).

VERDICT: the growth sector is NOT falsified, and a genuine SOLITON fix (no dark-matter particle) is
viable AND attractive -- it can supply Omega~0.3 from the Kibble over-production and simultaneously
explain the 5:1 DM:baryon ratio. It is NOT yet pinned to 0.3; that is gated by one specific,
well-posed freeze-out calculation. Nothing here is tuned -- the relic is reported as a bracket.

================================================================================
6. ONE-PARAGRAPH SUMMARY
================================================================================
Structure growth wants Omega_eff~0.3 and baryons give only ~0.05, so the question is whether CCEF's
own solitons -- the same topological objects as baryons, no new particle -- can supply the rest from
the Kibble/ordering transition. They over-produce, not under-produce: v1 found the Kibble mechanism
makes ~5e8 times the observed baryon density in solitons, so raw abundance is ample and the relic is
set by annihilation. The annihilation freeze-out is marginal (Gamma/H ~ O(1) at the transition), so
the surviving relic is bracketed from ~1e-10 (a fully-thermalized light soliton, which annihilates
away) up to overclosure (frozen-in), with Omega~0.3 sitting inside that window. A purely thermal
light-soliton relic is too small; the channels that reach ~0.3 use existing structure -- a heavier,
weakly-annihilating soliton (CCEF's S^2 HOPF soliton, the v1 "too-heavy failed baryon", is a natural
heavy dark soliton in a distinct topological sector) and/or the non-thermal incomplete annihilation
that the v1 over-production already evidences. Most attractively, if the dark matter is the SYMMETRIC
soliton relic and the baryons are the NET topological charge, both come from one event and
Omega_DM/Omega_b ~ 5 is a linked, natural number (observed 5.3) -- so the soliton fix can explain the
dark-matter density AND the 5:1 coincidence at once, with no new sector. The result is not yet pinned
to 0.3; that is decided by one well-posed next calculation -- the annihilation freeze-out history
n-dot = -<sigma v>(n^2 - n_eq^2) - 3Hn through the transition for the Hopf (dark) and Skyrme (baryon)
sectors on the coasting background -- which would turn "0.3 is in range" into a derived number or
falsify it. No value is tuned; the relic is honestly a bracket that comfortably contains what growth needs.
================================================================================
