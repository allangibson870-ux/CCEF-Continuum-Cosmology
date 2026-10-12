# Branch M rebuilt as a package, and tested (2026-10-12)

**Code:** `ccef_branchM.py` → `ccef_branchM_output.txt`.

**Branch M** = the minimal string-net rules, with no ℤ₃ lepton triality. Hence:
- proton decay via local dimension-6 junctions at Λ*;
- Majorana neutrinos (seesaw / Weinberg operator at Λ*);
- standard thermal leptogenesis.

Inputs carried over: reheating T_RH ~ 10¹⁹ GeV (`CCEF_reheat.md`); area-law ripples frozen at T_f = Λ* (`CCEF_ripples.md`).

## The package
| Piece | Result | Coefficient needed |
|---|---|---|
| **Neutrino masses** m₃ = k·v²/Λ* | **Λ* ≈ 6×10¹⁴ GeV** (k = 1); range 1.8×10¹⁴–1.8×10¹⁵ for k = 0.3–3 | k = O(1) |
| **Proton decay** τ = 8.7×10³⁵ yr (Λ*/10¹⁶)⁴/C² | Super-K satisfied and **Hyper-K discovery** for C in a window: 0.012–0.022 (Λ* = 6×10¹⁴); 0.11–0.20 (1.8×10¹⁵). Flavour-blind grains → **μ⁺π⁰ ≈ e⁺π⁰** | C ~ 0.01–0.2 (suppressed junction) |
| **Primordial ripples** (area-law, frozen at Λ*) | A_s = 2.1×10⁻⁹ needs c = 0.18 (Λ* = 6×10¹⁴) to 0.02 (1.8×10¹⁵) | c = O(0.02–0.2) ✅ |
| **Matter–antimatter** (thermal leptogenesis, M₁ ~ 0.1–1 Λ*, T_RH ≫ M₁) | Davidson–Ibarra ε_max = 0.01–0.06; strong washout (K ≈ 46, efficiency ~3×10⁻⁴) still gives η_B up to **2×10⁻⁸–2×10⁻⁷ (needed 6×10⁻¹⁰)** ✅ | CP phases in the neutrino junctions (explicit, as required anyway) |
| **Neutrinos** (Majorana anarchy, 4×10⁶ matrices) | normal ordering **26 : 1**; **Σm_ν = 77 meV** (66–95); lightest 11 meV; **m_ββ = 18 meV** (9–33); **P(m_ββ > 10 meV) = 0.79**, P(> 20 meV) = 0.45 | — |
| **Relic radiation** | ν^c heavy, so only thermal gravitons: **ΔN_eff ≈ 0.05** | — |
| **Lorentz protection** | Mechanism A needs **γ ≳ 4.6–5.8** (vs 3 in L₃); otherwise SUSY or random grains | stronger requirement ⚠️ |
| **Dark matter** | ❌ An axion with f_a = Λ* overproduces by **4×10³–6×10⁴** (a Planck-hot start forces the post-inflation scenario). Heavy right-handed-neutrino dark matter (Boyle–Finn–Turok style) thermalises at T ~ M and overcloses. Needs a separate Peccei–Quinn scale ~10¹⁰–10¹¹ GeV (unexplained) or a new candidate | **open hole** |
| **Strong CP** | the axion is still needed, at an unexplained scale | ⚠️ |

**A sweet spot exists:** Λ* ≈ 10¹⁵ GeV, with every coefficient in the 0.01–1 range. There, neutrino masses, ripple amplitude, proton decay at Hyper-K and leptogenesis all fit at once.

## New constraint for *both* branches: no stable Planck remnants
- With a Planck-hot start (T_RH ≈ 0.3–0.5 M), grain-count fluctuations are δ ≈ 0.16–0.35. The fraction of energy forming Planck-scale black holes is ~10⁻⁴–10⁻¹, while dark matter allows only ~10⁻²⁸.
- **If such black holes left stable remnants, the universe would be overclosed by ~10²⁶.**
- So CCEF needs **complete evaporation** (no stable remnants), and the "Planck-remnant dark matter" option is **excluded** in both branches.

## Branch M vs Branch L₃
| Item | **Branch L₃** | **Branch M** |
|---|---|---|
| Crossover Λ* | ~8×10¹⁰ GeV | **~10¹⁵ GeV** |
| Proton | stable | **decays; Hyper-K window**, μ⁺π⁰ ≈ e⁺π⁰ |
| Neutrinos | Dirac; Σ ≈ 72 meV; no 0νββ | **Majorana; Σ ≈ 77 meV; m_ββ ≈ 18 meV (likely seen by LEGEND-1000 / nEXO)** |
| Ordering | normal (175 : 1) | normal (26 : 1) |
| ΔN_eff | 0.14–0.19 | **≈ 0.05** |
| Primordial ripples | ❌ amplitude 10⁻⁷ too small | ✅ natural coefficient |
| Matter–antimatter | ❌ no working mechanism | ✅ standard leptogenesis |
| Dark matter | ✅ axion 74 μeV | ❌ none natural |
| Strong CP | ✅ axion at Λ* | ⚠️ axion at an unexplained scale |
| Lorentz protection | γ ≳ 3 | γ ≳ 5–6 (or SUSY / random grains) |
| Three generations | required by anomaly cancellation | not required |

## Verdict
- **Branch M is the more complete and more testable cosmology:**
  - it produces the primordial ripples and the matter excess with ordinary coefficients;
  - it predicts two things next-generation experiments are likely to see: **proton decay at Hyper-K** and **neutrinoless double-beta decay at ~10–30 meV**.
- **Its hole is dark matter:** the elegant L₃ axion does not survive (an axion at Λ* overproduces by 10⁴).
- **Branch L₃** keeps dark matter, Dirac neutrinos and the "three generations" derivation, but fails on the two biggest early-universe questions.
- **Neither branch is complete. The experiments separate them cleanly:**
  - **proton decay or 0νββ seen** → Branch M;
  - **neither seen, and ΔN_eff ≈ 0.14–0.19** → Branch L₃.
- The obvious next idea is a **hybrid**: Branch M for the early universe, plus a dark-matter mechanism that doesn't need the axion to sit at Λ*.
