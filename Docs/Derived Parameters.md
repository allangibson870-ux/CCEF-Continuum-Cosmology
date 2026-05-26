# CCEF / Spine v1.2.1 — Derived Parameters Summary (Principal-Symbol Consistent Physical Branch)
---
## Core Structural Parameters (Energy Functional) — Physical Branch
* **$A_1 = 1.0$**  
  → Quadratic gradient tension $|\nabla n|^2$. Axiomatic spatial normalization.
* **$A_2 = 0.3268$**  
  → Topological Skyrme channel $(\omega^2)$. Derived from locked core invariants: $A_2 = I_2 / I_4$.
* **$A_3 \approx 10^{-6}$**  
  → UV biharmonic regulator $(\nabla^2 n)^2$. RG-irrelevant operator on the invariant manifold. No independent infrared flow generator.
* **$A_4 = 3.5553$**  
  → Vacuum mass-gap channel. $A_4 = \tfrac{1}{6} I_2 / I_{\rm pot}$.
* **$Z_t = 1.0$**  
  → Temporal kinetic normalization.

---
## Kinetic Dressing (Principal Symbol Consistent)
* **$\chi \approx 1.63 \times 10^{-6}$**  
  → Principal-symbol amplitude renormalisation:  
  $$P(x,k) = Z_t(1+\chi E_0(x))\omega^2 - T^{ij}(x)k_i k_j$$  
  Not a metric coupling; a dispersion dressing term.

---
## Soliton & Core Field Quantities
* **Soliton Mass $M_{\rm intrinsic} \approx 236.0726$**  
  → Derrick-stable hedgehog minimisation of full energy functional.
* **Coherence Scale**  
  $$R_0 \approx \sqrt{A_3/A_1} \approx 10^{-3}$$  
  UV cutoff of stable topological texture support.
* **Derived coupling**  
  $$\gamma_{\rm derived} = A_3 A_4 \approx 3.5 \times 10^{-6}$$

---
## Interaction Kernel 
The kernel is the inverse of the Hessian operator:  
$$K(k) = \mathcal{H}^{-1}(k)$$  
Dual-pole decomposition:  
$$K(k) = \frac{A}{k^2 + m^2} + \frac{B}{k^2 + \Lambda^2}$$  
with $\Delta = \sqrt{A_1^2 + 4A_3A_4} \approx 1.000007$, $m^2 \approx 10^6$, $\Lambda^2 \approx 3.5$, $A = 1/\Delta$, $B = -A$.

---
## Principal Symbol → Ray Structure (Corrected Form)
Ray propagation is governed by $P(x,k) = 0$ with transport tensor:  
$$T^{ij}[n] = \delta^{ij} + A_2(\partial^i n \cdot \partial^j n)$$  
For hedgehog:  
$$T^{ij}k_i k_j = \left(1 + \frac{A_2}{r^2}\right)k_\perp^2 + k_r^2$$  

**Interpretation correction:**
* Defines an anisotropic dispersion cone
* NOT an emergent Riemannian metric
* Light rays follow Hamiltonian flow, not geodesics

---
## Effective Propagation Structure (Revised)
Principal symbol form:  
$$P(x,k) = Z_t(1+\chi E_0)\omega^2 - k_r^2 - \left(1+\frac{A_2}{r^2}\right)k_\perp^2$$  
Defines:
* direction-dependent phase velocity
* anisotropic null surfaces in phase space
* Finsler-type ray geometry (not metric geometry)

---
## Gravitational Slip 
$$\eta(k) = \frac{K_{\rm long}}{K_{\rm trans}}$$  
Correct interpretation: mode-dependent response ratio of the Hessian operator.  
Infrared limit: $\eta(k \to 0) \to \infty$ → longitudinal modes dominate IR transport.

---
## Bath Sector 
* $M_{\rm bath} \approx \sqrt{A_1/A_3} \approx 10^3$
* $g_2 \approx 1/A_3 \approx 10^6$
* $g_1 \approx 10^6$

---
## RG Structure (UPDATED)
Flow lives on a 2D invariant manifold. Effective dynamics reduce to a **rank-1 dominant mode** driven by $\chi E_0$. The system flows toward a stable IR attractor manifold (phase-1 dominance).

---

## Emergent Time from Soliton Condensation
In the pre-condensation regime the continuum field $n(x,t) \in S^2$ exists in a near-homogeneous, high-symmetry state with vanishing topological charge density. Global time translations are a coordinate redundancy with no physically meaningful clock — the system is effectively timeless.

Time becomes physically relevant only when topological solitons ($Q=1$ hedgehogs) condense due to the vacuum mass-gap $A_4$ and Skyrme term $A_2$. These stable, localized structures:
* Break global symmetry and create permanent texture-exclusion boundaries.
* Possess internal dynamics (breathing zero-modes, surface oscillations with eigenvalues $\lambda_n$).
* Generate irreversible entropy production through mergers, surface-mode excitations, and stochastic bath interactions.

### Relational Emergent Time Definition
To avoid circularity with a background coordinate time, we define emergent time through the topological activity functional:
$$\mathcal{A}[n] = \int d^3x \left( |\rho_{\rm top}(x)| + \alpha \, \sigma_\alpha^2(x) \right)$$

where $\rho_{\rm top}$ is the topological charge density and $\sigma_\alpha^2$ is the stochastic variance from the bath. The emergent time differential is defined as:
$$\bar{d}\tau = \frac{d\mathcal{A}}{\langle \mathcal{A} \rangle}$$

This is an inexact differential (denoted $\bar{d}\tau$) because the stochastic bath term $\alpha \sigma_\alpha^2(x)$ undergoes persistent local fluctuations even in the homogeneous phase. These fluctuations ensure a non-zero, positive global differential $d\mathcal{A} > 0$, preventing a "frozen" timeless state and providing the primordial drive for soliton condensation.

### Avoidance of Time Pockets
Localized differences in activity are suppressed by:
* Long-range kernel coupling $K(r)$, which enforces global coherence.
* The universal stochastic bath, which provides a baseline fluctuation rate everywhere.
* Topological protection and gradient energy cost, which penalize large desynchronization.

As a result, a coherent global emergent time $\tau$ forms after sufficient soliton condensation.

### Post-Condensation Dispersion Relations
In the post-condensation regime, frequencies appearing in the principal symbol (e.g. $\omega^2$) are understood with respect to the emergent time $\tau$:
$$\omega_\tau = \frac{\partial}{\partial \tau}$$

The dispersion relation is therefore rewritten as:
$$P(x,k) = Z_t(1+\chi E_0)\omega_\tau^2 - k_r^2 - \left(1+\frac{A_2}{r^2}\right)k_\perp^2$$

### Cosmological Implication
The transition from the timeless symmetric phase to the soliton-condensed regime defines a physical epoch that can influence the sound horizon, early Integrated Sachs-Wolfe effect, and the overall acoustic structure observed in the CMB.


---
## Cosmology (Reinterpreted IR Consistently)
$$
H^2(z) = H_0^2 \left[ \Omega_b (1+z)^3 + \Omega_{\rm bath} (1+z)^{1.5} + \Omega_{\rm gap} \right]
$$

**Interpretation:**
* $\Omega_{\rm bath}$ = dissipative continuum sector
* $\Omega_{\rm gap}$ = vacuum rigidity gap of $n(x,t)$ field
* IR behaviour governed by RG attractor regime (phase-1)

---
## Global Scale Calibration
* $E_0 \approx 30.608444$
* $L_0 \approx 1.610680$
Only external inputs.

---
## Core Structural Statement (UPDATED)
Everything emerges from:
* constrained field $n(x,t) \in S^2$
* energy functional with $(A_1,A_2,A_3,A_4)$
* Hessian operator spectrum
* principal symbol dispersion relation
* RG flow toward a rank-1 attractor manifold
* emergent relational time from soliton condensation

NOT from:
* spacetime geometry
* metric tensors
* curvature reconstruction

---
## Final Status (UPDATED)
Spine v1.2.1 is:
* self-consistent Hamiltonian ray theory
* anisotropic principal-symbol geometry
* closed EFT with RG flow to IR attractor
* rank-1 universality class system
* UV phase complexity that renormalises away
* emergent relational time from soliton condensation

and explicitly:
* not metric GR
* not Riemannian emergent geometry
* a nonlinear EFT with single-mode RG dominance
