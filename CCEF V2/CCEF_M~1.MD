================================================================================
CCEF v2 — HYPOTHESIS NOTE: WHAT DETERMINES THE EFFECTIVE LARGE-SCALE METRIC?
              THREE CANDIDATES TO REPLACE THE FALSIFIED ANSATZ a ∝ L_ord
Reframing after F/G/H: what those notes falsified is NOT the continuum and NOT
"CCEF cosmology" -- it is ONE IDENTIFICATION, the ansatz a(t) ∝ L_ord(t) (which
the redshift note introduced as "[given]", i.e. an assumption, never a derived
necessity). Same continuum, same action, same transition (eternal, ENERGY-based:
the ordered phase invades an eternal disordered medium because it is
energetically favored), same derived quantities. The question is re-opened at
the right level: GIVEN exactly this continuum, what plays the role of the
effective large-scale metric? Compiled 2026-07-02.
Labels: [HYP] hypothesis to be computed | [SOLID] already-derived input |
        [RISK] known danger | [KILL] first kill-test
================================================================================

--------------------------------------------------------------------------------
0. WHAT THE FALSIFICATION ACTUALLY REMOVED, AND WHAT IT FREED
--------------------------------------------------------------------------------
REMOVED: a(t) ∝ L_ord(t) -- the single-front-radius ruler. With it go coasting,
H = H0(1+z), and the F/G/H failures. NOTHING ELSE: the emergent acoustic metric
(c_eff = 1, universality Delta-c/c = 0), the composite graviton (massless,
healthy, z=1), the verified induced Einstein equation G_munu = 8 pi G T_munu
(5.8e-16), the redshift kinematics (metric redshift, Planck->Planck -- these
hold for ANY a(t)), the slip null eta = Sigma = 1, the growth machinery (re-run
per background), L* = sigma/DeltaF, gamma_0, DeltaF -- all [SOLID], all retained.

FREED: the ceiling theorem (p <= 1, q >= 0) is a theorem about FRONTS. If a(t)
is not a front radius, the ban on acceleration LIFTS. The data's q < 0 demand,
fatal to any coasting front, becomes admissible. The falsification was of the
ruler, and it points its own way out: the observed H(z) (radiation -> matter ->
Lambda-like) is exactly what a metric SOURCED BY THE CONTINUUM'S ENERGY CONTENT
would do -- and CCEF already possesses the equation that says so.

The three candidates below answer "what determines the metric" at three
different structural levels: DYNAMICS (A), GEOMETRY/BOUNDARY (B), DEFINITION (C).
They are not mutually exclusive -- B is the global geometry of A's solution, and
C is the microscopic definition underlying both -- but each stands alone as a
computable program with its own first calculation and kill-test.

================================================================================
CANDIDATE A — INDUCED-EINSTEIN CLOSURE (Sakharov-Friedmann)
"The metric is determined by the continuum's own verified field equation."
================================================================================
IDENTIFICATION [HYP]: the large-scale metric is the self-consistent solution of
the ALREADY-DERIVED induced Einstein equation, coarse-grained over the interior:
   G_munu[g] = 8 pi G <T_munu>_coarse ,
with <T_munu> built from what the continuum actually contains after the
transition: (i) RADIATION -- the thermalized latent heat of the energy-based
transition (rho_r ~ T^4, T ~ T_c at birth, redshifting as a^-4); (ii) MATTER --
solitons/baryons (Kibble-formed, a^-3) and defect relics; (iii) VACUUM-SECTOR
terms -- the CW floor U(chi_0) and the wall/bias energy of the ordering.
Homogeneity + isotropy then give an emergent FRIEDMANN equation
   H^2 = (8 pi G / 3) [ rho_r + rho_m + rho_vac(eff) ]  ( - k/a^2 ) ,
i.e. the metric is DYNAMICAL and SOURCED, not kinematically tied to any front.
L_ord becomes an ordinary internal length that grows THROUGH the metric (the
front is a structure IN the universe, not the universe itself).

WHY IT IS THE MINIMAL REPAIR: the equation is not imported from GR -- it is the
theory's own, verified to 5.8e-16 (Reference Sec 5). The a ∝ L_ord ansatz
OVERRODE this dynamics by fiat; candidate A simply stops overriding it. The
whole prior perturbation program (Poisson equation, growth, slip) already
assumed induced-Einstein response to delta-rho -- A extends the same statement
to the zeroth-order background, which is where it arguably always belonged.

EXPECTED HISTORY [HYP]: radiation era H ~ (1+z)^2 from the transition's latent
heat (T_c ~ 140 MeV start -> BBN-compatible thermal history), matter era from
solitons, late-time behavior set by rho_vac(eff) -- potentially Lambda-like,
and q < 0 is now allowed. This is structurally the observed universe.

WHAT IT INHERITS FOR FREE [SOLID]: redshift kinematics, graviton, slip null;
growth on this background = standard induced-Einstein growth (GR-like, fits).

[RISK 1 -- the induced cosmological constant]: Sakharov induction generates not
only 1/16piG (a1 term, computed, healthy) but a vacuum term (a0 term). CCEF
avoided the CC problem precisely BY tying a to L_ord; candidate A imports it.
Worse, the ordered phase's floor is NEGATIVE: U(chi_0) = -(3g^4/128pi^2)chi_0^4.
What is the physical zero? Plausible resolution: the interior gravitates
RELATIVE to the eternal disordered medium (U(0) = 0), making the interior
vacuum term negative (small AdS-like pull) or the wall/bias sector supplying a
positive effective component -- must be COMPUTED, not chosen. This is the
make-or-break of candidate A.                                            [RISK]
[RISK 2]: why did the front's L_ord ever look like the ruler? A must show that
in its solution, comoving observers see the domain grow ~ conformally (so the
old intuition was a coordinate artifact), or explain the ansatz's original
motivation away cleanly.

FIRST CALCULATION: coarse-grain T_munu of the post-transition medium (latent-
heat radiation + soliton dust + CW floor + wall skin at L*/L ~ 1e-39) and solve
G = 8piG<T> for a(t); compute the a0 (induced-Lambda) Seeley-DeWitt term in the
same heat-kernel framework that gave a1, INCLUDING the phase-relative zero
(interior minus eternal-medium). Deliverables: H(z), sign and size of
Lambda_eff.
[KILL]: r_d = 147 Mpc and 100 theta* = 1.041 come out essentially automatically
IF the radiation era is standard -- the kill-test is Lambda_eff: wrong sign or
wrong magnitude (the 10^120 problem returning) kills A. Then G's joint MCMC
re-run is the quantitative gate.

================================================================================
CANDIDATE B — BUBBLE-INTERIOR GEOMETRY (junction closure)
"We live inside the bubble; the metric is the interior solution, in interior
 time -- not the wall radius, in wall time."
================================================================================
IDENTIFICATION [HYP]: the ordered domain is a single bubble expanding into the
eternal disordered medium (the energy-based transition made geometric). The
effective metric for INTERIOR observers is fixed by the Israel junction
conditions at the wall (tension sigma, bias DeltaF -- both derived) plus the
interior content (latent-heat radiation at T ~ T_c, then solitons), with the
induced-Einstein equation governing both sides. The interior of such a bubble
is an OPEN (k = -1) FRW cosmology in its own comoving slicing; crucially,
INTERIOR COSMIC TIME IS NOT EXTERIOR FRONT TIME. The front can coast forever in
the eternal medium's clock (exactly as note H found -- that result becomes
CORRECT-BUT-IRRELEVANT, a statement about the outside) while the interior a(t)
runs a genuine radiation -> matter history driven by its own contents.

WHY IT IS ATTRACTIVE: it keeps EVERYTHING the F/G/H sequence established --
the front really does coast (H, in exterior time) -- and relocates the observed
cosmology to the slicing the observers actually live on. The "anchor tension"
(T_c-anchor vs L*-anchor, 29 orders apart, flagged [OPEN] in note F) dissolves:
T redshifts with INTERIOR a, while L_ord grows with EXTERIOR front time -- they
were never the same clock, and conflating them was the ansatz's deepest error.
The transition = a genuine hot big-bang surface (energy-based, eternal medium
before it): CCEF's ontology, standard cosmology's phenomenology.

EXPECTED HISTORY [HYP]: open FRW born at T ~ T_c: radiation era (a ~ t^1/2,
H ~ (1+z)^2 -- the CMB/BBN sector plausibly standard), matter era, then
curvature domination (H ~ (1+z), q = 0 -- coasting RETURNS, but only at late
times) unless a vacuum-sector term (candidate A's Lambda_eff) takes over first.

[RISK -- flatness/Omega_k]: an open interior with no inflationary phase must
explain |Omega_k0| < ~0.001 (Planck+BAO). Born curvature-dominated at T_c, the
natural Omega_k today is O(1) -- late-time curvature-coasting at z ~ 0.5-2 is
already strongly disfavored by G's BAO/SNe data. B needs either an enormous
initial curvature radius (WHY? -- possibly the pre-transition correlation
structure of the eternal medium sets it; must be derived, not assumed) or an
interior vacuum era. This is B's make-or-break.                          [RISK]
Secondary [RISK]: single-bubble vs many-bubble (Kibble) -- if the transition
nucleates densely, the one-bubble geometry is wrong and B degrades to A.

FIRST CALCULATION: Israel junction conditions for a sigma/DeltaF wall between
the eternal (disordered, U = 0) exterior and an ordered interior with radiation
rho_r(T_c) + floor U(chi_0), both sides under induced-Einstein gravity; extract
the interior FRW (a(t_int), k, curvature radius) and Omega_k(z). Deliverables:
Omega_k0 prediction; where curvature domination sets in.
[KILL]: Omega_k0. If the derived curvature radius cannot satisfy
|Omega_k0| < 0.001 without tuning, B is dead by its own numbers -- cleanly.

================================================================================
CANDIDATE C — CORRELATIONAL METRIC (definitional closure)
"Take 'metric from correlations of the field' literally at zeroth order:
 a(t) is a two-point function, not a domain size."
================================================================================
IDENTIFICATION [HYP]: the theory's foundational statement (Reference Sec 0:
"no external spacetime; metric, gravity, matter all emergent from correlations
of the field") already DEFINES the metric microscopically -- the same object
whose perturbation gives the graviton:
   g_ij(t)  ~  A1 sum_a < d_i n_a d_j n_a >_coarse   =>   a^2(t) from the
evolving CORRELATION CONTENT of the medium: condensate stiffness chi_0^2(t),
thermal Goldstone occupation (a T^4-weighted gradient energy), soliton/defect
density, wall density. The original sin, in this reading, was substituting the
correlation LENGTH (L_ord, where <nn> decays) for the correlation AMPLITUDE
tensor (which is what delta_g_ij ~ A1 d_i n d_j n actually coarse-grains to).
The graviton was always built from the amplitude object -- the background
should be too. One definition, zeroth + first order together.

MECHANISM FOR ERA STRUCTURE [HYP]: a^2(t) receives additive contributions from
distinct correlator components -- thermal-fluctuation part (falls as the medium
cools, ~ T^4/Lambda^4-weighted), condensate part (grows/saturates as ordering
completes), defect part (dilutes). DIFFERENT TERMS DOMINATE IN DIFFERENT ERAS,
giving era transitions (radiation-like -> matter-like -> saturation/Lambda-like)
from the correlator composition alone, with NO new scales -- everything is
built from Lambda, T_c, gamma_0, chi_0. The cooling law T(a) and the metric
definition a(<...(T)...>) close into a self-consistent dynamical system.

WHY IT IS THE DEEPEST OPTION: A imports the metric's dynamics (its own, but
still an equation); C derives what the metric IS, from which A's dynamics
should FOLLOW as the consistency (Ward identity / conservation) condition. If
C works, it explains WHY G = 8piG T holds for the background and what rho_vac
(A's [RISK 1]) actually is -- the CC problem becomes the calculable question
"what is the T -> 0 limit of the condensate correlator", with the eternal
medium supplying the subtraction point.

[RISK 1]: hardest derivation; the coarse-graining and the choice of comoving
coordinates must be fixed by the theory (danger of smuggling the answer in via
the window function).                                                    [RISK]
[RISK 2]: it may simply re-derive a ∝ L_ord in the scaling regime (if the
correlator is dominated by the domain structure, its only length IS L_ord) --
in which case C collapses back onto the falsified ansatz and dies fast. That
would itself be informative: it would prove the ansatz was C done right, and
eliminate the definitional route.                                        [RISK]

FIRST CALCULATION: evaluate A1<d_i n d_j n> in the post-transition cooling
medium: condensate + thermal (Rayleigh-Jeans at T_eff, the gamma-note bath) +
defect gas contributions; write a^2(t) explicitly; impose T ~ 1/a consistency
(metric redshift, already [SOLID]); solve the closed system for H(z).
Deliverables: which correlator term dominates when; the predicted era sequence
and exponents.
[KILL]: does a radiation-like era (H ~ (1+z)^2) emerge at T ~> eV, and does the
late-time exponent leave the falsified coasting line? If the system re-derives
a ∝ L_ord (RISK 2), C is dead on arrival -- check this FIRST, it is cheap.

================================================================================
COMPARISON AND RECOMMENDED ORDER
================================================================================
                      A (dynamics)      B (geometry)        C (definition)
  changes vs ansatz   minimal           moderate            maximal
  uses only derived   yes (G=8piGT)     yes (sigma,DeltaF)  yes (the correlator)
  radiation era       automatic         automatic           to be derived
  q<0 possible        yes (rho_vac)     via A's rho_vac     open
  make-or-break       sign/size of      Omega_k0 vs 1e-3    re-derives L_ord?
                      induced Lambda
  cheapest kill-test  a0/Lambda_eff     junction Omega_k    correlator eras
  relation            B = A's global geometry; C = the definition beneath A;
                      all three share the same first-principles inputs.
RECOMMENDED ORDER: C's RISK-2 check first (one afternoon: does the correlator
just give L_ord back?), then A's Lambda_eff computation (the pivotal number for
both A and B), then B's junction conditions (which need A's vacuum term anyway).
Note F/G machinery (cmb_coasting.py, mcmc_joint.py) is background-agnostic: any
candidate's H(z) can be dropped in for an immediate quantitative verdict --
theta*, r_d, and the full joint MCMC are now one-command kill-tests.

================================================================================
ONE-PARAGRAPH SUMMARY
================================================================================
What F/G/H falsified is the ansatz a ∝ L_ord -- the single-front ruler -- not the
continuum, and removing it also removes the ceiling theorem's ban on q < 0, which
was a theorem about fronts. Given exactly the same continuum, three candidates
answer "what determines the effective large-scale metric," at the levels of
dynamics, geometry, and definition. (A) Induced-Einstein closure: stop overriding
the theory's own verified equation G = 8piG T and let the coarse-grained contents
(latent-heat radiation, soliton matter, vacuum sector) source an emergent
Friedmann background -- minimal, automatically radiation-dominated early,
make-or-break on the sign and size of the induced Lambda (the CC problem the
ansatz had elegantly dodged). (B) Bubble-interior geometry: the ordered domain is
a bubble in the eternal medium and observers live on the interior slicing, where
junction conditions (sigma, DeltaF) plus interior content give an open FRW whose
cosmic time is not the front's time -- the H-note's eternal coasting front stays
true but describes the outside; make-or-break on deriving |Omega_k0| < 1e-3.
(C) Correlational metric: take "metric from correlations" literally -- a^2(t) is
the coarse-grained amplitude correlator A1<dn dn> (the same object whose
perturbation is the graviton), with era structure from which correlator component
(thermal, condensate, defect) dominates; deepest and hardest, dead on arrival if
it merely re-derives L_ord -- which is the cheap first check. Recommended order:
C's collapse check, A's Lambda_eff, B's junction conditions; every candidate's
H(z) can be fed straight into the existing theta*/r_d/joint-MCMC machinery for an
immediate verdict.
================================================================================
