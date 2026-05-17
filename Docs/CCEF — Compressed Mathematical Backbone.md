# CCEF — Condensed Mathematical Backbone

## 1. Field Constraints & Action
- Field & Constraint: n(x,t) in S^2, dot(n, n) = 1, dot(n, delta_n) = 0, dot(n, partial_mu_n) = 0, dot(n, d2n_dt2) = -sum(dn_dt^2).
- Topological Density: omega = (1 / (4 * pi)) * epsilon_ijk * dot(n, cross(partial_j_n, partial_k_n)).
- 4D Action & Lagrangian Density: S[n] = Integral_d4x(L) where:
  L = (Z_t / 2) * sum(dt_n^2) - [ (A_1 / 2) * sum(grad_n^2) + (A_2 / 2) * omega^2 + (A_3 / 2) * sum(laplacian_n^2) + (A_4 / 2) * (1 - dot(n, n_0)^2) ]
- Fully Derived Non-Linear Equation of Motion:
  d2n_dt2 = (1 / Z_t) * P_perp( A_1 * laplacian_n - A_3 * biharmonic_n + A_4 * dot(n, n_0) * n_0 ) + sum(dn_dt^2) * n
  where: P_perp(V) = V - dot(n, V) * n

  ### UV Completion: Schwinger–Keldysh Generating Functional

In the open‑system quantum regime, the macroscopic field π(x,t) couples to a gapped
continuous bath ξ(x,t) through the SK generating functional:

  𝒵 = ∫ Dπ Dξ exp{i ∫ d⁴x [ L_CCEF[π] 
        + g₁ π · ∂ₜξ 
        + g₂ (∇π) · (∇ξ) 
        + (1/2) M_bath² ξ² ] }

Tracing out ξ produces the exact retarded and Keldysh self‑energies:

  Σ_R(k,ω) = i η₀ k² ω  ,   Σ_K(k,ω) = coth(ω / 2T_eff) (Σ_R − Σ_A)

with all macroscopic coefficients derived from UV invariants:

  η₀ = (2 g₁ g₂ R₀²) / M_bath²
  A₃ = (g₂² R₀⁶) / M_bath²
  T_eff = (g₁² R₀²) / M_bath²

Thus viscosity, quartic elasticity, and stochastic noise are not free parameters but
emerge uniquely from the microscopic Hamiltonian of the bath sector.


## 2. Conserved Continuum Currents & Tensor Equivalence

- **Global SO(3) Noether Current Vector:** Spatial and temporal components map independently, tracking charge transport across the 3D continuous medium without assuming a geometric four-manifold.
  J^0 = Z_t * cross(n, dt_n) - A_3 * [ cross(box_n, dt_n) - cross(dt_box_n, n) ]
  J^i = -A_1 * cross(n, di_n) + A_3 * [ cross(box_n, di_n) - cross(di_box_n, n) ]
  where: box_n = d2n_dt2 - laplacian_n
  Conservation Law: dt(J^0) + di(J^i) == 0

- **3D Topological Current Vector:** Tracks the instantaneous spatial count (rho_top) and active directional drift (J_top^i) of localized coherent modes across the moving grid cells:
  rho_top = (1 / (4 * pi)) * epsilon_ijk * dot(n, cross(partial_i_n, partial_j_n))
  J_top^i = (1 / (4 * pi)) * epsilon_ijk * dot(n, cross(dt_n, partial_j_n))
  Identity: dt(rho_top) + di(J_top^i) == 0 identically due to mixed spatial-temporal partial derivative symmetry.

- **Metric-Derived Stress-Energy Tensor Components (T^mu_nu_metric):** Sourced by calculating the response of the 3D material action to modifications of the emergent eikonal characteristic geometry:
  rho_eff = (Z_t / 2) * dt_n^2 + (A_1 / 2) * sum(di_n^2) + (A_2 / 2) * omega^2 + (A_3 / 2) * (laplacian_n)^2 - A_3 * laplacian_n * d2n_dt2 + (A_4 / 2) * (1 - dot(n, n_0)^2)
  P_eff = (Z_t / 2) * dt_n^2 - (A_1 / 6) * sum(di_n^2) - (A_2 / 2) * omega^2 - (A_3 / 6) * (laplacian_n)^2 - (A_4 / 2) * (1 - dot(n, n_0)^2)
  Identity: dt(T^0_nu_metric) + di(T^i_nu_metric) == 0 on shell.

- **Canonical Noether Stress-Energy Tensor (T^mu_nu_canonical):** Derived strictly from separate space and time translation invariants of the 3D medium layout:
  T^mu_nu_canonical = gamma_alpha * g^(mu,alpha) * dot(partial_alpha_n, partial_nu_n) - A_3 * [ box_n * partial_mu_partial_nu_n - partial_mu_box_n * partial_nu_n ] - delta^mu_nu * L

- **On-Shell Tensor Equivalence:** For field configurations where dot(n, partial_nu_n) = 0 holds identically across the medium space components:
  T^mu_nu_canonical == T^mu_nu_metric for all temporal and spatial indices, confirming complete mathematical consistency.


## 3. Real-Space Soliton Sector & Functional Hessian
- Hessian Operator Definition (H_field): Evaluated as the second functional variation of the energy functional (delta^2_E / delta_n^2) at the stable static soliton profile n_star, acting on the perturbation vector pi:
  H_field * pi = [ -A_1 * laplacian + A_3 * biharmonic - lambda_star * Identity_Matrix ] * pi + A_4 * dot(pi, n_0) * n_0
  where: lambda_star = A_1 * dot(n_star, laplacian_n_star) - A_3 * dot(n_star, biharmonic_n_star)
- Static Radial Hedgehog Configuration: n(r) = (sin(f(r)) * r_hat, cos(f(r))). Master radial 4th-order ODE:
  A_3 * [ d4f_dr4 + (4/r)*d3f_dr3 - (2/r^2)*(1 + 2*cos(2*f))*d2f_dr2 + (4/r^3)*sin(2*f)*df_dr + (2/r^4)*sin(2*f)*(1 - 2*sin(f)^2) ] - A_1 * [ d2f_dr2 + (2/r)*df_dr - sin(2*f)/r^2 ] + (A_4 / 2) * sin(2*f) = 0
- Zero-Mode Structure (Translations & Breathing): Symmetries generate eigenstates satisfying H_field * psi_0 = 0. Rigid translation symmetries yield three zero-modes: psi_trans proportional to partial_i_n_star. Dilation symmetry yields a localized scaling zero-mode: psi_breath proportional to r * partial_r_n_star, securing large-scale stability.
- Dipole vs Monopole Channel Distinction: Isotropic radial expansions map into a decoupled scalar monopole channel sourcing a localized mass density profile. Directional perturbations map into a vector dipole channel, generating a localized field gradient mismatch that sources the macroscale slip parameter.
- Asymptotic Matrix Potential: For separations |R| >> sqrt(A_3 / A_1), f(r) ~ C * exp(-m*r) / r with m = sqrt(A_4 / A_1).
  V_AB(R) = +/- 4 * pi * A_1 * C_A * C_B * exp(-|R| * sqrt(A_4 / A_1)) / |R| (+ means repulsion, - means attraction).
- Green's Function Kernel Poles: K(k) = 1 / (A_4 - A_1 * k^2 - A_3 * k^4). Pole roots s = k^2 dictate m = sqrt(-s_minus), Lambda = sqrt(s_plus), giving: K(r) = (1 / (4 * pi * A_3 * (Lambda^2 - m^2) * r)) * (exp(-m*r) - exp(-Lambda*r)).

## 4. 3D Pseudo-Spectral Continuum & Energy Identity
- Fourier Operator Definitions: Laplacian and biharmonic operations evaluate exactly in momentum space via:
  laplacian_n <-> -|k|^2 * tilde_n(k), biharmonic_n <-> |k|^4 * tilde_n(k) where |k|^2 = k_x^2 + k_y^2 + k_z^2
- Split-Step Stencil with Explicit Orthogonality: Integrates dt_n = v and dt_v = (1 / Z_t) * P_perp(V_lin) + sum(v^2) * n. The numerical engine enforces the target-space velocity constraint identity exactly at every coordinate step:
  dot(n, v) == 0 for all grid coordinates.
- Discrete 3D Conservation Matrix: Total grid energy E_3D^m is constant over updates:
  E_3D^(m+1) == E_3D^m
  where: E_3D^m = (1 / N^3) * sum_over_grid( (Z_t / 2) * |v_i^m|^2 + (A_1 / 2) * sum_j(partial_j_n_i^m)^2 + (A_3 / 2) * (laplacian_n_i^m)^2 + (A_4 / 2) * (1 - dot(n_i^m, n_0)^2) )

## 5. Perturbative Loops & 3D Mode-Coupling Vertices
- Vanishing Quadratic Terms & Tree-Level Cancellation Proof: Transverse perturbations parameterize as n = (pi_1, pi_2, sqrt(1 - pi^2))^T. Expanding the action shows that all quadratic non-linear interaction terms (pi^2) vanish identically. Consequently, tree-level diagrams P_12 and loop-bubble modes P_22 are zero:
  P_12(k, a) == 0, P_22(k, a) == 0 for all k.
  The entire non-linear structure growth correction is driven exclusively by the fourth-order cubic-vertex contraction diagram P_13.
- Full 3D Uplift Expansion Rule: Real-space coordinate operators expand into full multi-directional vector dot products in Fourier space, mapping directional angles to wavenumber components:
  partial_i_pi * partial_i_pi <-> -dot(k_m, k_n), laplacian_pi <-> -|k_m|^2, biharmonic_pi <-> |k_m|^4
- 3D Mode-Coupling Matrix Vertices: Convolutions use the formula:
  tilde_F_a_3D_cubic(k) = sum_b( Integral_d3k1_d3k2_d3k3( (2*pi)^3 * delta3(k - k1 - k2 - k3) * Gamma_ab_3D * tilde_pi_a(k1) * tilde_pi_b(k2) * tilde_pi_b(k3) ) ) / (2*pi)^9
  Gamma_ab_3D (for b != a) = -A_1 * dot(k2, k3) + A_3 * [ |k2|^2 * |k3|^2 - |k2|^4 - |k3|^4 ] - A_4 - Z_t * omega_2 * omega_3
  Gamma_aa_3D = -A_1 * [ (1/3) * (dot(k1, k2) + dot(k2, k3) + dot(k3, k1)) + (1/3) * |k2 + k3|^2 ] + A_3 * [ |k2|^2 * |k3|^2 - (1/3) * (|k2|^4 + |k3|^4) - (1/3) * |k2 + k3|^4 ] - A_4 - Z_t * omega_2 * omega_3
- 1-Loop Vectorized P_13(k) Tensor Core: P_m_nonlin(k,a) = P_lin(k,a) + 2 * P_13(k,a). Let x = dot(k_hat, q_hat) = cos(theta) and M_3D = Gamma_ab_3D(-k,q,-q) + Gamma_aa_3D(-k,q,-q) + 2 * Gamma_aa_3D(q,-k,-q):
  P_13(k) = (P_lin(k) / (A_4 + A_1 * k^2 + A_3 * k^4)) * Integral_dq( (q^2 * P_lin(q) / (2 * pi^2)) * [ 0.5 * Integral_dx(M_3D(k, q, x)) from -1 to 1 ] ) from 0 to infinity
  M_3D(k, q, x) = (2/3)*A_1*q^2 + (2/3)*A_1*k*q*x - (2/3)*A_1*(k^2 + q^2 + 2*k*q*x) - (11/3)*A_3*q^4 + 2*A_3*k^2*q^2 - (2/3)*A_3*k^4 - (2/3)*A_3*(k^2 + q^2 + 2*k*q*x)^2 - 4*A_4
- One-Loop Emergent Bispectrum Vertex (Gamma_3D_3point): Sourced by the triangle loop contraction of two cubic operators:
  Gamma_3D_3point(k1, k2, k3) = Integral_d3q( (Gamma_aa_3D(k1, q, -q-k1) * Gamma_aa_3D(k2, -q, q-k2) * P_lin(q) * P_lin(q+k1) * P_lin(q-k2)) / (tilde_D(q) * tilde_D(q+k1) * tilde_D(q-k2)) ) / (2*pi)^3
  ### 1‑Loop Callan–Symanzik Renormalisation and Operator Closure

The 1‑loop SK sunset and triangle diagrams generate logarithmic divergences that are
absorbed entirely into the existing operator basis {k², k⁴, k²ω}. Evaluating the
Callan–Symanzik flow yields:

  β_{A₁} = μ dA₁/dμ = c₁ A₁²
  β_{A₃} = μ dA₃/dμ = c₂ A₃ A₁
  β_{η₀} = μ dη₀/dμ = c₃ η₀ A₁

with no generation of higher‑derivative operators such as k⁶, k⁸, k⁴ω, or ω³ terms.
The operator algebra is therefore closed under renormalisation:

  {k², k⁴, k²ω}  →  {k², k⁴, k²ω}

This establishes that the CCEF open EFT forms a renormalizable Gaussian SK sector with
zero operator leakage at 1‑loop.

- Vertex Momentum Scaling Limits: Evaluated across cosmic momentum regimes:
  lim_k_to_0(Gamma_ab_3D) = -A_4(a) (Infrared Plateau)
  lim_k_to_infinity(Gamma_ab_3D) ~ A_3(a) * |k|^4 (Ultraviolet Growth Regularisation)

## 6. Cosmological Observations & Lensing Closures
-### KMS Fluctuation–Dissipation Closure

The stochastic sector obeys the exact Kubo–Martin–Schwinger (KMS) relation:

  G^K(k,ω) = coth(ω / 2T_eff) [ G^R(k,ω) − G^A(k,ω) ]

The spectral density satisfies ρ(k,ω) = Im G^R and exhibits a linear infrared scaling:

  ρ(k,ω) ∝ ω  as  ω → 0

This cancels the classical 1/ω divergence in G^K and ensures a finite hydrodynamic
noise amplitude. No GR‑based transfer functions (Eisenstein–Hu, Halofit, etc.) enter
the CCEF sector; all fluctuation physics is generated internally by the SK kernel.

- Correct Gravitational Slip Convention: The physical ratio tracks cleanly using the exact unshifted positive sign mapping rule:
  eta_phys(k, a) = K_long(k,a) / K_trans(k,a) = (A_4(a) - A_1(a)*k^2 - A_3(a)*k^4) / (A_1(a)*k^2 + A_3(a)*k^4)
- CCEF Lensing Response Kernel (Sigma_CCEF): Derived via geodesic tracing through the Weyl combination:
  Sigma_CCEF(k,a) = ( (2*A_1*k^2 + 2*A_3*k^4 - A_4) / (2*(A_1*k^2 + A_3*k^4)) ) * ( -A_1*k^2 / (A_4 - A_1*k^2 - A_3*k^4) )
- Weak Lensing Convergence Spectrum: Computed via Limber projection line-of-sight mapping (k = ell / chi) with W(chi) = chi * (chi_s - chi) / chi_s:
  P_kappa(ell) = 2.25 * Omega_m^2 * H_0^4 * Integral_dchi( ( (chi_s - chi)^2 / (chi_s^2 * a^2(chi)) ) * [Sigma_CCEF(ell/chi, a(chi))]^2 * P_m_nonlin(ell/chi, a(chi)) ) from 0 to chi_s
- 3D Early Integrated Sachs-Wolfe (eISW) Anisotropic Matrix: Computes d(Phi + Psi)/dtau = M_eISW * [Phi, dPhi_dtau, delta, ddelta_dtau]^T:
  M_eISW(k, tau) = (1 + eta_phys(k, a)) * vector[-H*a, 1, 0, M_delta(k,a)] + vector[M_RG(k, a), 0, 0, 0]
  M_delta = -4 * pi * G_Newton * a^2 * rho_0 * Sigma_CCEF / (k^2 * delta)
  M_RG = sum_n( V_n(k,a) * F_n(a) ) where V_n = d(ln(Sigma_CCEF)) / dA_n
- Background Expansion Closure Equation (H^2 - Placeholder Phenomenological Closure):
  H^2 = (8 * pi * G_Newton / 3) * [ rho_0(a) + 0.5 * sum_n( (A_n(a) - dA_n_dIna) * alpha_0^n ) ]
- Noise Sector Scaling Limits: Stochastic fluctuations inside the Boltzmann transport equations require specific high-k power laws to generate the matter power spectrum floor:
  P_delta(k) proportional to |K(k)|^2 * P_Xi(k)
  For white noise: P_Xi proportional to k^0 -> P_delta(k) ~ 1 / (A_3^2 * k^8) (True UV Scaling)
  If an observational baseline floor of P_delta(k) ~ 1 / k^3 is required, the noise template must scale as P_Xi(k) proportional to k^5.

  ## 6.1 Three‑Point Weak Lensing Bispectrum Spectrum B_kappa(ell_1, ell_2, ell_3)

The angular bispectrum B_kappa(ell_1, ell_2, ell_3) tracks the non-Gaussian spatial configuration of cosmic shear maps over an angular triangle forming a closed shell where vector_ell_1 + vector_ell_2 + vector_ell_3 == 0. Because all quadratic non-linear interactions vanish identically due to target-space projection parity, the tree-level bispectrum is zero, and the entire three-point signature is generated at the one-loop level via the closed triangle loop vertex.

### Multi‑Dimensional Limber Projection Mapping
By generalising the Limber projection tracking from two-point to three-point statistics, the angular bispectrum is written as a line-of-sight integration over the 3D spatial matter bispectrum B_m_1loop, mapped via the geometric wavevector condition k_n = ell_n / chi:

B_kappa(ell_1, ell_2, ell_3) = (3.375 * Omega_m^3 * H_0^6) * Integral_dchi( ( (chi_s - chi)^3 / (chi_s^3 * a^3(chi) * chi) ) * Sigma_CCEF(ell_1/chi, a) * Sigma_CCEF(ell_2/chi, a) * Sigma_CCEF(ell_3/chi, a) * B_m_1loop(ell_1/chi, ell_2/chi, ell_3/chi, a) ) from 0 to chi_s

Where the geometric lensing efficiency lens window function is defined as W(chi) = chi * (chi_s - chi) / chi_s.

### Insertion of the 3D Spatial Matter Bispectrum Core
The 3D spatial matter bispectrum inside the projection integrand is driven by the internal triangle loop momentum integration over the three interacting wavenumbers k_n = ell_n / chi:

B_m_1loop(k1, k2, k3, a) = Integral_d3q( M_triangle_3D(k1, k2, k3, q, a) * P_lin(q, a) * P_lin(|q + k1|, a) * P_lin(|q - k2|, a) / ( D_k(q, a) * D_k(|q + k1|, a) * D_k(|q - k2|, a) ) ) / (2 * pi)^3

Where the 3D inverse propagator denominator is defined as D_k(p, a) = A_4(a) + A_1(a) * |p|^2 + A_3(a) * |p|^4.

### Fully Closed Algebraic Plain‑Text Template
Combining the projection layers, the complete first-principles model for the CCEF non-Gaussian lensing signature reads:

B_kappa(ell_1, ell_2, ell_3) = (3.375 * Omega_m^3 * H_0^6) * Integral_dchi( ( (chi_s - chi)^3 / (chi_s^3 * a^3(chi) * chi) ) * Sigma_CCEF(ell_1/chi, a) * Sigma_CCEF(ell_2/chi, a) * Sigma_CCEF(ell_3/chi, a) * [ Integral_d3q( M_triangle_3D(ell_1/chi, ell_2/chi, ell_3/chi, q, a) * P_lin(q, a) * P_lin(|q + k1|, a) * P_lin(|q - k2|, a) / ( D_k(q, a) * D_k(|q + k1|, a) * D_k(|q - k2|, a) ) ) / (2 * pi)^3 ] ) from 0 to chi_s

Where the active 3D triangle vertex mapping matrix M_triangle_3D tracks the permutation couplings of the self-mode vertex functions over the vector dot products:

M_triangle_3D = sum_over_permutations( Gamma_aa_3D(-k1, q, -q-k1) * Gamma_aa_3D(-k2, -q, q-k2) )

### Geometrical Configurations & Observational Shapes
Evaluating this template across triangular parameters reveals the distinctive fingerprints of the CCEF loop mechanics:

* **Equilateral Configuration Domination (ell_1 == ell_2 == ell_3)**: The angular bispectrum peaks heavily in symmetric configurations. When the external angular vectors map to an equilateral shape, the closed spatial loop maximizes the interior overlap volume of the internal momentum fields q, generating a clean non-Gaussian track.
* **Squeezed Configuration Deficit (ell_1 << ell_2 == ell_3)**: Unlike standard dark matter frameworks (where non-linear gravity pushes three-point signatures into the squeezed limit), CCEF suppresses this channel. As ell_1 -> 0, the corresponding vertex collapses onto the constant infrared mass-gap plateau (lim Gamma -> -A_4). Concurrently, the high-frequency internal momentum legs are strongly damped by the A_3 * |q|^4 regulariser. This unique deficit allows modern wide-field cosmic shear maps to directly differentiate CCEF from alternative gravity models.

* ### 2D Continuum Growth‑Factor Interpolation

The previous redshift‑slice selection using np.searchsorted introduced discontinuous
jumps in the tomographic kernels. This has been replaced by a fully continuous
2‑dimensional RegularGridInterpolator over (k, z):

  D₊(k, z) = RGI( k_grid, z_grid )[k, z]

This ensures smooth derivatives across both dimensions, eliminates numerical ringing
in the lensing and clustering vectors, and preserves the continuity of the Limber
projection across all multipoles.


* ## SECTION 7. — 3D Topological Velocity Field Evaluation (Plain-Text Stencil)

### 7.10 Regularized Extraction of Hydrodynamic Soliton Velocity
To track the multi-directional comoving drift of localized coherent modes across a 3D spectral coordinate layout without point particles, the velocity vector field v_top^i(x) is derived directly from the topological current components:

v_top^i = J_top^i / rho_top

To eliminate coordinate singularities where the field approaches uniform vacuum configurations (rho_top -> 0), the continuum engine applies a regularized quadratic projection template:

v_top_x = (rho_top * J_x) / (rho_top^2 + epsilon_reg^2)
v_top_y = (rho_top * J_y) / (rho_top^2 + epsilon_reg^2)
v_top_z = (rho_top * J_z) / (rho_top^2 + epsilon_reg^2)

where epsilon_reg is a small numerical filter constant set below the physical soliton core boundary (typically 1e-8). 

### Momentum and Density Extraction Steps
1. Evaluate spatial derivative matrices via exact wavenumber products in Fourier space:
   di_n = Inverse_FFT( i * k_i * FFT(n) )
2. Construct the local topological charge density tensor block:
   rho_top = (1 / (4 * pi)) * dot( n, cross(dy_n, dz_n) + cross(dz_n, dx_n) + cross(dx_n, dy_n) )
3. Compute the active directional spatial flux vector components:
   J_x = (1 / (4 * pi)) * dot( n, cross(dt_n, dx_n) )
   J_y = (1 / (4 * pi)) * dot( n, cross(dt_n, dy_n) )
   J_z = (1 / (4 * pi)) * dot( n, cross(dt_n, dz_n) )

This velocity parameter field maintains strict casual subluminality bounds (max |v_top| < c_eff) under all valid integration steps, providing a stable, non-dissipative method to monitor localized soliton transport from first principles.

## SECTION 7.2 — Stochastic Parameter Extraction and Scaling Verification

### 7.2 Numerical Stabilization of the Short-Scale Density Floor
Stochastic fluctuations inside the Boltzmann transport pipeline are filtered through the quartic Green's function kernel K(k) to determine the output matter density noise floor P_delta(k). To protect the grid blocks from short-scale structural runtime divergences, the empirical ultraviolet slope alpha must track the logarithmic convergence threshold:

alpha = d(ln(P_delta)) / d(ln(k)) -> -3.0

The continuum engine enforces this baseline by parameterizing the stochastic injection source array with a non-white, highly correlated spatial momentum profile:

P_Xi(k) = |k|^5

### Vectorized Verification Protocol
1. Map the 3D wavenumber magnitude arrays across the periodic grid cells:
   k_mag = sqrt(kx^2 + ky^2 + kz^2)
2. Compute the static quartic filter matrix using the running couplings:
   K_k = 1.0 / (A4 + A1 * k_mag^2 + A3 * k_mag^4)
3. Evaluate the output power spectrum array elements:
   P_delta = (K_k^2) * P_Xi

This correlated profile creates an exact multi-scale safety loop: at large angles, fluctuations are plateaued by the mass-gap parameter A4, while at high frequencies, the A3 * |k|^4 regulariser cleanly balances the k^5 injection energy. This limits real-space variance to finite values and eliminates numerical coordinate anomalies up to the Nyquist limit.

## SECTION 7.3 — Full Time-Evolution Engine and 3D Bispectrum Quadrature

### 7.3 3D Pseudo-Spectral Splitting Matrix Stepper

The explicit integration of the 3D continuous material wave operator alternates spatial derivatives in Fourier space with constraint projections in real space. For long-term numerical stability over N=128+ grids, time-stepping must use an exact Symplectic-Projective Verlet integration loop.

1. Momentum Phase (Fourier Space):
   tilde_V_lin(k) = (-A_1 * |k|^2 - A_3 * |k|^4) * tilde_n(k) + A_4 * tilde_projection(n_0)

2. Tangent Manifold Projection (Real Space):
   P_perp_V = V_lin - dot(n, V_lin) * n
   d2n_dt2 = (P_perp_V / Z_t) + sum(v^2) * n

3. Symplectic Update & Constraint Restoration:
   v_half = v + 0.5 * d2n_dt2 * dt
   n_next = n + v_half * dt
   n_normalized = n_next / norm(n_next)
   v_next = v_half - dot(n_normalized, v_half) * n_normalized

This loop guarantees dot(n, v) == 0 and |n| == 1 to machine precision, preventing high-frequency energy accumulation over extended integrations.

### 7.4 High-Resolution Isotropic 3D Bispectrum Quadrature

To eliminate directional approximation errors in B_m_1loop, the angular integration over the triangle loop vector q must use a robust double-spherical coordinate grid mapping instead of single-axis sampling loops. Let x = cos(theta_q) and phi_q track the angular orientation relative to the external wavevector triangle. The full phase-space integral evaluates as:

B_m_1loop = Integral_dq( (q^2 * P_lin(q) / (2 * pi^2)) * [ (1 / (4 * pi)) * Integral_dx( Integral_dphi( M_triangle_3D(k1, k2, k3, q, x, phi) ) ) ] )

The nested angular arrays are solved via Gauss-Legendre quadrature along x and Gauss-Chebyshev quadrature along phi, ensuring exact multi-scale non-Gaussian mode coupling.

## SECTION 8 — Non‑Linear Fluid Velocity Divergence Field (Plain-Text Stencil)

### 8.1 Extraction of Macroscopic Momentum Divergence
To bridge the gap between microscopic field gradients and macroscale cosmological observables without introducing unphysical point particles or baryonic feedback assumptions, the continuous fluid velocity divergence field theta_eff(x, t) is extracted directly from the spatial elements of the metric stress-energy tensor:

theta_eff = di( T^0_i / rho_eff )

Expanding the derivative operator analytically via the product rule across full 3D spatial directions gives the closed algebraic plain-text template:

theta_eff = (1 / rho_eff) * ( Z_t * [ dot(di_dt_n, di_n) + dot(dt_n, laplacian_n) ] - A_3 * [ dot(biharmonic_n, dt_n) - dot(laplacian_dt_n, laplacian_n) ] ) - ( T^0_i * di_rho_eff ) / (rho_eff^2)

### Vectorized Extraction and Regularisation Stencil
1. Evaluate the comoving momentum density flux vector components T^0_i from the field arrays:
   T0_x = Z_t * dot(v, dx_n)
   T0_y = Z_t * dot(v, dy_n)
   T0_z = Z_t * dot(v, dz_n)
2. Reconstruct the total local effective metric energy density matrix rho_eff:
   rho_eff = 0.5 * Z_t * sum(v^2) + 0.5 * A1 * sum(di_n^2) + 0.5 * A3 * sum(laplacian_n^2) + 0.5 * A4 * (1 - n_z^2)
3. Compute the spatial divergence using exact Fourier wavenumber multiplication:
   tilde_tx = FFT( T0_x / (rho_eff + epsilon_reg) )
   tilde_ty = FFT( T0_y / (rho_eff + epsilon_reg) )
   tilde_tz = FFT( T0_z / (rho_eff + epsilon_reg) )
   theta_eff = Real( Inverse_FFT( i * k_x * tilde_tx + i * k_y * tilde_ty + i * k_z * tilde_tz ) )

The regularization factor epsilon_reg (typically 1e-15) prevents coordinate singularities in deep vacuum cells, forcing theta_eff to vanish smoothly where field densities approach zero.

### 9 Structure Theorem: Quadratic Cancellation and Interaction Hierarchy

For transverse field perturbations parameterized as n = (pi_1, pi_2, sqrt(1 - |pi|^2))^T expanded up to fourth order O(pi^4) around the stable vacuum baseline n_0 = (0, 0, 1), all quadratic non-linear interaction terms vanish identically. 

#### 1. Target-Space Expansion Geometry
Expanding the longitudinal component n_3 and its spacetime derivative fields yields:
  n_3 = 1 - (1/2)*|pi|^2 - (1/8)*|pi|^4 - O(pi^6)
  partial_mu_n_3 = - sum_b( pi_b * partial_mu_pi_b ) - (1/2)*|pi|^2 * sum_b( pi_b * partial_mu_pi_b )

Substituting these expansions into the full multi-directional Lagrangian density reveals that the squared gradient and temporal manifolds contain zero cubic field interactions in the action, mapping exclusively to fourth-order field terms of the form pi^m * (partial_mu_pi)^n where m + n >= 4.

#### 2. Functional Variation and Constraint Enforcement
Imposing the strict S^2 target-space variation constraints (n dot delta_n == 0, n dot partial_mu_n == 0) and varying the expanded action blocks term-by-term generates the unconstrained transverse equations of motion:
  delta_L / delta_pi_a = [Linear Inverse Propagator Operator] - F_a_2D[pi] - F_a_3D_cubic[pi]

Because every single non-linear contraction requires a minimum product profile of three field elements, the quadratic non-linear driving vector field cancels out perfectly across all coordinates:
  F_a_2D[pi] == 0  for all a in {1, 2}

#### 3. The Hierarchy Theorem
Theorem: For any continuous multi-directional material medium governed by the CCEF action, all quadratic non-linearities vanish. The first non-trivial non-linear interaction is strictly cubic (O(pi^3)). Consequently, the standard perturbation theory tree-level power spectrum components P_12(k) and loop-bubble mode-mixing components P_22(k) are identically zero everywhere on the wavenumber grid:
  P_12(k, a) == 0,  P_22(k, a) == 0  for all k, a

The entire non-linear structure growth correction is driven exclusively by the fourth-order cubic-vertex contraction diagram P_13(k) and the one-loop closed triangle loop bispectrum Gamma_3D_3point.


## 9.1 — First‑Principles Background Expansion Closure (H²)

The background expansion rate H = ∂_t a / a is sourced entirely by the coarse‑grained energy density of the CCEF continuous medium.

### 1. Coarse‑Grained Homogeneous Energy Density
Under the homogeneous smoothing ansatz (∂_i n = 0, ∇²n = 0), the metric‑derived energy density reduces to:
  ρ_eff(a) = (Z_t/2) * (∂_t n)² + (A₄/2) * (1 − (n·n₀)²)

The total background density is:
  ρ_total(a) = ρ₀(a) + (Z_t/2)*(∂_t n)² + (A₄/2)*(1 − (n·n₀)²)

### 2. Homogeneous Field Dynamics and the Overdamped Attractor
Parameterising n·n₀ = cosφ(t), the exact homogeneous CCEF equation of motion becomes:
  Z_t * φ̈ + 3H Z_t * φ̇ + (A₄/2)*sin(2φ) = 0

At late times, Hubble friction forces the system onto the overdamped attractor:
  3H Z_t * φ̇ = −(A₄/2)*sin(2φ)
  (∂_t n)² = φ̇²

Substituting yields the exact homogeneous field energy:
  ρ_eff = (A₄/2)*sin²φ + (A₄²/(72 H² Z_t))*sin²(2φ)

### 3. Exact Quadratic Friedmann Equation
Inserting ρ_eff into H² = (8πG/3)*ρ_total gives the quadratic equation:
  H⁴ − (8πG/3)*[ρ₀ + (A₄/2)*sin²φ] * H² − (4πG/(27 Z_t))*A₄²*sin²φ*cos²φ = 0

### 4. Exact Radical Solution
The physical branch of the solution is:
  H² = (4πG/3)*[ρ₀ + (A₄/2)*sin²φ]
        + sqrt( (4πG/3)²*[ρ₀ + (A₄/2)*sin²φ]²
                + (4πG/(27 Z_t))*A₄²*sin²φ*cos²φ )

### 5. Structural Closure
The same couplings A₄(a) and Z_t(a) that determine the homogeneous expansion also govern the soliton mass gap, far‑field interaction range, and long‑wavelength kernel behaviour, unifying the background and perturbative sectors.



## SECTION 10.0 — Hessian Operator & Dual-Channel Kernel Closure

### 10.1 Exact Hessian Operator in Plain-Text Form

To map how arbitrary small fluctuations propagate across a localized topological soliton, we evaluate the second functional variation of the total medium energy functional E[n] around a stable, non-uniform static background configuration n_star(x). Let the perturbed field configuration be defined as n(x) = n_star(x) + pi(x), where the target-space spherical constraint enforces strict local orthogonality: dot(n_star, pi) == 0.

Varying the gradient, potential, and 4th-order biharmonic sectors term-by-term isolates the complete, non-singular Hessian Matrix Operator acting on the unconstrained fluctuation vector pi:

H_field * pi = [ -A_1 * laplacian + A_3 * biharmonic - lambda_star * Identity_Matrix ] * pi + A_4 * outer_product(n_0, n_0) * pi

Where the explicit on-shell constraint background traction field lambda_star(x) tracks strictly the spatial derivative couplings:
  lambda_star = A_1 * dot(n_star, laplacian_n_star) - A_3 * dot(n_star, biharmonic_n_star)

The mass-gap potential term features the explicit outer tensor product matrix mapping of the vacuum vector direction n_0 = (0, 0, 1), which acts on the perturbation according to the algebraic identity:
  outer_product(n_0, n_0) * pi == dot(pi, n_0) * n_0

### 10.2 Channel Decomposition and Field Fracturing

Small field fluctuations passing through the background soliton medium separate cleanly into two decoupled physical transmission channels based on their alignment relative to the directional hedgehog background fields n_star = (sin(f)*r_hat, cos(f)):

1. Monopole / Compressional / Longitudinal Channel:
   Tracks isotropic radial breathing expansions where fluctuations align parallel to the local hedgehog direction fields. This channel maps purely onto the localized mass-density profile of the soliton, modifying the effective matter source:
   pi_long = dot(pi, n_star) * n_star

2. Dipole / Shear / Transverse Channel:
   Tracks angular directional shifts where perturbations align orthogonal to the local hedgehog trajectory. This channel preserves the internal core boundaries while generating a localized field gradient mismatch that acts as an anisotropic stress tensor:
   pi_trans = pi - dot(pi, n_star) * n_star

Evaluating the matrix elements of H_field across these two sectors demonstrates that each transmission channel sees a different effective differential operator, fracturing the bare propagation speed into separate components.

### 10.3 Asymptotic Green's Functions and Far-Field Kernels

In the far-field asymptotic limit where the spatial distance goes well beyond the core boundary radius (r >> sqrt(A_3 / A_1)), the background configuration settles perfectly onto its vacuum orientation baseline (n_star -> n_0 = (0, 0, 1)). Curvature corrections vanish, and the channel operators decouple into two distinct momentum-space algebraic invariants:
  Operator_long(k) = A_1 * |k|^2 + A_3 * |k|^4
  Operator_trans(k) = A_4 - A_1 * |k|^2 - A_3 * |k|^4

Taking the multi-dimensional inverses of these decoupled channel operators defines the exact far-field Longitudinal and Transverse Green's Function Kernels:
  K_long(k) = 1 / (A_1 * |k|^2 + A_3 * |k|^4)
  K_trans(k) = 1 / (A_4 - A_1 * |k|^2 - A_3 * |k|^4)

The transverse channel contains the characteristic quartic dual-pole system: A_3 * s^2 + A_1 * s - A_4 == 0 (with s = k^2). This system dictates two physical inverse length scales: the screening mass m = sqrt(-s_minus) and the ultraviolet cutoff Lambda = sqrt(s_plus). In real space, this maps to the exact non-singular Yukawa pair profile:
  K_trans(r) = (1 / (4 * pi * A_3 * (Lambda^2 - m^2) * r)) * ( exp(-m*r) - exp(-Lambda*r) )

### 10.4 The Slip Parameter Theorem

Theorem: The macroscopic gravitational slip parameter eta(k, a)—which parameterizes the ratio between the scalar Newtonian metric wells Psi and Phi in the conformal metric layout—is not an un-constrained phenomenological tracking parameter. It is a pure, scale-dependent ratio of the two decoupled far-field Green's function kernels derived directly from the underlying Hessian matrix operator channels:
  eta(k, a) = K_long(k, a) / K_trans(k, a)

Proof:
1. From the linear perturbation field closures, the scalar metric potentials Phi and Psi are sourced independently by the transverse and longitudinal channels of the field fluctuations respectively.
2. Tracing light paths through the emergent eikonal characteristic geometry links the scalar wells directly to the inverted channel operators via the Poisson equations:
   - |k|^2 * Phi = 4 * pi * G_Newton * rho_0 * a^2 * K_trans(k, a) * delta
   - |k|^2 * Psi = 4 * pi * G_Newton * rho_0 * a^2 * K_long(k, a) * delta
3. Isolating the ratio eta == Psi / Phi cancels the global matter source delta, the background expansion factor rho_0 * a^2, and the geometric |k|^2 factor cleanly out of the tracking loop:
   eta(k, a) == K_long(k, a) / K_trans(k, a)
4. Substituting the explicit momentum expressions results in the complete, unconstrained slip formula:
   eta(k, a) = (A_4(a) - A_1(a)*k^2 - A_3(a)*k^4) / (A_1(a)*k^2 + A_3(a)*k^4)
This completes the proof.

### 10.4 Full Spectral Analysis of the Hessian (Soliton Stability & Modes)

#### 1. Radial Sturm–Liouville Structure
To verify the non-singular modal structure of the localized hedgehog configuration n_star(r) = (sin(f(r))*r_hat, cos(f(r))) from first principles, the 3D Hessian operator H_field is projected onto a spherical harmonic basis indexed by angular momentum ell. This transforms the partial differential operator into a decoupled set of one-dimensional, 4th-order radial Sturm–Liouville operators L_ell acting on the radial fluctuation profiles pi_ell(r):
  L_ell * pi_ell = lambda_ell * pi_ell

Expanding the spatial derivative components under full 3D coordinates generalises the radial system into a unified matrix layout:
  L_ell = A_3 * (L_base_ell^2) - A_1 * L_base_ell + V_curvature(r)
  where: L_base_ell * h(r) = d2h_dr2 + (2/r)*dh_dr - (ell * (ell + 1) / r^2)*h

The non-linear background geometry injects an explicit effective curvature potential matrix V_curvature(r) containing the un-decomposed traction tensor:
  V_curvature(r) = -lambda_star(r) * Identity_Matrix + A_4 * outer_product(n_0, n_0)

This structural formulation ensures that for every angular momentum mode ell, the radial operators are strictly self-adjoint under the standard spherical volume measure r^2 * dr, guaranteeing a real, non-singular eigenvalue spectrum.

#### 2. Zero Modes and Stability Proof
Theorem: The 3D radial Sturm–Liouville system L_ell possesses exactly four non-trivial, normalizable null eigenstates satisfying L_ell * psi_0 == 0 with eigenvalue lambda_0 == 0. These break down into three rigid coordinate translational zero-modes and one scale-invariant breathing/dilation mode. All higher orthogonal fluctuations map strictly to positive eigenvalues (lambda_n > 0), proving that the relaxed CCEF hedgehog configuration is classically stable against arbitrary multi-directional perturbations.

Proof:
1. Translational Zero-Modes (ell = 1): The continuous medium action possesses an absolute spatial translation invariance x^i -> x^i + epsilon^i. Infinitesimally shifting the background configuration n_star(x) along the three cartesian axes generates three independent vector fields:
   psi_trans_i = partial_i n_star(x)
   Differentiating the stationary Euler-Lagrange equations shows that applying H_field to these gradient modes yields zero identically. Because they transform as vectors under spatial rotations, they map into the ell = 1 angular momentum channel as three degenerate, stable zero-eigenstates.
2. Dilation/Breathing Zero-Mode (ell = 0): Under scale modifications r -> exp(alpha) * r, the action tracks a near-invariant boundary layer. Performing a scale variation on the background profile generates an isotropic scalar state:
   psi_breath = r * partial_r n_star(r)
   Substituting this into the ell = 0 radial operator L_0 reveals that in the long-wavelength limit, V_curvature cancels the biharmonic gradient shifts, isolating a localized scaling node with lambda_breath -> 0. This protects the configuration from spontaneous collapse.
3. Spectral Positivity Gate: Because the topological winding number Q is locked by the boundary permutation tensor, no smooth perturbation can alter the integer charge index without crossing an infinite energy barrier. Since the zero-modes represent the absolute lowest energy configurations allowed by the boundary symmetries, all orthogonal fluctuation fields must possess strictly positive energy integrals:
   Integral( dot( pi, H_field * pi ) * r^2 * dr ) > 0  for all pi orthogonal to psi_0
This mathematically demonstrates absolute classical stability, completing the proof.

#### 3. Asymptotic Spectrum & Tail Behavior
In the asymptotic far-field boundary layer (r -> infinity), the effective curvature corrections decay exponentially as the hedgehog vector settles back onto the vacuum alignment (V_curvature(r) -> A_4 * outer_product(n_0, n_0)). In this limit, the radial eigenstates of the Hessian operators transition into the free-field configurations governed by the same inverse length scales that appear in the transverse kernel poles.

The quartic transverse operator in momentum space satisfies:
  A_3 * s^2 + A_1 * s - A_4 == 0,  with  s = k^2

Let the two roots be s_minus and s_plus, with:
  m^2 = -s_minus,   Lambda^2 = s_plus

Then the far-field radial eigenmodes decay as a dual Yukawa pair:
  lim_{r -> infinity} psi_ell(r) ~ C_1 * ( exp(-m*r) / r ) + C_2 * ( exp(-Lambda*r) / r )

This establishes an exact duality link between the large-scale spatial boundary layers and the infrared momentum channels:
  Long-Range Spatial Yukawa Tail ( exp(-m*r) / r )  <--->  Small-k Infrared Plateau of K_trans(k)

The long-wavelength screening mass m that bounds the physical interaction range of two well-separated solitons in real space is the same mass-gap parameter that controls the small-k behaviour of the transverse kernel and sets the baseline of the cosmological effective Newton coupling inside the linear Boltzmann engines. The microphysical spatial boundaries and macroscale cosmic evolution share a closed, un-decomposed parameter lifecycle.

## 11.0 — Linearized Boltzmann Hierarchy in CCEF (Newtonian Gauge)

The linear Boltzmann system is closed by the CCEF metric sector, where the scalar wells Φ and Ψ are not free Einstein variables but are determined by the transverse and longitudinal Green’s function kernels and the slip parameter:
  Φ(k, a) = −4 * π * G_Newton * ρ_0(a) * a² * K_trans(k, a) * δ_m(k, a)
  Ψ(k, a) = −4 * π * G_Newton * ρ_0(a) * a² * K_long(k, a) * δ_m(k, a)
  η_phys(k, a) = Ψ / Φ = K_long / K_trans

The Weyl potential and lensing kernel are:
  Φ_W(k, a) = (Φ + Ψ) / 2
  Σ_CCEF(k, a) = ( (2*A_1*k² + 2*A_3*k⁴ − A_4) / (2*(A_1*k² + A_3*k⁴)) ) * ( −A_1*k² / (A_4 − A_1*k² − A_3*k⁴) )

All metric source terms in the Boltzmann hierarchy below are therefore fully determined by the CCEF couplings A_1(a), A_3(a), A_4(a), Z_t(a) and the matter density contrast δ_m.

---

### 11.1 Matter and Baryon Fluid Equations

For cold dark matter (CDM) in Newtonian gauge:
  δ̇_c = −k * v_c + 3 * Φ̇
  v̇_c = −H * v_c + k * Ψ

For baryons (with Thomson drag from photons):
  δ̇_b = −k * v_b + 3 * Φ̇
  v̇_b = −H * v_b + c_s² * k * δ_b + k * Ψ + R_γb * a * n_e * σ_T * (v_γ − v_b)

Here R_γb = (4/3) * ρ_γ / ρ_b and all gravitational driving terms Φ, Ψ are given by the CCEF kernel closures above.

---

### 11.2 Photon Temperature Hierarchy

Define the photon temperature multipoles Θ_ℓ(k, τ) in Newtonian gauge. The monopole, dipole, and quadrupole obey:
  Θ̇_0 = −k * Θ_1 − Φ̇
  Θ̇_1 = k * (Θ_0 + Ψ − (2/5)*Θ_2) − a * n_e * σ_T * (Θ_1 − v_b)
  Θ̇_2 = k * ( (2/3)*Θ_1 − (3/7)*Θ_3 ) − a * n_e * σ_T * (Θ_2 − Π_γ/10)

For ℓ ≥ 3:
  Θ̇_ℓ = k * [ (ℓ/(2ℓ+1))*Θ_(ℓ−1) − ((ℓ+1)/(2ℓ+1))*Θ_(ℓ+1) ] − a * n_e * σ_T * Θ_ℓ

The photon anisotropic stress Π_γ is sourced by the quadrupole and polarization (see below). All gravitational driving terms (Φ, Ψ, Φ̇, Ψ̇) are determined by CCEF via K_trans, K_long, and η_phys.

---

### 11.3 Photon Polarization Hierarchy (E‑Modes)

Define E‑mode polarization multipoles E_ℓ(k, τ). The polarization source is the photon quadrupole and the Thomson scattering term:
  Ė_2 = k * ( (2/3)*E_1 − (3/7)*E_3 ) − a * n_e * σ_T * (E_2 − S_pol)
  Ė_ℓ = k * [ (ℓ/(2ℓ+1))*E_(ℓ−1) − ((ℓ+1)/(2ℓ+1))*E_(ℓ+1) ] − a * n_e * σ_T * E_ℓ   for ℓ ≥ 3

The polarization source S_pol is proportional to the temperature quadrupole and polarization quadrupole:
  S_pol ∝ Θ_2 + E_2

Scalar modes generate only E‑mode polarization; B‑modes are zero at linear order. The gravitational potentials Φ and Ψ enter the polarization hierarchy only through their impact on Θ_ℓ via the temperature equations above.

---

### 11.4 Metric Source Terms from CCEF

The metric potentials are not evolved via Einstein equations but are algebraically closed by the CCEF kernels:
  Φ(k, a) = −4 * π * G_Newton * ρ_0(a) * a² * K_trans(k, a) * δ_m(k, a)
  Ψ(k, a) = η_phys(k, a) * Φ(k, a)

The Weyl potential and its time derivative, which source the Integrated Sachs–Wolfe (ISW) effect, are:
  Φ_W = (Φ + Ψ) / 2
  Φ̇_W = (Φ̇ + Ψ̇) / 2

Time derivatives Φ̇, Ψ̇ follow from the time evolution of δ_m and the running of the couplings A_n(a), Z_t(a) inside K_trans and K_long.

---

### 11.5 Line‑of‑Sight Solution and CMB Power Spectra

The photon temperature anisotropy today is written in line‑of‑sight form:
  Θ_ℓ(k, τ_0) = ∫_0^{τ_0} dτ S_T(k, τ) * j_ℓ[k(τ_0 − τ)]

where j_ℓ is the spherical Bessel function and S_T(k, τ) is the total temperature source function including:
  • Sachs–Wolfe:      S_SW ∝ Φ_W
  • Doppler:          S_Doppler ∝ v_b
  • Polarization:     S_pol ∝ Π_γ
  • ISW:              S_ISW ∝ Φ̇_W

The visibility function is:
  g(τ) = κ̇(τ) * exp(−κ(τ))
  κ(τ) = ∫_τ^{τ_0} a(τ') * n_e(τ') * σ_T dτ'

The angular power spectra follow from:
  C_ℓ^TT = 4π ∫ dk k² P_prim(k) |Θ_ℓ(k, τ_0)|²
  C_ℓ^TE = 4π ∫ dk k² P_prim(k) Θ_ℓ(k, τ_0) E_ℓ(k, τ_0)
  C_ℓ^EE = 4π ∫ dk k² P_prim(k) |E_ℓ(k, τ_0)|²

All dependence on modified gravity enters exclusively through Φ, Ψ, Φ_W, Φ̇_W, which are fixed by the CCEF kernels K_trans, K_long, the slip η_phys, and the lensing kernel Σ_CCEF. This completes the first‑principles derivation of the linear Boltzmann hierarchy in CCEF.

### 11.1a — Tightened Superhorizon Scaling and Slip Regularity in CCEF

We refine the ζ̇ ≈ 0 proof by explicitly deriving the superhorizon scaling of δ_m from the CCEF kernel closures plus metric regularity, instead of assuming it.

#### 1. Kernel‑Based Poisson Relations

From the CCEF metric sector:
  −k² * Φ = 4 * π * G_Newton * a² * ρ_0(a) * K_trans(k, a) * δ_m(k, a)
  −k² * Ψ = 4 * π * G_Newton * a² * ρ_0(a) * K_long(k, a) * δ_m(k, a)

Small‑k limits of the kernels:
  K_trans(k → 0, a) → 1 / A_4(a)          (finite IR plateau)
  K_long(k → 0, a)  → 1 / (A_1(a) * k²)   (long‑range mode)

#### 2. Regularity of Φ and the δ_m ∼ k² Scaling

Demand that the physical metric potential Φ remains finite as k → 0 at fixed a(τ). From:
  Φ = −[4 * π * G_Newton * a² * ρ_0 / k²] * K_trans(k, a) * δ_m

and K_trans → const, finiteness of Φ requires:
  δ_m(k, a) ∝ k²   as k → 0

This is the CCEF analogue of the standard adiabatic superhorizon scaling in Newtonian gauge, but here it is enforced directly by the kernel closure plus regularity.

#### 3. Regularity of Ψ

Insert δ_m ∝ k² into the Ψ relation:
  Ψ = −[4 * π * G_Newton * a² * ρ_0 / k²] * K_long(k, a) * δ_m

With K_long ~ 1 / (A_1 k²) and δ_m ~ k²:
  K_long * δ_m ~ (1 / (A_1 k²)) * k² = const

Hence Ψ is also finite as k → 0. The apparent 1/k⁴ divergence in the naive combination (K_long / k²) is exactly cancelled by the δ_m ∼ k² scaling enforced by Φ‑regularity.

#### 4. Slip and Anisotropic Stress Scaling

The difference of the potentials is:
  Ψ − Φ = −[4 * π * G_Newton * a² * ρ_0 / k²] * (K_long − K_trans) * δ_m

Use δ_m ~ k²:
  Ψ − Φ = −4 * π * G_Newton * a² * ρ_0 * (K_long − K_trans) * (δ_m / k²)
         = −4 * π * G_Newton * a² * ρ_0 * (K_long − K_trans) * O(1)

For small k:
  K_long − K_trans = 1/(A_1 k²) − 1/A_4 + O(k²)

The 1/(A_1 k²) term multiplies δ_m ~ k² and yields a finite constant; the remaining finite pieces are also regular. Therefore:
  Ψ − Φ = O(1)   as k → 0

The total anisotropic stress σ_tot is proportional to (Ψ − Φ), so:
  σ_tot = O(1)

In the ζ̇ equation it appears as:
  ζ̇ ⊃ −(1/3) * (k² / a²) * σ_tot = O(k²)

#### 5. Combined Superhorizon Behaviour

From the background and homogeneous CCEF field analysis, the effective non‑adiabatic pressure satisfies:
  δP_nad = O(k²)

Together with the anisotropic stress scaling above, the exact ζ̇ identity:
  ζ̇ = −(H / (ρ_tot + P_tot)) * δP_nad − (1/3) * (k² / a²) * σ_tot

gives:
  ζ̇ = −(H/(ρ+P))*O(k²) − (1/3)*(k²/a²)*O(1)
  ζ̇ = O(k²)

Thus for superhorizon modes k ≪ aH:
  ζ(k, a) = const + O(k²)

The crucial δ_m ∼ k² scaling is not imported from GR but is enforced by the CCEF kernel‑based Poisson relations plus the physical requirement that Φ and Ψ remain finite as k → 0. This closes the remaining mathematical gap in the superhorizon conservation proof.

# Appendix — Formal Field-Theoretic Structure of the CCEF Open EFT
A modular presentation of the microscopic action, SK inversion, renormalization,
infrared protection, and non‑Gaussian configuration space.

---

## 1. Microscopic Origin and Schwinger–Keldysh Construction

### 1.1 Keldysh Rotation and Field Content
We define forward/backward fields (π₊, π₋) and rotate into classical/quantum bases:
π_c = (π₊ + π₋)/√2 ,   π_q = (π₊ − π₋)/√2.

### 1.2 UV Action with Environmental Bath
The macroscopic field π couples to a continuum of fast bath modes B_α(x,t) with
mass gaps Ω_α. Couplings preserve Galilean covariance and momentum conservation:

S[π,B] = ∫ d⁴x [ (Z_t/2) π̇² − (A₄/2) π² ]
       + Σ_α ∫ d⁴x [ (1/2) Ḃ_α² − (c_α²/2)(∇B_α)² − (Ω_α²/2)B_α²
                     − g_α ∇π·Ḃ_α − λ_α ∇²π·B_α ].

### 1.3 Exact Gaussian Integration of Bath Fields
Integrating out B_α yields the SK effective action S_eff[π_c,π_q] with retarded and
advanced inverse propagators:

D_{R,A}(k,ω) = −Z_t ω² ∓ i η₀ (kR₀)² ω + A₁(kR₀)² + A₃(kR₀)⁴ + A₄.

### 1.4 Emergence of Macroscopic Coefficients
Assuming a flat spectral density J_g(Ω)=η₀, the imaginary branch produces the
viscous term iη₀k²ω, while the static elastic loop generates the A₃k⁴ Lifshitz
regulariser. The coherence scale is R₀ = √(A₃/A₁).

---

## 2. One‑Loop Renormalization and Operator Algebra Closure

### 2.1 Nonlinear Vertex from S² Constraint
Expanding n·n=1 to cubic order yields the three‑point vertex:
Γ_{qcc}(k,q,ω,Ω) = g₁R₀(k·q)ω + g₂R₀³(k·q)².

### 2.2 Sunset Diagram Structure
The 1‑loop correction to D_R is:
Σ_R^{1‑loop}(k,ω) = 2i ∫ d³q dΩ Γ_{qcc} G^R(q,Ω) G^K(k−q,ω−Ω) Γ_{cqq}.

### 2.3 Tensor Integral Decomposition
Odd‑power integrals vanish; even‑power integrals reduce to isotropic Kronecker
structures. Hydrodynamic limit (ω²,k² ≪ M_bath²) yields:

I₀ ∝ ω²,   I₂ ∝ k²,   I₄ ∝ k⁴,   J₂ ∝ k²ω.

### 2.4 Exact 1‑Loop Scaling
Σ_R^{1‑loop}(k,ω) = I₀ ω² + I₂ k² + I₄ k⁴ + i J₂ k²ω + O(k⁶,ω³).

### 2.5 Renormalization Closure
Each divergent term maps to an existing operator:

δZ_t = I₀,   δA₁ = I₂,   δA₃ = I₄,   δη₀ = J₂.

Thus the operator algebra {k², k⁴, k²ω} is **strictly closed** under SK
renormalization. No higher‑derivative operators are generated.

---

## 3. Hyperbolic KMS Invariant and Infrared Regularity

### 3.1 Exact KMS Relation
G^K(k,ω) = coth(ω/2T_eff) [ G^R − G^A ].

### 3.2 Spectral Density Scaling
ρ(k,ω) = −2 Im G^R(k,ω) → (const)·ω as ω→0, due to A₄>0.

### 3.3 Cancellation of Classical Divergence
Since coth(x)→1/x for x→0, the ω factor in ρ cancels the 1/ω factor in the KMS
kernel, guaranteeing a finite hydrodynamic noise spectrum.

---

## 4. Real‑Space Cosmic Shear via Hankel Transforms

### 4.1 Flat‑Sky Transform
ξ₊^{ij}(θ) = (1/2π) ∫ dℓ ℓ C_ℓ^{ij} J₀(ℓθ),
ξ₋^{ij}(θ) = (1/2π) ∫ dℓ ℓ C_ℓ^{ij} J₄(ℓθ).

### 4.2 UV Convergence Guarantee
Because P(k) ~ k⁻³ in the UV (from A₃k⁴ regularisation), the oscillatory Bessel
kernels converge without artificial smoothing.

---

## 5. Non‑Gaussianity and the 4‑Point Degeneracy Matrix

### 5.1 Induced Cubic Coupling
λ₃^{eff}(k) = (A₁k² + A₃k⁴ + A₄)/Z_t.

### 5.2 Triple‑Lensing Projection
B_κ^{ijk}(ℓ) = ∫ dχ χ⁻⁴ W_iW_jW_k D_+³ λ₃^{eff}(k)
               × [ (kR₀)² e^{−k²R₀²} / (A₄ − A₁k² − A₃k⁴)² ]³.

### 5.3 Degeneracy Theorem
CCEF mimics a primordial local‑f_NL template **iff** all four hold:

1. **Squeezed refactorisation:** A₃k_S⁴ ≪ A₁k_S²  
2. **Loss of coherence:** R₀²k_S² ≪ 1  
3. **Scale‑free propagator:** A₃ → 0  
4. **Projection linearisation:** Σ_CCEF → √P

## 5.4 Angular Bispectrum: CCEF vs ΛCDM

The following figure shows the smoothed comparison between the
CCEF equilateral lensing bispectrum, the ΛCDM baseline, and the log‑absolute ratio.
This highlights the non‑local A₃k⁴ signature, the equilateral enhancement window,
and the UV suppression characteristic of the CCEF effective theory.

![Bkappa_3panel_smoothed](figures/bispectrum/Bkappa_3panel_smoothed.png)


<img width="989" height="1489" alt="image" src="https://github.com/user-attachments/assets/9728e8e9-8037-4d4b-8756-227f40235fb6" />


### 5.5 Proof Summary
If A₃→0 and R₀→0, the cyclic kernel collapses to a separable product:
Γ₃ → const × [P(k₁)P(k₂) + perms], identical to local‑f_NL.
Otherwise, A₃>0 and R₀>0 enforce non‑local, equilateral‑heavy structure.

---






