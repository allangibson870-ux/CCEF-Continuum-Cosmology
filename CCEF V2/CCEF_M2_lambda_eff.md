================================================================================
CCEF v2 — DERIVATION NOTE: M2 (Lambda_eff) + M4 (ADIABATIC PERTURBATION ORIGIN)
Items M2 and M4 from the resume. M2 = the 1e122 cosmological-constant gate (Secs 0-7).
M4 = whether the ordering transition seeds the observed adiabatic ~scale-invariant
spectrum, or only excluded causal/defect seeds (Sec 8, added 2026-07-03 per instruction
to fold M4 into this note rather than open a new one).
Discipline: derive from the theory; no hand-fitting; no imported GR; if it fails, it
fails. Both scales used in M2 (M and Lambda) are pinned ELSEWHERE (Newton's constant and
the proton radius) -- there is no cosmological knob to turn, so nothing here is tuned.
Compiled 2026-07-03. Builds on: item M (induced-Einstein background), M1/M1b (the
non-locality scale M fixed by Newton), CCEF_U_chi_acceleration.md (the calculable
interior floor U(chi0) + the no-inflation/ceiling result), CCEF_perturbations_growth.md
(the field content's cosmological roles), CCEF_dichotomy.md (the coherence-patch /
eternal-medium ontology that DEFINES the reference zero).
Labels: [SOLID] derived/verified | [STRUCT] forced by structure | [NEG] honest negative
        | [DEFER] needs further structure
================================================================================

--------------------------------------------------------------------------------
0. THE QUESTION AND THE HEADLINE
--------------------------------------------------------------------------------
Item M exposed Lambda_eff as a load-bearing open: the induced-Einstein background
(G_munu = 8piG <T_munu>) gravitates the vacuum zero-point energy, and with the
non-locality scale M now pinned to Newton strength (M1/M1b: M = M_Pl*sqrt(6pi/N_eff)
~ 1.8e19 GeV), the Sakharov-induced vacuum term is QUADRATICALLY sensitive:
    a0 ~ N M^4 / 32pi^2 ~ 2.8e75 GeV^4   vs   rho_Lambda,obs = 2.5e-47 GeV^4,
a mismatch of 1.1e122 -- the full, standard cosmological-constant problem, now
unavoidable in CCEF. The resume flagged ONE in-theory subtraction candidate before
conceding a renormalized Lambda_eff: the PHASE-RELATIVE ZERO -- measure the vacuum
energy of the ordered observable patch RELATIVE TO the eternal disordered medium that
surrounds it (the N-note ontology: we live in a finite ordered coherence region inside
an infinite, mostly-disordered continuum; that medium, not an absolute zero, is the
physical reference state).

HEADLINE:
  THE SUBTRACTION IS REAL BUT INSUFFICIENT. It is not a trick and it is not tuned: the
  eternal medium is a genuine reference state of the same continuum, with the same UV
  completion (same M, same field content). The leading, phase-INDEPENDENT bulk piece
  (the M^4 term) therefore cancels EXACTLY in patch-minus-medium, by conservation of
  the total number of degrees of freedom across the ordering transition (Anderson-Higgs
  reshuffles the spectrum but conserves dof). This removes EXACTLY 40 orders of
  magnitude -- the calculable factor (Lambda/M)^2 = 1.7e-40, the same ratio that
  inverts item M's G_ind/G_N = 1.6e40. But it is 40, not 122. The survivor is the
  phase-DEPENDENT zero-point term ~ N M^2 Lambda^2 / 32pi^2 ~ 4.7e35 GeV^4, still 82
  orders too large. Even the deepest-IR condensation floor U(chi0) ~ -1.8e-7 GeV^4 is
  40 orders too large AND the wrong sign. No further in-theory subtraction exists.
  VERDICT: the 1e122 gate is NOT passed. Lambda_eff must be conceded as a renormalized
  input -- the second such constant in the cosmology sector, joining G_N. This is a
  concession, NOT a fit: M and Lambda are already fixed by Newton's constant and the
  proton radius, so Lambda_eff is not adjusted to match data; it is acknowledged as
  not predicted. [SOLID / NEG]

--------------------------------------------------------------------------------
1. THE NAIVE INDUCED VACUUM ENERGY (the gate)
--------------------------------------------------------------------------------
The same one-loop / heat-kernel induction that gives the Einstein term also generates a
cosmological-constant term. In the ghost-free non-local completion adopted in M1 (entire
form factor e^{p^2/M^2}, proper-time shift s -> s + 1/M^2), Sakharov's original QUADRATIC
scaling is restored, and the vacuum-energy (a0) coefficient is the quartic partner of the
a1 = R/6 Einstein coefficient:
    a0 = (N_eff / 32pi^2) [ c1 M^4 + c2 M^2 m^2 + c3 m^4 ln(M^2/m^2) + ... ] ,   c_i = O(1).
The leading term is the pure UV bulk:
    a0(naive) ~ N M^4 / 32pi^2 .
Numbers (N_eff = 9; M = M_Pl sqrt(6pi/9) = 1.77e19 GeV):
    a0(naive) = 2.78e75 GeV^4 = 0.12 M_Pl^4 ,
    a0 / rho_obs = 1.1e122 .                                                    [SOLID]
This is exactly the standard CC problem: a Planckian vacuum energy, 122 orders above the
observed 2.5e-47 GeV^4. It is now UNAVOIDABLE in CCEF precisely because M1 pinned M to
Newton strength (with the old "M*^2 ~ log(k_UV)" artifact, a0 was only log-sensitive and
one could pretend; the quadratic sensitivity that fixes G also fixes this).

--------------------------------------------------------------------------------
2. THE PATCH-MINUS-MEDIUM ZERO (the only in-theory subtraction)
--------------------------------------------------------------------------------
Ontology (CCEF_dichotomy.md, N-note): the observable universe is a finite ordered
coherence patch (amplitude chi = chi_0, easy-axis vacuum, gap Lambda) embedded in an
ETERNAL, mostly-disordered medium (chi -> 0 on average, no Anderson-Higgs). What can
gravitate INSIDE the patch, via the induced Einstein equation, is the vacuum stress of
the patch measured against the surrounding medium -- the medium's own vacuum energy is a
property of the shared continuum ground state, not a source that curves the patch's
emergent metric. So the physically correct object is
    rho_vac(eff) = rho_vac(ordered patch) - rho_vac(eternal medium) .           [STRUCT]

Both phases are states of the SAME continuum with the SAME non-local completion: same M,
same N_eff. Write each phase's induced vacuum energy in the a0 expansion above. Two facts
decide the subtraction:

  (a) dof CONSERVATION across the ordering transition. The ordered patch has a massive
      emergent gauge boson (3 polarizations, Anderson-Higgsed), a radial mode, and
      Goldstones; the disordered medium has the massless gauge (2 pol) plus the would-be
      Goldstone as an amplitude direction. The Higgs mechanism RESHUFFLES the spectrum
      but conserves the total number of modes N_eff. Hence the c1 M^4 coefficient -- which
      counts dof and nothing else -- is IDENTICAL in both phases and CANCELS EXACTLY in
      the difference.                                                            [SOLID]

  (b) The surviving leading term is phase-DEPENDENT through the mode MASSES. The ordered
      patch carries the gap Lambda = sqrt(A4) = 231 MeV (and m_gamma = g chi_0, etc.); the
      disordered medium does not. The mass spectra differ by O(Lambda^2). The c2 M^2 m^2
      term therefore does NOT cancel:
          Delta a0 = rho_vac(patch) - rho_vac(medium)
                   ~ (N_eff / 32pi^2) c2 M^2 (Lambda^2 - 0) ~ N_eff M^2 Lambda^2 / 32pi^2 .

This is a genuine, calculable, TUNING-FREE subtraction. Its size is fixed:
    Delta a0 ~ N M^2 Lambda^2 / 32pi^2 = 4.7e35 GeV^4
             = a0(naive) x (Lambda/M)^2 ,   (Lambda/M)^2 = 1.7e-40 .            [SOLID]

The medium reference buys EXACTLY the factor (Lambda/M)^2 = 1.7e-40 -- 40 orders of
magnitude, and not by coincidence: this is the same hierarchy (Lambda/M)^2 that in M1
inverted G_ind/G_N = 1.6e40. The continuum's two scales (stiffness/gap Lambda, non-
locality M) set BOTH the gravitational coupling and the depth of this subtraction.

--------------------------------------------------------------------------------
3. IT IS NOT ENOUGH -- BY 82 ORDERS
--------------------------------------------------------------------------------
    a0(naive)          2.78e75 GeV^4    ->  122 orders above observed
    after subtraction  4.75e35 GeV^4    ->   82 orders above observed  (removed 40)
    observed rho_Lambda 2.5e-47 GeV^4

The patch-minus-medium zero cancels the Planckian M^4 bulk but leaves the phase-dependent
M^2 Lambda^2 zero-point energy, still ~1.9e82 times the observed value. The 40 orders it
removes are real and free; the 82 that remain are fatal. [SOLID / NEG]

Why one cannot subtract further, in-theory:
  * The M^2 Lambda^2 term is GENUINELY phase-dependent -- it exists in the patch and not in
    the medium, so it is part of the real rho_vac DIFFERENCE and genuinely gravitates in
    the induced-Einstein equation. There is no reference state relative to which it
    vanishes without also erasing the gap Lambda that defines the ordered phase (and the
    proton).                                                                     [STRUCT]
  * No boson-fermion cancellation: CCEF has fermions (pi_4(S^3)=Z_2 statistics) but NO
    supersymmetry, so there is no systematic cancellation of zero-point energies.  [SOLID]
  * The deepest-IR object -- the calculable condensation floor from the Coleman-Weinberg
    potential (CCEF_U_chi_acceleration.md), U(chi0) = -(3g^4/128pi^2) chi_0^4 = -8.1e-4
    CCEF^4 = -1.82e-7 GeV^4 -- is what WOULD remain if the M^2 Lambda^2 term also somehow
    cancelled. It does not; but even that best case is |U(chi0)|/rho_obs = 7.3e39 (40
    orders too large) and NEGATIVE (an AdS-like vacuum, the wrong sign for the observed
    accelerating vacuum). So the deepest reachable floor is itself dead.         [SOLID / NEG]

--------------------------------------------------------------------------------
4. VERDICT AND CONSEQUENCE
--------------------------------------------------------------------------------
THE 1e122 GATE IS NOT PASSED. The phase-relative zero is the correct physical prescription
and it does real, non-tuned work (a clean 40 orders, = (Lambda/M)^2), but it falls 82
orders short. Lambda_eff is therefore conceded as a RENORMALIZED INPUT -- the cosmology
sector now carries two such constants:
    G_N       (renormalized input #1; the bare/UV Einstein term, per M1's Sakharov logic)
    Lambda_eff (renormalized input #2; the vacuum-energy counterterm, this note)
(plus the matter-sector tree coupling c4 ~ 0.028, Reference Sec 8.4). This is the SAME
status the cosmological constant has in every known QFT-plus-gravity framework: not solved,
absorbed. CCEF neither solves nor worsens the CC problem; the patch-minus-medium ontology
sharpens WHY (dof conservation removes the M^4, the gap survives at M^2 Lambda^2) but does
not close it.

NO TUNING WAS DONE (per the standing instruction, advised explicitly): Lambda_eff is not
fit to reproduce q_0 ~ -0.5 or rho_obs. M is fixed by Newton's constant (M1), Lambda by the
proton radius (Reference Sec 4); with both pinned, the residual 4.7e35 GeV^4 is a PREDICTION
of the failure, not an adjustable output. Conceding Lambda_eff = renormalized input is the
honest label, not a hand-fit. What this costs CCEF specifically: the observed dark-energy
scale and the observed sign (de Sitter, not AdS) are inputs, not consequences.

--------------------------------------------------------------------------------
5. UPDATED COSMOLOGY-SECTOR SCORECARD (item M branch, N-gains folded in)
--------------------------------------------------------------------------------
  Background phenomenology = LCDM (works, BY CONSTRUCTION -- the G-note LCDM control,
     chi2/dof = 0.87, IS this model).                                            [SOLID]
  Renormalized inputs:   G_N (M1) ; Lambda_eff (M2, THIS NOTE -- gate not passed).
  Structural opens remaining, load-bearing:
     M3  Z2 walls        -- DISSOLVED by the coherence-patch picture (N-gain).    [DONE]
     M1c gap hierarchy   -- does the ghost-free non-local completion protect
                            delta A4 ~ N M^2/16pi^2 (tuning ~3e-39)? [OPEN]
     M4  perturbations   -- FAILS make-or-break (Sec 8, THIS NOTE): the transition
                            gives causal/defect seeds (blue k^4, incoherent, iso-
                            curvature), ~26 orders too little large-scale power vs the
                            observed adiabatic n_s~0.965; no CCEF inflation to fix it.
                            Requires importing a foreign inflation sector. [NEG]
  CCEF-specific falsifiables (unaffected): soliton DM ratio (~5), transition GW
     background (item C), any deviation from GR growth (none expected).

--------------------------------------------------------------------------------
6. NEXT (M2 closed as a concession; M4 closed as a make-or-break failure, Sec 8)
--------------------------------------------------------------------------------
  DECISION POINT (advise before proceeding): with M4 failing, the minimal single-order-
      parameter program cannot originate cosmological structure. The remaining lines are
      no longer "finish CCEF cosmology" but "characterise what's left":
  M1c The scalar/gap hierarchy under the non-local completion (compute, do not assert) --
      the last purely-internal consistency check of the gravity spine.
  C   Primordial-GW amplitude from the ordering transition -- a genuine CCEF-specific
      falsifiable that does NOT depend on the (failed) adiabatic-seed question.
  B   gamma_0 O(1) prefactor;  D  re-derive c4 (parameter-free baryon mass).
  (An inflation sector to rescue M4 would be extra structure foreign to the one-field
   ethos; flag explicitly rather than bolt it on silently.)

--------------------------------------------------------------------------------
7. NUMBERS (reproducible; see m2_check.py)
--------------------------------------------------------------------------------
  E0 = 122.5 MeV/CCEF ;  1 CCEF^4 = 2.252e-4 GeV^4 ;  Lambda = 231 MeV ;
  M_Pl = 1.221e19 GeV ;  N_eff = 9 -> M = 1.77e19 GeV = 1.45 M_Pl ;
  rho_Lambda,obs = 2.5e-47 GeV^4.
  a0(naive)          = N M^4/32pi^2      = 2.78e75 GeV^4   (ratio 1.1e122)
  (Lambda/M)^2       = 1.71e-40          (subtraction gain; inverts G_ind/G_N=1.6e40)
  Delta a0 (residual)= N M^2 Lambda^2/32pi^2 = 4.75e35 GeV^4 (ratio 1.9e82)
  U(chi0) floor      = -8.1e-4 CCEF^4    = -1.82e-7 GeV^4  (ratio 7.3e39, NEGATIVE)
  Orders removed by patch-minus-medium: 40.  Orders remaining: 82.
  [M4] T_c = 140 MeV, t~3e-5 s ;  a_trans/a_rec ~ T_rec/T_c ~ 1.9e-9 ;
       observed CMB modes super-horizon at T_c by ~5e8 ;  causal P(k)~k^4 vs HZ k^1
       => large-scale power deficit ~6e-27 (~26 orders);  n_s,obs = 0.965.

================================================================================
8. ADDENDUM — M4: DOES THE ORDERING TRANSITION SEED ADIABATIC ~SCALE-INVARIANT
   PERTURBATIONS?  (added 2026-07-03; make-or-break for structure formation)
================================================================================

8.0 QUESTION AND HEADLINE
--------------------------------------------------------------------------------
The induced-Einstein background (item M) is LCDM by construction, but LCDM's acoustic
peaks and matter power spectrum ASSUME a primordial spectrum of curvature perturbations
that is (i) ADIABATIC, (ii) nearly SCALE-INVARIANT (Planck 2018 n_s = 0.9649 +- 0.0042),
(iii) COHERENT (laid down once, super-horizon, giving sharp acoustic peaks), and
(iv) GAUSSIAN, amplitude A_s ~ 2.1e-9 (curvature ~1e-5). M4 asks whether CCEF's ordering
transition SUPPLIES that spectrum, or only the defect/coarsening seeds the resume flagged
as "excluded by Planck (<few %)."

  HEADLINE: IT FAILS, on three INDEPENDENT counts, and the failure is structural, not a
  tuning miss. The transition generates CAUSAL seeds (Kibble defects + Model-A coarsening
  of the order parameter), which are forced by causality to a BLUE, ISOCURVATURE,
  INCOHERENT spectrum -- ~26 orders too little power on the largest observed scales, the
  wrong perturbation type, and unable to make coherent acoustic peaks. And CCEF's own
  dynamics forbid the inflationary epoch that would fix this: the ceiling theorem + the
  U_chi result give NO de Sitter from vacuum free energy, and M2 shows the vacuum energy
  is either Planckian-positive (uncontrolled) or negative (AdS) -- no slow-roll inflaton.
  The coherence-patch picture (N-note) solves background UNIFORMITY but by the same token
  makes the patch smooth; it does not, and cannot, generate the structured scale-invariant
  spectrum. Matching observations therefore requires IMPORTING an inflation sector foreign
  to CCEF's single-order-parameter program -- and CCEF's natural realization of that sector
  (the transition itself) is the excluded one. [SOLID / NEG -- make-or-break BREAKS]

8.1 WHAT THE TRANSITION ACTUALLY PRODUCES
--------------------------------------------------------------------------------
From CCEF_perturbations_growth.md the field content's cosmological roles are fixed: the
amplitude mode is gap-stiff (relaxes on ~gamma_0/m_sigma^2, tracks equilibrium, does NOT
seed), the Goldstones dilute as a^-4, and the clustering matter is the pressureless
soliton/defect fluid. So the ONLY primordial inhomogeneity the transition can imprint is
in the soliton/defect distribution laid down by the Kibble mechanism at T_c ~ 140 MeV
(t ~ 3e-5 s), plus the coarsening fluctuations of the order parameter as domains grow
(Model-A, one length xi(t) ~ t^1/2). Both are generated CAUSALLY -- no correlations exist
beyond the horizon at the time of generation. [SOLID]

8.2 OBSTRUCTION 1 -- CAUSALITY FORCES A BLUE SPECTRUM (the quantitative kill)
--------------------------------------------------------------------------------
Any perturbation sourced causally after the transition obeys the Traschen integral
constraints (local stress-energy conservation + causality): on comoving scales larger
than the horizon at generation, the induced density power spectrum is pinned to the
Zel'dovich/causal tail P_delta(k) -> k^4 as k -> 0. Scale-invariant adiabatic (Harrison-
Zel'dovich) is P_delta(k) ~ k^{n_s} ~ k^1. The two differ by k^3 on large scales. [SOLID]
  Quantify: in radiation domination the comoving Hubble radius grows as chi_h ~ a, so
  every observed CMB mode was OUTSIDE the horizon at T_c by
     k(horizon at T_c)/k(largest observed) ~ a_rec/a_trans ~ T_c/T_rec ~ 5e8 .
  Normalizing the causal and HZ spectra at the transition horizon, the causal seed delivers
     (k_large/k_horizon)^{4-1} ~ (1/5e8)^3 ~ 6e-27
  i.e. ~26 ORDERS too little power on the largest observed scales. Order-of-magnitude
  slop in the horizon estimate leaves it 20-30 orders off: robustly excluded. This is the
  same reason cosmic-defect models were ruled out by the CMB. [SOLID / NEG]

8.3 OBSTRUCTION 2 -- INCOHERENCE ERASES THE ACOUSTIC PEAKS
--------------------------------------------------------------------------------
Active/causal sources (defects, ongoing coarsening) source perturbations CONTINUOUSLY and
stochastically across the whole history, with random phases. Coherent acoustic peaks (which
Planck resolves sharply out to l ~ 2500) require the perturbations to be laid down ONCE,
super-horizon, with a fixed temporal phase, so all Fourier modes of a given k oscillate in
step. A continuously-sourced coarsening field cannot do this -- it gives smeared, low-
contrast features, not the observed peak series. (This is independent of 8.2 and mirrors
the item-F finding of no coherent peak structure, here from the SOURCE side rather than the
background.) [SOLID / NEG]

8.4 OBSTRUCTION 3 -- WRONG TYPE, AND NO INFLATION TO CONVERT IT
--------------------------------------------------------------------------------
Kibble/coarsening seeds are ISOCURVATURE (perturbations in the soliton/defect component
relative to radiation), whereas Planck constrains the primordial modes to be >99% ADIABATIC.
The only known way to obtain super-horizon ADIABATIC, scale-invariant, coherent modes is an
epoch with aH INCREASING (comoving horizon shrinking) -- i.e. accelerated expansion (p>1)
before the relevant scales exit. CCEF forbids exactly this:
  * The ceiling theorem (CCEF_internal_trigger.md) caps front-driven expansion at p <= 1
    (q >= 0): no acceleration from local coarsening dynamics. [THM]
  * In the induced-Einstein mode, inflation would need a positive vacuum energy -- but M2
    (Secs 1-4) shows the vacuum energy is either ~M^2 Lambda^2 ~ 5e35 GeV^4 (Planckian:
    would drive uncontrolled sub-Planck-time inflation with no graceful exit and the wrong
    amplitude) or the IR floor U(chi0) < 0 (AdS: no inflation at all). No slow-roll inflaton
    potential is derived, and the U_chi result already showed a vacuum floor COASTS, not
    inflates, in CCEF. [SOLID]
  * Timing: the transition is at T_c ~ 140 MeV (5 decades pre-BBN), far too late and too
    low-scale to push the ~Gpc CMB scales outside the horizon -- that needs ~60 e-folds at
    a high scale, which the second-order/weak 140-MeV transition does not provide. [SOLID]
So there is no CCEF mechanism to convert the causal isocurvature seeds into adiabatic
scale-invariant ones. [SOLID / NEG]

8.5 THE COHERENCE-PATCH CAVEAT (why the N-gain does NOT rescue M4)
--------------------------------------------------------------------------------
The N-note dissolves the horizon/uniformity problem by construction: inside one coherence
patch the order parameter is aligned, so the mean is smooth without needing inflation. But
uniformity of the MEAN is not the same as -- and pulls OPPOSITE to -- generating the
correct PERTURBATION spectrum. A patch that is smooth by construction has essentially no
adiabatic (curvature) power except what the transition fluctuations add, and those are
exactly the causal seeds killed in 8.2-8.4. One could ask whether the eternal pre-transition
continuum imprints super-horizon scale-invariant correlations; it cannot, because an
equilibrium medium has correlations that decay exponentially beyond ~1/Lambda -- short-
range, the opposite of scale-invariant. [SOLID / NEG]

8.6 VERDICT
--------------------------------------------------------------------------------
M4 is a make-or-break, and it BREAKS. CCEF's ordering transition produces causal, blue,
incoherent, isocurvature seeds -- excluded by Planck by ~26 orders in large-scale power and
by the very existence of coherent acoustic peaks -- and CCEF's own dynamics (ceiling theorem;
wrong-sign/Planckian vacuum from M2; no slow-roll inflaton; too-late 140-MeV transition)
forbid the inflationary epoch that would fix it. The induced-Einstein background "passes F+G
BY CONSTRUCTION," but it cannot originate the primordial spectrum that F+G's own LCDM control
assumes. Consequence: the minimal single-order-parameter cosmology cannot form structure from
first principles; recovering the observed universe requires bolting on an inflation sector
that is foreign to the one-field ethos AND whose natural CCEF realization (the transition) is
the excluded one.
  NO TUNING WAS AVAILABLE OR USED: the failure is fixed by causality plus scales pinned
  elsewhere (T_c, the RD horizon growth); there is no knob. Advising, per instruction: this
  closes the cosmology sector's constructive program. What survives is the particle/gravity
  spine (massless healthy graviton, slip null, induced Einstein at Newton strength from M1)
  plus CCEF-specific falsifiables that do NOT depend on seed origin -- the soliton DM ratio
  and the transition GW background (item C) -- which is where the remaining value lies.

================================================================================
Working principle: the theory speaks for itself, right or wrong. M2 -- the phase-relative
zero was the last in-theory shot at the CC; it lands 40 of the needed 122 orders and stops,
so Lambda_eff joins G_N as a renormalized input. M4 -- the ordering transition seeds only
causal (defect/coarsening) perturbations, excluded by ~26 orders and by peak coherence, and
CCEF forbids the inflation that would fix it. Two honest negatives; nothing was fit. End of
M2+M4 note.
================================================================================
