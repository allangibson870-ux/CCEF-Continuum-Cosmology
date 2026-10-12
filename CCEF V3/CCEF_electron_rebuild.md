# The grain electron, rebuilt as a bundle constituent (2026-10-12)

**Code:** `ccef_electron_rebuild.py` → `ccef_electron_rebuild_output.txt` (≈ 2.3 min).

**Why:** `CCEF_light_window.md` showed that electrons built as the bare charges of spin-ice light are, inside the photon phase:
- **too fast** (they hop at first order, J±; light is third order, J_ring); and
- **Mott-gapped** (the spin-ice charge energy acts as an on-site repulsion U/t ~ 20).

**Prior art:**
- quantum link models with dynamical matter (Wiese; Brower, Chandrasekharan, Wiese);
- Kogut–Susskind lattice gauge theory;
- quantum spin ice with matter (Hermele, Fisher, Balents);
- 0-flux vs π-flux quantum spin ice (Lee, Onoda, Balents 2012);
- Fu–Kane–Mele diamond model.

## The new rules
| Ingredient | Rule |
|---|---|
| Matter | fermions c_{v,s} at each junction (spin up/down): separate constituents of the relation bundles, qubit-encoded as before (P7: still one grain type) |
| Light | spin-ice grains, E_l = S^z_l (oriented A → B), ring exchange around hexagons (unchanged) |
| **Gauss law** | **G_v = div E − (n_v − 1) = 0.** Matter charge carries its own flux. The old J_zz term becomes J_G Σ G_v², which penalises only Gauss *violations* |
| Hop | −t c†_{w,s} S⁻_l c_{v,s} + h.c.: the charge moves together with its flux. **t is the constituent's own coupling, no longer J±** |
| Spin–orbit | Fu–Kane–Mele second-neighbour hop, made gauge-covariant (it carries the two link variables along its path) |
| What happens to the old spin-ice charges | still exist as pure Gauss violations, with energy ~J_zz ≈ 590 J_ring at the photon edge: very heavy, not the electron |

## Results [computed]
### 1. Exact gauge invariance; the on-site repulsion is gone
Exact check on one hexagonal ring (6 junctions, 6 grains, spin-½ matter; 2¹⁸ states):
- [H_hop, G_v] = 0 and [H_ring, G_v] = 0 exactly.
- 730 physical states; 602 of them have a doubly occupied junction, and **J_G ΣG² = 0 on every one**.
- Under the old rule, the same states cost 2.4 J_zz on average.

**The light sector no longer repels two electrons on one junction.**

### 2. The leftover Coulomb repulsion is far below the Mott threshold
Photon exchange gives U_eff/t = 4α·G(0)/C. Here G(0) = 0.446 and C = 0.266 are the diamond lattice Coulomb Green function at the origin and its large-distance coefficient.

| α | U_eff/t | Mott threshold |
|---|---|---|
| 0.08 (spin ice's natural value) | 0.54 | ≳ 5 |
| 0.013 (hypercharge) | 0.09 | |
| 1/137 | 0.05 | |

**The electron stays a free, light Dirac particle at any realistic coupling.**

### 3. Masslessness depends on the light's background flux
Spin-½ Fu–Kane–Mele with gauge-covariant hops was run on a diamond torus at L = 4 and 6, with twisted boundaries.

| Background | exact zero modes | states below \|E\| = 0.02 / 0.05 / 0.1 / 0.2 | verdict |
|---|---|---|---|
| **0-flux (unfrustrated spin ice)** | **12 = 3 Dirac points × 4** (L = 4 and 6) | 0 / 0 / 0 / 0 | **relativistic** |
| π-flux (frustrated spin ice) | 40 (L = 4), 32 (L = 6) | 0.2% / 0.6% / 2% / 6% | **not relativistic** (finite density of low-energy states, N(E) ~ E^1.1–1.6) |

- **The electron is relativistic only in zero-flux spin ice.**
- CCEF's grain Hamiltonian writes −J±(σ⁺σ⁻ + h.c.) with J± > 0, which is exactly the unfrustrated, zero-flux sign. It is also the sign for which the photon phase is established by sign-free Monte Carlo.
- **A frustrated (π-flux) light sector would be ruled out.**

### 4. One light cone, made concrete
- The Monte Carlo photon speed is c = 1.49 a·g (Kato & Onoda), with a = 4 in these units and g = J_ring. The rebuilt electron's cone speed is 4t (Fu–Kane–Mele, λ/t = 1/4).
- **One light cone requires t ≈ 1.49 J_ring.**
- The matter hop is now an independent constituent coupling, so this is a single matching condition. Before, it was impossible: the old charges ran at ~31× light speed.
- Why nature would pick t ≈ 1.5 J_ring is the remaining **Lorentz-protection question [OPEN]**.

## What changes and what doesn't
- **Unchanged:**
  - the electron's band structure (3 Dirac valleys = 3 generations, with Klein-four masses and mixing via the 8-site superstructure, `CCEF_valleys_edges.md`);
  - the fermion count (16 grain Dirac fields), so N_ent is unchanged;
  - the strong-CP parity structure.
- **Changed:**
  - matter is a separate bundle constituent, coupled through an exact Gauss law;
  - the light sector must be zero-flux (already so in Ĥ);
  - the old spin-ice charges become very heavy non-electron excitations.

## Caveats
- **The gauge-invariance check is on one ring.** The Dirac test treats the light as a static background flux (mean field). Photon fluctuations at α ≈ 0.08–0.01 are weak (U_eff/t ≲ 0.5) but were not simulated.
- **The Mott threshold is mean field**, and the Coulomb estimate uses the lattice Green function with an O(1) lattice-to-continuum factor.
- **Chirality is still provided by the separate mirror-gapping construction** (`CCEF_chiral.md`), not shown together with this one.

## Verdict
**The electron is rebuilt:**
- a fermionic constituent of the relation bundle;
- coupled to the spin-ice light through an exact Gauss law;
- with its own hop.

It is **exactly gauge invariant** and has **no on-site repulsion from the light sector**. Its residual Coulomb repulsion is ≤ 0.5 t, far below the Mott threshold of ~5 t. It is **massless** (3 Dirac valleys) in the zero-flux background that CCEF's Hamiltonian already specifies. **One light cone needs a single matching, t ≈ 1.5 J_ring.**
