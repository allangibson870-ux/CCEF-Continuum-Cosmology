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
## Principal Symbol → Ray Structure 
Ray propagation is governed by $P(x,k) = 0$ with transport tensor:  
$$T^{ij}[n] = \delta^{ij} + A_2(\partial^i n \cdot \partial^j n)$$  
For hedgehog:  
$$T^{ij}k_i k_j = \left(1 + \frac{A_2}{r^2}\right)k_\perp^2 + k_r^2$$  

**Interpretation correction:**
* Defines an anisotropic dispersion cone
* NOT an emergent Riemannian metric
* Light rays follow Hamiltonian flow, not geodesics

---
## Effective Propagation Structure 
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
## RG Structure 
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
## Cosmology 
$$
H^2(z) = H_0^2 \left[ \Omega_b (1+z)^3 + \Omega_{\rm bath} (1+z)^{1.5} + \Omega_{\rm gap} \right]
$$

### Acoustic Damping and the Bath Sector
The damping tail of the acoustic spectrum is governed by the interaction between the primary field and the dissipative continuum sector ($\Omega_{\rm bath}$). The spatial damping cutoff scale $k_D$ scales relationally with the topological activity $\mathcal{A}$:

$$k_D^2(\mathcal{A}) = \frac{\mathcal{A}^{1.5}}{g_2 \sqrt{1 + \chi E_0(\mathcal{A})}}$$

As the universe transitions through the condensation epoch, the rapid drop in phase velocity $v_p$ combined with the dilution of bath dominance freezes out the damping scale. This mechanism generates the high-frequency exponential suppression (damping tail) observed in the CMB spectrum through the UV regulator pole ($m^2 \approx 10^6$) of the Hessian kernel, completely independent of space expansion metric adjustments.

---

### Late-Stage Stability and the Vacuum Mass-Gap ($\Omega_{\rm gap}$)
In the late-stage post-condensation universe, as the topological activity stabilizes ($\mathcal{A} \to \infty$) and the bath sector dilutes ($\Omega_{\rm bath} \to 0$), the cosmological evolution is dominated by the vacuum mass-gap channel:

$$A_4 = 3.5553$$

Within the non-metric cosmological framework:

$$H^2(z) = H_0^2 \left[ \Omega_b (1+z)^3 + \Omega_{\rm bath} (1+z)^{1.5} + \Omega_{\rm gap} \right]$$

the parameter $\Omega_{\rm gap}$ functions as the dark energy surrogate. Rather than driving a metric expansion of space, $\Omega_{\rm gap}$ represents the irreducible vacuum rigidity floor of the constrained $n(x,t) \in S^2$ field. This vacuum mass gap penalizes further global transformations, stabilizing the rank-1 attractor manifold against late-stage fluctuations and locking the infrared structure into its final, frozen phase-1 dominance.

### Acoustic Damping and the Bath Sector
The damping tail of the acoustic spectrum is governed by the interaction between the primary field and the dissipative continuum sector ($\Omega_{\rm bath}$). The energy density scaling of this sector is derived from the infrared limit ($k \to 0$) of the dual-pole Hessian kernel $K(k) = \mathcal{H}^{-1}(k)$. 

In this infrared regime, transport is dominated by the mass-gap pole $\Lambda^2 \approx 3.5$. Integrating these continuum modes over the 3D active phase-space volume yields a spectral density scaling of $\xi_R^{-1.5}(\mathcal{A})$. This provides the rigorous derivation for the bath energy density scaling:
$$\Omega_{\rm bath}(z) \propto (1+z)^{1.5}$$

The characteristic spatial damping scale $k_D^2$ is derived by matching the transport dissipation rate to the phase velocity $v_p$ under the out-of-equilibrium Langevin field equation. Computing the effective friction coefficient $\Gamma_{\rm bath}$ from the available bath states yields the exact operator identity:
$$k_D^2(\mathcal{A}) = \frac{\mathcal{A}^{2.5}}{g_2 \sqrt{1 + \chi E_0(\mathcal{A})}}$$

During the condensation epoch, the rapid drop in phase velocity $v_p$ combined with the dilution of bath dominance freezes out the damping scale. This mechanism generates the high-frequency exponential suppression (damping tail) observed in the CMB spectrum. This suppression occurs through the UV regulator pole ($m^2 \approx 10^6$) of the Hessian kernel, completely independent of space expansion metric adjustments.

---

### The Baryonic Sector ($\Omega_{\rm b}$) as Soliton Density Packing
The baryonic matter sector ($\Omega_{\rm b}$) does not consist of particles embedded in expanding space. Instead, it represents the spatial packing density of the conserved, localized $Q=1$ topological solitons (hedgehogs) fixed by the intrinsic soliton mass:
$$M_{\rm intrinsic} \approx 236.0726$$

The standard cosmological scaling of matter density is recovered relationally. Let $(1+z) \equiv \xi_R^{-1}(\mathcal{A})$ be defined by the inverse growth of the RG correlation length. Because the total number of topological cores $N_Q$ is conserved post-condensation, and texture-exclusion boundaries prevent core collapse, the active spatial volume scales explicitly as:
$$V_{\rm active}(z) \propto \xi_R^3(\mathcal{A})$$

Thus, the effective baryon density scales strictly with the invariant manifold's active volume:
$$\Omega_{\rm b}(z) \propto \frac{N_Q \cdot M_{\rm intrinsic}}{V_{\rm active}(z)} \propto (1+z)^3$$

This derivation provides a strict topological origin for baryonic matter scaling within a completely static spatial network geometry.

---

### Late-Stage Stability and the Vacuum Mass-Gap ($\Omega_{\rm gap}$)
In the late-stage post-condensation universe, the topological activity stabilizes ($\mathcal{A} \to \infty$) and the bath sector dilutes ($\Omega_{\rm bath} \to 0$). The cosmological evolution is then dominated by the vacuum mass-gap channel:
$$A_4 = 3.5553$$

Within the non-metric cosmological framework:
$$H^2(z) = H_0^2 \left[ \Omega_{\rm b} (1+z)^3 + \Omega_{\rm bath} (1+z)^{1.5} + \Omega_{\rm gap} \right]$$

The parameter $\Omega_{\rm gap}$ functions as the dark energy surrogate, derived from the second variation of the energy functional. The vacuum mass-gap channel contributes a derivative-independent scalar floor to the Hessian operator:
$$\frac{\delta^2 E_{\rm pot}}{\delta n^2} \propto A_4$$

This term acts as a global restoring force. Any late-stage field perturbation $\delta n$ away from the stable IR attractor manifold incurs an energy cost proportional to $A_4 (\delta n)^2$. Rather than driving a metric expansion of space, $\Omega_{\rm gap}$ represents the irreducible vacuum rigidity floor of the constrained $n(x,t) \in S^2$ field. This mathematically penalizes further global transformations and locks the system into its final, frozen phase-1 dominance.



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
## Core Structural Statement 
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
## Final Status
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
