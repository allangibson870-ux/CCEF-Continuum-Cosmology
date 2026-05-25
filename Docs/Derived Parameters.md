# CCEF / Spine v1.2.1 — Derived Parameters Summary (Principal-Symbol Consistent Physical Branch)

---

## Core Structural Parameters (Energy Functional) — Physical Branch

* **$A_1 = 1.0$**  
  → Quadratic gradient tension $|\nabla n|^2$  
  Axiomatic spatial normalization.

* **$A_2 = 0.3268$**  
  → Topological Skyrme channel $(\omega^2)$  
  Derived from locked core invariants:  
  $A_2 = I_2 / I_4$

* **$A_3 \approx 10^{-6}$**  
  → UV biharmonic regulator $(\nabla^2 n)^2$  
  RG-irrelevant operator on the invariant manifold  
  No independent infrared flow generator.

* **$A_4 = 3.5553$**  
  → Vacuum mass-gap channel  
  $A_4 = \tfrac{1}{6} I_2 / I_{\text{pot}}$

* **$Z_t = 1.0$**  
  → Temporal kinetic normalization.

---

## Kinetic Dressing (Principal Symbol Consistent)

* **$\chi \approx 1.63 \times 10^{-6}$**  
  → Appears only as a principal-symbol amplitude renormalisation:

$$
P(x,k) = Z_t(1+\chi E_0(x))\omega^2 - T^{ij}(x)k_i k_j
$$

Not a metric coupling; a dispersion dressing term.

---

## Soliton & Core Field Quantities

* **Soliton Mass $M_{\text{intrinsic}} \approx 236.0726$**  
  → Derrick-stable hedgehog minimisation of full energy functional.

* **Coherence Scale**

$$
R_0 \approx \sqrt{A_3/A_1} \approx 10^{-3}
$$

UV cutoff of stable topological texture support.

* **Derived coupling**

$$
\gamma_{\text{derived}} = A_3 A_4 \approx 3.5 \times 10^{-6}
$$

---

## Interaction Kernel (Corrected Interpretation)

The kernel is NOT a metric Green function; it is the inverse of the Hessian operator in momentum space:

$$
K(k) = \mathcal{H}^{-1}(k)
$$

Dual-pole decomposition:

$$
K(k) = \frac{A}{k^2 + m^2} + \frac{B}{k^2 + \Lambda^2}
$$

with:

* $\Delta = \sqrt{A_1^2 + 4A_3A_4} \approx 1.000007$
* $m^2 = \frac{A_1 + \Delta}{2A_3} \approx 10^6$
* $\Lambda^2 = \frac{-A_1 + \Delta}{2A_3} \approx 3.5$
* $A = 1/\Delta$, $B = -A$

---

## Principal Symbol → Ray Structure (Corrected Form)

Ray propagation is governed by:

$$
P(x,k) = 0
$$

with transport tensor:

$$
T^{ij}[n] = \delta^{ij} + A_2(\partial^i n \cdot \partial^j n)
$$

For hedgehog:

$$
T^{ij}k_i k_j =
\left(1+\frac{A_2}{r^2}\right)k_\perp^2 + k_r^2
$$

➡ Interpretation correction:

- Defines an anisotropic dispersion cone
- NOT an emergent Riemannian metric
- Light rays follow Hamiltonian flow, not geodesics

---

## Effective Propagation Structure (Revised)

Principal symbol form:

$$
P(x,k) =
Z_t(1+\chi E_0)\omega^2 - k_r^2 - \left(1+\frac{A_2}{r^2}\right)k_\perp^2
$$

Defines:

* direction-dependent phase velocity
* anisotropic null surfaces in phase space
* Finsler-type ray geometry (not metric geometry)

---

## Gravitational Slip (Reinterpreted Correctly)

$$
\eta(k) = \frac{K_{\text{long}}}{K_{\text{trans}}}
$$

Correct interpretation:

- NOT spacetime anisotropy  
- It is a mode-dependent response ratio of the Hessian operator

Infrared limit:

$$
\eta(k \to 0) \to \infty
$$

➡ physically:
- longitudinal modes dominate IR transport
- generates effective lensing enhancement
- without invoking geometric curvature

---

## Bath Sector (Unchanged)

* $M_{\text{bath}} \approx \sqrt{A_1/A_3} \approx 10^3$
* $g_2 \approx 1/A_3 \approx 10^6$
* $g_1 \approx 10^6$

---

## RG Structure (UPDATED — CRITICAL REVISION)

Flow lives on an invariant manifold:

$$
\frac{d}{d\ln a}(A_1,A_2,A_3,A_4) \in \mathcal{M}_{2D}
$$

However, RG eigenmode analysis shows:

- **one relevant RG direction**
- **one marginal/irrelevant direction**
- effective flow is rank-1 dominated

So the RG structure reduces to:

> a single effective deformation mode driven by $\chi E_0$

No exact fixed points exist; instead:

> the system flows toward a stable IR attractor manifold (phase-1 dominance)

---

## Cosmology (Reinterpreted IR Consistently)

$$
H^2(z) = H_0^2[\Omega_b(1+z)^3 + \Omega_{\text{bath}}(1+z)^{1.5} + \Omega_{\text{gap}}]
$$

➡ interpretation:

- $\Omega_{\text{bath}}$ = dissipative continuum sector  
- $\Omega_{\text{gap}}$ = vacuum rigidity gap of $n(x,t)$ field  
- IR behaviour governed by RG attractor regime (phase-1)

---

## Global Scale Calibration

* $E_0 \approx 30.608444$
* $L_0 \approx 1.610680$

Only external inputs.

---

## Core Structural Statement (UPDATED)

Everything emerges from:

- constrained field $n(x,t) \in S^2$
- energy functional with $(A_1,A_2,A_3,A_4)$
- Hessian operator spectrum
- principal symbol dispersion relation
- RG flow toward a rank-1 attractor manifold

NOT from:
- spacetime geometry
- metric tensors
- curvature reconstruction

---

## Final Status (UPDATED)

Spine v1.2.1 is:

✔ self-consistent Hamiltonian ray theory  
✔ anisotropic principal-symbol geometry  
✔ closed EFT with RG flow to IR attractor  
✔ rank-1 universality class system  
✔ UV phase complexity that renormalises away  

and explicitly:

❌ not metric GR  
❌ not Riemannian emergent geometry  
✔ a nonlinear EFT with single-mode RG dominance
