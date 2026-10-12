# Audit of the frozen predictions after the computed N_eff (2026-10-12)

**Code:** `ccef_prediction_audit.py` → `ccef_prediction_audit_output.txt` (seconds).

**Why:**
- Every frozen prediction was made with the assumed N_eff = 9: grain length ℓ = 0.69 ℓ_P, grain scale M = 1.77×10¹⁹ GeV.
- The lattice computation (`CCEF_neff.md`) gives **N_eff ≈ 495** for the content CCEF builds (278 without mirror partners). That means **ℓ = 5.1 ℓ_P and M = 2.4×10¹⁸ GeV**.
- This audit checks, for each frozen prediction, whether it depends on ℓ, M or N_eff, and recomputes the dependent numbers with the *same formulas as the frozen code*.

**Rules followed:**
- No frozen file was edited. Frozen records stand as historical statements; this audit only reports how they are affected.
- *Naming note:* the gravity species count N_eff (≈ 495) is unrelated to the cosmological ΔN_eff (extra relativistic species, ≈ 0.14). Future documents should call the former N_sp.

## 0. Integrity of the freeze records
All seven freeze records were re-hashed: **every frozen file matches its recorded SHA-256**. The numass-fit record was checked against its post-void re-freeze. Nothing frozen has changed since freezing.

## 1. Summary
| Frozen prediction (freeze time, UTC 2026-10-11) | Depends on ℓ / M / N_eff? | Audit result |
|---|---|---|
| No phantom crossing; recruitment w(z) locus (12:09) | no | **unchanged** |
| fσ8 1.5–4% below ΛCDM | no | **unchanged** |
| Spacetime jitter / interferometer noise (12:36) | Channel A uses ℓ; Channel B (the GQuEST row) uses ℓ_P | **unchanged.** Channel A grows ×4–5 but stays far below any test |
| Proton-decay rows (12:50) | the Mechanism-A and grain-scale rows use M | **verdicts unchanged.** Excluded rows stay excluded; the grain-scale row stays unobservable (τ ~ 10⁴⁵ yr) |
| Branch L₃ Dirac package (13:19): no 0νββ, normal ordering, Σm_ν = 72 meV, m_β = 12.5 meV | no (anarchy plus measured splittings) | **unchanged** |
| ΔN_eff = 0.14 from ν^c (13:19) | needs only T_RH ≫ Λ* (ratio fixed) | **unchanged** |
| Neutrino-mass fit decision rule (13:32) | no | **unchanged** |
| S8 (17:04) | no | **unchanged** |
| **Axion dark matter, m_a = 74 μeV (14–400) (17:14)** | **yes:** f_a = Λ* = M·y^(2/3) ∝ M | **AFFECTED (major)** |
| **Finite volume ~(1–1.5 D_LSS)³** (paper table; from the L_max bound) | **yes:** L_max ∝ N_eff^(−2/3) | **AFFECTED (fails)** |
| ΔN_eff "up to 0.19 with thermal gravitons" (paper table, added 2026-10-12) | yes: T_RH ∝ M | **AFFECTED (minor):** the graviton increment becomes doubtful |
| Planck-mass remnants (secondary, not predictive) | yes: mass ~ M | 32 → **4 μg** |
| Branch M package (not formally registered) | ripple fit and Lorentz bound use M, η | see §4 |
| Hybrid asymmetric dark matter 2.5–10 GeV (not formally registered) | no | **unchanged** |

## 2. The axion moves up by ×7.4 [major]
In Branch L₃, the crossover scale comes from diluting the Dirac-neutrino Yukawa over the grains: Λ* = M·y^(2/3), proportional to M. The axion has f_a = Λ*.

| | Λ* (GeV) | m_a | frequency | misalignment Ωh² |
|---|---|---|---|---|
| frozen (N_eff = 9) | 7.7×10¹⁰ | **74 μeV** (14–400) | 18 GHz (3–96) | 0.039 (strings ×3) |
| no mirrors (278) | 1.4×10¹⁰ | 411 μeV (76–2,200) | 99 GHz | 0.005 (×23) |
| **full content (495)** | **1.0×10¹⁰** | **≈ 550 μeV** (100–3,000) | **≈ 130 GHz** (25–710) | 0.004 (strings ×32) |

**What changes:**
- The central value moves **outside the frozen band**.
- It lands in the high-mass window favoured by some post-inflation string simulations (≳ 500 μeV, Gorghetto et al.; quoted in the frozen code). There the strings, not misalignment, must supply ~97% of the dark matter. So it remains a viable dark-matter axion.
- The experiments shift: MADMAX/ALPHA cover the low end. The new centre (~130 GHz) is for broadband high-frequency searches (BREAD-type) and future dish/dielectric concepts.

**What does not change:** the post-inflation scenario, domain-wall number 1, miniclusters, and "no WIMPs".

## 3. The finite universe fails [major]
- The frozen finite-volume prediction comes from the everpresent-Λ magnitude ρ_Λ ~ β/(ℓ²√V₄). Requiring the past 4-volume to fit inside the cycle gives L_max = A·β^(2/3)·D_LSS, with A = 2.15 at N_eff = 9.
- A scales as N_eff^(−2/3), since ℓ² grows with N_eff.

| N_eff | median L_max | P(L_max ≥ 1 D_LSS) |
|---|---|---|
| 9 (frozen) | 1.04 D_LSS | 0.53 |
| 278 | 0.11 D_LSS | 10⁻⁸⁵ |
| **495** | **0.07 D_LSS** | **10⁻²⁶⁶** |

**With the computed N_eff, the same reasoning forces a universe ~0.07 of the CMB diameter across.** Existing CMB topology searches (including our own null result) exclude that.

Equivalently: for a universe of observed size, the grain-count dark-energy magnitude comes out **~55× too small**.

**The frozen "finite volume ~1–1.5 D_LSS" prediction is not consistent with the computed N_eff. It is moved to the negative results.**

Possible ways out, none yet derived:
1. The counting unit for Λ is the Planck 4-volume rather than the grain 4-volume (Sorkin's original form), which restores the magnitude. But it needs a reason why Λ counts something finer than grains.
2. The fluctuation amplitude grows with the number of species, e.g. σ(ρ_Λ) ∝ √N_sp.
3. N_eff is much smaller than computed (e.g. if Jacobson's η must exclude the UV-dominated lattice part). That contradicts the area-law result as it stands.

> **Follow-up (`CCEF_rishon_splitting.md`, post-hoc):** if relations are bundles of n ≈ 25–37 sub-grains and the Λ 4-volume counts their elementary update events, the finite universe is restored at ~1–3.5 D_LSS for J±/J_zz ≲ 0.1. The ν^c dilution over sub-grains returns the axion to ~150–170 μeV. Both are conjectural.

## 4. Branch M (not formally registered)
- **Λ* is fixed by neutrino masses** (v²/m₃ ≈ 6×10¹⁴ GeV), independent of M. Proton decay, the Majorana anarchy predictions, m_ββ ≈ 18 meV and leptogenesis are **unchanged**.
- **Ripple amplitude.** The area-law heat-capacity coefficient needed rises from c = 0.18 to c = 10.
  - If that coefficient counts species the way the entanglement does (c ∝ N_eff, natural since every field adds heat capacity), then **c/N_eff = 0.020 in both cases and the fit is unaffected**.
  - In that case Φ² ∝ (T/M_P)², independent of species.
- **Lorentz protection:** Mechanism A needs γ ≥ 6.4 (was 5.2).

## 5. Other framework numbers that shift (not frozen)
- **Reheating:** T_RH ~ 0.7–4.5×10¹⁸ GeV (was 0.5–3.4×10¹⁹). Thermal gravitons (equilibrium needs ≳ 3×10¹⁹ GeV) no longer thermalise.
- **Lorentz Mechanism A bounds** in §3.4: γ ≳ 1.25 (lab) and ≳ 3.1 (cosmic rays), were 1.19 and 2.79.
- **Branch L₃ monopole and thermal-history constraints** scale with Λ*, so their ratios to T_RH are unchanged. The existing tension (T_RH ≫ Λ*) is neither eased nor worsened.

## Verdict
- **Unchanged (9 of the 14 items in the table):**
  - dark energy w(z) and fσ8;
  - S8;
  - the Dirac-neutrino package (no 0νββ, normal ordering, Σm_ν = 72 meV, m_β);
  - the neutrino-mass fit rule;
  - ΔN_eff = 0.14;
  - proton-decay verdicts;
  - interferometer noise;
  - the hybrid.
- **Branch M** is mostly unchanged: its ripple fit is unaffected if the heat capacity counts species.
- **Affected:**
  - **the axion:** m_a ≈ 74 → ≈ 550 μeV, outside its frozen band but still a viable post-inflation dark-matter axion;
  - **the finite-volume prediction, which fails:** it would need a universe ~0.07 D_LSS, already excluded. Equivalently, grain-count dark energy is ~55× too weak;
  - minor: the thermal-graviton ΔN_eff increment and the remnant mass.
- **The frozen records are intact and untouched.** Any amended prediction (e.g. the axion at ~550 μeV) must be frozen separately, with a new timestamp and an explicit "post-audit" label.
