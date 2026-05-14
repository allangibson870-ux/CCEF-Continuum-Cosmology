# CCEF — Minimal Mathematical Backbone

## 1. Field & Constraint
- Field: $n(x,t)\in S^2,\ |n|=1$
- Variation constraint: $n\cdot\delta n=0$
- Topological density:  
  $\omega=\frac{1}{4\pi}\epsilon_{ijk}n\cdot(\partial_j n\times\partial_k n)$

## 2. Energy Functional

$$E[n]=\int d^3x\left[ \frac{A_1}{2}(\partial_i n)^2 +\frac{A_2}{2}\omega^2 +\frac{A_3}{2}(\nabla^2 n)^2 +\frac{A_4}{2}(1-(n\cdot n_0)^2) \right]$$

## 3. Euler–Lagrange / Dynamics

$$A_1\nabla^2 n - A_3\nabla^4 n + A_4(n\cdot n_0)n_0 + \lambda n = 0$$

$$\partial_t n = -\Gamma h_\perp + \Lambda(n\times h_\perp),\quad h=\frac{\delta E}{\delta n}$$

## 4. Soliton Sector
- Hedgehog:  
  $n_*=(\sin f(r)\hat r,\ \cos f(r))$
- Mass: $M=E[n_*]$
- Perturbation: $n=n_*+\pi,\ n_*\cdot\pi=0$

## 5. Hessian

$$(\mathcal{H}\pi)_i(x)=\int d^3y\,\frac{\delta^2E}{\delta n_i(x)\delta n_j(y)}\pi_j(y)$$

Eigenmodes: $\mathcal{H}\psi_i=\lambda_i\psi_i$

## 6. Kernel (Green Function)

$$\mathcal{H}K=\delta^{(3)},\qquad \pi(x)=\int K(x-y)J(y)\,dy$$

## 7. Quartic Kernel Form

$$K(k,a)=\frac{1}{A_4(a)-A_1(a)k^2-A_3(a)k^4}$$

Pole equation:  

$$A_3 s^2 + A_1 s - A_4 = 0,\quad s=k^2$$

Roots:

$$s_\pm=\frac{-A_1\pm\sqrt{A_1^2+4A_3A_4}}{2A_3}$$

Define:

$$m^2=-s_-,\qquad k_+^2=s_+$$

Real-space:

$$K(r)=\frac{1}{4\pi r}(C_1 e^{-mr}+C_2 e^{-k_+ r})$$

## 8. RG Flow

$$\frac{dA_1}{d\ln a}=c_1\rho_0\xi_R^2-d_1\Sigma$$

$$\frac{dA_3}{d\ln a}=c_3\rho_0\xi_R^4-d_3\Sigma\xi_R^2$$

$$\frac{dA_4}{d\ln a}=c_4\rho_0-d_4\Sigma$$

## 9. Background

$$\dot{\rho}_0+3H\rho_0=0$$

$$H^2=F(\rho_0,\alpha_0,P_R,\Sigma)$$

## 10. Perturbations

$$\ddot{\delta}+2H\dot{\delta} =4\pi G_{\text{eff}}(k,a)\rho_0(\delta+\chi\beta) -c_s^2 k^2\delta$$

$$G_{\text{eff}}(k,a)\propto K(k,a)$$

$$\eta(k,a)=\frac{K_{\text{long}}}{K_{\text{trans}}}$$

## 11. Hydrogen (Minimal)
Radial operator:

$$A_1 L_\ell R - A_3 L_\ell^2 R + A_4 R = \lambda R$$

Low-energy reduction:

$$L_\ell R + \kappa^2 R = 0,\qquad \kappa^2=\frac{A_4-\lambda}{A_1}$$

Quantization:

$$\kappa_{\ell n}=\frac{\alpha_{\ell n}}{R_{\text{eff}}}$$

Spectrum:

$$E_{n,\ell}\propto -\frac{1}{(n+\ell+1)^2}$$

## 12. Boltzmann Sector

$$\frac{\partial f}{\partial t} +\frac{p}{M(v)}\cdot\nabla_x f -\frac{1}{M(v)}(\nabla_x\Phi)\cdot\nabla_p f =C[f]+S[f]$$

$$\Phi(x)=\int K_{\text{ensemble}}(x-y)\,\delta\rho(y)\,dy$$

## 13. Noise Floor

$$S[f]=\nabla_p\cdot(D_p\nabla_p f)+\Xi_f$$

$$\langle \Xi_f(x,p,t)\Xi_f(x',p',t')\rangle =\left(\frac{\sigma_\alpha^2\hbar_{\text{eff}}}{\rho_0 c_n^3}\right) \delta(x-x')\delta(p-p')\delta(t-t')$$

$$P_{\delta,\text{noise}}(k)\propto \frac{1}{k^3}$$
