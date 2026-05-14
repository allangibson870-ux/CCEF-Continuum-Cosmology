# CCEF — Minimal Mathematical Backbone 

## 1. Field & Constraint
- Field: $n(x,t) \in S^2,\ |n| = 1$  
- Variation constraint: $n\cdot\delta n = 0$  
- Topological density:  
  $\omega = \frac{1}{4\pi} \epsilon_{ijk} n\cdot(\partial_j n \times \partial_k n)$

## 2. Energy Functional

$$E[n] = \int d^3x \left[ \frac{A_1}{2}(\partial_i n)^2 + \frac{A_2}{2} \omega^2 + \frac{A_3}{2}(\nabla^2 n)^2 + \frac{A_4}{2}(1 - (n\cdot n_0)^2) \right]$$

## 3. Euler–Lagrange

$$A_1 \nabla^2 n - A_3 \nabla^4 n + A_4(n\cdot n_0)n_0 + \lambda n = 0$$

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

## 8. RG Flow

$$\frac{dA_1}{d\ln a} = c_1 \rho_0 \xi_R^2 - d_1 \Sigma$$  

$$\frac{dA_3}{d\ln a} = c_3 \rho_0 \xi_R^4 - d_3 \Sigma \xi_R^2$$  

$$\frac{dA_4}{d\ln a} = c_4 \rho_0 - d_4 \Sigma$$

## 9. Background

$$\dot{\rho}_0 + 3H\rho_0 = 0$$  

$$H^2 = F(\rho_0, \alpha_0, P_R, \Sigma)$$

## 10. Perturbations

$$\ddot{\delta} + 2H \dot{\delta} = 4\pi G_{\text{eff}}(k,a) \rho_0 (\delta + \chi\beta) - c_s^2 k^2 \delta$$  

$$G_{\text{eff}} \propto K(k)$$  

$$\eta = \frac{K_{\text{long}}}{K_{\text{trans}}}$$

## 11. Hydrogen Sector
Radial operator:  

$$A_1 L_\ell R - A_3 L_\ell^2 R + A_4 R = \lambda R$$

Low-energy reduction:  

$$L_\ell R + \kappa^2 R = 0$$  

$$\kappa^2 = \frac{A_4 - \lambda}{A_1}$$

Boundary quantization (correct form):  

$$\kappa_{\ell n} = \frac{\alpha_{\ell n}}{R_{\text{eff}}}$$  

$$\lambda_{\ell n} = A_4 - A_1 \left(\frac{\alpha_{\ell n}}{R_{\text{eff}}}\right)^2$$

(REMOVED incorrect Rydberg scaling)

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
