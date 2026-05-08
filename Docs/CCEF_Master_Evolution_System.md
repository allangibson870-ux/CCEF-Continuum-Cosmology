# CCEF Master Evolution System v1.3
## RG–Soliton–Scattering Closure Framework

A closed deterministic continuum theory defined entirely by a constrained unit-norm field $n(x,t) \in S^{2}$. All physical structure — solitons, particles, interactions, stochasticity, and scattering — emerges from a single energy functional and its renormalisation group (RG) flow.

No external spacetime, quantum axioms, or cosmological background structures are assumed.

---

### 1. Fundamental Field Structure

**1.1 Primary Constraint**

$$ |n(x,t)| = 1 $$

The field lives on the manifold $S^{2}$.

**1.2 Energy Functional**

$$ E[n] = \int d^{3}x \, \mathcal{E}(n, \partial n, \partial^{2} n) $$

$$ \mathcal{E} = \mathcal{E}_{\nabla} + \mathcal{E}_{\text{top}} + \mathcal{E}_{\text{disp}} + \mathcal{E}_{\text{align}} $$

**Gradient Sector**

$$ \mathcal{E}_{\nabla} = \frac{A_{1}}{2} (\partial_{i} n \cdot \partial_{i} n) $$

**Topological Sector**

$$ \omega(x) = \frac{1}{4\pi}\epsilon_{ijk} (\partial_{i} n \cdot (\partial_{j} n \times \partial_{k} n)) $$

$$ \mathcal{E}_{\text{top}} = \frac{A_{2}}{2}\omega^{2} $$

**Dispersive Sector**

$$ \mathcal{E}_{\text{disp}} = \frac{A_{3}}{2} (\nabla^{2} n \cdot \nabla^{2} n) $$

**Alignment Sector**

$$ \mathcal{E}_{\text{align}} = \frac{A_{4}}{2} (n \cdot n_{0})^{2} $$

**1.3 Functional Derivative**

$$ h = \frac{\delta E}{\delta n} \quad,\quad h_{\perp} = h - (h \cdot n)n $$

**1.4 Microscopic Evolution**

$$ \partial_{t} n = \mathcal{-}\Gamma h_{\perp} + \lambda (n \times h_{\perp}) $$

**1.5 Soliton Condition**

$$ h_{\perp} = 0 $$

---

### 2. Minimal Soliton (Q = 1)

**2.1 Hedgehog Ansatz**

$$ n_{\ast}(x) = \left( \sin f(r)\frac{x}{r}, \cos f(r) \right) $$

**2.2 Profile Function**

$$ f(r) = 2\arctan\left(\frac{R}{r}\right) $$

**2.3 Soliton Scale**

$$ R^{2} \approx \frac{A_{2}}{A_{1}} $$

---

### 3. Kernel (Emergent Structure)

**3.1 Hessian Definition**

$$ K^{-1}(x,y) = \frac{\delta^{2} E}{\delta n(x)\delta n(y)}\Big|_{n=n_{\ast}} $$

**3.2 Fourier Form**

$$ K^{-1}(k) = m^{2} + c_{2} k^{2} + c_{4} k^{4} + \dots $$

---

### 4. Renormalisation Group (RG)

**4.1 Coarse-Graining Scale**

$$ \ell = \ln(L/L_{0}) $$

**4.2 Field Split**

$$ n = n_{<} + n_{>} $$

**4.3 RG Operator**

$$ \boxed{ \mathcal{R}[E] = -\ln \int \mathcal{D}n_{>}\, e^{-E[n_{<} + n_{>}]} } $$

**4.4 Saddle Form**

$$ \mathcal{R}[E] = E[n_{<} + n_{>}^{\ast}] + \frac{1}{2}\mathrm{Tr}\ln \left( \frac{\delta^{2} E}{\delta n^{2}} \right) $$

**4.5 Coupling Flow**

$$ \frac{dA_{i}}{d\ell} = \beta_{i}(A_{j}, K, \sigma_{\alpha}^{2}) $$

---

### 5. Emergent Stochasticity

**5.1 Origin**

$$ \Xi = \text{projection of unresolved RG modes} $$

**5.2 Effective Dynamics**

$$ \beta' + \Gamma_{\beta} \beta = S_{\delta} \delta + \Xi $$

**5.3 Noise Statistics**

$$ \langle \Xi \rangle = 0 $$

$$ \langle \Xi(x)\Xi(y) \rangle = C \sigma_{\alpha}^{2} \delta(x-y) $$

---

### 6. Projection Layer

$$ P_{O}[n] = \int d^{3}y \, W_{O}(x,y)\mathcal{F}_{O}[n(y)] $$

**Observables**

$$ \rho = P_{\rho}[n], \quad u_{i} = \frac{P_{J_{i}}[n]}{\rho} $$

$$ \delta = P_{\delta}[n], \quad \beta = P_{\beta}[n] $$

---

### 7. RG Stability Operator

**7.1 Linearisation**

$$ n = n_{\ast} + \eta $$

**7.2 Eigenvalue Problem**

$$ \boxed{ \hat{\mathcal{L}}_{RG}\eta = \lambda \eta } $$

**7.3 Operator Structure**

$$ \hat{\mathcal{L}}_{RG} = - A_{1} \nabla^{2} + A_{3} \nabla^{4} + V_{\text{eff}}(x) + \mathcal{S}_{\text{Sk}} + K \mathcal{V}^{(3)} $$

Subject to constraint: $n_{\ast} \cdot \eta = 0$

**7.4 First Eigenmodes**

**Translational mode**

$$ \psi^{(0)} = \partial_{i} n_{\ast}, \quad \lambda_{0} = 0 $$

**Breathing mode**

$$ \psi^{(1)}(\rho) \propto \frac{1-\rho^{2}}{(1+\rho^{2})^{2}} \quad,\quad \lambda_{1} \sim \frac{A_{1}}{R^{2}} $$

**Quadrupole mode**

$$ \psi^{(2)}(\rho,\theta) \propto \frac{\rho^{2}}{(1+\rho^{2})^{2}}Y_{2m} \quad,\quad \lambda_{2} \sim \frac{A_{1}}{R^{2}} + \frac{A_{2}}{R^{4}} $$

---

### 8. Cubic Interaction Vertex

**8.1 Definition**

$$ \mathcal{V}^{(3)} = \frac{\delta^{3} E}{\delta n^{3}}\Big|_{n_{\ast}} $$

**8.2 Mode Coupling**

$$ E^{(3)} = \sum_{ijk} g_{ijk} a_{i} a_{j} a_{k} $$

$$ g_{ijk} = \int \psi_{i} \psi_{j} \psi_{k} \mathcal{V}^{(3)} $$

**8.3 Mode Dynamics**

$$ \dot{a}_{n} = -\lambda_{n} a_{n} - \sum_{ij} g_{nij} a_{i} a_{j} $$

---

### 9. Scattering Amplitudes (Emergent S-Matrix)

**9.1 Evolution Operator**

$$ \mathcal{U} = \mathcal{T}\exp\left( -\int d\ell \, \hat{\mathcal{L}}_{RG}^{eff} \right) $$

**9.2 S-Matrix Definition**

$$ \boxed{ S_{fi} = \lim_{\ell \to \infty} \langle f | \mathcal{U} | i \rangle } $$

**9.3 Tree-Level Amplitude**

$$ \mathcal{A}_{ij \to kl} = \sum_{n} \frac{g_{ijn} g_{nkl}}{\lambda_{n} - \lambda_{i} - \lambda_{j}} $$

**9.4 Dressed Propagator Form**

$$ \mathcal{A}_{ij \to kl} = \sum_{n} g_{ijn} G_{n} g_{nkl} $$

$$ G_{n} = \frac{1}{\lambda_{n} + \Sigma_{n}} $$

**9.5 Self-Energy**

$$ \Sigma_{n} = \sum_{ij} \frac{g_{nij}^{2}}{\lambda_{i} + \lambda_{j}} $$

---

### 10. Fixed Points and Universality

$$ \mathcal{R}[E_{\ast}] = E_{\ast} $$

$$ \mathcal{U}_{Q} = \{E : Q \text{ invariant under RG}\} $$

---

### 11. System Closure

All physics reduces to:

$$ n \rightarrow E[n] \rightarrow \frac{\delta^{2} E}{\delta n^{2}} \rightarrow K \rightarrow \mathcal{R}[E] \rightarrow \hat{\mathcal{L}}_{RG} \rightarrow g_{ijk} \rightarrow S_{fi} $$

---

### Final Statement

CCEF is a closed deterministic continuum system in which:
- **solitons** = RG fixed points
- **particles** = eigenmodes of RG stability operator
- **interactions** = cubic functional curvature
- **scattering** = RG-resummed mode coupling
- **stochasticity** = unresolved RG projection
