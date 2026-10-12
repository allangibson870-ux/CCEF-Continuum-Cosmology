# The grain rules rewritten as local update events (2026-10-12)

**Code:** `ccef_grain_rules.py` → `ccef_grain_rules_output.txt` (about 25 s on one core).

**Why:** `CCEF_local_time.md` found two things:
- A clock at every junction removes the graviton's unstable mode and gives Newton's law.
- Consistent per-junction clocks are impossible for a smooth, continuous-time Hamiltonian. They are automatic when the dynamics is a set of **local update events** arranged by cause and effect.

So the grain Hamiltonian (light, electrons, weak/strong forces, geometry) has to be rewritten as a rulebook of local events.

**Prior art:**
- quantum cellular automata and quantum walks (Bisio, D'Ariano & Perinotti: Weyl/Dirac automata with emergent Lorentz covariance; Arrighi: quantum causal graph dynamics);
- Floquet / Trotter circuits for lattice gauge theories (the Gauss law is kept exactly by gauge-invariant gates);
- Wolfram-model causal invariance (Gorard 2020);
- causal sets (Bombelli, Lee, Meyer & Sorkin): random sprinkling as the route to Lorentz invariance;
- symmetric (Strang/palindromic) Trotter splitting.

Nothing below is a claim about nature. It is a reformulation together with checks on small systems.

## The rulebook

A **junction's clock** is the number of update events it has taken part in. An event may fire once every earlier event sharing a grain with it has fired: that is the **causal order**. No global time exists. Any listing of all events consistent with the causal order is one "slicing", and all slicings are equivalent.

| Event | Acts on | Update | Conserves | Status |
|---|---|---|---|---|
| **Light (ring)** | the 6 grains of one hexagonal ring | U = exp(−iεJ(O_h + O_h†)), O_h = σ⁺σ⁻σ⁺σ⁻σ⁺σ⁻ around the ring | Gauss charge at every junction (electric charge) | **tested here** |
| **Electron hop** | one bond (2 junctions); junctions update their 4 bonds in 4 "bond-direction" layers | exp(−iε h_bond), with Bravyi–Kitaev-dressed hops | fermion number; gauge charge | **tested here** (band level) |
| **Spin–orbit** | the next-nearest pairs, in 6 layers grouped by direction | exp(−iε h_SOC) | as above; time-reversal | **tested here** (band level) |
| **Weak / strong ring** | one ring of rishon-carrying relations | exp(−iε (plaquette)) | SU(2) / SU(3) Gauss law | inherited: the plaquette commutes exactly with the generators (`CCEF_nonabelian.md`), so its exponential does too |
| **Weak / strong hop** | one bond with its rishon pair | exp(−iε (gauge-covariant hop)) | as above | inherited, same argument |
| **Mirror gapping** | one junction (its 16 Weyl modes) | exp(−iε (Fidkowski–Kitaev / SMG quartic)) | all anomaly-free symmetries | design only (`CCEF_chiral.md`) |
| **Higgs / Yukawa** | one junction and its links | exp(−iε (Yukawa + Higgs-link term)) | gauge charges | design only |
| **Geometry rewiring** | a junction "star" (the template moves of `CCEF_geometry_groundstate.md`) | a unitary that mixes a star with its rewired version | the 4-grains-per-junction rule; Gauss law if both grains carry equal flux | **built**: `CCEF_geometry_events.md` |

The gauge sectors share one rule: **a gate built by exponentiating a gauge-invariant local term keeps the gauge law exactly.** So every force that already has a gauge-invariant grain Hamiltonian carries over to events with no extra work.

## Results [computed]

### 1. Light events keep electric charge exactly
- Setup: a periodic diamond patch with 8 junctions, 16 grains (a 2¹⁶ state space) and 96 six-rings.
- All 96 ring events conserve the Gauss charge at every junction. Maximum violation: **0** (exact).

### 2. Causal invariance with real light events
Eight ring events: 3 pairs are disjoint (they share no grain) and 25 pairs overlap. The initial state is a random state.

| Test | Result |
|---|---|
| Every update order that respects cause and effect (4 distinct orders here) | **same final state** (difference 5×10⁻¹⁸) |
| Reverse one overlapping pair, violating cause and effect | **23 of 25** reversals change the state (largest difference 0.04) |

The physics depends only on each junction's own clock, not on any global time.

Caveats:
- The patch is small, so only 4 distinct slicings exist. The earlier brickwork test (`CCEF_local_time.md`) had 269.
- The differences are small (0.04) because a ring update only acts on ice-rule configurations, which are a small part of a random state.
- 2 of the 25 overlapping pairs happen to commute.

### 3. The electron survives discrete time and stays massless
The grain Dirac electron (spin-½ Fu–Kane–Mele, `CCEF_grain_electrons.md`) is evolved in steps of size ε by update layers:
- The diamond's **4 bond directions are 4 natural layers**. Each one is a perfect matching: every junction updates exactly one of its bonds per layer.
- Six spin–orbit layers are added.

Three ways of ordering the layers were tested:
- sequential: one fixed order;
- symmetric: a palindromic half-step;
- random: a fresh order each step, averaged.

**Is the Dirac point (the 4-fold zero at X) still massless? Yes, exactly (≤10⁻¹⁶), for every step size and every order.** Discrete local updates do not give the electron a mass.

Cone speeds (the continuous-time value is 4.00):

| ε | sequential v_x / v_y (anisotropy) | symmetric | random order |
|---|---|---|---|
| 0.05 | 3.99 / 3.80 (5.1%) | 3.99 / 4.00 (0.17%) | 3.98 / 3.98 (0.10%) |
| 0.10 | 3.97 / 3.61 (10%) | 3.97 / 4.00 (0.67%) | 3.93 / 3.94 (0.25%) |
| 0.20 | 3.89 / 3.29 (18%) | 3.89 / 4.00 (2.7%) | 3.75 / 3.78 (0.72%) |
| 0.40 | 3.59 / 3.14 (14%) | 3.59 / 4.01 (11%) | 3.15 / 3.24 (2.9%) |

How each ordering's anisotropy scales with step size:
- **A fixed order picks out directions.** The anisotropy grows about linearly with step size (∝ ε).
- **Symmetric ordering** removes the linear term (∝ ε²).
- **Random ordering** is the most isotropic at every step size tested.

The random-order column averages the effective Hamiltonian over 120 random orders. That is a first-order estimate, not an exact random-circuit treatment.

## What this means for CCEF
- **The grain theory can be written entirely as local update events.**
  - Electric charge, and by inheritance the weak and strong gauge laws, are kept exactly.
  - Time at each junction is its update count, and the physics is independent of slicing.
- **The electron's masslessness is robust to discrete time.** It is protected by the lattice symmetry, not by the time-continuum.
- **Discrete time costs isotropy unless the update order is symmetric or random.** This links directly to the open Lorentz-protection problem (one light cone for all species):
  - A fixed update schedule acts like a preferred frame. It makes the speed of light depend on direction at order ε.
  - That is ruled out unless ε is tiny, since experiments bound direction-dependent electron/photon speeds extremely tightly.
  - Random update orders, in the spirit of causal-set sprinkling, suppress it.

**[CONJECT]** The grain universe has no global clock, so it has no fixed schedule. Its update order is set by the causal structure alone. If that structure is effectively random at the grain scale, isotropy would follow rather than having to be imposed. This is untested beyond the band-level check above.

## Open
1. **Geometry events:** turn the classical star rewiring into unitary events that change the causal graph itself (Arrighi-style quantum causal graph dynamics). This is the hardest piece.
2. **Same light cone for all species** under one shared event order (photon ring events and electron hop events interleaved), including the photon's own speed anisotropy.
3. **Physical step size:** is ε a free parameter, or is it fixed (e.g. ε ~ 1 in Planck units, as in quantum cellular automata)? With ε ~ 1, isotropy has to come from randomness or symmetry, not from smallness.
4. **Closing the non-linear local-time algebra** (Hojman–Kuchař–Teitelboim) for the coarse-grained event dynamics, which would give full Einstein gravity.
5. **Larger causal-invariance tests** on patches with many disjoint events (a reduced register of build(2)).

## Verdict
- **Done:** the grain rules have been rewritten as local update events with junction clocks.
- **Checked:**
  - exact charge conservation for light;
  - slicing independence for real light events;
  - an exactly massless Dirac electron under discrete bond-direction updates.
- **Found:**
  - fixed update orders make space direction-dependent, at order ε;
  - symmetric and especially random orders largely remove this.
- **Not done:** geometry-changing events, and a joint light-plus-electron event order.
