================================================================================
CCEF OPEN ACTION — McFADDEN–SKENDERIS <TT> TILT FOR THE 3D O(3) MEDIUM
Executes the single live open item flagged 2026-07-07 (Ref. v2.1, Sec 15.8):
"the full McFadden–Skenderis <TT> computation for 3D O(3) to pin the tilt coefficient."
Compiled 2026-07-08.  Labels as in the reference: [SOLID]/[CONJECT]/[NEG]/[OPEN].
Working principle: derive from the correlator, label honestly, flag every fit.
================================================================================

QUESTION (verbatim target). After S1–S3 (2026-07-07) the amplitude is conceded and
the TILT is billed as "the one surviving primordial prediction": n_s = 1 − eta_O(3)
= 0.963. S3 itself flags the gap: "The exact coefficient (−1×eta vs −c×eta) needs the
full McFadden–Skenderis <TT> computation for O(3)." This note performs that computation
at the level its own method allows and returns the coefficient.

--------------------------------------------------------------------------------
1. THE DICTIONARY (McFadden–Skenderis holographic cosmology)
--------------------------------------------------------------------------------
The primordial spectra are set by the stress-tensor 2-point function of the 3D medium:
   <T_ij(q) T_kl(−q)> = A(q) Pi_ijkl + B(q) pi_ij pi_kl ,
   pi_ij = delta_ij − q_i q_j/q^2 ,  Pi = transverse-traceless projector.
Power spectra (MS analytic continuation q→−iq):
   Delta_S^2(q) = − q^3 / (16 pi^2 Im B(−iq)) ,
   Delta_T^2(q) = − 2 q^3 / (pi^2 Im A(−iq)) ,
   n_s − 1 = d ln Delta_S^2 / d ln q .
The scalar tilt therefore lives ENTIRELY in the q-dependence of the scalar structure
function B(q). This is the correct object; the susceptibility argument of S3 is NOT.

--------------------------------------------------------------------------------
2. THE FIXED-POINT RESULT — n_s = 1 EXACTLY  [SOLID]
--------------------------------------------------------------------------------
T_mu_nu is CONSERVED (d^mu T_mu_nu = 0) and hence has scaling dimension EXACTLY
Delta_T = d = 3, with NO anomalous dimension — this is the same Ward identity that
holds the composite graviton at zero mass (Ref. Sec 5, Eq. 14–15). Conformal invariance
of the O(3) Wilson–Fisher fixed point then fixes, by dimensional analysis alone,
   B(q) = c_B q^3   (exactly),   c_B ∝ 1/C_T (central charge).
=> Delta_S^2 = const  =>  n_s = 1 EXACTLY, with ZERO coefficient on eta.
This CONFIRMS the flatness half of S3 and its shared origin with the massless graviton.
It also fixes the first half of the answer: at criticality the tilt is not −eta; it is 0.

--------------------------------------------------------------------------------
3. WHERE A TILT CAN COME FROM  (and where it cannot)
--------------------------------------------------------------------------------
Because B(q) ∝ q^3 is LOCKED by conformal symmetry, a nonzero tilt REQUIRES breaking
that symmetry — a deformation of the O(3) fixed point by some operator O of dimension
Delta with coupling lambda:
   B(q) = c_B q^3 [ 1 + kappa · lambda · (q/mu)^{Delta − 3} + ... ] ,
   n_s − 1 = (3 − Delta) · kappa lambda (q/mu)^{Delta−3} + O(lambda^2)   [leading].
So the tilt is controlled by the DEFORMING operator's distance from marginality (3−Delta)
and its running coupling — i.e. by a beta function. It is NOT controlled by the
order-parameter field anomalous dimension eta. eta = eta_phi describes <phi phi>, a
DIFFERENT correlator, not <TT>. Nothing in the <TT> structure produces an eta prefactor.

--------------------------------------------------------------------------------
4. WHAT ACTUALLY DEFORMS THE CCEF MEDIUM  [SOLID inputs, standard O(3) CFT data]
--------------------------------------------------------------------------------
The 3D O(3) universality class has two relevant scalar deformations off criticality:
   (i)  ordering field h  ↔  phi ,   Delta_phi = (d − 2 + eta)/2 = (1 + eta)/2 = 0.519 ;
   (ii) reduced temperature t ↔ energy op eps ~ phi^2 , Delta_eps = 3 − 1/nu ,
        nu_O(3) = 0.7112  =>  1/nu = 1.406  =>  Delta_eps = 1.594 .
BOTH are STRONGLY relevant (Delta well below 3); NEITHER is near-marginal. Consequences:
   * There is no near-marginal (3−Delta small) operator to give a SMALL, slowly-running
     tilt in the MS sense. The would-be marginal quartics of the CCEF action are the
     3-operator basis {O1,O2,O4} of Sec 14.1, whose one-loop beta is purely Gaussian
     (no interacting window) — they do not drive a conformal-window tilt either.
   * Cosmological modes sit at q << Lambda (deep IR), where a relevant deformation has
     already driven the medium FAR from the fixed point into the GAPPED phase. There
     B(q) → analytic q^4 (white noise) => n_s → 4 (steep BLUE). This is exactly the
     Sec 14.2(b) / 14.4 "scale-matching / common-obstruction" failure, now re-derived
     from <TT> directly: the scale-invariant (n_s=1) window is Lambda < q < M, which
     never reaches observable q << Lambda. [SOLID / NEG]

--------------------------------------------------------------------------------
5. IS n_s − 1 = −eta RECOVERABLE?  — NO.  [NEG for the coefficient]
--------------------------------------------------------------------------------
Track every route to a "−eta":
  (a) <TT> at criticality (the actual seed correlator, route c):  n_s − 1 = 0.
      Coefficient on eta is ZERO. (Section 2.)
  (b) <phi phi> (order-parameter inheritance, route b, already FAILED):
      n_s − 1 = 2 Delta_phi − 3 = (1 + eta) − 3 = eta − 2 = −1.963  =>  n_s = eta − 1
      = −0.963. This is the ONLY place a bare "−eta"-like term appears — and it comes
      dragging the −2 that makes it the steeply-RED, wrong-shape spectrum the reference
      already discarded. It is NOT n_s = 1 − eta.
  (c) The S3 susceptibility heuristic (chi ~ xi^{2−eta}): this is a statement about the
      ORDER-PARAMETER response, i.e. route (b) again. Grafting its −eta onto the flat
      <TT> spectrum of route (c) mixes two different correlators; it is not a derivation.
CONCLUSION: no operator in the 3D O(3) CFT gives a <TT> scalar tilt n_s − 1 = −eta with
coefficient −1 (or any derived −c·eta). The three self-consistent outcomes are:
     at the fixed point         n_s = 1        (T conserved)                [SOLID]
     off it, from <phi phi>      n_s = eta − 1 ≈ −0.96 (route b, wrong)     [SOLID/NEG]
     off it, IR (cosmological)   n_s → 4        (gapped white noise)        [SOLID/NEG]
The observed value 0.965 lies in NONE of these. The match n_s = 1 − eta = 0.963 is a
NUMERICAL COINCIDENCE — empirically 1 − n_s^obs ≈ 0.035 ≈ eta_O(3) — not a CCEF output.

--------------------------------------------------------------------------------
6. VERDICT  (folds back into Sec 15.8)
--------------------------------------------------------------------------------
FLATNESS survives, for the stated reason: T conservation ⇒ Delta_T = 3 ⇒ n_s = 1 at the
critical point, sharing the graviton's Ward identity. This half of S3 is [SOLID].

The TILT COEFFICIENT does NOT close. The MS <TT> computation gives coefficient 0 on eta
at criticality; any nonzero tilt is set by a relevant deformation (Delta_eps ≈ 1.59,
running ~ 1/nu), NOT by eta, and in the cosmological IR it runs the medium into the
gapped phase (white noise), reproducing the Sec 14.2/14.4 obstruction rather than a small
red −eta. Therefore:

  *** DOWNGRADE: the "one surviving prediction" n_s = 1 − eta = 0.963 is NOT derivable
      from CCEF's own seed correlator. CCEF robustly owns SPECTRUM FLATNESS (n_s = 1);
      it does NOT own the tilt magnitude/coefficient. The red-tilt-of-the-right-size
      claim reduces to a coincidence (1 − n_s^obs ≈ eta) plus a defensible-but-unquantified
      sign argument. S3's tilt is reclassified [CONJECT → NEG for the −eta coefficient;
      SOLID only for n_s = 1 flatness]. ***

Net standing of CCEF cosmology after this action: shape FLATNESS [SOLID]; tilt VALUE
[not derived]; amplitude [conceded, S1/S2]. The seed sector owns one robust structural
statement (flatness = graviton Ward identity) and no quantitative prediction.

--------------------------------------------------------------------------------
7. WHAT AN HONEST REVIVAL OF THE TILT NEEDS  (open, carried)
--------------------------------------------------------------------------------
T1 A mechanism that keeps OBSERVABLE (q << Lambda) modes NEAR criticality, so the
   n_s = 1 window reaches cosmological scales. This is the unsolved SOC / scale-matching
   problem (Sec 14.2, 14.4) — the SAME common obstruction, not a separate item.
T2 GIVEN T1, the tilt = (3 − Delta_deform) × running of the deforming coupling; compute
   its beta function to fix sign AND magnitude. Only then is n_s − 1 defined.
T3 Amplitude stays an import (S1/S2). Central charge C_T of 3D O(3) (bootstrap value,
   C_T/C_T^free ≈ 0.94, i.e. C_T = O(few)) reconfirms the ~10^6 shortfall of Sec 15.6 —
   independent of the tilt question.

RESIDUAL UNCERTAINTY (flagged): the SCALING conclusions here (Delta_T=3 ⇒ n_s=1;
tilt set by deformation, not eta; IR white noise) follow from conservation + standard
O(3) operator dimensions and are robust. The exact O(1) AMPLITUDE c_B (central charge)
and the full tensor A(q) would require the numerical/bootstrap 3D O(3) <TT>; they do not
change the coefficient result — the tilt is not −eta regardless of those constants.
================================================================================
End of open-action note (2026-07-08). Result: flatness SOLID; tilt coefficient −eta NOT
recovered; S3's surviving prediction downgraded to a coincidence + unquantified sign.
================================================================================
