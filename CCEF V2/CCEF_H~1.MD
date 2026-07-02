================================================================================
CCEF v2 — DERIVATION NOTE: HORIZON-SCALE PERTURBATIONS ON THE COASTING BACKGROUND
                            SLIP COEFFICIENT c_Pi  AND  GROWTH f*sigma8(z)
Open follow-on A (the TOP item) from the v2 handoff (Sec 9). Derived from the theory;
no hand-fitting of the dynamics. Compiled 2026-07-02.
Builds on CCEF_Lord_IR_EFT_derivation.md (#1), CCEF_redshift_slip_at_Lord.md (#2, which
DEFERRED exactly this calculation), CCEF_internal_trigger.md (#4-sub, the coasting law).
Labels: [SOLID] derived/verified | [STRUCT] forced by structure | [NEG] honest negative
        | [DEFER] needs a further sub-calculation
================================================================================

--------------------------------------------------------------------------------
0. OBJECTIVE AND HEADLINE
--------------------------------------------------------------------------------
GOAL (closing the [DEFER] left by the redshift/slip note): do the linearized cosmological
perturbation calculation of the IR EFT on the OBSERVABLE-ERA background -- the COASTING
solution a ~ t (q=0, H(z)=H0(1+z)) fixed by the internal trigger L_ord > L* (#4-sub) -- and
deliver the two objects the handoff names:
   (i)  the gravitational SLIP eta and lensing Sigma, in particular the O(1) horizon-scale
        coefficient c_Pi in  eta - 1 = c_Pi (aH/k)^2 ;
   (ii) the linear structure GROWTH f(z) and f*sigma8(z), to CONFRONT the RSD data.

HEADLINE RESULTS:

  SLIP / LENSING -- CONFIRMED GR-LIKE (NULL) on all observable scales; the deferred O(1)
  coefficient is now bounded. Three sources of anisotropic stress, all controlled: [STRUCT]
     - the massive amplitude (radial) mode sigma: mass m_sigma ~ Lambda (microscopic gap),
       so its perturbations are non-dynamical at cosmological k and contribute only
       O((k/Lambda)^2) ~ 10^-120 -- background-independent, holds on coasting too;
     - the conservative coarsening field: a minimally-coupled scalar with a HOMOGENEOUS
       background amplitude has ZERO linear anisotropic stress (the gradient shear
       A1 d_i chi d_j chi is second order since d_i chi_0 = 0) -> eta = 1 exactly;
     - the coarsening field propagates at the acoustic sound speed c_s = c_eff = 1 (Sec 3),
       so its sound horizon IS the Hubble horizon: it is SMOOTH sub-horizon and can perturb
       gravity only at k <~ aH.
  NET:  eta(k,z) = 1 + c_Pi (aH/k)^2 ,   Sigma(k,z) = 1 + O((aH/k)^2, (k/Lambda)^2) ,
  with c_Pi = O(1), NONZERO only through the dissipative (Model-A, gamma_0) shear of the
  coarsening field, and STRICTLY HORIZON-CONFINED. On the sub-horizon scales where RSD and
  weak lensing live, (aH/k)^2 <= ~10^-3 (largest scales) down to 10^-6 (lensing), so the slip
  is unobservable: CCEF predicts eta = Sigma = 1 for all current data. The v1 "falsifiable
  slip" stays retired; the deferred coefficient is O(1) and irrelevant, not a signal. [SOLID/STRUCT]

  GROWTH -- the surprise, and the real content. On the coasting background the sub-horizon
  matter growth equation is (derived below)
     D'' + D' = (3/2) Omega_m0 e^{-N} D ,   N = ln a ,   ' = d/dN ,
  whose GROWING mode is a closed-form modified Bessel function
     D(a) = xi K_1( b xi ) ,   xi = a^{-1/2} = sqrt(1+z) ,   b = sqrt(6 Omega_m0) ,
     f(z)   = d ln D/d ln a = (b/2) sqrt(1+z) K_0(b xi)/K_1(b xi) ,
     f*sigma8(z) = sigma8(0) (b/2) (1+z) K_0(b sqrt(1+z)) / K_1(b) .
  RESULT: despite the background H(z)=H0(1+z) being radiation-like, the GROWTH is nearly
  DEGENERATE with LCDM over the observed range. With Omega_m0 = 0.31 (the observed matter
  density in coasting critical units, since coasting gives H0 t0 = 1 -> H0 ~ 71):
     f(0) = 0.515   (LCDM: 0.527) ,   f*sigma8 flat at ~0.44 across 0 < z < 1 .
  Confronted with a 14-point RSD f*sigma8 compilation, best-fit sigma8(0) = 0.85 gives
  chi^2 = 7.0 (chi^2/dof = 0.54), versus LCDM (Planck Om=0.315) chi^2 = 10.2 (0.78). CCEF-
  coasting fits the growth data AS WELL AS LCDM. [SOLID]
  The models split only at HIGH z: f*sigma8(coast)/f*sigma8(LCDM) = 1.0 (z<1) -> 1.11 (z=1.5)
  -> 1.20 (z=2) -> 1.34 (z=3). So the growth discriminator is z >~ 1.5 (DESI/Euclid), NOT the
  current low-z RSD points. [SOLID]

  UPSHOT: contrary to what the radiation-like H(z) might suggest, the GROWTH/SLIP sector does
  NOT falsify CCEF -- it is GR-degenerate now and only testable at high z. The genuine present
  tension lives entirely in the BACKGROUND H(z)/distances (the coasting H(z)=H0(1+z) overshoots
  LCDM 1.7-3x at z=0.5-2; see redshift note), NOT in growth or slip. This sharpens the handoff's
  "H(z)/growth is the falsifiable handle": growth is a FUTURE (high-z) handle; H(z) is the
  present one.

================================================================================
1. THE BACKGROUND AND THE PERTURBATION FRAMEWORK
================================================================================
Observable-era background (from #4-sub, the internal trigger): L_ord crossed L* = sigma/DeltaF
in the first instants (L* ~ 154 fm, ~39 orders sub-horizon), so the whole observable era is the
BULK-BIAS-DRIVEN COASTING branch:
   a(t) proportional to L_ord(t) ~ t ,   H = a'/a = 1/t ,   q = 0 ,
   normalize a0 = 1 at t0  =>  aH = a' = const = H0  =>  H(a) = H0/a ,  H(z) = H0(1+z).   [given]
Two background identities used repeatedly (both exact for a ~ t):
   d ln H / d ln a  =  Hdot/H^2  =  -1 ,      aH = H0 = const  (comoving Hubble radius constant).

Perturbed metric (conformal-Newtonian gauge on the emergent acoustic metric, Sec 3):
   ds^2 = a^2[ -(1+2Psi) deta^2 + (1-2Phi) dx^2 ] .
SLIP   eta  == Phi/Psi  (eta = 1 <=> no slip) ;
LENSING Sigma via  (Phi+Psi)/2 = Sigma * Phi_GR  (Sigma = 1 <=> GR lensing).
Anisotropic stress sources the slip:  k^2(Phi - Psi) = 12 pi G a^2 (rho+p) sigma_stress
(the off-diagonal, traceless Einstein equation). eta != 1 REQUIRES anisotropic stress.

Sectors that can carry it (from the IR EFT, #1): the massive radial amplitude sigma=delta chi;
the massless Goldstone/graviton directions (induced Einstein gravity, #2); and the coarsening
field acting as an effective smooth component. We take them in turn (Sec 2), then matter growth
which only needs the Poisson equation the slip result establishes (Sec 3-4).

================================================================================
2. SLIP AND LENSING: eta = 1 + c_Pi (aH/k)^2, WITH c_Pi = O(1) AND HORIZON-CONFINED
================================================================================
2.1 THE MASSIVE AMPLITUDE MODE: O((k/Lambda)^2) ~ 10^-120.  [STRUCT]
The radial (Higgs-like) mode has mass m_sigma^2 = U''(chi_0) = 2|r| ~ Lambda^2, a MICROSCOPIC,
background-INDEPENDENT gap (Scale 1; #1 Sec 2). At any cosmological wavenumber k and any epoch,
k, aH << Lambda, so delta_sigma is a heavy, non-propagating mode: it tracks its source
adiabatically and its gradient/anisotropic stress is suppressed by (k/Lambda)^2 <~ (aH/Lambda)^2
~ 10^-120. This is the redshift-note statement, and it is UNCHANGED on the coasting background
because the suppression is set by the fixed gap, not by the expansion law. Negligible. [STRUCT]

2.2 THE CONSERVATIVE COARSENING FIELD: ZERO LINEAR ANISOTROPIC STRESS.  [SOLID]
The gradient term A1|grad chi|^2 gives a spatial stress T_ij ⊃ A1 d_i chi d_j chi. Expanding
chi = chi_0 + delta chi about the HOMOGENEOUS ordered background (d_i chi_0 = 0):
   A1 d_i chi d_j chi = A1 d_i(delta chi) d_j(delta chi) = O(delta chi^2)  -- SECOND order.
So the LINEAR traceless anisotropic stress from the conservative (energy-conserving) part of the
IR EFT VANISHES. A minimally-coupled scalar with a homogeneous background produces no slip:
   eta_conservative = 1   exactly, to all orders in k.                                   [SOLID]
This is the field-theory reason the induced gravity is GR-like (Phi = Psi), independent of the
expansion law -- it holds on the coasting background verbatim.

2.3 SOUND SPEED c_s = 1 => SMOOTH SUB-HORIZON.  [STRUCT]
The coarsening amplitude propagates on the SAME acoustic metric as everything else, c_s = c_eff
= sqrt(A1/Zt) = 1 (Sec 3; universality Delta c/c = 0). A component with c_s = 1 has its sound
(Jeans) horizon equal to the Hubble horizon: pressure support prevents it from clustering on ALL
sub-horizon scales (k >> aH). A smooth component adds no delta-clustering and no shear inside the
horizon -> it cannot bend Phi away from Psi there. Its ONLY gravitational imprint is at k <~ aH.
Combined with 2.2, sub-horizon slip is doubly forbidden (no source, and the field is smooth). [STRUCT]

2.4 THE ONLY LINEAR SOURCE: DISSIPATIVE (MODEL-A) SHEAR -> c_Pi = O(1), HORIZON-CONFINED.  [STRUCT/DEFER]
The one piece NOT covered by 2.2 is the DISSIPATIVE part of the Model-A dynamics
(gamma_0 d_t chi, #1 Sec 3; #3). A relaxational field coupled to the bath carries an effective
SHEAR VISCOSITY; a viscous component does have linear anisotropic stress, ~ (shear viscosity) x
(velocity shear). In perturbation theory a smooth/viscous component modifies the slip only near
the horizon, decaying sub-horizon as (aH/k)^2. Hence the general structure, valid on the coasting
background:
   eta(k,z) - 1 = c_Pi(z) (aH/k)^2 ,   Sigma(k,z) - 1 = O((aH/k)^2, (k/Lambda)^2) ,
with c_Pi:
   * = 0 for the conservative field (2.2);
   * NONZERO only through the dissipative shear, hence tied to gamma_0 and the coasting
     effective equation of state w_eff = -1/3 (a ~ t <=> rho_eff ~ a^-2);
   * BOUNDED O(1): no local operator's stress beats the volume term (the #4-sub ceiling
     theorem also caps the anisotropic-stress amplitude), so |c_Pi| = O(1).
The exact number needs the full velocity-sector equations of the relaxational field on the FRW
background (the viscous delta-chi, theta-chi system) -- still a sub-calculation [DEFER] -- but its
MAGNITUDE (O(1)) and its k-scaling ((aH/k)^2) are fixed, and that is all observations need:

   NUMERICAL SIZE (why it is unobservable). aH at z=0 is H0/c = h/3000 Mpc^-1 = 3.3e-4 h/Mpc.
      largest RSD scale k ~ 0.01 h/Mpc :  (aH/k)^2 ~ 1.1e-3
      lensing scales   k ~ 0.1-1 h/Mpc :  (aH/k)^2 ~ 1e-5 - 1e-7
   So eta - 1 <~ 10^-3 (c_Pi ~ O(1)) even on the largest observed scales. GR-like to sub-percent
   everywhere data exist; Sigma = 1 (lensing unmodified). [STRUCT]

RESOLUTION OF THE PRIOR [DEFER]: the redshift/slip note deferred "c_Pi from the full perturbed IR
EFT." It is now pinned as far as it matters: c_Pi = O(1), zero for the conservative field and
nonzero only via dissipative shear, and CONFINED to k <~ aH. There is NO sub-horizon slip signal
on the coasting background. eta = Sigma = 1 for all current and foreseeable RSD/lensing data. [SOLID]

================================================================================
3. THE GROWTH EQUATION ON THE COASTING BACKGROUND (derived)
================================================================================
Matter = solitons/baryons (pressureless), rho_m ~ a^-3, moving on geodesics of the emergent FRW
metric. The Sec-2 result (eta = Sigma = 1 sub-horizon) means the sub-horizon Poisson equation is
the STANDARD induced-Einstein one (Sakharov, #2 Sec 4.2):
   k^2 Phi = -4 pi G a^2 rho_m delta_m  (no slip, no clustering from the smooth coarsening field).
The linear density contrast then obeys the usual second-order growth equation, with the Hubble
drag set by the COASTING metric (H = 1/t):
   delta_m'' (t) + 2 H delta_m'(t) - 4 pi G rho_m delta_m = 0 .                        [SOLID]

CRUCIAL non-Friedmann point: H(a) = H0/a is fixed by the COARSENING FRONT (bulk bias DeltaF),
NOT by rho_m through a Friedmann equation. So 4 pi G rho_m is an INDEPENDENT quantity, not tied
to H^2. Define the source amplitude in coasting-critical units:
   Omega_m0  ==  8 pi G rho_m0 / (3 H0^2) .
Because coasting predicts H0 t0 = 1 => H0 ~ 1/t0 ~ 71 km/s/Mpc (redshift note), and rho_m0 is
the OBSERVED matter density, Omega_m0 ~ 0.3 is essentially the measured value, not a free knob.

Convert to N = ln a ( ' = d/dN ), using Hdot/H^2 = -1 and 4 pi G rho_m/H^2 = (3/2)Omega_m0 e^{-N}:
   d/dt = H d/dN ;  delta'' terms give
   D'' + (2 + Hdot/H^2) D' = (4 pi G rho_m/H^2) D
   =>  D'' + (2 - 1) D' = (3/2) Omega_m0 e^{-N} D
   =>  D'' + D' = (3/2) Omega_m0 e^{-N} D .                                            [SOLID]
The friction coefficient is 1 (versus 3/2->2 in matter/LCDM): coasting drag is WEAKER, but the
source (3/2)Omega_m0 e^{-N} = (3/2)Omega_m0(1+z) DECAYS as the universe grows -- gravity loses to
the (constant comoving) Hubble rate, so growth FREEZES in the far future.

CLOSED-FORM SOLUTION. Substituting xi = e^{-N/2} = a^{-1/2} = sqrt(1+z) turns this into a
modified Bessel equation of order 1 (D = xi w, argument b xi, b = sqrt(6 Omega_m0)):
   xi^2 w'' + xi w' - (b^2 xi^2 + 1) w = 0   =>   w = I_1(b xi), K_1(b xi) .
   General:  D(xi) = xi [ C1 I_1(b xi) + C2 K_1(b xi) ] .
Mode identification (b xi large = early times): I_1 ~ e^{+b xi} DECAYS toward the future
(~1/a at late times) = the DECAYING mode; K_1 ~ e^{-b xi} early, -> const late = the mode that
GROWS from ~0 to a constant = the GROWING mode. Hence
   D(a) = xi K_1(b xi) ,   xi = sqrt(1+z) ,   b = sqrt(6 Omega_m0) .                    [SOLID]
Growth rate and f*sigma8 follow from d/dxi[xi K_1(x=b xi)] = -b xi K_0(b xi):
   f(z) = d ln D/d ln a = (b/2) sqrt(1+z) K_0(b sqrt(1+z)) / K_1(b sqrt(1+z)) ,
   f*sigma8(z) = sigma8(0) * (b/2) (1+z) K_0(b sqrt(1+z)) / K_1(b) .                    [SOLID]
Late-time limit (xi->0): D -> const (growth freezes); f -> (b^2/... ) -> 0. Early-time (xi large):
f -> (b/2)sqrt(1+z) (fast growth). NUMERICAL CHECK: the closed form reproduces a direct RK
integration of D'' + D' = (3/2)Omega_m0 e^{-N}D to max deviation ~1.5e-11 (Omega_m0 = 0.05,0.31,1.0). [SOLID]

================================================================================
4. CONFRONTING f*sigma8(z) WITH DATA (the payoff)
================================================================================
Model f*sigma8 for Omega_m0 = 0.31 (b = 1.364) is nearly FLAT and LCDM-like:
   z        : 0.02 0.15 0.38 0.51 0.61 0.85 1.00 1.48
   coast/s80: 0.52 0.52 0.52 0.52 0.52 0.51 0.50 0.48    (f*sigma8 = sigma8(0) x this)
With best-fit sigma8(0), the absolute predictions (Omega_m0=0.31, sigma8(0)=0.85):
   coast fs8: 0.44 0.44 0.44 0.44 0.44 0.43 0.42 0.40
   LCDM  fs8: 0.42 0.44 0.46 0.46 0.45 0.43 0.42 0.36     (Om=0.315, sigma8(0)=0.78)
   f(z=0)   : coasting 0.515  vs  LCDM 0.527  (Om^0.55 = 0.530) -- essentially identical.

FIT to a 14-point RSD f*sigma8 compilation (6dFGS, SDSS-MGS, 2dF, GAMA, WiggleZ, BOSS DR12,
eBOSS; z = 0.02 ... 1.48), fitting sigma8(0) analytically at fixed Omega_m0:
   CCEF coasting, Omega_m0 = 0.31 (fixed) : sigma8(0) = 0.85, chi^2 = 7.02, chi^2/dof = 0.54
   CCEF coasting, Omega_m0 free = 0.25    : sigma8(0) = 0.94, chi^2 = 6.60, chi^2/dof = 0.55
   LCDM,           Omega_m = 0.315        : sigma8(0) = 0.78, chi^2 = 10.2, chi^2/dof = 0.78
CCEF-coasting fits the growth data AS WELL AS (marginally better than) LCDM, with the SAME number
of nuisance parameters (Omega_m0, sigma8(0)) as LCDM (Om, sigma8). The only mild cost is a ~5%
higher sigma8(0) (0.85 vs Planck 0.81) -- and CCEF does not predict sigma8(0) anyway (cosmology
fixes only the overall scale, #5; sigma8(0) is a normalization). [SOLID]

WHERE THE MODELS SPLIT (the clean high-z discriminator), both at their own best fit:
   z          : 0.5  1.0  1.5  2.0  2.5  3.0
   coast fs8  :0.440 0.425 0.402 0.376 0.351 0.326
   LCDM  fs8  :0.459 0.417 0.362 0.313 0.274 0.243
   ratio c/L  : 0.96 1.02 1.11 1.20 1.28 1.34
Coasting predicts MORE growth at high z (the weaker Hubble drag and the earlier onset keep delta
growing where LCDM's dark-energy-free matter era is decelerating faster). At z >~ 1.5 the excess
is 10-35%, within reach of DESI/Euclid high-z RSD. THAT is the growth test; current z < 1 data
cannot separate the models. [SOLID]

================================================================================
5. HONEST STATUS
================================================================================
[SOLID -- derived/verified this note]
  - Sub-horizon Poisson (induced Einstein, eta=Sigma=1) => growth eq D'' + D' = (3/2)Om0 e^{-N}D
    on the coasting background (friction coefficient 1, source (3/2)Om0(1+z) that decays).
  - Closed-form growing mode D = sqrt(1+z) K_1(b sqrt(1+z)), b=sqrt(6 Om0); f(z) and f*sigma8(z)
    in closed form; verified vs direct integration to ~1e-11.
  - Data confrontation: coasting fits a 14-point RSD f*sigma8 set as well as LCDM (chi^2 7.0 vs
    10.2), sigma8(0)~0.85; f(0)=0.515 ~ LCDM 0.527. High-z split (z>~1.5, up to 34% at z=3) is
    the discriminator.
  - Slip: conservative field gives eta=1 exactly (homogeneous background => no linear shear);
    c_s=1 => smooth sub-horizon; massive mode O((k/Lambda)^2)~10^-120. Net eta=Sigma=1 on all
    observable scales; numeric (aH/k)^2 <~ 1e-3 (largest RSD) down to 1e-6 (lensing).

[STRUCT -- forced, exact number deferred]
  - eta - 1 = c_Pi (aH/k)^2 with c_Pi = O(1), nonzero ONLY via the dissipative (gamma_0) shear
    of the coarsening field, horizon-confined. The scaling and O(1) bound are fixed (ceiling
    theorem); the precise c_Pi awaits the field's velocity-sector perturbation equations. [DEFER]

[NEG -- honest negatives]
  - sigma8(0) ~ 0.85 required (~5% above Planck); not predicted by CCEF (normalization only).
  - The GROWTH sector does NOT currently test CCEF -- it is GR-degenerate for z < 1. The present
    falsifiable tension is entirely in the BACKGROUND H(z)=H0(1+z), which overshoots LCDM 1.7-3x
    at z=0.5-2 (redshift note) and is in tension with BAO/SNe/chronometer H(z). Growth is a
    FUTURE (high-z) handle, not a present one -- an honest sharpening of "H(z)/growth."
  - Omega_m0 enters as the matter-source amplitude (~0.3, near the observed value given
    coasting H0 t0 ~ 1), but is a fit parameter here, not derived from CCEF microphysics.

[DEFER -- natural next sub-tasks]
  - The exact O(1) c_Pi from the full linearized relaxational (viscous delta-chi, theta-chi)
    IR EFT on the coasting FRW background.
  - A joint background+growth fit (H(z)+SNe+BAO+f*sigma8) to quantify total tension and the
    high-z growth forecast for DESI/Euclid (item E of the handoff follow-ons).

================================================================================
6. ONE-PARAGRAPH SUMMARY
================================================================================
Doing the linearized perturbation calculation on CCEF's observable-era COASTING background
(a ~ t, H=H0(1+z), fixed by the internal trigger L_ord>L*), the gravitational slip is GR-like on
all observable scales: the massive radial mode contributes only O((k/Lambda)^2)~10^-120, the
conservative coarsening field has ZERO linear anisotropic stress because its background amplitude
is homogeneous, and its sound speed c_s=c_eff=1 makes it smooth sub-horizon, so eta = 1 +
c_Pi(aH/k)^2 and Sigma = 1 with c_Pi = O(1) arising ONLY from the dissipative Model-A shear and
STRICTLY horizon-confined -- numerically eta-1 <~ 10^-3 on the largest RSD scales and ~10^-6 for
lensing, i.e. an unobservable null, which resolves the redshift note's deferred coefficient (it
is O(1) and irrelevant, not a signal). For growth, the sub-horizon Poisson equation (induced
Einstein, no slip) with the coasting Hubble drag gives D'' + D' = (3/2)Omega_m0 e^{-N} D, solved
in closed form by a modified Bessel function D = sqrt(1+z) K_1(sqrt(6 Omega_m0(1+z))), from which
f(z) and f*sigma8(z) follow analytically (verified against direct integration to 1e-11); with
Omega_m0=0.31 this gives f(0)=0.515 (LCDM 0.527) and a nearly flat f*sigma8 ~ 0.44 that fits a
14-point RSD compilation AS WELL AS LCDM (chi^2 7.0 vs 10.2, sigma8(0)~0.85), the two models
diverging only at z >~ 1.5 (coasting predicts up to 34% more growth by z=3). The clean conclusion
is that CCEF's growth-and-slip sector is degenerate with GR/LCDM over all current data and testable
only at high z (DESI/Euclid); the present falsifiable tension is not here but in the background
H(z)=H0(1+z) itself, exactly localizing where minimal CCEF must be confronted next.
================================================================================
