# The grain Hamiltonian, version 1 (2026-10-11)

**Code:**
- `ccef_grain_hamiltonian_mc.py`: geometry-sector Monte Carlo, 4 cores; output in `ccef_grain_hamiltonian_mc_output.txt` and `.json`;
- `ccef_gh_batch2.py`: slower anneals and robustness checks; output in `ccef_gh_batch2_output.txt` and `.json`.

## 1. The objects (P7: one grain type, "made of nothing")
- A **grain** is a qubit, and it is also a **relation**: it joins two **junctions**.
- A junction is simply where 4 grains meet. It is not a separate object.
- So the whole configuration is a bipartite 4-regular graph Γ whose *edges* are grains, plus the grains' qubit states.
- The two ends of each grain (A and B) give it a direction ("in/out"), which is what lets a Gauss law exist.

## 2. The Hamiltonian
**Ĥ = Ĥ_Γ + Ĥ_move + Ĥ_ice + Ĥ_ex**

| Term | Formula | What it does | Scale |
|---|---|---|---|
| **Ĥ_Γ** (geometry) | Σ_v [ U·sq(v) − K·hex(v) + W·θ(v) ] | U: no "squares" (two grains sharing both junctions' neighbours: crowding). K: rewards 6-rings (the plaquettes light lives on). W: no over-connection (3+ independent short routes between two junctions) | grain scale ~M |
| **Ĥ_move** | −Γ Σ ( \|Γ′⟩⟨Γ\| ), where two grains swap one junction each | quantum rewiring: geometry fluctuates. At high energy, Γ is a random graph where everything is a few steps from everything (the non-local pre-geometric phase) | ~M |
| **Ĥ_ice** | (J_zz/2) Σ_v Q_v², with Q_v = Σ_{i∈v} ±σᶻ_i | **Gauss law**: 2-in-2-out at every junction. σᶻ is the emergent electric field | J_zz ~ M |
| **Ĥ_ex** | −J_± Σ_v Σ_{i<j∈v} (σ⁺_i σ⁻_j + h.c.) | grain exchange. At third order it becomes ring exchange around 6-rings, J_ring = 12 J_±³/J_zz² (Hermele–Fisher–Balents 2004) | J_ring ≡ Λ* |

On the diamond relational graph, Ĥ_ice + Ĥ_ex is exactly **quantum spin ice**. The grains sit where the spins of the pyrochlore lattice do. This is the best-established qubit model whose low-energy physics is **emergent electromagnetism**: a photon, electric charges and magnetic monopoles.

## 3. Results

### 3a. Does Ĥ_Γ make 3-D space? (computed; 216 junctions, 432 grains, 8 anneals on 4 cores)
| Run | K, U, W | Energy/junction | 6-rings | Result |
|---|---|---|---|---|
| reference: random relations | — | −0.04 | 3.6 | "everything near everything" (shells 4, 12, 31, 62: exponential growth) |
| **reference: 3-D diamond** | 1, 8, 4 | **−12.00** | 12 | shells 4, 12, 24, 42, 64 |
| R1: rings only | 1, 8, 0 | −39.6 | 39.6 | **crumples** into dense knots (shells collapse after r = 3; d_s ≈ 1.9) |
| B3: weak anti-crowding | 1, 8, 2.5 | −13.3 | 15.4 | beats diamond with a crumpled non-3-D structure |
| R2, R3, B1, B2 | 1, 8, 4 | −10.9 to −11.5 | 11.3–12.3 | **locally diamond**: shells 4, 12, 24 exactly, no squares, θ ≈ 0.1; 16–22% perfect junctions; glassy beyond r = 3 |
| B4: strong anti-crowding | 1, 8, 8 | −10.1 | 10.2 | most 3-D-like at large r (shells 26, 38, 40), 13% perfect |
| R4: diamond heated | 1, 8, 4 | −12.0 at every T up to 2.7 | 12 | never melts (huge hysteresis) |

**What this shows:**
1. **Light alone crumples space.** Rewarding only the rings that light lives on (which ring exchange itself would generate) collapses space into tiny dense knots. That is the well-known "crumpled phase" problem of emergent-geometry models, reproduced here.
2. **Light plus a no-crowding rule makes 3-D.**
   - For W ≥ 4, nothing the anneals found beats the 3-D diamond.
   - Every run from random relations self-assembles to the **exact diamond structure out to 3 steps**.
   - The ground state for W ≥ 4 is very probably 3-D diamond space (not proven).
   - The "no over-connection" rule has a direct meaning: **two points of space can't be joined by too many independent short routes.** That is the property that makes space extended rather than knotted.
3. **Geometrogenesis is glassy and strongly first-order** in this classical limit. Cooling freezes into a defected, locally-diamond polycrystal, while a perfect diamond survives heating far past the cooling transition. So space forms with frozen-in grain-scale defects. Whether quantum rewiring (Ĥ_move) anneals them away is untested.

### 3b. Light (literature + scale matching)
- On the 3-D relational graph, Ĥ_ice + Ĥ_ex is quantum spin ice. The established results (from memory; check before citing):
  - a **deconfined U(1) Coulomb phase** with a gapless **photon** (linear dispersion, speed ~ J_ring·a/ħ);
  - gapped electric charges (energy ~J_zz, i.e. grain scale) and gapped magnetic monopoles;
  - a stable phase for J_±/J_zz ≲ 0.05;
  - entry into the Coulomb liquid by **thermal crossover**, as quantum Monte Carlo reports.
- **The monopole condition is met.** Light "switches on gently", which is the condition `CCEF_monopole_problem.md` needed.
- ~~**The hierarchy:** with M ↔ J_zz and Λ* ↔ J_ring, Λ*/M = 4.4×10⁻⁹ requires J_±/J_zz ≈ 7×10⁻⁴.~~ **[RETRACTED 2026-10-12, `CCEF_reheat.md`]**
  - The emergent light speed is c ~ J_ring·a, so with grain spacing a = ℓ the ring scale must be J_ring ~ ħc/ℓ = M, not Λ*.
  - The cubed ratio only makes the bare Gauss-law charges super-Planckian (J_zz ≫ M).
  - The M/Λ* hierarchy is unexplained.
- **Consistency:** square-ring exchange would appear at second order (≈ 10⁻⁶ M ≈ 2×10¹³ GeV) and would favour crumpling. The no-crowding penalty U must exceed that, and U ~ M does.

## 4. Scorecard
| Requirement | Status |
|---|---|
| One grain type, grains as relations (P7) | ✅ built in |
| Gauss law, emergent electric field | ✅ exact (Ĥ_ice) |
| Emergent photon (U(1)) | ✅ known physics of quantum spin ice on this graph |
| 3-D space from random relations | ✅ **locally**: needs the no-crowding/no-over-connection terms. ⚠️ glassy (defected polycrystal), ground state not proven |
| Gentle switch-on of light (monopoles) | ✅ crossover in quantum spin ice |
| Λ*/M hierarchy | ❌ unexplained (the "cubed ratio" claim was retracted: J_ring ~ M by unit consistency) |
| Fine-structure constant | ❌ quantum spin ice's emergent α ≈ 0.08 (literature, from memory); hypercharge needs α_Y(Λ*) ≈ 0.013 [OPEN] |
| SU(2) × SU(3) | ✅ built via rishon quantum links on grain-made fermions (`CCEF_nonabelian.md`; exact small-system checks). Needs ~20–50 grains per relation for the real couplings; large-scale dynamics not simulated |
| Light charged fermions (electrons, quarks) | ❌ spin-ice charges are heavy bosons. Route: Levin–Wen 2003 lattice-spin models with emergent fermions as string ends |
| A single speed of light for all species | ⚠️ one photon speed; matter needs V5 Mechanism A |
| Lorentz symmetry vs a crystal lattice | ⚠️ a perfect diamond is a preferred frame. The glassy/defected outcome may actually help ("random grains") [OPEN] |
| Gravity (Jacobson area law) | ⚠️ a local Ĥ gives area-law entanglement (compatible). **Graviton** (`CCEF_graviton.md`): background independence forces the linearised Einstein energy and exactly 2 helicity-2 waves; the extra scalar needs a *local* time constraint at every junction (not yet in Ĥ) |

## Bottom line
- This version builds, from **one type of qubit-relation**, a Hamiltonian whose low-energy world is 3-D space with light in it.
- It meets the "gentle switch-on" condition the monopole analysis needed. *(An earlier claim that it also explains the 10⁹ gap between grain and crossover scales was retracted on unit-consistency grounds; see `CCEF_reheat.md`.)*
- The numerics show **3-D is not automatic**: a pure light term crumples space. The extra ingredient is a rule against crowding and over-connection.
- Still missing: the weak and strong forces, light charged matter, the right value of α, and gravity's graviton.
