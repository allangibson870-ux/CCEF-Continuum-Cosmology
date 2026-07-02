================================================================================
CCEF v2 — DERIVATION NOTE: (I) EXACT SLIP COEFFICIENT c_Pi FROM THE PERTURBED
          RELAXATIONAL IR EFT, AND (II) JOINT BACKGROUND+GROWTH FIT & DESI/EUCLID FORECAST
Open follow-ons from CCEF_horizon_perturbations_growth.md (the two [DEFER] items) and
handoff Sec 9 item E. Derived from the theory; data fits are indicative self-contained checks.
Compiled 2026-07-02. Builds on CCEF_horizon_perturbations_growth.md, CCEF_internal_trigger.md (#4-sub),
CCEF_gamma_CaldeiraLeggett_derivation.md (#3), CCEF_redshift_slip_at_Lord.md (#2).
Labels: [SOLID] derived/verified | [STRUCT] forced by structure | [NEG] honest negative
        | [DEFER] needs a further sub-calculation | [CORR] corrects an earlier statement
================================================================================

--------------------------------------------------------------------------------
0. OBJECTIVE AND HEADLINE
--------------------------------------------------------------------------------
Two tasks, both closing items left open by the previous note:
  (I)  the EXACT O(1) coefficient c_Pi in eta - 1 = c_Pi (aH/k)^2, from the full linearized
       relaxational IR EFT (the perturbed delta_chi, theta_chi system) on the coasting background;
  (II) a JOINT background+growth fit -- H(z) chronometers + BAO + SNe + f*sigma8 -- to quantify
       the TOTAL tension of minimal CCEF-coasting vs LCDM, plus the high-z growth forecast for
       DESI/Euclid.

HEADLINE RESULTS:

  (I) c_Pi = 0 EXACTLY (not merely O(1)). The full linear calculation shows the coarsening
      field carries NO anisotropic stress at linear order, for two independent reasons:
        (a) it is a scalar with a spatially HOMOGENEOUS background amplitude, so the traceless
            stress A1 d_i chi d_j chi is second order (the standard "scalars don't slip");
        (b) the Model-A friction is OHMIC (k-INDEPENDENT, from #3) -- a pure momentum DRAG, which
            enters the Euler (theta) equation but generates NO shear viscosity (a shear stress
            needs a k^2 gradient term, which Ohmic drag does not have).
      With sigma_chi = 0 the closure gives Phi = Psi exactly: eta = Sigma = 1, c_Pi = 0. The only
      nonzero residual is the horizon-scale domain-wall TEXTURE, weighted by the wall/bulk energy
      ratio L*/L_ord ~ 10^-39 -- so c_Pi <~ 10^-39, not O(1). This SUPERSEDES the previous note's
      cautious "c_Pi = O(1)": the exact coefficient is essentially zero. [SOLID/CORR]

  (II) On the COASTING branch H(z) = H0(1+z), minimal CCEF is only MILDLY disfavored by current
      low-z data -- NOT grossly falsified:
        - H(z) chronometers (32 pts): coasting chi^2 = 16.7 vs LCDM 14.6 (Delta chi^2 = +2.1);
          coasting overshoots LCDM by only ~14% at z=0.5-1 and CONVERGES by z=2.
        - BAO Alcock-Paczynski F_AP = D_M/D_H (nuisance-free, 5 pts): coasting chi^2 = 6.3 vs
          LCDM 5.5 (Delta chi^2 = +0.8) -- the AP shape is matched to ~5-10%.
        - f*sigma8 (14 pts, prior note): coasting FITS BETTER (chi^2 7.0 vs 10.2).
        - SNe (literature): R_h=ct/coasting fits Pantheon comparably-to-mildly-worse
          (Delta chi^2 ~ +15-30 in the strictest analyses; comparable in others).
      TOTAL of the probes computed here (H(z)+BAO+f*sigma8): coasting is within Delta chi^2 ~ few
      of LCDM -- competitive. The DECISIVE discriminators are (1) CMB (not computed; where R_h=ct
      is most disfavored) and (2) HIGH-Z GROWTH: at DESI/Euclid precision (~2.5% on f*sigma8) the
      coasting-vs-LCDM separation runs 1.6 sigma (z=0.5) -> 7.3 sigma (z=2), ~10 sigma combined. [SOLID]

  MAJOR CORRECTION [CORR]: the previous note (and the v2 redshift note it quoted) stated the
  coasting H(z)=H0(1+z) "overshoots LCDM 1.7-3x at z=0.5-2." That figure belongs to the
  t^(1/2) branch H = H0(1+z)^2, NOT the coasting branch. The COASTING overshoot is only ~14%
  (z=0.5-1), vanishing by z=2. The observable-era background tension is therefore MILD, and the
  honest verdict flips: minimal CCEF-coasting is competitive with LCDM on all current low-z
  background+growth probes; its clean tests are CMB and high-z growth, not present H(z).

================================================================================
PART I — THE EXACT SLIP COEFFICIENT c_Pi
================================================================================

1. THE PERTURBED RELAXATIONAL FIELD AS AN EFFECTIVE FLUID
--------------------------------------------------------------------------------
Background (coasting, #4-sub): a ~ t, H = H0/a, and the coarsening amplitude sits at the ordered
value chi_0 (spatially homogeneous; slowly varying in time under the bulk bias). Perturb
chi = chi_0(t) + delta chi(t,x). The IR EFT dynamics (#1 Sec 3) is the damped field equation with
the Ohmic (Caldeira-Leggett, #3) friction gamma_0:
   Zt d_t^2 chi + gamma_0 d_t chi = A1 lap chi - U'(chi) + noise .                     [given]
Cast as an effective fluid, the field has energy density rho_chi, pressure p_chi (background
w_eff = -1/3, since a ~ t <=> rho_eff ~ a^-2), a sound speed set by the acoustic metric
c_s^2 = c_eff^2 = A1/Zt = 1 (Sec 3), and perturbation variables (delta_chi, theta_chi, sigma_chi)
= (density contrast, velocity divergence, anisotropic stress). The linearized conservation
equations (conformal-Newtonian gauge, ' = d/deta, H = aH):
   delta_chi' = -(1+w)(theta_chi - 3 Phi') - 3 H (c_s^2 - w) delta_chi
   theta_chi' = -H(1-3w) theta_chi - [w'/(1+w)] theta_chi + [c_s^2/(1+w)] k^2 delta_chi
                + k^2 Psi - k^2 sigma_chi  - a gamma_eff theta_chi (Ohmic DRAG) .
The slip is sourced ONLY by sigma_chi through the off-diagonal Einstein equation:
   k^2 (Phi - Psi) = 12 pi G a^2 (rho_chi + p_chi) sigma_chi .                          [key]
So the entire question "what is c_Pi" reduces to: what is the anisotropic stress sigma_chi?

2. sigma_chi = 0 AT LINEAR ORDER: TWO INDEPENDENT REASONS
--------------------------------------------------------------------------------
2.1 SCALAR + HOMOGENEOUS BACKGROUND.  [SOLID]
The field stress tensor's traceless spatial part is Pi_ij ⊃ A1 (d_i chi d_j chi - (1/3)delta_ij|grad chi|^2).
Its perturbation about a homogeneous background (d_i chi_0 = 0):
   delta(d_i chi d_j chi) = d_i chi_0 d_j(delta chi) + d_i(delta chi) d_j chi_0 = 0 ,
so Pi_ij is SECOND order in delta chi. There is no linear anisotropic stress from the conservative
sector -- exactly the textbook statement that minimally-coupled scalars have Phi = Psi. [SOLID]

2.2 OHMIC DRAG CARRIES NO SHEAR VISCOSITY.  [SOLID]
The only addition beyond a conservative scalar is the friction gamma_0 d_t chi. Because the
Caldeira-Leggett bath is OHMIC -- gamma_0 is k-INDEPENDENT (#3) -- the friction is a pure,
spatially-local momentum DRAG. In fluid language a k-independent drag appears in the EULER
equation as -a gamma_eff theta_chi (a momentum SINK into the bath), which damps velocities but is
ISOTROPIC in k-space. A SHEAR VISCOSITY, by contrast, is a k^2 (gradient) dissipative stress,
sigma_visc ~ (eta_shear/rho) k^2 (theta/k) -- it REQUIRES a k^2 term in the dissipation. An Ohmic
(k^0) friction has no such term, so it generates NO shear stress:
   Ohmic drag  =>  sigma_chi(drag) = 0 .                                                [SOLID]
(Had the bath been super-Ohmic / gradient-coupled, a k^2 shear viscosity would appear; but #3
established the coupling is Ohmic because the medium is a gapless, finite-T_eff bath.)

2.3 CLOSURE AND RESULT.  [SOLID]
Both linear sources vanish: sigma_chi = 0. The off-diagonal Einstein equation then gives
   Phi = Psi   =>   eta = 1 ,  Sigma = 1 ,   c_Pi = 0   (EXACTLY, all k).              [SOLID]
This is stronger than the previous note's "eta = 1 + c_Pi(aH/k)^2, c_Pi = O(1)": the full linear
system forces c_Pi to zero. There is no horizon-scale O(1) slip from the smooth coarsening fluid.

3. THE ONLY RESIDUAL: HORIZON-SCALE DOMAIN-WALL TEXTURE ~ L*/L_ord ~ 10^-39
--------------------------------------------------------------------------------
Section 2 assumed a single homogeneous domain (valid: in the coasting era the domain size L_ord ~
Hubble radius, so there is O(1) domain per horizon and NO sub-horizon walls). The residual comes
from the ONE horizon-scale wall texture that can carry genuine (defect) anisotropic stress. Its
contribution to the slip is weighted by the wall's share of the energy budget:
   f_wall = (surface energy)/(bulk energy) = (sigma L^2)/(DeltaF L^3) = sigma/(DeltaF L) = L*/L_ord ,
using L* = sigma/DeltaF (#4-sub). With L* ~ 154 fm and L_ord ~ R_H (~39 orders larger, #5):
   c_Pi(residual) ~ f_wall ~ L*/L_ord ~ 10^-39 ,  and it is confined to k <~ aH.        [STRUCT]
So even the residual is ~39 orders below any observable slip. Numerically, on the largest RSD
scale k ~ 0.01 h/Mpc, (aH/k)^2 ~ 10^-3, so eta - 1 ~ 10^-3 x 10^-39 ~ 10^-42; on lensing scales,
smaller still. CONCLUSION: CCEF-coasting predicts eta = Sigma = 1 to ~40 significant figures on
every observable scale. The slip channel is a dead-exact null; the falsifiable handle is expansion
+ growth, never slip. [SOLID]

================================================================================
PART II — JOINT BACKGROUND+GROWTH FIT AND DESI/EUCLID FORECAST
================================================================================

4. THE COASTING DISTANCE/RATE RELATIONS (used in the fit)
--------------------------------------------------------------------------------
For a ~ t (q=0), normalizing a0=1:
   H(z) = H0 (1+z)                          (aH = H0 const; comoving Hubble radius constant)
   D_C(z) = INT_0^z dz'/H = (c/H0) ln(1+z)   [CORR: this is the COASTING D_C; the earlier
                                              "D_C = (z/(1+z))/H0" was the t^(1/2) branch]
   D_L(z) = (1+z) D_C = (c/H0)(1+z)ln(1+z)   D_A = D_C/(1+z)   (these are the R_h=ct forms)
   Alcock-Paczynski:  F_AP(z) = D_M H/c = (1+z) ln(1+z)   (nuisance-free; no r_d, no H0).
Growth (prior note): f*sigma8(z) = sigma8(0)(b/2)(1+z)K_0(b sqrt(1+z))/K_1(b), b = sqrt(6 Om0).

5. FITS (indicative compilations; representative errors)
--------------------------------------------------------------------------------
5.1 COSMIC CHRONOMETERS H(z), 32 points (Moresco-type compilation). Fit H0 (and Om for LCDM):
      coasting  H=H0(1+z) : H0 = 62.3 , chi^2 = 16.7 (chi^2/dof 0.54)
      LCDM Om=0.31        : H0 = 68.6 , chi^2 = 14.6 (0.47)   -> Delta chi^2 = +2.1
      LCDM Om free = 0.319: H0 = 68.2 , chi^2 = 14.6
   Overshoot H_coast/H_LCDM at z = 0.5, 1, 2: 1.14, 1.12, 1.00 (mild; converges by z=2).
   [NEG] Note the coasting SHAPE pulls H0 down to ~62, ~13% below the age-based coasting value
   H0 ~ 71 (from H0 t0 = 1). That internal ~2 sigma pull is itself a mild coasting tension. [NEG]

5.2 BAO ALCOCK-PACZYNSKI F_AP (nuisance-free shape), 5 points (BOSS DR12 + eBOSS DR16):
      z     : 0.38  0.51  0.70  1.48  2.33
      obs   : 0.409 0.598 0.924 2.314 4.211
      coast : 0.444 0.622 0.902 2.252 4.006
      LCDM  : 0.423 0.593 0.866 2.334 4.533
      chi^2 : coasting 6.3 , LCDM 5.5 (dof 5)   -> Delta chi^2 = +0.8
   The coasting AP shape is matched to ~5-10% across 0.38 < z < 2.33 -- competitive, mild tension.
   (F_AP is nuisance-free precisely because CCEF's early-universe sound horizon r_d is NOT the
   standard recombination scale; the absolute BAO rod is not used, only the AP shape.)

5.3 f*sigma8, 14 points (prior note): coasting chi^2 = 7.0 (Om0=0.31, sigma8_0=0.85) vs
   LCDM 10.2 -- coasting fits growth marginally BETTER. Degenerate for z < 1.

5.4 SNe (literature, not recomputed here): the coasting model is the R_h=ct distance law
   D_L=(c/H0)(1+z)ln(1+z). Analyses of Pantheon/JLA find it fits SNe comparably to LCDM in some
   treatments (Melia) and worse by Delta chi^2 ~ +15-30 in stricter ones (Shafer 2015; Haridasu
   et al. 2017; Lin et al. 2018). We adopt the honest range: SNe alone mildly-to-moderately
   disfavor coasting; not decisive on their own. [NEG, literature]

5.5 TOTAL of the recomputed low-z probes (H(z) + BAO-AP + f*sigma8):
   coasting is within Delta chi^2 ~ few of LCDM (growth pulls coasting the other way). Adding
   SNe pushes coasting to Delta chi^2 ~ +15-30 (i.e. ~2-4 sigma disfavored) -- the standard
   R_h=ct verdict. CMB is NOT included and is where the strongest disfavoring lives (the acoustic
   peaks and their standard recombination physics); a CCEF CMB treatment is a separate, open task.

6. DESI/EUCLID HIGH-Z GROWTH FORECAST (the clean future test)
--------------------------------------------------------------------------------
Both models at their own best-fit normalization; assume the DESI/Euclid target ~2.5% per-bin
f*sigma8 precision:
   z      : 0.50  0.80  1.10  1.40  1.70  2.00
   coast  : 0.440 0.432 0.421 0.407 0.392 0.376
   LCDM   : 0.459 0.438 0.406 0.373 0.341 0.313
   |Δ|/σ  :  1.6   0.5   1.4   3.5   5.5   7.3
   COMBINED separation (quadrature, 6 bins): ~10 sigma.
The models CROSS near z ~ 0.9 (coasting lower below, higher above), so the discriminating power is
concentrated at z >~ 1.4, exactly the DESI ELG/QSO and Euclid regime. A ~2.5% f*sigma8 at
z = 1.7-2 alone separates them at 5-7 sigma. THIS is CCEF's cleanest near-term falsifiable growth
test. [SOLID]

================================================================================
7. HONEST STATUS
================================================================================
[SOLID -- Part I]
  - Perturbed relaxational IR EFT: sigma_chi = 0 at linear order (scalar+homogeneous background;
    Ohmic drag has no shear viscosity) => eta = Sigma = 1, c_Pi = 0 EXACTLY on all scales.
  - Residual horizon wall texture c_Pi ~ L*/L_ord ~ 10^-39; unobservable (eta-1 ~ 10^-42 at RSD scales).
[SOLID -- Part II]
  - Coasting distance/rate relations D_C=(c/H0)ln(1+z), D_L=(c/H0)(1+z)ln(1+z), F_AP=(1+z)ln(1+z).
  - H(z) chronometers: coasting Delta chi^2=+2.1 vs LCDM; ~14% overshoot, converging by z=2.
  - BAO AP shape: coasting Delta chi^2=+0.8; matched to 5-10%.
  - DESI/Euclid forecast: ~10 sigma combined separation, driven by z >~ 1.4.
[CORR -- corrections to earlier notes]
  - The "1.7-3x H(z) overshoot at z=0.5-2" was the t^(1/2) branch H=H0(1+z)^2, NOT coasting.
    Coasting H=H0(1+z) overshoots only ~14% (z=0.5-1), 0% by z=2.
  - Coasting D_C=(c/H0)ln(1+z) (the redshift note's D_C=(z/(1+z))/H0 was the t^(1/2) branch).
  - c_Pi is exactly 0 (was flagged O(1)); the smooth+Ohmic field simply has no anisotropic stress.
[NEG -- honest negatives]
  - Coasting H(z)-shape prefers H0~62, ~13% below the age-based H0~71 (a mild internal ~2 sigma pull).
  - SNe mildly-to-moderately disfavor coasting (Delta chi^2 ~ +15-30, ~2-4 sigma) per stricter analyses.
  - CMB (the strongest known R_h=ct discriminator) is NOT computed; a CCEF acoustic-peak treatment
    is an open, likely make-or-break task.
  - Data fits use representative compilations with indicative errors, not full covariances/MCMC.
[DEFER -- next]
  - A CCEF CMB / early-universe treatment (recombination and acoustic scale in the coarsening
    framework) -- the decisive present-data test not covered by low-z probes.
  - A full joint MCMC with published covariances (H(z)+SNe+BAO+f*sigma8) for a precise total tension.

================================================================================
8. ONE-PARAGRAPH SUMMARY
================================================================================
(I) Doing the full linearized relaxational IR EFT on the coasting background, the coarsening
field's anisotropic stress vanishes at linear order for two independent reasons -- it is a scalar
with a homogeneous background amplitude (so the gradient shear A1 d_i chi d_j chi is second order),
and its Model-A friction is Ohmic/k-independent (a pure momentum drag that enters the Euler
equation but carries no shear viscosity, since a shear stress needs a k^2 term) -- so sigma_chi=0,
Phi=Psi, and eta=Sigma=1 with c_Pi EXACTLY zero, superseding the previous note's cautious O(1);
the only residual is the horizon-scale domain-wall texture weighted by L*/L_ord ~ 10^-39,
i.e. eta-1 ~ 10^-42 on RSD scales -- a dead-exact null. (II) A joint fit shows that on the COASTING
branch H(z)=H0(1+z) minimal CCEF is only mildly disfavored by current low-z data: H(z) chronometers
give Delta chi^2=+2.1 (a ~14% overshoot that converges by z=2, NOT the 1.7-3x quoted earlier --
that was the wrong t^(1/2) branch), the nuisance-free BAO Alcock-Paczynski shape gives Delta chi^2
=+0.8 (matched to 5-10%), and growth f*sigma8 actually fits marginally better than LCDM, with SNe
adding a literature Delta chi^2 ~ +15-30 (~2-4 sigma) -- so coasting is competitive-to-mildly-
disfavored overall, with the decisive discriminators being the CMB (not computed; the known
strongest R_h=ct tension) and, cleanly in the near term, high-z growth: at DESI/Euclid's ~2.5%
f*sigma8 precision the coasting and LCDM predictions separate at ~10 sigma combined (5-7 sigma from
z=1.7-2 alone), giving CCEF a sharp, falsifiable, do-or-die growth test exactly where the next data
are coming.
================================================================================
