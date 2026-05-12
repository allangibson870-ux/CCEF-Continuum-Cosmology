# Spine v1.0: Theoretical Framework

## 0. Purpose & Ontological Commitment
The universe is described by a single constrained continuum field $n(x,t)$ with $|n(x,t)| = 1$.  
No spacetime geometry, no gauge fields, no quantum axioms, and no separate matter or force fields are assumed. All observable structure (particles, forces, cosmology, emergent geometry) must arise deterministically from the internal dynamics, topology, and coarse-grained behavior of this field.

**Closure Principle:** Every effective quantity must ultimately be a function of the state vector:
$X = \{ n(x,t),\ \xi_R,\ \rho_0,\ \delta,\ \beta,\ \sigma_\alpha^2,\ \dots \}$  
No free external functionals allowed.

## 1. Primitive Ontology & Constraint
*   **Single unit-norm field:** $n(x,t) \in S^2$, $|n| = 1$.
*   **Uniform vacuum:** $n(x,t) = n_0$.
*   **Variations:** All variations preserve the constraint $n \cdot \delta n = 0$.
*   **Derived:** Internal evolution occurs on the nonlinear manifold $S^2$.

## 2. Fundamental Energy Functional & Dynamics
**Axiom — Energy functional:**
$$E[n] = \int d^3x \left[ \frac{A_1}{2} |\nabla n|^2 + \frac{A_2}{2} \omega^2 + \frac{A_3}{2} (\nabla^2 n)^2 + \frac{A_4}{2} (n \cdot n_0)^2 \right]$$
with topological density $\omega = \frac{1}{4\pi} \epsilon_{ijk} n \cdot (\partial_j n \times \partial_k n)$.

**Derived Dynamics:** Projected Landau-Lifshitz-Gilbert-type equation:
$$\partial_t n = -\Gamma h_\perp + \Lambda (n \times h_\perp), \quad h = \frac{\delta E}{\delta n}$$

## 3. Soliton Sector
*   **Hedgehog ansatz:** $n_*(r) = (\sin f(r) \hat{r}, \cos f(r))$.
*   **Stable radius:** $R$ from minimization of $M(R) = E[n_*]$.
*   **Topological charge:** $Q \in \mathbb{Z}$ labels soliton species.
*   **Mass:** $M = E[n_*]$, response charge $q$, coupling $\alpha = q/M$.

**Status:** Analytic profile known; exact stability and spectrum requires numerics.

## 4. Linear Response & Hessian
*   **Perturbation:** $n = n_* + \pi$, where $n_* \cdot \pi = 0$.
*   **Hessian operator:** $\mathcal{H} = \frac{\delta^2 E}{\delta n^2} \big|_{n_*}$.
*   **Eigenmodes:** Zero modes (translations), shape/breathing modes, radiation modes.
*   **Mode expansion:** $\pi(x,t) = \sum a_i(t) \psi_i(x)$.

**Status:** Formalism established. Explicit spectrum pending.

## 5. Soliton Interaction Kernel (Critical Bridge)
The effective response kernel $K(r)$ (or $K(k)$) between solitons is derived from the linearized theory around a soliton background.

**Derivation Path:**
1. Compute Hessian $\mathcal{H}$ around one soliton.
2. Solve sourced linearized equation $\mathcal{H} \pi = J_{\rm source}$ for a second distant soliton.
3. Extract Green function $K(x-y)$ of $\mathcal{H}$.

**Derived Form:**
$$K(k) = \frac{A}{k^2 + m^2} + \frac{B}{k^2 + \Lambda^2} + \dots$$

*   **Long-range regime ($m \to 0$):** $K(r) \sim 1/r$
*   **Screened regime:** Yukawa falloff.
*   **Amplitude:** $A$ determined by background density and profile overlaps.

**Status:** Formal derivation outlined. Needs explicit computation/numerics.

## 6. Coarse-Graining & RG Flow
*   Block transformation + Wilsonian coarse-graining of the kernel and soliton ensemble.
*   Flow equations for $\xi_R(\ell)$, $A_i(\ell)$, $\sigma_\alpha^2(\ell)$.
*   **Fixed points:** Long-range coherent phase, screened phase, etc.

**Status:** Schematic beta functions exist. Explicit flows pending.

## 7. Collective Variables & Statistical Sector
*   **Inertial density:** $\rho = \langle M \rangle$ (coarse-grained)
*   **Response density:** $\sigma = \alpha \rho$
*   **Coupling field:** $\alpha(x,t) = \sigma / \rho$
*   **Variance:** $\sigma_\alpha^2$
*   **Correlation length:** $\xi_R$

Conservation laws and momentum balance derived from soliton ensemble averaging.

## 8. Background Expansion Closure
*   **Homogeneous state:** $\rho_0(a)$, $\alpha_0(a)$, $u = H(t) x$
*   **Continuity:** $\dot{\rho}_0 + 3H\rho_0 = 0$
*   **Closure relation:** $H^2 = F(\rho_0, \alpha_0, P_R, \Sigma)$ (to be derived from kernel + pressure)
*   **Acceleration:** Occurs when effective response pressure $P_R < -\rho_0/3$.

**Status:** Form established. Functional $F$ requires derivation from soliton gas + kernel.

## 9. Perturbation Equations
Linearized system for $\delta, \beta, \theta$ sourced by the derived kernel $K(k,a)$.
**Growth equation:**
$$\ddot{\delta} + 2H\dot{\delta} = 4\pi G_{\rm eff}(k,a) \rho_0 [\delta + \chi \beta] - c_s^2 k^2 \delta + \dots$$
All coefficients must descend from $K(k,a)$, $\xi_R$, and $\rho_0$.

## 10. Global Consistency Conditions
All sectors (kernel, background, perturbations, RG flow, noise floor, soliton masses) must close without external functions or contradictions.

## 11. Phases of the Continuum
Phase diagram in $(\xi_R, \sigma_\alpha^2)$:
1. Coherent long-range phase
2. Screened phase
3. Stochastic floor
4. Acceleration phase

## 12. Observables & Projections
*   Growth rate $f\sigma_8$
*   Slip parameter $\eta$
*   Scale-dependent clustering
*   Effective expansion history

All treated as projections of the underlying continuum (non-ontological translation layer).

## 13. Status Ledger & Open Items
*   **Solid:** Ontology, energy functional, dynamics, soliton ansatz, formal linear response.
*   **Partially Derived:** Kernel structure, collective equations.
*   **Needs Work:** Explicit Hessian spectrum, numerical soliton interactions, explicit RG betas, background closure $F$, full consistency audit.

***

### Appendices
*   **A. Detailed Calculations & Numerics**
*   **B. Interpretive Mappings to GR / Standard Cosmology**
*   **C. Supporting Documents Index**
