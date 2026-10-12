# How and where the grain world's left↔right symmetry breaks (2026-10-12)

**Code:** `ccef_parity_breaking.py` → `ccef_parity_breaking_output.txt`. Follows `CCEF_strong_cp.md`: diamond's bond-centred inversion (A ↔ B junctions) acts as parity on the grain fermions and forbids θ-type masses. But nature's weak force is left-handed only, so parity must break somewhere.

**Prior art:**
- left–right symmetric models (Pati–Salam; Mohapatra–Pati; Senjanović–Mohapatra);
- parity solutions of strong CP (Babu–Mohapatra; Barr–Chang–Senjanović);
- Weyl semimetals from inversion breaking (Murakami 2007);
- "breathing" pyrochlore lattices (condensed matter).

## 1. How: geometric "breathing" of the grain crystal [computed]
Make the two junction types slightly inequivalent (A ≠ B: a "breathing" crystal) and look at the grain Dirac fermion at X:

| Change | Scalar mass | θ-type mass | Low-energy fermion |
|---|---|---|---|
| none | 0 | 0 | one 4-fold Dirac point |
| **staggered junction energy ±V (breathing)** | **0** | **0** | **splits into 4 two-fold Weyl points**, separated in momentum ∝ V (0.010 at V = 0.02; 0.025 at V = 0.05) |
| spin–orbit strength λ_A ≠ λ_B | 0 | 0 | no change at X (to this order) |

**Reading:**
- **Breathing breaks parity (P) but preserves time reversal (T), so it preserves CP and cannot create the θ-type mass** (which is CP-odd).
- By CPT, T-symmetric P-breaking must break **C as well**. Breathing therefore breaks **P and C but conserves CP: exactly the pattern of nature's weak interaction**, which violates P and C maximally but CP only slightly, and has θ̄ ≈ 0.
- Its effect on the grain fermions is to **pull each Dirac particle's left- and right-handed halves apart in momentum**: a first step toward a chiral low-energy world.
  - Making the emergent SU(2) gauge field couple to only one handedness still needs the mirror partners gapped (symmetric mass generation). **[OPEN]**
- **Where the P-breaking choice comes from [CONJECT]:**
  - breathing is a property of the *crystal*;
  - it can be fixed by the **single seed** and never melts (the crystal survives its own reheating, `CCEF_reheat.md`);
  - so there is **one domain everywhere and no domain walls**, the one-seed picture again doing inflation's job.

**The remaining strong-CP subtlety:**
- Once P is broken geometrically, parity no longer protects arg det M. θ̄ can re-enter at order **(breathing) × (CP phase)** wherever both act on the same fermion masses.
- Keeping θ̄ < 10⁻¹⁰ while the CKM phase is O(1) needs the CP phases to sit in couplings that the breathing does not touch, e.g. the heavy right-handed or mirror sector. **[OPEN; computing this needs the chiral sector]**

## 2. Where: the left–right breaking scale v_R
If the breaking is left–right-model-like (a right-handed sector made heavy at v_R):

| v_R (GeV) | seesaw y²/f for m_ν = 0.05 eV | wall bias ε ≥ (v_R/M_P)² | θ̄ < 10⁻¹⁰ if loop factor κ ≤ | B−L→ℤ₂ string Gμ |
|---|---|---|---|---|
| 10⁴ (LHC-scale) | 2×10⁻¹¹ (tiny) | 7×10⁻³¹ | 10²⁰ | 7×10⁻³¹ |
| 10¹² | 2×10⁻³ | 7×10⁻¹⁵ | 10⁴ | 7×10⁻¹⁵ |
| **10¹³** | **0.02** | 7×10⁻¹³ | 10² | **7×10⁻¹³** |
| **10¹⁴** | **0.2** | 7×10⁻¹¹ | 1 | **7×10⁻¹¹** |
| 10¹⁵ (= Λ*) | 1.7 | 7×10⁻⁹ | 0.01 | 7×10⁻⁹ ❌ (pulsar timing) |

**A natural window: v_R ≈ 10¹³–10¹⁴ GeV**, just below the crossover Λ* ≈ 10¹⁵:
- seesaw couplings are ordinary (0.02–0.2);
- leptogenesis still works (M_N ~ 10¹³–10¹⁴);
- domain walls are removable, with θ̄ ~ 10⁻¹²–10⁻¹⁰;
- if B−L breaks to a ℤ₂, **cosmic strings form with Gμ ~ 10⁻¹²–10⁻¹⁰**: below the current pulsar-timing limit at the low end, near it at the top, and **within LISA's reach**.

## Verdict
- **How (best-supported picture):** the left↔right symmetry is broken by a **breathing of the grain crystal**, the two junction types becoming slightly different.
  - Computed: this breaks P and C but conserves CP and T, generates **no θ-type mass**, and pulls each fermion's left- and right-handed halves apart.
  - That is qualitatively the weak force's own symmetry pattern.
  - If the breathing is set by the single seed, it is the same everywhere: no domain walls.
- **Where:** if it proceeds through a heavy right-handed sector, the natural scale is **v_R ≈ 10¹³–10¹⁴ GeV**.
- **Predictions:**
  - possible **cosmic-string gravitational waves** (Gμ ~ 10⁻¹²–10⁻¹⁰; LISA, future pulsar timing);
  - **a neutron EDM** ~10⁻²⁸–10⁻²⁶ e·cm;
  - no right-handed W within LHC reach.
- **Open:**
  1. making the emergent weak force couple to only one handedness (gapping the mirror partners);
  2. keeping θ̄ < 10⁻¹⁰ once P is broken, by placing the CP phases away from the breathing;
  3. what sets the breathing amplitude.
