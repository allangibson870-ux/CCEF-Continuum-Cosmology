# How hot does crystallisation make the universe? (2026-10-12)

**Code:** `ccef_reheat.py` → `ccef_reheat_output.txt` (order-of-magnitude estimate).

## Correction first (unit consistency)
- In quantum spin ice the emergent light speed is c ~ J_ring·a/ħ.
- With the grains spaced at the gravity length a = ℓ, the ring-exchange scale must be J_ring ~ ħc/ℓ = **M** (the grain/Planck scale), **not** the crossover Λ*.
- The earlier identification "Λ* ↔ J_ring, so Λ*/M comes from (J_±/J_zz)³ ≈ (7×10⁻⁴)³" is therefore **inconsistent and retracted**. In the corrected mapping, J_zz ≫ J_ring ~ M simply means bare Gauss-law charges are super-Planckian.
- **The M/Λ* hierarchy is again unexplained.** Corrected in `CCEF_grain_Hamiltonian.md` and the GitHub paper.

## Estimate
- **Latent heat (our simulations, angle rule on):** ΔE = 3.6 K per junction (relaxed glass −8.4 → crystal −12) to 11.9 K (random tangle −0.1 → −12).
- **Junction density:** diamond with bond length ℓ gives n_J = 0.65/ℓ³.
- **Energy scale:** K = κM; unit consistency makes κ ~ 1 natural.
- **Temperature:** if the heat thermalises into radiation with g* degrees of freedom, ρ = n_J·ΔE·K = (π²/30) g* T_RH⁴.

| κ = K/M | g* | T_RH (GeV) | T_RH / Λ* | T_RH / K (space re-melts if ≳ 2.7) |
|---|---|---|---|---|
| **1 (natural)** | 107 | **0.9–1.2 ×10¹⁹** | ~10⁸ | 0.5–0.7 ✅ |
| 1 | 1000 | 5–7 ×10¹⁸ | ~10⁸ | 0.3–0.4 ✅ |
| 0.1 | 107 | 5–7 ×10¹⁸ | ~7×10⁷ | 2.9–3.9 ⚠️ borderline |
| 4×10⁻⁹ (the retracted mapping) | 107 | ~10¹⁷ | ~10⁶ | ~10⁶ ❌ re-melts |
| 10⁻³² | 107 | ~10¹¹ | ~1 | ~10²³ ❌ |

**Results:**
- **Crystallisation reheats the universe to about the Planck scale: T_RH ≈ 5×10¹⁸ – 3×10¹⁹ GeV (10³¹–10³² K).**
- **Self-consistency demands it.** If the geometry coupling were weaker than κ ≈ 0.1–0.16, the released heat would exceed diamond's stability range (~2.7 K in our runs) and **re-melt space**. Space can only stay crystallised if it is bound at nearly the Planck scale.
- Keeping T_RH below the matter switch-on Λ* would need κ < 2×10⁻³³ (K < 3×10⁻¹⁴ GeV per junction): not credible.

## Consequences
| Topic | Consequence |
|---|---|
| **Timeline** | tangle → seed → crystal (Janus point) → **hot universe at ~10¹⁹ GeV** → cools through Λ* ≈ 10¹¹ GeV (matter switches on) → standard hot Big Bang. A "hot Big Bang without inflation" that starts at about the Planck temperature |
| **Janus-state CP route** (`CCEF_janus_cpt.md` case b) | ❌ **Erased.** A thermal grain state at ~M is CP-symmetric, so any CP-odd phase from the Janus point is scrambled long before matter appears. The matter excess must come from **CP violation in the laws** (case c). The Janus mirror picture (antimatter on the other side; global balance) survives |
| **Right-handed neutrinos** | thermalised by the grain-scale plasma, then decoupled above Λ*: **ΔN_eff = 0.14** (g* = 106.75 at decoupling; smaller if more grain-level species) |
| **Gravitons** | if thermalised at ~M and decoupled: ΔN_eff ≈ 0.05 |
| **Total extra radiation** | **ΔN_eff ≈ 0.19** (if both thermalise with SM-like g*): **testable by Simons Observatory / CMB-S4** (σ ≈ 0.03–0.05). Sharpens the earlier {0, 0.06, 0.14} |
| **Monopoles** | depends on where the emergent U(1)_Y lives. On the grain lattice (spacing ℓ), monopoles are ~35 M; with T_RH ≈ 0.3–0.7 M, m/T ≈ 50–120 > 37 ✅ safe. If hypercharge only emerges at Λ*, monopoles are made while cooling through Λ*; that needs the switch-on temperature ≲ 0.95 Λ* (borderline, as before) |
| **Axion** | thermal at T ≫ f_a: post-inflation scenario ✅ (unchanged) |

## Caveats
- The latent heat comes from a classical toy geometry energy. The temperature assumes complete thermalisation into radiation, and the g* of grain-level modes above Λ* is unknown.
- Expansion during crystallisation, and where the heat actually goes (grain modes vs light), are not modelled.
- The answer is insensitive to most of this: T ∝ (ΔE·κ/g*)^{1/4}.

## Bottom line
**The universe starts at roughly the Planck temperature.** That isn't a choice: space can only stay crystallised if its binding energy is near the grain scale, and releasing that energy heats everything to ~10¹⁹ GeV.

This kills the "CP in the Janus state" route, because the heat scrambles it. The Janus mirror picture survives, but the matter excess then needs CP violation in the laws.

It also gives a new, testable prediction: **extra radiation ΔN_eff ≈ 0.14–0.19** from thermalised right-handed neutrinos (and gravitons), within reach of next-generation CMB experiments.
