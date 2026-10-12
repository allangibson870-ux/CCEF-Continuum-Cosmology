# Matter–antimatter asymmetry in the grain universe (2026-10-12)

**Code:** `ccef_baryogenesis.py` → `ccef_baryogenesis_output.txt` (order-of-magnitude estimates).

**Target:** η_B = 6.1×10⁻¹⁰, i.e. Y_B = n_B/s = 8.7×10⁻¹¹.

**Sakharov's conditions:** baryon-number violation, C/CP violation, departure from equilibrium.

**Branch L₃ inputs:**
- ℤ₃ lepton triality forbids ΔL = 1, 2, but allows ΔL = 3, electroweak sphalerons (ΔB = ΔL = 3) and **ΔB = 2, ΔL = 0** (the six-quark uddudd junction);
- crossover Λ* ≈ 7.7×10¹⁰ GeV;
- T_max ≲ 0.95 Λ* (monopoles);
- Dirac Yukawa y ≈ 2.9×10⁻¹³ from the grain dilution of ν^c, which dilutes **every** vertex containing ν^c.

## Mechanisms
| Mechanism | Branch L₃ | Why |
|---|---|---|
| **A. Standard (Majorana) leptogenesis** | **forbidden** | needs ΔL = 2; ℤ₃ forbids it. *(Works in Branch M in the usual way: M_N ≳ 10⁹ GeV ≤ T_max.)* |
| **B. Dirac leptogenesis** | **fails by ~10¹⁵–10¹⁷** | The "hiding" condition is met (y ≪ 10⁻⁸: ν_R never equilibrates). But the parent's decay channel into L ν^c is diluted like every ν^c vertex: branching ≲ 10⁻²⁵, so Y_B ≲ 10⁻²⁸. Using the heavy grain modes of ν^c as the parent also fails: they live ~3×10⁻⁹ s and decay at T ≈ 14 GeV, after sphalerons stop (132 GeV). **The dilution that makes Dirac neutrinos light also starves this mechanism.** |
| **C. Electroweak baryogenesis** | **fails** | m_H = 125 GeV makes the electroweak transition a smooth crossover; Standard Model CP violation is far too small; CCEF adds nothing at the electroweak scale |
| **D/E. ΔB = 2 at the geometrogenesis front** | **allowed, unquantified** | see below |

## The one open route: ΔB = 2 at the growth front [COND]
- **B violation:** the uddudd junction is allowed by the string-net rules in Branch L₃. Sphalerons then share the resulting B − L between baryons and leptons.
- **Out of equilibrium:** the advancing crystal front from the seed-growth simulations (`CCEF_geometry_groundstate.md` §4c).
- **Washout:** thermal ΔB = 2 processes (rate ~ c·T¹¹/Λ*¹⁰) erase any asymmetry while T > T_f:

| c (unknown) | 1 | 10⁻² | 10⁻⁴ | 10⁻⁶ | 10⁻⁸ |
|---|---|---|---|---|---|
| T_f / Λ* | 0.23 | 0.35 | 0.54 | 0.82 | > 1 (no washout) |

  So the temperature just behind the front must lie below T_f.
- **Size of CP bias needed:** with about one ΔB = 2 opportunity per crossover cell, the product (events per cell) × (CP bias) needed is only **3×10⁻¹¹** (for T = 0.2 Λ* behind the front) to **3×10⁻⁹** (T = 0.95 Λ*).
- **The missing ingredient:** a **grain-level source of CP violation**. Nothing in the framework provides one yet **[OPEN]**.
- **Test:** this route implies neutron–antineutron oscillation, but at Λ* ≈ 10¹¹ GeV its time is ~10²⁶ yr against a laboratory limit of ~3 yr. **Untestable.**

> **Follow-up (`CCEF_grain_CP.md`):**
> - Grains *can* carry CP violation: complex phases in the ΔB = 2 junction, or a junction-chirality coupling (χ is C-even, P-odd, T-odd). Frustrated junctions even have a built-in pair of mirror-image ground states.
> - The current Hamiltonian is CP-symmetric, though, so CP violation must be added or shown to arise spontaneously.
> - If it is spontaneous, a single seed is required to give one sign everywhere.
> - **Lattice test:** the junctions do *not* lock into one handedness (16-grain exact calculation; their handedness cancels on cooling). So in Branch L₃, CP violation must be added explicitly.
> - **Janus/CPT option (`CCEF_janus_cpt.md`):**
>   - B = 0 at the Janus point and opposite asymmetries on the two sides are automatic.
>   - The CP-odd ingredient may sit in the Janus-point state instead of the laws, but only if baryon violation switches off with cooling and the state's phase survives until matter exists.

## One seed, one sign [CONJECT]
- If space grew from a **single seed**, whatever bias the front carried has the same sign everywhere: no matter–antimatter domains.
- That is required observationally: no annihilation boundaries are seen out to ~Gpc scales, and the CCEF universe is only ~1 CMB diameter across.
- Several seeds with independent signs would be excluded unless a global CP bias fixes the sign.

## Verdict
- **Branch L₃ has no working baryogenesis mechanism today.** The textbook routes are forbidden (Majorana leptogenesis), starved by the theory's own neutrino dilution (Dirac leptogenesis) or too weak (electroweak).
- One route remains open: **ΔB = 2 processes at the geometrogenesis front with an unknown grain-level CP violation**, which requires a modest CP bias and a cool enough universe behind the front.
- **Branch M** has standard Majorana leptogenesis available.
- **Baryogenesis is a genuine pressure point for Branch L₃** and a reason, other than proton decay, why the M/L₃ fork matters.
- Correction to an earlier informal remark: Dirac leptogenesis looked like a natural fit for L₃'s tiny coupling, but the same dilution kills it.
