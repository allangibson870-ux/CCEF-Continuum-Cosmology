# A Finite Grain Universe: an exploratory framework and its confrontation with data

### CCEF V5 (Constrained Cellular Emergence Framework)

**Author:** Allan Gibson (independent, non-professional). **Date:** 11 October 2026.

**Prepared with:** extensive assistance from Claude (Anthropic), an AI model. It did the literature mapping, derivations, code and numerical runs, under the author's direction.

> [!IMPORTANT]
> **This is an exploratory hobby framework, not an established theory.** Nothing here is claimed as a discovery.
> - Almost every ingredient comes from published work by others (see [§1](#1-where-the-ideas-come-from) and the [references](#references)).
> - The contribution is a particular *combination* of known ideas, a set of explicit toy calculations, and a record of how that combination fares against current data, **including the many places where it fails or remains unproven.**
> - Where something seemed intriguing, it is labelled as a coincidence or conjecture, not as evidence.
> - The calculations were not peer reviewed.

---

## Abstract
We explore a picture in which the universe is a **finite network of identical quantum "grains"** (qubits) with no fundamental time. Space, gravity, gauge fields and matter are treated as collective properties of the network.

**The framework assembles existing ideas:**
- gravity from entanglement thermodynamics (Jacobson);
- dark energy from fluctuations in the number of discrete elements (Sorkin's "everpresent Λ");
- relational time (Page–Wootters);
- the Big Bang as the crystallisation of space from a pre-geometric graph (quantum graphity);
- light and charges from string-net condensation (Levin–Wen).

It adds one organising principle from the author: **there is only one kind of grain.**

**We then:**
1. derive a few consequences (a finite cosmic volume about one CMB diameter across, which fails once N_ent is computed (§12); cyclic expansion through recruitment of grains from a finite reservoir);
2. compare them with Planck, DESI DR2, gravitational-wave, Galactic-Centre, interferometer, proton-decay and lensing data, using simplified, compressed likelihoods;
3. explore the matter sector through string-net "rules";
4. build and simulate a first explicit grain Hamiltonian.

**Outcome.** Most comparisons are *consistent but not discriminating*. Several earlier hopes were **retracted** after proper statistical treatment. Some live tensions remain:
- a phantom-crossing preference in DESI;
- an interferometer bound on entanglement-gravity noise;
- the cosmological neutrino-mass bound.

**In the toy Hamiltonian:**
- 3-D space self-assembles only if an explicit "no over-connection" rule is added;
- string ends can be made fermions exactly;
- relativistic electrons require spin-½ and arise as exactly three Dirac species on the diamond grain graph.

We list a number of intriguing numerical coincidences, flagged as such, and a set of predictions frozen in advance for future experiments.

---

## Contents
0. [How to read this document](#0-how-to-read-this-document)
1. [Where the ideas come from](#1-where-the-ideas-come-from)
2. [Principles](#2-principles)
3. [The framework (Layer 1: grains, gravity, dark energy, time)](#3-the-framework)
4. [Cosmology: finite volume, cycles, recruitment dark energy](#4-cosmology)
5. [Matter from string-net rules](#5-matter-from-string-net-rules)
6. [Neutrinos, dark matter and monopoles](#6-neutrinos-dark-matter-and-monopoles)
7. [A first explicit grain Hamiltonian](#7-a-first-explicit-grain-hamiltonian)
8. [Electrons from grains](#8-electrons-from-grains)
9. [Confrontation with data: summary table](#9-confrontation-with-data)
10. [Predictions frozen for future experiments](#10-predictions-frozen-for-future-experiments)
11. [Intriguing coincidences (not evidence)](#11-intriguing-coincidences-not-evidence)
12. [Retractions and negative results](#12-retractions-and-negative-results)
13. [Open problems](#13-open-problems)
14. [Methods, caveats and reproducibility](#14-methods-caveats-and-reproducibility)
15. [Acknowledgements](#15-acknowledgements)
16. [References](#references)

---

## 0. How to read this document
Status labels (inherited from earlier CCEF versions):

| Label | Meaning |
|---|---|
| **[ESTABLISHED]** | published, mainstream result used as an ingredient (credit in §1) |
| **[COMPUTED]** | calculated here; code in the repository; not peer reviewed |
| **[COND]** | follows *if* a stated assumption holds |
| **[CONJECT]** | a conjecture or analogy, not derived |
| **[OPEN]** | unknown |
| **[NEG]** | shown here to fail |
| **[RETRACTED]** | an earlier claim withdrawn after a proper test |

Quantities: ℓ is the grain length; M = 1/ℓ is the grain energy scale; Λ* is the "crossover" scale where continuum field theory takes over from the network; D_LSS is the comoving diameter of the CMB last-scattering sphere.

---

## 1. Where the ideas come from
Nothing below is original unless stated. The framework is a synthesis.

| Ingredient | Source |
|---|---|
| Space as an emergent graph; Big Bang as "geometrogenesis" | Konopka, Markopoulou, Smolin, Severini (quantum graphity) |
| Einstein's equations as an equation of state of entanglement | Jacobson 1995, 2016; Sakharov induced gravity; Susskind–Uglum |
| Dark energy ~ 1/√(number of elements) | Sorkin; Ahmed, Dodelson, Greene, Sorkin ("everpresent Λ") |
| Time from correlations with internal clocks | Page & Wootters 1983; Höhn, Smith, Lock |
| Arrow of time from a "Janus point" | Barbour, Koslowski, Mercati; Carroll & Chen |
| Photons and fermions as string-net excitations | Levin & Wen 2003, 2005 |
| Emergent photon in a qubit model ("quantum spin ice") | Hermele, Fisher & Balents 2004 |
| Quantum link models | Chandrasekharan & Wiese 1997 |
| Lorentz symmetry as an emergent low-energy property | Chadha & Nielsen; Bednik, Pujolàs, Sibiryakov; Groot Nibbelink & Pospelov |
| Spectral tilt from criticality | Irges, Kalogirou, Koutroulis ("Ising cosmology") |
| Interferometer noise from entanglement gravity | Verlinde & Zurek |
| Apparent dark matter from emergent gravity | Verlinde 2016 |
| Fermions on graph vertices from qubits on edges | Bravyi & Kitaev ("superfast" encoding) |
| Dirac points from spin–orbit hopping on diamond | Fu, Kane & Mele 2007 |
| Discrete gauge symmetries protecting the proton | Ibáñez & Ross |
| Neutrino anarchy | Hall, Murayama & Weiner |
| Bulk right-handed neutrinos diluted by volume | Arkani-Hamed, Dimopoulos, Dvali, March-Russell |
| Post-inflation axion dark matter | Peccei–Quinn, Weinberg, Wilczek, KSVZ; string-network simulations (Buschmann et al., Gorghetto et al., Saikawa et al.) |
| Monopole relic physics | Kibble; Zurek; Preskill |

**Lineage of this project.**
- **CCEF v2/v3 (early 2026, author):** a continuum-field "twist on GR". The author judged it largely unsuccessful.
- **CCEF v3.9 (July 2026, author):** a hadronic S³ field programme.
- **CCEF V4/V4.1:** the move to grains, plus Lorentz-protection mechanisms.
- **V5 (this document):** reconciles these and adds the data tests, string-net rules, Hamiltonian and fermion work.

The author's own contributions are the overall motivation (a finite, grainy, cyclic universe with no actual infinities), principle P7, and the direction of each investigation.

---

## 2. Principles
- **P1 Finiteness.** A finite number N of grains; a finite Hilbert space; no physical infinities.
- **P2 Grains are qubits.**
- **P3 Space is a pattern** of grain relations. Distance, dimension and locality emerge.
- **P4 Time is relational:** a global constraint Ĥ|Ψ⟩ = 0, with time read from internal clocks. The arrow of time comes from coarse-grained entropy, and the Big Bang is a Janus point.
- **P5 Emergence:** gravity, gauge fields, fermions and Lorentz symmetry are low-energy collective properties.
- **P6 Cycles without a master clock.**
- **P7 One grain type** (the author's principle). If grains came in different types, each type would need a further explanation, leading to an infinite regress. So every particle must be a pattern of one kind of grain.

*Interpretive stance (the author's):* grains are relational primitives, "made of nothing". This is close to ontic structural realism and to "it from qubit".

---

## 3. The framework

### 3.1 Gravity from grain entanglement [ESTABLISHED mechanism; COND realisation]
- If grain entanglement obeys an area law S = η_g A/ℓ², Jacobson's argument gives Einstein's equations with

$$G=\frac{\ell^2}{4\eta_g},\qquad \ell=\sqrt{4\eta_g}\,\ell_P,\qquad N_{\rm ent}\equiv 24\pi\,\eta_g .$$

- **Naming.** N_ent (the "entanglement number") replaces the earlier label N_eff, which was easily confused with the cosmological ΔN_eff. It is only a conventional rescaling of η_g.
- **Derived from the current grain theory** (`CCEF_nent.md`), using no number from earlier CCEF versions. η_g is the entanglement area-law coefficient of everything living on the grains, computed exactly for Gaussian states on the diamond lattice and averaged over surface orientations and positions (as for a coarse horizon):
  - **per field:** scalar 0.027 (N_ent 2.0 per photon/gluon polarisation); grain Dirac fermion 0.337 (N_ent 25.4; spread over orientations 10%);
  - **content:** 16 grain Dirac fields (every SM Weyl plus its lattice mirror; 3 valleys = 3 generations), giving N_ent 407; 24 gauge polarisations, 48; the grains' own spin-ice Gauss-law edge entropy (0.60 nats per cut U(1) grain, Monte Carlo), 28 (1 U(1) grain per relation) to 112 (4);
  - **heavy fields count fully**, including the mirror partners (`CCEF_neff.md`).
- **Result: N_ent ≈ 480 (455–570 for the minimal content), giving ℓ ≈ 5.1 ℓ_P ≈ 8×10⁻³⁵ m and M ≈ 2.4×10¹⁸ GeV.**
  - Wider bounds, if the generations are not the valleys or the non-abelian bundles carry full edge entropy: up to ~1,300–1,800 (M ≈ 1.3–1.5×10¹⁸ GeV).
- **Updated** (`CCEF_valleys_edges.md`):
  - **Valleys = generations survives a structural test.** Local grain couplings on an 8-site superstructure reach all 18 three-flavour Dirac mass terms. The inversion-symmetric ones give exactly Hermitian flavour matrices (mixing plus CP phase, with θ̄ = 0), so the minimal fermion count stands.
  - **The SU(2)/SU(3) bundles carry ≈ 10–13 nats of edge entanglement per cut relation** (free lattice gauge vacuum, c_E = 0.853, flux-representation distribution capped by the link sizes). That adds 395–600.
  - **N_ent ≈ 880–1,080, giving ℓ ≈ 6.8–7.6 ℓ_P and M ≈ 1.6–1.8×10¹⁸ GeV** (≈ 455 if edge terms are excluded from η_g).
- A bundle of n grains per relation allows N_ent ≲ 39n, so n ≳ 13; this is consistent with the ~25–37 grains per relation the forces need.
- *Historical:* earlier work assumed N_eff ≈ 9 (ℓ = 1.1×10⁻³⁵ m, M = 1.77×10¹⁹ GeV), inherited from CCEF v3.9 without re-derivation. Predictions frozen under that assumption were audited (`CCEF_prediction_audit.md`).
- The bare geometry has exact coordinate freedom but **no elasticity** (geometry defects interact only on contact), so gravity's stiffness is **induced by the fields on the grains** (Sakharov–Jacobson), not supplied by the geometry itself.
- Whether the network carries a propagating spin-2 graviton is **[OPEN]**.
- Counting U(1) flux through a horizon gives S = A/4G − ½ ln(A/ℓ²) **[COMPUTED counting; COND physics]**.

### 3.2 Dark energy from the grain count [COND; magnitude ESTABLISHED by Sorkin]
- Treat Λ as conjugate to the 4-volume V₄ = N₄ℓ⁴. Poisson counting gives ρ_Λ ~ 1/(ℓ²√V₄), and Λℓ_P² ~ 10⁻¹²² as observed.
- V5 uses the *global* (whole-cycle) 4-volume, so Λ is constant within a cycle **[FORK]**.
- **[FORK] How many branches the Janus point has, and whether Λ counts them all** (added 2026-10-12).
  - A single classical history through a minimum of structure has exactly two halves (Barbour). In CCEF's timeless, quantum description, histories can leave the least-structured state in many directions: k branches, or a continuum.
  - **Physics inside one branch is unaffected by k:** grain rules, local clocks, crystallisation and reheating, induced gravity, N_ent, the axion, neutrinos and the prediction audit.
  - Matter vs antimatter generalises to Σ_branches B = 0. A CPT-symmetric Janus state gives mirror pairs (k = 4 → 2 matter + 2 antimatter branches); odd k needs a branch with B = 0.
  - **Option (i), Λ counts our branch only:** nothing changes.
  - **Option (ii), Λ counts every branch's 4-volume:** for k equal branches, Λ weakens by √(2/k) (×0.71, 0.58, 0.50 for k = 4, 6, 8). The finite-universe size under rishon splitting is multiplied by (2/k)^(1/3) (×0.79, 0.69, 0.63): **L ≈ 1.3 (x_c/x)(2/k)^(1/3) D_LSS**, with x_c ≈ 0.052 and N_ent ≈ 1,000. It is still recoverable for k = 8 if J±/J_zz ≲ 0.043.
  - From inside one branch, k could show up only through the size of Λ. That makes it in principle constrained, but only together with J±/J_zz.
- The amplitude coefficient was derived as **β = |x|/2** (median 0.34) from ΔV₄·Δρ_Λ ≥ ½ plus Poisson statistics **[COMPUTED]**.

### 3.3 Time [ESTABLISHED mechanism]
- Page–Wootters relational time with finite clocks, so time is grainy too.
- Recurrence (Bocchieri–Loinger) holds, but no clock survives between cycles.

### 3.4 Lorentz protection [COND]
All species emerge from one network, which suggests one shared light cone. Residual Lorentz violation must be suppressed:
- **Mechanism A (strong-coupling attractor):** δ ~ (E/M)^γ. Needs γ ≳ 1.2 (laboratory) and γ ≳ 2.8 (cosmic rays).
- **Mechanism B (emergent supersymmetry):** δ ~ (m_s/M)².
- **Fallback:** random (causal-set-like) grains.

None of these is derived from a concrete Hamiltonian **[OPEN]**.

---

## 4. Cosmology

### 4.1 Finite volume [COMPUTED; COND]
- Requiring the past 4-volume not to exceed the cycle's 4-volume bounds the side of a flat 3-torus: **L ≤ 2.15 β^{2/3} D_LSS** (old N_eff = 9).
- **Audit:** the coefficient scales as N_ent^(−2/3). With the computed N_ent ≈ 480–495 it gives L ≈ 0.07 D_LSS, which is excluded, so this result fails as it stands (see §12 and `CCEF_prediction_audit.md`).
- The median is **L_max ≈ 1.04 D_LSS**. That makes the universe roughly one CMB diameter across, which is in principle testable through CMB topology.

### 4.2 Cycles from grain recruitment [CONJECT → COMPUTED model]
- If G is constant, ℓ is constant, so expansion must recruit new grains into geometry from a finite reservoir.
- A mass-action model, H = H_∞(1 − y₀a³), gives an effective dark energy that is **thawing, never phantom** (w ≥ −1, with 1 + w ∝ a³ early on).
- Its CPL locus is **w_a ≈ −1.75(1 + w₀)**.
- Expansion halts when the reservoir is exhausted.

### 4.3 Primordial spectrum [NEG for the simple version; OPEN]
- The relation n_s = 1 − η is **prior art** (Irges et al.), and it does not follow at a critical point. The counting rule n_s − 1 = 6 − 2Δ needs an operator with Δ = 3 + η/2, and none exists in the Ising or O(3) spectra.
- Near-critical drift implies α_s = ±y(n_s − 1). Relevant drift is excluded at about 9σ; irrelevant drift is disfavoured at 3.7σ.
- Exact n_s = 1 is excluded at 8.4σ.
- **Without inflation, the framework has no working account of the primordial amplitude or tilt.**

---

## 5. Matter from string-net rules
Following Levin–Wen, particles are **ends of labelled strings**. The labels are the Standard Model representations (Q, u, d, L, e, ν^c, H), and a junction is allowed only if the labels fuse to "nothing": colour triality, SU(2) parity, hypercharge, fermion parity and Lorentz pairing.

**Results [COMPUTED]:**
- **The rules reproduce the Yukawa junctions**, and exactly **Weinberg's 12 baryon-violating dimension-6 junctions** as *local* vertices. So the proton is **not** topologically protected by the network as such. (An earlier hope that it was is **[RETRACTED]**.)
- **A search of all ℤ₃ gradings** that keep the Yukawas, leave the Higgs neutral, forbid every baryon-violating junction and are anomaly-free finds a **unique** solution: **lepton triality**, (Q, u, d, L, e, ν, H) = (0, 0, 0, 1, 2, 2, 0).
  - It is anomaly-free **only for 3 generations**.
  - It forbids every Majorana mass, so **neutrinos must be Dirac** (no neutrinoless double-beta decay).

**The framework forks:**

| | Branch M (minimal rules) | Branch L₃ (lepton triality) |
|---|---|---|
| Proton | decays; Super-K requires Λ* ≥ 4×10¹⁵√C GeV; flavour-blind μ⁺π⁰ ≈ e⁺π⁰ | absolutely stable |
| Neutrinos | Majorana allowed | Dirac only |
| Generations | any | exactly 3 required |
| Crossover Λ* | high | unconstrained by protons |

The proton-decay formula used is τ(p → e⁺π⁰) = 8.7×10³⁵ yr (Λ*/10¹⁶ GeV)⁴/C² **[COMPUTED, standard matrix elements]**. Super-K's limit already **excluded the low-Λ* versions of Branch M**.

---

## 6. Neutrinos, dark matter and monopoles
*(All in Branch L₃.)*

### 6.1 Why are Dirac neutrinos so light? [CONJECT mechanism; COMPUTED consequences]
- The observed masses need a Dirac Yukawa coupling of about 2.9×10⁻¹³.
- In the string-net, ν^c is the **only fermion string carrying no Standard Model gauge flux**. If such a string is not bound to the gauge condensate, it may spread over the ~(M/Λ*)³ grains of each crossover cell, diluting its coupling to y ≈ (Λ*/M)^{3/2}. This is analogous to bulk right-handed neutrinos in extra-dimension models.
- That needs **Λ* ≈ 8×10¹⁰ GeV** (range 1.4×10¹⁰–4×10¹¹).
- Assuming flavour-blind grains ("Dirac anarchy", 4×10⁶-sample Monte Carlo):
  - normal ordering favoured **175 : 1**;
  - **Σm_ν ≈ 72 meV** (68%: 64–84);
  - m₁ ≈ 9 meV, m_β ≈ 12.5 meV;
  - large lepton mixing;
  - ΔN_eff = 0.14 (or 0.06, or 0, depending on the thermal history).

**Fitted in the recruitment cosmology** (DESI DR2 BAO + Planck distance priors; geometric only, no CMB lensing):
- Δχ²(72 meV) = 3.05, a "mild tension" under the rule fixed in advance.
- **2.33 of that is already present at the 59 meV minimum** that oscillations allow. It is the generic DESI neutrino-mass tension, not specific to this model.
- The non-phantom recruitment dark energy **cannot relax** the bound.

### 6.2 Dark matter [CONJECT origin; COMPUTED consequences]
Ruled out within the framework:
- neutrinos;
- heavy ν^c modes (they decay);
- ℤ₃-protected relics (every charge combination is already occupied by ordinary matter);
- monopoles (flux limits);
- "apparent" entanglement dark matter.

On the last one: a Verlinde-type a₀ = cH₀/6 ≈ 1.1×10⁻¹⁰ m s⁻², but matter–radiation equality would come at z_eq ≈ 535 instead of 3387, and the Bullet Cluster is a problem.

**Favoured candidate:** the **QCD axion with f_a ≈ Λ***. It also addresses the strong-CP problem. With no inflation, the "post-inflation" scenario is forced, giving **m_a ≈ 74 μeV** (14–400 μeV; about 18 GHz), KSVZ coupling ≈ 3×10⁻¹⁴ GeV⁻¹, domain-wall number 1, and axion miniclusters.
- **Audit:** with the computed N_ent ≈ 480–495, Λ* ≈ 1.0×10¹⁰ GeV, so **m_a ≈ 550 μeV (~130 GHz)**, in the high-mass post-inflation window (`CCEF_prediction_audit.md`). The 74 μeV figure is the frozen record.

**Secondary:** Planck-mass black-hole remnants (~30 μg). Their abundance is not predictable.

### 6.3 The monopole problem without inflation [COMPUTED; COND]
- Compact emergent hypercharge implies monopoles. The minimal one is ≈ 35 Λ* ≈ 3×10¹² GeV on the emergent lattice.
- **No Kibble monopoles:** there is no GUT stage, and π₂ = 0 for every symmetry breaking in the framework.
- **Thermal monopoles:** a Boltzmann calculation shows the MACRO bound is respected if the hottest temperature of the geometric phase was T_max ≲ 0.95 Λ* (central mass estimate).
- **Emergence defects:** none, *if* the gauge fields switch on as a smooth crossover. The adiabaticity ratio is ~3×10⁸.

---

## 7. A first explicit grain Hamiltonian
**Objects (P7).** Each grain is a qubit *and a relation*: it joins two "junctions", and a junction is simply where four grains meet. The configuration is a bipartite 4-regular graph whose **edges are grains**.

$$\hat H=\underbrace{\sum_v\big[U\,{\rm sq}(v)-K\,{\rm hex}(v)+W\,\theta(v)\big]}_{\text{geometry}}+\hat H_{\rm rewire}+\underbrace{\frac{J_{zz}}{2}\sum_v Q_v^2}_{\text{Gauss law}}-\underbrace{J_\pm\sum_v\sum_{i<j\in v}(\sigma^+_i\sigma^-_j+{\rm h.c.})}_{\text{exchange}}$$

- **sq:** 4-cycles (crowding).
- **hex:** 6-rings (where light lives).
- **θ:** over-connection (three or more independent short routes between two junctions).
- **Q_v:** the oriented σᶻ sum at junction v.
- **The last two terms** are **quantum spin ice** on the grains: an emergent U(1) Coulomb phase with a photon (Hermele–Fisher–Balents). Ring exchange arises at third order, J_ring = 12J_±³/J_zz².

**Monte Carlo of the geometry sector [COMPUTED]** (216 junctions / 432 grains, simulated annealing on 4 cores):

| Rules | Outcome |
|---|---|
| Rings only (W = 0) | **Space crumples** into dense knots (energy −39.6 per junction vs −12 for 3-D diamond) |
| Weak anti-crowding (W = 2.5) | A non-3-D structure beats diamond |
| **W ≥ 4** | From random relations, every run self-assembles to **the exact 3-D diamond structure out to three steps**. Glassy at longer range (16–22% perfect junctions); nothing found beats diamond's energy |
| Diamond heated | Never melts in the run (strong hysteresis: first-order-like, glassy geometrogenesis) |

> **Follow-up (2026-10-12, `CCEF_geometry_groundstate.md`):**
> - **Diamond is *not* the ground state of the geometry term as written.** An exhaustive search of all 3,415 "folded" spaces finds tiny closed tori (54 junctions) at −18 per junction, saturating a proven lower bound. The true ground state is crumpled, and extended 3-D space is only metastable.
> - Adding a local **angle rule** (each pair of grains at a junction lies on at most 2 rings) gives a proof that E/N ≥ −12 for every graph, so diamond becomes a ground state. The over-connection term excludes the polytypes.
> - But with the rule, classical annealing, simulated quantum annealing, staged and ramped schedules all freeze in a glass (≈ −7) with extended defects. Quantum rewiring (path-integral approximation) does not help.
> - A crystal seed in a 1,728-junction universe neither grows nor melts at any temperature tested under local moves: the crystal–tangle front is pinned.
> - **With collective "template" moves** (a junction and its 4 neighbours rewired at once to continue the crystal pattern, ~8 grains), **even a one-cell seed grows to fill the whole 1,728-junction universe with perfect 3-D diamond** (the exact ground state). Unguided moves of the same size fail.
> - Caveats: this is a non-equilibrium growth rule; the registry comes from the seed's lattice; such collective terms would have to exist in Ĥ.
> - **With energy conserved and light as the only sink** (`CCEF_microcanonical_growth.md`): the light starts cold and no outside bath exists.
>   - One seed still converts the whole universe to perfect diamond (c = 1–30 light modes per junction).
>   - The full latent heat (≈ 12 per junction) goes into light: T = 12/c in geometry units, Planck-hot if the unit is ~M.
>   - The crystal survives its own heat (no melting even at c = 1).
>   - The hot early universe is crystallisation's own heat, computed.

**Reading:**
- 3-D space is **not automatic**. Light's own preference (many small rings) crumples space. An explicit rule against over-connection, "two points cannot be joined by too many independent short routes", is needed.
- ~~Mapping M ↔ J_zz and Λ* ↔ J_ring, the hierarchy Λ*/M ≈ 4×10⁻⁹ corresponds to J_±/J_zz ≈ 7×10⁻⁴.~~ **Retracted:** the emergent light speed c ~ J_ring·a forces J_ring ~ ħc/ℓ = M. The M/Λ* hierarchy is unexplained (`CCEF_reheat.md`).
- Quantum spin ice is reported to enter its Coulomb phase through a thermal crossover, which is the gentle switch-on the monopole argument needs (literature, quoted from memory).

> **Rewritten as local update events (2026-10-12, `CCEF_grain_rules.md`).** Local time (§13, item 7) requires the Hamiltonian above to be read as a rulebook of local events, not a continuous-time generator. A junction's clock is its count of updates, and events sharing a grain are ordered by cause and effect.
> - **Light ring events:** exp(−iεJ(O_h + h.c.)) on 6 grains. They keep the Gauss law exactly (96/96 rings).
> - **Slicing independence:** every causal ordering gives the same state (to 5×10⁻¹⁸); reversing overlapping events changes it.
> - **Weak/strong events:** keep their gauge laws by inheritance (an exponentiated gauge-invariant term stays gauge-invariant).
> - **Electrons:** updated bond-direction by bond-direction (the diamond's 4 bond directions are natural perfect-matching layers), they stay **exactly massless** for every step size. A fixed update order makes the electron's speed direction-dependent at O(ε). Symmetric and especially random orders suppress this (0.1–3% vs 5–18%).
> - **Geometry-rewiring events** (`CCEF_geometry_events.md`): a reversible two-grain switch acting on a superposition of grain networks, with the light state ice-rule (2-in/2-out) at every junction.
>   - Every branch keeps unitarity, 4 grains per junction and the Gauss law exactly (1,128 branches, 328 geometries).
>   - **Space may only rewire grains carrying equal electric flux.** Flux-blind switches create charge in 67% of the weight.
>   - The before/after relation between events can differ between superposed geometries (rare at this coupling).
>   - **Slicing independence holds only if the causal order is read from the quantum state.** Grain labels fail (0.55) and the classical diamond background fails (2×10⁻³); the self-consistent order is exact (3×10⁻¹⁶).

**Known shortfalls:**
- the emergent fine-structure constant of quantum spin ice is ≈ 0.08 (literature), while hypercharge needs ≈ 0.013;
- there is no SU(2) or SU(3) yet;
- no graviton is shown;
- a perfect crystal would define a preferred frame **[OPEN]**.

---

## 8. Electrons from grains
### 8.1 Fermionic string ends [COMPUTED, exact]
- A charge (Gauss-law violation) moves by flipping a grain. **Plain flips** give Levin–Wen T-junction statistics θ = 0 at all 864 tested junction-triples: **bosons**.
- **Dressed flips** (X on the grain times Z on the grains earlier in a fixed local order at both ends) give **θ = π at all 864**: **fermions**.
- All consistency checks pass: hops anticommute exactly when grains share a junction, create no stray flux, and leave the ring terms commuting.
- In the zero-flux sector the 432 grain qubits are **exactly** 216 junction fermions coupled to a gauge field (the Bravyi–Kitaev superfast encoding). Gauss parity equals fermion parity, so odd-charge ends are fermions.

### 8.2 Light and relativistic? [COMPUTED]
- **Spinless fermions:** nearest-neighbour hopping on the diamond graph gives **nodal lines** for *all 512* 0/π flux patterns of the 8-junction cell. This agrees with the codimension theorem for real (time-reversal-symmetric, spinless) Hamiltonians. **Lesson: relativistic electrons need spin-½.**
- **Spin-½** (two grains per relation) plus the Fu–Kane–Mele spin–orbit hop gives **exactly three 4-fold Dirac points**, one at each X point (one per spatial axis): three massless 4-component Dirac fermions.
  - The cones are isotropic exactly at **λ/t = 1/4**.
  - Unequal junction bonds t_i = t(1+ε_i) give masses equal to the three "Klein-four" combinations: m_x = t|ε₁+ε₂−ε₃−ε₄|, m_y = t|ε₁−ε₂+ε₃−ε₄|, m_z = t|ε₁−ε₂−ε₃+ε₄|.
- **Interpretation:** a fermion is massless while its junction is perfectly tetrahedral. Its mass measures the junction's distortion.
- **Valleys as generations, tested** (`CCEF_valleys_edges.md`):
  - On an 8-site (simple-cubic) superstructure, all three valleys fold to k = 0. Local grain couplings then reach all 18 Dirac mass terms for 3 flavours.
  - Uniform distortions give 3 masses and no mixing. Inversion-symmetric real couplings add mixing angles; complex (T-odd) ones add CP phases. The parity-odd (θ̄) direction stays exactly zero, which is the parity solution of strong CP.
  - **Three generations = three spatial axes.** Open: the mass hierarchy and the origin of the superstructure.

**Shortfalls:**
- these are vector-like (QED-type), not chiral (Standard Model-type) fermions;
- masses are not yet tied to a Higgs field;
- the isotropy and equal-speed-with-light conditions are tunings **[OPEN]**.
- ~~**Inconsistent with the photon phase as built**~~ (`CCEF_light_window.md`). As bare spin-ice charges, in the photon phase (J±/J_zz < 0.052) the electrons hop ~30× faster than light and feel U/t ≈ 19, beyond the Mott threshold U_c ≈ 5 t.
  - **Fixed by the rebuild** (`CCEF_electron_rebuild.md`). The electron is now a separate fermionic constituent of the relation bundle, coupled through the exact Gauss law div E = ρ, with its own hop t.
    - Exact gauge invariance; zero on-site repulsion from the light sector (602 doubly occupied physical states, all at zero cost).
    - Residual Coulomb U_eff/t = 4αG(0)/C ≤ 0.54 for α ≤ 0.08, far below Mott.
    - **Massless (3 Dirac valleys) in zero-flux spin ice.** That is the unfrustrated sign CCEF's Ĥ already has; a π-flux background would ruin it.
    - One light cone needs t ≈ 1.49 J_ring (Monte Carlo photon speed c = 1.49 a·J_ring). Why t takes that value is the remaining Lorentz-protection question.

---

## 9. Confrontation with data
Simplified likelihoods throughout (see [§14](#14-methods-caveats-and-reproducibility)).

| Test | Data | Result | Status |
|---|---|---|---|
| CMB topology: finite volume ~1 D_LSS | Planck SMICA/Commander, full and masked sky | An apparent E2 half-turn "lean" (P ≈ 0.08–0.14 per map) **vanished** once the choice among 11 allowed shapes was counted (P = 0.79). The fitted axis lay ~9° from the Galactic pole | consistent, no signal; lean **[RETRACTED]** |
| Dark energy w(z) | DESI DR2 + CMB (+SNe), projected (w₀, w_a) | Better than ΛCDM with Union3 (Δχ² 5.6) and DESY5 (Δχ² 9.1); 2–3σ from DESI's phantom-crossing best fits | mixed; live tension |
| Neutrino mass sum | DESI DR2 BAO + Planck priors | 72 meV: Δχ² 3.05 (2.33 generic) | mild tension |
| Weak-lensing S8 | KiDS-Legacy, DES Y3, HSC Y3, ACT DR6 (values quoted) | S8 = 0.800 for both models (σ8 −3% offset by higher Ω_m) | neither helps nor hurts |
| Galaxy lensing law | — | grain corrections ~10⁻¹¹⁰; achromatic | GR-like, untestable |
| GW propagation | GW170817, GWTC-3/4 | \|Δc\|/c ~ 10⁻⁷⁰, m_g = 0, no dispersion or birefringence | consistent, non-discriminating |
| S2 / Sgr A* | GRAVITY | deviations from GR ≤ 10⁻¹⁰ | consistent, non-discriminating |
| Spacetime jitter, paths (KPZ, χ ≈ 0.24) | Quasar imaging | far below excluded foam models | consistent |
| Spacetime jitter, entanglement gravity (Verlinde–Zurek) | Fermilab Holometer | natural amplitude **~3σ disfavoured** in one spectral model | live tension |
| Proton decay (Branch M) | Super-K | low-Λ* versions excluded | pruned |
| Primordial tilt | Planck | the criticality route fails as derived | negative |
| Apparent dark matter | CMB z_eq, Bullet Cluster | fails | negative |

---

## 10. Predictions frozen for future experiments
Code and outputs were hashed (SHA-256) with UTC timestamps **before** each comparison step. See [§14](#14-methods-caveats-and-reproducibility) for an important caveat about how blind these are.

| Prediction | Would count against it | Experiments |
|---|---|---|
| **No phantom crossing:** w(z) ≥ −1 at all z (recruitment) | confirmed w < −1 at z ≳ 0.5 | DESI DR3+, Euclid, Rubin |
| fσ8(z ≈ 0.5) 1.5–4% below ΛCDM for the DESI-preferred recruitment range | fσ8 = ΛCDM at the 1% level | DESI full-shape, Euclid |
| **Branch L₃:** no proton decay, **no neutrinoless double-beta decay**, normal ordering | any proton decay; any 0νββ; inverted ordering | Hyper-K, LEGEND-1000, nEXO, JUNO |
| Σm_ν ≈ 72 meV (68%: 64–84), m_β ≈ 12 meV | robust Σm_ν < 61 meV within this cosmology | DESI DR3, Euclid, CMB-S4 |
| ΔN_eff ≈ 0.14 (ν^c), up to ≈ 0.19 with thermal gravitons: crystallisation reheats to ~10¹⁹ GeV, so they thermalise (`CCEF_reheat.md`; earlier range {0, 0.06, 0.14}) | ΔN_eff < 0.05 or ≳ 0.3 | Simons Observatory, CMB-S4 |
| **Axion dark matter, m_a ≈ 74 μeV (14–400; ~3–100 GHz)** | nothing in that band; any WIMP signal | MADMAX, ALPHA, ORGAN, BREAD |
| **Branch M package** (`CCEF_branchM.md`, not formally pre-registered): Λ* ≈ 10¹⁵ GeV; proton decay in the Hyper-K window with **μ⁺π⁰ ≈ e⁺π⁰**; Majorana neutrinos, normal ordering, Σm_ν ≈ 77 meV, **m_ββ ≈ 18 meV (9–33)**; ΔN_eff ≈ 0.05 | GUT-like μ⁺π⁰ ≪ e⁺π⁰; no 0νββ down to ~5 meV; ΔN_eff ≈ 0.14+ | Hyper-K, LEGEND-1000, nEXO, CMB-S4 |
| **Hybrid** (Branch M + dark sector, `CCEF_hybrid.md`, not formally pre-registered): as Branch M, plus **asymmetric dark matter of ~2.5–10 GeV** with a massive dark photon; nothing in heavy-WIMP detectors | heavy-WIMP discovery; no light dark matter where its dark-photon coupling should show | SuperCDMS, CRESST, DarkSide, dark-photon searches |
| Entanglement-gravity interferometer noise at natural amplitude | exclusion with the correct spectral model | GQuEST |
| ~~Finite volume ~(1–1.5 D_LSS)³~~ **fails after the audit** (needs the old N_eff = 9; see below) | no topology down to ~1.5 D_LSS | LiteBIRD, COMPACT methods |

> **Audit after the computed N_ent (2026-10-12, `CCEF_prediction_audit.md`).** All freeze records were re-hashed and every frozen file is unchanged. These predictions assumed N_eff = 9 (M = 1.77×10¹⁹ GeV); the lattice gives N_ent ≈ 480–495 (M = 2.4×10¹⁸ GeV).
> - **Unchanged:** no phantom crossing; fσ8; S8; Branch L₃ (no p-decay, no 0νββ, normal ordering, Σm_ν = 72 meV, m_β); ΔN_eff = 0.14; proton-decay verdicts; interferometer noise (GQuEST row); hybrid dark matter.
> - **Axion: affected.** f_a = Λ* ∝ M, so **m_a ≈ 550 μeV (100–3,000; ~130 GHz)** instead of 74 μeV. That is outside the frozen band but still a viable post-inflation dark-matter axion (strings supply ~97%). The frozen record stands; any amended prediction must be frozen separately and labelled post-audit.
> - **Finite volume: fails.** The same formula gives L ~ 0.07 D_LSS, which is excluded; equivalently, grain-count dark energy is ~55× too weak (moved to §12).
> - **Minor:** the thermal-graviton increment to ΔN_eff (→ 0.19) is doubtful (T_RH ≈ 0.7–4.5×10¹⁸ GeV); the remnant mass is ~4 μg.

---

## 11. Intriguing coincidences (not evidence)
These are recorded because they are interesting and testable, **not** because they support the framework. An order-of-magnitude coincidence is often a 1-in-10 event.

1. **Three independent routes land near Λ* ~ 10¹¹ GeV:**
   - the Dirac-neutrino dilution (with 3-D grain counting);
   - the Lorentz-protection window (γ = 3 allows Λ* ≤ 4×10¹¹ GeV);
   - the post-inflation axion dark-matter window (f_a ~ 10¹⁰–1.4×10¹¹ GeV).

   The axion requirement also picks the dilution power p = 3/2 out of {1, 3/2, 2}.
2. **Two independent "threes."**
   - Lepton triality is anomaly-free only for **3 generations**.
   - Separately, spin-½ fermions on the 3-D diamond grain graph come out as **exactly 3 Dirac species**, one per spatial axis, with independent masses from three bond-distortion combinations. Reading the three species as generations is an old lattice idea ("tastes"); here it is a speculation only.
3. **The right-handed neutrino keeps reappearing.**
   - ℤ₃ lepton triality forces Dirac neutrinos, so ν^c must exist.
   - Branch M's leptogenesis needs Majorana ν^c.
   - Gapping the lattice's mirror fermions to make the weak force one-handed needs 16 Weyl fermions per generation (ℤ₁₆ anomaly), which also means ν^c (computed, `CCEF_chiral.md`).
   - Three independent routes.
4. **cH₀/6 ≈ 1.1×10⁻¹⁰ m s⁻²** lies within 10% of the MOND acceleration a₀. Verlinde noticed this; the grain picture gives it a natural home but does not derive it, and the full apparent-dark-matter idea fails here.
5. ~~**A cubed hierarchy.**~~ *Retracted (unit inconsistency, `CCEF_reheat.md`).* In its place:
   - **space must be bound at nearly the Planck scale or its own latent heat re-melts it**;
   - so the universe starts at ~10¹⁹ GeV, a hot Big Bang without inflation;
   - thermalised right-handed neutrinos (and gravitons) then predict ΔN_eff ≈ 0.14–0.19.
6. **"Spin-½ is required"** for relativistic electrons on the grain graph. That is consistent with nature, though it is a known theorem in a new setting.
7. **The gentle switch-on.** The same smooth emergence that avoids monopoles leaves the gapless axion phase scrambled. That produces exactly the axion-string ("post-inflation") scenario the dark-matter estimate assumed.
8. **Space may be metastable.** Under the original geometry rules, extended 3-D space is not the ground state: tiny closed universes are. It survives only because the dynamics is glassy. With the corrected rules, the ground states are finite flat diamond universes. They are unreachable by local moves, but **a single seed grows into a whole perfect universe** once collective "template" rewiring is allowed. Growth from one seed would give one registry everywhere, with no domain walls: a grain analogue of inflation's single causal patch (conjecture; `CCEF_geometry_groundstate.md`).
9. **A built-in handedness.**
   - The anomaly condition that forces 3 generations in Branch L₃ is exactly the minimum for a CP-violating phase.
   - A frustrated 4-grain junction has two mirror-image ground states (scalar chirality ±√3, a CP-odd quantity).
   - If CP violation arises spontaneously at geometrogenesis, growth from a single seed would give the whole universe one sign of matter excess (`CCEF_grain_CP.md`).
10. **Parity from geometry.**
    - Diamond's inversion symmetry (swapping the two junction types) acts as parity on the grain fermions.
    - It exactly forbids the θ-type quark mass phase even when couplings violate CP: the known "parity solution" of strong CP, here arising from the shape of space (`CCEF_strong_cp.md`).
    - A slight "breathing" of the crystal (the two junction types differing) breaks P and C but keeps CP: the same pattern as the weak force (`CCEF_parity_breaking.md`).
11. **The missing antimatter may be on the other side of the Janus point.**
    - In a CPT-symmetric grain universe, baryon number is exactly zero at the Janus point and opposite on its two sides.
    - The sign can be set by the universal state at the Janus point, with CP-symmetric laws (toy model).
    - In the cyclic picture, neighbouring cycles would be matter/antimatter mirrors (conjecture; `CCEF_janus_cpt.md`).
12. **Einstein gravity is forced.**
    - Once grains are background-independent, a systematic search finds the linearised Einstein (Fierz–Pauli) energy as the *only* relativistic dynamics for their metric fluctuations, with exactly the graviton's two polarisations.
    - The leftover scalar mode demands that time be re-labellable locally at every junction: emergent time must be local, not one global clock (`CCEF_graviton.md`).
    - A clock at every junction removes it and yields Newton's law. Consistent local clocks arise naturally if grains evolve by local update events, each junction's time being its count of relational updates (`CCEF_local_time.md`).
13. **m_ν ~ ρ_Λ^{1/4} ≈ 2 meV** (a well-known numerology). As a dynamical mechanism it is excluded here: it would make neutrinos about 0.3 eV at recombination.
14. **No clock, no preferred direction?**
    - When the grain electron is evolved by discrete local updates, a *fixed* update schedule makes space direction-dependent. *Random* update orders largely restore isotropy (`CCEF_grain_rules.md`).
    - A universe with no global clock has no fixed schedule, so isotropy might follow from the causal structure itself, as in causal-set sprinkling. This is a band-level observation only.
15. **Light tells space how it may change.**
    - In the grain rules, geometry can only rewire two grains that carry the same electric flux; otherwise charge would be created. The fields constrain the geometry's own moves.
    - When geometry is in superposition, "before/after" between events becomes part of the quantum state, as expected for quantum gravity by Hardy and by Zych et al. (`CCEF_geometry_events.md`).
16. **Grains give the shape, fields give the pull.**
    - The bare grain geometry has exact coordinate freedom but no elasticity: its defects interact only on contact.
    - Gravity's stiffness comes from the entanglement of the light and matter living on the grains (Sakharov–Jacobson), computed here as a finite lattice area law (`CCEF_induced_gravity.md`).
    - This is close to the author's intuition that gravity is "a combination of matter, mass and grains". It also implies N_ent ≈ 480 rather than the old 9.
17. **Space crystallising makes the Big Bang hot.** With energy conserved, one seed's crystallisation front leaves perfect 3-D space behind it and pours all its latent heat into light (`CCEF_microcanonical_growth.md`).
18. **The grain scale lands near the reduced Planck mass** (superseded: with the non-abelian edge entanglement, M ≈ 1.6–1.8×10¹⁸ GeV, ~30% below it). The derived N_ent ≈ 480 gives M ≈ 2.41×10¹⁸ GeV, within ~1% of M_P/√(8π) = 2.435×10¹⁸ GeV (exact equality needs N_ent = 48π² ≈ 474, inside the derived range 455–570). Probably a coincidence, since the range is wider than the match (`CCEF_nent.md`).
19. **Three generations from three dimensions, with CP violation but no strong CP problem.** The grain fermion has one Dirac valley per spatial axis. Inversion-symmetric grain couplings give exactly Hermitian flavour matrices: quark mixing and its CP phase arise while θ̄ = 0 automatically (`CCEF_valleys_edges.md`). A structural fit, not a derivation of the masses.

---

## 12. Retractions and negative results
Recorded deliberately; these are as much a part of the work as the positive items.

- **CMB "E2 lean":** retracted after the look-elsewhere correction (P = 0.79).
- **Grain-baryon protection window** (Λ* ≈ 3–6×10¹⁴ GeV): retracted. The string-net rules showed that baryon violation is local.
- **"Addition 3"** (neutrino masses from the Weinberg operator at Λ*): ruled out by Super-K in Branch M, and forbidden in Branch L₃.
- **n_s = 1 − η from criticality:** prior art, and not supported by the counting rule. Exact n_s = 1 is excluded.
- **v3.9 neutrino formula** m_ν = Λ²/√(MΛ): not SU(2)-invariant as written; forbidden in L₃.
- **Apparent dark matter** from grain entanglement: fails (CMB, Bullet Cluster). A CCEF-native variant gives a₀ 6–15× too small.
- **The hope that recruitment dark energy loosens the neutrino-mass bound:** it does not.
- **Rings-only geometry:** crumples space.
- **"Diamond is the ground state"** (rings + crowding + over-connection rules): refuted. Tiny tori reach −18 vs −12.
- **Simulated quantum annealing as a fix for glassy geometrogenesis:** no improvement at equal cost.
- **Baryogenesis in Branch L₃** (`CCEF_baryogenesis.md`):
  - Majorana leptogenesis is forbidden by ℤ₃;
  - Dirac leptogenesis fails by ~10¹⁶, because the ν^c dilution starves every ν^c channel and the heavy ν^c modes decay after sphalerons stop;
  - electroweak baryogenesis fails.
  
  Only a ΔB = 2 mechanism at the geometrogenesis front remains, and it needs an unknown grain-level CP source. Branch M keeps standard leptogenesis.
- **Spontaneous grain-level CP violation** (junctions locking into one handedness): not found in a 16-grain exact calculation.
- **Stable Planck-mass remnants:** incompatible with the Planck-hot start (they would overclose by ~10²⁶). Remnant dark matter is excluded in both branches (`CCEF_branchM.md`).
- **Branch M dark matter:** an axion at f_a = Λ* overproduces by ~10⁴, and heavy right-handed-neutrino dark matter overcloses.
- **Spinless electrons:** always nodal lines (512/512).
- **Finite volume ~1–1.5 D_LSS** (`CCEF_prediction_audit.md`): it relied on the old N_eff = 9.
  - With the computed N_ent ≈ 480–495, the same everpresent-Λ argument forces L ≈ 0.07 D_LSS, which is excluded by CMB topology searches. Equivalently, the grain-count dark-energy magnitude is ~55× too small for an observed-size universe.
  - Possible rescues: counting in Planck rather than grain 4-volumes; species-enhanced fluctuations. Neither is derived.
  - **Proposed rescue: rishon splitting** (`CCEF_rishon_splitting.md`; post-hoc). Each relation is a bundle of n ≈ 25–37 sub-grains, and the Λ 4-volume counts their elementary update events. This restores L ≈ 1–3.5 D_LSS if J±/J_zz ≲ 0.1.
    - It works only because the junction lattice is a crystal (hyperuniform). Spatial bundling alone recovers just ~6× of the missing 55×.
    - Prediction: L ≈ 0.1 (J_zz/J±) D_LSS.
    - The same bundling returns the axion to ~150–170 μeV (inside its frozen band).
    - Two underived assumptions; status **[CONJECT]**.
    - **Not a tuning** (`CCEF_light_window.md`, boundary corrected): spin ice carries light only for J±/J_zz < x_c ≈ 0.052 (quantum Monte Carlo, |J⊥|/J < 0.104).
      - Throughout that phase, with N_ent ≈ 880–1,080 (`CCEF_valleys_edges.md`), **L ≈ 1.3 (x_c/x) D_LSS ≳ 1.2 D_LSS**.
      - The rescue is automatic wherever light exists.
      - The axion stays at ~210–235 μeV (inside the frozen band).
- **v3.9 errata applied:** the helicity identity is (1/4π²)∫a∧da = B (not B²); the ordered-phase vector mass is 214 MeV (not 152).

---

## 13. Open problems
1. Derive Lorentz protection (γ ≳ 3, or alternatives) from the Hamiltonian.
2. ~~Prove (or refute) that 3-D diamond is the ground state.~~ Done (`CCEF_geometry_groundstate.md`): refuted as written (crumpling); proved with an added angle rule. **Kinetics:** local classical and quantum-annealing dynamics freeze in a glass, but collective star-template moves grow perfect space from a single seed. **Still open:** a label-free local continuation rule, closure on incommensurate universes, multiple seeds, and the origin of ~8-grain collective terms in Ĥ.
3. A primordial spectrum (amplitude and tilt) without inflation.
   - **Partial** (`CCEF_ripples.md`): area-law thermal fluctuations, frozen when residual non-local grain links vanish, give a scale-invariant spectrum automatically (the string-gas mechanism on grains).
   - The amplitude fixes the freeze-out at ~10¹⁴–10¹⁵ GeV, which matches Branch M's crossover, not L₃'s.
   - The tilt is not derived. Random grain noise and front-roughness mechanisms fail.
4. SU(2) × SU(3) from grains, for example through bundles of grains per relation (rishon / quantum-link constructions).
   - **Built** (`CCEF_nonabelian.md`): rishon quantum links on grain-made fermions.
   - Verified exactly on small systems: the non-abelian charge algebra, gauge-invariant ring and matter-hopping terms, and a 17-state physical SU(2) plaquette.
   - Needs ~20–50 grains per relation for the real couplings (or a short "D-theory" extra direction).
   - Not demonstrated: confinement or the continuum limit at scale; the coupling values.
5. Chiral fermions: mirror-fermion gapping, and Higgs-linked masses.
6. The emergent fine-structure constant (≈ 0.08 in spin ice vs ≈ 0.013 needed).
7. A propagating graviton from fluctuations of the relational graph.
   - **Partly built** (`CCEF_graviton.md`): background independence turns the would-be phonons into gauge (diffeomorphisms).
   - The only relativistic energy for the remaining metric fluctuations is then exactly the linearised Einstein (Fierz–Pauli) potential, or its unimodular WTDiff twin. It carries exactly 2 helicity-2, linearly dispersing waves (computed).
   - One extra helicity-0 mode is unstable unless a **local** time-reparametrisation constraint exists at every junction, so CCEF's global Page–Wootters time must become local.
   - **Local time worked out** (`CCEF_local_time.md`):
     - a clock at every point removes the unstable mode (exactly 2 graviton polarisations remain), and its constraint yields Newton's 1/r law;
     - consistent per-junction clocks require grain dynamics written as **local update events in a causal order**: 269 different causal update orders give the identical state, so each junction's time is just its update count;
     - **Grain rules recast as update events** (`CCEF_grain_rules.md`): light, electron and gauge events done (Gauss law exact; massless electron preserved; isotropy needs symmetric or random update order).
     - **Geometry-changing events built** (`CCEF_geometry_events.md`): exact rules on every branch; flux-matched rewiring; the causal order must be read from the quantum geometry.
     - **Coarse-grained** (`CCEF_induced_gravity.md`): geometry events give exact coordinate freedom (a whole-plane slip costs 0) but no elasticity (defects interact only on contact). Einstein's stiffness must be induced by the fields' entanglement (Jacobson), and that is computed: N_ent ≈ 480 for the full content (`CCEF_nent.md`), versus the old assumed 9.
     - **Open:** a propagating graviton wave in the event dynamics; gauge-field edge terms and the grain qubits' own entanglement in η_g; narrowing N_ent (non-abelian edge terms; valleys vs generations) and hence M; one shared light cone for photon and electron events; the physical step size ε; closing the full non-linear local-time algebra (which would give full Einstein gravity).
8. The recruitment and halting dynamics from first principles.
   - **The restart is missing.** Each side of the Janus point runs down to a cold heat death with space still crystallised. A cold universe does not re-melt space (a frozen pond in a cold world stays frozen; the crystal even survives its own latent heat, `CCEF_microcanonical_growth.md`).
   - A new cycle therefore needs either re-collapse (reheating the light until space re-melts, with Tolman's entropy-accumulation problem) or recurrence of the finite grain system (Bocchieri–Loinger), which arrives as a rare fluctuation that is itself a Janus point (with the Boltzmann-brain problem).
   - In contrast, Barbour's unconfined Janus universe has no heat death and no cycles. CCEF's finiteness is what allows cycles.
9. A real dark-matter mechanism: the axion's origin and quality problem.
10. The thermal history (T_max vs Λ*), which sets the monopole, ν^c and axion outcomes.
11. **Baryogenesis in Branch L₃:** a grain-level source of CP violation for ΔB = 2 processes at the geometrogenesis front, with the temperature behind the front below the washout scale (`CCEF_baryogenesis.md`).
    - Grains *can* carry CP violation (`CCEF_grain_CP.md`): complex phases in the ΔB = 2 junction, or a CP-odd junction-chirality coupling; frustrated junctions have a built-in chiral doublet.
    - But the current Hamiltonian is CP-symmetric, and a 16-grain exact test finds **no spontaneous chiral order**: junction handedness cancels on cooling, consistent with the literature on π-flux quantum spin ice.
    - CP violation would have to be added explicitly. **Open:** larger systems or other grain Hamiltonians; Branch M leptogenesis.
    - **Janus/CPT option worked out** (`CCEF_janus_cpt.md`): B = 0 at the Janus point and opposite asymmetries on the two sides are automatic. The CP-odd ingredient could sit in the Janus-point state, but crystallisation reheats to ~10¹⁹ GeV (`CCEF_reheat.md`), which scrambles that phase. **So CP violation must be in the laws**; the Janus mirror (antimatter on the other side) survives.
12. **The fork (Branch M vs L₃) is now central** (`CCEF_branchM.md`).
    - M explains the ripples and the matter excess and predicts proton decay plus 0νββ (~18 meV), but has no natural dark matter.
    - L₃ has the axion and Dirac neutrinos but fails the ripples and baryogenesis.
    - **Hybrid built** (`CCEF_hybrid.md`): Branch M plus a dark string-net sector. Asymmetric dark matter (~2.5–10 GeV) shares the leptogenesis asymmetry, which explains Ω_DM/Ω_b ≈ 5. The dark particle is stable by its own Gauss law.
    - It is the most complete package so far. **Open:** the dark mass, and Lorentz protection with γ ≳ 5–6.
13. **The Janus-branch fork** (§3.2): two-sided or multi-branch Janus point, and whether Λ's 4-volume count runs over our branch or all branches.
    - Needed: a rule fixing which 4-volume is conjugate to Λ in the timeless (Page–Wootters) description, and whether branches are counted before or after decoherence.
    - Under option (ii) the cosmic size L ≈ 0.1 (J_zz/J±)(2/k)^(1/3) D_LSS links the topology scale, the spin-ice coupling ratio and the number of branches.
    - **Strong CP, partial** (`CCEF_strong_cp.md`): diamond's inversion symmetry acts as parity on the grain fermions and exactly forbids the θ-type mass phase even with CP-violating couplings, so an axion-free "parity solution" is possible.
    - Still open: parity breaking in the chiral sector, and domain walls. Prediction: a neutron EDM near the next-generation reach.
    - **Parity breaking** (`CCEF_parity_breaking.md`):
      - A "breathing" of the grain crystal breaks P and C but conserves CP (the weak force's pattern) and creates no θ-type mass. It splits each fermion's left- and right-handed halves in momentum.
      - If set by the single seed, there are no domain walls. Natural left–right scale ~10¹³–10¹⁴ GeV, with possible cosmic strings Gμ ~ 10⁻¹²–10⁻¹⁰.
      - **Open:** a single-handed weak force (mirror gapping); θ̄ once breathing and CP phases overlap.
    - **Chiral weak force, route mapped** (`CCEF_chiral.md`):
      - Mirror partners can be gapped without left–right masses only if each generation has 16 Weyl fermions (ℤ₁₆ anomaly cancels), so the right-handed neutrino is required.
      - An exact toy shows interaction-only gapping works exactly when anomalies cancel (mod 8).
      - Design: breathing separates L/R; a mirror-only multi-fermion junction gaps the mirror copy at ~10¹³–10¹⁴ GeV.
      - **Not built:** emergent SU(2)/SU(3); full 3+1-d demonstration.

---

## 14. Methods, caveats and reproducibility
**Caveats (please read):**
- **Simplified statistics.** The DESI comparisons use projected Gaussian (w₀, w_a) summaries or compressed CMB distance priors, not full likelihoods. The neutrino fit omits CMB lensing; its ΛCDM limit is 103 meV vs DESI's 64 meV.
- **"Pre-registration" here** means code and numbers were frozen and hashed before the comparison step *within the working session*. The published results being compared against were in many cases broadly known to the AI assistant beforehand, so these are **not blind tests** in the strict sense. One registration was voided and redone after bugs were found; the voiding is recorded.
- **Literature values.** Some values (several S8 survey numbers, axion-string-simulation mass ranges, quantum-spin-ice α and crossover behaviour, Genzel dark-matter fractions) were quoted from the assistant's memory rather than freshly checked. They are marked in the companion documents and should be verified before citation.
- **Toy models.** The grain Hamiltonian runs are small (216 junctions), classical-limit simulated annealing for the geometry, and free-fermion band structures for the electrons. They demonstrate mechanisms; they are not a solution of the full quantum model.
- **No peer review.** Errors are likely. Issues and corrections are welcome.

**Environment:** Python 3.13, NumPy, SciPy, astropy-healpix. Planck maps are *not* included; download them from the Planck Legacy Archive.

**Companion files** (in the repository alongside this document):

| Topic | Code | Write-up |
|---|---|---|
| Math checks of V5 | `ccef_v5_checks.py` | `CCEF_V5_Reconciled.md` |
| β, torus and twisted-topology CMB tests; real-sky and masked fits; loopholes | `ccef_torus_cmb.py`, `ccef_topology_cmb.py`, `ccef_twist_fit.py`, `ccef_twist_fit_masked.py`, `ccef_loopholes.py` | `CCEF_beta_torus_results.md` |
| Spectral tilt | `ns_eta_test.py`, `ns_drift_test.py` | `CCEF_ns_eta_novelty_check.md` |
| Recruitment dark energy vs DESI | `ccef_recruitment_w.py`, `ccef_desi_compare.py` | `CCEF_DESI_results.md` |
| S2 / black holes; GW propagation | `ccef_s2_check.py`, `ccef_gw_check.py` | `CCEF_S2_check.md`, `CCEF_GW_check.md` |
| Spacetime jitter | `ccef_length_noise.py` | `CCEF_length_noise_results.md` |
| Proton decay; grain baryon; string-net rules | `ccef_proton_decay.py`, `ccef_grain_baryon.py`, `ccef_stringnet_rules.py` | `CCEF_proton_decay_results.md`, `CCEF_grain_baryon.md`, `CCEF_stringnet_rules.md` |
| Dirac neutrinos; neutrino-mass fit | `ccef_dirac_neutrino.py`, `ccef_numass_fit.py` | `CCEF_dirac_neutrino.md`, `CCEF_numass_fit_results.md` |
| Lensing / S8; apparent dark matter | `ccef_s8_lensing.py`, `ccef_grain_mond.py` | `CCEF_lensing.md` |
| Dark matter; monopoles | `ccef_dark_matter.py`, `ccef_monopole.py` | `CCEF_dark_matter.md`, `CCEF_monopole_problem.md` |
| Matter–antimatter asymmetry; grain CP violation; Janus/CPT | `ccef_baryogenesis.py`, `ccef_grain_cp.py`, `ccef_grain_chirality.py`, `ccef_janus_cpt.py` | `CCEF_baryogenesis.md`, `CCEF_grain_CP.md`, `CCEF_janus_cpt.md` |
| Reheating from crystallisation | `ccef_reheat.py` | `CCEF_reheat.md` |
| Primordial ripples without inflation | `ccef_ripples.py` | `CCEF_ripples.md` |
| Branch M package test (and the M vs L₃ comparison) | `ccef_branchM.py` | `CCEF_branchM.md` |
| Hybrid (Branch M + dark sector) | `ccef_hybrid.py` | `CCEF_hybrid.md` |
| Strong CP via grain parity | `ccef_strong_cp.py` | `CCEF_strong_cp.md` |
| How and where left↔right breaks | `ccef_parity_breaking.py` | `CCEF_parity_breaking.md` |
| Chiral weak force (mirror gapping) | `ccef_chiral.py` | `CCEF_chiral.md` |
| Weak and strong forces from grains (rishon links) | `ccef_nonabelian.py` | `CCEF_nonabelian.md` |
| Graviton from grains | `ccef_graviton.py` | `CCEF_graviton.md` |
| Local time (a clock at every junction) | `ccef_local_time.py` | `CCEF_local_time.md` |
| Grain rules as local update events | `ccef_grain_rules.py` | `CCEF_grain_rules.md` |
| Geometry rewiring as update events | `ccef_geometry_events.py` | `CCEF_geometry_events.md` |
| Energy-conserving crystallisation (light as the sink) | `ccef_geo_microcanonical.py` | `CCEF_microcanonical_growth.md` |
| Induced gravity: coordinate freedom, no elasticity, area law of grain fields | `ccef_induced_gravity.py` | `CCEF_induced_gravity.md` |
| N_ent first count (full grain field content, one cut) | `ccef_neff.py` | `CCEF_neff.md` |
| **N_ent derived** (orientation-averaged, edge entropy, current content only) | `ccef_nent.py` | `CCEF_nent.md` |
| Valleys as generations; SU(2)/SU(3) edge entanglement | `ccef_valleys_edges.py` | `CCEF_valleys_edges.md` |
| Electron rebuilt as a bundle constituent (Gauss law, Mott, flux, speed) | `ccef_electron_rebuild.py` | `CCEF_electron_rebuild.md` |
| Audit of frozen predictions after N_ent | `ccef_prediction_audit.py` | `CCEF_prediction_audit.md` |
| Rishon splitting (sub-structural bundling) as a rescue | `ccef_rishon_splitting.py` | `CCEF_rishon_splitting.md` |
| Light-sector window: photon phase vs rescue, electron speed and Mott check | `ccef_light_window.py` | `CCEF_light_window.md` |
| Grain Hamiltonian | `ccef_grain_hamiltonian_mc.py`, `ccef_gh_batch2.py` | `CCEF_grain_Hamiltonian.md` |
| Geometry ground state, glass, quantum annealing, seed growth | `ccef_geo_groundstate.py`, `ccef_geo_polytypes.py`, `ccef_geo_dynamics.py`, `ccef_geo_barriers.py`, `ccef_geo_ramp.py`, `ccef_geo_seed.py`, `ccef_geo_seed_big.py`, `ccef_geo_template_diag.py`, `ccef_geo_template.py` | `CCEF_geometry_groundstate.md` |
| Electrons | `ccef_grain_fermions.py`, `ccef_grain_fermion_nodes.py`, `ccef_grain_fermion_fluxsearch.py`, `ccef_grain_fkm.py`, `ccef_grain_lattice.py` | `CCEF_grain_electrons.md` |

**Freeze records** (full hashes in the `*_prereg_hash.txt` files):

| Item | Frozen (UTC, 2026-10-11) | File |
|---|---|---|
| DESI recruitment locus | 12:09:09 | `CCEF_DESI_prereg_hash.txt` |
| Spacetime jitter | 12:36:16 | `CCEF_length_noise_prereg_hash.txt` |
| Proton decay | 12:50:31 | `CCEF_proton_decay_prereg_hash.txt` |
| Dirac-neutrino predictions | 13:19:52 | `CCEF_dirac_neutrino_prereg_hash.txt` |
| Neutrino-mass fit (first hash voided; re-frozen) | 13:30:25 → **13:32:57** | `CCEF_numass_fit_prereg_hash.txt` |
| S8 lensing | 17:04:48 | `CCEF_s8_prereg_hash.txt` |
| Axion dark matter | 17:14:09 | `CCEF_dark_matter_prereg_hash.txt` |

---

## 15. Acknowledgements
- This work stands on decades of research by the authors listed in §1 and the references. Any merit in the combination belongs largely to them; any errors are ours.
- The derivations, code and analyses were produced with the AI model Claude (Anthropic), working interactively with the author.
- Data and results used: Planck Collaboration, DESI Collaboration, LIGO/Virgo/KAGRA, GRAVITY, Super-Kamiokande, Fermilab Holometer, KiDS, DES, HSC, ACT, MACRO, KATRIN, KamLAND-Zen, NuFIT.

---

## References
*Compiled with AI assistance; please verify details before formal citation.*

**Emergent geometry, gravity and time**
- T. Konopka, F. Markopoulou, L. Smolin, "Quantum graphity," arXiv:hep-th/0611197 (2006).
- T. Konopka, F. Markopoulou, S. Severini, "Quantum graphity: a model of emergent locality," Phys. Rev. D 77, 104029 (2008).
- A. Hamma, F. Markopoulou, I. Prémont-Schwarz, S. Severini, "Lieb–Robinson bounds and the speed of light from topological order," Phys. Rev. Lett. 102, 017204 (2009).
- T. Jacobson, "Thermodynamics of spacetime: the Einstein equation of state," Phys. Rev. Lett. 75, 1260 (1995).
- T. Jacobson, "Entanglement equilibrium and the Einstein equation," Phys. Rev. Lett. 116, 201101 (2016).
- T. Jacobson, "Black hole entropy and induced gravity," arXiv:gr-qc/9404039 (1994).
- L. Susskind, J. Uglum, Phys. Rev. D 50, 2700 (1994).
- A. D. Sakharov, "Vacuum quantum fluctuations in curved space and the theory of gravitation," Sov. Phys. Dokl. 12, 1040 (1968).
- S. Weinberg, E. Witten, "Limits on massless particles," Phys. Lett. B 96, 59 (1980).
- Z.-C. Gu, X.-G. Wen, arXiv:gr-qc/0606100 (2006); C. Xu, arXiv:cond-mat/0602443 (2006).
- D. N. Page, W. K. Wootters, Phys. Rev. D 27, 2885 (1983).
- P. A. Höhn, A. R. H. Smith, M. P. E. Lock, Phys. Rev. D 104, 066001 (2021).
- E. Moreva et al., Phys. Rev. A 89, 052122 (2014).
- J. Barbour, *The Janus Point* (Basic Books, 2020); J. Barbour, T. Koslowski, F. Mercati, Phys. Rev. Lett. 113, 181101 (2014).
- S. M. Carroll, J. Chen, arXiv:hep-th/0410270 (2004).
- P. Bocchieri, A. Loinger, Phys. Rev. 107, 337 (1957).
- C. Kelly, C. Trugenberger, F. Biancalana, "Self-assembly of geometric space from random graphs," Class. Quantum Grav. 36, 125012 (2019).
- J. Ambjørn, J. Jurkiewicz, R. Loll, "Emergence of a 4D world from causal quantum gravity," Phys. Rev. Lett. 93, 131301 (2004) (crumpled/branched phases of Euclidean triangulations and the causal fix).
- R. Martoňák, G. E. Santoro, E. Tosatti, "Quantum annealing of the traveling-salesman problem," Phys. Rev. E 70, 057701 (2004).

**Matter–antimatter and CP violation**
- A. D. Sakharov, JETP Lett. 5, 24 (1967).
- T. D. Lee, Phys. Rev. D 8, 1226 (1973).
- Ya. B. Zel'dovich, I. Yu. Kobzarev, L. B. Okun, Sov. Phys. JETP 40, 1 (1975).
- A. G. Cohen, A. De Rújula, S. L. Glashow, ApJ 495, 539 (1998).
- V. A. Kuzmin, V. A. Rubakov, M. E. Shaposhnikov, Phys. Lett. B 155, 36 (1985).
- A. G. Cohen, D. B. Kaplan, A. E. Nelson, Ann. Rev. Nucl. Part. Sci. 43, 27 (1993).
- M. Dine, R. G. Leigh, D. A. MacIntire, Phys. Rev. Lett. 69, 2030 (1992).
- K. Choi, D. B. Kaplan, A. E. Nelson, Nucl. Phys. B 391, 515 (1993).
- L. Freidel, D. Minic, T. Takeuchi, Phys. Rev. D 72, 104002 (2005).
- A. Perez, C. Rovelli, Phys. Rev. D 73, 044013 (2006).
- V. Kalmeyer, R. B. Laughlin, Phys. Rev. Lett. 59, 2095 (1987).
- X.-G. Wen, F. Wilczek, A. Zee, Phys. Rev. B 39, 11413 (1989).
- S. B. Lee, S. Onoda, L. Balents, Phys. Rev. B 86, 104412 (2012).
- F. J. Burnell, S. Chakravarty, S. L. Sondhi, Phys. Rev. B 79, 144432 (2009).
- L. Boyle, K. Finn, N. Turok, "CPT-symmetric universe," Phys. Rev. Lett. 121, 251301 (2018).
- I. Affleck, M. Dine, "A new mechanism for baryogenesis," Nucl. Phys. B 249, 361 (1985).

**Local time and causal update dynamics**
- S. A. Hojman, K. Kuchař, C. Teitelboim, "Geometrodynamics regained," Ann. Phys. 96, 88 (1976).
- R. Arnowitt, S. Deser, C. W. Misner, "The dynamics of general relativity," in *Gravitation: an introduction to current research* (1962) [arXiv:gr-qc/0405109].
- A. Bisio, G. M. D'Ariano, P. Perinotti, "Special relativity in a discrete quantum universe," Phys. Rev. A 94, 042120 (2016).
- P. Arrighi, S. Martiel, "Quantum causal graph dynamics," Phys. Rev. D 96, 024026 (2017).
- J. Gorard, "Some relativistic and gravitational properties of the Wolfram model," Complex Systems 29, 599 (2020).
- R. Gambini, J. Pullin, "Consistent discretization and loop quantum geometry," Phys. Rev. Lett. 94, 101302 (2005).
- L. Bombelli, J. Lee, D. Meyer, R. D. Sorkin, "Space-time as a causal set," Phys. Rev. Lett. 59, 521 (1987).
- G. Strang, "On the construction and comparison of difference schemes," SIAM J. Numer. Anal. 5, 506 (1968).
- N. Kato, S. Onoda, "Numerical evidence of quantum melting of spin ice: quantum-classical crossover," Phys. Rev. Lett. 115, 077202 (2015) [arXiv:1411.1918].
- C. R. Pace, S. C. Morampudi, R. Moessner, C. R. Laumann, "Emergent fine structure constant of quantum spin ice is large," Phys. Rev. Lett. 127, 117205 (2021) [arXiv:2009.04499].
- M. Hermele, M. P. A. Fisher, L. Balents, "Pyrochlore photons: the U(1) spin liquid in a S = 1/2 three-dimensional frustrated magnet," Phys. Rev. B 69, 064404 (2004).
- L. Hardy, "Towards quantum gravity: a framework for probabilistic theories with non-fixed causal structure," J. Phys. A 40, 3081 (2007).
- O. Oreshkov, F. Costa, Č. Brukner, "Quantum correlations with no causal order," Nat. Commun. 3, 1092 (2012).
- M. Zych, F. Costa, I. Pikovski, Č. Brukner, "Bell's theorem for temporal order," Nat. Commun. 10, 3772 (2019).
- L. Bombelli, R. K. Koul, J. Lee, R. D. Sorkin, "Quantum source of entropy for black holes," Phys. Rev. D 34, 373 (1986).
- M. Srednicki, "Entropy and area," Phys. Rev. Lett. 71, 666 (1993).
- D. Kabat, "Black hole entropy and entropy of entanglement," Nucl. Phys. B 453, 281 (1995).
- H. Kleinert, J. Zaanen, "World nematic crystal model of gravity explaining absence of torsion in spacetime," Phys. Lett. A 324, 361 (2004).
- G. Dvali, "Black holes and large N species solution to the hierarchy problem," Fortsch. Phys. 58, 528 (2010).
- M. Creutz, "Microcanonical Monte Carlo simulation," Phys. Rev. Lett. 50, 1411 (1983).
- C. Kipnis, C. Marchioro, E. Presutti, "Heat flow in an exactly solvable model," J. Stat. Phys. 27, 65 (1982).

**Emergent gravitons**
- M. Fierz, W. Pauli, Proc. R. Soc. Lond. A 173, 211 (1939).
- B. S. DeWitt, "Quantum theory of gravity. I. The canonical theory," Phys. Rev. 160, 1113 (1967).
- O. Benton, L. D. C. Jaubert, H. Yan, N. Shannon, "A spin-liquid with pinch-line singularities on the pyrochlore lattice," Nat. Commun. 7, 11572 (2016).
- M. Pretko, "Emergent gravity of fractons: Mach's principle revisited," Phys. Rev. D 96, 024051 (2017).
- E. Álvarez, D. Blas, J. Garriga, E. Verdaguer, "Transverse Fierz–Pauli symmetry," Nucl. Phys. B 756, 148 (2006).
- A. J. Beekman, J. Nissinen, K. Wu, J. Zaanen, "Dual gauge field theory of quantum liquid crystals in three dimensions," Phys. Rev. B 96, 165115 (2017).
- H. Kleinert, "Gravity as a theory of defects in a crystal with only second-gradient elasticity," Ann. Phys. (Leipzig) 499, 117 (1987).

**Non-abelian gauge fields from finite degrees of freedom**
- R. Brower, S. Chandrasekharan, U.-J. Wiese, "QCD as a quantum link model," Phys. Rev. D 60, 094502 (1999).
- D. Banerjee et al., "Atomic quantum simulation of U(N) and SU(N) non-Abelian lattice gauge theories," Phys. Rev. Lett. 110, 125303 (2013).
- T. Byrnes, Y. Yamamoto, "Simulating lattice gauge theories on a quantum computer," Phys. Rev. A 73, 022328 (2006).
- E. Zohar, J. I. Cirac, B. Reznik, "Quantum simulations of lattice gauge theories using ultracold atoms in optical lattices," Rep. Prog. Phys. 79, 014401 (2016).

**Chiral fermions and symmetric mass generation**
- E. Eichten, J. Preskill, "Chiral gauge theories on the lattice," Nucl. Phys. B 268, 179 (1986).
- L. Fidkowski, A. Kitaev, "Effects of interactions on the topological classification of free fermion systems," Phys. Rev. B 81, 134509 (2010).
- J. Wang, X.-G. Wen, "Non-perturbative regularization of 1+1D anomaly-free chiral fermions and bosons," arXiv:1307.7480 (2013).
- S. S. Razamat, D. Tong, "Gapped chiral fermions," Phys. Rev. X 11, 011063 (2021).
- D. Tong, "Comments on symmetric mass generation in 2d and 4d," JHEP 07, 001 (2022).
- K. Slagle, Y.-Z. You, C. Xu, Phys. Rev. B 91, 115121 (2015).

**Strong CP**
- A. E. Nelson, Phys. Lett. B 136, 387 (1984); S. M. Barr, Phys. Rev. Lett. 53, 329 (1984).
- K. S. Babu, R. N. Mohapatra, "A solution to the strong CP problem without an axion," Phys. Rev. D 41, 1286 (1990).
- S. M. Barr, D. Chang, G. Senjanović, "Strong CP problem and parity," Phys. Rev. Lett. 67, 2765 (1991).
- C. Abel et al. (nEDM at PSI), "Measurement of the permanent electric dipole moment of the neutron," Phys. Rev. Lett. 124, 081803 (2020).

**Dark sectors and asymmetric dark matter**
- M. Pospelov, A. Ritz, M. Voloshin, "Secluded WIMP dark matter," Phys. Lett. B 662, 53 (2008).
- J. L. Feng, J. Kumar, "The WIMPless miracle," Phys. Rev. Lett. 101, 231301 (2008).
- D. E. Kaplan, M. A. Luty, K. M. Zurek, "Asymmetric dark matter," Phys. Rev. D 79, 115016 (2009).

**Primordial perturbations without inflation**
- R. H. Brandenberger, C. Vafa, "Superstrings in the early universe," Nucl. Phys. B 316, 391 (1989).
- A. Nayeri, R. H. Brandenberger, C. Vafa, Phys. Rev. Lett. 97, 021302 (2006).
- J. Magueijo, L. Smolin, C. R. Contaldi, Class. Quantum Grav. 24, 3691 (2007).
- N. Afshordi, J. Magueijo, Phys. Rev. D 94, 101301 (2016).
- F. Markopoulou, L. Smolin, "Disordered locality in loop quantum gravity states," Class. Quantum Grav. 24, 3813 (2007).
- C. Prescod-Weinstein, L. Smolin, "Disordered locality as an explanation for the dark energy," Phys. Rev. D 80, 063505 (2009).
- K. Dick, M. Lindner, M. Ratz, D. Wright, Phys. Rev. Lett. 84, 4039 (2000).
- H. Murayama, A. Pierce, Phys. Rev. Lett. 89, 271601 (2002).

**Dark energy and discreteness**
- M. Ahmed, S. Dodelson, P. B. Greene, R. Sorkin, "Everpresent Λ," Phys. Rev. D 69, 103523 (2004).
- R. D. Sorkin, AIP Conf. Proc. 957, 142 (2007).
- N. Zwane, N. Afshordi, R. D. Sorkin, Class. Quantum Grav. 35, 194002 (2018).
- L. Bombelli, J. Henson, R. D. Sorkin, Mod. Phys. Lett. A 24, 2579 (2009).

**Gauge fields and fermions from qubits**
- M. Levin, X.-G. Wen, "Fermions, strings, and gauge fields in lattice spin models," Phys. Rev. B 67, 245316 (2003).
- M. Levin, X.-G. Wen, "String-net condensation," Phys. Rev. B 71, 045110 (2005).
- M. Levin, X.-G. Wen, "Colloquium: Photons and electrons as emergent phenomena," Rev. Mod. Phys. 77, 871 (2005).
- M. Hermele, M. P. A. Fisher, L. Balents, "Pyrochlore photons," Phys. Rev. B 69, 064404 (2004).
- O. I. Motrunich, T. Senthil, Phys. Rev. Lett. 89, 277004 (2002).
- S. Chandrasekharan, U.-J. Wiese, "Quantum link models," Nucl. Phys. B 492, 455 (1997).
- S. B. Bravyi, A. Yu. Kitaev, "Fermionic quantum computation," Ann. Phys. 298, 210 (2002).
- L. Fu, C. L. Kane, E. J. Mele, "Topological insulators in three dimensions," Phys. Rev. Lett. 98, 106803 (2007).
- H. B. Nielsen, M. Ninomiya, Nucl. Phys. B 185, 20 (1981).
- J. Kogut, L. Susskind, Phys. Rev. D 11, 395 (1975).
- J. Wang, X.-G. Wen, "A non-perturbative definition of the Standard Models," Phys. Rev. Research 2, 023356 (2020).
- I. García-Etxebarria, M. Montero, "Dai–Freed anomalies in particle physics," JHEP 08, 003 (2019).
- Quantum-spin-ice crossover and emergent α: Y. Kato, S. Onoda, Phys. Rev. Lett. 115, 077202 (2015); S. D. Pace et al., Phys. Rev. Lett. 127, 117205 (2021).

**Lorentz symmetry**
- S. Chadha, H. B. Nielsen, Nucl. Phys. B 217, 125 (1983).
- G. Bednik, O. Pujolàs, S. Sibiryakov, JHEP 11, 064 (2013).
- S. Groot Nibbelink, M. Pospelov, Phys. Rev. Lett. 94, 081601 (2005).
- J. Collins et al., Phys. Rev. Lett. 93, 191301 (2004).
- S. Coleman, S. L. Glashow, Phys. Rev. D 59, 116008 (1999).
- D. Mattingly, Living Rev. Relativ. 8, 5 (2005).
- LHAASO Collaboration, Phys. Rev. Lett. 133, 071501 (2024).

**Cosmology and primordial spectrum**
- Planck Collaboration, "Planck 2018 results. VI," A&A 641, A6 (2020).
- L. Chen, Q.-G. Huang, K. Wang, "Distance priors from Planck final release," JCAP 02, 028 (2019).
- DESI Collaboration, "DESI DR2 results II: BAO and cosmological constraints," arXiv:2503.14738 (2025).
- É. Aubourg et al., Phys. Rev. D 92, 123516 (2015).
- D. J. Eisenstein, W. Hu, ApJ 496, 605 (1998).
- N. Irges, A. Kalogirou, F. Koutroulis, "Ising cosmology," Eur. Phys. J. C 83, 431 (2023); Universe 9, 434 (2023).
- F. Kos, D. Poland, D. Simmons-Duffin, A. Vichi, JHEP 08, 036 (2016); S. M. Chester et al., Phys. Rev. D 104, 105013 (2021).
- COMPACT Collaboration (cosmic topology), e.g. Y. Akrami et al., Phys. Rev. Lett. 132, 171501 (2024).

**Gravitational tests and spacetime noise**
- LIGO/Virgo/Fermi/INTEGRAL, ApJL 848, L13 (2017) (GW170817).
- LIGO/Virgo/KAGRA, "Tests of GR with GWTC-3," arXiv:2112.06861.
- GRAVITY Collaboration, A&A 636, L5 (2020).
- E. Verlinde, K. Zurek, "Observational signatures of quantum gravity in interferometers," arXiv:1902.08207 (2019).
- K. Lee et al. (Holometer), Phys. Rev. D 108, 064038 (2023).
- GQuEST design, Phys. Rev. X 15, 011034 (2025).
- E. S. Perlman et al., ApJ 805, 10 (2015).
- M. Kardar, G. Parisi, Y.-C. Zhang, Phys. Rev. Lett. 56, 889 (1986).

**Particle physics: protons, neutrinos, axions, monopoles**
- S. Weinberg, Phys. Rev. Lett. 43, 1566 (1979).
- L. E. Ibáñez, G. G. Ross, Phys. Lett. B 260, 291 (1991); Nucl. Phys. B 368, 3 (1992).
- Super-Kamiokande, Phys. Rev. D 102, 112011 (2020) [arXiv:2010.16098].
- L. Hall, H. Murayama, N. Weiner, Phys. Rev. Lett. 84, 2572 (2000).
- N. Arkani-Hamed, S. Dimopoulos, G. Dvali, J. March-Russell, Phys. Rev. D 65, 024032 (2002).
- I. Esteban et al. (NuFIT 6.0), JHEP 12, 216 (2024).
- KamLAND-Zen, Phys. Rev. Lett. 130, 051801 (2023).
- KATRIN Collaboration, Science 388, 180 (2025).
- R. D. Peccei, H. R. Quinn, Phys. Rev. Lett. 38, 1440 (1977); S. Weinberg, Phys. Rev. Lett. 40, 223 (1978); F. Wilczek, Phys. Rev. Lett. 40, 279 (1978).
- J. E. Kim, Phys. Rev. Lett. 43, 103 (1979); M. Shifman, A. Vainshtein, V. Zakharov, Nucl. Phys. B 166, 493 (1980).
- M. Buschmann et al., Nature Commun. 13, 1049 (2022); M. Gorghetto, E. Hardy, G. Villadoro, SciPost Phys. 10, 050 (2021); K. Saikawa et al., arXiv:2401.17253 (2024).
- T. W. B. Kibble, J. Phys. A 9, 1387 (1976); W. H. Zurek, Nature 317, 505 (1985); J. Preskill, Phys. Rev. Lett. 43, 1365 (1979).
- MACRO Collaboration, Eur. Phys. J. C 25, 511 (2002).
- J. Polchinski, "Monopoles, duality, and string theory," Int. J. Mod. Phys. A 19S1, 145 (2004).

**Dark matter, lensing and galaxies**
- E. Verlinde, "Emergent gravity and the dark universe," SciPost Phys. 2, 016 (2017).
- D. Clowe et al., ApJ 648, L109 (2006).
- S. McGaugh, F. Lelli, J. Schombert, Phys. Rev. Lett. 117, 201101 (2016); F. Lelli et al., ApJ 836, 152 (2017).
- M. Brouwer et al., A&A 650, A113 (2021).
- R. Genzel et al., Nature 543, 397 (2017); ApJ 902, 98 (2020).
- A. H. Wright et al. (KiDS-Legacy), arXiv:2503.19441 (2025).
- DES Collaboration, Phys. Rev. D 105, 023520 (2022).
- X. Li et al. (HSC Y3), Phys. Rev. D 108, 123518 (2023).
- M. Madhavacheril et al. (ACT DR6 lensing), ApJ 962, 113 (2024).
- C. Carney et al., "Proposal for gravitational direct detection of dark matter," Phys. Rev. D 102, 072003 (2020).

---

*License and reuse: as per the repository. Corrections, critiques and refutations are welcome.*
