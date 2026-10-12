# Toward a one-handed (chiral) weak force from grains (2026-10-12)

**Code:** `ccef_chiral.py` → `ccef_chiral_output.txt`. Follows `CCEF_parity_breaking.md`.

**The problem** (a famous open problem in physics itself):
- Any lattice, grains included, produces fermions in left+right pairs (the Nielsen–Ninomiya theorem). Our grain electrons are vector-like Dirac particles.
- A one-handed SU(2) needs the unwanted **mirror** partners made heavy **without bilinear masses**, which would pair left with right.
- That is **symmetric mass generation (SMG)**.

**Prior art:**
- Eichten & Preskill 1986 (the mirror-fermion route, with early difficulties);
- Fidkowski & Kitaev 2010 (interaction-gapping obeys "mod 8" in one dimension);
- Wang & Wen (non-perturbative lattice definition of the Standard Model via SMG, 2013/2020);
- Razamat & Tong 2021; Tong 2022 (gapped chiral fermions; SMG in 2d and 4d);
- Slagle, You & Xu 2015, and later bilayer lattice studies (numerical SMG);
- García-Etxebarria & Montero 2019 (the ℤ₁₆ anomaly and the right-handed neutrino).

## 1. Can a mirror generation be gapped symmetrically? Only with ν^c [computed]
Anomalies of one Standard Model generation (left-handed Weyl basis):

| Anomaly | 15 Weyl (no ν^c) | 16 Weyl (with ν^c) |
|---|---|---|
| U(1)_Y³, grav²·U(1)_Y, SU(2)²U(1)_Y, SU(3)²U(1)_Y, SU(3)³ | 0 | 0 |
| Witten SU(2) (doublets mod 2) | 0 | 0 |
| every Weyl fermion has X = 5(B−L) − 4Y ≡ 1 (mod 4) | ✓ | ✓ |
| **ℤ₁₆: Weyl count mod 16** | **15 ✗** | **0 ✓** |

- All perturbative anomalies cancel either way.
- But the non-perturbative ℤ₁₆ anomaly of the spin-ℤ₄ symmetry X cancels **only with the right-handed neutrino**.
- **A mirror generation can be gapped while keeping X only if each generation has exactly 16 Weyl fermions.**
- The right-handed neutrino is therefore required by the chiral construction itself. This is a third, independent reason for ν^c in CCEF, after ℤ₃ lepton triality (Branch L₃) and Majorana leptogenesis (Branch M).

## 2. Symmetric mass generation works, in multiples of 8 [computed, exact]
Setup:
- n Majorana fermions with a time-reversal symmetry that forbids *every* bilinear mass but allows every four-fermion term;
- random interactions only.

| n | Unique gapped ground state | Typical gap |
|---|---|---|
| 4 | 0 / 40 | — (always degenerate) |
| **8** | **40 / 40** | 1.8 |
| 12 | 0 / 40 | — (always degenerate) |
| **16** | **12 / 12** | 0.4 |

**Interactions alone gap the system, with no bilinear mass, exactly when the anomaly cancels** (n ≡ 0 mod 8: the Fidkowski–Kitaev rule). This is a small-scale, exact proof of principle of the mechanism. In 3+1 dimensions the analogous rule is "16 Weyl per generation" (§1).

## 3. The construction in the grain world [design; not simulated]
1. **Content.**
   - Each generation's 16 Weyl fermions appear **twice** on the grain lattice, as the lattice forces: a *light* copy and a *mirror* (conjugate) copy.
   - The full spectrum is vector-like, so all gauge anomalies vanish automatically on the lattice.
2. **Separation.**
   - The crystal's **breathing** (A ≠ B junctions, `CCEF_parity_breaking.md`) breaks P and C but conserves CP.
   - It pulls each Dirac fermion's left- and right-handed halves apart in momentum (computed). The light and mirror copies sit at different nodes.
3. **Gapping.**
   - A multi-fermion grain junction (four-fermion, Spin(10)-like, the 3+1-d analogue of the Fidkowski–Kitaev term) acts on the **mirror nodes only**. It preserves SU(3)×SU(2)×U(1) and X.
   - That gaps the mirror generation at ~v_R ≈ 10¹³–10¹⁴ GeV without any left–right mass.
   - The light copy stays massless until the Higgs gives the usual masses. The emergent SU(2) then acts on one handedness at low energy: **a chiral weak force**.
4. **Why the gap is allowed:** each mirror generation has 16 Weyl fermions with ℤ₁₆ = 0 (§1).

## Status
| Piece | Status |
|---|---|
| Anomaly condition for mirror gapping | ✅ computed: 16 per generation, ν^c required |
| SMG mechanism (gapping without bilinears) | ✅ exact toy demonstration (mod-8 rule) |
| Left/right separation by crystal breathing | ✅ computed (Weyl splitting) |
| Mirror-only gapping interaction tied to the breathing | ⚠️ designed, not demonstrated |
| Emergent non-abelian SU(2) (and SU(3)) from grains | ❌ not built (rishon / bundle construction still open) |
| 3+1-d SMG in the presence of gauge fields | ❌ an open research question generally; supported by 2+1-d numerics and theory, not proven |

## Verdict
- **Not built in full, but the route is mapped and its two key requirements checked:**
  1. the anomaly arithmetic allows the mirror partners to be gapped **if and only if** every generation has 16 Weyl fermions, i.e. **right-handed neutrinos exist**;
  2. interaction-only gapping works exactly when anomalies cancel (exact demonstration).
- Combined with the crystal's breathing, which separates left from right, this gives a concrete design for a one-handed weak force from grains: **light copy kept, mirror copy gapped at ~10¹³–10¹⁴ GeV.**
- **Predictions:**
  - right-handed neutrinos must exist (third independent reason);
  - matter comes only in **complete generations of 16** (no partial or exotic chiral fermions);
  - mirror fermions at ~v_R, invisible to colliders.
- **Biggest remaining gap:** emergent non-abelian gauge fields (SU(2), SU(3)) from grains, and a full 3+1-d demonstration with the gauge field present.
