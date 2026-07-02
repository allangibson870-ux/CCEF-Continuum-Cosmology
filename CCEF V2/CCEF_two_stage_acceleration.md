================================================================================
CCEF v2 — DERIVATION NOTE: TWO-STAGE FREE ENERGY U(chi1,chi2) AND ACCELERATION
Sub-task of priority #4 (the "multi-stage ordering" route). Derived from the theory;
no hand-fitting; no GR/Friedmann imported (acceleration = coarsening convexity).
Compiled 2026-06-29. Builds on CCEF_U_chi_acceleration.md.
Labels: [SOLID] derived/verified | [STRUCT] forced by structure | [NEG] honest negative
        | [TUNE] requires a tuned input (flagged, not hidden)
================================================================================

--------------------------------------------------------------------------------
0. THE QUESTION AND THE HEADLINE
--------------------------------------------------------------------------------
Single-field CCEF tops out at coasting (q=0): no genuine acceleration (CCEF_U_chi note). The
proposed fix is MULTI-STAGE ordering -- a second order parameter chi2 with its own, later
ordering transition. Question: does U(chi1,chi2) yield late-time acceleration (q<0), with the
second scale DERIVED rather than tuned?

HEADLINE:
  YES, the MECHANISM is real and derived: every ordering transition releases free energy, and in
  COARSENING kinematics (a ~ L_ord) a RISING free-energy bias makes L_ord convex, i.e. q<0. A
  second, late transition therefore produces a TRANSIENT acceleration epoch that then relaxes back
  to coasting -- qualitatively dark-energy-like, and (unlike GR's eternal de Sitter) FINITE, in
  keeping with CCEF not being GR. Numerically a late stage-2 reaches q_min ~ -0.78 (cf. observed
  q0 ~ -0.5) and returns to coasting. [SOLID mechanism]

  BUT the magnitude is NOT free: a transition late enough to act now is LOW-scale, and its energy
  release scales as DeltaF2 ~ M2^4, suppressed relative to the primordial floor by (M2/M1)^4. To
  make a LATE transition energetically significant requires an anomalously FLAT, deep second well
  (a tuned small quartic b2) -- i.e. CCEF reproduces the cosmological-constant MAGNITUDE /
  COINCIDENCE problem rather than dissolving it. The second scale/depth is a TUNED input here, not
  derived. So: multi-stage ordering DELIVERS the right qualitative structure (finite late
  acceleration) but does NOT yet derive dark energy without a fit. [NEG / TUNE]

================================================================================
1. THE TWO-STAGE FREE ENERGY
================================================================================
Add a second amplitude chi2 (a second ordering channel) with its own potential and a coupling:
   U(chi1,chi2) = [ -(m1^2/2)chi1^2 + (b1/4)chi1^4 ]      (stage 1: the primary ordering)
                + [ -(m2^2/2)chi2^2 + (b2/4)chi2^4 ]      (stage 2: the late ordering)
                + (lam/2) chi1^2 chi2^2 .                  (interaction; boundedness needs lam>-sqrt(b1 b2))
Relaxational (Model A) dynamics, with the friction gamma_0 derived earlier:
   gamma_0 d_t chi_i = -dU/dchi_i .
Per-stage scales (independent timing vs depth -- the crux):
   amplitude  chi_i,0 = sqrt(m_i^2/b_i) ;  well DEPTH  DeltaF_i = m_i^4/(4 b_i) ;
   ordering TIME (instability rate) ~ 1/m_i^2 .
Stage 1 (m1^2=1, b1=1): orders at t~O(1), DeltaF1=0.25. Stage 2 is meant to be LATE (small m2^2).

================================================================================
2. HOW A TRANSITION ACCELERATES THE COARSENING (no GR)
================================================================================
Expansion is coarsening: a proportional to L_ord. The front is driven by the free-energy DEPTH of
the ordered state, DeltaF(t) = U(0,0) - U(chi1(t),chi2(t)) = -U(chi1,chi2). Late-time front EOM:
   gamma_0 dL/dt = DeltaF(t) + sigma/L  ->  (curvature sigma/L sub-dominant)  dL/dt = DeltaF(t)/gamma_0 .
Since a ~ L:
   a' = DeltaF/gamma_0 ,  a'' = DeltaF'/gamma_0 ,  q = -a a''/a'^2 = - gamma_0 L DeltaF' / DeltaF^2 .
   ===>  q < 0  iff  DeltaF'(t) > 0   (the free-energy bias is RISING).                 [SOLID]
A static floor (DeltaF'=0) gives q=0 (coasting, the single-field result). A transition, DURING
which DeltaF rises as chi orders, gives q<0 -- a transient acceleration epoch -- then q->0 once the
transition saturates (DeltaF'->0). Note q ~ -L DeltaF'/DeltaF^2: because L is large at late times,
even a modest late DeltaF' gives an O(1) negative q. So a LATE transition, IF it releases
appreciable energy, drives appreciable acceleration. The "if" is Sec 4.

================================================================================
3. NUMERICAL DEMONSTRATION (mechanism + the obstruction)
================================================================================
Integrated the coupled relaxational dynamics + front law. Parameter VALUES are illustrative
(separating the stages), NOT fit to data.

(a) MECHANISM CONFIRMED -- late + DEEP stage 2 (m2^2=0.01, b2=5e-4 -> chi2,0=4.47, DeltaF2=0.05):
       coasting plateau q ~ +0.03  ->  stage-2 q_min = -0.78 at t~800 (chi2 ordering)  ->  q -> 0 after.
    A clean, FINITE late-time acceleration epoch with q_min ~ -0.78 (comparable to observed
    q0 ~ -0.5), bracketed by coasting. The free-energy release DeltaF: 0.25 -> 0.30 across the epoch.
    [SOLID -- the multi-stage acceleration mechanism works.]

(b) OBSTRUCTION -- late + NATURAL stage 2 (m2^2=0.01, b2=1 -> chi2,0=0.10, DeltaF2=2.5e-5):
       stage-2 q_min = +0.000 (NEGLIGIBLE). A naturally-late (low-m2) transition is too SHALLOW to
    move the expansion. [NEG]

(c) WHY -- natural energy scaling. For b1=b2 the depth ratio is purely the scale ratio:
       DeltaF2/DeltaF1 = (M2/M1)^4 :   M2/M1=0.3 -> 8e-3 ;  0.1 -> 1e-4 ;  0.03 -> 8e-7.
    A transition late enough to act now sits at low scale M2, so its release is (M2/M1)^4-suppressed
    against the primordial floor DeltaF1. The deep case (a) only worked because b2 was tuned tiny
    (5e-4), i.e. an anomalously FLAT, deep well -- decoupling depth from timing by hand. [TUNE]

================================================================================
4. IS THE SECOND SCALE DERIVED? -- HONEST AUDIT
================================================================================
Two new inputs appear: m2^2 (timing) and b2 (depth/flatness). For a LATE, ENERGETICALLY RELEVANT
transition the theory must supply BOTH "small m2^2" (late) AND "small b2" (deep-despite-late).
  * Natural relativistic scaling (b ~ O(1)) ties depth to scale: DeltaF ~ M^4. Then late = low M =
    energetically negligible (Sec 3c). No acceleration.
  * Getting an O(1) |q| at late times needs DeltaF2 ~ DeltaF1 with M2 << M1 -> b2 ~ (M2/M1)^4 b1,
    a tuned, anomalously flat second well. Nothing in the current theory fixes b2 to this value.
  * A Coleman-Weinberg (dimensional-transmutation) second scale would be naturally LOW but also
    naturally SHALLOW (CW depth ~ scale^4) -- same obstruction.
VERDICT: the two-stage STRUCTURE is derived and the acceleration MECHANISM is real (q<0, finite
epoch). But the SCALE and DEPTH that would place a significant acceleration at the observed epoch
are TUNED inputs, not derived. CCEF here REPRODUCES the cosmological-constant magnitude/coincidence
problem (why is a late, low-scale ordering energetically comparable to today's expansion driving?)
in coarsening language; it does not dissolve it. Per the no-hand-fitting discipline, this is flagged
as a fit, not presented as a prediction. [NEG / TUNE]

================================================================================
5. WHAT IS GENUINELY GAINED (and the non-GR character)
================================================================================
  - A DERIVED MECHANISM for cosmic acceleration within CCEF: free-energy release during a late
    ordering transition -> rising DeltaF -> convex L_ord -> q<0. No GR, no Lambda. [SOLID]
  - The acceleration is intrinsically FINITE/TRANSIENT (returns to coasting), NOT eternal de Sitter.
    This is a sharp qualitative CCEF-vs-GR signature and matches "acceleration as a recent, finite
    epoch." A CCEF-specific prediction: w_eff is not exactly -1 and the acceleration switches off
    again as the transition completes -- falsifiable against future w(z)/H(z). [STRUCT]
  - q_min ~ -0.8 is readily reached, so MAGNITUDE is not a dynamical problem -- only the
    SCALE-SETTING (when, and why energetically relevant) is unresolved. [SOLID / NEG]

================================================================================
6. HONEST STATUS
================================================================================
[SOLID]
  - Two-stage U(chi1,chi2) + coupled Model-A dynamics + coarsening front law.
  - q = -gamma_0 L DeltaF'/DeltaF^2: any rising DeltaF gives q<0; a late transition gives a finite
    acceleration epoch (numerically q_min ~ -0.78), then coasting.
  - Acceleration is finite/transient (non-GR; not eternal de Sitter) -> falsifiable w(z) signature.
[NEG / TUNE]
  - A naturally-late (low-scale) transition is energetically negligible: DeltaF2/DeltaF1=(M2/M1)^4.
  - A significant late epoch needs a tuned flat-deep well (b2 ~ (M2/M1)^4): the second scale/depth
    is an INPUT, not derived. CCEF reproduces, not resolves, the cosmological-constant
    magnitude/coincidence problem.
[DEFER -- what could make it derived]
  - A mechanism that ties chi2's onset to an internal threshold (e.g. L_ord crossing a scale that
    turns a sub-dominant operator relevant), so timing AND depth follow from existing quantities
    rather than new ones. Not found yet; this is the crux for a parameter-free dark energy.
  - The horizon-scale perturbation calc (from the redshift/slip note) would then give w(z), f sigma_8
    across the acceleration epoch to confront data.

================================================================================
7. ONE-PARAGRAPH SUMMARY
================================================================================
Adding a second ordering channel, U(chi1,chi2) = [-(m1^2/2)chi1^2+(b1/4)chi1^4] +
[-(m2^2/2)chi2^2+(b2/4)chi2^4] + (lam/2)chi1^2chi2^2, and feeding the released free energy into the
coarsening front (a ~ L_ord, gamma_0 dL/dt = DeltaF(t)), gives q = -gamma_0 L DeltaF'/DeltaF^2, so
any epoch in which a transition is RELEASING free energy (DeltaF rising) is an epoch of genuine
acceleration q<0 -- and because the front returns to constant speed once the transition saturates,
the acceleration is FINITE/transient, not eternal de Sitter (a clean non-GR signature, with a
falsifiable w(z) that is not exactly -1). Numerically a late, deep stage-2 reaches q_min ~ -0.78
(comparable to the observed q0 ~ -0.5) flanked by coasting. The catch, found honestly: a transition
late enough to act today is low-scale, with energy release DeltaF2 ~ M2^4 suppressed by (M2/M1)^4
against the primordial floor; making it matter requires an anomalously flat, deep second well (a
tuned tiny b2). So the two-stage STRUCTURE and the acceleration MECHANISM are derived and real, but
the SCALE and DEPTH that would put a significant acceleration at the observed epoch are tuned inputs
-- CCEF reproduces the cosmological-constant magnitude/coincidence problem rather than dissolving
it. The genuinely-required next step is an internal trigger (e.g. L_ord crossing a threshold that
makes a sub-dominant operator relevant) that fixes the second transition's scale and depth from
existing quantities -- the open path to a parameter-free CCEF dark energy.
================================================================================
