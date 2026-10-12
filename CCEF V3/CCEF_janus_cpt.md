# Matter and antimatter in a CPT-symmetric (Janus-point) grain universe (2026-10-12)

**Code:** `ccef_janus_cpt.py` → `ccef_janus_cpt_output.txt`.

**Ideas used (not ours):**
- the Janus point (Barbour, Koslowski & Mercati 2014; Barbour 2020);
- the CPT-symmetric universe (Boyle, Finn & Turok 2018);
- Sakharov's conditions (1967);
- asymmetry set by initial conditions, as in Affleck–Dine (1985).

**Follows:** `CCEF_grain_CP.md`, where spontaneous chirality was not found.

## The question
Can the Janus point, the moment of least structure from which time's arrow points away in *both* directions, explain matter vs antimatter? On one side matter, on the other its CPT mirror?

## Two facts that follow from symmetry alone
1. **At the Janus point the baryon number is exactly zero.** CPT flips both baryon number and the direction of time, so in a CPT-symmetric universe B(t) = −B(−t), and B(0) = 0. In the grain picture this is doubly true: the Janus point is the pre-geometric tangle, where no particles exist. **So matter must appear after the Janus point, on each side.**
2. **The two sides are mirror images.**
   - Whatever excess forms on our side, the other side forms the CPT-opposite.
   - The cosmos as a whole stays balanced, and the "missing antimatter" is on the other side of the Janus point.
   - Each side's observers, using their own arrow of time, see *their* side as matter-dominated with the same laws.

## Grain check [computed]
Adding the CP-odd junction-chirality coupling (λ = 0.01) to the 4-grain junction Hamiltonian breaks P, T and CP but keeps **CPT** (and C). **A CP-violating grain universe can still be CPT-symmetric about a Janus point.**

## Janus toy model [computed]
- **Sectors:** matter (B = +1), antimatter (B = −1) and neutral (B = 0), each 40 levels.
- **The laws:** CPT-invariant, with baryon number violated only near the Janus point (a coupling that fades away on both sides, as when the universe cools).
- **The state:** CPT-invariant at t = 0, evolved forward and backward in time.

| Case | B at the Janus point | Our side, late | Mirror side, late |
|---|---|---|---|
| (a) CP-symmetric laws, CP-symmetric Janus state | 0 (10⁻²⁰) | 0 | 0 |
| **(b) CP-symmetric laws, CP-odd phase in the Janus state** | 0 (10⁻¹⁹) | **+0.0004** | **−0.0004** |
| (c) CP-violating laws, CP-symmetric Janus state | 0 (10⁻²⁰) | +0.023 | −0.023 |
| (d) As (b), but baryon violation **never switches off** | 0 | −0.002 ± 0.005, fluctuating about 0 | +0.002 ± 0.005 |

In case (d), the long-time (diagonal-ensemble) value of B is **2×10⁻¹⁵**: the asymmetry is erased.

**Reading:**
1. **The Janus picture moves Sakharov's CP condition, it doesn't remove it.** CP asymmetry must come either from the **laws** (case c, the standard route) or from the **state of the universe at the Janus point** (case b). Case b is new in emphasis: the laws can be perfectly CP-symmetric, and the "decision" about the sign is made at the Janus point, then read out once matter-making processes act.
2. **Baryon violation must switch off as the universe moves away from the Janus point** (out of equilibrium). If it stays on, the asymmetry averages to zero (case d), because CPT forces every energy eigenstate to have zero baryon number. The Janus arrow of time naturally provides the switch-off: cooling on both sides.
3. **Global balance and opposite signs on the two sides are automatic.** No antimatter is missing; it is in the mirror branch.

## What it means for the grain universe (Branch L₃)
| Requirement | Status in CCEF |
|---|---|
| B = 0 at the Janus point | ✅ automatic (the tangle has no matter, and CPT) |
| Baryon violation that switches off with cooling | ✅ the ΔB = 2 junction, rate ∝ T¹¹: active near Λ*, off below. If its strength factor c ≲ 10⁻⁷ it never even equilibrates (no washout) |
| A CP-odd ingredient | ⚠️ **either** explicit CP-odd grain couplings (case c), **or** a CP-odd phase in the universal grain state at the Janus point (case b) |
| Survival of a state-phase until matter exists | ❌/⚠️ the hot phase after crystallisation would erase it if it thermalises while baryon violation is active (case d). It works only if the matter-making epoch is out of equilibrium from the start, e.g. crystallisation happening near Λ* or a weak ΔB = 2 coupling |
| Size of the excess (6×10⁻¹⁰) | ❌ not predicted: set by the CP-odd laws or by the Janus state |

## Conjecture: alternating cycles
In CCEF's cyclic picture, each cycle ends by re-melting into the tangle, and the next cycle crystallises from it. If each re-melting is a Janus point, **neighbouring cycles are CPT mirrors of each other**: a matter cycle, then an antimatter cycle, and so on. Each looks matter-dominated to its own observers. Untestable, since no clock or record survives between cycles, but it is a coherent picture.

> **Update (`CCEF_reheat.md`):**
> - Crystallisation reheats the universe to ~10¹⁹ GeV. That thermal phase scrambles any CP-odd phase carried by the Janus-point state (case b), so the matter excess must come from CP violation in the laws (case c).
> - The mirror picture itself (antimatter on the other side, global balance) is unaffected.

## Verdict
- **The Janus/CPT option is self-consistent in the grain framework and the most economical answer so far.**
  - It explains where the antimatter is (the mirror branch) and why the cosmos is balanced overall.
  - It provides the out-of-equilibrium arrow.
  - It shows the laws can stay CP-symmetric, provided the Janus-point state carries a CP-odd phase that survives until matter switches on.
- **What it does not do:** predict the size of the excess. Nor does it remove the need for baryon violation that switches off as the universe cools.
- **The new open question:** what fixes the universal state at the Janus point, and could its CP-odd phase survive crystallisation?
