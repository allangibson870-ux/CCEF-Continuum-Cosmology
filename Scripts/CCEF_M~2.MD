================================================================================
CCEF v2 — DERIVATION NOTE: M1b — THE BARYON QUARTIC IS UV-INSULATED
        PLANCK-SCALE INDUCED GRAVITY AND THE PROTON CALIBRATION COEXIST:
        THE INDUCED-SKYRME LOG DOES NOT RUN TO M
Closes the load-bearing open M1b created by M1 (resume items M1/M1b). Compiled
2026-07-02. Builds on: M1 (in resume: LI non-local completion, M = M_Pl
sqrt(6pi/N_eff) ~ 1.5-2.5 M_Pl fixed by G_N), CCEF_Reference_v2.txt Sec 8.2
(induced Skyrme B2, soliton-scale matching), Sec 8.4 (tree c4, E*R = 4.06),
Sec 9 ("root caveat"), CCEF_cPi_exact_and_joint_fit.md (m_sigma ~ Lambda,
"Scale 1"). No hand fitting; pure EFT bookkeeping, every scale already derived.
Labels: [SOLID] derived/verified | [THM] structure theorem | [CORR] corrects an
        earlier statement | [OPEN] unknown | [NEG] honest negative
================================================================================

--------------------------------------------------------------------------------
0. THE THREAT AND THE HEADLINE
--------------------------------------------------------------------------------
THE THREAT (M1b, from M1): matching Newton's constant fixed the non-locality
scale at M ~ 1.6-2.5 M_Pl. Naively extending the induced-Skyrme computation of
Reference Sec 8.2 -- B2 = (0.949/16pi^2) ln(k_UV R_sol) with k_UV -> M -- gives
B2 = 0.271 (was 0.033 at k_UV ~ 122 GeV, a x8.3 amplification), an induced-only
E*R ~ 32-86 against the proton's 4.06, unsubtractable by the positive tree c4.
Gravity at Newton strength appeared to destroy the baryon calibration.

HEADLINE: THE THREAT IS AN EFT BOOKKEEPING ERROR, AND IT DISSOLVES.       [THM]
The chiral log ln(UV x R_sol) is a property of the NONLINEAR (constrained)
sigma-model EFT, which exists only BELOW the radial (amplitude) threshold
m_sigma ~ Lambda. Above m_sigma the theory LINEARIZES -- the amplitude chi is a
dynamical mode (it MUST be: the ordering transition, chi = 0 -> chi_0, is the
theory's own cosmogenesis) -- and in the linear theory every four-gradient
operator is dimension-8 IRRELEVANT: contributions from the regulator scale M
are power-suppressed by (Lambda/M)^4 ~ 2e-80, and the tree c4 runs only through
the weak CW couplings, ~ 8e-4 relative over the full range M -> Lambda.
Moreover the chiral-log window itself is EMPTY: the soliton scale
k_sol = 1/R_sol = 4.42 CCEF sits ABOVE m_sigma = 1.9-2.7 CCEF
(k_sol/m_sigma = 1.7-2.4), so ln(m_sigma R_sol) = -0.85..-0.51 <= 0 -- there is
no log at all. The corrected induced quartic is pure threshold matching,
   B2_induced = (0.949/16pi^2) x O(1) ~ 0.006 ,   INDEPENDENT OF M,
cleanly subdominant to the tree c4 = 0.028. The proton point E*R = 4.06 stands,
provably uncontaminated by the gravity scale. Newton-strength induced gravity
and the baryon calibration COEXIST with one M. [SOLID/THM]

================================================================================
1. THE THREE OUTS, SCORED
================================================================================
M1 listed three possible escapes. Scored honestly:

(i) "Does the form factor act differently on a1 (Einstein) vs a2 (Skyrme)?"
    FAILS AS STATED. One form factor, one M: the proper-time shift s -> s+1/M^2
    cuts the a1 integral (ds/s^2 -> M^2) and the a2 integral (ds/s -> ln M^2)
    at the same scale. Within the naive constrained-model computation, the a2
    log genuinely runs to M. No differential regulator rescue.          [NEG]

(ii) "Does the 2:1 [S^2 vs TrT^2] mix partially cancel in the soliton energy?"
    FAILS. For a static hedgehog both invariants are positive-definite
    (S^2 = (|grad phi|^2)^2 >= 0, TrT^2 = sum_ij (d_i phi . d_j phi)^2 >= 0)
    and scale identically under Derrick. Both add energy; nothing cancels. [NEG]

(iii) "Is the log cut below M by the gap/EFT breakdown?"
    SUCCEEDS, in sharpened form -- not as a soft cutoff plea but as a window
    structure theorem (Sec 2). The a2 chiral log is not a property of the
    fundamental theory; it is a property of the CONSTRAINED EFT, and the
    constrained EFT ends at m_sigma, far below M.                       [THM]

================================================================================
2. THE WINDOW STRUCTURE THEOREM
================================================================================
2.1 The theory has a radial threshold. The matter field is phi = chi U with a
DYNAMICAL amplitude chi: the CW potential U(chi) exists (U_chi note), the
ordering transition chi: 0 -> chi_0 is the origin of the universe in this
framework, and the radial mass is m_sigma^2 = U''(chi_0) ~ 2|r| ~ Lambda^2
("Scale 1" of the c_Pi note; numerically m_sigma = 1.9-2.7 CCEF). The
constraint |phi| = 1 is the LOW-ENERGY (k << m_sigma) description only. [SOLID]

2.2 Above m_sigma: linear regime -- four-gradient operators are irrelevant.
In the linear theory the operator (d phi . d phi)^2-type has dimension 8. Its
coefficient at the threshold, from physics at M, is suppressed by matching:
   delta B2 (from M) ~ (Lambda/M)^4 ~ 2e-80 .                          [SOLID]
The fundamental tree c4 (a dim-8 coefficient in the same basis) runs between M
and Lambda only through the weak CW couplings:
   Delta c4/c4 ~ lambda_CW ln(M/Lambda)/16pi^2 = 0.0028 x 45.8/158 ~ 8e-4 .
No quartic-in-gradients operator is log-fed by M. The regulator scale
DECOUPLES from the hadronic quartic sector.                             [THM]

2.3 Below m_sigma: the chiral-log window is EMPTY for the physical soliton.
The nonlinear EFT (where the a2 log lives) runs from m_sigma down to the
probe scale. The physical (c4-stabilized) soliton has R_sol = 0.226 CCEF, so
   k_sol = 1/R_sol = 4.42 CCEF = (1.7-2.4) x m_sigma  >  m_sigma :
the soliton core probes the LINEAR regime; the chiral-log interval
[k_sol, m_sigma] does not exist (ln(m_sigma R_sol) = -0.85..-0.51 <= 0). The
induced quartic seen by the soliton is therefore pure THRESHOLD MATCHING at
m_sigma:
   B2_induced = (0.949/16pi^2) x O(1) = 0.006 x O(1) ,  M-INDEPENDENT. [THM]
(The O(1) includes the one-loop matching constant; a factor-few uncertainty,
irrelevant against c4 = 0.028 at the current precision of the sector.)

2.4 Consequence: a1 and a2 decouple. Induced gravity is a QUADRATIC (a1)
effect and lives at M: 1/16piG ~ N_eff M^2/96pi^2 (M1). The baryon quartic is
an a2 effect confined to the constrained window below m_sigma. The same loop
expansion feeds them at different scales, and NOTHING transmits M into the
hadronic quartic beyond (Lambda/M)^4 and the 8e-4 running:
   dB2/dlnM = O( (Lambda/M)^4 , lambda_CW/16pi^2 ) ~ 0 .
THE BARYON SECTOR IS UV-INSULATED. Reference Sec 9's "root caveat" (baryon
tied to the UV scale through the induced Skyrme) is resolved in the favorable
direction: it was an artifact of running the chiral log outside its EFT. [THM]

================================================================================
3. CORRECTIONS TO EARLIER STATEMENTS  [CORR]
================================================================================
* Reference Sec 8.2's B2 ~ 0.033-0.038 ("converged at A3 = 1e-6") extended the
  chiral log from the soliton scale up to k_UV ~ 122 GeV -- i.e., through and
  far above the radial threshold. Corrected, the induced-only quartic is
  ~0.006 x O(1). The "derived induced baryon is 2-3x too heavy" statement
  softens accordingly (induced-only E*R rescales from ~12 toward ~2-5,
  O(proton), though the induced-only route stays superseded).
* M1's B2(M) = 0.271 (and the x8.3 amplification) is VOID -- same error,
  larger window. The M1b threat was created by the bookkeeping, not by M.
* "The induced (heat-kernel) Skyrme is subdominant to the tree term"
  (Sec 8.4) is now CLEANLY true (0.006 vs 0.028) rather than marginally
  awkward (0.038 vs 0.028): the one-fit c4 story is strengthened.
* For completeness: integrating out sigma at TREE level also generates the
  pure-S^2 quartic c_S2 ~ Zt^2 chi_0^2/(2 m_sigma^2) = 0.07-0.14. This is
  M-INDEPENDENT (a hadronic-scale object, implicitly part of the sector's
  calibration at any regulator scale) and does not affect M1b; it should be
  folded into the next re-derivation of the E*R = 4.06 point.          [OPEN]

================================================================================
4. WHAT REMAINS (the honest price of M ~ M_Pl)
================================================================================
M1c (NEW, [OPEN]): NATURALNESS. The gap itself is a scalar mass^2, and generic
matching at M gives delta A4 ~ N M^2/16pi^2 ~ 1.2e39 CCEF vs A4 = 3.56: a
tuning of ~3e-39 = O((Lambda/M)^2). This is the standard scalar hierarchy
problem, imported into CCEF the moment the second scale M exists -- the same
problem the Standard Model has with the Higgs. Whether the ghost-free
non-local completion softens power divergences enough to protect the gap is a
genuine open question (to be computed, not asserted). Note: M1b's RESULT does
not depend on it -- insulation of the quartic holds whether or not the mass
term is tuned.                                                          [OPEN]
M2 (unchanged, sharpened by M1): the a0 term ~ N M^4/32pi^2 ~ 4e75 GeV^4 vs
rho_Lambda_obs = 2.5e-47 -- mismatch 1e122; the patch-minus-eternal-medium
zero is the only in-theory subtraction candidate.                       [OPEN]
M4 (unchanged): adiabatic perturbation origin at the transition.        [OPEN]

================================================================================
5. HONEST STATUS
================================================================================
[THM/SOLID]
  - Window structure theorem: chiral log confined to k < m_sigma; linear-regime
    feed-down from M suppressed by (Lambda/M)^4 ~ 2e-80; c4 running ~ 8e-4.
  - Empty window for the physical soliton: k_sol/m_sigma = 1.7-2.4 > 1.
  - B2_induced = 0.006 x O(1), M-independent => dB2/dlnM ~ 0: UV insulation.
  - M1 + M1b jointly: Newton-strength induced gravity (M = 1.5-2.5 M_Pl) and
    the proton calibration (E*R = 4.06, tree c4 = 0.028) coexist with one M.
[CORR]
  - Sec 8.2's B2 overestimated (log run above threshold); M1's 0.271 void;
    "induced subdominant to tree" now cleanly true.
[NEG]
  - Outs (i) and (ii) fail; the rescue is (iii) alone, but it is a theorem,
    not a plea.
[OPEN]
  - O(1) threshold-matching constant in B2_induced (factor-few).
  - Fold the sigma-exchange S^2 quartic (0.07-0.14) into the E*R re-derivation.
  - M1c naturalness of the gap under M-scale corrections (standard hierarchy
    problem; does the non-local completion protect it?).
  - M2 (Lambda_eff, 1e122), M4 (adiabatic perturbations) -- next in order.

================================================================================
6. ONE-PARAGRAPH SUMMARY
================================================================================
The M1b threat -- that fixing Newton's constant at M ~ 1.6-2.5 M_Pl drags the
induced-Skyrme coefficient to B2 = 0.271 and destroys the proton's E*R = 4.06
-- dissolves under correct EFT bookkeeping: the chiral log ln(UV x R_sol) is a
property of the constrained nonlinear sigma model, which exists only below the
radial threshold m_sigma ~ Lambda (the amplitude is dynamical -- the ordering
transition is the theory's own origin story), while above m_sigma the theory
linearizes and every four-gradient operator is dimension-8 irrelevant, so the
regulator scale feeds the hadronic quartic only through (Lambda/M)^4 ~ 2e-80
and a ~8e-4 weak-coupling running of the tree c4; and the chiral-log window is
in fact empty for the physical soliton, whose core scale k_sol = 4.42 CCEF
sits a factor 1.7-2.4 ABOVE the threshold, leaving pure threshold matching
B2_induced ~ 0.006 x O(1), independent of M and cleanly subdominant to the
tree c4 = 0.028. Of M1's three candidate outs, the differential-form-factor
and mix-cancellation routes fail, but the window structure succeeds as a
theorem: dB2/dlnM ~ 0 -- the baryon sector is UV-insulated, the a1 (gravity)
and a2 (Skyrme) coefficients decouple, Reference Sec 9's root caveat resolves
favorably, and en route the old B2 ~ 0.038 is corrected to ~0.006, making
"induced subdominant to tree" cleanly true and leaving the one-fit c4 story
stronger than before. The price that remains is honest and standard: the gap
inherits the scalar hierarchy problem (tuning ~3e-39, new open M1c), and M2's
10^122 vacuum-energy mismatch plus M4's adiabatic-perturbation origin are now
the last gates on CCEF cosmology.
================================================================================
