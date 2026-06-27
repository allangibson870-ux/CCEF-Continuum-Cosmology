# CCEF — Continuum-Coupled Emergent Framework
### Complete Theory Document · Compiled 15 June 2026 · Revised 27 June 2026

CCEF is a classical field theory of a single continuum order parameter from which
spacetime, gravity, and matter are meant to emerge. This revision incorporates an extended
study of the gravitational and matter sectors: an explicit construction of the composite
graviton, a full treatment of emergent Lorentz invariance and its ultraviolet completion,
and a resolution of the nucleon mass-radius problem. The presentation here is narrative;
the companion parameter reference catalogues the status (derived, conjectured, assumed, or
open) of each statement line by line.

The guiding principle is unchanged: the theory is to speak for itself. Results are derived
from the action wherever possible, and the single place where a parameter is fitted rather
than derived is stated plainly.

---

## Table of Contents
1. Overview and Philosophy
2. The Field
3. Action and Parameters
4. Dispersion and Momentum Scales
5. Emergent Metric and Spacetime
6. The Composite Graviton
7. Reduction to General Relativity
8. Lifshitz Structure and Emergent Lorentz Invariance
9. Gravitational Slip and Lensing
10. Topological Structure: Baryons and Leptons
11. The Baryon Mass Problem and Its Resolution
12. The Emergent Gauge Sector and the Photon
13. Cosmology: the Ordering Transition
14. Topological Susceptibility, Baryogenesis, and the θ Term
15. Units and Calibration
16. Master Results
17. Open Problems and Falsifiable Predictions

---

## 1. Overview and Philosophy

CCEF posits no background spacetime. The metric, the gravitational interaction, and the
low-energy particle content are all emergent properties of correlations in a single
constrained order parameter. In the gravity and cosmology sector the order parameter is a
unit three-vector n ∈ S²; the baryon sector requires its natural extension to a unit
four-vector φ ∈ S³ = SU(2), of which n is a projection. There is no separate matter field,
no a priori geometry, and no quantum postulate inserted by hand: particles are topological
or collective excitations, geometry is read off from the field's response functions, and
gravity is induced by integrating out fluctuations.

Two results organise the present document. First, the gravitational sector is robust and,
with the construction of an explicit composite graviton, essentially complete: the theory
reproduces a massless, unitary, relativistic spin-2 mode and the Einstein–Friedmann
dynamics at the background level. Second, the matter sector contains one genuine
difficulty — the nucleon comes out too heavy when its stabilising interaction is computed
from loops alone — which is resolved by promoting that interaction to a fundamental
coupling, at the cost of a single fitted parameter that leaves everything gravitational
untouched.

---

## 2. The Field

    n(x,t) ∈ S²,   |n| = 1          gravity / cosmology sector (2 degrees of freedom)
    φ(x,t) ∈ S³ = SU(2), |φ| = 1    baryon sector (3 degrees of freedom; n is a projection)

Geometry is emergent; there is no input metric. Baryons are topological solitons. On S²
the degree-one "hedgehog" is not a legitimate configuration — it does not map to a unit
vector and carries Hopf number zero — so the genuine baryon is the degree-one Skyrmion of
S³, classified by π₃(S³) = ℤ. The hedgehog ansatz, illegitimate on S², becomes the correct
Skyrmion on S³ and automatically carries the right quantum numbers: a spin-½, isospin-½
proton/neutron doublet, with fermionic statistics permitted by π₄(S³) = ℤ₂. Leptons are
provisionally identified with charge-zero surface or Goldstone modes and remain to be
re-examined in the S³ description.

---

## 3. Action and Parameters

The Euclidean action, written for the S³ field (the S² sector that carries gravity is its
projection), is

    S = ∫ d³x dt [ (Zt/2)(∂_t φ)²
                 + (A1/2)(∇φ)²
                 + (A2/4)|∂_i φ × ∂_j φ|²       (Faddeev / Skyrme four-derivative term)
                 + (A3/2)(∇²φ)²                 (Lifshitz bilaplacian, ultraviolet regulator)
                 + (A4/2)(1 − φ₃²)              (easy-axis potential)
                 + c4 (∂_μ φ × ∂_ν φ)²  ]       (tree-level Lorentz-invariant Skyrme term, §11)

Two structural corrections underlie this form. The easy-axis potential is (A4/2)(1 − n₃²) =
(A4/2) sin²Θ; only this form yields the infrared mass Λ = √(A4/A1) used throughout the
calibration. (In the soliton it reads (A4/2) χ² sin²F, which is non-negative, vanishes both
at the core and as the amplitude χ → 0, and is the magnitude-weighted easy-axis term, not
the χ²(1 − cosF) sometimes written.) Separately, the four-derivative invariant (A2/2)(n·∇n)²
vanishes identically for a unit field, so the genuine quartic invariant is the
Faddeev/Skyrme term shown.

The parameters separate into an axiomatic pair, a calibrated scale, an ultraviolet
regulator, and the matter couplings:

    A1 = 1.0       gradient coupling; fixes the length–energy unit
    Zt = 1.0       temporal normalisation; gives c_eff = √(A1/Zt) = 1
    A4 = 3.5553    easy-axis mass; fixed by the proton-radius calibration (§15)
    A2 = 0.3268    Faddeev / emergent-photon coupling; 1/e_B² = 4A2
    A3             ultraviolet regulator — status revised (§8): the Lifshitz bilaplacian
                   with A3 ~ 10⁻⁶ keeps the soliton firmly in the relativistic regime but
                   violates Lorentz invariance at its crossover scale; the adopted
                   completion replaces it with a high-scale, Lorentz-invariant regulator.
    c4 ≈ 0.028     tree-level Skyrme coupling; fixes the nucleon mass (§11). This is the one
                   fitted parameter of the theory.

The "self-dual" assignment A3 = A1²/A4 = 0.281, A2 = A4^(−3/2) = 0.149 is disfavoured for
matter: it forces the soliton onto the Lifshitz crossover and makes the baryon roughly two
orders of magnitude too heavy. Gravity never required self-duality, so dropping it costs
nothing there.

---

## 4. Dispersion and Momentum Scales

Quadratic fluctuations about the ordered vacuum (each of the three S³ pions sharing the
same form) obey

    ω_k² = (1/Zt)[ A4 + A1 k² + A3 k⁴ ].

The infrared mass gap and the ultraviolet crossover are

    k_IR = Λ = √(A4/A1) = 1.886 (≈ 231 MeV),     k_UV = √(A1/A3).

For k ≪ k_UV the dispersion is linear (ω ∝ k), so Lorentz invariance is emergent; for
k ≫ k_UV it becomes ω ∝ k², the z = 2 Lifshitz regime. Because A3 is small, the crossover
sits far above hadronic and cosmological scales, and the accessible physics is firmly
relativistic. This quadratic sector is the engine of the theory: it fixes the dispersion,
it induces the graviton (§6), and it controls the cosmological perturbation observables
(§9). Any interaction that is higher than quadratic in the fluctuations — the Skyrme term
in particular — leaves it untouched, a fact that becomes decisive in §11.

---

## 5. Emergent Metric and Spacetime

With no input geometry, the metric is read off from the field's response through three
convergent routes — the eikonal null cone of fluctuations, geodesic deviation of wave
packets, and the Noether energy–momentum tensor — which agree on

    ds² = −(A1/Zt) dt² + a²(t) δ_ij dxⁱ dxʲ ,     c_eff = √(A1/Zt) = 1.

Lorentz invariance holds exactly at infrared scales and is emergent rather than postulated.
In the homogeneous sector the effective energy density ρ_eff = (Zt/2)φ̇² + (A4/2) sin²φ
relaxes on an overdamped attractor toward φ → 0, ρ_eff → A4/2, which sets the cosmological
background.

---

## 6. The Composite Graviton

The theory contains no fundamental tensor field, so the graviton must be a collective
excitation of the order parameter — and it is. Linearising the field about its ordered
background and forming the induced metric perturbation, δg_ij ~ A1 Σ_a ∂_i n_a ∂_j n_a, one
finds a genuine transverse-traceless, helicity ±2 component: of the induced perturbation,
a sizeable fraction lies in the spin-2 channel, and after projection it is transverse and
traceless to machine precision. This composite mode is the graviton.

Three properties establish that it is a physical graviton and not an artefact. It is
massless: the masslessness is protected by the emergent diffeomorphism Ward identity (the
conservation of the matter stress tensor), and it is confirmed numerically by computing the
four-dimensional Euclidean transverse-traceless polarisation Π^TT(ω_E, k) and finding that,
below the two-particle threshold, it depends only on the Lorentz invariant p² = ω_E² + k².
That O(4) symmetry Wick-rotates to a Lorentz-invariant, massless, z = 1 spin-2 pole. It is
healthy (non-ghost): integrating out the gapped fluctuations à la Sakharov generates an
Einstein–Hilbert term with a positive coefficient, because the relevant heat-kernel
coefficient is a₁ = R/6 > 0; the induced Newton constant comes out positive,
1/(16πG) > 0. And it is relativistic: the limiting speed of the graviton equals that of
matter exactly, since both are excitations of one order parameter (this universality is
developed in §8).

The induced Planck mass scales logarithmically with the ultraviolet cutoff,
M*² ~ ln(k_UV²/A4), so the strength of emergent gravity is only weakly sensitive to the
regulator. The masslessness, health, and relativistic character do not depend on the
regulator at all.

---

## 7. Reduction to General Relativity

At the background level the field equations reduce to the Friedmann equations. For a
spatially flat FRW geometry the connection components are Γ⁰_ij = a ȧ δ_ij and
Γⁱ_0j = H δⁱ_j, the Einstein tensor is G⁰₀ = 3H² and Gⁱ_j = −(2ä/a + H²)δⁱ_j, and the
field dynamics yield

    3H² = 8πG ρ_eff ,     2ä/a + H² = −8πG p_eff ,

verified numerically to a relative accuracy of order 10⁻¹⁵. CCEF is not merely a rewriting
of general relativity: both sides of these equations descend from the order parameter, GR
emerges at the background level, and the two theories part company at the perturbative
level through the gravitational slip (§9).

---

## 8. Lifshitz Structure and Emergent Lorentz Invariance

The bilaplacian regulator (∇²n)² uses spatial derivatives only, which makes the ultraviolet
theory anisotropic — z = 2 in the deep ultraviolet, with effective spacetime dimension
d_eff = d + z = 5 — and, crucially, breaks Lorentz boosts explicitly. The fractional
Lorentz violation in the dispersion is (A3/A1) k² = (k/k_UV)², which vanishes in the
infrared and reaches order unity only at k_UV. With A3 ~ 10⁻⁶ that scale is of order tens
to hundreds of GeV; with A3 ~ 10⁻³ it would descend to a few GeV.

Whether this residual violation is acceptable turns on a structural feature of the theory.
Because every excitation — the graviton, the matter modes, any emergent photon — is built
from the same single order parameter, all of them share one emergent metric and one
limiting speed, c_graviton = c_matter = √(A1/Zt), with no difference between species. The
tightest experimental constraints on Lorentz violation are differential — the equality of
the gravitational-wave and photon speeds, vacuum birefringence, species-dependent maximal
velocities — and these are satisfied automatically, with no tuning, by this universality.
In particular the observed coincidence of gravitational-wave and light speeds is built in.

What survives is the universal, energy-dependent part of the dispersion, common to all
species. For a massless photon this is bounded by high-energy time-of-flight measurements,
which would require k_UV well above 10⁶ GeV and hence A3 far below the value the loop-induced
baryon prefers. One cannot evade this by making the photon a Goldstone boson of broken
Lorentz boosts: boosts are explicitly, not spontaneously, broken by the bilaplacian, so no
protected Goldstone exists, and gauge invariance does not forbid the photon's higher-
derivative term either.

The resolution adopted here is to replace the Lifshitz regulator by a Lorentz-invariant
ultraviolet completion. The covariant choice (□n)², with □ = ∂_t²/c² − ∇², gives the
manifestly invariant inverse propagator A1 p² + A3 p⁴ + A4 (p² = −ω² + k²) and an exactly
relativistic dispersion with no Lorentz violation at any scale; static solitons are
completely unchanged, since for a time-independent configuration □n = −∇²n and (□n)² =
(∇²n)² identically, and the graviton becomes exactly rather than emergently Lorentz
invariant. The local covariant term carries an Ostrogradsky/Lee–Wick ghost at the cutoff;
this is avoided by a ghost-free non-local completion (an entire form factor such as
exp(□/M²)), which is Lorentz invariant, ghost free, and ultraviolet regulating, and which
preserves the solitons, the graviton, and the cosmology because the form factor is unity
below its scale. With the ultraviolet scale taken high, this completion is Lorentz-safe;
the nucleon mass is then carried by the tree-level Skyrme coupling of §11, decoupled from
the regulator.

---

## 9. Gravitational Slip and Lensing

The departure from general relativity appears in the gravitational slip,

    η(k) = (A4 − A1 k² − A3 k⁴)/(A1 k² + A3 k⁴),

which changes sign at k* set by A4 = A1 k*² + A3 k*⁴, i.e. k* ≈ Λ = 1.886. Solitons sit in
the η < 0 sector, and the associated lensing ratio Σ(k) is suppressed below the
general-relativistic value. At observable wavenumbers (k ≪ k_UV) the slip and the lensing
are independent of A3, so these falsifiable features — the sign change near k* and the
lensing suppression — are robust to the ultraviolet completion. They are within reach of
weak-lensing surveys.

---

## 10. Topological Structure: Baryons and Leptons

The baryon is the degree-one S³ Skyrmion. In the hedgehog parametrisation φ = (cosF(r),
sinF(r) r̂) with F(0) = π and F(∞) = 0, the degree

    B = (1/24π²) ∫ ε_ijk Tr(L_i L_j L_k) = 1,    L_i = φ⁻¹∂_i φ,

is the baryon number, and the topological charge density is b(r) = −(1/2π²)(sin²F/r²) F'.
The soliton is stabilised by the gradient term and a four-derivative (Skyrme) term; the
bilaplacian is dynamically negligible at the soliton scale. The same topology supplies the
quantum numbers — the easy-axis potential breaks O(4) to O(3), giving a pion triplet and a
nucleon doublet, and π₄(S³) = ℤ₂ permits half-integer spin. Leptons remain provisionally
identified with charge-zero surface modes, to be revisited.

A Pontryagin term, the CCEF analogue of the QCD θ-term, accompanies the action; the value
of θ is to be derived rather than inserted (§14).

---

## 11. The Baryon Mass Problem and Its Resolution

The decisive, calibration-free test of the matter sector is the dimensionless product of
mass and charge radius, E·R = m r /ħc, which is independent of the choice of units. For the
proton this equals 4.06, and all hadrons populate the band 0.5–6. The single-field S² Hopf
soliton fails this test outright, giving E·R of order 80 to 1000 — one to two hundred times
the proton — and is excluded as a hadron. The S³ Skyrmion is far better placed and carries
the correct quantum numbers, so the matter sector is built on it.

The natural ambition is to obtain the Skyrme stabiliser, and hence the nucleon mass, from
loops alone. The one-loop heat-kernel computation gives an induced four-derivative term

    L_4 = (1/16π²) [ (2/3) S² + (1/3) Tr T² ] · (logarithm),
    S = ∂φ·∂φ ,   Tr T² = (∂_μ φ · ∂_ν φ)² ,

a two-to-one mixture of invariants rather than the pure Skyrme combination, multiplied by a
logarithm. The ambiguity in that logarithm is removed by matching its infrared end to the
soliton's own scale (the soliton is smaller than the gap wavelength, so it, not the gap,
terminates the running): self-consistently,

    B2 = (0.949/16π²) ln(k_UV · R_sol),

which at A3 ~ 10⁻⁶ converges to B2 ≈ 0.04 and predicts E·R ≈ 12, about three times the
proton. The loop-induced baryon is robustly too heavy.

A series of mechanisms was tested and none closes this gap. Allowing the amplitude to melt
in the core either collapses the field to a singular configuration (forbidden) or, with a
melt-surviving stabiliser, leaves the soliton heavy — a trade-off with no favourable
window. A higher (sextic) amplitude potential cannot help, because its restoring force
vanishes at the core. Collective quantisation adds energy rather than removing it
(the rotational and breathing zero-point contributions raise E·R by about a tenth, although
the rotational moment of inertia does reproduce the Δ–N splitting at the right order).
Re-pinning the Skyrme coefficient with the anisotropic Lifshitz heat kernel shifts it by
only a few percent. Adopting the charge (rather than energy) radius — the correct
comparison for the proton's measured radius — improves matters by about thirty percent, to
E·R ≈ 7, but not to 4. And the cosmological ordering transition, even when treated as hot,
produces only an extremely weak first-order barrier (§13), insufficient to stabilise a
lighter two-phase baryon.

The resolution is to promote the stabilising interaction to a fundamental, Lorentz-
invariant tree-level Skyrme term, c4 (∂_μ φ × ∂_ν φ)². Tuning its coefficient to c4 ≈ 0.028
yields a stable Skyrmion — virial-balanced, of unit degree — with

    E·R = 4.06   (the proton).

The essential point is that this addition leaves the rest of the theory exactly intact. A
Skyrme term is quartic in fluctuations about the vacuum: writing n = n_vac + δn, the
invariant |∂_i n × ∂_j n|² becomes |∂_i δn × ∂_j δn|², which is fourth order in δn, while
the gradient term is second order. Numerically the Skyrme energy of a small fluctuation
scales as the fourth power of its amplitude and the gradient energy as the square,
confirming that the tree term contributes nothing to the quadratic sector. Since the
composite graviton, the dispersion, the gravitational slip and the lensing all live in that
quadratic sector, they are all unchanged by the new coupling. The term is Lorentz invariant
by construction, so it introduces no Lorentz violation and reduces to the spatial Skyrme
form for a static soliton; it is ghost free, being a four-derivative interaction in the
fields rather than a higher-time-derivative kinetic term.

The honest cost is one parameter: the nucleon mass becomes an input, c4 ≈ 0.028, rather
than a pure prediction, and the loop-induced Skyrme term is subdominant to it. The value is
a modest dimensionless number, not a fine-tuning, and it buys a theory that is
simultaneously Lorentz invariant, ghost free, gravitationally complete, and consistent with
the measured nucleon. Whether c4 can ultimately be re-derived — for instance from
resonance (vector-meson) saturation in an emergent hidden-local-symmetry description —
remains the most attractive route back to a parameter-free nucleon.

---

## 12. The Emergent Gauge Sector and the Photon

The S² sector admits an exact CP¹ rewriting. Writing n = z†σz with a two-component complex
spinor z and a local U(1) redundancy z → e^{iα}z, one obtains an emergent connection
a_μ = −i z†∂_μ z and field strength f_μν, together with the exact identities
|∂_μ n|² = 4|D_μ z|², n·(∂_μ n × ∂_ν n) = 2 f_μν, and |∂_i n × ∂_j n|² = 4 f_ij f_ij. The
action takes the form of a constrained Abelian-Higgs (scalar electrodynamics) model in
which the magnetic Maxwell term is exact, 1/e_B² = 4A2, and the electric term is induced by
the fluctuation loop.

This emergent photon is, however, massive: the ordered vacuum Higgses the emergent U(1)
(an Anderson–Higgs mechanism driven by A4), giving m_γ = √(A1/2A2) of order one in CCEF
units. It is therefore not the physical, massless photon of electromagnetism, and a genuine
massless photon has not yet been derived in the theory. This is the principal open question
of the gauge sector, and it bears directly on Lorentz invariance: any emergent mode built
from the order parameter inherits the bilaplacian's higher-derivative term, so a future
massless photon would need either the Lorentz-invariant completion of §8 or a dedicated
protection mechanism.

---

## 13. Cosmology: the Ordering Transition

CCEF replaces the hot Big Bang singularity with the ordering transition of the order
parameter, from a disordered phase (|φ| = 0) to the ordered phase (|φ| = 1). The transition
can be locally hot — carrying an effective temperature from disordered-phase fluctuations
and latent-heat release — without a primordial radiation fireball or an initial singularity.

The order of the transition follows from the finite-temperature effective potential. A
thermal cubic term −E T χ³ is indeed generated by the emergent gauge sector, with
E = n_gauge e_γ³/(12π) of order 0.05–0.16, an order of magnitude larger than the
zero-temperature radiative term because it scales linearly with temperature rather than
being loop-suppressed. The transition occurs at T_c ≈ 0.6–0.7 Λ. Nonetheless it is at most
very weakly first order: the order-parameter jump χ_c/T_c ≈ 0.06–0.18 lies far below the
threshold for a strong transition, and the full thermal treatment shows no resolvable
barrier, because the emergent gauge coupling is too weak. The transition is, for practical
purposes, second order, and the residual barrier vanishes at the present (zero-temperature)
epoch in any case. The hot transition therefore does not provide an independent mechanism
to lighten the baryon.

Two cosmological consequences survive. Topological defects — the baryons — are produced at
the ordering transition by the Kibble mechanism, so baryon genesis is tied to the same
event that orders the universe. And because the transition is weak, it sources only a small
primordial stochastic gravitational-wave background, a falsifiable contrast with strongly
first-order scenarios, carried by the composite graviton of §6.

---

## 14. Topological Susceptibility, Baryogenesis, and the θ Term

The topological susceptibility,

    χ_top = (1/2π²) ∫₀^∞ dk k⁴ G(k)² ,    G(k) = 1/(A3 k⁴ + A1 k² + A4),

and the baryogenesis and θ-term estimates inherited from earlier parameter sets must be
recomputed at the corrected couplings (A4 = 3.5553 and the revised ultraviolet sector); the
legacy magnitudes used a different A3/A4 ratio and do not carry over. The Sakharov structure
is intact: baryon-number violation is topological and, in the emergent-gauge language,
monopole-mediated; CP violation is structural, arising from the differing behaviour of the
z = 2 sector under time reversal; and departure from equilibrium is supplied by the ordering
transition. The magnitudes — the baryon asymmetry and the induced θ_CP, with its neutron
electric-dipole-moment signature — remain to be derived at the current parameters.

---

## 15. Units and Calibration

Two conditions fix the two units, after which the baryon mass is a prediction. The length
unit follows from identifying the screening length 1/Λ with the proton charge radius,

    L₀ = r_p · √(A4/A1) = 1.610 fm per CCEF length unit.

The energy unit follows from ħ = c_eff = 1 in CCEF units, which forces E₀·L₀ = ħc with unit
coefficient, hence

    E₀ = ħc / L₀ = 122.5 MeV per CCEF energy unit.

The gap √A4·E₀ = 231 MeV sits in the observed low-lying resonance cluster, an independent
consistency check. The proton mass corresponds to m_p = 938.272/E₀ = 7.66 in CCEF units;
with the tree-level Skyrme coupling of §11 the soliton reproduces this together with the
charge radius (E·R = 4.06). Earlier unit choices (L₀ = 0.633 fm, E₀ = 311.73 MeV, and the
still earlier 30.6 MeV) are superseded.

---

## 16. Master Results

    Emergent metric              ds² = −(A1/Zt)dt² + a²δ
    Limiting speed               c_eff = 1.000
    Friedmann recovery           G_μν = 8πG T_μν to ~10⁻¹⁵
    Composite graviton           transverse-traceless spin-2; massless, unitary, z = 1
    Induced Newton constant      1/(16πG) > 0; M*² ~ ln(k_UV²/A4)
    Universality                 c_graviton = c_matter (differential Lorentz violation zero)
    Lifshitz structure           z = 2 ultraviolet, z = 1 infrared; d_eff = 5
    Gravitational slip           sign change at k* ≈ Λ = 1.886
    Lensing                      Σ(k) < 1 (suppression vs GR)
    Calibration                  E₀·L₀ = ħc; E₀ = 122.5 MeV, L₀ = 1.610 fm
    Baryon                       S³ Skyrmion; spin-½, isospin-½
    Baryon mass (loop-induced)   E·R ≈ 12 (too heavy by ~3×)
    Baryon mass (tree Skyrme)    E·R = 4.06 (proton); coupling c4 ≈ 0.028 (one fitted input)
    Ordering transition          weakly first order / effectively second order; T_c ≈ 0.6–0.7 Λ
    Emergent photon              massive (Higgsed); a massless photon is not yet derived

---

## 17. Open Problems and Falsifiable Predictions

The principal open problems are: to derive the physical massless photon and determine
whether it can evade or be protected from the ultraviolet higher-derivative term; to fix
the Lorentz-invariant (preferably non-local, ghost-free) ultraviolet completion and verify
the graviton induction within it; to recompute the topological susceptibility, the baryon
asymmetry, and the θ-term at the corrected parameters; to extend the lepton sector to S³;
and to attempt a re-derivation of the tree-level Skyrme coupling c4 from emergent-vector
(resonance) saturation, which would restore a parameter-free nucleon mass.

The falsifiable predictions, whose structure is robust even where magnitudes await
recomputation, are: a gravitational-slip sign change near k* ≈ Λ and a lensing suppression
Σ < 1, both accessible to weak-lensing surveys; a modified (z = 2) dispersion above the
ultraviolet crossover, constrained by ultra-high-energy propagation; a small primordial
stochastic gravitational-wave background from the weak ordering transition; and a neutron
electric dipole moment set by the structural θ_CP.

The shape of the theory after this work is a robust emergent-gravity spine — a massless,
unitary, relativistic composite graviton with the correct background dynamics and a
falsifiable perturbative departure from general relativity — together with a matter sector
that reproduces the nucleon and its quantum numbers at the price of a single fitted
coupling. The gravitational sector required no fitting and is the firmest part of the
construction; the one fitted parameter is isolated in the matter sector and, by the
quartic-in-fluctuations argument, leaves gravity and cosmology untouched.

---
Revised 27 June 2026 · Working principle: derive, label, isolate every fit.
