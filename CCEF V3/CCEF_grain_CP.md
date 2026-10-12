# Can grains carry CP violation? (2026-10-12)

**Code:** `ccef_grain_cp.py` → `ccef_grain_cp_output.txt` (exact calculations on a 4-grain junction, plus phase counting). Follows `CCEF_baryogenesis.md`, where the only surviving matter–antimatter route in Branch L₃ needs grain-level CP violation.

## Symmetries at the grain level
| Symmetry | Grain-level action (spin-ice sector) |
|---|---|
| C | σˣ on every grain (emergent electric field and charge flip sign) |
| T | complex conjugation in the σᶻ basis (antiunitary) |
| P | an improper geometric map (at one junction: a mirror swapping two grains) |

Emergent Lorentz invariance plus locality gives CPT, so **CP violation ⇔ T violation**. Edge phases that are pure gauge (φ_ij = α_i − α_j) can be removed by rephasing grains. **Only the flux through each triangle of grains is physical.**

## Results
**1. The grain Hamiltonian as written (v1) has no CP violation [computed].** All its couplings are real, so C, P and T are each conserved. Pure-gauge phases change nothing; any net flux through a triangle of grains breaks T, and hence CP.

**2. Junction couplings can carry irremovable phases [counting].**
- The quark junction (Yukawa) amplitudes carry (N−1)(N−2)/2 CP phases: 0, 0, **1**, 3 for N = 1, 2, **3**, 4.
- **Branch L₃'s anomaly condition forces N = 3, exactly the minimum for one Kobayashi–Maskawa phase.**
- That phase is known to be far too weak for baryogenesis.
- The **ΔB = 2 six-quark junction** has many complex flavour coefficients with 3 generations. Only one overall phase can be removed (baryon-number rephasing), so **new CP phases at Λ* are allowed and unconstrained.** These are the ones the front mechanism would use.

**3. A genuine grain-level CP-odd coupling exists: junction chirality [computed].**
- The scalar chirality of a junction, χ = Σ_faces S_i·(S_j × S_k), is **C-even, P-odd, T-odd, i.e. CP-odd** (checked exactly).
- With the *frustrated* sign of grain exchange (J_± < 0), a single junction's ground state is a **2-fold doublet with χ = ±√3**: two mirror-image ground states. With the unfrustrated sign the ground state is unique and has χ = 0.
- A three-grain chiral coupling λ·χ splits the doublet **linearly** and picks a handedness: λ = 10⁻⁴ already selects χ = −√3, with the sign following λ.
- **Edge phases alone cannot do this.** A junction's four faces form a closed surface, so their fluxes cancel in total. Only a genuine three-grain term can bias the overall handedness.

**4. Other sources:**
- the QCD θ angle (relaxed to zero by the axion; useless at T ~ Λ*);
- a hypercharge θ-term (affects only monopoles, via the Witten effect).

## Two ways CP violation could enter, and what each implies
| Route | Origin | Sign across the universe | Status |
|---|---|---|---|
| **Explicit** | complex phases in the ΔB = 2 junction, or a three-grain chiral term λ·χ in Ĥ | the same everywhere automatically | allowed; not derived (new parameters) |
| **Spontaneous** | frustrated grain exchange → each junction has a chiral doublet; the network or the front could order with one handedness | **set by the seed**: one seed → one sign; several seeds → matter/antimatter domains (excluded) | possible in principle; whether the lattice orders chirally is **not shown** (π-flux quantum spin ice is reported to stay T-symmetric; from memory) |

## Constraints
- Any CP violation beyond Kobayashi–Maskawa must be invisible today. Electric dipole moments are tiny: electron < ~4×10⁻³⁰ e·cm, neutron < ~2×10⁻²⁶ e·cm (quoted from memory).
- So a grain chiral coupling must be **active only at the geometrogenesis front**, or be suppressed at low energy (e.g. by powers of E/Λ*).
- In the spontaneous route, the chiral order would have to melt once the Coulomb phase forms.

## Lattice test: does the network pick one handedness? [computed, 2026-10-12]
**Code:** `ccef_grain_chirality.py` → `ccef_grain_chirality_output.txt`.

**Setup:**
- 16-grain periodic pyrochlore cluster (8 junctions); the grains' light sector as a spin-½ XXZ model (Gauss law + exchange); exact Lanczos ground state;
- cooling via thermal pure quantum states (6 random vectors);
- chiral structure factors S = ⟨Z²⟩/(8⟨χ_t²⟩), where Z is the summed (uniform, CP-odd) or staggered (CP-even) junction chirality. **1 = independent junctions, 8 = all locked.**

| J_± | ⟨χ_t²⟩ (each junction) | Uniform S, ground state | Staggered S, ground state | On cooling |
|---|---|---|---|---|
| +0.05 (unfrustrated) | 0.41 | 0.22 | 0.22 | 1.0 → 0.33 at T = 0.02 |
| −0.05 (frustrated) | 1.39 | 0.04 | 0.04 | 1.0 → 0.61 |
| −0.15 | 1.74 | 0.01 | 0.01 | 1.0 → 0.02 |
| −0.50 (Heisenberg point) | 1.88 | 0.01 | 0.01 | 1.0 → 0.01 |

**Reading:**
- Individual junctions are strongly chiral when frustrated (⟨χ²⟩ up to 1.9).
- But as the network cools through its ring-exchange (light switch-on) scale, their handedness becomes **strongly anti-correlated and cancels**. The net chirality goes to ≈ 0, below even the uncorrelated value of 1.
- Ground states are unique and gapped (gap 0.04–0.37), with no quasi-degenerate "tower" of chiral states, which is the usual finite-size sign of incipient symmetry breaking.
- **So no spontaneous CP violation in this model.** That agrees with the literature, where π-flux quantum spin ice is a time-symmetric liquid.
- **Caveat:** 16 grains is tiny. A different grain Hamiltonian (e.g. with an extra ring-sign pattern or longer-range terms) could still order chirally.

## What other theories say (context; references in the GitHub paper's style, quoted from memory)
| Idea | What it says | Relation here |
|---|---|---|
| Sakharov 1967 | baryon violation + CP violation + non-equilibrium | framework used |
| Spontaneous CP violation (T. D. Lee 1973) | CP-symmetric laws, CP-violating vacuum | our "spontaneous route": not realised in this model |
| Domain-wall problem (Zel'dovich, Kobzarev, Okun 1974) | spontaneous CP breaking makes walls between opposite-handed regions; needs inflation (or one seed) | why a single seed would matter |
| No antimatter domains (Cohen, De Rújula, Glashow 1998) | domains must be ≳ the visible universe | one sign everywhere required |
| Electroweak baryogenesis at bubble walls (Kuzmin–Rubakov–Shaposhnikov 1985; Cohen–Kaplan–Nelson 1993) | asymmetry made at moving phase fronts | analogue of the growth-front idea |
| Transitional CP violation (Comelli, Pietroni, Riotto, 1990s) | CP broken only inside moving walls | how EDM limits could be avoided |
| CP as a gauge symmetry in string theory (Dine–Leigh–MacIntire 1992; Choi–Kaplan–Nelson 1993) | all CP violation is spontaneous in quantum gravity | favours spontaneous, which this test did not find in grains |
| Loop quantum gravity (Freidel–Minic–Takeuchi 2005; Perez–Rovelli 2006) | quantum geometry (Immirzi parameter) can give parity/CP-odd fermion forces | precedent for geometry-born CP violation |
| Chiral spin liquids (Kalmeyer–Laughlin 1987; Wen–Wilczek–Zee 1989) | frustrated magnets can order chirally | the hoped-for mechanism; not this model |
| Quantum spin ice (Hermele–Fisher–Balents 2004; Lee–Onoda–Balents 2012; Burnell–Chakravarty–Sondhi 2009) | the frustrated sign usually gives a time-symmetric π-flux liquid; some chiral "monopole-flux" proposals | consistent with our negative result |
| CPT-symmetric universe (Boyle, Finn, Turok 2018) | antimatter "anti-universe" on the other side of the Big Bang | fits the Janus point; an alternative where no net CP violation is needed globally |

## Verdict
- **Yes, grains *can* carry CP violation:** through complex junction amplitudes (new phases at Λ* in the ΔB = 2 junction), or through a junction-chirality coupling, which is a natural CP-odd quantity built purely from grains.
- **But nothing in the framework *requires* it.** The current Hamiltonian is CP-symmetric, and adding CP violation means adding parameters or proving spontaneous chiral order.
- **Intriguing, not evidence:**
  1. The same anomaly condition that forces 3 generations in Branch L₃ is the minimum needed for a CP phase.
  2. Each junction has a built-in pair of mirror-image ground states, a ready-made handedness for grains to choose.
  3. If CP violation is spontaneous, growth from **one seed** is exactly what would give the whole universe the same sign of matter excess.
- **Lattice test (above): it does not order chirally.** Junction handedness cancels on cooling, so the spontaneous route fails in this model. CP violation in Branch L₃ would have to be **put in explicitly** (new CP-odd grain couplings), which costs predictivity.
- Alternatives worth noting:
  - **Branch M**: standard leptogenesis;
  - a **CPT-symmetric (Janus) universe** in the Boyle–Finn–Turok style, where our side's excess is mirrored by the other side's.
