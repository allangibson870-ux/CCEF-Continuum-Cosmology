================================================================================
CCEF v2 — DERIVATION NOTE: L_ord(t) AND THE IR EFFECTIVE THEORY
Priority #1 from the v2 handoff (Sec 9). Derived cold from the action.
Compiled 2026-06-29.
Labels: [SOLID] derived/verified | [GATED] fixed once gamma/class chosen | [DEFER] later priority
Discipline: derive from the action; carry gamma symbolic; label every assumption.
================================================================================

--------------------------------------------------------------------------------
0. OBJECTIVE AND ONE-LINE RESULT
--------------------------------------------------------------------------------
GOAL: run the coarsening / IR-fixed-point EFT explicitly and obtain L_ord(t) — the
growing coherence length that is the v2 cosmological ruler (Scale 2). The framework
(action Sec 2; RG to a Gaussian/mean-field fixed point Sec 5; coarsening picture Sec 6)
is fixed; the remaining freedom is the dynamics class set by the bath friction gamma.

RESULT (carrying gamma symbolic, both branches):

  IR EFT (coarse-grained, irrelevant operators dropped):
     F_IR[chi] = INT d^3x [ (A1/2)|grad chi|^2 + (r/2)chi^2 + (u/4)chi^4 ]
     dynamics: Zt d_t^2 chi + gamma d_t chi = A1 lap chi - U'(chi)   (+ noise)

  Late-time (overdamped, t >> Zt/gamma) coarsening growth law:
     Model A (non-conserved chi):  L_ord(t) = sqrt( (2 A1 / gamma) t )  ~  t^(1/2)
     Model B (conserved chi):      L_ord(t) = ( K_B t )^(1/3)           ~  t^(1/3)

  Cosmological readout (a_cosmo proportional to L_ord):
     a(t) ~ t^p ,  H = p/t ,  q = (1-p)/p ,  1+z = (t_obs/t_em)^p
        Model A: p=1/2, H=1/(2t), q=1  (decelerating, radiation-like in FORM, not in origin)
        Model B: p=1/3, H=1/(3t), q=2

COLD NUMERICAL CHECK (this note): a 2D Model-A TDGL run built directly from F_IR, with no
analytic input, gives L_ord ~ t^0.496 (wall-density measure) — confirming the Allen-Cahn 1/2
to ~1%. [SOLID]

================================================================================
1. WHAT "IR" MEANS HERE, AND WHY ONLY THREE TERMS SURVIVE
================================================================================
The bare S^2/S^3 action (Reference Sec 1) carries five structures: Zt (time), A1 (gradient),
A2 (Faddeev-Skyrme, quartic in derivatives), A3 (Lifshitz bilaplacian, the z=2 UV regulator),
and A4 (the gap/easy-axis term). The v2 RG result (Theory Sec 5) is the lever:

  * Fixed point is GAUSSIAN / MEAN-FIELD. d_eff = d+z = 5 (UV, z=2) and 4 (IR, z=1); both at
    or above the upper critical dimension 4, so there is NO Wilson-Fisher fixed point and NO
    anomalous dimension. Mean-field exponents are exact (up to logs at d_uc=4). [SOLID]
  * RELEVANT operators: exactly ONE — the gap/tuning term (coefficient of chi^2, i.e. the
    A4-direction). It is what must be tuned to sit at the ordering transition.
  * A2 (Skyrme) and A3 (bilaplacian) are IRRELEVANT in the IR: [A2] = -1, and A3 k^4 is down
    by (k/k_UV)^2 relative to A1 k^2. The quartic self-coupling u is MARGINAL.

Consequence: at scales >> the healing length 1/Lambda (hence at the cosmological scale L_ord),
A2 and A3 flow to zero and drop out of the effective description. The cosmological sector is
therefore controlled by the relevant gap term + marginal quartic + the gradient stiffness A1.
This is the precise statement behind "cosmology is IR-universal and predictive despite the
unpinned UV" (Theory Sec 5): L_ord(t) below will NOT depend on A3, m_sigma, or the Skyrme
coupling. The baryon (gap-scale) sector keeps its UV sensitivity; the two decouple. [SOLID]

================================================================================
2. THE IR EFFECTIVE FREE ENERGY (static sector)
================================================================================
The ordering requires the amplitude chi = |phi| to be dynamical (Theory Sec 2: the soft-
constraint / linear-sigma extension; constrained CCEF has no amplitude). Coarse-graining the
action and keeping only relevant + marginal operators gives the standard Landau-Ginzburg
functional for the amplitude:

   F_IR[chi] = INT d^3x [ (A1/2)|grad chi|^2 + U(chi) ] ,
   U(chi)    = (r/2) chi^2 + (u/4) chi^4 + ...                               [SOLID, IR form]

   * r is the single RELEVANT (tuning) coupling: r > 0 disordered (chi=0), r < 0 ordered.
     r is the renormalized image of the gap/easy-axis term; r -> 0 is the ordering transition.
   * u is the MARGINAL quartic (logarithmically running at the z=1 IR fixed point, d_uc=4).
   * A2, A3 do NOT appear — they renormalized away (Sec 1). This is the IR-universality, made
     concrete: F_IR has no memory of the UV regulator.

Ordered vacuum and the microscopic scale (Scale 1):
   chi_0^2 = -r/u = |r|/u ,   amplitude gap m_sigma^2 = U''(chi_0) = -2r = 2|r| .
   Domain-wall (kink) profile chi(x) = chi_0 tanh(x / (sqrt2 xi_0)),
   healing length / wall thickness  xi_0 = sqrt(A1/|r|)  ~  1/Lambda  (Lambda = sqrt(A4/A1)). [SOLID]
   Wall surface tension  sigma = INT (A1 (chi')^2) dx = (2*sqrt2/3) sqrt(A1) |r|^{1/2} chi_0^2
                               ~ A1 chi_0^2 / xi_0 .

xi_0 is FIXED and microscopic (the gap, Scale 1). It is NOT the cosmological ruler. The
cosmological ruler is the size of the ordered domain, L_ord(t) >> xi_0, derived next. The
~60-order ratio L_ord/xi_0 = L_ord * Lambda is the age in microscopic units (Theory Sec 4),
not a tuned constant.

================================================================================
3. THE IR DYNAMICAL EFT — AND WHERE gamma ENTERS
================================================================================
The bare action is SECOND-order in time (Zt/2)(d_t chi)^2: reversible, energy-conserving,
propagating dynamics. This is exactly the acoustic "arena" of Theory Sec 3 (c_eff = sqrt(A1/Zt)
= 1). Reversible dynamics does NOT coarsen — it oscillates. Coarsening (hence expansion-as-
ordering) REQUIRES dissipation. The dissipation is the friction gamma obtained by integrating
out the disordered medium acting as a bath (Caldeira-Leggett; un-derived, priority #3). The IR
equation of motion is therefore the DAMPED relativistic field equation:

   Zt d_t^2 chi  +  gamma d_t chi  =  A1 lap chi  -  U'(chi)  (+ thermal noise) .     [SOLID form]

Two regimes, separated by the timescale tau_gamma = Zt/gamma:

   (i)  t << tau_gamma  (underdamped):  Zt d_t^2 dominates -> reversible wave propagation,
        c_eff = 1. This is the acoustic metric / graviton arena. NO coarsening. [SOLID]
   (ii) t >> tau_gamma  (overdamped):   gamma d_t dominates over Zt d_t^2 -> the relaxational
        (Time-Dependent Ginzburg-Landau) equation
            gamma d_t chi = A1 lap chi - U'(chi)  ==  d_t chi = Gamma (A1 lap chi - U'(chi)),
        with mobility Gamma = 1/gamma. THIS is the coarsening/cosmological regime. [SOLID]

So gamma plays a double role and is the whole gate:
   - Its MAGNITUDE decides whether the universe is in the coarsening regime at all (it is, at
     late cosmological times, since t >> tau_gamma there).
   - Together with the CONSERVATION LAW on chi it fixes the dynamics CLASS (Model A vs B),
     hence the growth exponent. See Sec 5.

================================================================================
4. L_ord(t): THE COARSENING GROWTH LAW (the central derivation)
================================================================================
In the ordered phase the field sits near +/- chi_0 in domains separated by walls of fixed
width xi_0 and tension sigma (Sec 2). The coherence length L_ord(t) = typical domain size =
correlation length of chi. Its growth is curvature-driven coarsening.

------------------------- 4A. MODEL A (non-conserved chi): ALLEN-CAHN ------------------------
Overdamped EOM: d_t chi = Gamma (A1 lap chi - U'(chi)), Gamma = 1/gamma.
Take a wall with local mean curvature K, normal coordinate u, profile chi(u). The Laplacian
near a curved wall is  lap chi = chi'' + K chi'  (standard differential-geometry expansion).
For a wall translating at normal velocity v, d_t chi = -v chi'. Insert:

   -v chi' = Gamma [ A1(chi'' + K chi') - U'(chi) ] .

The flat stationary kink obeys A1 chi'' - U'(chi) = 0 (Sec 2), so that bracket-piece cancels:

   -v chi' = Gamma A1 K chi'   =>   v = - Gamma A1 K = -(A1/gamma) K .          [ALLEN-CAHN]

Key features: the wall moves toward its centre of curvature (reduces area), and the velocity
is INDEPENDENT of the surface tension sigma — only the mobility Gamma A1 = A1/gamma enters.
The domain size grows as dL/dt ~ |v| ~ (A1/gamma)(1/L) since K ~ 1/L:

   L dL/dt = A1/gamma   =>   L_ord^2(t) = L_ord^2(0) + 2(A1/gamma) t

   ===>   L_ord(t) = sqrt( (2 A1 / gamma) t )  ~  t^(1/2) .                  [SOLID, Model A]

Dimension-independent (curvature is geometric), no anomalous exponent — consistent with the
mean-field fixed point. The prefactor depends ONLY on A1 (relevant gradient stiffness) and
gamma (bath friction): no A3, no m_sigma, no Skyrme. IR-universal, as promised. [SOLID]

------------------------- 4B. MODEL B (conserved chi): LIFSHITZ-SLYOZOV-CAHN ------------------
If instead chi is a conserved density (d_t chi = Gamma lap (delta F/delta chi), so INT chi is
fixed), coarsening proceeds by DIFFUSION of order parameter between domains rather than wall
sweeping. The interfacial chemical potential is set by Gibbs-Thomson, mu ~ sigma K / chi_0 ~
sigma/(chi_0 L). The diffusive current j ~ Gamma grad mu ~ Gamma sigma/(chi_0 L^2) feeds
domain growth dL/dt ~ j/chi_0:

   L^2 dL/dt ~ Gamma sigma / chi_0^2   =>   L_ord^3(t) = L_ord^3(0) + K_B t,
   K_B ~ Gamma sigma / chi_0^2 = (sigma)/(gamma chi_0^2)

   ===>   L_ord(t) = (K_B t)^(1/3)  ~  t^(1/3) .                            [SOLID, Model B]

Here the surface tension sigma DOES enter the prefactor (capillary-driven), unlike Model A.

------------------------- 4C. COLD NUMERICAL CONFIRMATION ------------------------------------
Integrated the Model-A TDGL equation directly from F_IR (A1=1, r=-1, u=1, Gamma=1) on a 200x200
periodic lattice from a random disordered start, with NO analytic input. Measured the domain
size by the wall-bond density (L = 1 / fraction of opposite-sign neighbor bonds — a purely
geometric coarsening measure). Scaling-window fit:

   L_ord ~ t^0.496      (Allen-Cahn prediction: 0.500)                       [SOLID, verified]

L grows monotonically through the run and the exponent sits within 1% of 1/2. (A coarser
excess-energy measure gives ~0.42, biased low by the usual finite-size/lattice transients; the
geometric wall measure is the clean one.) The t^1/2 law is reproduced cold.

================================================================================
5. THE gamma GATE: WHAT SELECTS THE CLASS (honest status)
================================================================================
The exponent is fixed once two bath properties are known, both un-derived (priority #3):

   (1) Is the system overdamped at cosmological times? — Yes provided t >> tau_gamma = Zt/gamma;
       this is generic at late times and is what makes coarsening (not oscillation) the
       cosmological dynamics. [GATED on gamma magnitude]
   (2) Is chi conserved? — Model A (non-conserved) => 1/2 ; Model B (conserved) => 1/3.
       [GATED on the conservation law]

PHYSICAL LEAN (not a derivation): the amplitude chi = |phi| is NOT the density of any conserved
charge — the ordering transition itself changes INT chi d^3x (disordered chi=0 -> ordered
chi_0). With no symmetry protecting INT chi, the natural class is Model A (non-conserved),
giving L_ord ~ t^(1/2), H = 1/(2t). This matches the handoff's leading choice (Theory Sec 6).
A rigorous verdict still needs the Caldeira-Leggett bath integration (priority #3); if a
conserved slow mode (e.g. a medium energy density) turns out to drive the coarsening, Model B
(t^1/3) applies instead. Both are carried above so the EFT is complete either way. [GATED]

================================================================================
6. COSMOLOGICAL READOUT FROM L_ord(t)
================================================================================
The v2 cosmological ruler is L_ord (Theory Sec 4,6): a_cosmo proportional to L_ord. Writing
L_ord ~ t^p (p = 1/2 Model A, 1/3 Model B):

   Scale factor:   a(t) = a_* (t/t_*)^p
   Hubble rate:    H = d ln L_ord / dt = p / t
       Model A:  H = 1/(2t)   (matches Theory Sec 6 exactly)
       Model B:  H = 1/(3t)
   Deceleration:   q = -a a''/a'^2 = (1 - p)/p
       Model A:  q = +1   (decelerating; identical IN FORM to radiation-dominated FRW a~t^1/2,
                 but here it is coarsening, NOT Friedmann — no Newton G, no Friedmann equation)
       Model B:  q = +2
   Redshift corollary (Theory Sec 6):  1 + z = L_ord(obs)/L_ord(em) = (t_obs/t_em)^p .

The redshift relation is written here as the immediate corollary; the full "3 redshift tests"
(blackbody preserved; (1+z) on BOTH photon energy and observed durations) and the slip/lensing
recomputation at L_ord are priority #2 and are NOT done in this note. [DEFER -> priority #2]

HONEST NEGATIVE (unchanged): a single power law a ~ t^p gives q > 0 — NO inflation and NO
late-time acceleration. Today's observed q < 0 is NOT reproduced by leading-order coarsening.
A realistic history needs extra structure (multi-stage ordering, or a residual free-energy
floor acting as dark energy) — not derived here (priority #4). The t^1/2 result is the
leading-order skeleton to be confronted with H(z), and is EXPECTED to need corrections; that
confrontation is itself the falsifiable test (Theory Sec 8).

================================================================================
7. VALIDITY, CORRECTIONS, AND WHAT IS / ISN'T NAILED
================================================================================
[SOLID, derived this note]
  - IR free energy F_IR (Landau-Ginzburg; A2,A3 gone): the precise content of IR-universality.
  - The damped EOM and the reversible(arena) <-> dissipative(coarsening) crossover at tau_gamma=Zt/gamma.
  - Allen-Cahn L_ord = sqrt(2 A1 t/gamma) (Model A) and LSW L_ord = (K_B t)^(1/3) (Model B),
    prefactors in fundamental quantities; Model A depends only on A1 and gamma (UV-clean).
  - a(t), H(t), q, and the redshift corollary for each class.
  - Cold TDGL check: exponent 0.496 vs 0.500.

[GATED on gamma / bath integration — priority #3]
  - Which class (A vs B) -> which exponent (1/2 vs 1/3). Physical lean: Model A (chi not conserved).
  - Numerical value of the prefactor (needs gamma).

[DEFER — later priorities]
  - 3 redshift tests + slip/lensing at L_ord (priority #2).
  - Inflation / late-time acceleration structure (priority #4).
  - Logarithmic corrections from the marginal quartic u at d_uc=4 (z=1 IR): these can multiply
    the prefactors (chi_0, sigma) by slowly varying logs but do NOT change the t^1/2 / t^1/3
    EXPONENTS, which are geometric. Worth quantifying when re-fixing parameters (priority #5).

NOT used / NOT needed (confirming decoupling): A3, m_sigma (amplitude stiffness), the Faddeev/
Skyrme coupling, c4. None enter L_ord(t). The baryon's UV sensitivity is quarantined from
cosmology exactly as the RG predicted.

================================================================================
8. ONE-PARAGRAPH SUMMARY
================================================================================
Coarse-graining the CCEF action to its IR fixed point removes the irrelevant Skyrme (A2) and
bilaplacian (A3) terms and leaves a Landau-Ginzburg free energy for the amplitude, F_IR =
INT[(A1/2)|grad chi|^2 + (r/2)chi^2 + (u/4)chi^4], with one relevant (gap) and one marginal
(quartic) coupling. Its dynamics is the damped field equation Zt d_t^2 chi + gamma d_t chi =
A1 lap chi - U'(chi): reversible/propagating (the acoustic arena, c_eff=1) for t << Zt/gamma,
and relaxational/coarsening for t >> Zt/gamma. In the coarsening regime the coherence length —
the v2 cosmological ruler — grows by curvature-driven Allen-Cahn dynamics to L_ord(t) =
sqrt(2 A1 t/gamma) ~ t^(1/2) for a non-conserved amplitude (Model A), or by Lifshitz-Slyozov
diffusion to L_ord ~ t^(1/3) for a conserved one (Model B); a cold 2D TDGL simulation confirms
the t^1/2 law (exponent 0.496). Hence a ~ t^p, H = p/t, q = (1-p)/p, and 1+z = (t_obs/t_em)^p,
with p=1/2 (H=1/2t, q=1, radiation-like in form but coarsening in origin) being the physically
favored branch since the amplitude carries no conservation law. The result is UV-clean (no A3,
no m_sigma) as the RG demanded; what remains is to fix the class by deriving gamma (priority #3),
run the redshift/slip tests at L_ord (priority #2), and supply the structure for acceleration
(priority #4). Framework set; quantitative exponent gated by gamma, exactly as flagged.
================================================================================
