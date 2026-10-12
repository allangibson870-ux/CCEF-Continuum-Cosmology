# The graviton from grains (2026-10-12)

**Code:** `ccef_graviton.py` → `ccef_graviton_output.txt` (exact linear algebra).

**Prior art:**
- emergent linearised gravitons in lattice models (Gu & Wen 2006; Xu 2006);
- rank-2 tensor spin liquids, including on the **pyrochlore lattice the grains form** (Benton, Jaubert, Yan & Shannon 2016);
- fracton gravity (Pretko 2017);
- "world-crystal" / quantum-liquid-crystal gravity (Kleinert; Beekman, Nissinen, Wu & Zaanen 2017);
- WTDiff / unimodular gravity (Álvarez, Blas, Garriga & Verdaguer 2006);
- Fierz–Pauli 1939; ADM; DeWitt 1967.

## Why grains give a tensor field with diffeomorphism gauge symmetry [argument]
- In a crystal, displacing atoms is physical: there are phonons with 3 polarisations (helicity 0 and ±1), not gravitons.
- Grains, however, are **relational**: there is no background space in which a junction "sits". Shifting junctions while keeping all relations is **not physical**; it is a gauge redundancy.
- So the would-be phonons become **pure gauge (diffeomorphisms)**, and what remains physical is the coarse-grained **metric fluctuation h_ij**: the density and orientation of relations.
- Background independence (P3) is exactly what turns a crystal's sound into gravity's gauge structure.

## Which energy, which waves? [computed]
- **Setup:** a symmetric tensor h_ij with a positive "electric" kinetic term (as any qubit/grain model has) and the most general first-derivative energy, V = a K²(h·h) + b |K·h|² + c (K·h·K) tr h + d K² (tr h)².
- **Method:**
  - find every V invariant under the candidate symmetry;
  - count the physical plane-wave modes;
  - check each mode's helicity, stability and dispersion.

| Symmetry | Invariant V (a, b, c, d) | Physical modes |
|---|---|---|
| **DIFF** (all coordinate changes) | **(¼, −½, ½, −¼): exactly the Fierz–Pauli / linearised Einstein potential, and the only one** | **2 helicity-2 waves, ω ∝ k (the graviton)**; 1 helicity-0 mode with ω² < 0 (**unstable**) |
| **TDIFF + Weyl** (volume fixed: unimodular / WTDiff) | (¼, −½, ⅓, −5/36): the WTDiff potential, unique | 2 helicity-2 waves, ω ∝ k; 1 helicity-0 mode, unstable |
| DIFF + Weyl | **none** | no relativistic dynamics at all |

**Reading:**
1. **The graviton emerges automatically.** Any background-independent tensor sector of the grains has *exactly* the linearised Einstein energy (or its unimodular twin) as its only first-derivative dynamics. Its propagating waves include **exactly two helicity-2, linearly dispersing (relativistic) polarisations: the graviton.** The search rediscovered Einstein gravity unaided.
2. **The catch: one extra scalar mode, unstable.**
   - With the positive-definite kinetic energy a grain (qubit) model naturally has, the helicity-0 "conformal" mode has negative energy. This is the lattice version of gravity's famous **conformal-factor problem**.
   - In Einstein's theory this mode is removed by the **Hamiltonian constraint**: a *local* time-reparametrisation invariance ("many-fingered time", one constraint per point of space).
3. **What this demands of CCEF.**
   - CCEF's time is relational, built on Page–Wootters' **single global** constraint Ĥ|Ψ⟩ = 0.
   - **A clean graviton requires promoting it to a *local* constraint at every junction:** each junction is its own clock, and time can be re-labelled independently everywhere. With that, only the 2 graviton polarisations remain (linearised GR's reduced phase space).
   - This is a sharp new requirement, and it fits the user's emergent-time picture naturally: time read from *local* correlations, not one master clock.
4. **The unimodular link.** CCEF counts 4-volume by grains (the origin of its dark energy). That is exactly unimodular gravity. Its gravitons are the same 2 helicity-2 waves, and it is the form in which the cosmological constant becomes a free integration constant: consistent with CCEF's dark-energy picture.

## Status
| Piece | Status |
|---|---|
| Diffeomorphism gauge symmetry from background independence | argued (relational grains) |
| Unique linearised-Einstein energy; 2 helicity-2 relativistic waves | ✅ computed |
| Removing the unstable helicity-0 mode | ⚠️ requires a **local** time-reparametrisation constraint at each junction (not yet in the grain Hamiltonian) |
| A microscopic grain Hamiltonian producing h_ij | ⚠️ prior art (rank-2 pyrochlore spin liquid, Gu–Wen rotor model) shows it is possible on this lattice; not built here |
| Graviton speed = light speed; universal coupling to all energy (equivalence principle) | ❌ open (same Lorentz-protection issue; universality not shown) |
| Consistency with CCEF's Jacobson thermodynamic gravity | compatible: both give Einstein's equations at long wavelengths |

## Verdict
- **Gravitons do emerge from grains**, in a strong sense. Once the grains are background-independent, the only possible relativistic dynamics for their metric fluctuations is **linearised Einstein gravity**, and it carries exactly the graviton's two polarisations.
- **The price** is one unstable scalar mode, which Einstein gravity removes with *local* time-reparametrisation. **CCEF's global relational time must become local**: every junction a clock.
- **This is now the single clearest requirement on the grain dynamics for gravity.** It ties the graviton directly to the theory's picture of emergent time.
- **Predictions are unchanged:** gravitational waves travel at c with no dispersion and two polarisations (`CCEF_GW_check.md`). Any extra (scalar) polarisation would indicate the local constraint is broken.
