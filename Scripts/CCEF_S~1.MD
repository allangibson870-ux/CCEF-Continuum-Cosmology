# Dressed S³ baryon: dynamical χ + m_σ scan — results

Goal: extend the S³ hedgehog to a dynamical amplitude χ(r) with
V(χ)=(m_σ²/8)(χ²−1)², use the **full induced 4-derivative operator** (not the
pure-Skyrme proxy), scan m_σ, and check whether E·R≈4.06 is reached at
c=m_σ/Λ≈0.5–0.7. Λ=√(A4/A1)=1.886.

Scripts: `ccef_s3_dressed.py` (functional + analytic gradient, verified to 1e-10),
`ccef_s3_relax2.py` / `ccef_s3_relax3.py` (collapse-control relaxers).

## What was built and validated
Hedgehog φ=χ(r)(cosF, sinF r̂). Energy density:

    e = (A1/2)[χ'² + χ²(F'²+2sin²F/r²)]          (2-derivative)
      + [4-derivative operator]                   (see below)
      + (A4/2) χ² sin²F                           (easy-axis term = (A4/2)(1−n₀²)·χ², matches ccef3d.py)
      + (m_σ²/8)(χ²−1)²                            (amplitude stiffness)

Two 4-derivative operators implemented:
- **pure Skyrme** (proxy used in the optimistic core-melting docs): c4·½(S²−TrT2)
- **induced 2:1 mix** (the genuine heat-kernel term, CC694B): B2·[(2/3)S²+(1/3)TrT2]

Important correction made along the way: the potential must be (A4/2)χ²sin²F
(the field-magnitude–weighted easy-axis term, ≥0, →0 at the origin and as χ→0),
**not** χ²(1−cosF); the latter peaks at the origin and produces unphysical
core melting / collapse. With the corrected term the frozen results match:

| operator | E | R (energy-rms) | E·R | degree | virial |
|---|---|---|---|---|---|
| pure Skyrme c4=0.15 | 44.3 | 0.525 | **23.3** | 0.98 | 0.000 |
| induced 2:1, B2=0.025 | 27.3 | 0.396 | **10.8** | 1.00 | 0.001 |
| induced 2:1, B2=0.035 | 32.9 | 0.450 | **14.8** | 1.00 | 0.001 |

The pure-Skyrme frozen number (E·R=23.3, R=0.52) **reproduces the doc's
frozen result** (25.7, 0.52). The induced-operator frozen numbers (E·R≈11–15)
**independently reproduce CC694B's "E·R ~ 9–13"** for the genuine induced term.

## The m_σ scan — and why it does NOT give a clean hit
Allowing χ to relax (dynamical amplitude), free energy minimization does **not**
reproduce the optimistic docs' gentle partial-melt (χ_min≈0.08 in a shell, E·R≈5).
Instead the amplitude **collapses to χ≈0 throughout the soliton interior** — a
"melted core" (restored-symmetry bubble) bounded by a χ domain wall — at every
m_σ tested, even stiff m_σ=3.5 (c=1.86):

| c=m_σ/Λ | m_σ | E | R | E·R | χ_min |
|---|---|---|---|---|---|
| 1.86 | 3.50 | 0.6 | 1.24 | 0.8 | 0.000 |
| 1.00 | 1.89 | 0.6 | 1.38 | 0.8 | 0.000 |
| 0.70 | 1.32 | 0.6 | 1.98 | 1.1 | 0.000 |
| 0.50 | 0.94 | 0.6 | 3.72 | 2.4 | 0.000 |

Why: the gradient energy density χ²(∇n)² at the soliton wall is O(10–50), so
melting saves far more (≈15·χ²) than the amplitude potential costs at χ=0
(m_σ²/8 ≈ 0.1–1.5). Melting therefore always wins, and as it proceeds the
Skyrme stabilizer (∝χ⁴) dies, removing size stabilization. The resulting E·R is
dominated by the (crudely resolved) χ-wall and sweeps from <1 up toward ~2.4 as
m_σ softens — it never sits at a controlled stationary value of 4.06.

## Bottom line (honest)
**The full induced operator does not deliver a stable E·R≈4.06 at c≈0.5–0.7.**
- Frozen induced soliton: E·R≈11 (≈2.6× the proton) — corroborates CC694B.
- Dynamical-χ "core melting", under genuine free minimization, drives a full
  amplitude collapse (χ→0, melted core), not the gentle χ_min≈0.08 partial-melt
  the optimistic docs assume. There is no robust stationary dressed soliton at 4.06.
- So core-melting as a *mechanism* lowers E·R a lot, but not in a controlled way
  that lands on the proton; the optimistic E·R≈5 figure appears to be a
  **constrained / metastable** configuration, not the free minimum.

This supports CC694B's pessimistic verdict over the optimistic core-melting
notes: the one-loop S³ baryon is ~2–3× too heavy-for-its-size, and amplitude
dressing does not cleanly close the gap.

## What would settle it (next step, not done here)
The doc's partial-melt branch (χ_min≈0.08) — if it exists as a genuine local
minimum — must be found with a constrained solver, not free gradient flow:
solve the coupled Euler–Lagrange BVP for (F,χ) at fixed baryon number with the
size held by a Lagrange constraint (or a Newton/relaxation BVP solver), and test
whether that branch is a true local minimum or a saddle. Only then is the
m_σ→E·R curve trustworthy near 4.06. The verified functional + analytic
gradients in `ccef_s3_dressed.py` are the right starting point.
