# 04. Soliton–Sector Closure

## 1. Statement of the Problem

The soliton sector introduces state variables $S_i(a)$ and conserved topological charges $Q_i$ that describe baryonic and leptonic excitations embedded in the continuum field. Their RG evolution is given by  
$$\frac{dS_i}{d\ell} = F_i(K,\xi_R,\sigma_\alpha^2), \qquad \frac{dQ_i}{d\ell} = 0.$$

The goal is to eliminate the free functional dependence in $F_i$ and tie the soliton evolution directly to the kernel and variance sectors, ensuring that soliton properties are not arbitrary inputs but derived consequences of the continuum dynamics.

---

## 2. Starting Definitions

Topological charge:  
$$Q = \frac{1}{4\pi}\int d^3x\,\epsilon_{ijk}\,\partial_i n \cdot (\partial_j n \times \partial_k n).$$

Soliton state variables:  
$$S_i(a).$$

Mass functionals:  
$$m_i(a) = \int d^3x\,\mathcal{E}_{\text{soliton},i}(n).$$

Mass flow:  
$$\frac{dm_i}{d\ell} = \alpha_K K(k\to 0) - \alpha_\xi \xi_R^{-1} + \alpha_\sigma \sigma_\alpha^2.$$

Soliton RG flow:  
$$\frac{dS_i}{d\ell} = F_i(K,\xi_R,\sigma_\alpha^2).$$

---

## 3. Derivation

### 3.1 Constraint from topological invariance

Since  
$$\frac{dQ_i}{d\ell} = 0,$$  
the soliton configuration must remain in the same topological class under RG flow.

This implies that $S_i(a)$ cannot change in a way that alters the winding number. Therefore, the allowed flow must be tangent to the moduli space of fixed‑charge solitons.

Thus  
$$F_i \propto \frac{\partial m_i}{\partial S_i}.$$

The soliton flow must be a gradient flow of the soliton mass functional.

---

### 3.2 Coupling to the mass flow

The mass flow equation  
$$\frac{dm_i}{d\ell} = \alpha_K K_0 - \alpha_\xi \xi_R^{-1} + \alpha_\sigma \sigma_\alpha^2$$  
(where $K_0 = K(k\to 0)$)  
implies that $m_i$ is fully determined by the kernel and variance sectors.

Thus  
$$\frac{dm_i}{d\ell} = \frac{\partial m_i}{\partial S_i}\frac{dS_i}{d\ell}.$$

Substituting the gradient‑flow form,  
$$\frac{dS_i}{d\ell} = -\lambda_S \frac{\partial m_i}{\partial S_i},$$  
we obtain  
$$\frac{dm_i}{d\ell} = -\lambda_S \left(\frac{\partial m_i}{\partial S_i}\right)^2.$$

Matching this to the continuum expression fixes $\lambda_S$.

Thus the soliton flow is  
$$\frac{dS_i}{d\ell} = -\lambda_S \frac{\partial m_i}{\partial S_i},$$  
with  
$$\lambda_S = -\frac{\alpha_K K_0 - \alpha_\xi \xi_R^{-1} + \alpha_\sigma \sigma_\alpha^2}{\left(\frac{\partial m_i}{\partial S_i}\right)^2}.$$

---

### 3.3 Eliminating the free functional $F_i$

We now have  
$$F_i(K,\xi_R,\sigma_\alpha^2) = -\lambda_S \frac{\partial m_i}{\partial S_i},$$  
where $\lambda_S$ is fixed by the kernel, correlation length, and variance sectors.

Thus the soliton flow is no longer arbitrary:  
- its direction is fixed by the gradient of the soliton mass,  
- its magnitude is fixed by the continuum RG flows.

This eliminates the free functional $F_i$.

---

## 4. Result

The soliton‑sector RG flow is  
$$\frac{dS_i}{d\ell} = -\lambda_S \frac{\partial m_i}{\partial S_i},$$  
with  
$$\lambda_S = -\frac{\alpha_K K_0 - \alpha_\xi \xi_R^{-1} + \alpha_\sigma \sigma_\alpha^2}{\left(\frac{\partial m_i}{\partial S_i}\right)^2}.$$

This removes the functional freedom in $F_i$ and ties soliton evolution directly to the kernel, correlation length, and variance sectors.

---

## 5. Conditions for Cosmology

- Soliton charges remain conserved.  
- Soliton evolution must be tangent to fixed‑charge moduli space.  
- Mass flow must match the continuum RG expression.  
- Soliton dynamics become fully determined by $K$, $\xi_R$, and $\sigma_\alpha^2$.

---

## 6. Notes

- This completes the soliton‑sector closure.  
- All soliton properties now follow from continuum RG flows.  
- Next eliminations: mass‑flow consistency or cosmological perturbation closure.
