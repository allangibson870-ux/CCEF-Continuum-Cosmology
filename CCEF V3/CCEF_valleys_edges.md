# Two checks before rebuilding the electron: valleys as generations, and non-abelian edge entanglement (2026-10-12)

**Code:** `ccef_valleys_edges.py` → `ccef_valleys_edges_output.txt` (4 s).

## Part 1. Are the 3 X-valleys the 3 generations? [computed]
**What generations require:**
1. identical gauge charges;
2. independent masses;
3. mixing (CKM/PMNS) with a CP-violating phase;
4. ideally, compatibility with CCEF's strong-CP solution. That solution uses inversion: Hermitian mass matrices force θ̄ = 0 (`CCEF_strong_cp.md`).

Requirement 1 is automatic, since the valleys belong to one lattice field.

**The method:**
- The three valleys sit at different crystal momenta (X_x, X_y, X_z), so they can mix only if the vacuum is periodic on the 8-site simple-cubic cell rather than the 2-site diamond cell. In that cell all three valleys fold to k = 0: **12 zero modes, 3 valleys × 4 Dirac components**, cleanly separated by the primitive translations.
- The Dirac mass terms for 3 flavours were found as all Hermitian operators anticommuting with the three velocity matrices: **18 = 9 parity-even + 9 parity-odd**, as expected for 3 Dirac flavours.
- I then tested which of these local grain perturbations can reach: bond hoppings, spin-orbit-type, complex and spin-dependent bond terms, and on-site potentials and fields.

| Perturbations | Mass terms reached | Parity-even (A) | Parity-odd (B, the θ̄ direction) | Mixes valleys? |
|---|---|---|---|---|
| (a) uniform bond-direction distortions (diamond-periodic) | 3 / 18 | 3 / 9 | 0 | **no** (3 masses only) |
| (b) 8-site-periodic, inversion- and T-symmetric | 6 / 18 | 6 / 9 | 0 | **yes**: masses + mixing angles, no CP phase |
| (c) 8-site-periodic, inversion-symmetric, incl. complex (T-odd) couplings | 9 / 18 | **9 / 9** | **0** | **yes**: a general Hermitian 3×3 flavour matrix |
| (d) everything 8-site-periodic | 18 / 18 | 9 / 9 | 9 / 9 | yes |

**Reading:**
- **The valleys pass every structural test for generations.**
  - Local grain couplings can produce any mass and mixing pattern.
  - With inversion-symmetric couplings they produce exactly the **Hermitian** flavour matrices: three masses, three mixing angles and CP phases, while the parity-odd part, and hence **θ̄ = arg det M, stays exactly zero**.
  - That is the classic parity solution of strong CP (Babu–Mohapatra type), and it matches CCEF's own strong-CP result. CP violation in the CKM matrix and the absence of strong CP violation come out of the same symmetry.
- **There are exactly three generations because space has three axes:** one X-valley per spatial direction. This coincides with the independent "three" required by the ℤ₃ anomaly in Branch L₃.
- **Conditions found:**
  1. **Mixing needs the vacuum to break the diamond's translations down to the 8-site cubic cell**: a weak superstructure in the matter couplings, with amplitude of order the quark masses. Without it the mixing matrix is exactly the identity.
  2. **A CP phase needs complex (time-reversal-odd) couplings**, as it must, since CP violation is T violation.
- **Not explained:** the mass *hierarchy* (why 1 : 200 : 3,500), and the origin of the superstructure.

## Part 2. How much edge entanglement do the SU(2) and SU(3) bundles carry? [computed estimate]
- The flux crossing a surface is a shared label. For a non-abelian link it carries a representation R, contributing **H(p_R) + ⟨ln dim R⟩** per cut link (Donnelly; Donnelly–Wall).
- **Estimate:**
  1. **Electric fluctuations of the free lattice gauge field on the diamond** (hexagon plaquettes, exact Gaussian vacuum): ⟨Π²⟩ per link per colour component, **c_E = 0.853** (converged: 0.852 at L = 3, 0.853 at L = 4).
  2. At coupling g², ⟨E²⟩ = c_E/g² per component, so ⟨C₂(R)⟩ = dim(G)·c_E/g².
  3. p_R ∝ dim(R)² e^(−τC₂(R)), fixed by that mean and truncated to the link Hilbert-space sizes the forces need (`CCEF_nonabelian.md`: SU(2) ~200–1,500 states, SU(3) ~3×10⁴–6×10⁶).

| Group | g² | link states | H(p) | ⟨ln dim R⟩ | edge per cut link |
|---|---|---|---|---|---|
| SU(2) | 0.25–0.40 | 200–1,500 | 1.6–2.3 | 1.5–1.7 | **3.3–4.0** |
| SU(3) | 0.25–0.40 | 3×10⁴–6×10⁶ | 2.7–4.2 | 3.8–4.6 | **6.5–8.9** (smaller links cap the fluctuations) |

- **Per cut relation, SU(2) + SU(3) edge ≈ 9.7–12.9 nats.** The crude bound was 25.6.
- **This adds N_ent ≈ 395–600.** At the low end, neighbour correlations were taken into account using the spin-ice factor 0.87.

## Updated entanglement number
| Piece | N_ent |
|---|---|
| 16 grain Dirac fields | 407 |
| 24 gauge polarisations | 48 |
| U(1) (spin-ice) edge | 28 |
| **SU(2) + SU(3) edge (new)** | **395–600** |
| **Total** | **N_ent ≈ 880–1,080** |

**Grain length ℓ ≈ 6.8–7.6 ℓ_P; grain scale M ≈ 1.6–1.8×10¹⁸ GeV.** The non-abelian edge entanglement is the second-largest piece, almost as large as all the fermions together.

**Knock-on effects (computed from the earlier formulas):**
- **Axion** (rishon-diluted Λ* ∝ M): **m_a ≈ 210–235 μeV**, still inside the frozen band (14–400 μeV).
- **Finite universe under rishon splitting:** L ∝ N_ent^(−2/3).
  - *Corrected:* the photon-phase boundary is J±/J_zz ≈ 0.052 in this convention, not 0.104 (`CCEF_light_window.md`).
  - At that edge L ≈ 1.2–1.4 D_LSS, so **the rescue stays automatic wherever light exists**.
  - Relation: L ≈ 1.3 (x_c/x) D_LSS.
- The reduced-Planck-mass coincidence of `CCEF_nent.md` disappears (M is now ~30% below it).

## Caveats
- **The edge estimate makes several approximations:**
  - a Gaussian (free-field) vacuum with a heat-kernel form for p_R;
  - the coupling at the grain scale taken as g² = 0.25–0.40, with an unknown lattice-to-continuum matching factor;
  - link Hilbert-space sizes taken from the earlier coupling estimates.
- **Whether edge terms belong in gravity's η_g** is the Kabat / Donnelly–Wall question, answered "yes" here. If they are excluded, N_ent returns to ≈ 455.
- **The valley result is structural:** it shows that the needed couplings are available and symmetry-allowed. It does not derive their values, the mass hierarchy, or why the vacuum has the 8-site superstructure.

## Verdict
1. **Valleys = generations survives a real test.**
   - Local grain couplings give a fully general flavour structure.
   - With inversion symmetry, exactly the Hermitian mass matrices of the parity solution arise: CKM-type mixing and CP phases with θ̄ = 0.
   - Three generations = three spatial axes.
   - The price is an 8-site superstructure in the matter couplings (for mixing) and complex couplings (for the CP phase).
2. **The non-abelian bundles carry substantial edge entanglement:** ≈ 10–13 nats per cut relation. That raises **N_ent to ≈ 880–1,080 (M ≈ 1.6–1.8×10¹⁸ GeV)**.
   - The axion stays inside its frozen band (~220 μeV).
   - The rishon-splitting rescue now needs the photon sector at J±/J_zz ≲ 0.07 rather than anywhere in its phase.
