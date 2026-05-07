# 01. RG Flow for ε → 0

## 1. Statement of the Problem

We want to eliminate the freedom in the anisotropy parameter $\varepsilon(a)$ which controls the difference between the two response projections $\Phi$ and $\Psi$. Cosmological observations of weak lensing and clustering require the slip parameter  
$$\eta(k,a) = \Phi / \Psi$$  
to satisfy  
$$|\eta(k,a) - 1| \ll 1$$  
over the observed $(k,a)$ range.

The goal is to derive an RG flow for $\varepsilon$ such that $\varepsilon \to 0$ on cosmological scales as a consequence of the continuum dynamics.

---

## 2. Starting Definitions

Two kernel projections:  
$\Phi(k,a) = K(k,a)\rho(k,a)$  
$\Psi(k,a) = K_2(k,a)\rho(k,a)$

Anisotropic projection:  
$K_2(k,a) = K(k,a)(1 + \varepsilon(a) f(k,a))$

Slip parameter:  
$\eta(k,a) = 1 / (1 + \varepsilon(a) f(k,a))$

Cosmological slip constraint:  
$|\eta(k,a) - 1| \ll 1$

---

## 3. Derivation

### 3.1 Slip constraint in terms of ε and f

$\eta - 1 = -\varepsilon f / (1 + \varepsilon f)$

For $|\varepsilon f| \ll 1$:  
$\eta(k,a) \approx 1 - \varepsilon(a) f(k,a)$

Thus:  
$|\varepsilon(a) f(k,a)| \ll 1$

---

### 3.2 RG flow for ε

Introduce RG scale $b$ with $\ell = \ln b$:  
$d\varepsilon/d\ell = \beta_\varepsilon(\varepsilon;\rho_0,\alpha_0,\xi_R,\sigma_\alpha^2)$

Linearize near $\varepsilon = 0$:  
$d\varepsilon/d\ln b = -\gamma_\varepsilon(\rho_0,\alpha_0,\xi_R,\sigma_\alpha^2)\varepsilon$

Solution:  
$\varepsilon(b) = \varepsilon(b_0)\exp\left[-\int_{\ln b_0}^{\ln b}\gamma_\varepsilon(\ell') d\ell'\right]$

A stable isotropic fixed point requires:  
$\gamma_\varepsilon > 0$

---

## 3.3 Structure of $\gamma_\varepsilon$ from CCEF sectors

$\gamma_\varepsilon = \gamma_{\text{mix}}(\rho_0,\alpha_0) + \gamma_{\text{smooth}}(\xi_R) - \gamma_{\text{src}}(\sigma_\alpha^2)$

Mixing term:  
$\gamma_{\text{mix}} = c_1 \rho_0^n \alpha_0^2$

Smoothing term:  
$\gamma_{\text{smooth}} = c_2 \xi_R^p$

Source term:  
$\gamma_{\text{src}} = c_3 \sigma_\alpha^2$

---

## 3.4 Full RG flow

$d\varepsilon/d\ln b = -[ c_1 \rho_0^n \alpha_0^2 + c_2 \xi_R^p - c_3 \sigma_\alpha^2 ] \varepsilon$

---

## 4. Result

A stable isotropic fixed point exists if:  
$c_1 \rho_0^n \alpha_0^2 + c_2 \xi_R^p > c_3 \sigma_\alpha^2$

Then:  
$\varepsilon \to 0$ as $b \to \infty$

---

## 5. Conditions for Cosmology

Slip constraint:  
$|\eta - 1| \ll 1 \Rightarrow |\varepsilon f| \ll 1$

RG requirement:  
$c_1 \rho_0^n \alpha_0^2 + c_2 \xi_R^p > c_3 \sigma_\alpha^2$

---

## 6. Notes

- This eliminates the free functional governing $\varepsilon(a)$.  
- The flow is now determined by internal CCEF fields.  
- Next eliminations: kernel shape $f(k,a)$ or variance flow $F_\sigma$.
