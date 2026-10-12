# The strong-CP problem in the grain universe (2026-10-12)

**Code:** `ccef_strong_cp.py` → `ccef_strong_cp_output.txt`.

**Why it matters:** the CCEF hybrid (`CCEF_hybrid.md`) has no room for an axion at the crossover scale.

**The problem:**
- θ̄ = θ_QCD + arg det(M_u M_d) must be below ~10⁻¹⁰ (neutron electric dipole moment, EDM);
- yet quarks show CP violation (the CKM phase ≈ 1.2 rad), which needs complex couplings that would normally make θ̄ large.

**Known solutions (prior art):**
- the axion (Peccei–Quinn);
- a massless up quark (excluded by lattice QCD);
- spontaneous CP violation (Nelson 1984; Barr 1984);
- **the parity solution** (Babu & Mohapatra 1990; Barr, Chang & Senjanović 1991).

## 1. The Janus/CPT structure cannot fix θ
The θ-term is C-even, P-odd and T-odd, so it is CP-odd but **CPT-even**. A CPT-symmetric (Janus) universe places no constraint on it. *(This corrects a hope raised in conversation.)*

## 2. The grains contain a parity symmetry that forbids θ-type masses [computed]
- Diamond has an exact **bond-centred inversion** that swaps the two junction types (A ↔ B).
- In the spin-½ grain fermions (`CCEF_grain_electrons.md`), each X point carries a 4-component Dirac fermion. Exactly **two** mass types are possible, found numerically as the Hermitian matrices anticommuting with all three velocity matrices:
  - a scalar mass;
  - a pseudoscalar ("iγ⁵") mass. Its phase relative to the scalar is the fermion's contribution to θ̄.
- **Test** (400 random perturbations of the grain hopping each, including complex, CP-violating hoppings):

| Perturbations | rms scalar mass | rms pseudoscalar (θ-type) mass |
|---|---|---|
| **respecting diamond's inversion** | 3.5×10⁻² | **4×10⁻¹⁸ (exactly zero)** |
| breaking it | 1.8×10⁻² | 1.7×10⁻² (O(1) chiral phase) |

- **While the grain lattice's inversion symmetry holds, the θ-type quark mass phase is forbidden, even when the couplings carry CP violation.**
- Inversion acts on the grain fermions as **parity** (A/B sublattices ↔ left/right). The bond-anisotropy masses found earlier are the allowed scalar type.
- Together with θ_QCD = 0 (θ is P-odd, so it vanishes in a parity-symmetric gauge sector), this is the **parity solution of strong CP, arising from the geometry of the grain crystal**.

## 3. The catch: parity must be broken somewhere
The weak force is chiral (left-handed only), so parity cannot be exact at low energy. In parity solutions, θ̄ is then generated only **radiatively**, from wherever P is broken, and can be ~10⁻¹¹–10⁻¹⁰.

**Domain walls.** If P is broken *spontaneously* at scale v after the Planck-hot start, domain walls form. Removing them needs a small explicit bias ε ≳ (v/M_P)², which feeds θ̄ ~ κε (κ = loop factor):

| v (GeV) | ε needed | θ̄ < 10⁻¹⁰ requires κ ≲ |
|---|---|---|
| 10¹² | 7×10⁻¹⁵ | 10⁴ ✅ |
| 10¹⁴ | 7×10⁻¹¹ | 1 ✅ |
| 10¹⁵ (≈ Λ*) | 7×10⁻⁹ | 0.01 ⚠️ |
| 10¹⁶ | 7×10⁻⁷ | 10⁻⁴ ❌ |

**Alternative [CONJECT]:** if the choice of which handedness is gapped (the mirror-gapping that makes the Standard Model chiral) is **inherited from the single crystal seed**, which survives the reheating, there is only one domain and **no walls at all**. The one-seed picture would then again supply what inflation normally does.

> **Follow-up (`CCEF_parity_breaking.md`):**
> - A geometric "breathing" of the crystal (A ≠ B junctions) breaks P and C but conserves CP. It creates no θ-type mass and splits each Dirac fermion into separated Weyl halves.
> - The natural left–right scale is ~10¹³–10¹⁴ GeV.
> - **Open:** keeping θ̄ < 10⁻¹⁰ once both breathing and CP phases act on the same masses.

## 4. Predictions if this is the solution
- **No strong-CP axion.** In the hybrid, dark matter is asymmetric anyway, so haloscopes would see nothing.
- **A neutron EDM not far below the current limit:** with θ̄ generated radiatively at ~10⁻¹¹–10⁻¹⁰, d_n ≈ 2×10⁻²⁷ – 2×10⁻²⁶ e·cm (current limit 1.8×10⁻²⁶; next-generation n2EDM-class goal ~10⁻²⁷). **Likely testable.**
- The size of θ̄ is model-dependent: it depends on how parity is broken in the chiral sector, which is not built yet.

## Verdict
- **Partial success.** The grain crystal's own inversion symmetry acts as parity on the emergent fermions. That **exactly forbids the θ-type quark mass phase even with CP-violating couplings** (computed), and with θ_QCD = 0 it gives the known "parity solution" of strong CP **without an axion**.
- This connects three earlier threads: the electrons' A/B sublattices, the chiral-fermion (mirror-gapping) problem, and the single-seed geometry.
- **Open:**
  - how parity is broken to give the chiral weak force without feeding θ̄ above 10⁻¹⁰;
  - avoiding domain walls (scale ≲ 10¹⁴ GeV, or inheritance from the single seed).
- **Prediction:** a neutron EDM within reach of the next generation of experiments, and no axion.
