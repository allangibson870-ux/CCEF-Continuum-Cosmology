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

#### 1. Statement of the Problem
All collective response, emergent long-range behaviour, effective coupling strengths, and perturbation sourcing must originate from the microscopic field $n(x,t)$. The central object is the soliton interaction kernel $K(r)$ (or $K(k)$ in Fourier space). This kernel must be derived explicitly from the fundamental energy functional via linear response around a soliton background. No external propagators, no imported Poisson equations, and no assumed force laws are permitted. Residual freedoms in the kernel shape must be eliminated by internal consistency.

#### 2. Starting Definitions
Single soliton background (hedgehog configuration):

$$n\_{ \ast }(x) = \bigl( \sin f(r) \hat{r}, \cos f(r) \bigr), \qquad f(r) \approx 2\arctan(R/r)$$

where $R$ is the stable radius obtained by minimizing $M(R) = E[n\_{ \ast }]$.

Perturbation around the soliton:

$$n(x) = n\_{ \ast }(x) + \pi(x), \qquad n\_{ \ast } \cdot \pi = 0$$

The Hessian operator is the second functional derivative:

$$(\mathcal{H} \pi)^{i}(x) \equiv \left. \frac{\delta^{2} E}{\delta n^{i}(x)\delta n^{j}(y)} \right|\_{n\_{ \ast }} \pi^{j}(y)$$

The interaction kernel $K(x-y)$ is defined as the Green function of this operator: it maps the effective source created by one soliton to the response field $\pi$ felt by another.

#### 3. Derivation

**3.1 Construction of the Hessian from the Energy Functional**
Start with the microscopic energy density:

$$\mathcal{E} = \frac{A_1}{2} |\partial_i n|^2 + \frac{A_2}{2} \omega^2 + \frac{A_3}{2} |\nabla^2 n|^2 + \frac{A_4}{2} (n \cdot n_0)^2$$

Expand $E[n_* + \pi]$ to quadratic order in the transverse field $\pi$. After lengthy but straightforward projection onto the plane perpendicular to $n_*$, the resulting Hessian $\mathcal{H}$ is a linear, self-adjoint, elliptic differential operator acting on $\pi$.

It contains:
* Second-order spatial derivatives from the $A_1$ term,
* Projected contributions from the topological density $\omega$ (via $A_2$),
* Fourth-order derivatives from the dispersive $A_3$ term,
* Effective mass-like terms from $A_4$ and the background curvature induced by $n_*$.

In the far-field region ($r \gg R$), where $n_* \approx n_0 + \mathcal{O}(1/r^2)$, the operator simplifies to a massive vector wave operator projected transverse to $n_0$.

**3.2 Sourced Linear Response**
A second distant soliton (centered at separation $d \gg R$) acts as an effective source $J(x-d)$ for the perturbation $\pi$ around the first soliton. The linearized equation is:

$$\mathcal{H} \pi(x) = J(x - d)$$

The solution is the convolution $\pi(x) = \int K(x - y) \, J(y - d) \, d^3 y$, where $K(x-y)$ is the Green function (fundamental solution) satisfying:

$$\mathcal{H} K(x-y) = \delta^{(3)}(x-y) \quad \text{(projected to transverse directions)}$$

**3.3 Far-Field Kernel and Momentum-Space Form**
In Fourier space the Green function takes the generic form:

$$K(k) = \frac{A(a)}{k^2 + m^2(a)} + \frac{B(a)}{k^2 + \Lambda^2(a)} + \mathcal{O}(k^4 \text{ terms})$$

where:
* The leading massless or light channel ($m(a) \to 0$) produces the long-range $1/r$ tail.
* $m(a) \approx 1/\xi_R(a)$ is controlled by the correlation length.
* $\Lambda(a) \approx 1/R$ encodes core-scale suppression.
* Amplitudes $A(a)$ and $B(a)$ are fixed by overlap integrals of the soliton profile.

**3.4 Dual-Channel Structure (Internal Derivation)**
The Hessian $\mathcal{H}$ admits distinct eigenchannels because $\pi$ lives in the tangent plane to $S^2$:
* Longitudinal/compressional modes (coupling primarily to density variations),
* Transverse/shear-like distortions.

Projecting the response onto these channels naturally yields two kernels $K$ and $K_2$, with the slip parameter $\eta$ emerging from their ratio.

**3.5 Elimination of Residual Shape Freedom**
The shape function $f(k,a)$ in the anisotropic projection $K_2 = K[1 + \varepsilon(a) f(k,a)]$ is fixed by Section 06 logic, yielding $f(k,a) = C(a) k^2$.

#### 4. Result
The soliton interaction kernel is derived as:

$$K(k,a) = \frac{A(a)}{k^2 + m^2(a)} + \frac{B(a)}{k^2 + \Lambda^2(a)}$$

#### 5. Conditions for Cosmology
* Correct infrared ($k \to 0$) response strength.
* Long-range channel ($m \to 0$) must emerge dynamically.
* Dual-channel splitting must be traceable to the same microscopic Hessian.
* Amplitudes must scale with background density $\rho_0(a)$.

#### 6. Notes
The kernel is the Green function of the derived Hessian. Once numerical computation of $\mathcal{H}$ is complete, all higher-level sectors (RG flow, perturbations, background closure) become fully determined.


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
