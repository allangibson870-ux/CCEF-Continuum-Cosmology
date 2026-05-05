# CCEF Particle Sector v0.2  
### One‑Core and Two‑Core Soliton Families

This file defines a minimal particle‑like sector inside CCEF using only:

- the continuum field `n(x,t)`
- soliton textures (one‑core and two‑core)
- response kernels `K(k,a)`, `K2(k,a)`
- variance sector `sigma_alpha^2(delta,a)`
- density‑triggered RG flow

No QFT, no GR, no quantization.

---

## 1. One‑Core Soliton Species (v0.1)

These are the simplest localized excitations (single‑core solitons) of `n(x,t)`.

| Species       | Symbol    | Core Type   | Effective Mass Relation | Kernel Couplings (g_grav, g_EM, g_weak) | Notes                          |
|--------------|-----------|------------|-------------------------|------------------------------------------|--------------------------------|
| Electron‑like | `S_e`     | One‑core   | `m_e >> m_nu`           | `(1, +1, epsilon)`                       | Massive, charged, stable       |
| Photon‑like   | `S_gamma` | One‑core (radiative mode) | `~ 0`             | `(0, 0, 0)` as a source; follows kernels as a probe | Massless/very light excitation |
| Neutrino‑like | `S_nu`    | One‑core   | `m_nu << m_e`           | `(1, 0, g_weak)`                         | Neutral, weakly coupled        |

**Interpretation**

- All three species share the same one‑core morphology of `n(x,t)`.
- Their differences arise from internal texture and kernel‑coupling patterns.
- “Charge” is the pattern of kernel response, not a fundamental label.

---

## 2. Kernel Sectors

We conceptually partition the response kernels into three sectors:

| Kernel Sector | Symbol        | Range      | Role                                                |
|---------------|--------------|-----------|-----------------------------------------------------|
| Grav‑like     | `K_grav(k,a)` | Long‑range | Universal attraction; couples to all massive solitons |
| EM‑like       | `K_EM(k,a)`   | Long‑range | Sign‑sensitive; couples only to solitons with EM response |
| Weak‑like     | `K_weak(k,a)` | Short‑range | Enables rare transitions; suppressed in low‑variance regions |

These are not gauge fields — they are structured response channels of the continuum.

---

## 3. One‑Core Interaction Table (v0.1)

| Process                              | Allowed? | Mediating Kernel(s)      | Notes                                      |
|--------------------------------------|----------|--------------------------|--------------------------------------------|
| `S_e + S_e -> S_e + S_e`             | Yes      | `K_EM`, `K_grav`         | Coulomb‑like + grav‑like scattering        |
| `S_e + S_nu -> S_e + S_nu`           | Yes      | `K_weak`, `K_grav`       | Weak‑like + grav‑like                      |
| `S_nu + S_nu -> S_nu + S_nu`         | Yes      | `K_weak`, `K_grav`       | Very weak scattering                       |
| `S_e + S_e -> S_e + S_e + S_gamma`   | Yes      | `K_EM`                   | Radiative continuum excitation (bremsstrahlung‑like) |
| `S_e -> S_e + S_gamma`               | Yes      | `K_EM`                   | Accelerated soliton emits photon‑like mode |
| `S_e -> S_nu + ...`                  | Rare     | `K_weak`                 | Requires high variance; environment‑dependent |

---

## 4. Variance and Environment Dependence

The variance sector `sigma_alpha^2(delta,a)` modulates interaction sharpness:

- Halos (high delta)  
  - `sigma_alpha^2 -> 0`  
  - interactions become sharp and classical‑like  
  - soliton identities stable

- Voids (low delta)  
  - `sigma_alpha^2` remains large  
  - interactions noisy, rare, fuzzy  
  - “quantum‑like” behaviour emerges naturally

This replaces the role of Planck’s constant and vacuum fluctuations.

---

## 5. Example One‑Core Interaction  
### `S_e + S_e -> S_e + S_e + S_gamma` (bremsstrahlung‑like)

1. Two electron‑like solitons `S_e` approach with relative acceleration.  
2. Their overlapping textures distort `n(x,t)` and strongly excite the EM‑like kernel `K_EM`.  
3. The continuum develops a propagating disturbance that stabilizes into a photon‑like soliton `S_gamma`.  
4. Outgoing state: two deflected `S_e` solitons + one emitted `S_gamma`.  
5. Energy balance is enforced by the continuum energy functional for `n(x,t)`.  
6. In halos (low variance), emission is sharp; in voids (high variance), emission is noisy and probabilistic.

No quantization, no operators — just soliton dynamics, kernels, and variance inside CCEF.

---

## 6. Two‑Core Composite Soliton (Proton‑Like)  
### CCEF Particle Sector v0.2 Extension

We now add a two‑core composite soliton representing a proton‑like object.

### 6.1 Species Definition

| Species      | Symbol | Core Type | Description |
|-------------|--------|-----------|-------------|
| Proton‑like | `S_p`  | Two‑core  | A bound configuration of two one‑core solitons with a stable internal texture pattern |

**Structural Notes**

- `S_p` is not fundamental.  
- It is a bound state of two one‑core solitons (e.g. two `S_e`‑like or mixed‑texture cores).  
- Stability arises from a balance between:
  - short‑range repulsion (internal texture pressure)
  - long‑range attraction (grav‑like kernel)
  - medium‑range binding (EM‑like or weak‑like kernel components)

---

### 6.2 Effective Mass

The effective mass of the composite soliton is:

- `m_p = m_core1 + m_core2 + E_binding`

Where:

- `m_core1`, `m_core2` are the effective masses of the constituent one‑core solitons  
- `E_binding` is negative (binding energy)  

Hierarchy:

- `m_p >> m_e`  
- `m_p >> m_nu`  

This matches the role of a proton‑like object without invoking QFT or quarks.

---

### 6.3 Kernel Coupling Pattern

The composite soliton inherits and combines the kernel couplings of its constituents.

Example pattern:

- `g_p = (g_grav = 2, g_EM = +1, g_weak = small)`

Interpretation:

- Grav‑like coupling doubles (two cores)  
- EM‑like coupling sums to a net positive charge  
- Weak‑like coupling is small but nonzero  

This reproduces the role of a positively charged, massive, stable particle.

---

### 6.4 Stability Conditions

`S_p` is stable when:

1. Binding kernel (medium‑range) provides net attraction  
2. Internal texture pressure prevents collapse  
3. Variance `sigma_alpha^2` is low enough to avoid decoherence  
4. Density‑triggered RG drives the composite into a stable fixed point in halos  

In voids, high variance can destabilize the composite, giving environment‑dependent behaviour.

---

### 6.5 Interaction Table (Composite Included)

| Process                            | Allowed? | Mediating Kernel(s) | Notes                                      |
|------------------------------------|----------|----------------------|--------------------------------------------|
| `S_p + S_e -> S_p + S_e`           | Yes      | `K_EM`, `K_grav`     | Coulomb‑like + grav‑like                   |
| `S_p + S_gamma -> S_p + S_gamma`   | Yes      | `K_EM`               | Photon‑like scattering                     |
| `S_p + S_nu -> S_p + S_nu`         | Yes      | `K_weak`, `K_grav`   | Weak‑like + grav‑like                      |
| `S_p -> S_e + S_e + S_nu`          | Rare     | `K_weak`             | Requires high variance; unstable in voids  |
| `S_p + S_e -> S_p + S_e + S_gamma` | Yes      | `K_EM`               | Radiative excitation                       |
| `S_p + S_p -> bound state`         | Possible | `K_grav`, `K_EM`     | Larger composite (nucleus‑like)            |

This gives the beginnings of nuclear‑like structure without any QFT or GR.

---

### 6.6 Example: Formation of the Composite Soliton  
#### Process: `S_e + S_e -> S_p`

1. Two one‑core solitons approach.  
2. Their textures overlap and excite medium‑range kernel components.  
3. The continuum relaxes into a two‑core bound configuration.  
4. Excess energy is shed as one or more `S_gamma` excitations.  
5. The final state is a stable composite soliton `S_p`.  

This is the CCEF analogue of forming a proton‑like object.

---

## 7. Summary

The CCEF particle sector v0.2 provides:

- a minimal one‑core sector: `S_e`, `S_gamma`, `S_nu`  
- a two‑core composite: `S_p` (proton‑like)  
- masses from the continuum energy of `n(x,t)`  
- charges as kernel‑coupling patterns  
- interactions as soliton scattering and continuum excitations  
- quantum‑like behaviour from variance and density‑triggered RG  

All of this remains strictly within CCEF’s ontology:

- no QFT  
- no GR  
- no external structures  
- everything emerges from the continuum, solitons, kernels, and variance.
