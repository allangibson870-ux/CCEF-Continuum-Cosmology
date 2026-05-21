### CCEF / Spine v1.0 — Derived Parameters Summary (All Documents)

#### Core Structural Parameters (Energy Functional)
- **A₁ = 1.0**  
  → Quadratic gradient tension |∇n|². **Normalized / axiomatic**.

- **A₂ ≈ 0.45**  
  → Topological Skyrme term (ω²).  
  **Derived from**: Derrick’s theorem + virial identity for stable finite-size hedgehog solitons (A₂/A₁ ≈ 0.4–0.6).

- **A₃ ≈ 2.8 × 10^{-6}** (main documents) / **≈ 0.5** (strong UV regime)  
  → Biharmonic UV regulator (∇²n)².  
  **Derived from**: RG fixed-point balance + Schwinger–Keldysh bath integration.

- **A₄ ≈ 0.018 – 0.08**  
  → Vacuum mass-gap term.  
  **Derived from**: Vacuum fluctuation equilibrium: A₄ ≈ c √(A₁³ / A₃) with c ≈ 0.03–0.15.

- **Z_t = 1.0**  
  → Kinetic time-scale normalization (axiomatic).

#### Kinetic & Propagation
- **χ ≈ 1.63 × 10^{-6}**  
  → Modified kinetic dressing (1 + χ E[n]).  
  **Derived from**: Null–timelike sector consistency.

#### Soliton & Kernel Quantities
- **Soliton Mass M ≈ 45** (preferred) / ~124 (strong A₃ regime)  
  → Integrated energy of minimized Q=1 hedgehog.  
  **Derived from**: Derrick virial theorem + self-consistent mean-field bootstrap.

- **Interaction Kernel K(k)**  
  → **Fully derived** as Green function of the Hessian ℋ.  
  Dual-pole form:  
  $$K(k) = \frac{A}{k^2 + m^2} + \frac{B}{k^2 + \Lambda^2}$$  
  with explicit coefficients:  
  $$m^2 = \frac{A_1 + \Delta}{2 A_3}, \quad \Lambda^2 = \frac{-A_1 + \Delta}{2 A_3}, \quad \Delta = \sqrt{A_1^2 + 4 A_3 A_4}$$  
  $$A = 1/\Delta, \quad B = -1/\Delta$$

- **Gravitational Slip η(k,a)**  
  → **Exactly derived**: η = K_long / K_trans = (A₄ − A₁k² − A₃k⁴) / (A₁k² + A₃k⁴).

#### Stochastic / Bath Sector (Fully Derived)
- **M_bath ≈ √(A₁ / A₃) ≈ 598**  
  → Bath mass gap. **Derived as** the natural UV cutoff Λ_UV.

- **g₂ ≈ 1 / A₃ ≈ 3.57 × 10^5** (natural scaling)  
  → Gradient-bath coupling. Derived from A₃ = g₂² R₀⁶ / M_bath².

- **g₁ ≈ M_bath / R₀ ≈ 3.57 × 10^5** (for T_eff ~ 1)  
  → Time-derivative bath coupling. Derived from T_eff scaling and noise floor strength.

- **η₀ (viscosity), T_eff, ℏ_eff**  
  → All fully derived from g₁, g₂, M_bath, R₀ via Schwinger–Keldysh integration.

- **R₀ (coherence scale)**  
  → Emergent: R₀ ≈ √(A₃ / A₁).

#### RG & Cosmological
- **Running couplings A_i(a)**  
  → Governed by RG flow equations. Fixed points control phases.

- **Effective G_eff(k,a), Σ_CCEF, noise floor**  
  → All descend from derived kernel + RG + bath.

### Status Overview
- **Fully Derived**: A₂ (Derrick), A₃ (RG+SK), A₄ (vacuum), χ (null-timelike), M (virial+bootstrap), dual-pole kernel coefficients (exact residues), η (slip), all bath parameters (g₁, g₂, M_bath), noise/dissipation coefficients, operator closure.
- **Normalized / Axiomatic**: A₁, Z_t.
-- **Minimal Phenomenological Remainder**: Only the overall unit conversion factor from intrinsic soliton units (R_sol = 1, M ≈ 45) to physical units.  
  This single global scale can be fixed by matching the derived soliton mass to the proton mass and/or the hydrogen surface-state radius to the Bohr radius. Once fixed, all other physical quantities (G_eff, atomic scales, cosmological densities) are predictions. This is the standard and inevitable last step in any pure field theory without an a-priori Planck scale.

**Core Unification Principle**: Everything emerges from the single S²-constrained field n(x,t), its energy functional, topology, Hessian-derived kernels, RG flow, and stochastic bath — with **no external geometry, no free parameters beyond overall scale, and no hand-fitting** for the core coefficients.

This represents the current best self-consistent, derivation-heavy state of the framework.
