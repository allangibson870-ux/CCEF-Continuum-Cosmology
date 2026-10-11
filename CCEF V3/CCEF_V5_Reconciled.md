# CCEF V5: the reconciled framework

**Constrained Cellular Emergence Framework, version 5 (2026-10-11).** Author: Allan Gibson; prepared with Claude (Anthropic).

**Combines:**
- `CCEF_Reference_v3.9.txt` (July 2026, the matter and hadronic program);
- `CCEF_V4/CCEF_V4_Cellular_Emergence.tex` (V4.1: grains, relational time, entanglement gravity, Lorentz protection);
- `CCEF_derived_additions.md`, `CCEF_beta_torus_results.md` (finite volume, β, topology tests);
- `CCEF_ns_eta_novelty_check.md` (tilt analysis).

**Reviewed in:** `CCEF_v3.9_review.md`. **Math checked by:** `ccef_v5_checks.py` (39 PASS / 2 FAIL in v3.9, both fixed here / 1 note).

**Labels (as in v3.9):** [SOLID] verified · [COND] conditional · [ANSATZ] assumed · [OPEN] unknown · [NEG] shown to fail · [FORK] a choice V5 makes explicitly · [TEST] a falsifiable output.

---

## 0. One-paragraph summary
The universe is a **finite network of grains** (qubits joined by quantum-link gauge spins) with no fundamental time. Below the grain scale ℓ ≈ 1.1×10⁻³⁵ m, the network's entanglement produces **Einstein gravity** with the observed G, and fluctuations in the number of grains produce **dark energy of the observed size**. The universe is born when the network crystallises into 3D space (**geometrogenesis**), and expansion is grains joining that space from a finite reservoir, so **cycles are derived**. Inside the geometric phase, at the hadronic scale (Λ = 231 MeV), lives v3.9's **S³ order parameter**: baryons are Skyrmions, and the Hopf base/fiber structure links baryon number to a vector-field helicity. The finite grain count fixes the **volume of the universe at about one CMB diameter**, a prediction that is testable now. Planck's large-angle sky is consistent with it but does not support it: an apparent lean towards a half-turn (E2) shape disappeared once the choice of shape was included in the statistics (P = 0.79).

---

## 1. Principles
- **P1 Finiteness.** N grains, finite Hilbert space, no physical infinities. *(V4)*
- **P2 Grains are qubits.** Their state space CP¹ is v3.9's order-parameter manifold.
- **P3 Space is a pattern** of grain connectivity; distance, dimension and locality emerge.
- **P4 Time is relational:** a global constraint Ĥ|Ψ⟩ = 0, with time read off internal clocks (Page–Wootters); arrow from coarse-grained entropy, Big Bang = Janus point.
- **P5 Emergence:** gravity, gauge fields, fermions and Lorentz symmetry are low-energy collective properties.
- **P6 Cycles without a master clock** (now *derived*; §5.3).
- **P7 One grain type (adopted 2026-10-11).** Different grain types would each need a further explanation: an infinite regress. All particles are patterns of one kind of grain, so baryon and lepton numbers are accidental, not fundamental.
- **Working principle (from v3.9):** derive from the action; label honestly; flag every fit; never tune a coefficient to hit a target.

**Replaced from v3.9:** "one infinite, eternal continuum on a fixed flat manifold" becomes a finite network. The continuum S³ field survives as an **effective field theory** of the geometric phase (§3).

---

## 2. Layer 1 (Planck scale): grains, gravity, dark energy, Lorentz symmetry

### 2.1 Gravity from grain entanglement [SOLID mechanism; COND realisation]
- **Area law:** S_ent = η_g A/ℓ². With Jacobson's equation of state this gives Einstein's equations with **G = ℓ²/(4η_g)**.
- **Consistency with induced gravity (check D1, exact):** this equals v3.9's M_Pl² = N_eff M²/48π² with M = 1/ℓ, provided η_g = N_eff/(24π).
- **Numbers:** N_eff ≈ 9 gives **ℓ = 1.1×10⁻³⁵ m** and **M = 1.77×10¹⁹ GeV**, v3.9's own non-locality scale (check C6).

**Graviton (this resolves v3.9 issue 1):** the graviton is *not* a bound state of the hadronic field. It is either the metric of Sakharov induced gravity or a collective mode of the grain network, whose Lorentz invariance is only emergent. Either way the Weinberg–Witten theorem does not apply. **Whether a propagating spin-2 mode exists in the network is [OPEN].**

**Scale mismatch (resolves v3.9 issue 2):** gravity no longer comes from the 122.5 MeV field, so the "44 uncomputable e-folds" disappear. G comes from the grain scale directly.

### 2.2 Dark energy from the grain count [COND, magnitude SOLID]
In unimodular form, Λ is conjugate to the total 4-volume, and V₄ = N₄ℓ⁴ (one grain-tick = ℓ⁴):
- **Fluctuation:** ΔV₄·Δρ_Λ ≥ ½. With Poisson counting, **σ(ρ_Λ) = 1/(2ℓ²√V₄)** (check D10).
- **Magnitude:** Λℓ_P² ~ N^(−½) ~ 10⁻¹²², against 2.9×10⁻¹²² observed (check D3).
- **[FORK] Global vs causal volume.** V5 adopts the *global* (whole-cycle) 4-volume: Λ is constant within a cycle and avoids the early-universe problem of Sorkin's causal version. The cost: w = −1 within a cycle, which DESI could contradict (§7).

### 2.3 Gauge fields and fermions [COND]
- **Photon:** a quantum-link / string-net U(1) of the grain network, Coulomb phase (V4).
- **Fermions:** string-net endpoints (Levin–Wen).
- A Standard-Model-like string-net is [OPEN].

### 2.4 Lorentz protection [COND]
Every species emerges from one network, so all share one light cone. v3.9 had the same insight ("one order parameter gives c_grav = c_matter").

**Mechanism A:** strong-coupling flow, with leftover Lorentz violation shrinking as (E/M)^γ.
- Requirements: γ ≳ 1.2 (laboratory) and γ ≳ 2.8 (cosmic rays) (check D5).

**Mechanism B:** emergent supersymmetry suppresses it to (m_s/M)²: 3×10⁻³¹ at m_s = 10 TeV.
- Prediction: superpartners between about 1 TeV and 5.6×10⁷ GeV (check D6).

**Fallback:** random (causal-set-like) grains.

### 2.5 Black-hole entropy [SOLID counting; COND physics]
U(1) quantum-link flux through a horizon, with one global Gauss constraint, gives **S = A/4G − ½ ln(A/ℓ²)** (check D8). Loop quantum gravity's SU(2) closure gives −3/2.

---

## 3. Layer 2 (hadronic scale): v3.9's S³ field as the matter EFT

### 3.1 What carries over [SOLID within the EFT]
- **The action** S[z], z ∈ S³: A₁ = Z_t = 1, A₂ = 0.3268, A₄ = 3.5553, Skyrme c₄ ≈ 0.028 (one fit), calibrated so Λ = 231 MeV and E₀ = 122.5 MeV.
- **The CP¹ identities** (checks A1–A4).
- **Baryons** = Skyrme solitons (π₃(S³) = Z), fermionic via π₄(S³) = Z₂ (Finkelstein–Rubinstein), isospin rotor tower (N, Δ).
- **The cross-sector topology, corrected:** (1/4π²)∫a∧da = **B**, not B² (check B1). The Hopf charge of the projected field equals the baryon number.

### 3.2 [FORK] What is the Hopf-fiber vector? (resolves v3.9 issue 5)
v3.9 needs the universe *disordered* (massless photon = Hopf fiber) and *ordered* (Skyrmion baryons) in the same field. V5 lays out two options:

| | **Fork B (adopted)** | Fork A (alternative) |
|---|---|---|
| Photon | grain-network quantum-link U(1) (§2.3) | Hopf fiber in the disordered melt (v3.9) |
| Hopf-fiber vector | hadronic **hidden-local-symmetry vector meson** in the ordered S³ phase | the photon |
| Baryons | Skyrmions of the ordered field, **consistent** | need another home: **inconsistent as written** |
| Helicity link (1/4π²)∫a∧da = B | about the *vector-meson* field, a hadronic statement | about *EM*: baryogenesis = helical magnetogenesis, CMB TB/EB [TEST] |
| Status | consistent; loses the CMB helicity prediction | keeps the prediction; requires resolving the phase contradiction |

**Vector mass (fixes v3.9 issue 4):** from v3.9's own action, m² = A₁/A₂, giving **214 MeV** (not 152). That's still not the ρ (775 MeV), so **Fork B requires recalibrating** A₁/A₂ to the vector-meson spectrum. In Fork B the ratio A₁/A₂ is fixed by m_ρ, which removes one free choice. The HLM transition numbers (v3.9 §16.13.1) change by the corrected factor (E ×2.83).

### 3.3 Leptons and neutrinos [ANSATZ; FORK]
- **Option L1:** string-net fermions (V4), with masses [OPEN].
- **Option L2:** v3.9's M-sector lepton construction (17.3 + Part X): N_g = 3 = dim(adjoint), census exact, m_ν = Λ²/√(MΛ) = 0.026 eV (check C12; observed 0.05 eV), electron tuned at about 1 in 450.
  - **Conflict:** the M-sector's angular inflaton (f ≈ 7.3 M_Pl) would drive about 100 e-folds of inflation, making the universe far larger than §5.2 allows. L2 is compatible with V5 only if that mode was never displaced (no inflation).
- V5 keeps L2's structural results (Witten-anomaly content, generation count) as a candidate. It does not adopt M-sector inflation.

---

## 4. Time, entropy, cycles (from V4)
- **Relational time:** Page–Wootters with finite clocks, so time is grainy too. [SOLID mechanism]
- **Arrow of time:** coarse-grained entropy; geometrogenesis is a **Janus point**.
- **Recurrence:** a finite system returns arbitrarily close to earlier states (Bocchieri–Loinger), and no clock survives between cycles, so "how many cycles" has no physical answer.

---

## 5. Cosmology

### 5.1 Geometrogenesis Big Bang [COND]
The Big Bang is the pre-geometric to geometric transition.
- **Horizon problem:** solved by pre-geometric all-to-all connectivity.
- **Flatness:** conjectured from crystallisation.
- **Replaces:** v3.9's interface/bubble cosmology (closed by its own birth theorem, 16.15.6) and its M-sector inflation.
- **Requirement:** the transition must *not* be mean-field (group-field-theory analyses find mean-field, which would mean η = 0).

### 5.2 Finite volume from Λ [SOLID derivation; TEST]
- **Inputs:** ρ_Λ = β/(ℓ²√V₄,cycle) with **β derived = |x|/2** (median 0.34), plus cycle consistency (the past 4-volume can't exceed the cycle's).
- **Result:** the side of a flat 3-torus satisfies **L ≤ L_max = 2.15 β^⅔ D_LSS** (N_eff = 9; 3.18 for N_eff = 5).
- **Median L_max = 1.04 D_LSS (N_eff = 9) or 1.54 D_LSS (N_eff = 5)** (check D9). The universe should be about one CMB diameter across.
- **Remaining time:** expansion halts within roughly 1–25 Gyr (sooner for larger universes; table in `CCEF_beta_torus_results.md`).

### 5.3 Cycles derived [COND]
Constant G means constant ℓ, so expansion requires recruiting grains. A finite N means the reservoir empties: expansion halts, the network re-melts, and a new cycle begins. As recruitment slows, the effective dark energy should weaken first (the direction DESI hints at; unmodelled).

### 5.4 Large-angle CMB tests (computed) [TEST]
| Test | Result |
|---|---|
| Cubic torus, L = 1–2 D_LSS | allowed; no anomaly relief (P ≈ ΛCDM) |
| **E2 half-turn, V^⅓ = 1.0 D, L₃ = 0.7 D** | allowed (nearest image 1.10 D); P(low quadrupole) 0.104 vs 0.046; P(low S₁/₂) 0.149 vs 0.075; **about 2× relief** |
| E3 quarter-turn | no relief |
| **E2 axis fitted to Planck SMICA (real sky)** | Δ = +10.4; P(≥ \| ΛCDM) = 0.14; likelihood ratio E2:ΛCDM ≈ **1.6**; axis (l, b) = (7°, −81°), 23° from the quadrupole–octopole axis and **9° from the Galactic pole (foreground warning)** |
| **LOOPHOLES CLOSED (supersedes the rows below)** | With the model choice included (best of 11 allowed shapes, the same procedure for data and 300 ΛCDM skies): **P = 0.79, so no signal.** The earlier lean came from selecting E2 with L₃ = 0.7 D using the same anomaly statistics. ΛCDM skies put fitted axes near the Galactic pole only about 1% of the time, so the near-pole axis is a coincidence or a Galactic/systematic effect, not topology. See `CCEF_beta_torus_results.md` Part 5 |
| **E2, Galactic plane cut (masked likelihood, SMICA raw)** | \|b\| < 20°: Δ = +9.08, P(≥ \| ΛCDM) = **0.08**, likelihood ratio **1.6**; \|b\| < 30°: P = 0.20, ratio 1.2; axis stable to ≤ 6° in all fits. **Not an inpainting artifact**; weak but stable |
| **E2 axis fitted to Planck Commander** | Δ = +10.7; P(≥ \| ΛCDM) = 0.10; likelihood ratio ≈ **1.7**; axis (189°, +81°): **the same as SMICA to 0.3°.** Not a method-specific artifact; a common Galactic-plane effect not yet excluded (masked fit pending) |

### 5.5 Primordial perturbations [OPEN]
- **n_s = 1 − η is prior art** (Irges–Kalogirou–Koutroulis 2023) and **does not follow at the critical point.** The counting rule n_s − 1 = 6 − 2Δ needs an operator with Δ = 3 + η/2, and none exists in the Ising or O(3) spectrum (v3.9 Sec 16.1 reached the same conclusion).
- **Near-critical drift** gives the consistency relation **α_s = ±y(n_s − 1)**: relevant drift is excluded at 9σ and irrelevant drift disfavoured at 3.7σ (check D4). A lattice run confirms the drift, with no Planck-compatible window. Only a nearly marginal operator survives (O(3) cubic anisotropy, y ≈ 0.01), and then n_s becomes a fitted amplitude.
- **v3.9's topological seed** (A_s = 2.4×10⁻⁹; arithmetic checked, C18) relies on the M-sector inflation conveyor. **It does not carry over** to V5's no-inflation cosmology. n_s = 1 exactly (v3.9's "owned" value) is excluded at 8.4σ.

---

## 6. Ledger
| Category | Items |
|---|---|
| **Fits** | c₄ (baryon mass); A₁/A₂ recalibrated to the vector meson (Fork B) |
| **Inputs** | N_eff (5–9; the explicit count is [OPEN]); network couplings |
| **Derived outputs** | ℓ and M (from G); size of ρ_Λ; β; L_max; cycles; −½ ln A |
| **Tunings** | m_e (only if lepton option L2) |
| **Conceded** | none (v3.9 conceded Λ; V5 derives its magnitude) |

---

## 7. Predictions and falsifiers
| V5 expects | Would count against V5 | Probe |
|---|---|---|
| Finite universe, volume ≈ (1–1.5 D_LSS)³, twisted shape favoured | No topology signal down to about 1.5 D_LSS with improved methods | COMPACT, Planck/LiteBIRD maps, Euclid |
| *(Retracted 2026-10-11: the "E2 lean" has no significance once model choice is counted, P = 0.79)* | — | — |
| **Grain recruitment (mass action, pre-registered 2026-10-11): thawing w(z) ≥ −1, 1 + w ∝ a³, locus w_a ≈ −1.75(1 + w₀).** DESI DR2: beats ΛCDM with Union3 (Δχ² 5.6) and DESY5 (Δχ² 9.1); 2–3σ tension with DESI's phantom-preferring best fits (`CCEF_DESI_results.md`) | **Confirmed phantom crossing (w < −1 at z ≳ 0.5)** | DESI DR3+, Euclid, Rubin |
| No Lorentz violation in current data; any future signal ∝ E^γ, γ ≳ 3 | Linear dispersion | LHAASO, CTA |
| **Proton decay (pre-registered 2026-10-11, P7):** τ(p → e⁺π⁰) = 8.7×10³⁵ yr (Λ*/10¹⁶)⁴/C², μ⁺π⁰ ≈ e⁺π⁰. **Super-K (> 2.4×10³⁴ yr) excludes Λ* = 4×10¹¹ (Mechanism A, γ = 3), 3×10¹⁴ and 6×10¹⁴ GeV (neutrino link) → Λ* ≥ 4×10¹⁵ GeV;** Addition 3 ruled out; Mechanism A needs γ ≳ 6.3 (`CCEF_proton_decay_results.md`) | Proton decay seen with μ⁺π⁰ ≪ e⁺π⁰ (GUT pattern) | **Hyper-K** |
| **String-net rules (2026-10-11):** the baryon-violating junctions are local (no topological protection; the earlier window is retracted). The proton is protected only by a ℤ₃ **lepton-triality** grading: anomaly-free **only for N_gen = 3**, forbids Majorana masses. **Fork:** Branch M (Λ* ≥ 4×10¹⁵ GeV, proton decay with μ ≈ e possible, Majorana allowed) vs **Branch L₃ (proton absolutely stable, Dirac ν, no 0νββ, low Λ* allowed)** (`CCEF_stringnet_rules.md`) | Branch L₃ is killed by any proton decay or any 0νββ | Hyper-K, LEGEND-1000, nEXO |
| **Dirac neutrino masses, Branch L₃ (pre-registered 2026-10-11, CONJECT mechanism):** ν^c is the only fermion string with no gauge flux, so it spreads over the ~(M/Λ*)³ grains of each cell. That dilutes the Yukawa to y ≈ (Λ*/M)^{3/2} = 3×10⁻¹³ at **Λ* ≈ 8×10¹⁰ GeV** (consistent with Mechanism A at γ = 3; Z3 strings harmless). Flavour-blind grains imply Dirac anarchy: **normal ordering (175 : 1), Σm_ν = 72 meV (68%: 64–84), m₁ ≈ 9 meV, m_β ≈ 12 meV, large mixing; ΔN_eff = 0.14 (or 0.06 with SUSY) if the grains thermalised ν^c, else 0** (`CCEF_dirac_neutrino.md`). **Fit in the recruitment cosmology (pre-registered): MILD TENSION.** Δχ²(72 meV) = 3.05, of which 2.33 is already present at the 59 meV floor (generic DESI tension). Non-phantom recruitment cannot loosen the bound (`CCEF_numass_fit_results.md`) | inverted ordering; any 0νββ; Σm_ν < 61 meV (95%) in CCEF's own cosmology; ΔN_eff ≳ 0.3 | JUNO, DESI DR3/Euclid, Simons Obs./CMB-S4, LEGEND/nEXO |
| **Lensing (2026-10-11, S8 pre-registered):** the lensing law is GR (grain corrections ~10⁻¹¹⁰, achromatic). Recruitment lowers σ8 by up to 3% but raises Ω_m, so **S8 = 0.800 for both CCEF and ΛCDM** (neither helps nor hurts against KiDS, DES, HSC or ACT). **The discriminator is fσ8(z = 0.5), 1.5–4% below ΛCDM.** Grain-entanglement "apparent dark matter" (Verlinde-type, a₀ = cH₀/6 ≈ 1.1×10⁻¹⁰, matching MOND) **cannot replace dark matter** (z_eq, CMB, Bullet Cluster). A real dark-matter component is still required: **open hole** (`CCEF_lensing.md`) | fσ8 consistent with ΛCDM at the 1% level for y₀ ≳ 0.03 | DESI full-shape RSD, Euclid |
| **Dark matter (pre-registered 2026-10-11, CONJECT origin):** the **QCD axion at the crossover, f_a ≈ Λ*** (strong-CP fix; post-inflation scenario forced by no inflation). **m_a ≈ 74 μeV (14–400), about 18 GHz**, g_aγγ(KSVZ) ≈ 3×10⁻¹⁴ GeV⁻¹, N_DW = 1, miniclusters. It selects the neutrino dilution power p = 3/2. Excluded: ν/ν^c, ℤ₃ relics, monopoles, apparent DM. Secondary: Planck-mass black-hole remnants. **Monopoles (worked out, `CCEF_monopole_problem.md`):** no Kibble monopoles (no GUT, π₂ = 0). Thermal monopoles (m ≈ 35 Λ* ≈ 3×10¹² GeV) are safe if T_max ≲ 0.95 Λ*; no emergence defects if the gauge fields switch on as a crossover (adiabaticity 3×10⁸) (`CCEF_dark_matter.md`) | nothing in 3–100 GHz haloscopes; any WIMP signal | MADMAX, ALPHA, ORGAN, BREAD |
| ~~Grain baryon (2026-10-11, CONJECT):~~ *(window retracted, see the row above)* a proton is about 10⁶⁰ grains (three colour-string ends at a junction). Only charge and colour triality are exactly conserved; B is exponentially protected if its violation needs a string-net topology change. **Window Λ* ≈ 3–6×10¹⁴ GeV, g² ≈ 15–20, S ≈ 4–5** reconciles Lorentz protection (γ ≈ 5), neutrino masses and proton stability (`CCEF_grain_baryon.md`) | No proton decay down to about 10³⁶ yr would close the window | Hyper-K |
| **Spacetime jitter (pre-registered 2026-10-11):** grainy paths give KPZ noise (χ ≈ 0.24, unobservable; survives the quasar-imaging foam limits); grainy gravity gives Verlinde–Zurek ⟨δL²⟩ = c_B ℓ_P L (about 4×10⁻¹⁸ m on 1 m), **~3σ tension with the Holometer at α ≈ 1 (model-dependent)** (`CCEF_length_noise_results.md`) | GQuEST excludes the VZ signal at natural amplitude with the correct spectral model; or **detects it** (support) | **GQuEST (tabletop, now)**, Holometer re-analysis |
| GWs: speed = c (\|Δc\|/c ~ 10⁻⁷⁰), m_g = 0, no dispersion, no birefringence, no echoes, d_L(GW) = d_L(EM). Checked against GW170817 and GWTC-3/4: consistent (`CCEF_GW_check.md`) | GW dispersion, graviton mass, birefringence (e.g. GW190521/GW191109 hints confirmed), echoes | LIGO/Virgo/KAGRA, LISA, ET |
| S2/Sgr A*: exactly GR (deviations ≤ 10⁻¹⁰; grainy core 10⁻¹⁰⁰; Hawking 10⁻⁸⁷). Consistent (`CCEF_S2_check.md`) | any non-GR S2 precession | GRAVITY+ |
| Superpartners between about 1 TeV and 6×10⁷ GeV (if Mechanism B is needed) | — | future colliders |
| Fork A only: parity-odd CMB TB/EB tied to the sign of η_B | — | CMB polarisation |
| Running α_s small if a critical origin is used | — | CMB plus large-scale structure |

---

## 8. Open problems (ranked)
1. **Robustness of the E2 real-sky lean:** other Planck maps and a masked likelihood.
2. **Lorentz protection in a concrete Ĥ:** γ ≳ 3 or an emergent SUSY window.
3. **A concrete Ĥ with a stable, local 3D geometric phase** that is not mean-field at geometrogenesis. **Version 1 built** (`CCEF_grain_Hamiltonian.md`):
   - grains are qubit-relations, joined at 4-grain junctions;
   - Ĥ = geometry (rings − crowding − over-connection) + rewiring + spin-ice Gauss law + exchange;
   - Monte Carlo: rings alone crumple space; with no-crowding (W ≥ 4), random relations self-assemble to locally exact 3-D diamond (glassy);
   - light = quantum-spin-ice photon (crossover switch-on); Λ*/M from J_±/J_zz ≈ 7×10⁻⁴.

   Open: α, SU(2)×SU(3), light fermions, graviton.
   **Electrons added** (`CCEF_grain_electrons.md`):
   - dressed grain flips make string ends fermions (exact, θ = π at all junctions);
   - spinless versions always give nodal lines (512/512 flux patterns), so spin-½ is required;
   - with 2 grains per relation + spin–orbit there are **exactly 3 massless Dirac fermions at the 3 X points**, isotropic at λ = t/4;
   - masses = Klein-four combinations of the junction-bond distortions;
   - three-generation reading [CONJECT].

   Open: chirality (mirror gapping, needs ν^c), Higgs-linked masses, a common speed with light.
4. **Primordial spectrum without inflation:** both amplitude and tilt (now strongly constrained by the running relation).
5. **The photon fork:** realise Fork B's string-net photon, or resolve Fork A's phase contradiction.
6. **Recalibrate the hadronic EFT** to the vector-meson spectrum, and recompute v3.9's HLM numbers and the 17.5 lock with the corrected mass.
7. **The recruitment and halting dynamics**, giving the late-time w(z).
8. **Count N_eff explicitly**, including the signs of vector and spinor contributions.
9. **Leptons:** string-net (L1) or M-sector without its inflaton (L2). In Branch L₃ the tiny Dirac Yukawa has a candidate explanation (grain dilution of ν^c, `CCEF_dirac_neutrino.md`). Still open: derive the spreading assumption and the power 3/2 from a concrete Ĥ, and fit Σm_ν inside the recruitment cosmology. Note that v3.9's m_ν = Λ²/√(MΛ) is not SU(2)-invariant (it has no Higgs vev) and is forbidden in L₃.

---

## 9. Errata applied to v3.9 material
- (1/4π²)∫a∧da = **B** (was B²). Downstream: "dH = (2B+dB)dB" becomes dH = dB; the lepton obstruction is unchanged; in the seed-field estimate the additive option is the consistent one.
- Ordered-phase vector mass = **√(A₁/A₂) = 214 MeV** (was √(A₁/2A₂) = 152 MeV). HLM cubic E 0.100 → 0.284; χ_c/T_c 0.113 → 0.32; recompute dependent results.
- "n_s = 1 owned" becomes **n_s = 1 at leading order; tilt open; excluded if exact.**
- The composite-graviton [SOLID] label is withdrawn. Gravity is re-founded at the grain scale (§2.1).

## 10. File map
| File | Contents |
|---|---|
| `CCEF_v3.9_review.md` | review of v3.9 |
| `ccef_v5_checks.py`, `ccef_v5_checks_output.txt` | math checks |
| `CCEF_V4/` | V4.1 paper (grains, Lorentz protection) and changelog |
| `CCEF_derived_additions.md` | finite volume, cycles, neutrino and black-hole additions |
| `CCEF_beta_torus_results.md`, `ccef_torus_cmb.py`, `ccef_topology_cmb.py`, `ccef_twist_fit.py` | β derivation and CMB topology tests (simulated and real sky) |
| `CCEF_ns_eta_novelty_check.md`, `ns_eta_test.py`, `ns_drift_test.py` | tilt analysis and running constraint |
