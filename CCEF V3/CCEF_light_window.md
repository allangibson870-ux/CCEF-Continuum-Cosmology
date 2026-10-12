# The light sector's window: rescue confirmed, electrons must be rebuilt (2026-10-12; boundary corrected)

**Code:** `ccef_light_window.py` → `ccef_light_window_output.txt` (≈ 30 s).

> **Correction (same day):** the first version of this note quoted the photon-phase boundary as J±/J_zz ≈ 0.104.
> - Kato & Onoda write H = J s^z s^z + J⊥(s^x s^x + s^y s^y), so J± = −J⊥/2 in the convention used here (−J±(s⁺s⁻ + h.c.), J_ring = 12J±³/J_zz²). Their own ring scale g = 3J⊥³/(2J²) = 12J±³/J_zz² confirms it.
> - **The boundary is J±/J_zz ≈ 0.052** (|J⊥|/J ≈ 0.104).
> - The conclusions below are strengthened, not weakened.
>
> A second error is also corrected: CCEF's grain Hamiltonian writes −J±(σ⁺σ⁻ + h.c.) with J± > 0. That is the **unfrustrated** (zero-flux) sign, the one the Monte Carlo covers, not the frustrated sign as stated earlier.

**Question:** rishon splitting (`CCEF_rishon_splitting.md`) restores the finite universe when the light sector's coupling ratio x = J±/J_zz is small. Is that forced, and is everything else on the grains consistent with it?

**Literature:**
- **Photon-phase boundary:** Kato & Onoda, quantum Monte Carlo ([arXiv:1411.1918](https://ar5iv.arxiv.org/html/1411.1918); PRL 115, 077202, 2015). The quantum Coulomb liquid ends at |J⊥| ≈ 0.104 J (J±/J_zz ≈ 0.052). The photon speed is c ≈ 1.49 a g.
- **Emergent QED parameters:** Pace, Morampudi, Moessner & Laumann ([arXiv:2009.04499](https://arxiv.org/pdf/2009.04499)). The emergent α ≈ 0.08 is tunable.
- **Spin-ice charges outrun the light (Cherenkov):** [arXiv:1906.01628](https://arxiv.org/pdf/1906.01628), as summarised by search.

## 1. The rescue is the photon's own existence condition [computed]
| x = J±/J_zz | R = J_zz/J_ring | median universe size L (D_LSS), n = 25 / 31 / 37, N_ent = 495 |
|---|---|---|
| **0.052 (edge of the photon phase)** | 593 | **1.9 / 2.1 / 2.2** |
| 0.04 | 1,302 | 2.5 / 2.7 / 2.9 |
| 0.03 | 3,086 | 3.3 / 3.6 / 3.8 |
| 0.02 | 10,417 | 5.0 / 5.4 / 5.7 |

- **Light exists only for x < 0.052, and throughout that range the rishon-splitting universe is ≳ 2 D_LSS.**
- With the updated N_ent ≈ 880–1,080 (`CCEF_valleys_edges.md`), the edge value is **1.2–1.4 D_LSS**. That is still ≳ 1 D_LSS wherever light exists.
- **The rescue is automatic, not a tuning: L ≈ 1.3 (x_c/x) D_LSS.**

## 2. Electrons built as bare spin-ice charges fail in that window [computed]
**(a) Too fast:**

| x | charge hopping / light scale = 1/(12x²) |
|---|---|
| 0.052 | 31 |
| 0.03 | 93 |

**(b) Mott-gapped.** The grain electron's mean-field threshold is U_c = 4.95 t (staggered magnet). Against it:
- U/t ~ 1/x ≈ 19–33 for hopping set by J±;
- U/t ~ R ≳ 590 if the hopping were matched to light.

**Conclusion:** the electron must be rebuilt. It must be a separate bundle constituent, coupled through div E = ρ, with its own hop. **Done in `CCEF_electron_rebuild.md`.**

## Verdict
- **Wherever the grains carry light (J±/J_zz < 0.052), the rishon-split dark energy gives a universe ≳ 1.2 D_LSS.** The rescue is automatic.
- **Electrons made of bare spin-ice charges cannot live there:** they are too fast (×31) and Mott-gapped. The rebuilt electron fixes this.
