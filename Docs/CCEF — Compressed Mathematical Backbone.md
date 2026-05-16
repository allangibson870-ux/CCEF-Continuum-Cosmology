# CCEF — Compressed Mathematical Backbone (Plain-Text Edition)

## 1. Field Constraints & Action
- Field & Constraint: n(x,t) in S^2, dot(n, n) = 1, dot(n, delta_n) = 0, dot(n, partial_mu_n) = 0, dot(n, d2n_dt2) = -sum(dn_dt^2).
- Topological Density: omega = (1 / (4 * pi)) * epsilon_ijk * dot(n, cross(partial_j_n, partial_k_n)).
- 4D Action & Lagrangian Density: S[n] = Integral_d4x(L) where:
  L = (Z_t / 2) * sum(dt_n^2) - [ (A_1 / 2) * sum(grad_n^2) + (A_2 / 2) * omega^2 + (A_3 / 2) * sum(laplacian_n^2) + (A_4 / 2) * (1 - dot(n, n_0)^2) ]
- Fully Derived Non-Linear Equation of Motion:
  d2n_dt2 = (1 / Z_t) * P_perp( A_1 * laplacian_n - A_3 * biharmonic_n + A_4 * dot(n, n_0) * n_0 ) + sum(dn_dt^2) * n
  where: P_perp(V) = V - dot(n, V) * n

## 2. Conserved Spacetime Currents
- Global SO(3) Noether Current: J^mu = Z_t * g^(mu,0) * cross(n, dt_n) - A_1 * g^(mu,i) * cross(n, di_n) - A_3 * [ cross(box_n, partial_mu_n) - cross(partial_mu_box_n, n) ] -> divergence(J) = 0.
- 3D Topological Current Vector: J_top^mu = (1 / (8 * pi)) * epsilon^(mu,nu,alpha,beta) * epsilon_abc * n^a * partial_nu_n^b * partial_alpha_n^c
  rho_top = (1 / (4 * pi)) * epsilon_ijk * dot(n, cross(partial_i_n, partial_j_n))
  J_top^i = (1 / (4 * pi)) * epsilon_ijk * dot(n, cross(dt_n, partial_j_n))
  Identity: dt(rho_top) + divergence(J_top) = 0 identically.
- Stress-Energy Tensor (T^mu_nu = rho_eff + P_eff):
  rho_eff = (Z_t / 2) * dt_n^2 + (A_1 / 2) * sum(di_n^2) + (A_2 / 2) * omega^2 + (A_3 / 2) * (laplacian_n)^2 - A_3 * laplacian_n * d2n_dt2 + (A_4 / 2) * (1 - dot(n, n_0)^2)
  P_eff = (Z_t / 2) * dt_n^2 - (A_1 / 6) * sum(di_n^2) - (A_2 / 2) * omega^2 - (A_3 / 6) * (laplacian_n)^2 - (A_4 / 2) * (1 - dot(n, n_0)^2)
  Identity: partial_mu(T^mu_nu) = 0 on shell.

## 3. Real-Space & Momentum Soliton Sector
- Static Radial Hedgehog: n(r) = (sin(f(r)) * r_hat, cos(f(r))). Master radial 4th-order ODE:
  A_3 * [ d4f_dr4 + (4/r)*d3f_dr3 - (2/r^2)*(1 + 2*cos(2*f))*d2f_dr2 + (4/r^3)*sin(2*f)*df_dr + (2/r^4)*sin(2*f)*(1 - 2*sin(f)^2) ] - A_1 * [ d2f_dr2 + (2/r)*df_dr - sin(2*f)/r^2 ] + (A_4 / 2) * sin(2*f) = 0
- Asymptotic Multi-Body Potential Matrix: For separations |R| >> sqrt(A_3 / A_1), f(r) ~ C * exp(-m*r) / r with m = sqrt(A_4 / A_1).
  V_AB(R) = +/- 4 * pi * A_1 * C_A * C_B * exp(-|R| * sqrt(A_4 / A_1)) / |R| (+ is replication/repulsion, - is attraction).
- Green's Function Kernel Poles: K(k) = 1 / (A_4 - A_1 * k^2 - A_3 * k^4). Pole roots s = k^2 dictate m = sqrt(-s_minus), Lambda = sqrt(s_plus).
  K(r) = (1 / (4 * pi * A_3 * (Lambda^2 - m^2) * r)) * (exp(-m*r) - exp(-Lambda*r)).

## 4. 3D Pseudo-Spectral Continuum & Energy Identity
- Split-Step Stencil: Integrates dt_n = v and dt_v = (1 / Z_t) * P_perp(V) + sum(v^2) * n.
  Fourier space drive: tilde_V_lin(k) = (-A_1 * |k|^2 - A_3 * |k|^4) * tilde_n(k) + A_4 * tilde_projection(n_0)
- Discrete 3D Conservation Matrix: Total grid energy E_3D^m is constant over updates:
  E_3D^(m+1) = E_3D^m
  where: E_3D^m = (1 / N^3) * sum_over_grid( (Z_t / 2) * |v_i^m|^2 + (A_1 / 2) * sum_j(partial_j_n_i^m)^2 + (A_3 / 2) * (laplacian_n_i^m)^2 + (A_4 / 2) * (1 - dot(n_i^m, n_0)^2) )

## 5. Perturbative Loops & 3D Mode-Coupling Vertices
- Cubic Non-Linear Expansion: Transverse fluctuations pi_a obey: Z_t * d2pi_a_dt2 - A_1 * laplacian_pi_a + A_3 * biharmonic_pi_a + A_4 * pi_a = F_a_3D_cubic[pi]. Tree-level P_22 loops vanish identically.
- 3D Mode-Coupling Matrix Vertices: Convolutions use the formula:
  tilde_F_a_3D_cubic(k) = sum_b( Integral_d3k1_d3k2_d3k3( (2*pi)^3 * delta3(k - k1 - k2 - k3) * Gamma_ab_3D * tilde_pi_a(k1) * tilde_pi_b(k2) * tilde_pi_b(k3) ) ) / (2*pi)^9
  Gamma_ab_3D (for b != a) = -A_1 * dot(k2, k3) + A_3 * [ |k2|^2 * |k3|^2 - |k2|^4 - |k3|^4 ] - A_4 - Z_t * omega_2 * omega_3
  Gamma_aa_3D = -A_1 * [ (1/3) * (dot(k1, k2) + dot(k2, k3) + dot(k3, k1)) + (1/3) * |k2 + k3|^2 ] + A_3 * [ |k2|^2 * |k3|^2 - (1/3) * (|k2|^4 + |k3|^4) - (1/3) * |k2 + k3|^4 ] - A_4 - Z_t * omega_2 * omega_3
- 1-Loop Vectorized P_13(k) Tensor Core: P_m_nonlin(k,a) = P_lin(k,a) + 2 * P_13(k,a). Let x = dot(k_hat, q_hat) = cos(theta) and M_3D = Gamma_ab_3D(-k,q,-q) + Gamma_aa_3D(-k,q,-q) + 2 * Gamma_aa_3D(q,-k,-q):
  P_13(k) = (P_lin(k) / (A_4 + A_1 * k^2 + A_3 * k^4)) * Integral_dq( (q^2 * P_lin(q) / (2 * pi^2)) * [ 0.5 * Integral_dx(M_3D(k, q, x)) from -1 to 1 ] ) from 0 to infinity
  M_3D(k, q, x) = (2/3)*A_1*q^2 + (2/3)*A_1*k*q*x - (2/3)*A_1*(k^2 + q^2 + 2*k*q*x) - (11/3)*A_3*q^4 + 2*A_3*k^2*q^2 - (2/3)*A_3*k^4 - (2/3)*A_3*(k^2 + q^2 + 2*k*q*x)^2 - 4*A_4

## 6. Cosmological Observations & Lensing Closures
- Emergent Characteristic Metric: Null surface condition g^mu_nu * k_mu * k_nu = 0 gives contravariant elements g^00 = -1, g^ii = c_eff^2(a) = A_1(a) / Z_t(a). Covariant spatial components: g_ii = 1 / c_eff^2(a).
- CCEF Lensing Response Kernel & Slip: Sourced by Weyl potential Phi_lens = 0.5 * (Phi + Psi). K_long = 1 / (A_1 * k^2 + A_3 * k^4), K_trans = 1 / (A_4 - A_1 * k^2 - A_3 * k^4). Slip parameter eta_phys = -K_long / K_trans. Geodesic closure yields:
  Sigma_CCEF(k,a) = ( (2*A_1*k^2 + 2*A_3*k^4 - A_4) / (2*(A_1*k^2 + A_3*k^4)) ) * ( -A_1*k^2 / (A_4 - A_1*k^2 - A_3*k^4) )
- Weak Lensing Convergence Spectrum: Computed via Limber line-of-sight mapping (k = ell / chi) with W(chi) = chi * (chi_s - chi) / chi_s:
  P_kappa(ell) = 2.25 * Omega_m^2 * H_0^4 * Integral_dchi( ( (chi_s - chi)^2 / (chi_s^2 * a^2(chi)) ) * [Sigma_CCEF(ell/chi, a(chi))]^2 * P_m_nonlin(ell/chi, a(chi)) ) from 0 to chi_s
- 3D Early Integrated Sachs-Wolfe (eISW) Anisotropic Matrix: Computes d(Phi + Psi)/dtau = M_eISW * [Phi, dPhi_dtau, delta, ddelta_dtau]^T:
  M_eISW(k, tau) = (1 + eta_phys(k, a)) * vector[-H*a, 1, 0, M_delta(k,a)] + vector[M_RG(k, a), 0, 0, 0]
  M_delta = -4 * pi * G_Newton * a^2 * rho_0 * Sigma_CCEF / (k^2 * delta)
  M_RG = sum_n( V_n(k,a) * F_n(a) ) where V_n = d(ln(Sigma_CCEF)) / dA_n
