================================================================================
CCEF v2 — DERIVATION NOTE: HORIZON-SCALE PERTURBATIONS -> SLIP + GROWTH f*sigma8(z)
Top open follow-on after the v2 priority list (Sec 9 item A). Derived from the theory;
no hand-fitting; the only gravity used is the DERIVED induced-Einstein IR (Sakharov),
NOT imported GR/Friedmann. Compiled 2026-06-29.
Builds on CCEF_internal_trigger.md (coasting), CCEF_redshift_slip_at_Lord.md, CCEF_priority5.
Labels: [SOLID] derived/verified | [STRUCT] forced by structure | [NEG] honest negative
        | [INPUT] effective input (flagged), not a new fit beyond what any cosmology needs
================================================================================

--------------------------------------------------------------------------------
0. WHAT THIS DELIVERS
--------------------------------------------------------------------------------
The redshift/slip note left two items for the linearized theory on the coasting background
(a ~ t, H = 1/t): the horizon-scale SLIP coefficient, and the growth of structure f*sigma8(z).
Both are done here.

HEADLINE:
  SLIP: eta = Sigma = 1 (GR-like) at ALL observable scales, INCLUDING the horizon. The clustering
    matter (solitons = baryons/defects) is pressureless (no anisotropic stress), and the order-
    parameter field perturbations that could carry anisotropic stress are negligible -- the
    amplitude mode is gapped (m_sigma huge -> relaxes instantly) and the Goldstone modes dilute as
    a^-4. So the horizon-scale coefficient I previously flagged is ~0: eta-1 = O(Omega_Gold/Omega_m)
    ~ a^-1 -> 0. No cosmological modified-gravity slip signal. [SOLID / STRUCT]

  GROWTH: on the coasting background the DERIVED induced-Einstein IR gravity gives the standard
    sub-horizon growth equation, but with H=1/t set by COARSENING (not Friedmann) and the source
    DECOUPLED from H^2:
        delta'' + (2/x) delta' - (eps/x^3) delta = 0 ,   x=t/t0,  eps = 4 pi G rho_m0 t0^2 = (3/2)Omega_eff .
    Solving it:
      * If the clustering density is BARYONS ONLY (Omega_b~0.05, eps~0.075): f*sigma8 ~ 0.13-0.19,
        ~3x BELOW the observed ~0.40-0.48. CCEF-with-baryons-only badly UNDER-produces structure.
        => the growth data INDEPENDENTLY demand an Omega_eff ~ 0.3 clustering component. [NEG -> INPUT]
      * If Omega_eff ~ 0.3 (eps~0.45; a soliton/defect "dark matter", the SAME density LCDM needs):
        f*sigma8(z) ~ 0.40, essentially FLAT over z=0-1, and f(z=0)~0.50 -- a good match to RSD data
        and very close to LCDM, but with a DISTINCTIVE flatter shape (no mid-z peak). [SOLID shape]
  So structure growth points to the same Omega_m~0.3 as LCDM (not a new CCEF fit -- it is the matter
  density any cosmology needs), and, given it, predicts a flat f*sigma8~0.40 -- falsifiable against
  LCDM's slightly peaked shape at future precision.

================================================================================
1. PERTURBATION SETUP ON THE COASTING BACKGROUND
================================================================================
Background (derived): emergent metric ds^2 = -dt^2 + a^2 dx^2, a ~ t (coasting, from the internal
trigger L*), H = 1/t. Scalar perturbations Phi, Psi (longitudinal gauge). Field content and its
cosmological role:
  * AMPLITUDE mode delta_chi: mass^2 = U''(chi_0) = m_sigma^2, the GAP-SCALE stiffness. Linearized
    (overdamped Model A): gamma_0 d_t delta_chi = A1 lap delta_chi/a^2 - m_sigma^2 delta_chi + (metric).
    For any cosmological k, k/a << m_sigma, so the mass term dominates -> delta_chi relaxes on the
    microscopic time gamma_0/m_sigma^2, i.e. it tracks equilibrium ADIABATICALLY and does NOT grow
    and does NOT cluster. [SOLID]
  * GOLDSTONE (phase) modes: gapless, relativistic (z=1). Energy density redshifts like radiation,
    rho_Gold ~ a^-4 -> negligible at late times. [SOLID]
  * SOLITONS (baryons/defects): conserved topological charges -> number density n ~ a^-3, they are
    the pressureless CLUSTERING component (the "matter" of CCEF). [SOLID]
So the ONLY component that clusters and grows is the pressureless soliton fluid; the field itself is
inert cosmologically (amplitude gapped, Goldstones diluting). This single fact drives both results.

================================================================================
2. THE SLIP AT HORIZON SCALE: eta = Sigma = 1
================================================================================
The IR gravity is induced Einstein (Sakharov; Reference Sec 6, massless healthy z=1 graviton).
Einstein gravity sourced by a component with NO anisotropic stress gives Phi = Psi, i.e. eta = 1.
Anisotropic-stress sources here:
  * solitons: pressureless -> zero anisotropic stress. [SOLID]
  * amplitude field: gapped/relaxing -> negligible perturbation, negligible stress. [SOLID]
  * Goldstones: relativistic (could carry stress) BUT rho_Gold/rho_soliton ~ a^-4/a^-3 = a^-1 -> 0.
Hence the residual horizon-scale slip is bounded by the Goldstone-to-matter density ratio:
   eta(k~H) - 1  =  O( Omega_Gold/Omega_m )  ~  a^-1  ->  0  (and the static piece is O((k/Lambda)^2)~1e-120).
CONCLUSION: eta = Sigma = 1 to high precision at ALL observable scales, horizon included. The
horizon-scale coefficient flagged in the redshift/slip note is therefore ~0. CCEF cosmology has NO
modified-gravity slip signature; lensing and dynamics agree (Sigma=1). The genuine cosmological
signal is entirely in the EXPANSION+GROWTH, not in slip. [SOLID / STRUCT]

================================================================================
3. THE GROWTH EQUATION (non-GR background, derived IR gravity)
================================================================================
Sub-horizon, the induced-Einstein Poisson equation lap Phi = 4 pi G a^2 delta_rho (with the DERIVED
induced G) plus mass+momentum conservation of the pressureless solitons gives the standard growth
equation -- but on the COASTING background and with the source NOT tied to H^2:
   d^2 delta/dt^2 + 2H d(delta)/dt - 4 pi G rho_m delta = 0 ,   H = 1/t (coasting, NON-Friedmann).
Solitons conserve number: rho_m = rho_m0 (a0/a)^3 = rho_m0 (t0/t)^3. Nondimensionalize x = t/t0
(a ~ x, 1+z = 1/x) and define the ONLY parameter
   eps == 4 pi G rho_m0 t0^2 = (3/2) Omega_eff ,   Omega_eff == 8 pi G rho_m0/(3 H0^2) (clustering today).
   =>   delta'' + (2/x) delta' - (eps/x^3) delta = 0 .                                 [SOLID]
NON-GR content, stated plainly: H=1/t is fixed by coarsening, and eps (the source) is INDEPENDENT
of the background rate -- there is no Friedmann constraint linking rho_m to H. Late-time behavior:
the source eps/x^3 falls faster than the friction 2/x, so delta -> const (growth FREEZES) and
f = dln delta/dln a -> 0 in the far future; today (x=1) we are still in the growing tail.

================================================================================
4. RESULTS: f*sigma8(z)  (sigma8_0 = 0.8, numerically solved)
================================================================================
   MODEL                                z=0.0  0.3  0.5  1.0  1.5
   CCEF eps=0.075 (baryons only, Om=0.05) f*s8: 0.13 0.14 0.15 0.18 0.19   [3x too low -> NEEDS DM]
   CCEF eps=0.45  (Om_eff=0.30)           f*s8: 0.40 0.41 0.41 0.40 0.38   [FLAT ~0.40; good]
   CCEF eps=1.0   (Om_eff=0.67)           f*s8: 0.65 0.60 0.57 0.48 0.41   [too high at z=0; f>1]
   LCDM Om=0.30 (reference)               f*s8: 0.41 0.46 0.46 0.43 0.37
   OBSERVED (RSD surveys, orientation)    f*s8: ~0.40-0.48 (roughly FLAT) over z=0-1
Reading:
  (a) BARYONS-ONLY FAILS: eps~0.075 gives f*sigma8 ~ 3x below data. Structure growth INDEPENDENTLY
      requires a clustering Omega_eff ~ 0.3 -- exactly the "matter density" LCDM needs. In CCEF this
      must be a SOLITON/defect dark-matter component (baryons ~0.05 are far too few). [NEG -> INPUT]
  (b) WITH Omega_eff ~ 0.3: CCEF coasting gives f*sigma8 ~ 0.40, essentially FLAT across z=0-1, with
      f(z=0) ~ 0.50 (LCDM: 0.51). A viable match, and DISTINCT from LCDM in SHAPE -- LCDM peaks mildly
      near z~0.4-0.5 (0.46) then declines, whereas CCEF is flat (no peak). [SOLID shape prediction]
  (c) f CAN EXCEED 1 for large eps (weak-friction coasting + source not capped by H^2) -- a
      qualitative CCEF signature absent in LCDM (where f = Omega_m(z)^0.55 <= 1). [STRUCT]

================================================================================
5. HONEST STATUS
================================================================================
[SOLID / STRUCT]
  - Amplitude mode gapped (inert); Goldstones dilute (a^-4); solitons are the pressureless
    clustering matter. From this: eta = Sigma = 1 at all observable scales incl. horizon
    (slip coefficient ~0). No MG slip signal.
  - Growth equation on the coasting background from the DERIVED induced-Einstein gravity (not GR):
    delta'' + (2/x)delta' - (eps/x^3)delta = 0; late-time freezing.
  - With Omega_eff~0.3: f*sigma8 ~ 0.40 FLAT over z=0-1, close to LCDM and data; distinctive flat
    (no-peak) shape; f can exceed 1. Numerically solved.

[NEG / INPUT]
  - Baryons-only (Omega_b~0.05) UNDER-produces growth ~3x. CCEF must supply a soliton/defect DARK-
    MATTER component with Omega ~ 0.25 to match f*sigma8. This is the SAME matter density any
    cosmology needs (not a new CCEF fit), but it is an INPUT here: the soliton/defect relic abundance
    must be DERIVED from baryogenesis / the Kibble mechanism (Reference Sec 10-11) -- not done here.
    If that abundance cannot reach Omega~0.3, CCEF growth is falsified. This is the sharp open issue.
  - Omega_eff enters only through the source; the coasting EXPANSION (a~t, H0 t0=1) is unchanged by it
    (non-Friedmann) -- so CCEF does NOT need Omega to "close" the universe, unlike GR. Structure and
    expansion are decoupled, which is itself a distinctive, testable feature.

[DEFER]
  - Derive the soliton/defect relic Omega from the ordering transition (Kibble + the derived
    second-order/weak transition) -> tests whether Omega_eff~0.3 is achievable from first principles.
  - Full k-dependent transfer function / CMB (needs the early ordering era + horizon crossing) --
    beyond this sub-horizon growth calc.

================================================================================
6. ONE-PARAGRAPH SUMMARY
================================================================================
On the coasting background (a~t, H=1/t), the only cosmologically active perturbations are the
pressureless solitons (baryons/defects): the amplitude mode is gap-stiff and relaxes instantly, and
the Goldstones dilute as a^-4. Consequently the gravitational slip is eta=Sigma=1 (GR-like) at all
observable scales including the horizon -- the previously-flagged horizon coefficient is ~0
(bounded by Omega_Gold/Omega_m ~ a^-1) -- so CCEF has no modified-gravity slip signal and its
falsifiable cosmology lives in expansion+growth. Using the DERIVED induced-Einstein IR gravity (not
imported GR) the sub-horizon growth obeys delta'' + (2/x)delta' - (eps/x^3)delta = 0 with H=1/t set
by coarsening and the source eps=(3/2)Omega_eff DECOUPLED from H^2; growth freezes in the far
future. Solving it: baryons alone (Omega~0.05) under-produce structure ~3x, so the growth data
independently demand Omega_eff~0.3 -- a soliton/defect dark matter, the same density LCDM's "matter"
supplies; given it, CCEF predicts f*sigma8~0.40 essentially FLAT across z=0-1 (f(z=0)~0.50), a
viable match that is distinct from LCDM's mildly peaked shape and can even give f>1. The honest open
issue is whether the soliton/defect relic abundance can actually reach Omega~0.3 from the ordering
(Kibble) transition -- a first-principles baryogenesis calculation that would turn this required
input into a prediction (or falsify the growth sector). Notably, because expansion and clustering
are decoupled in CCEF, Omega is NOT needed to close the universe -- a clean structural difference
from GR.
================================================================================
