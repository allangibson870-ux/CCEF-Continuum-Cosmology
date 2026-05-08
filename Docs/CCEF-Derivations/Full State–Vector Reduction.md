# 07. Full State–Vector Reduction

## 1. Statement of the Problem

After eliminating all free functionals in the kernel, variance, soliton, mass, and perturbation sectors, the final task is to identify the **minimal dynamical state vector** of the theory.

Originally, CCEF contains many apparent degrees of freedom:
- continuum density $n(\mathbf{x},a)$,
- kernel $K(k,a)$,
- anisotropy $\varepsilon(a)$,
- kernel shape $f(k,a)$,
- variance $\sigma_\alpha^2(a)$,
- correlation length $\xi_R(a)$,
- soliton states $S_i(a)$,
- soliton masses $m_i(a)$,
- perturbation fields $(\delta,\beta)$,
- noise statistics $\Xi_\beta$.

The goal is to show that, after all eliminations, **only a small subset remains dynamical**, and all others are derived quantities.

---

## 2. Starting Definitions

Continuum density:
$$n(\mathbf{x},a).$$

Background density:
$$\rho_0(a) = \langle n \rangle.$$

Kernel:
$$K(k,a) = \frac{A(a)}{k^2 + \xi_R^{-2}(a)}.$$

Correlation length flow:
$$\frac{d\xi_R}{d\ell} = \xi_R\left[\gamma_K - \gamma_\sigma \sigma_\alpha^2\right].$$

Variance fixed point:
$$\sigma_\alpha^2 = \frac{\gamma_K}{\gamma_\sigma}.$$

Perturbation system:
$$\beta' + \Gamma_\beta \beta = S_\delta \delta + \Xi_\beta,$$
$$\delta'' + A\delta' + B\delta = C\beta.$$

Soliton flow:
$$\frac{dS_i}{d\ell} = -\lambda_S \frac{\partial m_i}{\partial S_i}.$$

---

## 3. Derivation

### 3.1 Eliminating the anisotropy sector

From the RG flow:
$$\varepsilon \to 0.$$

From the kernel‑shape constraint:
$$f(k,a) = C(a)k^2.$$

Thus the anisotropic kernel becomes:
$$K_2 = K.$$

**No anisotropy variables remain.**

---

### 3.2 Eliminating the variance sector

From the variance‑flow elimination:
$$\sigma_\alpha^2 = \frac{\gamma_K}{\gamma_\sigma}.$$

Thus $\sigma_\alpha^2$ is no longer dynamical.

The effective noise scale becomes:
$$\hbar_{\text{eff}} = \frac{\gamma_K}{\gamma_\sigma}\rho_0.$$

**No variance variables remain.**

---

### 3.3 Eliminating the soliton sector

From the soliton‑sector closure:
$$\frac{dS_i}{d\ell} = -\lambda_S \frac{\partial m_i}{\partial S_i},$$

and from mass‑flow consistency:
$$m_i(a) = m_i(\ell_0) + \int(\alpha_K K_0 - \alpha_\xi \xi_R^{-1} + \alpha_\sigma \sigma_\alpha^2)d\ell.$$

Thus:
- $m_i(a)$ is determined by $(K_0,\xi_R,\sigma_\alpha^2)$,
- $S_i(a)$ is determined by $m_i(a)$.

**No soliton variables remain.**

---

### 3.4 Eliminating the perturbation coefficients

From perturbation closure:
- $A = A(K,\rho_0)$,
- $B = B(K,\rho_0)$,
- $C = C(K,\rho_0)$,
- $\Gamma_\beta = \Gamma_\beta(K,\xi_R,\rho_0)$,
- $S_\delta = S_\delta(K,\rho_0)$.

Thus the only dynamical perturbation fields are:
$$\delta(k,a), \qquad \beta(k,a).$$

**No perturbation coefficients remain.**

---

### 3.5 Remaining dynamical fields

After all eliminations, the only fields that still evolve independently are:

1. **The continuum density field**  
   $$n(\mathbf{x},a).$$

2. **The correlation length**  
   $$\xi_R(a).$$

3. **The perturbation fields**  
   $$\delta(k,a), \qquad \beta(k,a).$$

Everything else is derived from these.

---

## 4. Result: The Minimal State Vector

The full CCEF state vector reduces to:

$$\boxed{\mathcal{X}(a) = \{\,n(\mathbf{x},a),\ \xi_R(a),\ \delta(k,a),\ \beta(k,a)\,\}}.$$

All other quantities are fixed functions of $\mathcal{X}$:

- Kernel:
  $$K = K(n,\xi_R).$$

- Noise:
  $$\hbar_{\text{eff}} = (\gamma_K/\gamma_\sigma)\rho_0.$$

- Soliton masses:
  $$m_i = m_i(K,\xi_R).$$

- Perturbation coefficients:
  $$A,B,C,\Gamma_\beta,S_\delta = \text{functions of } (K,\xi_R,\rho_0).$$

- Slip:
  $$\eta = 1.$$

- Anisotropy:
  $$\varepsilon = 0.$$

- Kernel shape:
  $$f(k,a) = C(a)k^2.$$

**No free parameters.  
No free functions.  
No arbitrary inputs.**

---

## 5. Conditions for Cosmology

- The background density $\rho_0(a)$ must follow the Friedmann‑like equation derived from the continuum.  
- The correlation length must follow its RG flow.  
- Perturbations must evolve under the closed LITE system.  
- All soliton properties must follow from $(K,\xi_R,\rho_0)$.

---

## 6. Notes

- This completes the full state‑vector reduction.  
- The theory is now fully predictive.  
- Next step: global consistency conditions and observational predictions.
