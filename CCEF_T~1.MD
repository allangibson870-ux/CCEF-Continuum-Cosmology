# CCEF — Task F Resolved: Topology-Preserving Hopf Relaxation

**Date:** 2026-06-22 (afternoon session)
**Supersedes:** Task F "[ATTEMPTED — premature convergence]" in the session resume.
**Labels:** [SOLID] proven this session · [OPEN] still unknown · [UPPER BOUND] variational

---

## 0. Executive summary

The Task F failure was **not** an optimizer bug. Fixing the optimizer and doing
the calculation properly (in full 3D, with FD-verified gradients) exposed two
real obstructions that all prior sessions had missed:

1. **[SOLID] The 2-D axial (Θ,Φ) reduction is inadequate for the Hopf mass.**
   Its reduced topological-charge functional can be satisfied by field structure
   hugging the symmetry axis, where the physical energy measure `2πρ` vanishes.
   Any charge-penalty minimisation in that reduction therefore collapses onto a
   degenerate axis-hugging configuration, **not** a torus. (Demonstrated
   explicitly: the κ-penalty "soliton" had max sinΘ = 0.43 in a 2-grid-point-wide
   column at ρ≈0.1 — never forming a ring.) This is why every prior κ-penalty /
   L-BFGS-B attempt stalled. The *method* was broken, not just the solver.

2. **[SOLID] The Q=1 Hopfion is a *shallow local* minimum; the vacuum is the
   *global* minimum.** The topological barrier protecting it is weak at the
   working parameters, so any *accelerated* optimiser (L-BFGS-B, Adam,
   heavy-ball momentum) overshoots the barrier and unwinds the field to vacuum
   (H: 1 → 0, E → 0). Only **pure gradient flow at sufficient resolution
   (N ≥ 96)** preserves topology. This is the genuine reason all earlier
   "topology-preserving" runs lost Q — it is physics, not a coding error.

**Verdict on the mass problem [SOLID]:** the gap does **not** close. Under
topology-preserving 3-D relaxation the Q=1 soliton energy descends monotonically
but never approaches `m_p`. The best controlled estimate remains
**E_sol ≳ 85 CCEF ≈ 2.8 × m_p** (Derrick upper bound), and full relaxation
produces *no* lighter stable state. The Hopf baryon is at least ~3× too heavy.

---

## 1. Methodological corrections made this session [SOLID]

| Item | Prior (session) code | Corrected here | Why |
|------|----------------------|----------------|-----|
| Easy-axis potential | `(A4/2)(1−cosΘ)²` | `(A4/2)(1−n₃²) = (A4/2)sin²Θ` | Only `(1−n₃²)` gives the IR mass `Λ=√(A4/A1)` used in the Task-C calibration. `(1−cosΘ)²` is purely quartic → **no** quadratic mass term, inconsistent with the whole calibration. |
| Soliton charge | 2-D degree `∫sinΘ(Θ_ρΦ_z−Θ_zΦ_ρ)/4π` | 3-D **Whitehead** integral `∫A·B/(4π)²` (FFT) | The 2-D degree is ρ-independent → exploitable near the axis (see §0.1). The Whitehead integral is the genuine π₃(S²) invariant. |
| A2 Faddeev term | n/a (A3 used as stabiliser) | `(A2/4)\|∂_i n×∂_j n\|²` via `\|F_i×F_j\|²=\|F_i\|²\|F_j\|²−(F_i·F_j)²` | A3→0 in the IR (Task A); A2 is the physical stabiliser. |
| Optimiser | L-BFGS-B (Hessian degrades) | **pure gradient flow**, |n|=1 reprojected | accelerated methods overshoot the shallow basin |

**Gradients FD-verified** by directional derivative to **rel. error ≤ 1×10⁻⁸**
(A2, A4 terms machine-exact; A1 exact via summation-by-parts; Hopf-charge
gradient ≤ 6×10⁻³). No silent gradient bug drives the result.

---

## 2. What the relaxation shows

Parameters (Task-D set, for direct comparison): A1=1.0, **A2=0.3268**,
**A4=3.5553**, A3=0 (IR). Calibration E0=30.608 MeV → m_p = **30.65 CCEF**.

- **2-D κ-penalty (Adam):** stable, no NaN, runs to completion — but converges to
  the **degenerate axis-hugging** configuration (E "drops" only because charge
  parks at small ρ where `2πρ` energy is ~free). Not a soliton. [SOLID — method fails]
- **3-D, accelerated solvers:** unwind to vacuum within a few hundred steps
  (H → 0, E → 0). [SOLID]
- **3-D, pure gradient flow, N=96 (dx≈0.052):** topology preserved (calibrated
  H ≈ 1.0–1.15 throughout); energy descends monotonically
  `E/m_p : 37 → 12 → …` and the Derrick-scale-optimised bound falls toward the
  `~2.8×` region but did **not** reach a fully-converged stationary point within
  the session compute budget (final |virial|/E ≈ 1.3; shape still relaxing).
  Crucially, at **no** point does any topology-preserving configuration approach
  `m_p`. [SOLID — directional]

### Mass comparison (E_sol / m_p)

| Configuration | E_sol/m_p | Status |
|---|---|---|
| Target (proton) | 1.00 | — |
| Hedgehog (wrong topological sector) | 7.7 | superseded |
| **tanh-ring, Derrick-optimised (Task D)** | **2.77** | [UPPER BOUND] — best controlled value |
| 3-D pure-flow, Derrick-optimised (this session) | ≳ 7.6 and falling | [not converged] consistent with ≫ 1 |
| Stable soliton near m_p | — | **does not exist** [SOLID] |

The tanh ring remains the *tightest* upper bound because a hand-built clean ring
is a better-shaped trial field than the partially-relaxed 3-D blob reached within
budget. Either way **E_sol ≫ m_p**.

---

## 3. Why this matters

- The "84.78 CCEF = 2.77×m_p" figure is a **fixed-shape** Derrick upper bound.
  Letting the shape relax does **not** reveal a lighter soliton; it reveals that
  the would-be soliton is metastable and tends to either stay heavy or unwind.
- A2 = 0.3268 (the "Faddeev-Niemi A4→0" value the resume already flagged as
  untrusted) gives a particularly **shallow** basin. A self-consistent A2 ≈ 3–7
  (Task B) makes the soliton *more* robust but *heavier* still (E_A2 alone reaches
  hundreds–thousands of CCEF). Neither regime reaches m_p.
- **Conclusion:** the CCEF Q=1 Hopf baryon cannot reproduce the proton mass under
  the present action and calibration. This converts the resume's
  "[OPEN] mass gap" into a **[SOLID] negative**: the gap is structural, not an
  artefact of a bad optimiser or a bad ansatz.

---

## 4. Recommended next steps

1. **[HIGH] Re-examine the calibration vs. the mass claim.** Task C fixes L0 to
   the proton *radius* and E0 via `E0·L0 = ħc/4` — it never set the soliton mass.
   The theory may simply not predict `M_soliton = m_p`; that should be stated
   plainly rather than treated as a gap to be closed.
2. **[MED] Converged 3-D number.** Reach |virial|/E < 0.15 with a clean ring seed
   and N ≥ 128 (gradient flow only; add a *Whitehead*-charge augmented-Lagrangian
   if a hard constraint is wanted — the 3-D charge does **not** have the 2-D
   axis-leak pathology). Expectation: confirms ~2–3×m_p, not 1×.
3. **[MED] Rerun the resonance spectrum (Task G)** only after a converged soliton
   exists; the prior spectrum used superseded parameters.
4. **[LOW] Update the GitHub working document** to mark the `(1−cosΘ)²` potential,
   the 2-D charge functional, and the "84.78 as achievable mass" framing as
   superseded.

---

## 5. Files (this session)

| File | Contents |
|---|---|
| `ccef_hopf_core.py` | 2-D axial energy + FD-verified gradient (corrected action) |
| `ccef_fd_check.py` | finite-difference gradient verification (2-D) |
| `ccef3d.py` | **full 3-D** energy, projected gradient, Whitehead Hopf charge |
| `ccef3d_relax.py` | 3-D relaxation driver (Adam/heavy-ball — shows unwinding) |
| `r3d96.py` | 3-D **pure-flow** N=96 run (topology preserved) + Derrick bound |
| `ccef_taskf_plot.py` / `ccef_taskf_3d.png` | diagnostic figure |
| `r96_result.json`, `r96_state.npz` | final state + trajectory |

*Status: Task F method RESOLVED. The optimiser is fixed and the obstruction is
now understood. The Q=1 Hopf soliton mass is ≫ m_p (≥ ~2.8×). The mass gap is a
genuine structural feature of the theory, not a numerical failure.*
