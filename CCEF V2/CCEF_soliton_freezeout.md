================================================================================
CCEF v2 — DERIVATION NOTE: SOLITON FREEZE-OUT HISTORY ON THE COASTING BACKGROUND
The calc that decides the soliton-dark-matter question (turn "0.3 is in range" into a
number, or falsify). Derived from the theory; no hand-fitting.
Compiled 2026-06-29. Builds on CCEF_soliton_relic_abundance.md, CCEF_perturbations_growth.md.
Labels: [SOLID] derived/verified | [STRUCT] structural | [NEG] honest negative (falsification-level)
        | [DEFER] possible rescue, needs new structure
================================================================================

--------------------------------------------------------------------------------
0. THE RESULT UP FRONT
--------------------------------------------------------------------------------
Solving the Boltzmann freeze-out dn/dt = -<sv>(n^2 - n_eq^2) - 3Hn on the CCEF background gives a
clean analytic relic, and it does NOT save the soliton-dark-matter idea -- it OVER-produces:

  RELIC (exact, coasting a~t):  N_inf/N_formed = 2/(2+lambda),   lambda = Gamma_i/H_i (annih. efficiency).
      (radiation-like early phase a~t^1/2 gives 1/(1+2lambda) -- same conclusion.)
  KEY NUMBER:  lambda ~ O(1), because the emergent expansion at the transition is FAST, H_i ~ Lambda,
      NOT gravitationally slowed (no M_Pl suppression). Standard cosmology has Gamma/H ~ <sv> m M_Pl
      ~ 1e13 (efficient freeze-out); CCEF has Gamma/H ~ 1 (INEFFICIENT).
  CONSEQUENCE:  the Kibble over-production F = n_KZM/n_b ~ 5e8 is NOT cleaned up. The symmetric
      soliton relic survives at ~2/3 of formation, so
          Omega_DM/Omega_b ~ F * 2/(2+lambda) ~ 3e8   =>  Omega_DM ~ 1e7   (OVERCLOSURE by ~1e8).
  To instead hit the observed Omega_DM/Omega_b = 5.3 would need lambda ~ 1.9e8 (annihilation 1e8x
  stronger than the theory gives) -- NOT available.

VERDICT: the soliton relic FAILS -- not by scarcity (which was the worry) but by OVER-PRODUCTION.
The coasting/emergent expansion is too fast for annihilation to reduce the Kibble over-production.
So the simple "solitons ARE the dark matter" fix does NOT work at freeze-out; it overshoots
Omega~0.3 by ~8 orders. This also flags an over-closure problem for v1's KZM baryogenesis (the
symmetric relic it never annihilated). Reaching Omega~0.3 requires a DILUTION mechanism or an
annihilation ~1e8x stronger than estimated -- new structure, not present here. Honest "if it fails,
it fails": the soliton dark-matter route, as it stands, is falsified by over-production. [NEG]

================================================================================
1. THE BOLTZMANN EQUATION ON THE COASTING BACKGROUND
================================================================================
Post-formation (T < m, so n_eq is Boltzmann-suppressed -> drop it), on a ~ t (coasting, H = 1/t):
   dn/dt = -<sv> n^2 - 3 H n .
Use the comoving density N = n a^3 = n t^3 and nondimensionalize x = t/t_i (formation at x=1,
N(1)=1 in units of the formed density). With lambda == <sv> n_i t_i = Gamma_i/H_i:
   dN/dx = -lambda N^2 / x^3 .                                                         [SOLID]
Separable -> 1/N_inf = 1 + (lambda/2)(1 - 1/x^2)|_{x->inf} = 1 + lambda/2, hence
   N_inf = 2/(2 + lambda) .                                                            [SOLID, exact]
Numerically confirmed: lambda=1 ->0.667, 3 ->0.400, 10 ->0.167, 100 ->0.0196, 1e4 ->2.0e-4.
The physics: the annihilation integral INT x^-3 dx CONVERGES (fast), so annihilation shuts off
within ~ONE Hubble time of formation and the relic is only mildly suppressed (2/(2+lambda)) unless
lambda is enormous. (Early radiation-like phase a~t^1/2 gives INT x^-3/2 dx = 2, N_inf=1/(1+2lambda)
-- a bit more annihilation, same qualitative conclusion.)

================================================================================
2. THE DECISIVE NUMBER: lambda = Gamma_i/H_i ~ O(1)  (why CCEF differs from WIMPs)
================================================================================
Formation at the ordering transition: soliton density n_i ~ Lambda^3 (one per healing volume),
geometric cross-section <sv> ~ 1/Lambda^2 -> Gamma_i = <sv> n_i ~ Lambda.
Expansion rate there: the coarsening starts with L_ord ~ 1/Lambda, so t_i ~ 1/Lambda and H_i ~ Lambda.
   => lambda = Gamma_i/H_i ~ O(1) .                                                    [SOLID est.]
THE CRUX (structural): in STANDARD cosmology the expansion is gravitationally slowed,
H ~ T^2/M_Pl << T, so Gamma/H ~ <sv> T M_Pl ~ 1e13 >> 1 and annihilation is very efficient (the WIMP
freeze-out that yields tiny relics). In CCEF the expansion at the transition is EMERGENT and FAST,
H ~ Lambda ~ T -- there is NO M_Pl slowdown -- so Gamma/H ~ 1 and annihilation is only marginal. The
absence of a huge Planck mass in the early expansion rate is exactly why CCEF cannot efficiently
annihilate its over-produced defects. [STRUCT]

================================================================================
3. THE RELIC AND THE OVER-CLOSURE
================================================================================
The symmetric soliton relic today = (formed abundance) x N_inf, and the formed abundance is the
Kibble over-production F = n_KZM/n_b ~ 5e8 (v1, Working Directory Sec 11) times the baryon density:
   Omega_DM/Omega_b = F * N_inf = F * 2/(2+lambda).
   lambda=1   -> 3.3e8   (Omega_DM ~ 1.6e7)   OVERCLOSURE
   lambda=10  -> 8.3e7
   lambda=1e3 -> 1.0e6
   lambda=1e8 -> 10       (Omega_DM ~ 0.49)   <- only here does it approach observed
Observed Omega_DM/Omega_b = 5.3. Required lambda = 2F/5.3 - 2 ~ 1.9e8. The theory gives lambda ~ 1.
=> the relic overshoots the observed dark-matter density by ~8 orders of magnitude. [SOLID / NEG]

Note this is the SAME wall v1 hit for baryons (KZM over-produces by 5e8), now shown to persist for
the SYMMETRIC relic: v1 suppressed the NET charge (theta ~ 2e-9) to fix baryons, but that does
nothing to the symmetric defect-antidefect population, which -- per Sec 1-2 -- does NOT annihilate
away on the fast emergent background and therefore over-closes. The freeze-out calc exposes this. [NEG]

================================================================================
4. WHAT COULD RESCUE IT (all require new structure; none is tuning-free yet)
================================================================================
  (a) STRONG DILUTION / entropy injection AFTER freeze-out: a later ordering sub-transition (or
      reheating from the ordering latent heat) that dumps entropy and dilutes all solitons by ~1e8.
      This would need to bring BOTH baryons and DM down together; to leave Omega_DM/Omega_b ~ 5 it
      must act on the ALREADY net-vs-symmetric-separated populations. Deriving a ~1e8 dilution from
      an independent quantity would make it a prediction; choosing it to hit 0.3 would be tuning
      (rejected). [DEFER]
  (b) MUCH STRONGER ANNIHILATION: lambda ~ 1e8 needs <sv> ~ 1e8 x geometric -- e.g. a long-range
      attractive soliton-antisoliton force (Sommerfeld-like enhancement). A specific, checkable
      cross-section question for the Skyrme/Hopf sectors; not generically ~1e8. [DEFER]
  (c) ABANDON symmetric-soliton DM: keep only the NET charge (baryons, Omega~0.05). Then the growth
      sector (which wants Omega_eff~0.3) is NOT supplied by solitons -> CCEF growth needs conventional
      dark matter or is falsified against f*sigma8. This is the honest fallback if (a),(b) fail. [NEG]

================================================================================
5. HONEST STATUS
================================================================================
[SOLID]
  - Coasting-background freeze-out relic N_inf = 2/(2+lambda) (exact; numerically confirmed);
    annihilation freezes within ~1 Hubble time.
  - lambda = Gamma_i/H_i ~ O(1) because the emergent expansion is fast (H_i~Lambda, no M_Pl slowdown)
    -- the structural reason CCEF cannot efficiently annihilate defects, unlike WIMP freeze-out.
  - Omega_DM/Omega_b ~ F * 2/(2+lambda) ~ 3e8 with F~5e8 -> OVERCLOSURE by ~1e8. Hitting 5.3 needs
    lambda~2e8, unavailable.
[NEG -- falsification-level]
  - The simple soliton-dark-matter fix FAILS by OVER-production, not scarcity. The Kibble
    over-production survives the (inefficient) freeze-out and over-closes.
  - Same wall for v1 KZM baryogenesis: the un-annihilated symmetric relic over-closes; theta-
    suppression fixes only the net charge.
[DEFER -- rescues, all new structure]
  - Entropy-dilution epoch (a later ordering sub-transition); or a Sommerfeld-enhanced annihilation
    (~1e8); or accept baryons-only (Omega~0.05) and let growth demand conventional DM / be falsified.

================================================================================
6. ONE-PARAGRAPH SUMMARY
================================================================================
Solving the freeze-out Boltzmann equation on the CCEF background gives the exact comoving relic
N_inf = 2/(2+lambda) with lambda = Gamma_i/H_i the annihilation efficiency at formation; because the
annihilation integral converges, annihilation shuts off within about one Hubble time and only mildly
suppresses the abundance unless lambda is enormous. The decisive number is lambda ~ O(1): CCEF's
emergent expansion at the ordering transition is FAST (H_i ~ Lambda, with no gravitational/M_Pl
slowdown), so Gamma/H ~ 1 -- in stark contrast to standard WIMP freeze-out where H ~ T^2/M_Pl makes
Gamma/H ~ 1e13 and annihilation efficient. With lambda ~ 1 the Kibble over-production F = n_KZM/n_b
~ 5e8 is NOT cleaned up, so the symmetric soliton relic gives Omega_DM/Omega_b ~ F*2/(2+lambda) ~
3e8 -- an over-closure by ~8 orders; reaching the observed 5.3 would need lambda ~ 2e8, which the
theory does not provide. So the soliton-dark-matter fix fails at freeze-out -- by OVER-production,
not scarcity -- and the same wall afflicts v1's KZM baryogenesis, whose symmetric defect relic was
never annihilated. Rescue requires genuinely new structure: a ~1e8 entropy-dilution epoch (e.g. a
later ordering sub-transition), or a ~1e8 Sommerfeld-enhanced annihilation cross-section, or
abandoning symmetric-soliton dark matter and accepting that growth then needs conventional dark
matter (or is falsified against f*sigma8). Honest bottom line, in the theory's own spirit: as it
stands, the soliton dark-matter route is falsified by over-production, and the open question is
whether a first-principles dilution or annihilation-enhancement -- not a tuned one -- can bring the
relic down to Omega~0.3.
================================================================================
