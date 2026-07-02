================================================================================
CCEF v2 — DERIVATION NOTE: REDSHIFT TESTS AND SLIP/LENSING AT L_ord
Priority #2 from the v2 handoff (Sec 9). Derived from the theory; no hand-fitting.
Compiled 2026-06-29. Builds on CCEF_Lord_IR_EFT_derivation.md and
CCEF_gamma_CaldeiraLeggett_derivation.md.
Labels: [SOLID] derived/verified | [STRUCT] forced by structure | [NEG] honest negative
        | [DEFER] needs a further sub-calculation
================================================================================

--------------------------------------------------------------------------------
0. OBJECTIVE AND HEADLINE
--------------------------------------------------------------------------------
GOAL (the "make-or-break"): recompute redshift in the IR effective theory at the coherence
length L_ord, run the 3 redshift tests, and recompute gravitational slip eta and lensing Sigma
at L_ord (the v1 sign-change at k=Lambda was the wrong scale).

HEADLINE RESULTS:
  REDSHIFT -- PASSES all three tests. The coarsening expansion is a GENUINE METRIC redshift
  (not tired light), because CCEF has one universal emergent metric on which all massless modes
  and all clocks propagate with the same c_eff (Reference Sec 9, Delta c/c = 0):
     (1) photon energy:  E_obs/E_em = 1/(1+z)                                   [SOLID, PASS]
     (2) durations:      dt_obs/dt_em = (1+z)                                   [SOLID, PASS]
     (3) blackbody:      Planck -> Planck at T_obs = T_em/(1+z)                 [SOLID, PASS]
  with  1+z = L_ord(obs)/L_ord(em) = (t_obs/t_em)^(1/2).  Derived consequences:
     H(z) = H0 (1+z)^2 ,  D_C = (1/H0) z/(1+z) ,  D_L = z/H0 ,  D_A = (1/H0) z/(1+z)^2 .
  HONEST NEGATIVE: H(z)=H0(1+z)^2 is radiation-like and OVERSHOOTS LCDM by 1.7-3x at z=0.5-2 --
  the single-stage coarsening law has no matter/dark-energy era. Expected; needs priority #4. [NEG]

  SLIP / LENSING -- the v1 falsifiable sign-change does NOT survive at cosmological scales.
  The v1 eta(k)=(A4-A1k^2-A3k^4)/(A1k^2+A3k^4), sign change at k=Lambda, is a GAP-SCALE
  (soliton-environment) quantity; evaluated at cosmological k<<Lambda it gives the absurd
  eta ~ (Lambda/k)^2 ~ 10^76 -- a clear mis-scaling, exactly as the handoff warned. The correct
  IR statement: CCEF's induced gravity is Sakharov-induced EINSTEIN gravity (massless, healthy,
  z=1 graviton, Reference Sec 6), so at observable sub-horizon scales
     eta_cosmo ~ 1 ,  Sigma_cosmo ~ 1   (GR-like),                              [STRUCT]
  with static corrections of order (k/Lambda)^2 ~ 10^-120 (utterly negligible). The ONLY place a
  cosmological-scale departure can live is horizon-scale anisotropic stress of the coarsening
  field; its O(1) coefficient needs the full perturbed IR EFT (deferred). [DEFER]
  NET: there is currently NO validated cosmological modified-gravity slip signal. The falsifiable
  handle is the EXPANSION HISTORY H(z) (and the growth it drives), not slip. This removes a
  spurious v1 prediction -- an honest correction, not a new detection.

================================================================================
1. SETUP: THE METRIC AND THE REDSHIFT DEFINITION
================================================================================
From the prior notes: the emergent acoustic metric (Reference Sec 3, multiple routes) is
   ds^2 = -dt^2 + a^2(t) dx^2 ,   c_eff = sqrt(A1/Zt) = 1 ,
and the cosmological ruler is the coherence length with the DERIVED (Model A) coarsening law
   a(t) proportional to L_ord(t) = sqrt( (2 A1/gamma_0) t )  ~  t^(1/2) ,   H = a'/a = 1/(2t).
Redshift is defined kinematically by the ratio of scale factors between emission and observation:
   1 + z  ==  a(t_obs)/a(t_em)  =  L_ord(obs)/L_ord(em)  =  (t_obs/t_em)^(1/2) .       [def]

The decisive theoretical input for ALL three tests: UNIVERSALITY. A single order parameter gives
ONE emergent metric shared by the graviton and every matter/Goldstone/photon mode, with exactly
equal speeds (Reference Sec 9: Delta c/c = 0, so GW170817 etc. are auto-satisfied). Therefore
the redshift is (a) achromatic (same factor for all frequencies) and (b) identical for light and
for clocks. That is precisely what separates a genuine metric expansion from tired light.

================================================================================
2. THE THREE REDSHIFT TESTS
================================================================================
2.1 PHOTON ENERGY redshifts as 1/(1+z).  [SOLID, PASS]
A massless IR mode (z=1, omega = c_eff k, k<<k_UV) propagates on the metric with conserved
COMOVING wavevector. The physical wavelength stretches as lambda_phys = a(t) lambda_comoving, so
   lambda_obs/lambda_em = a_obs/a_em = 1+z   =>   E_obs/E_em = lambda_em/lambda_obs = 1/(1+z).
This reproduces the handoff's "1+z = L_ord ratio" AND attaches it to the photon energy. PASS.

2.2 DURATIONS / TIME INTERVALS dilate as (1+z).  [SOLID, PASS]
Two wavefronts (or pulses) emitted a proper interval dt_em apart travel the SAME comoving null
path INT dt/a(t) = const. Differentiating the null condition gives dt_obs/a_obs = dt_em/a_em, so
   dt_obs/dt_em = a_obs/a_em = 1+z.
Light-curve / line-width / variability timescales stretch by (1+z) -- the standard FRW time
dilation, here following purely from the emergent metric. PASS. (Because clocks = massive
solitons follow timelike geodesics of the SAME metric with the SAME c_eff, the dilation is
universal, not a photon-only artifact.)

2.3 BLACKBODY is PRESERVED: Planck -> Planck at T_obs = T_em/(1+z).  [SOLID, PASS]
Three ingredients, all supplied by the metric + universality:
  (i)  achromaticity: every mode redshifts by the SAME factor k -> k/a (z=1, linear dispersion
       across the cosmological band, since k<<k_UV) -- so the spectrum is rescaled, not distorted;
  (ii) phase-space (Liouville) conservation along geodesics: occupation per mode is conserved;
  (iii) photon-number conservation (no absorption by the transparent ordered medium).
Then the Planck occupation n(nu) = 1/(exp(h nu/kT)-1) maps under nu -> nu/(1+z) to
   n(nu/(1+z)) = 1/(exp(h nu/(k T)) - 1) = 1/(exp(h nu' /k(T/(1+z))) - 1),
i.e. exactly a Planck spectrum at T_obs = T_em/(1+z). VERIFIED numerically: the occupation
identity n(nu;T) = n(nu/(1+z); T/(1+z)) holds to machine precision. PASS.
  Falsifiable corollary (NOT a failure): only photons with k approaching k_UV (~240 MeV) would
  redshift chromatically (z=2 Lifshitz) and distort -- utterly negligible for the CMB, but a
  matter-of-principle spectral-distortion prediction at ultra-high frequencies.

BONUS (Tolman surface-brightness test): genuine metric expansion dims surface brightness as
(1+z)^-4 (vs (1+z)^-1 for tired light). CCEF, being a true metric redshift, predicts the (1+z)^-4
Tolman law -- a further falsifiable distinguishing test it passes by construction. [SOLID]

WHY THIS MATTERS: tired-light / fake-redshift models generically FAIL 2.2 (no time dilation) and
2.3 (blackbody distortion). CCEF passes all three because the redshift is a real metric effect on
a universal emergent metric. This is the make-or-break, and it is made. [SOLID]

================================================================================
3. DERIVED OBSERVABLES (H(z), DISTANCES) AND THE HONEST H(z) TENSION
================================================================================
With a ~ t^(1/2): t = t_obs/(1+z)^2, H = 1/(2t), hence
   H(z) = H0 (1+z)^2 ,   H0 = 1/(2 t_obs).                                       [SOLID]
This is identical IN FORM to a radiation-dominated FRW rate (H ~ a^-2), but here it is coarsening,
not Friedmann. Distances (flat, c=1), verified numerically:
   D_C(z) = INT_0^z dz'/H(z') = (1/H0) z/(1+z)
   D_L(z) = (1+z) D_C = z/H0           (exactly linear in z)
   D_A(z) = D_C/(1+z) = (1/H0) z/(1+z)^2
Checks (H0=1): D_C(1)=0.5, D_L(1)=1.0=z/H0, D_A(1)=0.25, D_C(1100)=0.99909 -- all match the
closed forms to machine precision.

HONEST NEGATIVE [NEG]: H(z)=H0(1+z)^2 overshoots a standard LCDM rate badly --
   z=0.5: 2.25 H0 vs 1.31 H0 (1.7x) ;  z=1: 4.0 vs 1.76 (2.3x) ;  z=2: 9.0 vs 2.97 (3.0x).
The single-stage coarsening law is a decelerating (q=+1) radiation-like skeleton with NO matter
era and NO acceleration. The Hubble diagram D_L = z/H0 likewise has no late-time acceleration.
This is the EXPECTED shortfall (handoff Sec 7/8): a realistic history needs extra structure
(multi-stage ordering, or a residual free-energy floor as dark energy) -- priority #4, not done
here. What this note establishes is that the redshift KINEMATICS are sound; the dynamical
HISTORY is incomplete.

================================================================================
4. SLIP AND LENSING AT L_ord
================================================================================
4.1 WHY THE v1 FORMULA IS THE WRONG SCALE.  [STRUCT]
V1 gave eta(k) = (A4 - A1 k^2 - A3 k^4)/(A1 k^2 + A3 k^4), i.e. eta+1 = A4/(A1k^2+A3k^4), with a
sign change at k* = sqrt(A4/A1) = Lambda (V1 doc Sec 9; Reference Sec 5). This was derived from
the GAPPED vacuum/soliton fluctuation spectrum (omega^2 = A4 + A1k^2 + A3k^4); in V1 it described
the environment of a soliton AT GAP-SCALE wavenumbers (hence "eta(k_sol) = -0.512, solitons in
the eta<0 sector"). Evaluated at a cosmological wavenumber k ~ 1/L_ord << Lambda it gives
   eta + 1 = A4/(A1 k^2) = (Lambda/k)^2 ~ (Lambda L_ord)^2 ~ 10^76 ,
a nonsensical "slip." The gap A4 is a microscopic (Scale-1) restoring term; it is NOT the
restoring term for Scale-2 cosmological perturbations. The formula simply does not apply at L_ord.

4.2 THE CORRECT IR STATEMENT: INDUCED EINSTEIN GRAVITY => eta ~ Sigma ~ 1.  [STRUCT]
In the IR (k<<k_UV, k<<Lambda) the order-parameter dynamics flows to the Gaussian/mean-field,
relativistic z=1 fixed point (Reference Sec 5,6). The composite graviton there is massless,
healthy (induced 1/16piG > 0, Sakharov), and Lorentz-invariant -- i.e. the emergent gravity IS
induced Einstein gravity. Einstein gravity sourced by ordinary (non-anisotropic) IR matter gives
NO slip: Phi = Psi, eta = 1, and the lensing/Weyl modification Sigma = 1. So the DEFAULT, leading
cosmological prediction is GR-like:
   eta_cosmo(k) = 1 + O((k/Lambda)^2) ,   Sigma_cosmo(k) = 1 + O((k/Lambda)^2) .
The leading irrelevant-operator correction is (k/Lambda)^2 ~ (1/(Lambda L_ord))^2 ~ 10^-120 at
cosmological k -- unobservable. The v1 sign-change at k=Lambda lives ~38 orders of magnitude above
any lensing wavenumber and never enters the observable window. [STRUCT]

4.3 THE ONLY POSSIBLE COSMOLOGICAL-SCALE SIGNAL: horizon-scale anisotropic stress.  [DEFER]
A real (small) departure from eta=1 can come only from the coarsening field's OWN perturbations
acting as a clustering component with anisotropic stress, which is appreciable only near the
horizon k ~ H ~ 1/L_ord and decays on sub-horizon scales. Schematically eta - 1 ~ c_Pi (H/k)^2
with c_Pi an O(1) number set by the linearized IR EFT (the perturbed F_IR + the gamma_0
relaxational dynamics on the FRW background). Computing c_Pi requires the full perturbed IR EFT --
the linear cosmological perturbation equations of the coarsening field -- which is a further
sub-calculation NOT done here. Until then there is no quantitative cosmological slip prediction.
[DEFER -> a clean next sub-task]

4.4 CONSEQUENCE.  [NEG, honest]
The v1 "falsifiable slip sign-change at k* (and Sigma=0.537 suppression)" does NOT carry to
cosmological scales -- it was a gap-scale artifact. At observable scales CCEF is, to overwhelming
precision, GR-like in slip and lensing (eta=Sigma=1). Therefore the genuine, falsifiable
cosmological signature of CCEF is NOT modified-gravity slip but the modified EXPANSION HISTORY
H(z)=H0(1+z)^2 and the structure-growth history it drives (growth feels the altered Hubble
friction even with eta=1). Slip is, at present, a null prediction -- stated honestly.

================================================================================
5. HONEST STATUS
================================================================================
[SOLID -- redshift kinematics]
  - 1+z = (t_obs/t_em)^(1/2); photon energy 1/(1+z); durations (1+z); blackbody preserved
    (occupation identity verified numerically); Tolman (1+z)^-4 surface brightness.
  - All follow from one universal emergent metric (Delta c/c = 0) => genuine metric redshift, not
    tired light. The three tests PASS. (Make-or-break: passed.)
  - H(z)=H0(1+z)^2, D_C=(z/(1+z))/H0, D_L=z/H0, D_A=(z/(1+z)^2)/H0 -- numerically confirmed.

[NEG -- honest negatives]
  - H(z)=H0(1+z)^2 overshoots LCDM 1.7-3x (z=0.5-2): single-stage coarsening has no matter/DE
    era, no acceleration. Needs priority #4 (multi-stage ordering / free-energy floor).
  - Cosmological slip/lensing is GR-like (eta=Sigma=1); the v1 sign-change is a confirmed UV
    (gap-scale) artifact. No validated cosmological MG slip signal exists right now.

[STRUCT / DEFER -- needs one more sub-calculation]
  - eta=Sigma=1 + O((k/Lambda)^2 ~ 10^-120) rests on the IR theory being induced Einstein gravity
    (Reference Sec 6) -- solid as a leading statement; the horizon-scale anisotropic-stress
    coefficient c_Pi (the only place an O((H/k)^2) signal could appear) requires the full
    linearized IR EFT on the FRW coarsening background. That perturbation calculation is the
    natural follow-on (and would also deliver growth f sigma_8(z) to confront data).

[CAVEAT carried from earlier notes]
  - The PHYSICAL massless photon is still un-derived (Reference Sec 12 OPEN); the redshift tests
    here use the massless IR modes the theory DOES have (Goldstone/graviton sector, z=1). The
    kinematics are metric-universal, so they apply to any massless mode, but a CMB-photon
    statement formally awaits the massless-photon derivation.

================================================================================
6. ONE-PARAGRAPH SUMMARY
================================================================================
Recomputing redshift in the IR theory at the coherence length, the coarsening expansion
a ~ L_ord ~ t^(1/2) gives a GENUINE metric redshift, 1+z = (t_obs/t_em)^(1/2), that PASSES all
three tests -- photon energy ~ 1/(1+z), durations ~ (1+z), and blackbody preserved at
T_obs=T_em/(1+z) -- because CCEF has one universal emergent metric on which every massless mode
and clock moves with identical c_eff (Delta c/c=0), the hallmark that separates real expansion
from tired light; the Tolman (1+z)^-4 surface-brightness law follows too. The derived observables
H(z)=H0(1+z)^2, D_C=(z/(1+z))/H0, D_L=z/H0, D_A=(z/(1+z)^2)/H0 are confirmed numerically, but
H(z) overshoots LCDM by 1.7-3x over z=0.5-2: the single-stage coarsening law is a decelerating,
radiation-like skeleton with no matter/dark-energy era (priority #4). For slip and lensing, the
v1 sign-change at k=Lambda is shown to be a gap-scale artifact (it gives an absurd (Lambda/k)^2 at
cosmological k); the correct IR theory is Sakharov-induced Einstein gravity, so eta=Sigma=1 to
within (k/Lambda)^2 ~ 10^-120, and the only possible cosmological-scale departure is horizon-scale
anisotropic stress of the coarsening field whose O(1) coefficient awaits the full perturbed IR
EFT. Net: the redshift sector is sound (make-or-break passed), the slip sector is GR-like (the v1
prediction was mis-scaled), and CCEF's real falsifiable cosmological handle is the expansion
history H(z) and the growth it drives -- not modified-gravity slip.
================================================================================
