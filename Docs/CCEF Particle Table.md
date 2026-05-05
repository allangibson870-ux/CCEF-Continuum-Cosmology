# CCEF Particle Table v0.1  
### (One‑Core Soliton Family)

This defines a minimal particle‑like sector inside CCEF using only:
- soliton textures of the continuum field `n(x,t)`
- response kernels `K(k,a)`, `K2(k,a)`
- variance sector `sigma_alpha^2(delta,a)`
- density‑triggered RG flow

No QFT, no GR, no quantization.

---

## 1. Soliton Species (One‑Core Family)

| Species       | Symbol  | Core Type  | Effective Mass Relation      | Kernel Couplings (g_grav, g_EM, g_weak) | Notes                          |
|--------------|---------|------------|------------------------------|------------------------------------------|--------------------------------|
| Electron‑like | `S_e`   | Single‑core | `m_e >> m_nu`                | `(1, +1, epsilon)`                       | Massive, charged, stable       |
| Photon‑like   | `S_gamma` | Single‑core (radiative mode) | `~ 0`                        | `(0, 0, 0)` as a source; follows kernels as a probe | Massless/very light excitation |
| Neutrino‑like | `S_nu`  | Single‑core | `m_nu << m_e`                | `(1, 0, g_weak)`                         | Neutral, weakly coupled        |

**Interpretation**

- All three species share the same one‑core morphology of `n(x,t)`.
- Their differences arise from internal texture and kernel‑coupling patterns.
- “Charge” is the pattern of kernel response, not a fundamental label.

---

## 2. Kernel Sectors

We conceptually partition the response kernels into three sectors:

| Kernel Sector | Symbol            | Range      | Role                                                |
|---------------|-------------------|-----------|-----------------------------------------------------|
| Grav‑like     | `K_grav(k,a)`     | Long‑range | Universal attraction; couples to all massive solitons |
| EM‑like       | `K_EM(k,a)`       | Long‑range | Sign‑sensitive; couples only to solitons with EM response |
| Weak‑like     | `K_weak(k,a)`     | Short‑range | Enables rare transitions; suppressed in low‑variance regions |

These are not gauge fields — they are structured response channels of the continuum.

---

## 3. Interaction Table (v0.1)

| Process                          | Allowed? | Mediating Kernel(s)      | Notes                                      |
|----------------------------------|----------|--------------------------|--------------------------------------------|
| `S_e + S_e -> S_e + S_e`         | Yes      | `K_EM`, `K_grav`         | Coulomb‑like + grav‑like scattering        |
| `S_e + S_nu -> S_e + S_nu`       | Yes      | `K_weak`, `K_grav`       | Weak‑like + grav‑like                      |
| `S_nu + S_nu -> S_nu + S_nu`     | Yes      | `K_weak`, `K_grav`       | Very weak scattering                       |
| `S_e + S_e -> S_e + S_e + S_gamma` | Yes    | `K_EM`                   | Radiative continuum excitation (bremsstrahlung‑like) |
| `S_e -> S_e + S_gamma`           | Yes      | `K_EM`                   | Accelerated soliton emits photon‑like mode |
| `S_e -> S_nu + ...`              | Rare     | `K_weak`                 | Requires high variance; environment‑dependent |

---

## 4. Variance and Environment Dependence

The variance sector `sigma_alpha^2(delta,a)` modulates interaction sharpness:

- **Halos (high delta)**  
  - `sigma_alpha^2 -> 0`  
  - interactions become sharp and classical‑like  
  - soliton identities stable

- **Voids (low delta)**  
  - `sigma_alpha^2` remains large  
  - interactions noisy, rare, fuzzy  
  - “quantum‑like” behaviour emerges naturally

This replaces the role of Planck’s constant and vacuum fluctuations.

---

# Example Interaction  
## `S_e + S_e -> S_e + S_e + S_gamma`  
### (CCEF analogue of bremsstrahlung)

**1. Setup**

Two electron‑like solitons `S_e` approach with relative acceleration.

**2. Continuum Response**

Their overlapping textures source the EM‑like kernel:

- the local configuration of `n(x,t)` is distorted,
- the EM‑like response `K_EM` is strongly excited in the interaction region.

**3. Radiative Mode Formation**

The continuum develops a propagating disturbance:

- a localized, outward‑moving pattern in `n(x,t)`  
- this stabilizes into a photon‑like soliton `S_gamma` (same one‑core family, different internal texture).

**4. Outgoing State**

- two deflected `S_e` solitons  
- one emitted `S_gamma` soliton  
- energy balance enforced by the continuum energy functional for `n(x,t)`

**5. Variance Dependence**

- In halos: low `sigma_alpha^2` → emission is sharp and repeatable.  
- In voids: high `sigma_alpha^2` → emission is noisy and probabilistic.

No quantization, no operators — just soliton dynamics, kernels, and variance inside CCEF.
