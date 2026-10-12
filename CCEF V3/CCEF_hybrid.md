# The CCEF hybrid: Branch M early universe + a dark string-net sector (2026-10-12)

**Code:** `ccef_hybrid.py` → `ccef_hybrid_output.txt` (order-of-magnitude estimates). Follows `CCEF_branchM.md`, whose open hole was dark matter.

## Construction
- **Base: Branch M**, i.e. the minimal string-net rules, crossover Λ* ≈ 10¹⁵ GeV, which gives:
  - Majorana neutrinos and thermal leptogenesis;
  - proton decay in the Hyper-K window (μ⁺π⁰ ≈ e⁺π⁰);
  - area-law primordial ripples frozen at Λ*;
  - the Planck-hot start (T_RH ~ 10¹⁹ GeV).
- **Added: a dark sector made of extra string *labels* on the same grains** (P7 kept: no new grain type):
  - a vector-like dark fermion χ charged under a dark U(1)_D (or dark SU(N)), neutral under the Standard Model;
  - **Stability is automatic:** the lightest dark-charged string end cannot decay, by the dark Gauss law, just as the electron is stable by electric charge conservation.
- **Why dark matter must have its own interactions:**
  - after a Planck-hot start every sector is thermalised at ~M;
  - a stable relic with only gravitational interactions can never annihilate, so it overcloses;
  - so dark matter must annihilate within its own sector.
- **Dark and ordinary sectors share a temperature at ~M.** The dimension-6 portal junctions at Λ* freeze out at ~10¹⁴ GeV. Later Standard Model entropy releases leave the dark sector cooler: T_D/T_γ ≈ 0.33, times self-heating.

## Two versions
### H1: Secluded thermal relic
- χχ̄ annihilates into dark photons, σv = πα_D²/m².
- Right abundance ("WIMPless miracle"): m_χ ≈ **0.4–1.8 TeV for α_D = 0.01–0.03** (scales linearly with α_D).
- **The dark photon must be massive.** A massless one would be heated by χ annihilation and add ΔN_eff ≈ 0.21 (0.26 with gravitons), which the CMB disfavours. A massive one must decay before nucleosynthesis: kinetic mixing ε ≳ 2×10⁻¹⁰ (10 MeV) to 2×10⁻¹¹ (1 GeV).
- **The mass is not predicted.**

### H2: Asymmetric dark matter [preferred]
- A portal junction at Λ* (e.g. (LH)(χφ_D), allowed in Branch M) shares the **B−L asymmetry from leptogenesis** with χ before freezing out. The dark excess and the baryon excess have one origin.
- m_χ = (Ω_DM/Ω_b)·m_p/(n_χ/n_B) ≈ **2.5–10 GeV** (5 GeV for equal numbers).
- The symmetric part annihilates away if α_D ≳ 10⁻⁴: easy.
- **This explains why dark matter and ordinary matter have similar densities** (5.4 : 1), a coincidence most theories leave unexplained. The dark mass itself (a few GeV, e.g. a dark-confinement scale) is not predicted.

## The hybrid package
| Item | Hybrid (H2) | Branch L₃ | Branch M |
|---|---|---|---|
| Primordial ripples | ✅ (area-law, Λ* ≈ 10¹⁵, c ~ 0.02–0.2) | ❌ | ✅ |
| Matter excess | ✅ leptogenesis | ❌ | ✅ |
| **Dark matter** | ✅ **asymmetric, ~2.5–10 GeV, same origin as baryons** | ✅ axion 74 μeV | ❌ |
| Ω_DM/Ω_b ≈ 5 | ✅ explained (given m_χ) | ✗ coincidence | — |
| Proton decay | ✅ Hyper-K window, μ⁺π⁰ ≈ e⁺π⁰ | stable | ✅ |
| Neutrinos | Majorana, NO (26 : 1), Σ ≈ 77 meV, **m_ββ ≈ 18 meV** | Dirac, no 0νββ | same as hybrid |
| ΔN_eff | **≈ 0.05** (gravitons; massive dark photon) | 0.14–0.19 | ≈ 0.05 |
| Strong CP | ⚠️ needs an axion at an unexplained scale (f_a ~ 10⁹–10¹¹, sub-dominant dark matter) or another solution | ✅ | ⚠️ |
| Lorentz protection | γ ≳ 5–6 (or SUSY / random grains) | γ ≳ 3 | same |
| Three generations derived | ✗ | ✅ | ✗ |
| New ingredients | dark labels, a dark force, a portal junction | Z3 grading | — |

> **Strong CP (follow-up, `CCEF_strong_cp.md`):**
> - The grain crystal's inversion symmetry acts as parity on the emergent fermions and forbids the θ-type quark mass phase even with CP-violating couplings (computed). With θ_QCD = 0, that is the axion-free "parity solution".
> - **Open:** how parity breaks in the chiral sector without feeding θ̄ > 10⁻¹⁰, and domain walls.
> - **Prediction:** a neutron EDM within reach of the next generation of experiments; no axion.

## Testable signatures of the hybrid
- **Proton decay** at Hyper-K, with similar e⁺π⁰ and μ⁺π⁰ rates.
- **Neutrinoless double-beta decay** at ~10–30 meV (LEGEND-1000, nEXO); normal ordering; Σm_ν ≈ 77 meV.
- **ΔN_eff ≈ 0.05** (CMB-S4 can just reach this).
- **Light dark matter (2.5–10 GeV) plus a dark photon:** low-mass direct detection (SuperCDMS, CRESST, DarkSide-type), and dark-photon searches if ε is not tiny. Nothing in heavy-WIMP detectors.
- Shared with the whole framework: non-phantom dark energy; a finite universe; no Hawking points; slightly blue primordial gravitational waves if any.

## Verdict
**The hybrid is the most complete version of CCEF so far.** For the first time, one package covers primordial ripples, the matter excess, dark matter (with the 5 : 1 ratio explained), neutrino masses and proton decay, without inflation.

**The price:**
- extra structure (dark labels, a dark force, a portal);
- a dark-matter mass of a few GeV that isn't derived;
- an unsolved strong-CP problem;
- a stronger Lorentz-protection requirement;
- losing L₃'s derivation of three generations.

It also makes a cluster of near-term predictions (proton decay, 0νββ, ΔN_eff ≈ 0.05, light dark matter) that experiments in the next ~10–15 years can confirm or kill.
