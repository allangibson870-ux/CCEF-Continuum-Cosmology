# Finite-T effective potential V_eff(χ,T): thermal cubic, T_c, and the barrier test

The real test of the hot-transition hypothesis. Computed the finite-temperature one-loop
effective potential for the CCEF order-parameter amplitude χ, with the emergent gauge field
(the Higgsed CP¹ U(1), and the S³ SU(2) variant) as the thermal-cubic source. Params:
A4=3.5553, e_γ²=1/4A2=0.765, tree quartic a₄=m_σ²/8=0.444, Λ=√A4=1.886.

## 1. Thermal cubic — CONFIRMED (the hypothesis was right that it exists)
The high-T expansion gives V_eff(χ,T) = (a₂_tree + D T²)χ² − **E T χ³** + a₄χ⁴, with the
cubic coefficient from the gauge thermal loop:

  E = n_gauge · e_γ³ / (12π) = **0.053** (U(1), 3 dof) … **0.16** (SU(2), 9 dof)

This is **19–57× larger** than the zero-T gauge Coleman-Weinberg coefficient (0.0028) —
exactly as anticipated: the thermal term scales as ~T and is **not** 1/64π²-loop-suppressed.
So a thermal cubic genuinely appears once the transition is hot.

## 2. Critical temperature — FOUND
The transition occurs at **T_c ≈ 1.1–1.3 CCEF (≈ 0.6–0.7 Λ)** (U(1): 1.285; SU(2): 1.11).
Full-J_B scan: as T rises toward T_c the broken minimum moves from χ≈0.83 (T=1.0) smoothly
toward 0 — a transition does happen at a well-defined T_c.

## 3. Is the barrier strong enough for the two-phase baryon at E·R≈4? — NO
Two independent reasons, both decisive:

**(a) The transition is far too weakly first-order — effectively second-order.**
- Order-parameter jump χ_c/T_c = E/2a₄ = **0.06** (U(1)), **0.18** (SU(2)). Strong first-order
  needs χ_c/T_c ≳ 1; CCEF is ~6–17× below that.
- High-T barrier height ≈ a₄χ_c⁴/16 ≈ **1e-6** (U(1)) to **4e-5** (SU(2)) — i.e. 2e-6–1e-4 of
  the condensation energy.
- The **full thermal function** (not the expansion) shows **no resolvable barrier at all**:
  the broken minimum slides continuously to zero through T_c, and the near-origin bump is
  negative (no metastable disordered phase). So in practice the transition is **continuous /
  second-order**; the thermal cubic is real but too weak (e_γ²≈0.77 is ~6× too small) to
  carve a usable barrier.
- Negligible barrier ⇒ negligible surface tension ⇒ no thin-wall two-phase bubble to
  stabilize a melted-core baryon.

**(b) Even the tiny finite-T barrier vanishes at the present T=0 — where the proton lives.**
At T=0 the potential is V = a₄(χ²−1)², for which χ=0 is a **maximum** (V''(0)=2a₂_tree<0):
no metastable disordered phase, no barrier, in any gauge case. The thermal barrier is a
near-T_c feature only. The present proton is a T≈0 object, so it sees the second-order
potential and is **not** stabilized as a two-phase object regardless of the early-universe
transition.

## Verdict
- **Thermal cubic: confirmed** (and ~20–60× the zero-T term — the hypothesis's central
  physics point was correct).
- **T_c: found**, ≈0.6–0.7 Λ.
- **Barrier strong enough to stabilize the two-phase baryon at E·R≈4: no.** The emergent
  gauge coupling is too weak (χ_c/T_c≈0.06–0.18 ≪ 1, effectively second-order), and the
  barrier vanishes at the present T=0 where the proton actually exists.

So the hot-transition route **does not rescue the baryon mass**. It is a genuine, quantitative
"no" — not the cold-case "no thermal term at all," but "the thermal term is there yet too
weak, and it's the wrong temperature for today's proton."

## What survives / side-results
- **Baryon genesis is fine:** even a second-order/weak transition forms topological defects
  (the baryons) via the Kibble mechanism — the cosmological "matter from ordering" picture
  holds; only the mass-lowering via two-phase stabilization fails.
- **GW prediction:** a weak/second-order transition gives little-to-no stochastic
  gravitational-wave background from bubble collisions — so CCEF predicts a *small* primordial
  GW signal from this transition (a falsifiable contrast with strongly-first-order scenarios).
- The baryon-mass options remain: (a) a fundamental tree-level Lorentz-invariant Skyrme
  coupling (~0.012, one parameter); (b) accept the ~4× near-miss with a high-scale safe
  regulator. The gravity/cosmology spine is untouched.

## Caveats
- High-T expansion is marginal (T_c ~ masses), so the *full* J_B treatment was used for the
  barrier conclusion (it shows effectively second-order); the high-T numbers (E, χ_c/T_c) are
  the analytic cross-check.
- Daisy/ring resummation of the scalar sector was approximated by thermal masses; it does not
  create a barrier (it weakens, not strengthens, first-order), so the conclusion is robust.
- e_γ²=1/4A2 is the exact CCEF identity; strong first-order would need A2 ~10× smaller.
