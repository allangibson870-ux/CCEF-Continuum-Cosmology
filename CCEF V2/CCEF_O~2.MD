================================================================================
CCEF OPEN ACTION (2) — PRIMORDIAL AMPLITUDE FROM THE DISORDERED-PHASE <TT> LOOP
Recompute A_s by evaluating <T T> strictly as a loop-level convolution integral in the
disordered phase (<|Phi|>=0), with the tree-level classical condensate removed.
Compiled 2026-07-08.  Labels: [SOLID]/[NEG]/[OPEN].  Principle: derive, do NOT tune to target.
Numerical checks run (3D bubble, exact); see Sec 4.
================================================================================

REQUESTED HYPOTHESIS. Moving the seed calculation to the disordered melt sets <|Phi|>=0,
kills the classical condensate cross-term, shifts the whole burden to the internal momentum
integral of critical fluctuations, and thereby "naturally suppresses" A_s past the C_T
bottleneck. I carried this out. RESULT: it does NOT work, and the stated root-error diagnosis
does not match what the loop actually is. Details below, honestly.

--------------------------------------------------------------------------------
1. THE STRESS TENSOR IS ALREADY PURELY COMPOSITE -- there was no condensate term to remove
--------------------------------------------------------------------------------
T_mu_nu for the order parameter is bilinear in fields: T ~ d_mu n . d_nu n (+ improvement).
Its 2-point function is therefore, at leading order, a ONE-LOOP CONVOLUTION of two field
propagators -- a bubble -- with NO tree/classical piece:
   <T(q) T(-q)> = (sym) INT d^3k/(2pi)^3  V(k,q,q-k) G(k) G(q-k) ,   G(k)=1/k^2 (critical).
A nonzero <|Phi|> would ADD a tree contraction (one leg -> condensate), but in the melt
<|Phi|>=0 removes exactly that piece and leaves the bubble. So "eliminating the condensate
and shifting to the internal momentum integral" is not a new regime -- IT IS the standard
definition of <TT> at a critical point. The reference already worked here: the graviton
Pi^TT was verified in the disordered phase (Ref. Sec 15.4), and the seed C_T was the
disordered critical mode count (Sec 14.2, 15.6). There was no ordered-phase classical
condensate "dominating the math" in the prior seed estimate; the earlier number was already
the loop/critical value.

--------------------------------------------------------------------------------
2. WHAT THE LOOP CONVOLUTION ACTUALLY GIVES -- it IS C_T, and C_T is O(N)  [SOLID]
--------------------------------------------------------------------------------
The bubble of a conserved bilinear is, by conformal invariance, fixed to
   <T(q)T(-q)>_scalar  =  C_T * (numerical O(1)) * q^3 ,
and C_T -- the central charge -- is DEFINED as the normalisation of exactly this loop.
Counting fields in the loop:  C_T = N_fields x C_T^{single} .  The convolution cannot
manufacture a coefficient unrelated to its own field content; the field count IS the
coefficient. So the loop "burden shift" lands back on C_T ~ N ~ few. The MS scalar amplitude
   A_s = 1 / (16 pi^2 C_T)
is then O(1e-3) for N=2..4 -- SIX orders too LARGE, identical to Sec 15.6. The momentum
integral does not rescue it because C_T is the very thing the momentum integral computes.

--------------------------------------------------------------------------------
3. DOES THE MOMENTUM INTEGRAL SUPPLY A LARGE SUPPRESSION? -- NO  [SOLID, checked]
--------------------------------------------------------------------------------
The only numbers a convergent 3D critical loop produces are O(1) kinematic coefficients and
the standard loop factor 1/16pi^2 (already in the MS formula). Concretely, the elementary
3D bubble
   I(q) = INT d^3k/(2pi)^3  1/(k^2 (q-k)^2)  =  1/(8|q|)   [coefficient = 1/8].
The derivative vertices of T promote 1/(8q) -> C_T q^3 with a coefficient still O(1)xN.
Nowhere does a factor ~1e-6 appear. A convergent, scale-invariant integral returns the
scale-invariant CFT structure with an O(1) prefactor -- BY CONSTRUCTION it cannot output the
extra 10^6 suppression, which would require C_T ~ 3e6 (see Sec 4). [SOLID]

--------------------------------------------------------------------------------
4. NUMERICAL VERIFICATION (run 2026-07-08)
--------------------------------------------------------------------------------
   3D bubble I(q=1):  numeric 0.125000  vs exact 1/(8q)=0.125000   ratio 1.0000  [confirmed]
   inner ∫(dk/k)ln|(k+q)/(k-q)| = 4.93480  vs exact pi^2/2 = 4.93480               [confirmed]
   1/16pi^2 = 6.33e-3
   A_s = 1/(16pi^2 C_T):   N=2 (C_T~1.9) -> 3.4e-3 ;  N=3 (C_T~2.8) -> 2.2e-3 ;
                           N=4 (C_T~3.8) -> 1.7e-3      [all ~1e-3, need 2.1e-9]
   C_T required for A_s=2.1e-9:  3.0e6   =>  shortfall vs C_T~3:  ~1.0e6 .
(C_T^{O(N)} from conformal bootstrap ~ 0.94 N in free-scalar units -- a few, not 3e6.)

--------------------------------------------------------------------------------
5. THE "TURBULENT / OUT-OF-EQUILIBRIUM PHASE-SPACE" ESCAPE -- assessed  [NEG, already closed]
--------------------------------------------------------------------------------
The one way to escape C_T is to ABANDON the equilibrium-critical <TT> and use a genuine
NON-equilibrium (wave-turbulent / kinetic) spectrum, where phase-space restrictions could
suppress power. But this route:
  (a) FORFEITS the conformal <TT> shape that supplies n_s=1 -- a turbulent cascade has its
      OWN inertial-range exponents, not the Ward-identity flatness (Ref. Sec 15.8/S3). You
      cannot keep the scale-invariant shape AND invoke turbulence to kill the amplitude; a
      steady cascade has CONSTANT exponents, so amplitude and tilt stay LOCKED (this is
      exactly the wall recorded in Sec 15.6 and the S1/S2 super-Ohmic result, Sec 15.8).
  (b) Offers no DERIVED suppression factor. Asserting that scattering "naturally suppresses"
      by ~10^6 without a computed kernel is precisely the move the reference's own working
      principle forbids (cf. the 2026-07-04 retraction of the fabricated C~N_eff=9 that had
      been chosen to hit a target). A number this large must be derived, not asserted.
  (c) The equilibrium critical medium is a FEW-dof classical theory; the deep reason A_s is
      too large (Sec 15.6) is that small-C_T scale-invariance forces O(1) fluctuations --
      "precisely why inflation exists." Non-equilibrium dynamics does not change the dof
      count.

--------------------------------------------------------------------------------
6. VERDICT
--------------------------------------------------------------------------------
The disordered-phase loop-convolution amplitude is C_T-controlled with C_T ~ N ~ few,
reproducing A_s ~ 1e-3 and the SAME ~10^6 shortfall. The condensate was never the culprit:
<TT> is intrinsically the composite bubble, and the prior estimate already lived in the
disordered/critical phase. The momentum integral yields O(1) coefficients (verified: 1/8)
and cannot supply a 1e-6 suppression; doing so would require either C_T ~ 3e6 (absent in a
few-field theory) or a non-equilibrium spectrum that destroys the n_s=1 shape and was already
found not to close (Sec 15.6, 15.8-S1/S2).

  *** RESULT: the disordered-melt recomputation does NOT bypass the C_T bottleneck.
      Amplitude remains an IMPORT; Sec 15.8's S1/S2 (amplitude not closed) stands. The
      standing is unchanged: CCEF owns spectrum FLATNESS [SOLID] (T-conservation Ward
      identity, shared with the massless graviton), NOT the amplitude and NOT the tilt
      coefficient (see companion note CCEF_openaction_MS_TT_tilt). ***

--------------------------------------------------------------------------------
7. WHAT WOULD ACTUALLY BE REQUIRED (open, honest)
--------------------------------------------------------------------------------
A1 A large effective central charge C_T ~ 3e6 from within CCEF. Only a large-N (or a tower
   of light modes) medium supplies it -- absent in CP^1..CP^3 (Sec 14 NEXT-DIRECTION already
   noted large-N helps C_T but breaks the S^2 graviton spine). This is the real lever, and
   it is a change of field content, not a phase or a loop re-labelling.
A2 OR a derived (not asserted) non-equilibrium suppression kernel with a COMPUTED factor,
   which must simultaneously preserve n_s=1. No such kernel exists to date (super-Ohmic bath
   gave the right STRUCTURE but W~0.14, short by ~100 -- Sec 15.8 S1).
================================================================================
End of open-action(2) note (2026-07-08). Amplitude NOT closed by the disordered-phase loop;
C_T~few bottleneck intrinsic; turbulent escape forfeits the shape and is undable-derived.
================================================================================
