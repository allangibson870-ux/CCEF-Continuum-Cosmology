# Sextic core penalty test — does it stabilize a shallow melt?

Test of the proposal: add a positive sextic to the radial potential to penalize
the deep χ=0 core and stabilize a shallow melt without new free parameters.
Script: `ccef_s3_sextic.py` (induced 2:1 operator, analytic gradient verified 1e-10).

## Sign correction
The literal `+λ(χ²−1)³` is **negative** at χ=0 (it *rewards* melting), so it
can't penalize the core. The correct-sign, bounded form is

    V_sext = λ(1−χ²)³   for χ<1   (flat for χ>1, so no χ>1 runaway)

This is ≥0, vanishes with its first two derivatives at χ=1, and adds +λ at χ=0.

## Result: the sextic does NOT cure the collapse
Size-adaptive relaxation, c=m_σ/Λ=0.70 (m_σ=1.32), induced operator B2=0.025:

| λ | E | R | E·R | χ_min | virial |
|---|---|---|---|---|---|
| 0.0 | 0.46 | 1.01 | 0.46 | 0.000 | 1.05 |
| 0.5 | 0.46 | 0.92 | 0.42 | 0.000 | 1.07 |
| 2.0 | 0.48 | 0.93 | 0.44 | 0.000 | 1.11 |
| 6.0 | 0.52 | 1.05 | 0.54 | 0.000 | 1.21 |
| 15.0| 0.58 | 0.95 | 0.55 | 0.000 | 1.32 |

Even λ=15 leaves χ_min→0 and a non-stationary (virial≠0), collapsed soliton.

## Why a polynomial penalty can't win
The melting saves gradient energy ≈ ½A1(1−χ²)(∇n)², which stays roughly
**constant in (1−χ²)** as χ→0. Any `(1−χ²)ⁿ` penalty has a restoring force
`−∂V/∂χ ∝ χ(1−χ²)ⁿ⁻¹` that **vanishes linearly as χ→0**. So near the core the
penalty's marginal cost goes to zero while the gradient saving does not — the
melt always wins at χ=0. Raising λ raises the *height* at χ=0 but not the
*slope* that would push χ back up. This is structural, not a tuning failure.

## One ambiguous hint
A heavily damped, size-pinned melt from the frozen state (λ=10) transiently held
χ_min≈0.55 in a shell at r≈0.49 — i.e. the penalty *can* arrest melting in a
constrained setting — but that run was **not energetically convergent** (E and R
blew up), so it yields no trustworthy E·R. It only suggests the shallow-melt
branch may exist *as a constrained solution*, consistent with the earlier
finding that it is not the free minimum.

## Verdict
The sextic core penalty, as proposed, does **not** stabilize a shallow melt
under free relaxation and does **not** deliver a controlled E·R≈4.06. Combined
with the earlier scan, the dressed-S³ program does not close the nucleon gap by
amplitude dressing alone — supporting CC694B's verdict (induced operator →
E·R~9–13, proton missed ~2–3×).

The remaining viable route is **not** a richer χ-potential but a proper
**constrained solver**: relax (F,χ) at fixed baryon number with the size held by
a Lagrange multiplier (or Newton/relaxation of the Euler–Lagrange BVP), then test
whether the shallow-melt branch (χ_min~0.1–0.5) is a genuine local minimum and,
if so, read its E·R(m_σ). The user's second idea — a running m_σ(χ) (soft core,
stiff shell) from the same O(4) loops as the graviton — would change the *slope*
of the restoring force near χ=0 and is the more promising potential-side fix; it
was not tested here due to session limits.
