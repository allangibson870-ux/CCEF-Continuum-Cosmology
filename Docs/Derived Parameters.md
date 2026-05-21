### CCEF / Spine v1.0 — Derived Parameters Summary (All Documents)

#### Core Structural Parameters (Energy Functional)
- **A₁ = 1.0**  
  → Quadratic gradient tension |∇n|². Normalized / axiomatic.

- **A₂ ≈ 0.45** (new prominence in Spine)  
  → Topological Skyrme term (ω²).  
  **Status**: Phenomenological in most docs; contributes to soliton binding and currents.

- **A₃ ≈ 2.8 × 10^{-6}** (main documents) / **A₃ ≈ 0.5** (Spine numerical example)  
  → Biharmonic UV regulator (∇²n)².  
  **Derived from**:  
  - RG fixed-point balance (A₁k² ≈ A₃k⁴ at core).  
  - Schwinger–Keldysh bath integration: A₃ = (g₂² R₀⁶)/M_bath².  
  - Hessian Green function for interaction kernel.  
  (Note: Different numerical regimes across document versions; ratio A₃/A₁ fixes core scale.)

- **A₄ ≈ 0.018** (main) / **A₄ ≈ 0.08** (Spine example)  
  → Vacuum mass-gap / potential term (1 − (n·n₀)²).  
  **Derived role**: Sets IR plateau of kernels (K_trans(k→0) → 1/A₄), homogeneous background energy, and screening mass m.

- **Z_t = 1.0**  
  → Kinetic time-scale normalization.

#### Kinetic & Propagation
- **χ ≈ 1.63 × 10^{-6}**  
  → Modified kinetic dressing (1 + χ E[n]).  
  **Derived from**: Null–timelike consistency (shared E₀(r) for refractive lensing and wavepacket orbits/precession).

#### Soliton & Kernel Quantities
- **Soliton Mass M**  
  → ≈45 (main gravity/orbitals docs) or ≈124 (Spine numerical example with A₃=0.5).  
  **Strongly unified**: Same M appears in lensing, orbits, and collective dynamics.

- **Interaction Kernel K(k)**  
  → Fully derived in principle: Green function of the Hessian operator ℋ around hedgehog background.  
  Explicit dual-pole form:  
  $$K(k) = \frac{A(a)}{k^2 + m^2(a)} + \frac{B(a)}{k^2 + \Lambda^2(a)}$$  
  with poles from A₃ s² + A₁ s − A₄ = 0 (s = k²).  
  Long-range: m → 0 → logarithmic ensemble potential.

- **Gravitational Slip η(k,a)**  
  → Exactly derived: η = K_long / K_trans = (A₄ − A₁k² − A₃k⁴) / (A₁k² + A₃k⁴).

#### Stochastic / Bath Sector
- **η₀ (viscosity), T_eff, ℏ_eff**  
  → Derived from Schwinger–Keldysh bath integration (g₁, g₂, M_bath, R₀).  
  Noise floor P_δ,noise ∝ ℏ_eff / k³ (with correlated injection).

- **R₀ (coherence / core scale)**  
  → Emergent: R₀ ≈ √(A₃ / A₁).

#### RG & Cosmological
- **Running couplings A_i(a)**  
  → Governed by RG flow equations (explicit schematic forms in Spine v1.0). Fixed points control IR → UV transition and phases.

- **Effective G_eff(k,a), Σ_CCEF, etc.**  
  → All descend from the derived kernel + RG.

### Status Overview (Across All Documents)
- **Fully Derived**: Kernel K(k) from Hessian Green function, χ (null-timelike), η (slip), dual-pole structure (m, Λ), A₃ (RG + SK bath), noise/dissipation coefficients (bath), operator closure (no quadratic non-linearities, renormalizable).
- **Normalized**: A₁, Z_t.
- **Partially / Numerically Constrained**: A₂, A₄, soliton mass M, precise RG beta coefficients.
- **Still Phenomenological**: Some global unit conversions and exact bath couplings (gᵢ, M_bath) — can be further fixed by matching observed particle masses / couplings.

**Core Unification Principle (Spine v1.0)**: Everything (particles as solitons, forces via Hessian kernels, cosmology via RG + ensemble, atoms as surface modes) must emerge from the single S² field, its energy functional, topology, and coarse-grained response. No external geometry or axioms permitted.

**Key Strength**: The interaction kernel is now explicitly positioned as derivable from the microscopic Hessian (major advance over pure phenomenology).
