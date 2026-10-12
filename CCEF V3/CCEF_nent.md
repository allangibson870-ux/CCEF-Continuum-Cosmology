# N_ent: gravity's entanglement number, derived from the current grain theory (2026-10-12)

**Code:** `ccef_nent.py` → `ccef_nent_output.txt` (12 s).

**Name:**
- **N_ent** (the "entanglement number") replaces the old label "N_eff" for gravity's count, which clashed with the cosmological ΔN_eff (extra relativistic species, ≈ 0.14 in CCEF).
- The physical quantity is η_g: the entanglement across a surface per grain area ℓ². N_ent = 24π η_g is only a conventional rescaling.

**Rule:** only the current grain theory is used, no number from earlier CCEF versions. The relation is Jacobson's: G = ℓ²/(4η_g), so ℓ = √(4η_g) ℓ_P.

**Prior art:**
- Jacobson (1995) and Sakharov (induced gravity);
- Srednicki and Bombelli–Koul–Lee–Sorkin (area law);
- Casini & Huerta (lattice entanglement);
- Donnelly & Wall and Kabat (gauge-field edge modes and contact terms);
- Dvali (species and the strength of gravity).

## A. Per-field coefficients: averaged like a horizon [computed]
A horizon is a coarse surface, not one lattice plane, so the coefficient was computed for the cubic plane families and for both inequivalent (111) gaps, and averaged. The computation is exact for Gaussian states with two cuts per slab.
- Positions were weighted by gap width: a plane at a random position in (111) falls in the wide gap ¾ of the time.
- Families were weighted 3 : 6 : 4 for (001) : (110) : (111).

| Surface | grains cut per ℓ² | scalar η_g | grain Dirac fermion η_g |
|---|---|---|---|
| (001) | 0.750 | 0.0288 | 0.360 |
| (110) | 0.530 | 0.0253 | 0.327 |
| (111) narrow gap | 1.299 | 0.0416 | 0.457 |
| (111) wide gap | 0.433 | 0.0218 | 0.295 |
| (111), position-weighted | 0.650 | 0.0268 | 0.336 |
| **horizon average** | 0.618 (isotropic geometry: 0.650) | **0.0266 (N_ent 2.0)** | **0.337 (N_ent 25.4)** |

**Robust:** per unit area the fermion coefficient varies by only 10% between orientations. The single-cut (001) value used before (0.360) was ~7% high.

## B. Field content of the current grain theory
| Sector (how the current theory builds it) | η_g | N_ent |
|---|---|---|
| **Fermions:** each Standard-Model Weyl field plus its lattice-forced mirror is one grain Dirac field; 16 per generation (ν^c required by the anomaly argument); 3 X-valleys = 3 generations, so **16 fields** | 5.40 | **407** |
| **Gauge bosons:** spin-ice light (2) + SU(2) rishon links (6) + SU(3) rishon links (16) polarisations, free-field proxy | 0.64 | **48** |
| Higgs: *not yet built* in the grain theory (4 real scalars if added) | (0.11) | (8) |

## C. The grains' own Gauss-law (edge) entanglement [computed]
- The electric flux crossing a surface is a classical label shared by both sides. In gauge theories this "edge" term is part of the horizon entropy (Donnelly–Wall).
- For the spin-ice U(1) it was computed by Monte Carlo: 30,000 ice-rule states of a 1,024-grain diamond, 64 grains crossing a plane, with block entropies of up to 12 neighbouring cut grains.
- **Result: 0.60 nats per cut U(1) grain** (0.69 = ln 2 for a single grain; the ice rule correlates neighbours).
- With 1–4 U(1) grains per relation (the earlier coupling estimate), this adds **N_ent 28–112**.
- For the SU(2)/SU(3) rishon bundles only bounds are available, from 0 up to n ln 2 per cut relation (n ≤ 37), i.e. up to +1,190.

## Result
| Case | η_g | **N_ent** | ℓ | M = ħc/ℓ |
|---|---|---|---|---|
| fields only (minimal content) | 6.03 | 455 | 4.91 ℓ_P | 2.49×10¹⁸ GeV |
| **fields + computed U(1) edge (central)** | **6.41** | **483** | **5.06 ℓ_P = 8.2×10⁻³⁵ m** | **2.41×10¹⁸ GeV** |
| fields + U(1) edge with 4 U(1) grains | 7.52 | 567 | 5.49 ℓ_P | 2.23×10¹⁸ GeV |
| valleys ≠ generations (48 fermion fields) + U(1) edge | 17.2 | 1,297 | 8.29 ℓ_P | 1.47×10¹⁸ GeV |
| everything + full non-abelian edge (upper bound) | 23.4 | 1,762 | 9.67 ℓ_P | 1.26×10¹⁸ GeV |

**Derived: N_ent ≈ 480 (455–570 for the content the theory currently builds), so ℓ ≈ 5 ℓ_P and M ≈ 2.4×10¹⁸ GeV.**
- The earlier single-cut count (495) is confirmed to within 3%. Everything built on it (the audit, rishon splitting, the light-sector window) stands; the universe-size formula shifts by +2%.
- **What dominates:** the fermions (~85%). The number is essentially "16 grain Dirac fields × 25 each".
- **What could move it:**
  1. whether the 3 valleys really are the 3 generations (if not, ×2.7);
  2. how much edge entropy the non-abelian rishon bundles carry (unknown; at most ×3.6).

> **Follow-up (`CCEF_valleys_edges.md`):**
> - Valleys = generations passes a structural test, so the minimal fermion count stands.
> - The SU(2)/SU(3) bundles carry ≈ 10–13 nats of edge entanglement per cut relation (estimated rather than bounded). That adds 395–600, giving **N_ent ≈ 880–1,080, M ≈ 1.6–1.8×10¹⁸ GeV**.
> - The reduced-Planck coincidence below no longer holds.

## Intriguing (numerology, not evidence)
- **The derived M = 2.41×10¹⁸ GeV is within 1% of the reduced Planck mass** M_P/√(8π) = 2.435×10¹⁸ GeV.
- Exact equality needs N_ent = 48π² ≈ 474, which lies inside the derived range (455–570).
- The range is far wider than the match, so it is recorded only as a coincidence.

## Caveats
- **Gauge bosons are free-field proxies** (2 scalars per gauge boson); real lattice gauge fields differ in detail.
- **The U(1) edge entropy uses the classical ice ensemble** (equal-weight ice states), an approximation to the quantum spin-ice ground state.
- **Jacobson's premises are assumed**, and whether edge terms belong in η_g is the Kabat / Donnelly–Wall question, answered "yes" here.
- **The fermion count rests on two features of the current construction:** mirrors forced by the lattice, and valleys as generations. The first is a theorem (Nielsen–Ninomiya); the second is a conjecture.

## Verdict
- **From the current grain theory alone: N_ent ≈ 480** (455–570), the grain length ℓ ≈ 5 Planck lengths, and the grain scale M ≈ 2.4×10¹⁸ GeV.
- It is dominated by the 16 grain Dirac fields that the theory's own chirality construction requires.
- The two things that could still change it substantially are whether the valleys are the generations, and the non-abelian edge entropy.
