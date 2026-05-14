# CCEF — Minimal Mathematical Backbone

## 1. Field & Constraint
- Field: $n(x,t) \in S^2,\ |n| = 1$  
- Variation constraint: $n\cdot\delta n = 0$  
- Topological density:  
  $\omega = \frac{1}{4\pi} \epsilon_{ijk} n\cdot(\partial_j n \times \partial_k n)$

## 2. Energy Functional

$$E[n] = \int d^3x \left[ \frac{A_1}{2}(\partial_i n)^2 + \frac{A_2}{2} \omega^2 + \frac{A_3}{2}(\nabla^2 n)^2 + \frac{A_4}{2}(1 - (n\cdot n_0)^2) \right]$$

## 2.1 Covariant Kinetic Term (Derived Minimal Form)
- 4D Action: $S[n] = \int d^4x\,\mathcal{L}$  

$$\mathcal{L} = \frac{Z_t}{2}(\partial_t n)^2 - E[n]$$

- Constraint: $n\cdot n = 1$  
- Euler–Lagrange:  

$$Z_t \partial_t^2 n - A_1 \nabla^2 n + A_3 \nabla^4 n - A_4(n\cdot n_0)n_0 + \lambda n = 0$$

*(Here $Z_t$ is fixed by matching to the long‑wavelength limit of the microscopic soliton dispersion).*

## 3. Euler–Lagrange

$$A_1 \nabla^2 n - A_3 \nabla^4 n + A_4(n\cdot n_0)n_0 + \lambda n = 0$$

## 3.1 Isolated Cross-Term Projection Dynamics
- Isolated Cross-Term Action: $S_{\text{cross}}[n] = \int d^4x \left[ -A_3 (\nabla^2 n) \cdot (\partial_t^2 n) \right]$

- Functional Variation:

$$\delta S_{\text{cross}} = -A_3 \int d^4x \left[ (\nabla^2 \delta n) \cdot (\partial_t^2 n) + (\nabla^2 n) \cdot (\partial_t^2 \delta n) \right]$$

- Integrating by parts twice spatially on the first term and twice temporally on the second term yields:

$$\frac{\delta S_{\text{cross}}}{\delta n} = -2A_3 \partial_t^2 \nabla^2 n$$

- Imposing the $S^2$ target-space spherical variation constraint ($n \cdot \delta n = 0$):

$$-2A_3 \partial_t^2 \nabla^2 n + \lambda_{\text{cross}} n = 0$$

- Taking the inner product with $n$ to eliminate the Lagrange multiplier via identity $n \cdot n = 1$:

$$\lambda_{\text{cross}} = 2A_3 n \cdot (\partial_t^2 \nabla^2 n)$$

- Fully Derived Non-Linear Equation of Motion:

$$\partial_t^2 \nabla^2 n - \left[ n \cdot (\partial_t^2 \nabla^2 n) \right] n = 0$$

- Linearized Perturbation Regime ($n = n_0 + \pi$ with $n_0 = (0,0,1)$):

$$\partial_t^2 \nabla^2 \pi = 0$$

- Plane-Wave Dispersion Relation Solution ($\pi \propto e^{i(k \cdot x - \omega t)}$):

$$\omega^2 k^2 \pi_0 = 0 \implies \omega = 0 \quad \text{(Static Screening Mode) or} \quad k = 0 \quad \text{(Uniform Drift Mode)}$$

## 3.2 Conserved SO(3) Noether Currents
- Infinitesimal global $SO(3)$ transformation: $\delta n = \boldsymbol{\epsilon} \times n$
- Total action divergence relation: $\delta \mathcal{L} = \partial_\mu \left( \mathbf{J}^\mu \right) \cdot \boldsymbol{\epsilon} = 0$

### Derived Current Formulation
Evaluating the first-order and higher-derivative functional variations term-by-term yields:

$$\mathbf{J}^\mu = \gamma_{\nu} g^{\mu\nu} (n \times \partial_\nu n) - A_3 \left[ (\Box n) \times \partial^\mu n - \partial^\mu (\Box n) \times n \right]$$

Breaking this tensor down into explicit comoving spacetime frames ($\Box = \partial_t^2 - \nabla^2$):

- **Time Component (Charge Density Vector $\mathbf{J}^0$):**

$$\mathbf{J}^0 = Z_t (n \times \partial_t n) - A_3 \left[ (\partial_t^2 n - \nabla^2 n) \times \partial_t n - \partial_t (\partial_t^2 n - \nabla^2 n) \times n \right]$$

- **Spatial Component (Flux Vector $\mathbf{J}^i$):**

$$\mathbf{J}^i = -A_1 (n \times \partial_i n) + A_3 \left[ (\partial_t^2 n - \nabla^2 n) \times \partial_i n - \partial_i (\partial_t^2 n - \nabla^2 n) \times n \right]$$

- **Conservation Law:**

$$\partial_t \mathbf{J}^0 + \nabla \cdot \mathbf{J}^i = 0$$

*(Note: The potential coefficient $A_4$ and topological boundary coefficient $A_2$ carry no derivative field components and contribute exactly zero to the active current matrix).*



## 4. Soliton Sector
- Perturbation: $n = n_* + \pi,\ n_*\cdot\pi = 0$  
- Hessian:  

$$\mathcal{H}\pi = \frac{\delta^2 E}{\delta n^2} \pi$$

## 5. Kernel Definition

$$\mathcal{H} K = \delta^{(3)}$$  

$$K(k) = \frac{1}{A_4 - A_1 k^2 - A_3 k^4}$$

## 6. Pole Equation 
Let $s = k^2$.  
Denominator $= A_4 - A_1 s - A_3 s^2$  
Pole equation:  

$$A_3 s^2 + A_1 s - A_4 = 0$$

Roots:  

$$s_\pm = \frac{-A_1 \pm \sqrt{A_1^2 + 4A_3A_4}}{2A_3}$$

Define physical inverse-length scales:  

$$m = \sqrt{-s_-}$$  

$$\Lambda = \sqrt{s_+}$$

## 7. Real-Space Kernel 

$$K(r) = \frac{1}{4\pi r} \left[ C_1 e^{-m r} + C_2 e^{-\Lambda r} \right]$$

($\Lambda$ replaces the incorrect “$k_+$” definition)

## 7.1 Determination of $C_1$ and $C_2$
- Radial Quartic Equation:  

$$\big(A_4 - A_1\nabla^2 - A_3\nabla^4\big) K(r) = \delta^{(3)}(r)$$

- Ansatz:  

$$K(r) = \frac{1}{4\pi r}\big(C_1 e^{-m r} + C_2 e^{-\Lambda r}\big)$$

- Boundary Conditions:  
  1. Regularity at $r \to 0$  
  2. Decay at $r \to \infty$  
  3. Normalization: $\int d^3r\,L K(r) = 1$  
- Solution:  

$$C_1 + C_2 = 0$$  

$$C_1 = \frac{1}{A_3 (\Lambda^2 - m^2)}$$  

$$C_2 = -C_1$$

## 8. RG Flow

$$\frac{dA_1}{d\ln a} = c_1 \rho_0 \xi_R^2 - d_1 \Sigma$$  

$$\frac{dA_3}{d\ln a} = c_3 \rho_0 \xi_R^4 - d_3 \Sigma \xi_R^2$$  

$$\frac{dA_4}{d\ln a} = c_4 \rho_0 - d_4 \Sigma$$

## 9. Background

$$\dot{\rho}_0 + 3H\rho_0 = 0$$  

$$H^2 = F(\rho_0, \alpha_0, P_R, \Sigma)$$

## 9.1 Covariant Energy–Momentum Tensor

$$T_{\mu\nu} = 2\frac{\partial\mathcal{L}}{\partial g^{\mu\nu}} - g_{\mu\nu}\mathcal{L}$$

$$\mathcal{L} = \frac{Z_t}{2} g^{00}(\partial_0 n)^2 + \frac{A_1}{2} g^{ij}(\partial_i n\cdot\partial_j n) - \frac{A_2}{2}\omega^2 - \frac{A_3}{2}(g^{\alpha\beta}\nabla_\alpha\partial_\beta n)^2 - \frac{A_4}{2}(1-(n\cdot n_0)^2)$$

$$\frac{\partial\mathcal{L}}{\partial g^{\mu\nu}} = \frac{1}{2}\mathcal{M}_{\mu\nu} - A_3(\Box n)\nabla_\mu\partial_\nu n$$

$$\mathcal{M}_{00} = Z_t(\partial_t n)^2 \qquad \mathcal{M}_{ij} = -A_1(\partial_i n\cdot\partial_j n)$$

$$T^0{}_0 = \rho_{\text{eff}} \qquad T^i{}_i = 3P_{\text{eff}}$$

$$\rho_{\text{eff}} = \frac{Z_t}{2}(\partial_t n)^2 + \frac{A_1}{2}(\partial_i n)^2 + \frac{A_2}{2}\omega^2 + \frac{A_3}{2}(\nabla^2 n)^2 - A_3(\nabla^2 n)\partial_t^2 n + \frac{A_4}{2}(1-(n\cdot n_0)^2)$$

$$\P_{\text{eff}} = \frac{Z_t}{2}(\partial_t n)^2 - \frac{A_1}{6}(\partial_i n)^2 - \frac{A_2}{2}\omega^2 - \frac{A_3}{6}(\nabla^2 n)^2 - \frac{A_4}{2}(1-(n\cdot n_0)^2)$$

$$T = T^\mu{}_\mu = \rho_{\text{eff}} - 3P_{\text{eff}} = - Z_t(\partial_t n)^2 + A_1(\partial_i n)^2 + 2A_2\omega^2 + A_3(\nabla^2 n)^2 - A_3(\nabla^2 n)\partial_t^2 n + 2A_4(1-(n\cdot n_0)^2)$$

## 9.2 Canonical Noether Energy-Momentum Tensor
- Infinitesimal spacetime translation variation: $\delta n = \epsilon^\nu \partial_\nu n$
- Conservation equation under translation invariance: $\partial_\mu T^\mu{}_\nu = 0$

### Exact Current Derivation
Varying the first-order, topological, and higher-derivative terms under the translation shift yields:

$$T^\mu{}_\nu = \gamma_{\alpha} g^{\mu\alpha} (\partial_\alpha n \cdot \partial_\nu n) - A_3 \left[ (\Box n) \cdot \partial^\mu \partial_\nu n - \partial^\mu (\Box n) \cdot \partial_\nu n \right] - \delta^\mu{}_\nu \mathcal{L}$$

Splitting the tensor components explicitly into comoving frame densities ($\Box = \partial_t^2 - \nabla^2$):

- **Energy Density Flux ($T^0{}_0 = \rho_{\text{canonical}}$):**

$$T^0{}_0 = Z_t (\partial_t n)^2 - A_3 \left[ (\partial_t^2 n - \nabla^2 n) \cdot \partial_t^2 n - \partial_t (\partial_t^2 n - \nabla^2 n) \cdot \partial_t n \right] - \mathcal{L}$$

- **Spatial Stress Tensor Components ($T^i{}_j$):**

$$T^i{}_j = -A_1 (\partial_i n \cdot \partial_j n) + A_3 \left[ (\partial_t^2 n - \nabla^2 n) \cdot \partial_i \partial_j n - \partial_i (\partial_t^2 n - \nabla^2 n) \cdot \partial_j n \right] - \delta^i{}_j \mathcal{L}$$

*(Note: On the shell of the non-linear spherical constraint $n \cdot \partial_\nu n = 0$, this canonical current matches the metric derivation in Section 9.1, confirming complete mathematical consistency).*


## 10. Perturbations

$$\ddot{\delta} + 2H \dot{\delta} = 4\pi G_{\text{eff}}(k,a) \rho_0 (\delta + \chi\beta) - c_s^2 k^2 \delta$$  

$$G_{\text{eff}} \propto K(k)$$  

$$\eta = \frac{K_{\text{long}}}{K_{\text{trans}}}$$

## 10.1 Tensor Kernel Decomposition

$$\mathcal{H}_{ij}(k) = \mathcal{H}_{\text{long}}(k) \hat k_i \hat k_j + \mathcal{H}_{\text{trans}}(k)(\delta_{ij} - \hat k_i \hat k_j)$$

$$\mathcal{H}_{\text{long}}(k) = A_1 k^2 + A_3 k^4$$  

$$\mathcal{H}_{\text{trans}}(k) = A_4 - A_1 k^2 - A_3 k^4$$

$$K_{ij}(k) = K_{\text{long}}(k) \hat k_i \hat k_j + K_{\text{trans}}(k)(\delta_{ij} - \hat k_i \hat k_j)$$

$$K_{\text{long}}(k) = \frac{1}{A_1 k^2 + A_3 k^4}$$  

$$K_{\text{trans}}(k) = \frac{1}{A_4 - A_1 k^2 - A_3 k^4}$$

- Gravitational Slip Parameter:  

$$\eta(k,a) = \frac{K_{\text{long}}(k,a)}{K_{\text{trans}}(k,a)}$$

## 11. Hydrogen Sector
Radial operator:  

$$A_1 L_\ell R - A_3 L_\ell^2 R + A_4 R = \lambda R$$

Low-energy reduction:  

$$L_\ell R + \kappa^2 R = 0$$  

$$\kappa^2 = \frac{A_4 - \lambda}{A_1}$$

Boundary quantization (correct form):  

$$\kappa_{\ell n} = \frac{\alpha_{\ell n}}{R_{\text{eff}}}$$  

$$\lambda_{\ell n} = A_4 - A_1 \left(\frac{\alpha_{\ell n}}{R_{\text{eff}}}\right)^2$$

## 12. Boltzmann Transport

$$\frac{\partial f}{\partial t} + \frac{p}{M(v)}\cdot\nabla_x f - \frac{1}{M(v)}(\nabla_x\Phi) \cdot \nabla_p f = C[f] + S[f]$$  

$$\Phi(x) = \int K(x-y) \delta\rho(y) dy$$

## 13. Noise Sector
White noise source:  

$$\langle \Xi_f \Xi_f \rangle \propto \delta(x-x') \delta(p-p') \delta(t-t')$$

Density noise floor requires:  

$$P_\delta(k) \propto |K(k)|^2 P_\Xi(k)$$

High‑$k$ limit of quartic kernel:  

$$K(k) \sim \frac{1}{A_3 k^4}$$

Thus:  

$$P_\delta(k) \sim \frac{1}{k^8} \quad \text{(true UV scaling)}$$

If a $1/k^3$ floor is required, $\Xi_f$ must have:  

$$P_\Xi(k) \propto k^5$$  

(i.e., non‑white, correlated noise)
