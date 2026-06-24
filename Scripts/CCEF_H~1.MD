# CCEF — The ħc Coefficient, Derived from First Principles
**2026-06-22. No hand-fitting.** Result: **E0·L0 = ħc** (coefficient = **1**, not 1/4).

## Setup
CCEF natural units: A1 = Zt = 1 ⟹ emergent light speed c_eff = √(A1/Zt) = 1.
So the CCEF length unit L0 and time unit T0 obey **L0 = c·T0** (c = physical light
speed; this is what "c_eff = 1" means once mapped to physical units).

## Derivation (action quantisation) [SOLID]
The only quantum input is the standard one: **the action is measured in units of ħ**,
i.e. the dimensionless CCEF action numbers *are* S/ħ (ħ_CCEF ≡ 1). Then convert the
action to physical units. Since `S = ∫dt d³x L` has units of energy × time,

```
S_phys = (E0 · T0) · S_CCEF        (energy unit × time unit)
S_phys = ħ · S_CCEF                 (ħ_CCEF = 1)
⟹  E0 · T0 = ħ
```

Insert T0 = L0/c:

```
E0 · L0 = ħ c          →   coefficient = 1
```

## Two independent cross-checks (same answer) [SOLID]
1. **Gap mode E = ħω.** IR dispersion ω² = (1/Zt)(A4 + A1k²) ⟹ gap frequency
   ω₀ = √A4 (CCEF). Frequency unit = c/L0, so ω₀,phys = √A4·c/L0. Its quantum energy
   E = ħω₀,phys must equal the gap energy √A4·E0 ⟹ **E0·L0 = ħc**.
2. **Compton wavelength.** Gap mode has CCEF mass √A4 and CCEF size 1/√A4.
   λ_C = ħ/(m c) ⟹ (1/√A4)L0 = ħc/(√A4·E0) ⟹ **E0·L0 = ħc**.

All three routes give the **same** coefficient 1. There is **no factor of 1/4**.
The resume's "(4π)/π = 4" was a post-hoc rationalisation, not a derivation.

## Numbers
L0 = r_p·√(A4/A1) = 1.610 fm (radius calibration, coefficient-independent).

| Coefficient | E0 | m_p in CCEF | gap mode | m_sol/m_p (fixed pt, IR) |
|---|---|---|---|---|
| **1 (first principles)** | **122.5 MeV** | **7.66** | **231 MeV** | **≈ 17×** |
| 1/4 (doc conjecture) | 30.6 MeV | 30.6 | 57.8 MeV | ≈ 4.3× |

## Independent support for coefficient = 1 [SOLID]
With coefficient 1 the elementary CCEF excitation (mass gap) sits at **231 MeV** —
landing on the resume's quasinormal-resonance cluster (**233–298 MeV**) found by a
completely separate calculation. The 1/4 choice would put the gap at 57.8 MeV,
inconsistent with that scale. So the resonance spectrum independently favours
coefficient 1.

## Consequence for the mass gap [SOLID]
The first-principles coefficient makes the discrepancy **worse, not better**: the
Q=1 Hopf baryon is ≈ **17× too heavy** (best IR-limit fixed-point bound), versus the
≈4× the unjustified 1/4 produced. The 1/4 had been flattering the result by exactly
that factor of four.

**Bottom line:** the ħc relation is `E0·L0 = ħc` with coefficient 1, derived (not
fitted) from ħ_CCEF = 1 and c_eff = 1, and cross-checked three ways plus the
resonance scale. It confirms — more strongly — that CCEF predicts a baryon roughly
an order of magnitude heavier than the proton. The mass mismatch is structural and
is now free of the one adjustable-looking constant in the calibration.
