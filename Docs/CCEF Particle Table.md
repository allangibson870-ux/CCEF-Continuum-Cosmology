# CCEF Particle Sector v1.1  
## Unified Mathematical Edition + Soliton RG Flow Extension  
### Topology‑Consistent, Ontology‑Pure, Q‑Core, Kernel‑Locked, Texture‑Excluded, and RG‑Driven Solitons

This section defines the complete mathematical structure of the CCEF particle sector, including:

- field equations  
- kernel operators  
- mass functionals  
- topological invariants  
- texture‑exclusion conditions  
- beta‑decay rules  
- hydrogen surface‑state equations  
- nuclear geometry  
- explicit soliton RG flow (new in v1.1)

All content remains strictly within CCEF ontology:

- fundamental object: `n(x,t)`  
- no GR geometry  
- no QFT operators  
- all “particles” are soliton attractors of the continuum  

---

## 1. Field and Kernel Foundations

### 1.1 Continuum Field

Fundamental field: `n(x,t)`  
Dynamics: `E[n] = ∫ d^3x · ℰ(n, ∇n, ∇²n, …)`

### 1.2 Kernel Operators

- Grav‑like: `K_grav(x − x', a)`  
- EM‑like: `K_EM(x − x', a)`  
- Weak‑like: `K_weak(x − x', a)`  

### 1.3 Kernel Response Functional

`Φ(x) = ∫ d^3x' · K(x − x', a) n(x')`  
`E_int = (1/2) ∫ d^3x · n(x) Φ(x)`

### 1.4 Variance Sector

Variance: `σ_α²(δ, a)`  
- small in halos  
- large in voids  

---

## 2. Soliton Definitions

### 2.1 Q‑Core Solitons (Baryons)

Topological charge:  
`Q = (1 / 4π) ∫ d^3x · εᵢⱼₖ (∂ᵢn · (∂ⱼn × ∂ₖn))`  
All baryons: `Q = 1`.

### 2.2 Kernel‑Locked Solitons (Leptons)

Leptons: `Q = 0`  
Stability: `δE[n] / δn = 0` under kernel locking.

---

## 3. Mass Functionals

`m = ∫ d^3x · ℰ_soliton(n)`  
Hierarchy: `m_Sn > m_Sp >> m_Se >> m_Sν`  
Binding: `m_bound = Σ m_i − E_binding`

---

## 4. Coupling Definitions

`g_EM = ∫ n Φ_EM`  
`g_weak = ∫ n Φ_weak`  
`g_grav = ∫ n Φ_grav`

---

## 5. Texture Exclusion Principle

Electron texture: `θ_e(x)`  
Gradient‑stress: `S_grad = ∫ |∇(θ_e(1) − θ_e(2))|²`  
Exclusion: `S_grad → ∞` ⇒ overlap forbidden.

---

## 6. Beta Decay (Topology‑Correct)

`S_n(Q=1) → S_p(Q=1) + S_e(Q=0) + S_ν(Q=0)`  
Core conservation: `1 → 1 + 0 + 0`  
Amplitude: `A ∝ ∫ θ_n K_weak θ_p`

---

## 7. Hydrogen as a Surface‑State System

Proton trough: `Φ_p = ∫ K_EM n_p`  
Electron equation: `δE[n_e]/δn_e + λ Φ_p = 0`  
Modes: `L_p ψ = λ ψ`

---

## 8. Nuclear Geometry (Q‑Core Merging)

Two `Q=1` → one `Q=2` soliton.  
Energy: `E_Q=2 < E_Q=1 + E_Q=1`  
Shape: `n_Q=2(x) = n₀(f(r,θ))`

---

## 9. Summary Table

| Species | Symbol | Q | EM | Weak | Exclusion | Mass |
|--------|--------|---|----|-------|-----------|-------|
| Proton | S_p | 1 | +1 | small | n/a | large |
| Neutron | S_n | 1 | 0 | moderate | n/a | > S_p |
| Electron | S_e | 0 | -1 | small | Yes | small |
| Neutrino | S_ν | 0 | 0 | moderate | No | tiny |
| Photon | S_γ | 0 | 0 | 0 | No | ≈0 |

---

## 10. Soliton RG Flow Extension (v1.1)

### 10.1 RG Coarse-Graining

`b = e^ℓ`, `ℓ = ln b`.

### 10.2 RG State Vector

`X(ℓ) = [K, ξ_R, A, B, S_i]ᵀ`  
`A = C_α α² ρ`  
`B = C_σ σ_α² ρ`

### 10.3 Kernel RG Flow

`dK/dℓ = β_K(K, ξ_R)`  
`K = A/(k²+m²) + B/(k²+Λ²)`  
`m = 1/ξ_R`, `Λ = 1/R_sol`

### 10.4 Correlation Length Flow

`dξ_R/dℓ = ξ_R [γ_K (∂ ln K / ∂ ln k)|_{k→0} − γ_σ σ_α²]`

### 10.5 Soliton RG Map

`dS_i/dℓ = F_i(K, ξ_R, σ_α²)`  
`dQ_i/dℓ = 0`

### 10.6 Soliton Classes

- Proton: `dS_Q=1/dℓ = 0`  
- Electron: `dE_e/dℓ = −η₁ ξ_R^{-1} + η₂ σ_α²`  
- Neutron: `S_n = S_Q=1 + S_Q=0 + δB`

### 10.7 Mass Flow

`m_i = ∫ E_i`  
`dm_i/dℓ = α_K K(k→0) − α_ξ ξ_R^{-1} + α_σ σ_α²`

---

# CCEF‑LITE v1.2  
## Stochastic Response System (Quantum Floor)

This section introduces irreducible fluctuations of the soliton gas into the transport equations.  
No Hilbert space, no GR, no external QFT.  
All stochasticity arises from internal variance `σ_α²(a)`.

---

## Quantum‑Corrected Coupling Perturbation

`β' + [Γ_α + D_α k²/a²] β = s(a) δ + P(k,a)`  
`P(k,a)` = Gaussian white noise from soliton discreteness.

Noise amplitude (Quantum Floor):

`ħ_eff(a) = σ_α²(a) ρ₀(a)`

As `ρ₀` dilutes, `ħ_eff` decreases slowly → relative noise increases → power spectrum never reaches zero.

---

## Stochastic Behaviour of δ(k,a)

- Large scales: classical growth dominates.  
- Intermediate scales: noise subdominant.  
- Small scales: diffusion kills classical structure; noise dominates; δ → finite floor.

Interpretation:

- Zero‑point analogue: residual δ at high k.  
- Decoherence: as `ξ_R` → IR fixed point, fluctuations suppressed.  
- No external quantum theory: all from `σ_α²`.

---

## Tightened ASCII Form (v1.2)

Stochastic beta equation:  
`β' + Γ_β β = S_δ δ + Ξ_β`  
`Γ_β = Γ_β0 + D_β k²/a²`

Noise:  
`<Ξ_β> = 0`  
`<Ξ_β Ξ_β'> = N_β δ_D(ln a - ln a') δ_D(k - k')`  
`N_β = C_β ħ_eff f_β(k)`  
`ħ_eff = σ_α² ρ₀`

δ‑equation:  
`δ'' + A δ' + B δ = C β`  
`P_δ = P_δ,cl + P_δ,noise`

High‑k limit:  
`K ≈ A/k²`, `G_eff ≈ A`  
`δ_cl → 0`, `δ_noise → const`

Noise floor:  
`P_δ,noise ∝ A² ρ₀³ σ_α² f_β(k) a/k`

This is the CCEF‑native irreducible fluctuation level.

