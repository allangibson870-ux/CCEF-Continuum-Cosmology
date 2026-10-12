# Geometry rewiring as local update events (2026-10-12)

**Code:** `ccef_geometry_events.py` → `ccef_geometry_events_output.txt` (≈ 2.3 min, one core).

**Why:** `CCEF_grain_rules.md` rewrote light, electrons and the gauge forces as local update events with a clock at every junction. The missing rule was the one that changes **space itself**: grains rewiring which junctions they join. In a grain universe the network *is* the geometry. A rewiring event therefore changes the very network that defines "neighbour", "local" and "before/after". This is the step the graviton and local-time results need (`CCEF_graviton.md`, `CCEF_local_time.md`).

**Prior art:**
- Arrighi & Martiel, quantum causal graph dynamics (unitary, causal evolution of a superposition of graphs);
- quantum graphity (Konopka, Markopoulou, Smolin), whose graph-rewiring Hamiltonians are the continuous-time cousin;
- degree-preserving "edge switches" in random-graph theory;
- Hardy's causaloid, Oreshkov–Costa–Brukner indefinite causal order, and Zych, Costa, Pikovski & Brukner ("Bell's theorem for temporal order"): causal order can itself be quantum when gravity/geometry is;
- causal sets (Bombelli, Lee, Meyer, Sorkin).

Citations are quoted from memory. Nothing below is a claim about nature. These are constructions and checks on a finite model.

## The rule

The state is a **superposition of grain networks**, each carrying the light (spin-ice) qubit on every grain:
|ψ⟩ = Σ amp · |network, fluxes⟩.

**Geometry event R(g₁, g₂):**
- **The move:** the local switch (a,b),(c,d) ↔ (a,d),(c,b) of two grains, where a, c are A-junctions and b, d are B-junctions.
- **When it is allowed:**
  - a and c share a neighbour (locality);
  - no double link would be created;
  - **the two grains carry the same electric flux** (gauge invariance; see result 1).
- **Reversibility:** the switch is its own inverse, so the event is the unitary e^(−i[[εE(G), θ],[θ, εE(G′)]]) on the pair {G, G′}. Here E is the local geometry energy (4-cycles penalised, 6-rings rewarded) counted through the two grains. That equals the change of the total energy.

**Light events** (ring flips) now apply only **if their six grains currently form a ring** in that branch, so light follows the geometry.

Every rule keeps:
- 4 grains per junction;
- the bipartite (A/B) structure;
- no double links;
- unitarity.

## Results [computed]
Setup: a diamond universe with 216 junctions and 432 grains, in a random ice-rule light state (2-in/2-out at every junction).

### 1. The rules are kept exactly, and geometry must respect electric flux
| Check (14 events near one junction → 1,128 branches, 328 distinct geometries) | Result |
|---|---|
| Norm (unitarity) | 1.000000000000 |
| Branches breaking 4-grains-per-junction / bipartite / no double links | **0** |
| Largest electric charge created in any branch | **0** |
| Same switches but **flux-blind** (ignoring electric flux) | **67%** of the weight ends in branches with created charges |

**A rewiring event can only swap grains carrying the same electric flux.** Otherwise moving a grain's end carries its flux to a new junction and creates charge from nothing.
- In the diamond ice state this blocks **52%** of geometrically possible switches (2,808 of 5,832 allowed).
- **Geometry and light are not independent sectors:** the electric field constrains how space can rewire.
- One switch in perfect diamond costs ΔE = +6 to +10 (rings destroyed), so diamond is locally stable.

### 2. Reach
- A geometry event reads everything within 2 steps of its 4 anchor junctions (≈ 43 junctions), but writes only 2 grain ends.
- A light event reads and writes 6 grains.

**Geometry events have a much wider causal footprint than light events.**

### 3. The causal relation can depend on the branch of the geometry
240 pairs of events, all on different grains, acting on prepared superpositions of geometries:

| Footprints (a conservative light cone) | Pairs | Order matters in |
|---|---|---|
| never overlap | 135 | **0** (commute to 2×10⁻¹⁶) |
| always overlap | 101 | 43 |
| overlap in some branches only | 4 | 0 |

Checked branch by branch:
- order matters in no branch for 197 pairs;
- in every branch for 42;
- **in some branches only for 1**.

**So whether one event is "before" another can differ between superposed geometries.** It is rare at this coupling.

### 4. Slicing independence needs a causal order taken from the quantum geometry
Setup:
- 8 events (switches and light rings, all on different grains) in one neighbourhood;
- they act on a superposition of 4 geometries;
- the neighbourhood was chosen (after 44 tries) as one where the quantum geometry adds a causal link that the classical diamond does not imply.

| Causal order taken from… | Ordered pairs | Distinct slicings | Max state difference |
|---|---|---|---|
| grain labels only (the rule used for fixed geometry) | 0 | 149 | **0.55 (fails)** |
| the classical diamond: where order matters there | 5 | 144 | **2.1×10⁻³ (fails)** |
| the quantum state, self-consistently (where order matters in any branch reached) | 6 | 132 | **3×10⁻¹⁶ (exact)** |
| footprints (conservative light cone) | 10 | 49 | 3×10⁻¹⁶ (exact) |

What the table shows:
- **With changing geometry, local time stays consistent (slicing-independent) only if the cause-and-effect order is read from the quantum state of the geometry itself.**
  - Grain labels fail.
  - A fixed classical background fails.
- **The conservative light-cone rule always works but over-orders:** 49 vs 132 allowed slicings.
- **The failure of the classical order is small (2×10⁻³)** because the off-diamond branches carry little weight here, but it is not zero.

## What this means for CCEF
1. **The full grain rulebook is now local events.** Geometry, light, electrons and the gauge forces all evolve by local, reversible updates with a clock at every junction. Geometry events keep every rule exactly (unitarity, 4 grains per junction, Gauss law).
2. **Light constrains geometry.**
   - Space can only rewire between grains carrying equal electric flux.
   - So geometry and electromagnetism are coupled at the level of the rules, not added separately.
   - **[CONJECT]** This is a possible microscopic root of "matter/fields tell space how to change". It echoes the author's suggestion that gravity is a combination of matter, mass and grains, and the induced-gravity tradition (Sakharov, Jacobson).
3. **Cause and effect become part of the quantum state.**
   - When geometry is in superposition, the before/after relation between events can differ between branches.
   - The only slicing-independent rule tested reads the causal order from the state itself.
   - This is the grain-level version of the expectation (Hardy; Zych et al.) that quantum gravity has indefinite causal order. Here it shows up rarely and weakly, as a small effect.
4. **Unitary events cannot anneal space on their own.**
   - The classical seed-growth "template" moves (`CCEF_geometry_groundstate.md`) used a heat bath (Metropolis).
   - Reversible events conserve information, so crystallising a tangle into diamond must hand the tangle's energy and entropy to another sector: light and matter.
   - That is the reheating already estimated (`CCEF_reheat.md`, ~10¹⁹ GeV).
   - **This is an argument, not a simulation:** a unitary seed-growth run with the light sector as the sink has not been done.

## Caveats
- **Small universe; only a few events.** The coupling (θ = 0.6, ε = 0.1) and the energy (U₄ = K₆ = 1, no angle rule, no over-connection term) are illustrative, not the full geometry energy of `CCEF_geometry_groundstate.md`.
- **Branch-dependent causal links were rare** (1 in ~200 pairs; 1 neighbourhood in 44) and their effect was small (2×10⁻³).
- **The flux-matching rule is the simplest gauge-invariant choice.** Richer events (switch plus compensating ring flip) could open more moves.
- **The self-consistent causal order was built by sampling** many slicings until no new links appeared (12 quiet rounds). It is not a proof.

## Open
1. ~~Seed growth with light as the energy/entropy sink.~~ **Done** (`CCEF_microcanonical_growth.md`): it completes, and T_light = 12/c. A fully unitary template rule is still open.
2. ~~Coarse-graining to linearised Einstein.~~ **Partly done** (`CCEF_induced_gravity.md`): geometry gives coordinate freedom but no elasticity, so the stiffness is induced by the fields' entanglement (N_eff ≈ 31.5 computed). A propagating graviton in the event dynamics is not shown.
3. **Larger θ / longer runs:** how common does branch-dependent causal order become, and does it decohere?
4. Include the angle rule and over-connection term, and the electron and rishon sectors, in the same event order.

## Verdict
- **Built:** geometry rewiring as local, reversible update events on a superposition of grain networks.
- **Exact on every branch:** unitarity, the junction rule and the Gauss law.
- **Found:**
  - (i) geometry may only rewire grains carrying equal electric flux;
  - (ii) the cause-and-effect relation can differ between superposed geometries;
  - (iii) local time stays consistent only if the causal order is read from the quantum state itself. Grain labels and a classical background both fail (computed).
- **Not done:** unitary crystallisation with an energy sink, and the coarse-grained link to Einstein gravity.
