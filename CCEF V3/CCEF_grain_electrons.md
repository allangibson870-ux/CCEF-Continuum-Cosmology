# Light charged matter (electrons) from grains: the fermion-string construction (2026-10-11)

Builds on `CCEF_grain_Hamiltonian.md`.

**Code and outputs** (`_output.txt` files alongside):

| Script | What it does |
|---|---|
| `ccef_grain_fermions.py` | exact Pauli algebra; its Part 2 band check is superseded |
| `ccef_grain_fermion_bands.py` | twisted-boundary band check (too coarse, superseded) |
| `ccef_grain_fermion_nodes.py` | exact Bloch node search |
| `ccef_grain_fermion_fluxsearch.py` | all 512 flux patterns, 4 cores |
| `ccef_grain_fkm.py` | spin-½ version |
| `ccef_grain_lattice.py` | shared helpers |

## Step 1: making string ends into fermions [exact, verified]
In the grain Hamiltonian, a charge sits at a junction where the Gauss law is violated, and it moves by flipping the grain to the next junction.
- **Plain flip (X_i):** the Levin–Wen T-junction test gives θ = 0 at **all 864** junction-triples. These string ends are **bosons**, as in quantum spin ice.
- **Dressed flip** (X_i × Z on the grains that come earlier in a fixed local order at both junctions): θ = π at **all 864** triples, so the ends are **fermions**.
- **Consistency checks** on the 216-junction torus, all passing:
  - hops anticommute exactly when two grains share a junction;
  - hops create no stray flux;
  - the dressed ring terms all commute;
  - Gauss parity flips only at a hop's two ends.
- **What this means:** in the sector where every ring term = +1, the 432 grain qubits are **exactly** 216 fermions on the junctions coupled to a gauge field. Gauss parity = fermion parity = (−1)^Q, so **odd-charge string ends are fermions**. That is the electron's charge–statistics link.
- This algebra is the Bravyi–Kitaev "superfast" fermion encoding, realised by the grains themselves.

## Step 2: are they light, and relativistic?

### Spinless fermions: no [computed + known theorem]
- Nearest-neighbour hopping on the 3-D grain graph, with 0 or π flux per ring, gives **nodal lines**: gapless (light) but not relativistic.
- An exhaustive search of **all 512 0/π flux patterns** of the 8-junction cell gave **lines in every case**.
- This reproduces the codimension theorem: spinless, time-reversal-symmetric fermions in 3-D generically have nodal lines, not points.
- **Lesson: relativistic electrons must carry spin-½.**

### Spin-½ fermions (two grains per relation → two modes per junction) [computed]
Add the spin–orbit hop through the shared neighbour, H_SO = i(8λ/a²) Σ c† s·(d₁×d₂) c (the Fu–Kane–Mele form):

| Result | Value |
|---|---|
| λ = 0 | nodal lines (150 distinct zeros found) |
| **λ ≠ 0** | **exactly 3 isolated Dirac points, at the three X points (one per spatial axis), each 4-fold degenerate**: three massless 4-component Dirac fermions (electron + positron) |
| Cone shape at X | v_∥ = t·a, v_⊥ = 4λ·a: **isotropic (Lorentz-like) exactly at λ/t = 1/4** |
| Masses from unequal junction bonds t_i = t(1+ε_i) | m_x = t\|ε₁+ε₂−ε₃−ε₄\|, m_y = t\|ε₁−ε₂+ε₃−ε₄\|, m_z = t\|ε₁−ε₂−ε₃+ε₄\| (numerics match to 5 digits) |

**Reading the results:**
1. **Light electrons for a structural reason.** A fermion is exactly massless while the junction stays perfectly tetrahedral (all four grain-bonds equal). Its mass measures the junction's distortion. A light electron (m_e ≪ Λ*) means junctions are nearly perfect: |ε| ~ m_e/Λ* ~ 10⁻¹⁴. That is "technically natural": no symmetry-breaking, no mass.
2. **Three species, one per spatial axis [CONJECT].**
   - The diamond grain graph gives exactly three Dirac fermions, one at each X point. That is a consequence of space having three axes.
   - Their masses are the three independent "Klein-four" combinations of the four bond distortions. So **any mass hierarchy is possible**, including e : μ : τ = 1 : 207 : 3477. It isn't predicted; it fits with three numbers.
   - It is tempting to read the three X-valleys as the **three generations**. This is an old lattice idea ("tastes = generations"), now arising naturally. Combined with the earlier ℤ₃-anomaly result (exactly 3 generations needed in Branch L₃), there are **two independent "threes"**. Flag only; not derived.
3. **Lorentz symmetry needs one tuning.** The electron cone is round only at λ = t/4, and its speed v_e = t·a must also equal the photon's c ~ J_ring·a. Literature (from memory) suggests Coulomb interactions drive speeds and anisotropies toward a common value, but only logarithmically. That is V5's Mechanism A problem again. **[OPEN]**

## What's still missing
| Issue | Status |
|---|---|
| Electron charge couples to the emergent photon | ✅ in structure (dressed σ^± hops carry the U(1) charge); not yet simulated dynamically |
| Spin-½ | ✅ needed and provided (two grains per relation); spin transforms correctly via the spin–orbit term |
| Relativistic, massless-until-distorted electrons | ✅ (3 Dirac points) |
| Isotropy and a common speed with light | ⚠️ needs λ = t/4 and t ≈ J_ring [OPEN] |
| Chirality (weak force acts on left-handed only) | ❌ these are vector-like Dirac fermions (fine for QED, not for the full Standard Model). Route: gap the mirror partners by symmetric mass generation, which requires 16 Weyl fermions per generation, i.e. the right-handed neutrino. Branch L₃ already has it (Dirac neutrinos). |
| Generation mixing (CKM/PMNS) | ❌ the X-valleys sit at different momenta; mixing needs valley-mixing terms [OPEN] |
| Masses tied to the Higgs | ❌ here mass = junction distortion; the Standard Model needs distortion ∝ Higgs field [OPEN] |

## Bottom line
- The grains can make electrons. Decorating the grain flips makes string ends **fermions**, an exact construction verified at every junction.
- Giving each relation two grains (spin) plus a spin–orbit hop makes them **relativistic Dirac particles**, massless until the junction distorts. That explains why charged matter can be far lighter than the grain scale.
- The 3-D grain geometry gives **exactly three** such particles, one per spatial axis, with masses from three independent bond distortions: a natural home for three generations (conjecture).
- Open: making them chiral (Standard Model), tying their mass to the Higgs, and locking their speed to light's.
