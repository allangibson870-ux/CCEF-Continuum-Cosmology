# Sub-structural relation bundling ("rishon splitting") as a rescue (2026-10-12)

**Code:** `ccef_rishon_splitting.py` → `ccef_rishon_splitting_output.txt` (seconds).

**The problem it addresses:** the audit (`CCEF_prediction_audit.md`) found that with the computed N_eff ≈ 495:
- the grain length is ℓ = 5.1 ℓ_P;
- the grain-count dark energy ρ_Λ ~ β/(ℓ²√V₄) comes out ~55× too weak;
- equivalently, the finite-universe prediction shrinks to ~0.07 D_LSS (excluded);
- separately, the axion moved from 74 to ~550 μeV.

**The idea (the author's proposal):**
- A relation is not one grain but a **bundle of n sub-grains** (rishons). n ≈ 25–37 was already needed for the force strengths (`CCEF_nonabelian.md`).
- Gravity's G is set by the *fields* on the junction lattice, so N_eff and ℓ are unchanged.
- But the dark-energy 4-volume count should count the **finest independent elements**: the sub-grains, or their elementary update events.

**Prior art:**
- Sorkin's everpresent Λ (ρ_Λ ~ 1/ΔV₄ from Poisson counting);
- rishon / quantum-link models (Harari, Shupe; Brower, Chandrasekharan, Wiese);
- hyperuniformity of crystals (Torquato);
- quantum spin ice ring exchange J_ring = 12J±³/J_zz² (Hermele, Fisher, Balents).

## 1. When does finer counting help? [computed, Monte Carlo]
| How the elements arise | σ(V₄)/V₄ |
|---|---|
| (a) random bundles, each with exactly n sub-grains | 1.58×10⁻² (= 1/√bundles) |
| (b) random bundles, random occupancy | 1.61×10⁻² |
| **(c) a crystal of bundles, random sub-grain events** | **2.88×10⁻³ (= 1/√sub-grains)** |

**Finer counting shrinks the 4-volume noise, and so strengthens Λ, only if the bundle (junction) count does not itself fluctuate.**
- If junctions were sprinkled randomly, their noise would dominate and bundling would gain nothing.
- In CCEF the junctions form a **crystal**: one-seed growth produces perfect diamond. A crystal is hyperuniform, with count noise only from region boundaries, so the condition is met.
- This is a nice internal consistency: the crystallisation result is what makes the rescue possible.

## 2. How many elements are needed [computed]
With counting length ℓ_c² = ℓ²/√n₄ (n₄ = independent elements per ℓ⁴ of spacetime), the frozen formula gives:

**median L_max = 0.072 × n₄^(1/3) D_LSS**

| Target | n₄ needed |
|---|---|
| 1.0 D_LSS | 2,700 |
| 1.04 D_LSS (exactly the frozen value) | 3,025 = (N_eff/9)² |
| 1.5 D_LSS | 9,100 |

## 3. Where the elements come from [computed]
n₄ = (sub-grains per ℓ³) × (events per sub-grain per light-crossing time) = 1.3n × R.

**Spatial bundling alone (R = 1) is not enough:** n₄ ≈ 32–48, giving L ≈ 0.23–0.26 D_LSS, still excluded. It supplies only ~6× of the needed 55×.

**Microscopic update events supply the rest.**
- In quantum spin ice, light is the *slow* third-order ring exchange.
- Each grain is updated R = J_zz/J_ring = (J_zz/J±)³/12 times per light-crossing time.

| J±/J_zz | R | median L_max (D_LSS), n = 25 / 31 / 37 |
|---|---|---|
| 0.03 | 3,086 | 3.3 / 3.6 / 3.8 |
| 0.05 | 667 | 2.0 / 2.2 / 2.3 |
| 0.08 | 163 | 1.25 / 1.35 / 1.43 |
| **0.10** | **83** | **1.00 / 1.08 / 1.14** |
| 0.15 | 25 | 0.67 / 0.72 / 0.76 |
| 0.20 | 10 | 0.50 / 0.54 / 0.57 |

- **For J±/J_zz ≲ 0.1, deep in spin ice's photon phase, the finite universe comes back at ~1–3.5 D_LSS.** That is the frozen range or somewhat larger, consistent with the CMB.
- The cosmic size becomes tied to the light sector's coupling ratio: **L ≈ 0.1 (J_zz/J±) D_LSS.** Since n₄ enters only as its cube root, the result is not finely tuned.
- The reported edge of the spin-ice Coulomb phase (literature ~0.05–0.2, quoted from memory) is close to this threshold. That makes it a real constraint on the grain rules, not a free fit.

## 4. Side effect: the axion returns to its frozen band [computed]
- The gauge-singlet ν^c string has no gauge charge to tie it to particular rishons, so it can spread over **all** sub-grains of a crossover cell.
- Its dilution then involves 1.3n(M/Λ*)³ sub-grains, giving Λ* = M·y^(2/3)·(1.3n)^(1/3).

| | Λ* (GeV) | m_a |
|---|---|---|
| audit (no sub-grains) | 1.0×10¹⁰ | 546 μeV |
| n = 25 / 31 / 37 | 3.3 / 3.6 / 3.8 ×10¹⁰ | **171 / 159 / 150 μeV (36–41 GHz)** |

**Back inside the frozen band (14–400 μeV)**, though the central value is ~2× the frozen 74 μeV. n was fixed earlier by the force strengths, not tuned here. Whether ν^c really spreads over all rishons is an assumption.

## What is and is not fixed
| Item | Status with rishon splitting |
|---|---|
| N_eff ≈ 495, M ≈ 2.4×10¹⁸ GeV | unchanged (the fields live on the junction lattice) |
| Finite volume / Λ magnitude | **restored (1–3.5 D_LSS) if J±/J_zz ≲ 0.1** and the 4-volume counts microscopic grain events; not restored by spatial bundling alone |
| Axion | **back in the frozen band**, ~150–170 μeV, if ν^c spreads over sub-grains |
| Other predictions | unchanged (as in the audit) |

> **Janus-branch fork (paper §3.2, §13 item 13):** if the Janus point has k branches and Λ counts all of them, the size is multiplied by (2/k)^(1/3) (×0.79 / 0.69 / 0.63 for k = 4 / 6 / 8).
> - With N_ent ≈ 880–1,080 and the corrected photon edge (J±/J_zz ≈ 0.052), L ≈ 1.3 (x_c/x)(2/k)^(1/3) D_LSS.
> - For k = 8 this needs J±/J_zz ≲ 0.043 for L ≥ 1 D_LSS.
> - If Λ counts our branch only, nothing changes.

## Caveats
- **Post-hoc.** This rescue was devised after the failure was found. It is a hypothesis to be tested, not a confirmation, and the frozen records stand as they were.
- **Two new assumptions:**
  1. the 4-volume that is conjugate to Λ counts *elementary update events* of the microscopic grain rule (spin-flip scale J_zz), not junctions;
  2. those events are statistically independent (Poisson), while the junction lattice is crystalline.

  Neither is derived.
- In the event picture of `CCEF_grain_rules.md`, the microscopic spin-ice events happen at an energy J_zz ~ R·M, above the grain scale M. Whether such fast internal events count as spacetime elements is exactly the open question.
- **If the rishons' own entanglement adds to N_eff,** M drops further and the requirement n₄ ∝ N_eff² grows. This only partly compensates, because n₄ also grows with n.
- **The Coulomb-phase boundary of quantum spin ice** is quoted from memory and depends on the model details.

## Verdict
- **Rishon splitting can fix it, but only in its strong form.**
  - Counting the bundles' sub-grains alone recovers ~6× of the missing 55×: not enough.
  - Counting the elementary events of the sub-grains, which in spin ice happen ~(J_zz/J±)³/12 times per light-crossing, restores the finite universe at **~1–3.5 D_LSS for J±/J_zz ≲ 0.1**.
  - This relies on the crystal (hyperuniform) junction lattice that one-seed growth produces.
- **The same bundling brings the axion back to ~150–170 μeV**, inside its frozen band.
- **The price** is two new, physically motivated but underived assumptions, and a new link: **the size of the universe is set by the light sector's coupling ratio, L ≈ 0.1 (J_zz/J±) D_LSS**.
