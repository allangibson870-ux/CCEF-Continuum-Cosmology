# CCEF — Fully Restored Plain-Text Mathematical Backbone

## 1. Field Constraints & Action
- Field & Constraint: n(x,t) in S^2, dot(n, n) = 1, dot(n, delta_n) = 0, dot(n, partial_mu_n) = 0, dot(n, d2n_dt2) = -sum(dn_dt^2).
- Topological Density: omega = (1 / (4 * pi)) * epsilon_ijk * dot(n, cross(partial_j_n, partial_k_n)).
- 4D Action & Lagrangian Density: S[n] = Integral_d4x(L) where:
  L = (Z_t / 2) * sum(dt_n^2) - [ (A_1 / 2) * sum(grad_n^2) + (A_2 / 2) * omega^2 + (A_3 / 2) * sum(laplacian_n^2) + (A_4 / 2) * (1 - dot(n, n_0)^2) ]
- Fully Derived Non-Linear Equation of Motion:
  d2n_dt2 = (1 / Z_t) * P_perp( A_1 * laplacian_n - A_3 * biharmonic_n + A_4 * dot(n, n_0) * n_0 ) + sum(dn_dt^2) * n
  where: P_perp(V) = V - dot(n, V) * n

## 2. Conserved Spacetime Currents & Tensor Equivalence
- Global SO(3) Noether Current: J^mu = Z_t * g^(mu,0) * cross(n, dt_n) - A_1 * g^(mu,i) * cross(n, di_n) - A_3 * [ cross(box_n, partial_mu_n) - cross(partial_mu_box_n, n) ] -> divergence(J) = 0.
- 3D Topological Current Vector: J_top^mu = (1 / (8 * pi)) * epsilon^(mu,nu,alpha,beta) * epsilon_abc * n^a * partial_nu_n^b * partial_alpha_n^c
  rho_top = (1 / (4 * pi)) * epsilon_ijk * dot(n, cross(partial_i_n, partial_j_n))
  J_top^i = (1 / (4 * pi)) * epsilon_ijk * dot(n, cross(dt_n, partial_j_n))
  Identity: dt(rho_top) + divergence(J_top) = 0 identically.
- Metric-Derived Stress-Energy Tensor (T^mu_nu_metric):
  rho_eff = (Z_t / 2) * dt_n^2 + (A_1 / 2) * sum(di_n^2) + (A_2 / 2) * omega^2 + (A_3 / 2) * (laplacian_n)^2 - A_3 * laplacian_n * d2n_dt2 + (A_4 / 2) * (1 - dot(n, n_0)^2)
  P_eff = (Z_t / 2) * dt_n^2 - (A_1 / 6) * sum(di_n^2) - (A_2 / 2) * omega^2 - (A_3 / 6) * (laplacian_n)^2 - (A_4 / 2) * (1 - dot(n, n_0)^2)
  Identity: partial_mu(T^mu_nu_metric) = 0 on shell.
- Canonical Noether Stress-Energy Tensor (T^mu_nu_canonical):
  T^mu_nu_canonical = gamma_alpha * g^(mu,alpha) * dot(partial_alpha_n, partial_nu_n) - A_3 * [ box_n * partial_mu_partial_nu_n - partial_mu_box_n * partial_nu_n ] - delta^mu_nu * L
- On-Shell Tensor Equivalence: For field configurations where dot(n, partial_nu_n) = 0 holds identically:
  T^mu_nu_canonical == T^mu_nu_metric for all mu, nu components.

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
- Vertex Momentum Scaling Limits: Evaluated across cosmic momentum regimes:
  lim_k_to_0(Gamma_ab_3D) = -A_4(a) (Infrared Plateau)
  lim_k_to_infinity(Gamma_ab_3D) ~ A_3(a) * |k|^4 (Ultraviolet Growth Regularisation)

## 6. Cosmological Observations & Lensing Closures
- Emergent Metric & Weyl Potentials: Metric components trace as g^00 = -1, g^ii = A_1 / Z_t. The scalar gravity wells decompose explicitly from the split kernel channels:
  Phi = -4 * pi * G_Newton * rho_0 * a^2 * K_trans(k,a) * delta
  Psi = -4 * pi * G_Newton * rho_0 * a^2 * K_long(k,a) * delta
  Phi_lens = (Phi + Psi) / 2
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


