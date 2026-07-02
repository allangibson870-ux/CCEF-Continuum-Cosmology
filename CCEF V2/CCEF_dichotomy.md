================================================================================
CCEF v2 — DERIVATION NOTE: THE DICHOTOMY
        a(t) FROM INTERNAL COARSENING IN THE COHERENCE-PATCH PICTURE:
        THE SCALING THEOREM, THE DEATH OF THE POWER-LAW FAMILY, AND WHY
        CONTENT-RESPONSE IS INDUCED EINSTEIN (NOT IMPORTED GR)
Closes the reframed background question (resume item N). Compiled 2026-07-02.
Builds on: CCEF_gamma_CaldeiraLeggett_derivation.md (Model A, xi ~ t^1/2),
CCEF_cmb_acoustic.md + CCEF_joint_mcmc.md (the kill-test machinery, reused),
CCEF_Reference_v2.txt Sec 5-6 (correlator metric, composite graviton, Ward
identity, G_munu = 8 pi G T_munu verified 5.8e-16), resume item M (the
induced-Einstein branch and its opens M1-M4).
ONTOLOGY (fixed input): order emerges LOCALLY within the infinite, eternal
continuum. The observable universe is a finite, expanding region of coherence
inside a mostly disordered medium. There is NO macroscopic domain wall
surrounding us -- the boundary of the patch is a correlation crossover, not a
defect. No walls, no ponds, no fronts, no front-radius ruler anywhere below.
Labels: [SOLID] derived/verified | [THM] theorem | [NEG] honest negative |
        [STRUCT] forced by structure | [OPEN] unknown
================================================================================

--------------------------------------------------------------------------------
0. THE QUESTION AND THE ANSWER
--------------------------------------------------------------------------------
QUESTION: in the coherence-patch picture, derive the effective large-scale a(t)
from internal coarsening alone -- without re-introducing the falsified ansatz
a ~ L_ord, and without importing GR.

ANSWER (a dichotomy, both horns derived):
  HORN 1 [THM+NEG]: internal coarsening alone CANNOT give the observed a(t) --
  not because of any parameter choice, but structurally: dynamical scaling
  leaves the coarsening state exactly ONE evolving length, so every possible
  correlator-built metric is a pure power law a ~ t^{p/2}, H = H0(1+z)^{2/p}.
  The complete one-parameter family is falsified by the data at every point
  (best member: Delta chi2 = +242 AND theta* off 79x; no member fits two eras
  at once).
  HORN 2 [THM+STRUCT]: matching the data requires era transitions, i.e. a
  metric that responds to WHICH energy component currently dominates. But for
  a metric built from the field's correlators, the emergent-diffeomorphism
  Ward identity -- the same [SOLID] identity that keeps the composite graviton
  massless -- forces that response to be the induced-Einstein one. CONTENT-
  RESPONSIVE METRIC == INDUCED EINSTEIN. This is not imported GR; it is the
  already-verified (5.8e-16) consistency condition of CCEF's own graviton
  sector, now applied at zeroth order.
  THERE IS NO THIRD OPTION. One-length scaling => power law (dead, all of it);
  content response => induced Einstein (resume item M), carrying its honest
  opens (M1 induced-G magnitude, M2 Lambda_eff, M4 perturbation origin) -- but
  with two genuine gains from the coherence-patch picture itself (Sec 4).

================================================================================
1. SETUP: COARSENING WITHOUT WALLS, AND WHAT "METRIC" CAN MEAN
================================================================================
1.1 The state. After the (energy-based, local) onset of order, the medium
inside the patch is a Model-A relaxational coarsening state of the continuous
order parameter (S^2 director / S^3 field). No walls are needed for coarsening:
continuous symmetries coarsen through TEXTURES, with the same derived growth
law xi(t) = sqrt(2 A1 t / gamma_0) ~ t^{1/2} (gamma note; the exponent is the
universality class, not a detail). The patch is the region where the two-point
function has support: C(r,t) = chi_0^2 f(r/xi(t)) -- dynamical scaling, the
defining property of coarsening. Its edge is where f decays: a crossover into
disorder, not a wall. [SOLID]

1.2 What can play a(t). "No external spacetime; metric emergent from
correlations of the field" (Reference Sec 0). At zeroth order the candidates
are the coarse-grained equal-time expectation values of local operators:
   <d_i n_a d_j n_a>, <(d_t n)^2>, chi_0^2(t), C(r,t) and its moments,
   defect/texture densities, mode-occupation integrals, ...
Isotropy makes every tensor candidate proportional to delta_ij; so a^2(t) is
some scalar functional of the coarsening state. The old ansatz picked ONE such
functional (the correlation length itself, a ~ xi). The question is what the
FULL space of choices can give.

================================================================================
2. HORN 1 -- THE SCALING THEOREM AND THE DEATH OF THE POWER-LAW FAMILY
================================================================================
2.1 THE SCALING THEOREM. [THM]
In the scaling regime the coarsening state is statistically self-similar: all
equal-time correlations depend on time only through xi(t). (Microscopic lengths
-- Lambda^-1, the texture core -- enter as t-independent CONSTANTS; they carry
no evolution.) Therefore any a(t) constructed from equal-time expectation
values of local operators of the scaling state obeys
   a(t) = ( xi(t)/xi_0 )^p ,
where p is fixed by the scaling dimension of whichever operator defines the
metric (p = 1 for the length itself, p = -1 for gradient-energy-type operators,
etc. -- every choice lands somewhere on the p-axis, and p cannot evolve while
scaling holds). With the derived xi ~ t^{1/2}:
   a ~ t^{p/2}  =>  H(z) = H0 (1+z)^{2/p}  ==  H0 (1+z)^n ,  n = 2/p .
CONSEQUENCE: the complete space of pure internal-coarsening cosmologies is a
ONE-PARAMETER FAMILY of exact power laws over the entire post-transition
history. The falsified coasting/ansatz cosmology is just the n = 1 member; the
old "t^{1/2} branch" is the n = 2 member. Nothing else exists on this horn.

2.2 THE WHOLE FAMILY IS FALSIFIED. [SOLID/NEG]
Every member was run through the published-covariance machinery of notes F/G
(Pantheon+ 1580 SNe full STAT+SYS cov, offset-marginalized; DESI DR2 13-point
BAO vector + official cov, r_d free; 32 chronometers; theta* analytic-exact for
power laws):
   n      SNe        CC (H0)       BAO        joint    t0 = 13.77/n Gyr
   0.8    1403.8     22.6 (67.5)   1011.5     2437.9   17.2
   1.0    1490.5     16.7 (62.3)    187.1     1694.3   13.8   (= coasting)
   1.2    1664.9     21.5 (57.0)    195.8     1882.2   11.5
   1.4    1921.9     37.9 (51.7)    877.5     2837.3    9.8
   1.577  2214.0     62.7 (47.0)   1913.3     4190.0    8.7
   2.0    3137.0    160.5 (36.2)   5436.3     8733.8    6.9   (= t^{1/2})
   [LCDM, same probes: 1417.9]
   * Joint low-z best member: n = 1.055, chi2 = 1659.9 -> Delta chi2 = +242
     vs LCDM; AND its acoustic scale is 100 theta* = 82.5 -- 79x Planck.
   * The theta*-matching member exists (a nontrivial fact): n = 1.5774 gives
     100 theta* = 1.044 ~ Planck (because LCDM is near-matter-dominated over
     most of the z* -> 0 path, n ~ 1.5 mimics it there). But it pays
     Delta chi2 ~ +2772 at low z and gives t0 = 8.7 Gyr -- younger than its
     oldest stars. Dead.
   * BBN requires n = 2.000 at T ~ MeV; growth-era distances want n ~ 1.5;
     the late universe wants n ~ 0.5-0.8. NO single n serves two eras, let
     alone four.
VERDICT: the data do not merely disfavor a bad member -- they exclude the
FAMILY, i.e. they exclude the scaling structure itself. The observed universe
has ERA TRANSITIONS; a one-length state cannot have any. [NEG]
(Robustness: the theorem's premise -- strict scaling -- is exactly what breaks
in the presence of additional gravitating scales; that is Horn 2, not a rescue
of Horn 1. Scaling VIOLATIONS within pure coarsening (logs, transients near
the transition) modify power laws by slowly-varying factors near t_i, not by
era transitions at z ~ 3000 and z ~ 0.3.)

================================================================================
3. HORN 2 -- CONTENT-RESPONSE IS INDUCED EINSTEIN (NOT IMPORTED GR)
================================================================================
3.1 What the data demand. The observed n(z) runs 2 (BBN/CMB era) -> 1.5
(matter era) -> ~0.5 (today). The transitions happen at the redshifts where
the dominant ENERGY COMPONENT changes (radiation/matter equality; matter/
vacuum-sector equality). So the effective metric must be a functional not of
the coarsening geometry alone but of the CONTENTS -- rho_r, rho_m, rho_vac
fractions. This is a data-forced structural statement, independent of any
theory. [STRUCT]

3.2 The Ward identity closes the argument. [THM]
In CCEF the metric and the graviton are the SAME correlator object at zeroth
and first order (delta g_ij ~ A1 d_i n d_j n, Reference Sec 6). The composite
graviton is massless because the emergent diffeomorphism Ward identity ties
its self-energy to the conserved matter stress tensor -- that identity is
verified [SOLID] and is not optional: it is what makes the gravity sector
healthy. But the SAME identity fixes, at zeroth order, HOW the correlator-
built metric responds to a homogeneous <T_munu>: the response kernel is the
induced Einstein tensor with the induced Newton constant (Sakharov) --
   G_munu[g_corr] = 8 pi G_ind <T_munu>   (verified in-theory to 5.8e-16).
A correlator metric that responded to the contents any OTHER way would break
the identity that keeps the graviton massless: one cannot have the CCEF
graviton and a non-Einstein background response from the same correlator.
CONCLUSION: the only content-responsive a(t) available to CCEF is the
induced-Einstein (emergent Friedmann) one. It is not imported: GR's role here
is played by a consistency condition the theory already proved about itself.
[THM]

3.3 The dichotomy, stated once. [THM]
Either the metric-defining correlators see only the coarsening structure
(one length => power law => excluded, Sec 2), or they see the contents
(=> induced Einstein => resume item M). There is no third construction:
any functional of the state either evolves through xi(t) alone or it does
not; if it does not, its extra time-dependence enters through densities,
and the Ward identity dictates the coupling.

================================================================================
4. WHAT THE COHERENCE-PATCH PICTURE BUYS (real gains, kept)
================================================================================
Folding the no-wall ontology into the induced-Einstein branch removes two of
its four load-bearing problems' worth of structure:
  * M3 (Z2 wall problem) DISSOLVES: within one coherence patch n_3 is aligned
    BY DEFINITION of coherence; the easy-axis Z2 walls exist only where
    independent patches meet -- beyond the observable region. No percolated
    wall network inside our patch; the sigma^{1/3} = 154 MeV vs 1 MeV
    Zel'dovich crisis of item M simply does not arise.               [STRUCT]
  * UNIFORMITY IS COHERENCE: the observable universe is, by construction, one
    correlated region -- large-scale homogeneity needs no inflation and no
    tuning; it is what "a coherence patch" means.                    [STRUCT]
Remaining opens of the surviving branch (unchanged from item M):
  M1. Induced-G magnitude: M* ~ 0.1 GeV vs M_Pl (G_ind/G_N ~ 1.6e40), log-only
      in A3. THE decisive calculation: can the Lorentz-invariant non-local UV
      completion (Reference Sec 9) supply M* ~ M_Pl?                  [OPEN]
  M2. Lambda_eff: calculable piece U(chi_0) < 0 and ~7e39 x rho_Lambda_obs;
      compute the a0 term with the phase-relative zero (patch minus eternal
      medium) before conceding a second renormalized constant.        [OPEN]
  M4. Perturbation origin: defect/texture-sourced spectra are Planck-excluded
      (< few %); the transition must yield adiabatic, near-scale-invariant
      seeds. Make-or-break for structure formation.                   [OPEN]

================================================================================
5. HONEST STATUS
================================================================================
[THM]
  - Scaling theorem: pure internal coarsening admits ONLY a(t) = (xi/xi_0)^p,
    H = H0(1+z)^{2/p} -- the complete family, all p.
  - Ward-identity closure: a correlator metric that responds to contents must
    respond as induced Einstein, on pain of breaking the graviton's own
    massless-ness identity. The dichotomy has no third horn.
[SOLID/NEG -- computed]
  - Family falsification: best member n = 1.055 (Delta chi2 = +242, theta*
    79x); theta*-member n = 1.577 (Delta chi2 = +2772, t0 = 8.7 Gyr); n = 2
    (BBN member): joint chi2 = 8733.8. No member survives two eras.
[STRUCT -- kept gains]
  - No-wall ontology: M3 dissolved; homogeneity = coherence, no inflation
    needed for uniformity. Both carry to the induced-Einstein branch.
[NEG -- honest scope]
  - This note ends the search for a purely coarsening-geometric a(t). The
    surviving line for CCEF cosmology is single: induced Einstein with the
    coherence-patch ontology, gated by M1 (first), M2, M4.
[OPEN]
  - M1, M2, M4 as above. If M1 fails (M* cannot reach M_Pl), CCEF has no
    viable background cosmology on ANY known construction -- that would be
    the honest end of the cosmology sector, cleanly localized in one number.

================================================================================
6. ONE-PARAGRAPH SUMMARY
================================================================================
In the coherence-patch picture -- local order growing inside an eternal,
mostly disordered continuum, with no wall around us -- the background question
"what is a(t)?" has a complete, two-horned answer. Horn 1: because the Model-A
coarsening state obeys dynamical scaling, it carries exactly one evolving
length xi ~ t^{1/2}, so EVERY metric built from its equal-time correlators is
a pure power law a ~ xi^p, H = H0(1+z)^{2/p}; running the entire family
through the published-covariance machinery kills every member (joint-best
n = 1.055: Delta chi2 = +242 with theta* 79x too large; the theta*-matching
n = 1.577: Delta chi2 = +2772 and an 8.7 Gyr universe; BBN's n = 2: chi2 =
8734) -- the data demand era transitions, which a one-length state cannot
contain. Horn 2: a metric that instead responds to the contents is forced, by
the same emergent-diffeomorphism Ward identity that keeps CCEF's composite
graviton massless, to respond as G_munu = 8 pi G <T_munu> -- induced Einstein,
already verified in-theory to 5.8e-16, so content-response is not imported GR
but the theory's own consistency condition applied at zeroth order. There is
no third option. The coherence-patch ontology survives with two real gains --
the Z2 wall problem dissolves (walls live only where patches meet, beyond the
observable region) and homogeneity is coherence by construction -- leaving
CCEF cosmology a single line gated by three numbers: the induced Planck mass
(M1, decisive and first), the effective vacuum energy with the patch-minus-
medium zero (M2), and an adiabatic perturbation mechanism at the transition
(M4). If M1 fails, the cosmology ends honestly, localized in one calculable
number; if it succeeds, CCEF's background is emergent Friedmann with Kibble
solitons for matter and the transition itself for the hot beginning.
================================================================================
