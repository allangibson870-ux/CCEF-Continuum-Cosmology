# From one global clock to a clock at every junction (2026-10-12)

**Code:** `ccef_local_time.py` → `ccef_local_time_output.txt`.

**Why this was needed:** `CCEF_graviton.md` found that the grains' metric fluctuations carry the 2 graviton polarisations plus one unstable scalar mode. Einstein's theory removes that mode with a *local* time constraint (one per point), whereas CCEF had a single global Page–Wootters constraint. Local time is what relativity already requires (no universal "now"); it was not a stated assumption of the author.

**Prior art:**
- Dirac's constraint analysis and ADM;
- "geometrodynamics regained" (Hojman, Kuchař & Teitelboim 1976): consistency of local time-relabellings essentially forces Einstein's equations;
- Tomonaga–Schwinger many-fingered time;
- Page–Wootters; Höhn et al. (relational dynamics);
- causal sets; quantum cellular automata with emergent Lorentz covariance (Bisio, D'Ariano & Perinotti); quantum causal graph dynamics (Arrighi);
- Wolfram-model causal invariance (Gorard 2020);
- consistent / perfect discretisations (Gambini & Pullin; Dittrich).

## A. What a local clock does for gravity [computed]
| Time structure | Physical modes of the grain metric field |
|---|---|
| coordinate freedom only | 2 helicity-2 waves (ω² = +0.25k²) + 1 helicity-0 mode, **unstable** (ω² = −0.25k²) |
| + one **global** clock (Page–Wootters) | **unchanged**: a single constraint acts only on the uniform K = 0 mode |
| + a **local** clock at every point (linearised Hamiltonian constraint) | **exactly 2 helicity-2 waves, stable, ω ∝ k: the graviton and nothing else** |

**Newton's law lives in the local clock constraint.** With matter, the local constraint reads K_iK_j h_ij − K² tr h = 16πGρ. For a point mass it gives:

| r | Φ (computed) | Newton −GM/r |
|---|---|---|
| 1 | −1.00 | −1.00 |
| 2 | −0.51 | −0.50 |
| 4 | −0.24 | −0.25 |

(The ~2% differences are from numerical integration.) Newtonian attraction is the *constraint* part of gravity, not a wave.

## B. What local clocks require of the grains [computed]
1. **A smooth, continuous-time grain Hamiltonian cannot be split into consistent per-junction clocks.**
   - Local terms on neighbouring junctions do not commute (|[h_v, h_w]| = 1.4 for a ring of grains).
   - So the constraints C_v = p_v + h_v are mutually inconsistent: the lattice face of gravity's well-known "constraint algebra" problem.
2. **Dynamics as local *update events* makes local time automatically consistent.**
   - Grains update in local two-grain events, arranged by cause and effect (a brickwork / causal set).
   - Each junction's clock is simply **how many updates it has undergone**.
   - **Test:** 269 different update orders, all respecting cause and effect (equivalently, 269 different "global time slicings"), all give **the same final state** (differences ≤ 5×10⁻¹⁶). An order that violates cause and effect gives a different state (difference 1.48).
   - **The physical state depends only on each junction's own clock reading, never on a global time order.**

## What this means for CCEF
- **Grain dynamics should be formulated as local update events (a quantum causal structure), not a continuous-time global Hamiltonian.**
  - "Time" at a junction = the number of relational updates it has experienced.
  - The **causal order** of updates defines light cones.
  - Any global time is just one of many equivalent slicings.
- **This fits the framework's emergent-time principle (P4) more closely than the global clock did:** time made of relational events, with the Janus point's two arrows pointing away from the least-structured state along the causal order.
- **It removes the graviton's unstable mode and yields Newton's law** at the linearised level.

## Open
- **Recasting the existing grain Hamiltonian** (spin-ice light, rishon forces, geometry rewiring) as local update rules.
  - The seed-growth "template" moves are already event-like.
  - The quantum-cellular-automaton literature shows Weyl/Dirac particles with emergent Lorentz covariance can arise this way.
- **Showing that the coarse-grained update dynamics closes the full (non-linear) local-time algebra**, which by Hojman–Kuchař–Teitelboim would give full Einstein gravity, not just its linearised form.
- **Lorentz protection** (one light cone for all species) becomes a property of the causal update structure.

## Verdict
- **A single global clock cannot give a clean graviton; a clock at every junction can**, and it brings Newton's law with it (computed).
- At the grain level, consistent local clocks require the dynamics to be **local update events in a causal order**. Then local time is exactly consistent (tested), and each junction's time is just its count of relational updates.
- **This changes how CCEF's dynamics should be written:** as a quantum causal structure of grain updates rather than a continuous-time Hamiltonian.
