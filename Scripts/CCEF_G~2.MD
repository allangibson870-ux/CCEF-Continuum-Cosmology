# Composite graviton — 4D Euclidean verdict

Settles the three items left open after Action 1, using the real couplings
(A1=1, A2=0.3268, A4=3.5553, Zt=1). Script: `ccef_graviton_4d.py`.

## (1) z=1 and masslessness — confirmed numerically
Computed the covariant TT polarization Π^TT(ω_E, k) on circles of fixed
p² = ω_E² + k² in the Euclidean (ω_E, k) plane, varying the angle from
pure-time → 45° → pure-space.

| p² | spread across angles |
|---|---|
| 0.5 | 0.00% |
| 2.0 | 0.00% |
| 6.0 | 0.00% |
| 12.0 | 0.00% |

Π^TT is a function of p² **only** (Euclidean O(4) symmetry) all the way up to
the 2-particle threshold p²=4A4≈14.2. That is exactly the Wick-rotation
statement: O(4) Euclidean ⇒ after ω_E→iω the polarization is Lorentz
invariant in (ω²−k²) ⇒ **z=1**, and the pole sits at p²=0 ⇒ **massless**.
Below threshold Π is smooth/analytic (matter is gapped), so the massless
graviton is a sharp pole with no absorptive contamination.

## (2) Sign / ghost-vs-healthy — HEALTHY
The flat-space ⟨TT⟩ bubble slope (Action 1, Part C) came out negative, but that
is a seagull-contaminated form factor, **not** the graviton kinetic sign. The
clean object is the induced Einstein–Hilbert coefficient via the
Schwinger–DeWitt heat kernel, whose a₁ = R/6 coefficient is **positive** for a
minimal scalar. Integrating out the two gapped tangent modes (factor 2), with
A3 providing the UV cutoff s_min = 1/k_UV², k_UV² = A1/A3:

    1/(16πG_ind) = (1/96π²) · E1(A4/k_UV²) ≈ (1/96π²) · ln(k_UV²/A4)

| A3 | k_UV² | ln(k_UV²/A4) | 1/(16πG_ind) | M*²=1/8πG | verdict |
|---|---|---|---|---|---|
| 1e-6 (baryon regime) | 1e6 | 11.97 | +1.26e-2 | 2.53e-2 | **healthy** |
| 0.281 (self-dual) | 3.56 | 0.22 | +2.3e-4 | 4.6e-4 | healthy but degenerate |

Both give 1/G > 0 → **non-ghost, propagating massless spin-2**. At the
self-dual point k_UV² = A4 exactly, so the relativistic IR window collapses
(ln→0) and the induced-gravity construction degenerates — independently
consistent with the reference flagging self-dual as disfavoured.

## (3) Masslessness — structural
The heat-kernel expansion generates only a₀ (cosmological constant, tuned away
by the background field equation) and a₁ (the R term). No diff-invariant mass
term for h^TT exists, so m_graviton = 0 is protected — matching the numerical
O(4)/pole-at-zero result in (1).

## Bottom line
The composite-graviton escape **works**: the gapped order parameter induces a
massless, healthy, z=1 spin-2 mode — emergent GR with no fundamental graviton.

## Honest caveat (quantitative, not structural)
The induced Planck mass here grows only **logarithmically** with k_UV, because
the EH term was extracted in the relativistic IR window (standard 4D heat
kernel). The true CCEF UV is Lifshitz z=2 (effective dim d+z=5), where the
scaling of M*² with k_UV could be power-law rather than log. The **sign,
masslessness, and z=1** results are robust to this; the **magnitude/scaling**
of the Planck scale (hence the strength of emergent gravity vs the soliton
scale) is the remaining quantitative question — best answered with the
anisotropic (Lifshitz) heat kernel for the operator ∂_τ² + A4 − A1∇² + A3∇⁴.
