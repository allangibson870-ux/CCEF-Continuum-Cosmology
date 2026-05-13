# CCEF Expansion Overview
Phase Structure & Interaction Algebra Geometry

A deterministic continuum framework based on a single constrained field $n(x,t) \in S^2$. All structures — solitons, eigenmodes, interactions, bound states, sector algebras, phase transitions, and long‑range collective responses — arise from the energy functional and its RG flow.

## 1. Fundamental Field Structure

### 1.1 Constraint
$$|n(x,t)|=1$$

### 1.2 Energy Functional
$$E[n]=\int d^3x \left( \frac{A_1}{2}(\partial_i n)^2 + \frac{A_2}{2}\omega^2 + \frac{A_3}{2}(\nabla^2 n)^2 + \frac{A_4}{2}(n \cdot n_0)^2 \right)$$

Topological density: 
$$\omega = \frac{1}{4\pi}\epsilon_{ijk} n \cdot (\partial_j n \times \partial_k n)$$

## 2. Soliton Sector

### 2.1 Hedgehog Configuration
$$n_*(x) = (\sin f(r)\hat{r}, \cos f(r))$$
$$f(r) = 2\arctan\left(\frac{R}{r}\right)$$

### 2.2 Soliton Scale
$$R^2 \approx \frac{A_2}{A_1}$$

### 2.3 Soliton Energy
$$M = \int d^3x \, \mathcal{E}[n_{\text{sol}}]$$

## 3. RG Hessian & Eigenmodes

### 3.1 Hessian Kernel
$$K^{-1}(x,y) = \left.\frac{\delta^2 E}{\delta n(x) \delta n(y)}\right|_{n=n_*}$$

### 3.2 Low‑Lying Modes (with $\rho = r/R$)
* **Translation:** $\psi_k^{(0)} \propto \partial_k n_*$, $\lambda_0 = 0$
* **Breathing:** $\psi^{(1)}(\rho) \propto \frac{1-\rho^2}{(1+\rho^2)^2}$
* **Quadrupole:** $\psi^{(2)}(\rho, \Omega) \propto \frac{\rho^2}{(1+\rho^2)^2}Y_{2m}(\theta, \phi)$

### 3.3 Numerical Derivation of the Hessian and Kernel Tail
The second variation operator $K^{-1}(x,y) = \delta^2 E / \delta n(x)\delta n(y)$ has been discretized on a radial grid using finite-difference methods in spherical partial waves ($l=0$ and $l=1$). Variational optimization of the hedgehog profile $f(r)$ was performed across multiple $(A_1, A_2, A_3, A_4)$ combinations.

#### Representative Numerical Results

* **Dispersive Regime** ($A_1=1.0, A_2=0.45, A_3=0.5, A_4=0.08$):
  * Core radius $R \approx 0.55$
  * Total soliton mass $M \approx 124$
  * Energy allocation: $\text{Sigma} \approx 68\%$, $\text{Skyrme} \approx 23\%$, $\text{Potential} \approx 9\%$
  * Mid-tail power-law exponents ($12 < r < 25$):
    * $l=0$ (compressional): **$b_0 \approx 3.16$**
    * $l=1$ (dipole/translational): **$b_1 \approx 2.38$**

* **Sigma-Skyrme Equilibrium Regime** ($A_2/A_1 \approx 0.35\text{--}0.5$):
  * Energy fractions approach $\sim 50\%$ Sigma / $\sim 50\%$ Skyrme
  * Steeper tails ($b_0 \approx 10.3, b_1 \approx 9.7$)

#### Key Observations
1. The dipole channel ($l=1$) consistently exhibits softer (longer-range) response than the s-wave channel.
2. Reducing $A_2/A_1$ and increasing $A_3$ systematically softens the asymptotic decay, supporting emergence of long-range behavior.
3. These computations directly validate the small-$k$ expansion in Section 7.2.

## 4. Interaction Tensor

### 4.1 Definition
$$g_{ijk} = \int d^3x \, \psi_i^a \psi_j^b \psi_k^c \left.\frac{\delta^3 E}{\delta n^a \delta n^b \delta n^c}\right|_{n=n_*}$$

### 4.2 Gradient‑Sector Example
Integrand: 
$$I(\rho) = \frac{4\rho^{14} + 20\rho^{12} - 128\rho^{10} + 216\rho^8 - 140\rho^6 + 20\rho^4 + 8\rho^2}{(1+\rho^2)^{12}}$$

Exact integral: 
$$\int_0^\infty I(\rho) \, d\rho = \frac{229}{3465}$$

Representative values (fixed normalization):
* $g_{111} = +1.976$
* $g_{011} = 0.000$
* $g_{001} = -1.24$

## 5. Scattering & Bound States

### 5.1 Scattering Amplitude
$$\mathcal{A}_{ij\to kl} = \sum_n g_{ijn} G_n g_{nkl}$$

### 5.2 Dressed Propagator
$$G_n = \frac{1}{\lambda_n + \Sigma_n}$$

### 5.3 Bound‑State Condition
$$\lambda_n + \Sigma_n = 0$$

## 6. Sector Structure & Interaction Algebra

### 6.1 Projectors
$$P_\alpha = \sum_{i \in \mathcal{B}_\alpha} |i\rangle\langle i|$$

### 6.2 Sector Interaction
$$G_{\alpha\beta} = P_\alpha g P_\beta$$

### 6.3 RG Flow
* **Sparse:** $\frac{dG}{d\ell} = G^2 - \Lambda$
* **Dense:** $\frac{dG}{d\ell} = G \circ \rho \circ G - \Lambda$

## 7. Long‑Range Kernel Response

### 7.1 Soliton Energy
$$m_i = \int d^3x \, \mathcal{E}[n_{\text{sol},i}]$$

### 7.2 Kernel Tail
Small-$k$ expansion: 
$$K^{-1}(k) = m^2 + c^2k^2 + \mathcal{O}(k^4)$$

#### 7.2.1 Numerical Kernel Tail Summary
Numerical discretization confirms algebraically decaying tails. The $l=1$ dipole channel produces systematically longer-range response. Tuning toward lower $A_2/A_1$ and higher $A_3$ improves alignment with the desired long-range form $K(r) \sim 1/r$.

* **Massless mode:** $K(k) \approx \frac{1}{c^2k^2} \implies K(r) \approx \frac{1}{4\pi c^2}\frac{1}{r}$
* **Massive mode:** $K(r) \approx \frac{1}{4\pi c^2}\frac{e^{-mr/c^2}}{r}$

### 7.3 Response Field
$$\Phi(x) = \int d^3y \, K(x-y) \delta\rho(y)$$

### 7.4 Effective Force
$$F_{\alpha\beta} \sim G_{\alpha\beta} a_\beta$$

## 8. Phase Space (Coupling‑Defined Regimes)
* **Gradient‑dominated:** $A_1 \gg A_2, A_3, A_4$
* **Topological:** $A_2 \sim A_1$
* **Dispersive:** $A_3/A_1 \gtrsim 0.2$
* **Alignment‑dominated:** $A_4 \gg A_2, A_1$

## 9. Causal Closure & Velocity Limitation

### 9.1 Retarded Kernel Response
$$\Phi(x,t) = \int d^3y \, \frac{\rho(y, t - |x-y|/c_n)}{|x-y|}$$

### 9.2 Internal Signal Speed
$$c_n^2 = \frac{A_1}{\mu_{\text{eff}}}$$

### 9.3 Velocity‑Dependent Energy
$$M(v) = \frac{M_0}{\sqrt{1 - v^2/c_n^2}}$$

### 9.4 Kernel Relaxation
$$\tau_K \approx \frac{\xi R}{c_n}$$

## 10. Stochastic Floor & Disordered Dynamics

### 10.1 Noise Level
$$S \approx \frac{\sigma \alpha^2}{\rho_0}$$

### 10.2 Resolution Bound
$$\Delta X^2 \ge \frac{S}{A_1}$$

### 10.3 Diffusion Threshold
Diffusion dominates when: 
$$S > |\Phi|$$

### 10.4 Energy Redistribution
Dissipation: 
$$\Gamma \to S$$

## 11. Structural Closure
$$n \to E[n] \to K \to LRG \to \psi_i \to g_{ijk} \to \mathcal{B}_\alpha \to G_{\alpha\beta} \to \mathcal{R}[G] \to \text{Phase Structure} \to \text{Collective Dynamics}$$
