================================================================================
CCEF v2 — DERIVATION NOTE: PRIORITY #5 — RE-FIX PARAMETERS FROM COSMOLOGY
                            + CROSS-SECTOR CONSISTENCY TEST
Capstone of the v2 priority list (Sec 9). Derived from the theory; no hand-fitting;
no GR imported; no dark-energy assumption. A-parameters re-derived for V2 unless they
were already fixed in the Theory-Status doc.
Compiled 2026-06-29. Builds on all five prior v2 notes.
Labels: [SOLID] derived/verified | [STRUCT] forced by structure | [FIT] a genuine fit (flagged)
        | [UNIV] follows from IR-universality
================================================================================

--------------------------------------------------------------------------------
0. THE TWO TASKS, AND THE HEADLINE
--------------------------------------------------------------------------------
T1: re-fix the minimal parameter set from cosmology.
T2: does ONE parameter point work for cosmology + particles + Lorentz invariance?

HEADLINE:
  T1. Cosmology is IR-UNIVERSAL (proven, v2 Sec 5): its exponents and the three redshift tests do
      NOT depend on the UV couplings (A2, A3, m_sigma, Skyrme). So cosmology CANNOT re-fix the
      dimensionless minimal parameters -- it pins only ONE overall scale (equivalently the gap
      Lambda, shared with the particle sector). This is not a failure; it is the price/flip-side of
      predictivity. The dimensionless couplings must come from the particle + LI sectors. [UNIV]

  T2. YES -- one parameter point works across all three sectors, and it works by STRUCTURAL
      DECOUPLING, not by a joint fit:
         A1 = Zt = 1           (units axiom; in the Theory-Status doc -- not re-derived)
         A4  -> gap Lambda ~ 231 MeV   (hadronic; set by the particle sector, used by cosmology
                                        as its microscopic ruler -- ONE shared scale)
         A2 ~ 0.327            (Faddeev / emergent-gauge; particle sector)
         A3  -> high-scale Lorentz-invariant regulator (k_UV > 1e6 GeV); the Lifshitz A3 is retired
         c4 ~ 0.028            (tree Skyrme; the SINGLE fitted number -- baryon mass)   [FIT]
      The only dangerous cross-sector tension (v1's baryon-vs-Lorentz, ~9-13 orders in A3) was
      already resolved in v2 by the tree Skyrme c4 + the high-scale LI regulator (Reference Sec 8-9).
      Cosmology adds NO new fit and NO new tension, because it is blind to the UV. Net: the whole
      theory carries exactly ONE fit (c4); cosmology is FIT-FREE. [STRUCT / FIT]

  COSMOLOGICAL CROSS-CHECKS (parameter-free, no tuning):
    * The internal-trigger crossover L* = sigma/DeltaF comes out MICROSCOPIC (~154 fm ~ 180/Lambda),
      ~39 orders below the Hubble radius. So the observable universe crossed L* in its first instants
      and COASTS (a ~ t, q=0) throughout -- the curvature-driven t^1/2 phase was a gap-era transient.
    * Coasting predicts H0 t0 = 1 exactly; observed H0 t0 = 0.988 (H0=70, t0=13.8 Gyr) -- agreement
      to ~1%, with NO dark energy and NO tuning. CCEF inherits the (real) success of coasting here.
    * The horizon in gap units is R_H * Lambda ~ 1.5e41 = the age of the universe in microscopic
      units -- the "hierarchy is just the age," with no second fundamental scale. [SOLID]

================================================================================
1. T1 -- WHAT COSMOLOGY CAN AND CANNOT FIX
================================================================================
The v2 program was to FREE the parameters from v1's proton anchor and re-anchor on cosmology. The
RG result (v2 Sec 5) constrains how far that can go:
  * IR-universal quantities (no UV dependence): the coarsening exponent (1/2 -> 0 across L*), the
    three redshift tests, the decelerate->coast history. These are the SAME for any A2, A3, A4. They
    therefore impose NO constraint on those couplings. [UNIV]
  * Scale-carrying quantities: H0, the age t0, and L* DO carry dimensionful information. But L* is
    microscopic (Sec 3) so the observable history is pure coasting with H0 t0 = 1; this fixes only
    the relation between H0 and the age (one number), degenerate with "how long ordering has run."
CONCLUSION: cosmology fixes ONE overall scale and nothing else. It does NOT re-fix A2, A3, A4 as
dimensionless couplings. The honest v2 statement is: "re-anchor the SCALE on cosmology; take the
dimensionless couplings from particles + LI." The gap Lambda is the single shared scale, and the
particle sector already sets it at the hadronic value. [UNIV]

(Provenance note: A1=Zt=1 are the units axioms present in the Theory-Status doc, so they are kept,
not re-derived. A4, A2, A3 were FREED from v1's proton-anchored numbers; below they are re-fixed
from the particle + LI sectors, with cosmology checked for consistency.)

================================================================================
2. T2 -- THE MINIMAL CROSS-SECTOR PARAMETER POINT
================================================================================
   PARAMETER  VALUE / STATUS              FIXED BY                       SECTOR(S) IT SERVES
   --------   -----------------------     -------------------------      ----------------------
   A1 = Zt    1 (units; c_eff=1)          units axiom (in doc)           all (sets length-energy)
   A4         gap Lambda ~ 231 MeV        particle sector (hadron scale) particles + cosmology(ruler)
   A2         ~0.327                      baryon structure / photon      particles (+ via g, the
                                                                          coasting RATE prefactor)
   A3         high-scale LI regulator     Lorentz invariance bounds      LI / UV (k_UV>1e6 GeV)
              (Lifshitz A3 retired)
   c4         ~0.028   [FIT]              baryon mass E*R=4.06           particles (the one fit)
   --------   -----------------------     -------------------------      ----------------------
Cosmology's role: it consumes A1=Zt=1 (units) and the gap Lambda (as the microscopic ruler for
L_ord); through the CW floor it also depends on A2/g and the amplitude, but only in the SCALE of
L* and the coasting rate -- not in the exponent. It introduces NO new parameter and NO new fit.

CONSISTENCY TEST -- does this ONE point satisfy all three sectors simultaneously?
  COSMOLOGY:   yes -- IR-universal; the exponent/tests hold for this (or any) UV; L* microscopic =>
               coasting; H0 t0 = 1 ~ observed. [SOLID]
  PARTICLES:   yes -- Lambda~231 MeV gives the hadron band; A2~0.327 the Faddeev/photon sector;
               c4~0.028 the nucleon E*R=4.06 (Reference Sec 8, 11). [SOLID; c4 is the fit]
  LORENTZ INV: yes -- with A3 replaced by the high-scale LI (non-local, ghost-free) regulator,
               differential LV = 0 (universality) and the universal LV is pushed to k_UV>1e6 GeV;
               the baryon mass is carried by c4, DECOUPLED from the UV scale (Reference Sec 9). [SOLID]
=> ONE point works. [STRUCT]

WHY IT WORKS (honest mechanism): the three sectors DECOUPLE. The RG proves cosmology is UV-blind,
so it cannot conflict with the particle/LI choices. The historically dangerous conflict was
baryon-vs-LV over A3; v2 removed it by not using A3 for the baryon (tree c4) and by retiring the
Lifshitz term for an LI regulator. With that conflict gone and cosmology decoupled, consistency is
automatic. This is a genuine PASS, but it is "consistency by non-conflict," not a tight joint
determination -- cosmology does not independently TEST the particle numbers (Sec 4). [STRUCT]

================================================================================
3. COSMOLOGICAL CROSS-CHECKS (parameter-free)
================================================================================
Using the single point (Lambda=231 MeV, A2=0.327 -> g^2=1.53, g^4=2.34):
  * Crossover scale (internal-trigger note): L* = sigma/DeltaF ~ (128 pi^2/3 g^4)(1/Lambda)
    = 180/Lambda = 154 fm. Hubble radius c/H0 = 1.3e41 fm. So L*/R_H ~ 1e-39: the universe left the
    curvature-driven t^1/2 regime ~39 orders of expansion ago and has COASTED (a~t, q=0) ever since.
    The cosmological prediction is therefore COASTING throughout the observable era -- derived, not
    chosen. [SOLID]
  * Coasting consistency: a~t => H = 1/t => H0 t0 = 1 exactly. Observed H0 t0 = 0.988 (H0=70 km/s/Mpc,
    t0=13.8 Gyr) -- agreement to ~1%, with no dark energy and nothing tuned. (This is the well-known
    near-coincidence that coasting / R_h=ct models capture; CCEF DERIVES the coasting, so it inherits
    the success honestly.) [SOLID]
  * Hierarchy = age: R_H * Lambda ~ 1.5e41 -- the horizon measured in healing lengths is just the
    age in microscopic units; no second fundamental constant. (NB: the Theory-Status doc's loose
    "~60 orders" is, for a hadronic Lambda, actually ~41 orders -- corrected here.) [SOLID]

These are the only places cosmology touches the parameters, and they are CONSISTENCY CHECKS /
predictions, not fits. A future primordial-GW amplitude from the ordering transition (Reference
Sec 8/10) would be a second, independent cross-check tying cosmology to Lambda. [predict]

================================================================================
4. HONEST STATUS AND THE REMAINING FIT
================================================================================
[SOLID / STRUCT]
  - Cosmology is IR-universal => fixes one overall scale, not the dimensionless couplings (T1).
  - One parameter point (A1=Zt=1; Lambda~231 MeV; A2~0.327; A3->high-scale LI regulator; c4~0.028)
    satisfies cosmology + particles + LI simultaneously (T2). Consistency holds by decoupling.
  - Parameter-free cosmological checks pass: L* microscopic => coasting; H0 t0 = 1 vs 0.988;
    hierarchy = age (R_H*Lambda ~ 1e41).

[FIT -- the single remaining hand-fit in the whole theory]
  - c4 ~ 0.028 (baryon mass). This is the lone fitted number; cosmology adds ZERO further fits.
    Removing it needs the particle-sector "emergent-vector / hidden-local-symmetry (rho) saturation"
    re-derivation (Reference Sec 12 open) -- not a cosmology task.

[HONEST LIMITATIONS]
  - The cross-sector test is passed by NON-CONFLICT (decoupling), not by a tight simultaneous fit:
    cosmology cannot independently test A2/A4/c4 because it is UV-blind. So "one point works" is a
    consistency statement, weaker than a joint over-determination. The genuine joint cross-checks
    are future (primordial GW amplitude; an observed decelerate->coast or L* signature).
  - The coasting prediction (q=0, H(z)=H0(1+z), H0 t0=1) is the firm, parameter-free cosmological
    output. If data robustly require q<0 today beyond coasting, minimal CCEF is falsified -- to be
    met by re-examining foundations, never by tuned additions (consistent with the no-fit discipline).

================================================================================
5. ONE-PARAGRAPH SUMMARY
================================================================================
Priority #5 asks whether the minimal parameters can be re-fixed from cosmology and whether one point
serves all sectors. Because the RG makes cosmology IR-universal, cosmology fixes only ONE overall
scale (the gap Lambda, shared with particles) and cannot pin the dimensionless UV couplings -- the
honest limit of the "re-anchor on cosmology" program. The single cross-sector point is A1=Zt=1
(units), Lambda~231 MeV (hadronic gap, also cosmology's microscopic ruler), A2~0.327 (Faddeev/
photon), A3 replaced by a high-scale Lorentz-invariant regulator, and c4~0.028 (the one fitted
number, baryon mass). This point satisfies cosmology, particles, and Lorentz invariance
simultaneously, and it does so by structural decoupling: the RG proves cosmology is UV-blind, while
the old baryon-vs-LV conflict was already removed by the tree Skyrme c4 plus the LI regulator, so no
tension remains. Parameter-free cosmological cross-checks come out well: the internal-trigger
crossover L*=sigma/DeltaF is microscopic (~154 fm, ~39 orders sub-horizon), so the universe coasts
(a~t, q=0) throughout the observable era; coasting predicts H0 t0 = 1 against an observed 0.988
(~1%), with no dark energy and nothing tuned; and the horizon is just ~1e41 healing lengths, the age
in microscopic units. The whole theory thus carries exactly ONE hand-fit -- c4 in the baryon sector
-- and cosmology is entirely fit-free. The remaining honesty: the cross-sector pass is consistency
by decoupling rather than a tight joint fit, so cosmology does not yet independently over-determine
the particle numbers; the firm, falsifiable cosmological prediction is the coasting history, and the
genuine joint cross-checks (primordial GW amplitude; a decelerate->coast signature) lie in future
data.
================================================================================
