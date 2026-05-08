# 05. Mass–Flow Consistency

## 1. Statement of the Problem

The soliton masses evolve under RG flow according to  
$$\frac{dm_i}{d\ell} = \alpha_K K(k\!\to\!0) - \alpha_\xi \xi_R^{-1} + \alpha_\sigma \sigma_\alpha^2.$$

This expression contains no free functional, but the soliton mass $m_i(a)$ is still an independent state variable unless we show that it is fully determined by the continuum fields.

The goal is to eliminate the remaining freedom in $m_i(a)$ by demonstrating that the mass flow is completely fixed by the kernel, correlation length, and variance sectors, and that no additional soliton‑sector input is required.

---

## 2. Starting Definitions

Soliton mass functional:  
$$m_i(a) = \int d^3x\,\mathcal{E}_{\text{soliton},i}(n).$$

Mass flow:  
$$\frac{dm_i}{d\ell} = \alpha_K K_0 - \alpha_\xi \xi_R^{-1} + \alpha_\sigma \sigma_\alpha^2,$$  
where $K_0 = K(k\to 0)$.

Soliton flow (from previous derivation):  
$$\frac{dS_i}{d\ell} = -\lambda_S \frac{\partial m_i}{\partial S_i}.$$

Gradient relation:  
$$\frac{dm_i}{d\ell} = \frac{\partial m_i}{\partial S_i}\frac{dS_i}{d\ell}.$$

---

## 3. Derivation

### 3.1 Matching the two mass flows

We have two expressions for $dm_i/d\ell$:

1. From continuum RG:
   $$\frac{dm_i}{d\ell} = \alpha_K K_0 - \alpha_\xi \xi_R^{-1} + \alpha_\sigma \sigma_\alpha^2.$$

2. From soliton gradient flow:
   $$\frac{dm_i}{d\ell} = -\lambda_S\left(\frac{\partial m_i}{\partial S_i}\right)^2.$$

Equating them gives  
$$-\lambda_S\left(\frac{\partial m_i}{\partial S_i}\right)^2 = \alpha_K K_0 - \alpha_\xi \xi_R^{-1} + \alpha_\sigma \sigma_\alpha^2.$$

Thus  
$$\lambda_S = -\frac{\alpha_K K_0 - \alpha_\xi \xi_R^{-1} + \alpha_\sigma \sigma_\alpha^2}{\left(\frac{\partial m_i}{\partial S_i}\right)^2}.$$

This shows that the soliton mass flow is not independent: it is fixed by the continuum fields.

---

### 3.2 Eliminating $m_i(a)$ as an independent variable

Since  
$$\frac{dm_i}{d\ell} = f(K_0,\xi_R,\sigma_\alpha^2),$$  
the mass is obtained by integrating a known function of continuum fields:

$$m_i(\ell) = m_i(\ell_0) + \int_{\ell_0}^{\ell}\left[\alpha_K K_0 - \alpha_\xi \xi_R^{-1} + \alpha_\sigma \sigma_\alpha^2\right] d\ell'.$$

Thus $m_i(a)$ is not a free function:  
- its evolution is fixed,  
- its value at any scale is determined by the continuum fields,  
- and its initial value is fixed by the topological class (baryon vs lepton).

Therefore the soliton mass is fully slaved to the continuum RG flows.

---

### 3.3 Consistency with the soliton‑sector closure

From the previous derivation,  
$$\frac{dS_i}{d\ell} = -\lambda_S \frac{\partial m_i}{\partial S_i}.$$

Since $\lambda_S$ is now fixed by the mass flow, the soliton flow is also fixed.

Thus:
- $S_i(a)$ is determined by $m_i(a)$,
- $m_i(a)$ is determined by $(K_0,\xi_R,\sigma_\alpha^2)$,
- therefore $S_i(a)$ is determined by $(K_0,\xi_R,\sigma_\alpha^2)$.

No soliton‑sector freedom remains.

---

## 4. Result

The mass flow is  
$$\frac{dm_i}{d\ell} = \alpha_K K_0 - \alpha_\xi \xi_R^{-1} + \alpha_\sigma \sigma_\alpha^2,$$  
and this fully determines $m_i(a)$.

The soliton‑sector flow coefficient is  
$$\lambda_S = -\frac{\alpha_K K_0 - \alpha_\xi \xi_R^{-1} + \alpha_\sigma \sigma_\alpha^2}{\left(\frac{\partial m_i}{\partial S_i}\right)^2}.$$

This eliminates the last free degree of freedom in the soliton sector.

---

## 5. Conditions for Cosmology

- Soliton masses must track the continuum RG flows.  
- No independent soliton mass function is allowed.  
- Mass evolution must be consistent with the noise and kernel sectors.  
- Baryon/lepton mass ratios remain fixed by topology, not by free parameters.

---

## 6. Notes

- This completes the soliton‑mass closure.  
- All soliton properties are now determined by continuum fields.  
- Next eliminations: cosmological perturbation closure or full state‑vector reduction.
