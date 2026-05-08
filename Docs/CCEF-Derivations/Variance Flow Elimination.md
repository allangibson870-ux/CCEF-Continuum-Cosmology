# 03. Variance Flow Elimination for $F_\sigma$

## 1. Statement of the Problem

The variance sector introduces a functional freedom in the RG flow of the internal variance $\sigma_\alpha^2(a)$ via  
$$\frac{d\sigma_\alpha^2}{d\ell} = F_\sigma(\rho_0, K, \xi_R, \sigma_\alpha^2).$$

We want to eliminate the free functional $F_\sigma$ and replace it with a form determined entirely by internal CCEF quantities and cosmological consistency, so that $\sigma_\alpha^2(a)$ is no longer an arbitrary input but a derived quantity.

The key requirement is that the effective noise scale  
$$\hbar_{\text{eff}}(a) = \sigma_\alpha^2(a)\,\rho_0(a)$$  
remains finite, stable, and compatible with the observed late‑time noise floor in cosmological perturbations.

---

## 2. Starting Definitions

Variance flow:  
$$\frac{d\sigma_\alpha^2}{d\ell} = F_\sigma(\rho_0, K, \xi_R, \sigma_\alpha^2).$$

Effective noise scale:  
$$\hbar_{\text{eff}}(a) = \sigma_\alpha^2(a)\,\rho_0(a).$$

Correlation length flow:  
$$\frac{d\xi_R}{d\ell} = \xi_R\left[\gamma_K - \gamma_\sigma \sigma_\alpha^2\right],$$  
where $\gamma_K$ encodes the kernel contribution and $\gamma_\sigma$ the variance backreaction.

Cosmological noise floor (schematic):  
$$P_{\delta,\text{noise}} \propto \rho_0^3\,\sigma_\alpha^2\,f_\beta(k)\,\frac{a}{k}.$$

---

## 3. Derivation

### 3.1 RG fixed point condition

We require that the variance sector admits a stable fixed point  
$$\frac{d\sigma_\alpha^2}{d\ell} = 0 \quad \Rightarrow \quad F_\sigma(\rho_0, K, \xi_R, \sigma_\alpha^2) = 0.$$

Near the fixed point, expand  
$$F_\sigma \approx A_\sigma(\rho_0, K, \xi_R)\,\sigma_\alpha^2 - B_\sigma(\rho_0, K, \xi_R).$$

The fixed point value is then  
$$\sigma_{\alpha,\ast}^2 = \frac{B_\sigma}{A_\sigma}.$$

---

### 3.2 Coupling to the correlation length

The correlation length flow  
$$\frac{d\xi_R}{d\ell} = \xi_R\left[\gamma_K - \gamma_\sigma \sigma_\alpha^2\right]$$  
must also admit a stable fixed point $\xi_R \to \xi_{R,\ast}$.

At the joint fixed point,  
$$\gamma_K(\rho_0, K) - \gamma_\sigma \sigma_{\alpha,\ast}^2 = 0,$$  
so  
$$\sigma_{\alpha,\ast}^2 = \frac{\gamma_K}{\gamma_\sigma}.$$

Comparing with the previous expression, we identify  
$$\frac{B_\sigma}{A_\sigma} = \frac{\gamma_K}{\gamma_\sigma}.$$

Thus the variance fixed point is determined by the kernel sector via $\gamma_K$ and the backreaction coefficient $\gamma_\sigma$.

---

### 3.3 Functional form of $F_\sigma$

A minimal choice consistent with the fixed point is  
$$\frac{d\sigma_\alpha^2}{d\ell} = A_\sigma(\rho_0, K, \xi_R)\left(\sigma_\alpha^2 - \frac{\gamma_K}{\gamma_\sigma}\right).$$

To avoid introducing new arbitrary functions, we tie $A_\sigma$ to the correlation length scale:  
$$A_\sigma(\rho_0, K, \xi_R) = \lambda_\sigma\,\xi_R^{-q},$$  
with constant $\lambda_\sigma$ and exponent $q > 0$.

Thus  
$$\frac{d\sigma_\alpha^2}{d\ell} = \lambda_\sigma\,\xi_R^{-q}\left(\sigma_\alpha^2 - \frac{\gamma_K}{\gamma_\sigma}\right).$$

This form ensures:
- relaxation toward the fixed point $\sigma_{\alpha,\ast}^2 = \gamma_K/\gamma_\sigma$,  
- stronger flow when $\xi_R$ is small (short‑range correlations),  
- weaker flow when $\xi_R$ is large (long‑range correlations).

---

### 3.4 Behaviour of $\hbar_{\text{eff}}$

Using  
$$\hbar_{\text{eff}}(a) = \sigma_\alpha^2(a)\,\rho_0(a),$$  
and the fixed point value $\sigma_{\alpha,\ast}^2 = \gamma_K/\gamma_\sigma$, we obtain  
$$\hbar_{\text{eff},\ast}(a) = \frac{\gamma_K}{\gamma_\sigma}\,\rho_0(a).$$

Thus the effective noise scale tracks the background density with a proportionality set by the kernel and backreaction coefficients.

This directly controls the amplitude of the noise floor in the density power spectrum.

---

## 4. Result

The free functional $F_\sigma$ is eliminated by choosing the variance flow to be  
$$\frac{d\sigma_\alpha^2}{d\ell} = \lambda_\sigma\,\xi_R^{-q}\left(\sigma_\alpha^2 - \frac{\gamma_K}{\gamma_\sigma}\right),$$  
with constants $\lambda_\sigma$ and $q > 0$.

The fixed point value is  
$$\sigma_{\alpha,\ast}^2 = \frac{\gamma_K}{\gamma_\sigma},$$  
and the effective noise scale becomes  
$$\hbar_{\text{eff},\ast}(a) = \frac{\gamma_K}{\gamma_\sigma}\,\rho_0(a).$$

This removes the functional freedom in $F_\sigma$ and ties the variance sector to the kernel and correlation length dynamics.

---

## 5. Conditions for Cosmology

- The variance flow must admit a stable fixed point.  
- The fixed point must be compatible with the correlation length flow.  
- The effective noise scale must remain finite and track $\rho_0(a)$.  
- The resulting noise floor in $P_\delta$ must be consistent with observations.

---

## 6. Notes

- This completes the elimination of the free functional $F_\sigma$.  
- The variance sector is now slaved to the kernel and correlation length.  
- Next eliminations: soliton‑sector closure or mass‑flow constraints.
