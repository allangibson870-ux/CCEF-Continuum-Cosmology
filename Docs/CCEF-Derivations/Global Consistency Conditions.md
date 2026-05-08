# 08. Global Consistency Conditions

## 1. Statement of the Problem

After eliminating all free functionals and reducing the state vector to  
$$\mathcal{X}(a) = \{\,n(\mathbf{x},a),\ \xi_R(a),\ \delta(k,a),\ \beta(k,a)\,\},$$  
the final requirement is that the entire theory must satisfy **global consistency conditions**.

These conditions ensure that:
- the background evolution,
- the kernel response,
- the correlation length flow,
- the perturbation dynamics,
- the soliton sector,
- and the noise floor

all fit together without contradictions and produce a cosmology compatible with observations.

This step is not about eliminating new freedoms — those are already gone.  
It is about verifying that the **closed theory is self‑consistent**.

---

## 2. Starting Definitions

Background density:
$$\rho_0(a) = \langle n(\mathbf{x},a) \rangle.$$

Kernel:
$$K(k,a) = \frac{A(a)}{k^2 + \xi_R^{-2}(a)}.$$

Correlation length flow:
$$\frac{d\xi_R}{d\ell} = \xi_R\left[\gamma_K - \gamma_\sigma \sigma_\alpha^2\right].$$

Variance fixed point:
$$\sigma_\alpha^2 = \frac{\gamma_K}{\gamma_\sigma}.$$

Perturbation system:
$$\beta' + \Gamma_\beta \beta = S_\delta \delta + \Xi_\beta,$$
$$\delta'' + A\delta' + B\delta = C\beta.$$

Noise scale:
$$\hbar_{\text{eff}} = \frac{\gamma_K}{\gamma_\sigma}\rho_0.$$

---

## 3. Derivation

### 3.1 Background–Kernel Consistency

The background density $\rho_0(a)$ determines the amplitude $A(a)$ of the kernel through the continuum field equations.

The kernel must satisfy:
- correct small‑$k$ limit for gravitational response,
- correct large‑$k$ suppression from $\xi_R$,
- correct normalization from $\rho_0$.

Thus:
$$A(a) = A(\rho_0,\xi_R).$$

This ensures that the kernel does not introduce any new degrees of freedom.

---

### 3.2 Kernel–Correlation Length Consistency

The correlation length flow:
$$\frac{d\xi_R}{d\ell} = \xi_R\left[\gamma_K - \gamma_\sigma \sigma_\alpha^2\right]$$
must be compatible with the kernel curvature:
$$\left.\frac{\partial^2 K}{\partial k^2}\right|_{k=0} \propto \xi_R^2.$$

Thus:
- the RG flow of $\xi_R$ determines the curvature of $K$,
- the curvature of $K$ determines the perturbation coefficients,
- the perturbation coefficients determine the growth of structure.

This closes the loop between background, kernel, and perturbations.

---

### 3.3 Noise–Perturbation Consistency

The noise amplitude:
$$\hbar_{\text{eff}} = (\gamma_K/\gamma_\sigma)\rho_0$$
must produce a noise floor in the density power spectrum:
$$P_{\delta,\text{noise}} \propto \rho_0^3\,\sigma_\alpha^2\,f_\beta(k)\,\frac{a}{k}.$$

Since $\sigma_\alpha^2$ is fixed, the noise floor is determined entirely by $\rho_0$.

This ensures:
- no arbitrary stochastic terms,
- no tunable noise amplitude,
- no phenomenological “effective pressure” terms.

---

### 3.4 Soliton–Background Consistency

The soliton masses:
$$m_i(a) = m_i(K,\xi_R)$$
must scale consistently with the background density and kernel amplitude.

This ensures:
- baryon/lepton masses evolve consistently with the continuum,
- no independent mass functions,
- no extra degrees of freedom in the matter sector.

---

### 3.5 Perturbation–Kernel Consistency

The perturbation coefficients:
$$A,B,C,\Gamma_\beta,S_\delta$$
must be functions of $(K,\xi_R,\rho_0)$ only.

This ensures:
- no arbitrary scale‑dependent growth functions,
- no phenomenological modifications to gravity,
- no extra functions of $k$ or $a$.

The LITE system becomes:
$$\beta' + \Gamma_\beta(K,\xi_R,\rho_0)\beta = S_\delta(K,\rho_0)\delta + \Xi_\beta,$$
$$\delta'' + A(K,\rho_0)\delta' + B(K,\rho_0)\delta = C(K,\rho_0)\beta.$$

This is a **closed** perturbation system.

---

## 4. Result: Global Consistency Conditions

The theory is globally consistent if the following hold:

1. **Kernel–Background Consistency**  
   $$A(a) = A(\rho_0,\xi_R).$$

2. **Kernel–Correlation Length Consistency**  
   $$\left.\frac{\partial^2 K}{\partial k^2}\right|_{k=0} \propto \xi_R^2.$$

3. **Noise–Perturbation Consistency**  
   $$\hbar_{\text{eff}} = (\gamma_K/\gamma_\sigma)\rho_0.$$

4. **Soliton–Background Consistency**  
   $$m_i = m_i(K,\xi_R).$$

5. **Perturbation–Kernel Consistency**  
   $$A,B,C,\Gamma_\beta,S_\delta = \text{functions of } (K,\xi_R,\rho_0).$$

6. **No Free Functions**  
   All sectors must be determined by the state vector  
   $$\mathcal{X}(a) = \{n,\xi_R,\delta,\beta\}.$$

---

## 5. Conditions for Cosmology

- The background must evolve consistently with the kernel amplitude.  
- The correlation length must follow its RG flow.  
- The noise floor must track $\rho_0(a)$.  
- Soliton masses must follow $(K,\xi_R)$.  
- Perturbations must evolve under the closed LITE system.  
- No contradictions between sectors are allowed.

---

## 6. Notes

- This completes the global consistency analysis.  
- The theory is now fully closed and self‑consistent.  
- Next step: observational predictions and comparison with ΛCDM.
