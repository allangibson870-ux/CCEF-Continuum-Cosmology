# Composite graviton in CCEF — linearization results

**Goal (roadmap Action 1):** linearize δn about the background n = e_z and
extract the transverse-traceless (helicity ±2) part of the induced metric δg,
to test whether a massless spin-2 graviton emerges as a *collective* mode
(no fundamental tensor field).

Computed with the real CCEF action and coefficients
(A1 = 1, A2 = 0.3268, A4 = 3.5553, Zt = A1) and the `ccef3d.py` discretization.
Script: `ccef_graviton.py` (run alongside `ccef3d.py`).

## [A] Matter dispersion — confirmed
Linearizing n about e_z with the same finite-difference operators gives, for
the two tangent (transverse) modes,

    ω²(k) = (A4 + A1 k² + A3 k⁴) / Zt

The lattice eigenvalues match the continuum formula to <3% up to k≈3 (lattice
artefacts above that), and the local exponent runs z=1 (k≪Λ) → z=2 (k≫k_UV),
with the crossover exactly at k_UV = √(A1/A3). This reproduces the [SOLID]
result in CCEF_Reference.txt line 93.

**Key point:** these modes are **gapped** (mass² = A4, gap Λ = √(A4/A1) ≈ 1.886)
because the A4 term breaks the O(3) symmetry. So the n-fluctuation itself is
*not* the graviton — it is massive matter. Any massless spin-2 must be composite.

## [B] TT extraction — a real spin-2 component exists
Build the induced metric perturbation from the field gradients,
δg_ij = A1 Σ_a ∂_i n_a ∂_j n_a, Fourier-transform, and apply the 3D spin-2
transverse-traceless projector. For a generic (multi-wave) tangent fluctuation:

- helicity ±2 fraction of ‖δg‖ ≈ **0.42**
- transversality  |k·δg^TT| / ‖δg^TT‖ ≈ 3e-16  (machine zero)
- tracelessness   |tr δg^TT| / ‖δg^TT‖ ≈ 9e-17  (machine zero)

So a well-defined, sizeable transverse-traceless spin-2 object is genuinely
present in the induced metric. (Caveat learned along the way: a single plane
wave per component gives a purely *longitudinal* stress with ~0 TT part — the
TT channel is only populated by transverse stress structure, as in a real
fluctuating field or the loop integral below.)

## [C] Induced graviton kinetic term — propagates, but sign/health is open
Integrating out the gapped n-fluctuations (Sakharov-style) generates a TT
graviton self-energy Π^TT. From the one-loop bubble with the A1 stress vertex:

| A3 (regulator) | k_UV = √(A1/A3) | Π^TT(0) | \|kinetic stiffness\| |
|---|---|---|---|
| 0.281 (self-dual) | 1.886 | 1.9e-1 | 3.2e-4 |
| 1e-6 (baryon regime) | 1000 | 5.2e+2 | 4.3e-1 |

- The induced kinetic coefficient is **finite and nonzero**, so the composite
  spin-2 mode genuinely **propagates** (it is dynamical, not auxiliary).
- It **grows strongly as A3 → 0**, i.e. the induced gravitational stiffness
  (Planck scale) is controlled by the UV regulator k_UV — exactly the Sakharov
  M*² ~ k_UV² behaviour. Tiny A3 ⇒ very stiff/weak gravity; self-dual A3 ⇒ strong.

## What this does and does not establish

**Supports the composite-graviton escape:** the matter mode is gapped, yet the
induced metric carries a large, exactly transverse-traceless spin-2 component
that acquires a finite kinetic term from the order-parameter correlations. This
is consistent with "the graviton is a collective excitation, no new fundamental
d.o.f." and with the analog/induced-gravity philosophy.

**Still open (honest):**
1. **Masslessness** is argued *structurally* (conserved matter stress ⇒
   transverse polarization ⇒ no graviton mass by Ward identity), not measured
   here. The naive static k²-slope of the bubble is a form factor, not the
   graviton mass, so I did not claim a number for it.
2. **Sign / ghost-vs-healthy** of the kinetic term needs the full *Lorentzian*
   covariant polarization with fixed signature conventions plus the tadpole /
   cosmological-constant subtraction. The Euclidean magnitudes above are
   convention-robust; the overall sign is not, so I am not asserting "healthy"
   from this alone.
3. **z=1 for the graviton** follows from IR Lorentz invariance of the source
   propagator (A1 = Zt ⇒ c_eff = 1); a direct check would compute Π^TT(ω,k) and
   confirm the (ω² − k²) structure.

**Suggested next step (Action 1b):** compute the covariant Π^TT(ω,k) on a small
4D Euclidean grid, Wick-rotate, subtract the tadpole, and read off (i) absence
of a k⁰ pole (mass = 0), (ii) sign of the (ω²−k²) coefficient (health), (iii)
M*² vs k_UV scaling. The machinery is already in `ccef_graviton.py`.
