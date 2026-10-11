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
1. derive a few consequences (a finite cosmic volume about one CMB diameter across; cyclic expansion through recruitment of grains from a finite reservoir);
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

$$G=\frac{\ell^2}{4\eta_g},\qquad \eta_g=\frac{N_{\rm eff}}{24\pi}\ \text{(matching Sakharov induced gravity)}.$$

- With N_eff ≈ 9 this gives ℓ ≈ 1.1×10⁻³⁵ m and M ≈ 1.77×10¹⁹ GeV.
- Whether the network carries a propagating spin-2 graviton is **[OPEN]**.
- Counting U(1) flux through a horizon gives S = A/4G − ½ ln(A/ℓ²) **[COMPUTED counting; COND physics]**.

### 3.2 Dark energy from the grain count [COND; magnitude ESTABLISHED by Sorkin]
- Treat Λ as conjugate to the 4-volume V₄ = N₄ℓ⁴. Poisson counting gives ρ_Λ ~ 1/(ℓ²√V₄), and Λℓ_P² ~ 10⁻¹²² as observed.
- V5 uses the *global* (whole-cycle) 4-volume, so Λ is constant within a cycle **[FORK]**.
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
- Requiring the past 4-volume not to exceed the cycle's 4-volume bounds the side of a flat 3-torus: **L ≤ 2.15 β^{2/3} D_LSS** (N_eff = 9).
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

**Reading:**
- 3-D space is **not automatic**. Light's own preference (many small rings) crumples space. An explicit rule against over-connection, "two points cannot be joined by too many independent short routes", is needed.
- Mapping M ↔ J_zz and Λ* ↔ J_ring, the hierarchy Λ*/M ≈ 4×10⁻⁹ corresponds to **J_±/J_zz ≈ 7×10⁻⁴**, deep inside the Coulomb phase.
- Quantum spin ice is reported to enter its Coulomb phase through a thermal crossover, which is the gentle switch-on the monopole argument needs (literature, quoted from memory).

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

**Shortfalls:**
- these are vector-like (QED-type), not chiral (Standard Model-type) fermions;
- masses are not yet tied to a Higgs field;
- the isotropy and equal-speed-with-light conditions are tunings **[OPEN]**.

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
| ΔN_eff ∈ {0, 0.06, 0.14} | ΔN_eff ≳ 0.3 | Simons Observatory, CMB-S4 |
| **Axion dark matter, m_a ≈ 74 μeV (14–400; ~3–100 GHz)** | nothing in that band; any WIMP signal | MADMAX, ALPHA, ORGAN, BREAD |
| Branch M alternative: p → μ⁺π⁰ ≈ e⁺π⁰ | GUT-like μ⁺π⁰ ≪ e⁺π⁰ | Hyper-K |
| Entanglement-gravity interferometer noise at natural amplitude | exclusion with the correct spectral model | GQuEST |
| Finite volume ~(1–1.5 D_LSS)³ | no topology down to ~1.5 D_LSS | LiteBIRD, COMPACT methods |

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
3. **The right-handed neutrino keeps reappearing.** ℤ₃ lepton triality forces Dirac neutrinos, so ν^c must exist. Defining a chiral Standard Model on a lattice by gapping mirror fermions is believed to need 16 Weyl fermions per generation, which also means ν^c.
4. **cH₀/6 ≈ 1.1×10⁻¹⁰ m s⁻²** lies within 10% of the MOND acceleration a₀. Verlinde noticed this; the grain picture gives it a natural home but does not derive it, and the full apparent-dark-matter idea fails here.
5. **A cubed hierarchy.** The ~10⁹ gap between the grain scale and the crossover scale corresponds to one modest ratio (≈ 7×10⁻⁴) cubed in the spin-ice mapping.
6. **"Spin-½ is required"** for relativistic electrons on the grain graph. That is consistent with nature, though it is a known theorem in a new setting.
7. **The gentle switch-on.** The same smooth emergence that avoids monopoles leaves the gapless axion phase scrambled. That produces exactly the axion-string ("post-inflation") scenario the dark-matter estimate assumed.
8. **m_ν ~ ρ_Λ^{1/4} ≈ 2 meV** (a well-known numerology). As a dynamical mechanism it is excluded here: it would make neutrinos about 0.3 eV at recombination.

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
- **Spinless electrons:** always nodal lines (512/512).
- **v3.9 errata applied:** the helicity identity is (1/4π²)∫a∧da = B (not B²); the ordered-phase vector mass is 214 MeV (not 152).

---

## 13. Open problems
1. Derive Lorentz protection (γ ≳ 3, or alternatives) from the Hamiltonian.
2. Prove (or refute) that 3-D diamond is the ground state of the geometry sector; understand the glassy dynamics and whether quantum rewiring anneals the defects.
3. A primordial spectrum (amplitude and tilt) without inflation.
4. SU(2) × SU(3) from grains, for example through bundles of grains per relation (rishon / quantum-link constructions).
5. Chiral fermions: mirror-fermion gapping, and Higgs-linked masses.
6. The emergent fine-structure constant (≈ 0.08 in spin ice vs ≈ 0.013 needed).
7. A propagating graviton from fluctuations of the relational graph.
8. The recruitment and halting dynamics from first principles.
9. A real dark-matter mechanism: the axion's origin and quality problem.
10. The thermal history (T_max vs Λ*), which sets the monopole, ν^c and axion outcomes.

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
| Grain Hamiltonian | `ccef_grain_hamiltonian_mc.py`, `ccef_gh_batch2.py` | `CCEF_grain_Hamiltonian.md` |
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
