# 06. Cosmological Perturbation Closure

## 1. Statement of the Problem

The cosmological perturbation sector introduces two dynamical fields:
- the density contrast $\delta(k,a)$,
- the velocity‑like field $\beta(k,a)$.

Their evolution is governed by the LITE system:
$$\beta' + \Gamma_\beta \beta = S_\delta \delta + \Xi_\beta,$$
$$\delta'' + A\delta' + B\delta = C\beta.$$

The noise term $\Xi_\beta$ depends on the effective noise scale  
$$\hbar_{\text{eff}}(a) = \sigma_\alpha^2(a)\rho_0(a).$$

The goal is to eliminate the remaining functional freedom in the perturbation sector by showing that all coefficients $(A,B,C,\Gamma_\beta,S_\delta)$ and the noise statistics are fully determined by the continuum RG flows and the previously closed sectors.

---

## 2. Starting Definitions

LITE system:
$$\beta' + \Gamma_\beta \beta = S_\delta \delta + \Xi_\beta,$$
$$\delta'' + A\delta' + B\delta = C\beta.$$

Noise statistics:
$$\langle \Xi_\beta \rangle = 0,$$
$$\langle \Xi_\beta \Xi_\beta' \rangle = C_\beta\,\hbar_{\text{eff}}\,f_\beta(k)\,\delta_D(\ln a - \ln a')\delta_D(k-k').$$

Effective noise scale:
$$\hbar_{\text{eff}} = \sigma_\alpha^2 \rho_0.$$

Kernel response:
$$\Phi = K\rho, \qquad \Psi = K_2\rho.$$

Slip parameter:
$$\eta = \Phi/\Psi.$$

---

## 3. Derivation

### 3.1 Closure of the noise sector

From the variance‑flow elimination:
$$\sigma_\alpha^2 \to \sigma_{\alpha,\ast}^2 = \gamma_K/\gamma_\sigma.$$

Thus
$$\hbar_{\text{eff}}(a) = \frac{\gamma_K}{\gamma_\sigma}\rho_0(a).$$

Since $\rho_0(a)$ is fixed by the background cosmology, the noise amplitude is no longer a free function.

Therefore:
- the amplitude of $\Xi_\beta$ is fixed,
- the noise floor in $P_\delta$ is fixed,
- no free stochastic parameters remain.

---

### 3.2 Closure of the slip and response coefficients

From the kernel‑shape constraint:
$$f(k,a) = C(a)k^2,$$
and from the RG flow of $\varepsilon$:
$$\varepsilon \to 0.$$

Thus
$$\eta(k,a) \to 1.$$

This removes all anisotropic freedom from the perturbation equations.

The coefficients $(A,B,C)$ depend on the gravitational response through $\Phi$ and $\Psi$, and therefore become functions of $K(k,a)$ alone.

Thus:
- $A = A(K,\rho_0)$,
- $B = B(K,\rho_0)$,
- $C = C(K,\rho_0)$.

No free functional dependence remains.

---

### 3.3 Closure of the damping coefficient $\Gamma_\beta$

The damping term is
$$\Gamma_\beta = \Gamma_{\beta 0} + D_\beta k^2/a^2.$$

The $k^2$ term is fixed by the kernel curvature:
$$D_\beta \propto \left.\frac{\partial^2 K}{\partial k^2}\right|_{k=0}.$$

The constant term $\Gamma_{\beta 0}$ is fixed by the background expansion and the RG‑determined correlation length:
$$\Gamma_{\beta 0} = \Gamma_{\beta 0}(\xi_R,\rho_0).$$

Thus $\Gamma_\beta$ is fully determined by $(K,\xi_R,\rho_0)$.

---

### 3.4 Closure of the source term $S_\delta$

The source term couples density to velocity:
$$\beta' + \Gamma_\beta \beta = S_\delta \delta + \Xi_\beta.$$

The coefficient $S_\delta$ arises from the continuity equation and depends only on:
- the background density $\rho_0$,
- the kernel response $K$,
- the slip parameter (now fixed to 1).

Thus
$$S_\delta = S_\delta(K,\rho_0).$$

No functional freedom remains.

---

## 4. Result

All perturbation‑sector coefficients are now fixed:

- Noise amplitude:
  $$\hbar_{\text{eff}} = (\gamma_K/\gamma_\sigma)\rho_0.$$

- Damping:
  $$\Gamma_\beta = \Gamma_\beta(K,\xi_R,\rho_0).$$

- Source:
  $$S_\delta = S_\delta(K,\rho_0).$$

- Density‑evolution coefficients:
  $$A = A(K,\rho_0), \qquad B = B(K,\rho_0), \qquad C = C(K,\rho_0).$$

- Noise statistics:
  $$\langle \Xi_\beta \Xi_\beta' \rangle = C_\beta\,(\gamma_K/\gamma_\sigma)\rho_0\,f_\beta(k)\,\delta_D(\ln a - \ln a')\delta_D(k-k').$$

The perturbation sector contains **no free functions**.

---

## 5. Conditions for Cosmology

- Slip must approach unity.  
- Noise amplitude must track $\rho_0(a)$.  
- Kernel curvature fixes small‑$k$ behaviour.  
- All perturbation coefficients must be functions of $(K,\xi_R,\rho_0)$ only.  
- No arbitrary functions of $k$ or $a$ remain.

---

## 6. Notes

- This completes the closure of the cosmological perturbation sector.  
- All perturbation dynamics are now determined by the continuum RG flows.  
- Next eliminations: full state‑vector reduction or global consistency conditions.
