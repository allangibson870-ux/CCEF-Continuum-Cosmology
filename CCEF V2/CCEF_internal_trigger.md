================================================================================
CCEF v2 — DERIVATION NOTE: THE INTERNAL TRIGGER (L_ord CROSSING L*), NO TUNING
Follow-on to priority #4. Derived entirely from existing quantities; NO new scale,
NO tuning, NO hand-fitting; NO GR imported; NO assumption that acceleration is required.
Compiled 2026-06-29. Builds on CCEF_U_chi_acceleration.md, CCEF_two_stage_acceleration.md.
Labels: [SOLID] derived/verified | [STRUCT] forced by structure | [THM] ceiling theorem
================================================================================

--------------------------------------------------------------------------------
0. FRAMING (the right question)
--------------------------------------------------------------------------------
We do NOT ask "how do we make CCEF produce dark energy." We ask: as the ordered domain grows,
does L_ord cross any INTERNAL threshold -- built only from quantities the theory already has --
at which a previously sub-dominant operator takes over and changes the expansion? Then we report
whatever the continuum does, with no target. This avoids the tuned second scale of the two-stage
note and respects the principle that the continuum should answer the expansion from what it IS.

HEADLINE:
  YES -- there is exactly one such trigger, and it is fully derived: L_ord crossing
     L* = sigma / DeltaF ,
  the ratio of the (derived) domain-wall tension sigma to the (derived, radiative) bulk free-
  energy bias DeltaF. Below L* the surface term dominates (curvature-driven, a ~ t^1/2, q=+1);
  above L* the bulk term dominates (bias-driven, a ~ t, q=0). The crossover is UNIVERSAL: its
  shape depends only on L/L* (verified -- p = 0.50 -> 0.61 at L* -> 0.96), independent of the
  value of DeltaF. No new scale, no tuning. [SOLID]

  And a CEILING THEOREM closes the question of acceleration once and for all: no LOCAL operator
  contributes a free energy growing faster than the VOLUME (L^3), so the front driving force can
  at most approach a constant (DeltaF); hence the expansion exponent p <= 1 and q >= 0 ALWAYS.
  The continuum decelerates, then coasts. It NEVER accelerates from its own local dynamics. Dark
  energy is therefore not a feature the theory can manufacture by an internal trigger -- and, per
  the framing, not one it needs to. [THM]

================================================================================
1. THE OPERATOR-SCALING ARGUMENT (where the trigger comes from)
================================================================================
A single ordered domain of size L has a free energy assembled from the action's operators, each
scaling with L by its geometric content:
   BULK (volume) free-energy bias:     F_bulk   ~ -DeltaF * L^3     (the ordered phase is lower)
   SURFACE (wall) tension:             F_surf   ~ +sigma  * L^2
   BENDING (bilaplacian A3, curvature^2): F_bend ~ +kappa * K^2 * Area ~ kappa * L^0  (const)
   ...higher-derivative operators scale with even MORE inverse powers of L (smaller at large L).
The driving force on the coarsening front is -dF/dL per unit area; the Model-A front law (with the
derived friction gamma_0) is
   gamma_0 dL/dt = sigma/L  +  DeltaF  +  O(1/L^3) .
Term by term:
   * sigma/L (surface/curvature): DECREASES as the domain grows -> decelerating, gives a ~ t^1/2.
   * DeltaF (bulk bias): CONSTANT -> gives constant front speed -> a ~ t (coasting).
   * bending and higher: fall as 1/L^3 or faster -> always sub-dominant at large L; never trigger.
The ONLY change of regime is surface -> bulk, when sigma/L drops below DeltaF, i.e. at
   L*  =  sigma / DeltaF .                                                          [SOLID]
This is the internal trigger: the bulk bias DeltaF -- "sub-dominant" while L < L* (curvature wins)
-- becomes the dominant driving once L_ord > L*. Both sigma and DeltaF are existing, derived
quantities (sigma from the kink profile, DeltaF from the radiative Coleman-Weinberg potential,
CCEF_U_chi note). No external scale is introduced; L* is fixed by the theory's own numbers.

================================================================================
2. WHAT THE TRIGGER DOES (verified)
================================================================================
Solving gamma_0 dL/dt = sigma/L + DeltaF exactly,
   t(L) = (gamma_0/DeltaF)[ L - (sigma/DeltaF) ln(1 + DeltaF L/sigma) ] ,
the local expansion exponent p(L) = d ln L/d ln t behaves as (numerically confirmed, and
independent of the value of DeltaF -- the curve depends only on L/L*):
   L = 1e-2 L* :  p = 0.502    (curvature-driven  -> a ~ t^1/2, q = +1, decelerating)
   L =     L*  :  p = 0.613    (crossover; analytic 0.61)
   L = 1e+2 L* :  p = 0.963    (bulk-driven       -> a ~ t,    q =  0, coasting)
So as the universe ages and L_ord sweeps through L*, the expansion smoothly and IRREVERSIBLY
crosses over from decelerating (q=+1) to coasting (q=0). One trigger, one crossover, derived. The
redshift kinematics (the three tests) are unchanged across it (the metric is the same; see the
redshift note). [SOLID]

================================================================================
3. THE CEILING THEOREM: WHY NO INTERNAL TRIGGER CAN ACCELERATE
================================================================================
Claim: for any set of LOCAL operators, the coarsening exponent satisfies p <= 1, hence q >= 0.
Proof sketch [THM]:
  - A local operator's contribution to a domain's free energy is an integral of a local density
    over the domain; the most extensive possible scaling is the VOLUME, F ~ L^3. (Anything with
    derivatives or confined to the wall scales as a LOWER power of L.)
  - The front driving force is -dF/dL per unit area; the volume term gives a CONSTANT (DeltaF),
    and every other term gives a driving that DECREASES with L (sigma/L, kappa/L^3, ...).
  - Therefore gamma_0 dL/dt is bounded above by a constant at large L => dL/dt -> const => L ~ t
    at most => a ~ L grows at most linearly => p <= 1 => q = (1-p)/p >= 0.   QED (sketch)
Consequence: NO internal trigger -- no operator becoming relevant as L_ord grows -- can drive
genuine acceleration (q<0), because acceleration needs p>1 (super-linear L_ord), which needs a
driving force that GROWS with L, which no local operator provides. The two-stage note's transient
q<0 required a second transition's free energy to be RELEASED (DeltaF rising in time); a static
operator landscape, however rich, cannot do this -- it can only redistribute among terms that are
all bounded by the constant volume term. The coasting ceiling (q=0) is firm. [THM]

================================================================================
4. THE CONTINUUM'S ANSWER (no dark energy, no tuning)
================================================================================
Putting it together, the expansion history the continuum GIVES -- from what it is, with nothing
fit -- is:
   early (L_ord < L*):  a ~ t^(1/2),  H = 1/(2t),  q = +1   (curvature-driven coarsening)
   late  (L_ord > L*):  a ~ t,        H = 1/t,     q =  0   (bulk-bias-driven coasting)
   crossover at L* = sigma/DeltaF, both derived; the transition is monotone, decelerating->coasting.
This is a parameter-free SHAPE (one internal crossover); only the LOCATION of L* in physical units
awaits the parameter-fixing of priority #5 (sigma and DeltaF are computed once A1,A4,quartic,gauge
are pinned -- they are not chosen). There is NO acceleration, NO cosmological constant, NO dark-
energy component, and NOTHING tuned. If observations require genuine acceleration (q<0) that the
coasting ceiling cannot supply, that is a clean FALSIFICATION of minimal CCEF -- exactly the kind
of honest, do-or-die confrontation the discipline calls for, not an invitation to add tuned
structure.

REINTERPRETING "dark energy": in CCEF there is no substance called dark energy; the late-time
near-coasting is simply the bulk ordering bias driving the front at constant speed. What a GR
analyst would fit as "Lambda" is, here, the constant DeltaF of the ordering -- and it produces
COASTING (a~t), not de Sitter acceleration (a~e^{Ht}). The continuum answers the expansion; it
does not need, and does not contain, a dark-energy fluid. [STRUCT]

================================================================================
5. HONEST STATUS
================================================================================
[SOLID / THM]
  - Internal trigger L* = sigma/DeltaF derived from existing quantities; no new scale, no tuning.
  - It produces ONE monotone crossover: decelerating t^1/2 (q=+1) -> coasting t (q=0), verified
    (p: 0.50 -> 0.61 at L* -> 0.96), universal in L/L*.
  - Ceiling theorem: local operators give p <= 1, q >= 0. No internal trigger can accelerate.
  - "Dark energy" reinterpreted: a GR Lambda maps to the ordering bias DeltaF, which COASTS, not
    inflates. CCEF needs no dark-energy component.
[PENDING -- not a fit, a computation]
  - The physical value of L* (hence the crossover redshift) follows from sigma and DeltaF once the
    minimal parameters are fixed from cosmology (priority #5). These are computed, not tuned.
[FALSIFIABLE]
  - The decelerate->coast history (q never < 0) is the firm prediction. If data robustly require
    q<0 today, minimal CCEF (local operators, single growing domain) is falsified -- to be met by
    re-examining the foundations, NOT by adding tuned components.

================================================================================
6. ONE-PARAGRAPH SUMMARY
================================================================================
Asking only what the growing continuum does on its own, there is exactly one internal trigger:
L_ord crossing L* = sigma/DeltaF, the ratio of the derived wall tension to the derived radiative
bulk bias. Because a domain's surface free energy scales as L^2 and its bulk bias as L^3, the
front driving gamma_0 dL/dt = sigma/L + DeltaF crosses over from curvature-dominated to bulk-
dominated at L*, taking the expansion from decelerating a ~ t^1/2 (q=+1) to coasting a ~ t (q=0) --
a single, monotone, parameter-free crossover whose shape depends only on L/L* (verified: the local
exponent runs 0.50 -> 0.61 at L* -> 0.96). A ceiling theorem then settles acceleration in general:
no local operator's free energy grows faster than the volume (L^3), so the front driving is bounded
by the constant DeltaF, the exponent obeys p <= 1, and q >= 0 always -- no internal trigger, however
constructed, can produce genuine acceleration (q<0), which would need a driving force that grows
with L. So the continuum's honest expansion history is decelerate-then-coast, with what a GR
analyst would call Lambda being nothing but the ordering bias DeltaF, which coasts rather than
inflates. There is no dark-energy component, nothing is tuned, and the prediction (q never < 0) is
cleanly falsifiable -- which is exactly how the theory should be allowed to speak.
================================================================================
