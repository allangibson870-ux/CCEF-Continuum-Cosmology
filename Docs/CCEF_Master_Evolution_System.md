# CCEF Master Evolution System v1.2 (Closed RG-Soliton Formulation)

A closed deterministic continuum theory based on a single constrained field $n(x,t) \in S^{2}$, where all physical structure, solitons, interactions, stochasticity, and large-scale behavior emerge from an energy functional and its renormalisation group (RG) flow.

No external spacetime, quantum postulates, or cosmological inputs are assumed. All scales and observables are emergent.

---

# 1. Fundamental Field Theory

## 1.1 Primary Constraint

$$ |n(x,t)| = 1 $$

The system is defined entirely on the unit sphere manifold $S^{2}$.

---

## 1.2 Energy Functional

$$ E[n] = \int d^{3}x \, \mathcal{E}(n, \partial n, \partial^{2} n) $$

$$ \mathcal{E} = \mathcal{E}_{\nabla} + \mathcal{E}_{\text{top}} + \mathcal{E}_{\text{disp}} + \mathcal{E}_{\text{align}} $$

---

### Gradient Sector

$$ \mathcal{E}_{\nabla} = \frac{A_{1}}{2} (\partial_{i} n \cdot \partial_{i} n) $$

---

### Topological (Skyrme) Sector

$$ \omega(x) = \frac{1}{4\pi}\epsilon_{ijk} (\partial_{i} n \cdot (\partial_{j} n \times \partial_{k} n)) $$

$$ \mathcal{E}_{\text{top}} = \frac{A_{2}}{2}\omega^{2} $$

---

### Dispersive Sector

$$ \mathcal{E}_{\text{disp}} = \frac{A_{3}}{2} (\nabla^{2} n \cdot \nabla^{2} n) $$

---

### Alignment Sector

$$ \mathcal{E}_{\text{align}} = \frac{A_{4}}{2} (n \cdot n_{0})^{2} $$

---

## 1.3 Functional Derivative

$$ h = \frac{\delta E}{\delta n} \quad,\quad h_{\perp} = h - (h \cdot n)n $$

---

## 1.4 Microscopic Evolution

$$ \partial_{t} n = -\Gamma h_{\perp} + \lambda (n \times h_{\perp}) $$

---

## 1.5 Soliton Condition

$$ h_{\perp} = 0 $$

defines stationary soliton solutions.

---

# 2. Minimal Soliton Construction

## 2.1 Hedgehog Ansatz (Q = 1)

$$ n_{*}(x) = \left( \sin f(r)\frac{x}{r}, \cos f(r) \right) $$

---

## 2.2 Profile Function

$$ f(r) = 2\arctan\left(\frac{R}{r}\right) $$

---

## 2.3 Boundary Conditions

$$ f(0) = \pi \quad,\quad f(\infty) = 0 $$

---

## 2.4 Soliton Scale

$$ R^{2} \approx \frac{A_{2}}{A_{1}} $$

---

# 3. Kernel (Derived Structure)

## 3.1 Definition

$$ K^{-1}(x,y) = \frac{\delta^{2} E}{\delta n(x)\delta n(y)}\Big|_{n=n_{*}} $$

---

## 3.2 Fourier Form

$$ K^{-1}(k) = m^{2} + c_{2} k^{2} + c_{4} k^{4} + \dots $$

---

## 3.3 Response Field

$$ \Phi(x) = \int d^{3}y\,K(x,y)n(y) $$

---

## 3.4 Interaction Energy

$$ E_{\text{int}} = \frac{1}{2}\int d^{3}x\, n(x)\Phi(x) $$

---

# 4. Renormalisation Group (RG)

## 4.1 Coarse-Graining Scale

$$ \ell = \ln(L/L_{0}) $$

---

## 4.2 Field Split

$$ n = n_{<} + n_{>} $$

---

## 4.3 RG Operator

$$ \boxed{ \mathcal{R}[E] = -\ln \int \mathcal{D}n_{>}\, e^{-E[n_{<} + n_{>}]} } $$

---

## 4.4 Saddle Form

$$ \mathcal{R}[E] = E[n_{<} + n_{>}^{*}] + \frac{1}{2}\mathrm{Tr}\ln \left( \frac{\delta^{2} E}{\delta n^{2}} \right) $$

---

## 4.5 Coupling Flow

$$ \frac{dA_{i}}{d\ell} = \beta_{i}(A_{j}, K, \sigma_{\alpha}^{2}) $$

---

# 5. Emergent Stochasticity

## 5.1 Origin

$$ \Xi = \text{projection of unresolved RG modes} $$

---

## 5.2 Effective Dynamics

$$ \beta' + \Gamma_{\beta} \beta = S_{\delta} \delta + \Xi $$

---

## 5.3 Statistics

$$ \langle \Xi \rangle = 0 $$

$$ \langle \Xi(x)\Xi(y) \rangle = C \sigma_{\alpha}^{2} \delta(x-y) $$

---

# 6. Projection Layer

$$ P_{O}[n] = \int d^{3}y\,W_{O}(x,y)\mathcal{F}_{O}[n(y)] $$

---

## Observables

$$ \rho = P_{\rho}[n],\quad u_{i} = \frac{P_{J_{i}}[n]}{\rho} $$

$$ \delta = P_{\delta}[n],\quad \beta = P_{\beta}[n] $$

---

# 7. RG Stability Operator

## 7.1 Linearisation

$$ n = n_{*} + \eta $$

---

## 7.2 Eigenvalue Problem

$$ \boxed{ \hat{\mathcal{L}}_{RG}\eta = \lambda \eta } $$

---

## 7.3 Operator Form

$$ \hat{\mathcal{L}}_{RG} = - A_{1} \nabla^{2} + A_{3} \nabla^{4} + V_{\text{eff}}(x) + \mathcal{S}_{\text{Sk}} + K \mathcal{V}^{(3)} $$

subject to:

$$ n_{*} \cdot \eta = 0 $$

---

# 8. Radial Fluctuation Operator

## 8.1 Reduced Form

$$ \left[ - \partial_{\rho}^{2} - \frac{2}{\rho}\partial_{\rho} + \frac{\ell(\ell+1)}{\rho^{2} } + \frac{4}{(1+\rho^{2})^{2}} \right]\psi = \epsilon \psi $$

---

# 9. First Three Eigenmodes

## 9.1 Translational Mode

$$ \psi^{(0)} = \partial_{i} n_{*} \quad,\quad \lambda_{0} = 0 $$

---

## 9.2 Breathing Mode

$$ \psi^{(1)}(\rho) \propto \frac{1-\rho^{2}}{(1+\rho^{2})^{2}} \quad,\quad \lambda_{1} \sim \frac{A_{1}}{R^{2}} $$

---

## 9.3 Quadrupole Mode

$$ \psi^{(2)}(\rho,\theta) \propto \frac{\rho^{2}}{(1+\rho^{2})^{2}}Y_{2m} \quad,\quad \lambda_{2} \sim \frac{A_{1}}{R^{2}} + \frac{A_{2}}{R^{4}} $$

---

# 10. Fixed Points and Universality

$$ \mathcal{R}[E_{\ast}] = E_{\ast} $$

$$ \mathcal{U}_{Q} = \{E : Q \text{ invariant under RG}\} $$


---

# 11. Mass Spectrum

$$ m \sim \min(\lambda_{n}) $$

Mass = lowest nonzero eigenvalue of RG stability operator.

---

# 12. System Closure

$$ n \rightarrow E[n] \rightarrow \frac{\delta^{2} E}{\delta n^{2}} \rightarrow K \rightarrow \mathcal{R}[E] \rightarrow E' \rightarrow n' $$

---

# Final Statement

CCEF is a closed deterministic continuum system in which:

- solitons are RG fixed-point configurations
- kernels are Hessian inverses of energy curvature
- stochasticity emerges from RG truncation
- particles correspond to eigenmodes of RG stability
- mass is an eigenvalue of deformation stability
