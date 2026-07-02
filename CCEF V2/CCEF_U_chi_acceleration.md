================================================================================
CCEF v2 — DERIVATION NOTE: U(chi) RADIATIVELY, AND WHETHER ANY U ACCELERATES
Priority #4 from the v2 handoff (Sec 9). Derived from the theory; no hand-fitting.
No GR / Friedmann imported -- acceleration is treated as coarsening kinematics.
Compiled 2026-06-29. Builds on CCEF_Lord_IR_EFT_derivation.md,
CCEF_gamma_CaldeiraLeggett_derivation.md, CCEF_redshift_slip_at_Lord.md.
Labels: [SOLID] derived/verified | [STRUCT] forced by structure | [NEG] honest negative
        | [DEFER] needs further structure
================================================================================

--------------------------------------------------------------------------------
0. THE TWO QUESTIONS, AND THE HEADLINE
--------------------------------------------------------------------------------
Q1: Can U(chi) be derived (radiative self-generation)?
Q2: Does any U give late-time acceleration / inflation?

HEADLINE:
  A1. YES, partially. The one-loop Coleman-Weinberg potential from integrating out the
      Goldstone + emergent-gauge fluctuations (with chi-dependent masses) is computable and comes
      out SECOND-ORDER (smooth), of the form
         U(chi) = (m0^2/2) chi^2 + (b/4) chi^4 + (3 g^4/64 pi^2) chi^4 [ ln(chi^2/mu^2) - 25/6 ],
      i.e. a radiatively-generated, log-corrected quartic. The mass term m0^2 is the single tuned
      relevant operator; the rest is predicted. The ordered minimum sits at chi_0 with a residual
      free-energy FLOOR  DeltaF = U(0) - U(chi_0) = (3 g^4/128 pi^2) chi_0^4 > 0. [SOLID structure;
      overall scale UV-sensitive, but RG-irrelevant for the cosmological EXPONENT, Sec 5 of v2.]

  A2. NO -- not genuine acceleration, for ANY static U, within minimal single-field coarsening.
      Because expansion is COARSENING (a ~ L_ord), not Friedmann, a free-energy floor does NOT
      act as a cosmological constant. Instead it biases the order-parameter front, which moves at
      CONSTANT velocity (verified numerically: v proportional to DeltaF), giving
         L_ord ~ v t  (LINEAR)  =>  a ~ t,  H = 1/t,  q = 0   (COASTING).
      This UPGRADES the no-floor result (q=+1, a~t^1/2) to a marginal coasting cosmology, but it
      is NOT acceleration (q<0). The eternal equilibrium bath keeps the friction gamma_0 constant
      (no "cooling"), so no static U can do better than q=0. [SOLID / NEG]

  SHARP NON-GR POINT: the SAME free-energy floor DeltaF that would drive exponential de Sitter
  inflation (H=const, a~e^{Ht}) in GR drives only LINEAR coasting (a~t) in CCEF. CCEF does NOT
  inflate from vacuum free energy. This both (i) explains why the old "inflation from exponential
  ordering" was wrong (it mis-used the local amplitude as the ruler) and (ii) is a falsifiable
  qualitative split between CCEF and GR. [STRUCT]

  WHAT GENUINE ACCELERATION WOULD REQUIRE: a front whose driving force GROWS or whose friction
  DROPS in time -- i.e. MULTI-STAGE ordering (a second ordering transition switching on a new
  relevant operator at late times). That is extra structure beyond the minimal theory; it is NOT
  supplied by any static U and is NOT hand-fit here. [DEFER -> priority for a complete history]

================================================================================
1. Q1 -- RADIATIVE U(chi) FROM COLEMAN-WEINBERG
================================================================================
Integrate out the fast fluctuations around a homogeneous amplitude background chi. The modes with
chi-dependent masses (from the action, Reference Sec 1-2):
  * Emergent CP^1 gauge boson (the "photon"): Anderson-Higgses on the ordered vacuum, mass
    m_gamma^2 = g^2 chi^2 with g^2 = A1/(2 A2) (Reference Sec 2: m_gamma=sqrt(A1/2A2) at chi_0).
    -> 3 massive-vector polarizations, the dominant CW source.
  * Amplitude (radial sigma) fluctuation: mass^2 = U''(chi).
  * Goldstone (angular) modes: massless directions; their determinant depends on chi via the
    stiffness chi^2 but gives no chi^4 ln term at leading order (they enter the wave-function /
    kinetic renormalization, not the dominant CW quartic).

One-loop effective potential (relativistic z=1 IR window, which controls the log; the z=2 UV only
renormalizes the cutoff mu, i.e. ties the scale to A3 -- Reference's "scale tied to A3/cutoff"):
   U_1loop(chi) = SUM_i (n_i/2) INT d^4k_E/(2pi)^4 ln( k^2 + M_i^2(chi) )
                = SUM_i n_i ( M_i^4 / 64 pi^2 ) [ ln(M_i^2/mu^2) - c_i ] .
The massive-vector piece (n=3, c=5/6) dominates:
   U_gauge(chi) = (3 g^4 / 64 pi^2) chi^4 [ ln(g^2 chi^2/mu^2) - 5/6 ] .
Adding the tree mass and quartic:
   U(chi) = (m0^2/2) chi^2 + (b/4) chi^4 + (3 g^4/64 pi^2) chi^4 [ ln(chi^2/mu^2) - 25/6 ] .  [SOLID]

Properties (all derived, none fit):
  (i)  SECOND-ORDER / SMOOTH: U is analytic with a single non-degenerate minimum; even at m0^2 = 0
       the radiative chi^4 ln chi generates a minimum at chi_0 != 0 (Coleman-Weinberg radiative
       symmetry breaking) with NO barrier. Confirms the handoff's "comes out second-order, gradual
       swelling, not nucleation." [SOLID]
  (ii) The MASS term m0^2 is the one RELEVANT (tuned) operator; the quartic is MARGINAL (runs
       logarithmically); the gauge CW term is PREDICTED from g (=A1/2A2). [SOLID]
  (iii) RESIDUAL FLOOR: minimizing, U(chi_0) = -(3 g^4/128 pi^2) chi_0^4 < 0 while U(0)=0, so the
       ordered phase lies BELOW the disordered phase by
          DeltaF == U(0) - U(chi_0) = (3 g^4/128 pi^2) chi_0^4  > 0 .                  [SOLID]
       DeltaF is the bulk free-energy bias that drives the ordered domain to grow. Its MAGNITUDE
       is UV-sensitive (through g, chi_0, mu ~ cutoff/A3) -- consistent with the v2 result that the
       UV is unpinned but RG-IRRELEVANT for the cosmological exponent (it sets the coasting RATE,
       not the q). [SOLID + caveat]

================================================================================
2. Q2 -- WHAT U DOES TO THE EXPANSION (coarsening kinematics, NOT GR)
================================================================================
Expansion in CCEF is the coarsening of the ordered domain: a proportional to L_ord(t). Therefore
"acceleration" means d^2 a/dt^2 > 0, i.e. L_ord(t) CONVEX (grows faster than linear). It is NOT a
Friedmann response to an energy density. We must NOT read DeltaF as a cosmological constant; we
must feed it into the order-parameter front dynamics. The relaxational front EOM (Model A, the
derived class) with the potential U is
   gamma_0 d_t chi = A1 lap chi - U'(chi) ,
whose moving-front (domain-wall) solutions set L_ord(t). Two driving terms compete:
   - CURVATURE (surface tension sigma, ~1/L): always DECELERATING (force fades as domains grow).
   - BULK BIAS (the floor DeltaF): a constant push of the favored phase.

REGIME TABLE (all from the same EOM; gamma_0 = const because the bath is eternal/equilibrium):
   DeltaF = 0  (symmetric wells):  pure curvature  ->  L_ord ~ t^(1/2),  q = +1   (decelerating)
   DeltaF > 0  (floor):            constant-speed front ->  L_ord ~ t,    q = 0    (COASTING)
   (faster than linear):           requires growing drive / falling friction -> NOT from static U

NUMERICAL CONFIRMATION (this note): a 1D driven TDGL with a tilted double well
U'(chi) = -chi + chi^3 - h (bias h ~ DeltaF) gives a front moving at CONSTANT velocity, with
   v(h=0.05,0.10,0.20) = 0.105, 0.204, 0.417 ;  v/h = 2.09, 2.04, 2.09 (const) ; linear-fit R^2 ~ 1 ;
   h=0 front stationary.
So v proportional to DeltaF and CONSTANT in time => L_ord = v t (LINEAR) => a ~ t, q = 0. The
analytic Allen-Cahn front speed v = (3/sqrt2) h ~ 2.12 h matches. [SOLID]

THE NON-GR CONTRAST (central, and the reason the user's "no GR" instruction matters):
   In GR a vacuum free-energy density DeltaF sources H = sqrt(8 pi G DeltaF/3) = const => a ~ e^{Ht}
   (de Sitter inflation). In CCEF the SAME DeltaF drives a coarsening front at CONSTANT SPEED =>
   a ~ t (coasting). Same free energy, qualitatively different cosmology. CCEF does not inflate
   from a floor. This is exactly why the earlier "exponential ordering inflation" (a_eff ~ chi,
   H = chi'/chi) was a GR-like illusion built on the wrong (UV, amplitude) ruler; with the correct
   L_ord ruler and genuine coarsening kinematics, a floor coasts, it does not inflate. [STRUCT]

================================================================================
3. CAN ANYTHING IN THE MINIMAL THEORY GIVE q < 0? -- HONEST AUDIT
================================================================================
Acceleration (L_ord convex) needs the front to speed up: either the driving force grows, or the
friction gamma_0 falls, with time. Check each against the theory:
  * Static U: gives at most a constant DeltaF -> constant front speed -> q = 0. Cannot exceed
    linear. (A larger DeltaF gives a faster coast, not an accelerating one.) [SOLID, NEG]
  * Falling friction gamma_0 ~ Zt^2 chi_0^2 T_eff: would need the medium's effective temperature
    T_eff to DROP in time. But the disordered medium is ETERNAL and at fixed equilibrium (v2
    ontology, Sec 1) -- it is an infinite reservoir, so T_eff = const and gamma_0 = const. No
    "cosmic cooling" of the bath, hence no acceleration from dropping friction. [SOLID, NEG]
  * Growing DeltaF: would need U itself to change in time, i.e. a SECOND ordering transition
    switching on a new relevant operator at late times (MULTI-STAGE ordering). Not present in the
    minimal single-field theory; it is genuine extra structure. [DEFER]
VERDICT: within minimal CCEF (one order-parameter, eternal bath, static radiatively-derived U),
the expansion is decelerating (q=+1) or, with the floor, marginally coasting (q=0). It NEVER
accelerates (q<0). [SOLID, NEG]

================================================================================
4. COSMOLOGICAL READOUT OF THE COASTING (floor) CASE
================================================================================
If the radiative floor dominates at late times (DeltaF L >> sigma, i.e. domains past the bias
scale), L_ord ~ t and:
   a ~ t,  H = 1/t,  q = 0,   1+z = a_0/a = t_0/t = H_0/H => H(z) = H0 (1+z).
   D_C(z) = INT_0^z dz'/H(z') = (1/H0) ln(1+z) ;  D_L = (1+z)(1/H0) ln(1+z) ;
   D_A = (1/H0) ln(1+z)/(1+z).
This is the eternal-coasting ("R_h = ct"-like) cosmology -- a marginal, much-debated but not-dead
fit to SNe/BAO, and a clear improvement on the t^(1/2) skeleton (which gave H(z)=H0(1+z)^2,
overshooting by 1.7-3x; see the redshift note). The coasting RATE H_0 is set by DeltaF (UV-
sensitive, unpinned), but the EXPONENT q=0 is universal. The redshift kinematics (3 tests) carry
over unchanged from the redshift note -- still a genuine metric redshift. [SOLID structure;
rate not pinned]

OBSERVED q_0 ~ -0.5 (acceleration) is therefore NOT reproduced by minimal CCEF. The honest gap:
minimal CCEF tops out at coasting; genuine acceleration needs multi-stage ordering (Sec 3).

================================================================================
5. HONEST STATUS
================================================================================
[SOLID -- derived]
  - U(chi) one-loop Coleman-Weinberg form; second-order/smooth; radiative symmetry breaking; the
    mass term is the single tuned operator, the gauge CW quartic is predicted.
  - The residual floor DeltaF = (3 g^4/128 pi^2) chi_0^4 > 0.
  - Floor -> biased Model-A front at CONSTANT speed (numerically v proportional to DeltaF, R^2~1)
    -> L_ord ~ t -> a ~ t, q = 0 coasting; readout H(z)=H0(1+z), D_L=(1+z)ln(1+z)/H0.
  - Non-GR split: a floor that inflates (de Sitter) in GR only coasts (a~t) in CCEF.

[NEG -- honest negatives]
  - No static U gives q < 0. Minimal CCEF cannot accelerate: bath eternal (gamma_0 const), static
    U gives only a constant bias. Best case is coasting (q=0); observed q_0<0 is not reached.
  - The floor's MAGNITUDE (hence the coasting H_0) is UV-sensitive/unpinned -- only the exponent
    q=0 is universal.

[DEFER -- the genuinely-required extra structure]
  - Late-time acceleration (q<0) needs MULTI-STAGE ordering: a second ordering transition turning
    on a new relevant operator at late times, so the front re-accelerates (growing DeltaF). This
    is derivable in principle (a second tuned operator / a cascade of orderings) but is NOT part
    of the minimal action and is NOT hand-fit here. Next concrete sub-task: write the two-stage
    free energy U(chi_1, chi_2) and test whether the second stage yields q<0 -- with the second
    transition's scale derived, not tuned to data.
  - Equivalently, an explicit horizon-scale perturbation calc (from the redshift/slip note) would
    give growth f sigma_8(z) for the coasting background to confront data.

================================================================================
6. ONE-PARAGRAPH SUMMARY
================================================================================
The amplitude potential is partially derivable: the one-loop Coleman-Weinberg potential from the
Goldstone and Anderson-Higgsed emergent-gauge fluctuations is U(chi) = (m0^2/2)chi^2 + (b/4)chi^4
+ (3g^4/64pi^2)chi^4[ln(chi^2/mu^2) - 25/6], which is second-order/smooth (radiative symmetry
breaking, no barrier), with the mass term the single tuned operator and a residual free-energy
floor DeltaF = (3g^4/128pi^2)chi_0^4 > 0 below the disordered phase. Whether any U accelerates is
decided by coarsening kinematics, not Friedmann: a ~ L_ord, so acceleration means L_ord convex.
Feeding the floor into the derived Model-A front dynamics, the front moves at CONSTANT velocity
proportional to DeltaF (confirmed numerically, v/h ~ const, R^2 ~ 1), so L_ord ~ t and a ~ t, H=1/t,
q = 0 -- a coasting cosmology, an improvement on the t^(1/2) (q=+1) skeleton but NOT acceleration.
Crucially, the same floor that would drive exponential de Sitter inflation in GR only coasts in
CCEF -- the theory does not inflate from vacuum free energy, which also retires the old
exponential-ordering inflation. Because the disordered bath is eternal (friction constant) and a
static U supplies only a constant bias, NO static U reaches q < 0: minimal CCEF tops out at
coasting. Genuine late-time acceleration requires multi-stage ordering (a second, later ordering
transition giving a growing drive) -- real extra structure, derivable but beyond the minimal
action, and deliberately not hand-fit here.
================================================================================
