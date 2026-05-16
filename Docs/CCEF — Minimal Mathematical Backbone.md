# CCEF — Minimal Mathematical Backbone

## 1. Field & Constraint
- Field: $n(x,t) \in S^2,\ |n| = 1$  
- Variation constraint: $n\cdot\delta n = 0$  
- Topological density:  
  $\omega = \frac{1}{4\pi} \epsilon_{ijk} n\cdot(\partial_j n \times \partial_k n)$

## 2. Energy Functional

$$E[n] = \int d^3x \left[ \frac{A_1}{2}(\partial_i n)^2 + \frac{A_2}{2} \omega^2 + \frac{A_3}{2}(\nabla^2 n)^2 + \frac{A_4}{2}(1 - (n\cdot n_0)^2) \right]$$

## 2.1 Covariant Kinetic Term (Derived Minimal Form)
- 4D Action: $S[n] = \int d^4x\,\mathcal{L}$  

$$\mathcal{L} = \frac{Z_t}{2}(\partial_t n)^2 - E[n]$$

- Constraint: $n\cdot n = 1$  
- Euler–Lagrange:  

$$Z_t \partial_t^2 n - A_1 \nabla^2 n + A_3 \nabla^4 n - A_4(n\cdot n_0)n_0 + \lambda n = 0$$

*(Here $Z_t$ is fixed by matching to the long‑wavelength limit of the microscopic soliton dispersion).*

## 3. Euler–Lagrange

$$A_1 \nabla^2 n - A_3 \nabla^4 n + A_4(n\cdot n_0)n_0 + \lambda n = 0$$

## 3.1 Isolated Cross-Term Projection Dynamics
- Isolated Cross-Term Action: $S_{\text{cross}}[n] = \int d^4x \left[ -A_3 (\nabla^2 n) \cdot (\partial_t^2 n) \right]$

- Functional Variation:

$$\delta S_{\text{cross}} = -A_3 \int d^4x \left[ (\nabla^2 \delta n) \cdot (\partial_t^2 n) + (\nabla^2 n) \cdot (\partial_t^2 \delta n) \right]$$

- Integrating by parts twice spatially on the first term and twice temporally on the second term yields:

$$\frac{\delta S_{\text{cross}}}{\delta n} = -2A_3 \partial_t^2 \nabla^2 n$$

- Imposing the $S^2$ target-space spherical variation constraint ($n \cdot \delta n = 0$):

$$-2A_3 \partial_t^2 \nabla^2 n + \lambda_{\text{cross}} n = 0$$

- Taking the inner product with $n$ to eliminate the Lagrange multiplier via identity $n \cdot n = 1$:

$$\lambda_{\text{cross}} = 2A_3 n \cdot (\partial_t^2 \nabla^2 n)$$

- Fully Derived Non-Linear Equation of Motion:

$$\partial_t^2 \nabla^2 n - \left[ n \cdot (\partial_t^2 \nabla^2 n) \right] n = 0$$

- Linearized Perturbation Regime ($n = n_0 + \pi$ with $n_0 = (0,0,1)$):

$$\partial_t^2 \nabla^2 \pi = 0$$

- Plane-Wave Dispersion Relation Solution ($\pi \propto e^{i(k \cdot x - \omega t)}$):

$$\omega^2 k^2 \pi_0 = 0 \implies \omega = 0 \quad \text{(Static Screening Mode) or} \quad k = 0 \quad \text{(Uniform Drift Mode)}$$

## 3.2 Conserved SO(3) Noether Currents
- Infinitesimal global $SO(3)$ transformation: $\delta n = \boldsymbol{\epsilon} \times n$
- Total action divergence relation: $\delta \mathcal{L} = \partial_\mu \left( \mathbf{J}^\mu \right) \cdot \boldsymbol{\epsilon} = 0$

### Derived Current Formulation
Evaluating the first-order and higher-derivative functional variations term-by-term yields:

$$\mathbf{J}^\mu = \gamma_{\nu} g^{\mu\nu} (n \times \partial_\nu n) - A_3 \left[ (\Box n) \times \partial^\mu n - \partial^\mu (\Box n) \times n \right]$$

Breaking this tensor down into explicit comoving spacetime frames ($\Box = \partial_t^2 - \nabla^2$):

- **Time Component (Charge Density Vector $\mathbf{J}^0$):**

$$\mathbf{J}^0 = Z_t (n \times \partial_t n) - A_3 \left[ (\partial_t^2 n - \nabla^2 n) \times \partial_t n - \partial_t (\partial_t^2 n - \nabla^2 n) \times n \right]$$

- **Spatial Component (Flux Vector $\mathbf{J}^i$):**

$$\mathbf{J}^i = -A_1 (n \times \partial_i n) + A_3 \left[ (\partial_t^2 n - \nabla^2 n) \times \partial_i n - \partial_i (\partial_t^2 n - \nabla^2 n) \times n \right]$$

- **Conservation Law:**

$$\partial_t \mathbf{J}^0 + \nabla \cdot \mathbf{J}^i = 0$$

*(Note: The potential coefficient $A_4$ and topological boundary coefficient $A_2$ carry no derivative field components and contribute exactly zero to the active current matrix).*



## 4. Soliton Sector
- Perturbation: $n = n_* + \pi,\ n_*\cdot\pi = 0$  
- Hessian:  

$$\mathcal{H}\pi = \frac{\delta^2 E}{\delta n^2} \pi$$

## 4.1 Energy–Momentum and Interaction Structure of Radial Solitons

For the static hedgehog configuration

$$n(r) = (\sin f(r)\,\hat r,\; \cos f(r)),$$

the covariant energy–momentum tensor reduces to purely spatial components.

### Energy Density

$$\rho_{\mathrm{eff}}(r) = \frac{A_1}{2}\left[(f')^{2} + \frac{2\sin^{2}f}{r^{2}}\right] + \frac{A_3}{2}\left[f'' + \frac{2}{r}f' - \frac{\sin(2f)}{r^{2}}\right]^{2} + \frac{A_4}{2}\sin^{2}f$$

### Radial Pressure

$$P_r(r) = \frac{A_1}{2}\left[(f')^{2} - \frac{2\sin^{2}f}{r^{2}}\right] - \frac{A_3}{2}\left[f'' + \frac{2}{r}f' - \frac{\sin(2f)}{r^{2}}\right]^{2} - \frac{A_4}{2}\sin^{2}f$$

### Tangential Pressure

$$P_t(r) = -\frac{A_1}{2}(f')^{2} + \frac{A_3}{2}\left[f'' + \frac{2}{r}f' - \frac{\sin(2f)}{r^{2}}\right]^{2} - \frac{A_4}{2}\sin^{2}f$$

### Local Conservation

Static spherical symmetry requires

$$\frac{dP_r}{dr} + \frac{2}{r}(P_r - P_t) = 0$$

Substituting the explicit expressions yields

$$\frac{dP_r}{dr} + \frac{2}{r}(P_r - P_t) = -f'(r)\,\Big[ A_3\nabla^{4}f - A_1\left(f'' + \frac{2}{r}f' - \frac{\sin(2f)}{r^{2}}\right) + \frac{A_4}{2}\sin(2f) \Big]$$

The bracketed term is the radial Euler–Lagrange equation, so the conservation law holds identically.

### Total Soliton Mass

$$M_{\mathrm{soliton}} = 4\pi\!\int_{0}^{\infty} r^{2}\,\rho_{\mathrm{eff}}(r)\,dr$$

---

## Asymptotic Soliton–Soliton Interaction

For two well‑separated solitons with profile angles $f_A(\mathbf{r})$ and $f_B(\mathbf{r}-\mathbf{R})$, the combined configuration is approximated by

$$f_{\mathrm{tot}}(\mathbf{r}) = f_A(\mathbf{r}) \pm f_B(\mathbf{r}-\mathbf{R}),$$

with the sign determined by the relative topological charge.

Inserting into the static energy functional and subtracting self‑energies gives the interaction potential

$$V_{AB}(\mathbf{R}) =\!\int d^{3}x\Big[ A_1\,\partial_i f_A\,\partial_i f_B + A_4\,\cos f_A\,\sin f_B + A_3\,\nabla^{2}f_A\,\nabla^{2}f_B \Big]$$

For large separations, the profiles obey

$$f(r)\sim C\,\frac{e^{-m r}}{r}, \qquad m=\sqrt{\frac{A_4}{A_1}},$$

and the short‑range $A_3$ term is suppressed.  
The asymptotic interaction reduces to

$$V_{AB}(\mathbf{R}) =\pm 4\pi A_1\,C_A C_B\,\frac{e^{-|\mathbf{R}|\sqrt{A_4/A_1}}}{|\mathbf{R}|}$$

* The upper sign corresponds to soliton–soliton repulsion.
* The lower sign corresponds to soliton–antisoliton attraction.


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

## 7.1 Determination of $C_1$ and $C_2$
- Radial Quartic Equation:  

$$\big(A_4 - A_1\nabla^2 - A_3\nabla^4\big) K(r) = \delta^{(3)}(r)$$

- Ansatz:  

$$K(r) = \frac{1}{4\pi r}\big(C_1 e^{-m r} + C_2 e^{-\Lambda r}\big)$$

- Boundary Conditions:  
  1. Regularity at $r \to 0$  
  2. Decay at $r \to \infty$  
  3. Normalization: $\int d^3r\,L K(r) = 1$  
- Solution:  

$$C_1 + C_2 = 0$$  

$$C_1 = \frac{1}{A_3 (\Lambda^2 - m^2)}$$  

$$C_2 = -C_1$$

## 7.2 Numerical Continuum Evolution (1D Reduction)

To evolve the CCEF field directly in continuum form, we implement the 1D reduction of the full second–order evolution equation

$$Z_t\,\partial_t^2 n = A_1\nabla^2 n - A_3\nabla^4 n + A_4(n\cdot n_0)n_0 - (n\cdot V)n + Z_t|\partial_t n|^2 n,$$

where $V$ denotes the spatial drive vector inside the Euler–Lagrange operator and the projection term enforces the spherical constraint $n\cdot n=1$.

### Spatial Operators

Periodic finite–difference stencils give

$$\nabla^2 n = \frac{n_{i+1}-2n_i+n_{i-1}}{dx^2}, \qquad \nabla^4 n = \frac{n_{i+2}-4n_{i+1}+6n_i-4n_{i-1}+n_{i-2}}{dx^4}.$$

### Projected Evolution Equation

The raw drive vector is

$$V = A_1\nabla^2 n - A_3\nabla^4 n + A_4(n\cdot n_0)n_0.$$

Projection onto the tangent space of $S^2$ is performed via

$$P_\perp V = V - (n\cdot V)n.$$

The full acceleration becomes

$$\partial_t^2 n = \frac{P_\perp V}{Z_t} + |\partial_t n|^2 n.$$

### Time Integration

A leapfrog/Verlet scheme updates the field:

$$\partial_t n \rightarrow \partial_t n + (\partial_t^2 n)\,dt, \qquad n \rightarrow n + (\partial_t n)\,dt.$$

After each update, the target–space constraint is enforced algebraically:

$$n \rightarrow \frac{n}{|n|}.$$

This algorithm provides a direct numerical realization of the CCEF continuum dynamics, preserving the spherical constraint and the exact structure of the spatial operators without introducing any external assumptions.

## 7.3 Perturbative Expansion and Mode‑Coupling Structure (1D Reduction)

We expand the transverse components of the field as

$$n(x,t) = (\pi_1,\;\pi_2,\;\sqrt{1-\pi^2}), \qquad \pi^2=\pi_1^2+\pi_2^2,$$

and retain terms up to cubic order. Substituting into the 1D evolution equation yields the transverse perturbation equation

$$Z_t\,\partial_t^2\pi_a - A_1\,\partial_x^2\pi_a + A_3\,\partial_x^4\pi_a + A_4\,\pi_a = \mathcal{F}^{(3)}_a[\pi].$$

### Cubic Non‑Linear Driving Term

$$\mathcal{F}^{(3)}_a[\pi] = \pi_a\!\left[ A_1\sum_b(\partial_x\pi_b)^2 + A_3\sum_b(\partial_x^2\pi_b)^2 - A_4\sum_b\pi_b^2 + Z_t\sum_b(\partial_t\pi_b)^2 \right] - \pi_a\,\partial_x\!\left[ A_1\sum_b\pi_b\partial_x\pi_b \right] + A_3\pi_a\,\partial_x^2\!\left[ \sum_b\big((\partial_x\pi_b)^2+\pi_b\partial_x^2\pi_b\big) \right].$$

### Fourier Representation

$$\pi_a(x,t) = \int\frac{dk}{2\pi}\,\tilde\pi_a(k,t)e^{ikx}.$$

The linear operator becomes

$$\tilde D(k) = -Z_t\omega^2 + A_1 k^2 + A_3 k^4 + A_4.$$

The cubic term transforms into a momentum‑conserving convolution:

$$\tilde{\mathcal{F}}^{(3)}_a(k) = \sum_b\!\int\!\frac{dk_1}{2\pi}\frac{dk_2}{2\pi}\frac{dk_3}{2\pi} (2\pi)\delta(k-k_1-k_2-k_3)\, \Gamma_{ab}(k_1,k_2,k_3)\, \tilde\pi_a(k_1)\tilde\pi_b(k_2)\tilde\pi_b(k_3).$$

### Mode‑Coupling Coefficients

#### Cross‑Mode Coupling $(b\neq a)$

$$\Gamma_{a,b\neq a}(k_1,k_2,k_3) = -A_1(k_2 k_3) + A_3\!\left(k_2^2 k_3^2 - k_2^4 - k_3^4\right) - A_4 - Z_t\,\omega_2\omega_3.$$

#### Self‑Mode Coupling $(b=a)$

$$\Gamma_{aa}(k_1,k_2,k_3) = -A_1\!\left[ \frac{1}{3}(k_1k_2+k_2k_3+k_3k_1) + \frac{1}{3}(k_2+k_3)^2 \right] + A_3\!\left[ k_2^2 k_3^2 - \frac{1}{3}(k_2^4+k_3^4) - \frac{1}{3}(k_2+k_3)^4 \right] - A_4 - Z_t\,\omega_2\omega_3.$$

### Vertex Scaling

In the infrared limit,

$$\lim_{k\to 0}\Gamma_{ab} = -A_4.$$

In the ultraviolet limit,

$$\Gamma_{ab}(k)\sim A_3 k^4.$$

Thus the mass‑gap parameter $A_4$ sets the IR interaction plateau, while the higher‑derivative coefficient $A_3$ governs UV mode‑coupling growth and stabilizes high‑frequency continuum dynamics.

## 7.4 Pseudo‑Spectral Continuum Evolution (1D Reduction)

The 1D CCEF evolution equation

$$Z_t\,\partial_t^2 n = A_1\nabla^2 n - A_3\nabla^4 n + A_4(n\cdot n_0)n_0 - (n\cdot V)n + Z_t|\partial_t n|^2 n$$

can be implemented exactly using a pseudo‑spectral method, where all spatial derivatives are evaluated in Fourier space.

### Fourier Operators

For a periodic domain of length $L$ with $N$ modes,

$$k = \frac{2\pi m}{L},\qquad m\in\{-N/2,\dots,N/2-1\}.$$

The Laplacian and bi‑Laplacian act as

$$\nabla^2 n \;\longleftrightarrow\; -k^2 \tilde n, \qquad \nabla^4 n \;\longleftrightarrow\; k^4 \tilde n.$$

### Linear Drive Vector

Transforming $n$ to Fourier space and applying the operators gives

$$V_{\text{lin}} = A_1\nabla^2 n - A_3\nabla^4 n + A_4(n\cdot n_0)n_0.$$

### Target‑Space Projection

The spherical constraint is enforced by projecting the drive vector onto the tangent space of $S^2$:

$$P_\perp V = V - (n\cdot V)n.$$

### Non‑Linear Kinetic Term

The kinetic reinforcement term is

$$|\partial_t n|^2 n.$$

### Final Acceleration

$$\partial_t^2 n = \frac{P_\perp V}{Z_t} + |\partial_t n|^2 n.$$

### Time Integration

A leapfrog/Verlet update advances the field:

$$\partial_t n \rightarrow \partial_t n + (\partial_t^2 n)\,dt, \qquad n \rightarrow n + (\partial_t n)\,dt.$$

After each update, the algebraic constraint is restored:

$$n \rightarrow \frac{n}{|n|}.$$

This pseudo‑spectral scheme provides an exact representation of the spatial operators and preserves the target‑space constraint throughout the evolution.




## 8. RG Flow

$$\frac{dA_1}{d\ln a} = c_1 \rho_0 \xi_R^2 - d_1 \Sigma$$  

$$\frac{dA_3}{d\ln a} = c_3 \rho_0 \xi_R^4 - d_3 \Sigma \xi_R^2$$  

$$\frac{dA_4}{d\ln a} = c_4 \rho_0 - d_4 \Sigma$$

### 8.1 Stability Control (Derived Minimal Form)

Define the quartic kernel denominator:

$$D(k,a)=A_4(a)-A_1(a)k^2-A_3(a)k^4$$

Poles occur when:

$$A_3(a)k^4 + A_1(a)k^2 - A_4(a)=0$$

Solve for the pole locations by setting $s=k^2$:

$$A_3(a)s^2 + A_1(a)s - A_4(a)=0$$

$$s_\pm(a)=\frac{-A_1(a)\pm\sqrt{A_1(a)^2+4A_3(a)A_4(a)}}{2A_3(a)}$$

Define the associated inverse-length scales:

$$m(a)=\sqrt{-s_-(a)},\qquad \Lambda(a)=\sqrt{s_+(a)}$$

#### 8.1.1 RG-Admissible Domain (No Accidental Poles)

Let the operational comoving momentum band be:

$$k\in[k_{\mathrm{IR}},k_{\mathrm{UV}}]$$

and the cosmological interval:

$$a\in[a_{\min},a_{\max}]$$

The RG trajectory $(A_1(a),A_3(a),A_4(a))$ is admissible only if:

$$D(k,a)\neq 0 \quad \forall\,k\in[k_{\mathrm{IR}},k_{\mathrm{UV}}],\; \forall\,a\in[a_{\min},a_{\max}]$$

Stronger stability condition:

$$\min_{a\in[a_{\min},a_{\max}]}\; \min_{k\in[k_{\mathrm{IR}},k_{\mathrm{UV}}]} |D(k,a)|>0$$

This prevents RG drift from moving a pole into the physical band.

#### 8.1.2 Intentional Pole Interpretation (Emergent Coherent Modes)

If a pole at $k^2=k_\star^2(a)$ is intentionally promoted to a physical coherent mode, then near the pole:

$$K(k,a)\sim \frac{1}{Z_\star(a)}\frac{1}{k^2-k_\star^2(a)}$$

Residue definition:

$$Z_\star(a)=\left[\frac{\partial(k^2)}{\partial D}\right]^{-1}_{k^2=k_\star^2(a)}$$

Since:

$$D(k,a)=A_4(a)-A_1(a)k^2-A_3(a)k^4$$

we obtain:

$$\frac{\partial D}{\partial(k^2)}=-A_1(a)-2A_3(a)k^2$$

Thus:

$$Z_\star(a)=\big[-A_1(a)-2A_3(a)k_\star^2(a)\big]^{-1}$$

Positivity requirement (no ghost excitation):

$$-A_1(a)-2A_3(a)k_\star^2(a)>0$$

Band-separation requirement:

$$k_\star(a)\notin[k_{\mathrm{IR}},k_{\mathrm{UV}}]$$

unless the pole is explicitly designated as a coherent mode with positive residue.

This completes the minimal stability closure of the quartic kernel under RG flow.

### 8.2 Structural Closure (Minimal Form)

#### 8.2.1 Dynamical Stability
Let $\Psi_A$ be all coupled perturbations.  
The bilinear operator defines

$$\mathbf{M}(k^2,a).$$

Stability requires

$$\det \mathbf{M}(k^2,a)\neq 0 \quad \forall k\in[k_{\mathrm{IR}},k_{\mathrm{UV}}],\; \forall a\in[a_{\min},a_{\max}].$$

#### 8.2.2 Causal Structure
Dispersion:

$$\omega=\omega(k,a),\qquad v_g=\partial_k\omega.$$

Causality requires

$$v_g(k,a)<\infty \quad \forall k\in[k_{\mathrm{IR}},k_{\mathrm{UV}}].$$

#### 8.2.3 Soliton / Coherent‑Mode Spectrum
Static localized states satisfy

$$A_4 n + A_1\nabla^2 n - A_3\nabla^4 n + \mathcal{N}[n]=0, \qquad n\cdot n=1.$$

Solutions $n_\star(x)$ define the coherent‑mode spectrum.

#### 8.2.4 Structural Power Spectrum
The kernel

$$K(k,a)=\frac{1}{A_4-A_1 k^2-A_3 k^4}$$

gives

$$P(k,a)\propto |K(k,a)|^2.$$

#### 8.2.5 Internal Scaling
Coefficient evolution obeys

$$\frac{dA_n}{d\ln a} = \mathcal{F}_n(A_1,A_3,A_4),$$

derived from internal mode interactions.

#### 8.2.6 Sector Decomposition
Independent subsectors arise only if

$$\mathbf{M}(k^2,a) = \mathbf{M}_1(k^2,a)\oplus\mathbf{M}_2(k^2,a).$$

#### 8.2.7 Runaway Elimination
Time evolution remains second‑order:

$$\partial_t^2 n = \mathcal{G}(n,\partial_t n,\nabla^2 n,\nabla^4 n,a).$$

Higher derivatives act only spatially.

#### 8.2.8 Coherent‑Mode Bounds
Each mode satisfies

$$\int E_\star(n_\star(x),a)\,d^3x < \mathcal{E}_{\mathrm{bound}}(a).$$

### 8.3 Emergent Hyperbolic Operator and Causal Structure

The effective perturbation dynamics reduce to the single evolution equation

$$\ddot{\delta} +2H_{\mathrm{eff}}(a)\,\dot{\delta} - c_{\mathrm{eff}}^2(a)\,\nabla^2\delta + \ell^2(a)\,\nabla^4\delta - m_{\mathrm{eff}}^2(a)\,\delta =0,$$

with coefficients inherited directly from the RG–evolved kernel parameters:

$$c_{\mathrm{eff}}^2(a)=\frac{A_1(a)}{Z_t(a)},\qquad \ell^2(a)=\frac{A_3(a)}{Z_t(a)},\qquad m_{\mathrm{eff}}^2(a)=\frac{A_4(a)}{Z_t(a)}.$$

In the infrared limit $k\to 0$, the principal part becomes

$$\ddot{\delta}-c_{\mathrm{eff}}^2(a)\,\nabla^2\delta=0,$$

which is strictly hyperbolic whenever $c_{\mathrm{eff}}^2(a)>0$.  
Time derivatives remain second order, the spatial operator reduces to a positive‑definite Laplacian, and a well‑defined causal cone emerges without assuming any background metric.

Hyperbolicity is selected dynamically by the RG flow:

$$A_1(a)>0,\qquad Z_t(a)>0$$

ensuring a positive propagation speed $c_{\mathrm{eff}}^2(a)$.  
The coefficient $A_4(a)$ contributes only a mass gap through $m_{\mathrm{eff}}^2(a)$ and does not affect the existence of the causal cone.

## 8.4 Emergent Eikonal Metric (Derived Minimal Form)

Starting from the infrared limit of the CCEF perturbation operator,

$$\ddot{\delta} - c_{\mathrm{eff}}^{2}(a)\,\nabla^{2}\delta = 0, \qquad c_{\mathrm{eff}}^{2}(a)=\frac{A_{1}(a)}{Z_{t}(a)},$$

we apply the standard eikonal substitution

$$\delta(x,t)=e^{iS(x,t)}, \qquad k_{\mu}=\partial_{\mu}S,$$

which isolates the characteristic surfaces of the PDE.  
Substituting into the IR operator yields the dispersion relation

$$-\omega^{2} + c_{\mathrm{eff}}^{2}(a)\,k^{2} = 0.$$

Identifying this with the null condition of an emergent characteristic geometry,

$$g^{\mu\nu}(a)\,k_{\mu}k_{\nu}=0,$$

forces the contravariant metric components

$$g^{00}(a)=-1, \qquad g^{11}(a)=g^{22}(a)=g^{33}(a)=c_{\mathrm{eff}}^{2}(a).$$

The covariant metric follows uniquely by inversion:

$$
g_{\mu\nu}(a)=
\begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & c_{\mathrm{eff}}^{-2}(a) & 0 & 0 \\
0 & 0 & c_{\mathrm{eff}}^{-2}(a) & 0 \\
0 & 0 & 0 & c_{\mathrm{eff}}^{-2}(a)
\end{pmatrix}.
$$

No ansatz is introduced:  
The metric is the **unique characteristic tensor** implied by the CCEF wave operator.  
It depends only on the RG‑evolved internal coefficients $A_{1}(a)$ and $Z_{t}(a)$, requires no external geometric structure.



## 9. Background

$$\dot{\rho}_0 + 3H\rho_0 = 0$$  

$$H^2 = F(\rho_0, \alpha_0, P_R, \Sigma)$$

## 9.1 Covariant Energy–Momentum Tensor

$$T_{\mu\nu} = 2\frac{\partial\mathcal{L}}{\partial g^{\mu\nu}} - g_{\mu\nu}\mathcal{L}$$

$$\mathcal{L} = \frac{Z_t}{2} g^{00}(\partial_0 n)^2 + \frac{A_1}{2} g^{ij}(\partial_i n\cdot\partial_j n) - \frac{A_2}{2}\omega^2 - \frac{A_3}{2}(g^{\alpha\beta}\nabla_\alpha\partial_\beta n)^2 - \frac{A_4}{2}(1-(n\cdot n_0)^2)$$

$$\frac{\partial\mathcal{L}}{\partial g^{\mu\nu}} = \frac{1}{2}\mathcal{M}_{\mu\nu} - A_3(\Box n)\nabla_\mu\partial_\nu n$$

$$\mathcal{M}_{00} = Z_t(\partial_t n)^2 \qquad \mathcal{M}_{ij} = -A_1(\partial_i n\cdot\partial_j n)$$

$$T^0{}_0 = \rho_{\text{eff}} \qquad T^i{}_i = 3P_{\text{eff}}$$

$$\rho_{\text{eff}} = \frac{Z_t}{2}(\partial_t n)^2 + \frac{A_1}{2}(\partial_i n)^2 + \frac{A_2}{2}\omega^2 + \frac{A_3}{2}(\nabla^2 n)^2 - A_3(\nabla^2 n)\partial_t^2 n + \frac{A_4}{2}(1-(n\cdot n_0)^2)$$

$$\P_{\text{eff}} = \frac{Z_t}{2}(\partial_t n)^2 - \frac{A_1}{6}(\partial_i n)^2 - \frac{A_2}{2}\omega^2 - \frac{A_3}{6}(\nabla^2 n)^2 - \frac{A_4}{2}(1-(n\cdot n_0)^2)$$

$$T = T^\mu{}_\mu = \rho_{\text{eff}} - 3P_{\text{eff}} = - Z_t(\partial_t n)^2 + A_1(\partial_i n)^2 + 2A_2\omega^2 + A_3(\nabla^2 n)^2 - A_3(\nabla^2 n)\partial_t^2 n + 2A_4(1-(n\cdot n_0)^2)$$

## 9.2 Canonical Noether Energy-Momentum Tensor
- Infinitesimal spacetime translation variation: $\delta n = \epsilon^\nu \partial_\nu n$
- Conservation equation under translation invariance: $\partial_\mu T^\mu{}_\nu = 0$

### Exact Current Derivation
Varying the first-order, topological, and higher-derivative terms under the translation shift yields:

$$T^\mu{}_\nu = \gamma_{\alpha} g^{\mu\alpha} (\partial_\alpha n \cdot \partial_\nu n) - A_3 \left[ (\Box n) \cdot \partial^\mu \partial_\nu n - \partial^\mu (\Box n) \cdot \partial_\nu n \right] - \delta^\mu{}_\nu \mathcal{L}$$

Splitting the tensor components explicitly into comoving frame densities ($\Box = \partial_t^2 - \nabla^2$):

- **Energy Density Flux ($T^0{}_0 = \rho_{\text{canonical}}$):**

$$T^0{}_0 = Z_t (\partial_t n)^2 - A_3 \left[ (\partial_t^2 n - \nabla^2 n) \cdot \partial_t^2 n - \partial_t (\partial_t^2 n - \nabla^2 n) \cdot \partial_t n \right] - \mathcal{L}$$

- **Spatial Stress Tensor Components ($T^i{}_j$):**

$$T^i{}_j = -A_1 (\partial_i n \cdot \partial_j n) + A_3 \left[ (\partial_t^2 n - \nabla^2 n) \cdot \partial_i \partial_j n - \partial_i (\partial_t^2 n - \nabla^2 n) \cdot \partial_j n \right] - \delta^i{}_j \mathcal{L}$$

*(Note: On the shell of the non-linear spherical constraint $n \cdot \partial_\nu n = 0$, this canonical current matches the metric derivation in Section 9.1, confirming complete mathematical consistency).*


## 10. Perturbations

$$\ddot{\delta} + 2H \dot{\delta} = 4\pi G_{\text{eff}}(k,a) \rho_0 (\delta + \chi\beta) - c_s^2 k^2 \delta$$  

$$G_{\text{eff}} \propto K(k)$$  

$$\eta = \frac{K_{\text{long}}}{K_{\text{trans}}}$$

## 10.1 Tensor Kernel Decomposition

$$\mathcal{H}_{ij}(k) = \mathcal{H}_{\text{long}}(k) \hat k_i \hat k_j + \mathcal{H}_{\text{trans}}(k)(\delta_{ij} - \hat k_i \hat k_j)$$

$$\mathcal{H}_{\text{long}}(k) = A_1 k^2 + A_3 k^4$$  

$$\mathcal{H}_{\text{trans}}(k) = A_4 - A_1 k^2 - A_3 k^4$$

$$K_{ij}(k) = K_{\text{long}}(k) \hat k_i \hat k_j + K_{\text{trans}}(k)(\delta_{ij} - \hat k_i \hat k_j)$$

$$K_{\text{long}}(k) = \frac{1}{A_1 k^2 + A_3 k^4}$$  

$$K_{\text{trans}}(k) = \frac{1}{A_4 - A_1 k^2 - A_3 k^4}$$

- Gravitational Slip Parameter:  

$$\eta(k,a) = \frac{K_{\text{long}}(k,a)}{K_{\text{trans}}(k,a)}$$

## 11. Hydrogen Sector
Radial operator:  

$$A_1 L_\ell R - A_3 L_\ell^2 R + A_4 R = \lambda R$$

Low-energy reduction:  

$$L_\ell R + \kappa^2 R = 0$$  

$$\kappa^2 = \frac{A_4 - \lambda}{A_1}$$

Boundary quantization (correct form):  

$$\kappa_{\ell n} = \frac{\alpha_{\ell n}}{R_{\text{eff}}}$$  

$$\lambda_{\ell n} = A_4 - A_1 \left(\frac{\alpha_{\ell n}}{R_{\text{eff}}}\right)^2$$

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
