# CCEF — Calibration vs. Mass Claim, and Current Parameters
**2026-06-22.** No hand-fitting. Labels: [SOLID] / [CONJECT] / [OPEN].

## 1. The calibration does not claim the proton mass — it predicts it
Two units are fixed by two conditions, **neither of which is the mass**:
1. **Length** ← proton charge radius: screening length `L0/Λ = r_p` ⟹ `L0 = r_p·√(A4/A1)`
2. **Energy** ← quantum relation: `E0·L0 = ħc/4`

The soliton mass is therefore a *derived prediction*. Correct, non-fitting structure.

## 2. The mass prediction reduces to ONE dimensionless condition
With both units fixed, all dimensionful factors cancel:

```
m_sol / m_p = (E_sol / √A4) · [ ħc / (4 r_p m_p) ]
            = (E_sol / √A4) · 0.0616
```

- Gap closes  ⟺  **E_sol/√A4 = 16.24**.
- Today's relaxation: E_sol/√A4 ≈ 45  →  **m_sol ≈ 2.78 × m_p** (too heavy).
- The "1/4" in `E0·L0 = ħc/4` is [CONJECT] and does ~4× of work: with full ħc the
  requirement becomes E_sol/√A4 = 4.06 (worse). The mass prediction floats by
  exactly the undetermined ħc coefficient.

**The mass gap is a sharp falsifiable prediction, not calibration slack.**

## 3. The knot: A4 does double duty
A4 sets **both** the screening length (Λ=√(A4/A1) → L0, E0) **and** the soliton
energy. It is not free.
- Calibration assumes **A4 = 3.5553** → L0=1.611 fm, E0=30.6 MeV, target m_p=30.65 CCEF.
- Task-B self-consistency wants **A4 ≈ 0.14–1.02** → L0≈0.6 fm, E0≈80 MeV, target≈11–16 CCEF.
- These disagree. **Calibration and soliton sector are not yet mutually consistent.**
  Resolving this (one A4 that satisfies both) is the real open problem.

## 4. Current parameters
| Param | Value | Status |
|---|---|---|
| A1 | 1.0 | [SOLID] axiomatic |
| Zt | 1.0 | [SOLID] axiomatic |
| A3 | 0 (IR); runs, β(A3)=−A3²/16π²A1; A3_UV core only | [SOLID] Task A |
| r_p (input) | ≈ 0.854 fm | [SOLID] target |
| L0 | r_p·√(A4/A1) = 1.611 fm (if A4=3.5553) | [SOLID] given A4 |
| E0 | ħc/(4 L0) = 30.6 MeV | [SOLID] method; 1/4 [CONJECT] |
| m_p | 30.65 CCEF (if A4=3.5553) | derived |
| **A2** | not pinned: 0.327 (FN, untrusted) / 3.4–6.9 (Task B) / 8.971 (superseded) / 37.4 (v3.1 core) | **[OPEN]** |
| **A4** | not pinned & conflicted: 3.5553 (calibration) vs 0.14–1.02 (Task B) | **[OPEN]** |

## 5. Verdict
Calibration is clean (radius + ħc; mass left as prediction). The prediction fails
by ~2.8×, and the failure sits in (i) the unproven 1/4 coefficient and (ii) the
dimensionless soliton energy E_sol/√A4, coupled through A4. Closing it requires
*deriving* the ħc coefficient and a jointly-consistent (A2, A4) — not fitting.
