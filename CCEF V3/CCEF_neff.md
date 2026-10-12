# N_eff: gravity's species count for the full grain field content (2026-10-12)

**Code:** `ccef_neff.py` → `ccef_neff_output.txt` (26 s).

**Background:**
- In CCEF, Newton's constant is induced (Sakharov–Jacobson) by the entanglement of the fields living on the grains: G = ℓ²/(4η_g), with η_g = N_eff/(24π).
- The framework had **assumed N_eff ≈ 9**, giving M = ħc/ℓ ≈ 1.77×10¹⁹ GeV.
- `CCEF_induced_gravity.md` computed η_g on the grain lattice for a scalar and the grain electron and found N_eff ≈ 31.5 for those two alone.
- This note does the full count.

**Prior art:**
- Sakharov; Jacobson (1994, 1995);
- Srednicki and Bombelli et al. (area law);
- Kabat (gauge-field contact terms);
- Dvali (species bound: N species weaken gravity, M ~ M_P/√N);
- lattice "tastes = generations" (for the 3 X-valleys).

## 1. Heavy fields still count [computed]
The area law is set at the grain scale, so a field's mass matters only if it approaches the grain scale itself.

| Field | N_eff |
|---|---|
| scalar, mass 0 / 0.1 M / 0.3 M / 1.0 M | 2.18 / 2.14 / 1.94 / 1.09 |
| grain fermion, gapless / gapped by bond dimerisation (gap 1.04, 1.45 in grain units) | 27.1 / 25.2 / 23.0 |

- **Every Standard Model field counts fully**, being lighter than 10⁻¹⁶ M.
- **So do the mirror partners**, gapped at ~10¹³–10¹⁴ GeV ≈ 10⁻⁵ M (`CCEF_chiral.md`). Gravity's strength counts every field on the grains, light or heavy.

## 2. Grain electron vs spin–orbit strength [computed]
λ = 0.10 / 0.25 / 0.50 gives N_eff = 26.8 / 27.1 / 29.0. The result is robust.

## 3. The full content as CCEF builds it [computed counting]
| Sector | How it lives on the grains | N_eff |
|---|---|---|
| Fermions | 16 Weyl per generation (ν^c included), each paired with its lattice mirror into one grain Dirac field. The 3 X-valleys are the 3 generations, so there are **16 grain Dirac fields** | **434** (429–463) |
| Gauge bosons | 12 × 2 polarisations (massless-scalar proxy) | 52 |
| Higgs doublet | 4 real scalars | 9 |
| **Total** | | **N_eff ≈ 495** (490–524) |
| without mirror partners (for comparison) | 8 grain Dirac fields | 278 |

## 4. What it implies for the grain scale
ℓ = √(N_eff/6π) ℓ_P and M = ħc/ℓ:

| N_eff | ℓ | M |
|---|---|---|
| 9 (assumed so far) | 0.69 ℓ_P = 1.1×10⁻³⁵ m | 1.77×10¹⁹ GeV |
| 31.5 (light + electron) | 1.29 ℓ_P | 9.4×10¹⁸ GeV |
| 278 (no mirrors) | 3.84 ℓ_P | 3.2×10¹⁸ GeV |
| **495 (full, with mirrors)** | **5.1 ℓ_P = 8.3×10⁻³⁵ m** | **2.4×10¹⁸ GeV** |

**The grains are about 5 Planck lengths across, not 0.7.** The grain scale M is about 7× lower than assumed.

## 5. Cross-check with the grain budget (rough)
- A relation that is a bundle of n grains (qubits) can carry at most about n ln 2 of entanglement across a cut.
- On this cut that bounds N_eff ≲ 39 n.
- The full content therefore needs **n ≳ 13 grains per relation**.
- `CCEF_nonabelian.md` independently needed ~25–37 grains per relation to reach the real force strengths.
- **Consistent:** the relation bundles have room for the entanglement the fields need.

## Intriguing (numerology, not evidence)
- **M ≈ 2.4×10¹⁸ GeV is within ~3% of the reduced Planck mass** M_P/√(8π) = 2.435×10¹⁸ GeV.
- Exact equality would need N_eff = 48π² ≈ 474, against 495 computed (range 490–524).
- Likely a coincidence: the gauge-sector proxy alone is uncertain by more than the difference.

## Consequences and what must be re-checked
- **Every CCEF number that uses M = 1.77×10¹⁹ GeV or N_eff = 9 shifts.** M falls by ×0.13 and ℓ grows by ×7.4. Examples:
  - the reheating temperature (T ~ M);
  - the finite-volume bound of §4.1 (stated for N_eff = 9);
  - the hierarchy M/Λ*;
  - the dark-energy normalisation through ℓ.
- **The frozen pre-registrations are left untouched.** Those that depend on M need an audit and should be reported as affected, not silently changed **[OPEN]**.

## Caveats
- **The gauge bosons are treated as massless scalars.** Real gauge fields add edge-mode and contact terms (Kabat; the contact term can be negative). Their grain realisation as rishon bundles carries extra fermionic rishon modes, which would *raise* N_eff.
- **The grain qubits' own Gauss-law entanglement is not included.**
- **The area-law coefficient was computed for one cut orientation** ((001)) and depends on lattice details. Finiteness is the robust point; the exact value is not universal.
- **The fermion count depends on CCEF's own constructions:** 3 valleys = 3 generations (conjecture), and a mirror for every Weyl (forced by the lattice). Without mirrors, N_eff ≈ 278.
- **Jacobson's premises** (local Lorentz invariance, Unruh temperature, local equilibrium) are assumed.

## Verdict
- **N_eff ≈ 500 for the field content CCEF actually builds** (range ~490–520 with mirrors; ~280 without).
- That makes the grain ≈ 5 Planck lengths and **M ≈ 2.4×10¹⁸ GeV**, replacing the assumed N_eff ≈ 9 and M ≈ 1.77×10¹⁹ GeV.
- **The relation bundles of ~25–37 grains needed for the forces have enough room** for this much entanglement.
