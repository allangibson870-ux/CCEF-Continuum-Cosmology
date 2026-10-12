# Crystallising space with energy conserved: light as the only sink (2026-10-12)

**Code:** `ccef_geo_microcanonical.py` → `ccef_geo_microcanonical_output.txt` (5,000 star moves; c = 1, 3, 9, 30) and `ccef_geo_microcanonical_long_output.txt` (15,000 star moves; c = 1, 1.5, 2, 3). Four cores, about 1.5 and 4 minutes.

**Why:**
- The seed-growth result (`CCEF_geometry_groundstate.md` §4c) used Metropolis at a fixed temperature, which assumes an outside heat bath.
- The grain rules are reversible local events (`CCEF_grain_rules.md`, `CCEF_geometry_events.md`), and nothing lies outside the universe.
- So when space crystallises, the energy it releases (~12 geometry units per junction) and the tangle's disorder must go into the universe's own light and matter. Can growth still complete under those terms, and how hot does it leave the light?

**Prior art:**
- Creutz's microcanonical "demon" Monte Carlo;
- the Kipnis–Marchioro–Presutti energy-exchange model;
- latent heat and recalescence in crystal growth (ordinary materials science);
- the reheating estimate of `CCEF_reheat.md`.

## The model
- **The light sector is the bath.** Every junction holds a light energy D_v ≥ 0 with c light modes, so the light temperature is T = ⟨D⟩/c.
- **A geometry move pays its energy change from (or into) the light in its own footprint.** This applies to both the star template (the same growth rule as before) and single swaps.
- **Acceptance is exact microcanonical:** min(1, ((P − ΔE)/P)^(k−1)), with P the light energy in the footprint and k = c × (junctions in the footprint). The light energy is then re-shared within the footprint.
- **Light events carry energy along grains** (energy-conserving random exchange).
- **Total energy (geometry + light) is conserved to 10⁻¹²** in every run.

**Start:** the tiny seed, one cubic cell of crystal in an otherwise fully tangled 1,728-junction universe (E/N = −0.03), with the light **cold** (T = 0). So the only energy available for uphill moves is what crystallisation itself releases.

## Results [computed]
| Light modes per junction c | After 1,250–1,875 star moves | Final light temperature | Long run (15,000 moves) |
|---|---|---|---|
| 30 | perfect diamond, E/N = −12.000 | 0.40 | — |
| 9 | perfect | 1.33 | — |
| 3 | perfect | 3.99 | perfect throughout |
| 2 | perfect | 5.99 | perfect throughout |
| 1.5 | perfect | 7.98 | perfect throughout |
| 1 | perfect | **11.97** | thermal defects come and go (98.6%, 97.7%, back to 100%); **no melting** |

1. **Space still crystallises from one seed when energy is conserved and light is the only sink.** The whole universe becomes perfect 3-D diamond in every run, as fast as with the outside bath (~1,000–2,000 star moves).
2. **Crystallisation reheats the light by exactly the energy it releases.** T_final = 11.97/c in geometry units: a 12-unit-per-junction latent heat poured into the light. This is the reheating step of the CCEF early universe, now produced by the dynamics rather than estimated.
3. **The crystal survives its own heat.** Even at c = 1, where the light ends as hot as the full crystallisation energy per junction, defects appear and heal but space does not melt. The large defect cost (+36 per switch with the angle rule) keeps them rare.
4. **Where the disorder goes:** the tangle's disorder ends up in the light, whose entropy rises from zero (a cold start) to c·ln(T) + const per junction. Space becomes perfectly ordered, and the arrow of time points from ordered geometry to hot light. This is the reversible-events argument of `CCEF_geometry_events.md`, now computed.

## Reading for the CCEF early universe
- The sequence is: one seed → a crystallisation front sweeps the universe → **all the released energy is in light (and later matter)** → a hot, radiation-dominated universe in perfect 3-D space.
- That is the "Planck-hot start" assumed elsewhere (`CCEF_reheat.md`), arising here self-consistently.
- **If the geometry energy unit is ~M, the light ends at T ~ 12M/c.** That is near-Planckian for any c of a few to tens, consistent with the earlier ~10¹⁹ GeV estimate (using the classical heat capacity of the light; quantum statistics would modify the numbers).
- **The crystallisation front is a natural place for the ΔB = 2 / CP-violating processes** needed for baryogenesis in Branch L₃ (`CCEF_baryogenesis.md`). Behind the front, the light is hot.

## Caveats
- **The star template is still the directed, non-equilibrium growth rule of §4c.** Only the acceptance changed, from outside bath to energy conserved. A fully reversible (unitary) template rule remains open.
- **The light is a classical heat reservoir with c modes per junction**, not the spin-ice photon itself.
- **Energy units are the geometry couplings** (K = 1, U = 8, W = 4, angle rule). The mapping to GeV assumes the geometry unit is ~M.
- **"No melting" is on the run's timescale** (15,000 star moves plus 45,000 single swaps); earlier work found strong hysteresis.

## Verdict
- **With energy strictly conserved and light as the only sink, one seed still turns the whole universe into perfect 3-D space.**
- **Crystallisation pours its full latent heat into light**: T = 12/c in geometry units, Planck-hot if the unit is ~M. It does so without melting the crystal it made.
- **The hot early universe is the crystallisation's own heat, computed.** The remaining non-reversible ingredient is the directed template rule itself.
