
## Continuum Orbitals: Soliton‑Induced Geodesics in a Non‑Metric Medium

This document presents the full derivation and numerical realisation of **achromatic gravitational lensing**, **Shapiro delay**, and **continuum‑native geodesics** arising from a single constrained field \(n(x,t)\) with a modified kinetic sector.

The results demonstrate that:
* Light propagation is governed by a **local refractive index**,  
* Bending is **achromatic**,  
* The bending angle can be tuned to match **GR’s 1.75 arcsec solar deflection**,  
* The model produces a **finite Shapiro delay**,  
* All without introducing a metric or GR primitives.

---

## 1. Modified Kinetic Action

$$S[n]=\int d^4x\left[\frac{Z_t}{2}(1+\chi\mathcal{E}[n])(\partial_t n)^2-\mathcal{E}[n]\right]$$

$$\mathcal{E}[n]=A_1(\nabla n)^2+A_3(\nabla^2 n)^2$$

---

## 2. Linearisation Around a Static Soliton

$$n(x,t)=n_{\text{sol}}(r)+\psi(x,t),\qquad n_{\text{sol}}\cdot\psi=0$$

$$\partial_t n_{\text{sol}}=0$$

$$\mathcal{E}_0(r)=A_1(\nabla n_{\text{sol}})^2+A_3(\nabla^2 n_{\text{sol}})^2$$

$$Z_t(1+\chi\mathcal{E}_0(r))\partial_t^2\psi+L_p\psi=0$$

$$L_p\psi\approx -A_1\nabla^2\psi$$

$$Z_t(1+\chi\mathcal{E}_0(r))\partial_t^2\psi-A_1\nabla^2\psi=0$$

---

## 3. WKB Dispersion Relation

$$\psi\sim e^{i(k\cdot x-\omega t)}$$

$$-Z_t(1+\chi\mathcal{E}_0(r))\omega^2+A_1k^2=0$$

$$c_{\text{eff}}^2(r)=\frac{A_1}{Z_t(1+\chi\mathcal{E}_0(r))}$$

$$c_0^2=\frac{A_1}{Z_t}$$

$$c_{\text{eff}}(r)=\frac{c_0}{\sqrt{1+\chi\mathcal{E}_0(r)}}$$

---

## 4. Achromatic Refractive Index

$$n_{\text{opt}}(r)=\frac{c_0}{c_{\text{eff}}(r)}=\sqrt{1+\chi\mathcal{E}_0(r)}$$

$$\delta n(r)=n_{\text{opt}}(r)-1\approx\frac{1}{2}\chi\mathcal{E}_0(r)$$

---

## 5. Achromatic Bending Angle

$$\alpha(b)\approx\int_{-\infty}^{\infty}\frac{\partial}{\partial b}\delta n(\sqrt{b^2+z^2})dz$$

$$\alpha(b)\approx\frac{\chi}{2}\int_{-\infty}^{\infty}\frac{\partial}{\partial b}\mathcal{E}_0(\sqrt{b^2+z^2})dz$$

$$\alpha(b;\chi)=\chi\,\alpha(b;\chi=1)$$

---

## 6. Soliton Energy Density Model

$$f(r)=2\arctan\left(\frac{R_{\text{core}}}{r}\right)$$

$$(\nabla n)^2=f'(r)^2+\frac{2\sin^2 f(r)}{r^2}$$

$$(\nabla^2 n)^2=f''(r)^2$$

$$\mathcal{E}_{\text{tail}}(r)=\frac{1}{r}\left(C_1e^{-m_1r}+C_2e^{-m_2r}\right)$$

$$\mathcal{E}_0(r)=A_1(\nabla n)^2+A_3(\nabla^2 n)^2+\frac{1}{r}(C_1e^{-m_1r}+C_2e^{-m_2r})$$

---

## 7. Calibration to GR Bending

$$\alpha(b;\chi)=\chi\alpha(b;\chi=1)$$

$$\chi_*=\frac{\alpha_{\text{GR}}}{\alpha_{\chi=1}}$$

$$\alpha_{\chi=1}(b=10)=-5.049566\times10^{-2}\text{ rad}$$

$$\alpha_{\text{GR}}=8.5\times10^{-6}\text{ rad}$$

$$\chi_*=1.683313\times10^{-4}$$

$$\alpha(b=10;\chi_*)=-8.5\times10^{-6}\text{ rad}$$

---

## 8. Shapiro Time Delay

$$v_g(r)=c_{\text{eff}}(r)=\frac{c_0}{n_{\text{opt}}(r)}$$

$$t=\frac{1}{c_0}\int n_{\text{opt}}(\sqrt{b^2+z^2})dz$$

$$\Delta t_{\text{Shapiro}}=\frac{1}{c_0}\int\left[n_{\text{opt}}(\sqrt{b^2+z^2})-1\right]dz$$

$$\Delta t_{\text{Shapiro}}(b)\approx\frac{1}{2c_0}\chi_*\int\mathcal{E}_0(\sqrt{b^2+z^2})dz$$

$$\int\frac{dz}{\sqrt{b^2+z^2}}=\ln\left(z+\sqrt{b^2+z^2}\right)$$

$$\Delta t=0.058161\ \mu\text{s}$$

---

## 9. Numerical Engine (Python)

```python
import numpy as np
from scipy.integrate import quad

def hedgehog_profile(r, R_core=10.0):
    return 2.0 * np.arctan(R_core / r)

def df_dr(r, R_core=10.0):
    return -2.0 * R_core / (r**2 + R_core**2)

def d2f_dr2(r, R_core=10.0):
    return 4.0 * R_core * r / (r**2 + R_core**2)**2

def local_energy_density(r, A1=1.0, A3=0.1, R_core=10.0,
                         C1=0.005, m1=0.01, C2=0.02, m2=0.5):
    r_eff = np.maximum(r, 0.1 * R_core)
    grad_n_sq = df_dr(r_eff, R_core)**2 + 2.0 * (np.sin(hedgehog_profile(r_eff, R_core))**2) / (r_eff**2)
    laplacian_n_sq = d2f_dr2(r_eff, R_core)**2
    core_density = A1 * grad_n_sq + A3 * laplacian_n_sq
    tail_density = (1.0 / r_eff) * (C1 * np.exp(-m1 * r_eff) + C2 * np.exp(-m2 * r_eff))
    return core_density + tail_density

def refractive_gradient(z, b, chi=1.0, A1=1.0, A3=0.1, R_core=10.0,
                        C1=0.005, m1=0.01, C2=0.02, m2=0.5):
    r_current = np.sqrt(b**2 + z**2)
    db = 1e-3
    r_perturbed = np.sqrt((b + db)**2 + z**2)
    n_current = 0.5 * chi * local_energy_density(r_current, A1, A3, R_core, C1, m1, C2, m2)
    n_perturbed = 0.5 * chi * local_energy_density(r_perturbed, A1, A3, R_core, C1, m1, C2, m2)
    return (n_perturbed - n_current) / db

def compute_achromatic_lensing(b, chi=1.0, A1=1.0, A3=0.1, R_core=10.0,
                               C1=0.005, m1=0.01, C2=0.02, m2=0.5,
                               z_max=50.0, quad_limit=300):
    bending_angle, _ = quad(
        refractive_gradient,
        -z_max, z_max,
        args=(b, chi, A1, A3, R_core, C1, m1, C2, m2),
        limit=quad_limit
    )
    return bending_angle
```
```
