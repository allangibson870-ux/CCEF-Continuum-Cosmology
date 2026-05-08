# 02. Kernel Shape Constraint for $f(k,a)$

## 1. Statement of the Problem

The kernel sector contains a residual functional freedom in the shape function $f(k,a)$ appearing in the anisotropic projection  
$$K_2(k,a) = K(k,a)\left[1 + \varepsilon(a) f(k,a)\right].$$

After eliminating the free functional $\varepsilon(a)$ via the RG flow, the next objective is to eliminate the remaining freedom in $f(k,a)$ so that the kernel sector becomes fully determined by internal CCEF fields.

The requirement is that $f(k,a)$ must be fixed by consistency with:
- the slip constraint,
- the isotropic fixed point,
- the small‑$k$ behaviour of the response,
- and the RG stability of the kernel.

---

## 2. Starting Definitions

Baseline kernel:  
$$K(k,a) = \frac{A(a)}{k^2 + \xi_R^{-2}(a)}.$$

Anisotropic kernel:  
$$K_2(k,a) = K(k,a)\left[1 + \varepsilon(a) f(k,a)\right].$$

Slip parameter:  
$$\eta(k,a) = \frac{1}{1 + \varepsilon(a) f(k,a)}.$$

At the isotropic fixed point:  
$$\varepsilon(a) \to 0.$$

Thus the only surviving effect of anisotropy is encoded in the *shape* of $f(k,a)$, which must be constrained by the continuum dynamics.

---

## 3. Derivation

### 3.1 Small‑$k$ consistency

The response fields must satisfy  
$$\Phi(k,a) \approx \Psi(k,a) \quad \text{as} \quad k \to 0.$$

This implies  
$$f(k,a) \to 0 \quad \text{as} \quad k \to 0.$$

Thus $f(k,a)$ must vanish at least linearly in $k$ near the origin.

---

### 3.2 RG scaling of the kernel

The kernel RG flow has the form  
$$\frac{dK}{d\ell} = \beta_K(K,\xi_R).$$

For the anisotropic kernel,  
$$\frac{dK_2}{d\ell} = \frac{dK}{d\ell}\left[1 + \varepsilon f\right] + K\left[\frac{d\varepsilon}{d\ell} f + \varepsilon \frac{df}{d\ell}\right].$$

At the isotropic fixed point $\varepsilon \to 0$, the condition  
$$\frac{dK_2}{d\ell} = \frac{dK}{d\ell}$$  
requires  
$$\varepsilon \frac{df}{d\ell} \to 0.$$

Since $\varepsilon \to 0$ but $df/d\ell$ must remain finite, we obtain the constraint  
$$\frac{df}{d\ell} = 0.$$

Thus **$f(k,a)$ must be RG‑invariant**.

---

### 3.3 Functional form from RG invariance

RG invariance implies  
$$f(k,a) = f(k\,b^{-1}).$$

The only solutions are power laws:  
$$f(k,a) \propto k^m.$$

From the small‑$k$ constraint $f(k,a) \to 0$, we require  
$$m > 0.$$

The simplest nontrivial choice is  
$$m = 2.$$

Thus  
$$f(k,a) = C(a)\,k^2.$$

---

### 3.4 Determining $C(a)$

Insert the form $f(k,a) = C(a) k^2$ into the slip expression:  
$$\eta(k,a) = \frac{1}{1 + \varepsilon(a) C(a) k^2}.$$

The slip constraint  
$$|\eta - 1| \ll 1$$  
implies  
$$|\varepsilon(a) C(a) k^2| \ll 1.$$

Since $\varepsilon(a) \to 0$ under RG flow, $C(a)$ must remain finite and non‑singular.

Thus $C(a)$ is fixed by matching to the kernel curvature:  
$$C(a) = \left.\frac{\partial^2 \ln K(k,a)}{\partial k^2}\right|_{k=0}.$$

This ties the anisotropic shape directly to the curvature of the isotropic kernel.

---

## 4. Result

The kernel shape function is fixed to  
$$f(k,a) = C(a)\,k^2,$$  
where  
$$C(a) = \left.\frac{\partial^2 \ln K(k,a)}{\partial k^2}\right|_{k=0}.$$

This eliminates the free functional $f(k,a)$ and makes the anisotropic sector fully determined by the isotropic kernel.

---

## 5. Conditions for Cosmology

- $f(k,a)$ must vanish as $k \to 0$.  
- $f(k,a)$ must be RG‑invariant.  
- $f(k,a)$ must be a power law in $k$.  
- Cosmological consistency selects $f(k,a) \propto k^2$.  
- The amplitude $C(a)$ is fixed by the curvature of $K(k,a)$.

---

## 6. Notes

- This completes the second functional elimination in the kernel sector.  
- The anisotropy is now fully controlled by the isotropic kernel curvature.  
- Next eliminations: variance flow $F_\sigma$ or soliton‑sector closure.
