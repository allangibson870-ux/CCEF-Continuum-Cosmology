# Where gravity's stiffness comes from: geometry events vs. the fields on the grains (2026-10-12)

**Code:** `ccef_induced_gravity.py` → `ccef_induced_gravity_output.txt` (23 s).

**Question:** coarse-grained, do the geometry-rewiring events (`CCEF_geometry_events.md`) give the linearised Einstein (Fierz–Pauli) dynamics found to be unique in `CCEF_graviton.md`? And if so, what sets Newton's constant?

**Prior art:**
- Sakharov (induced gravity, 1967);
- Jacobson (1994 induced gravity and black-hole entropy; 1995 Einstein equation of state);
- Susskind & Uglum (1994), Kabat (1995: gauge-field contact terms);
- Bombelli, Koul, Lee & Sorkin (1986) and Srednicki (1993): entanglement area law;
- Kröner and Kleinert (defects as curvature: the "world crystal"); Kleinert & Zaanen (2004, world nematic crystal);
- Dvali (the species bound: many fields weaken gravity).

Citations are quoted from memory. Nothing below is a claim about nature.

## B1. A huge rewiring can cost nothing [computed]
- **The test:** slip a whole plane of the 216-junction diamond universe sideways by one lattice vector. That rewires all 36 grains crossing the plane (8% of all grains).
- **Result:** energy change **0.000**. All 216 junctions are still perfect, and every junction still has 4 grains.
- **Reading:** in a relational universe this is a change of coordinates (a large diffeomorphism), not a physical change. The geometry sector has **exact coordinate freedom**, the first ingredient of Einstein gravity.

## B2. Geometry defects do not feel each other at a distance [computed]
- One geometry defect (a flux-allowed switch) costs +36 in geometry units (angle-rule energy).
- Pairs of defects, interaction energy E₁₂ − E₁ − E₂:

| Separation (junction steps) | 0 | 1 | 2 | **3** | **4** | **5** | **6** |
|---|---|---|---|---|---|---|---|
| max \|interaction\| | 48 | 30 | 16 | **0** | **0** | **0** | **0** |

**Contact interaction only.** In a crystal of atoms, defects push on each other through long-range strain (~1/r³). A relational graph has no positions, hence **no elasticity**. Coarse-grained, the bare geometry energy is just (core energy) × (number of defects). It contains **no Einstein/Fierz–Pauli stiffness** and no gapless geometry waves of its own.

**So the geometry supplies the degrees of freedom and the coordinate freedom, but not the stiffness.**

## B3. The stiffness comes from the fields living on the grains [computed]
This is Sakharov's induced gravity in Jacobson's form:
- if the fields living on the grains have an entanglement area law S = η_g A/ℓ²,
- then local equilibrium gives Einstein's equations with **G = ℓ²/(4η_g)**;
- linearised, these are the unique Fierz–Pauli dynamics of `CCEF_graviton.md`.

η_g was computed exactly (Gaussian states, slab cut, two cuts, transverse momenta) on the diamond grain lattice. ℓ is the grain length.

| Transverse × depth (cells) | η_g scalar (one photon polarisation, proxy) | η_g grain electron (spin-½ Fu–Kane–Mele) |
|---|---|---|
| 6×6 × 6 | 0.0287 | 0.3587 |
| 10×10 × 8 | 0.0289 | 0.3599 |
| 14×14 × 10 | 0.0290 | 0.3603 |

**A clean area law, converged.** On the grain lattice the coefficient is finite and computable. The grains themselves are the cutoff, so there is no ultraviolet infinity.

| Content | N_eff = 24π η_g |
|---|---|
| one scalar (one photon polarisation, proxy) | 2.18 |
| the grain electron | 27.2 |
| photon (2 polarisations) + grain electron | **31.5** |
| CCEF so far (assumed) | 9 |

## What this means for CCEF
1. **Gravity is induced.** Coarse-grained, the division of labour is:
   - **the grains provide the geometry and its coordinate freedom** (B1), plus local clocks (`CCEF_local_time.md`);
   - **the light and matter living on the grains provide gravity's stiffness**, through their entanglement (B3).

   The bare geometry energy contributes only local defect costs (B2). In this model, gravity really is "a combination of matter, mass and grains", as the author suggested, in the precise sense of Sakharov and Jacobson.
2. **The assumed N_eff ≈ 9 is too small.**
   - Light plus one grain electron already give N_eff ≈ 31.5 on the lattice. A full matter content (quarks, three generations, weak and strong force fields) would raise it further. This is the "species" effect: more fields, weaker gravity per grain.
   - Since ℓ = √(N_eff/6π) ℓ_P, N_eff ≈ 31.5 gives **ℓ ≈ 1.29 ℓ_P and M = ħc/ℓ ≈ 9.4×10¹⁸ GeV**, instead of 1.77×10¹⁹ GeV. M scales as N_eff^(−1/2).
   - **[OPEN]** Every number in the framework that uses M = 1.77×10¹⁹ GeV would shift by √(9/N_eff). The frozen pre-registrations are left untouched; this is recorded as an inconsistency to resolve.
3. **Linearised Einstein dynamics follow if Jacobson's premises hold** (local Lorentz symmetry and Unruh temperature, local equilibrium). The uniqueness argument of `CCEF_graviton.md` then fixes the linearised form, and the local-time result supplies the constraint (Newton's law).

> **Follow-up (`CCEF_neff.md`):** full content gives N_eff ≈ 495, so ℓ ≈ 5.1 ℓ_P and M ≈ 2.4×10¹⁸ GeV. Heavy fields, including the mirror partners, count fully.

## Caveats
- **The photon is approximated by massless scalars.** Real gauge fields carry extra "edge"/contact contributions (Kabat), and the grain qubits' own Gauss-law entanglement was not included.
- **The lattice area-law coefficient depends on the cut** (orientation, position) and on lattice details. Being finite and computable is the point; the exact value is not universal.
- **Jacobson's argument is assumed, not simulated.** No graviton wave was propagated through the event dynamics here.
- The geometry energy used is the angle-rule energy of `CCEF_geometry_groundstate.md`. Defect energies depend on that choice; the absence of long-range interaction does not.

## Verdict
- **Coarse-grained, the geometry events are pure geometry:**
  - exact coordinate freedom (a whole-plane slip costs 0);
  - only contact interactions between defects (zero beyond 2 steps), so no elasticity and no Einstein stiffness of their own.
- **The stiffness, Newton's constant, comes from the entanglement of the fields on the grains** (Sakharov–Jacobson). It is computed here as a converged lattice area law.
- **It implies N_eff ≳ 31 rather than 9,** which would lower the grain scale M to ≲ 10¹⁹ GeV. This is a real tension to carry forward.
