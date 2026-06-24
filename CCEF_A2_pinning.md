# CCEF — Can A2 be pinned? (first OPEN action)
**2026-06-22. No hand-fitting.** Labels: [SOLID] / [OPEN].

## Result: A2 is NOT pinnable by soliton self-consistency [SOLID]
With **A1 = 1** (axiom) and **A4 = 3.5553** (calibration) fixed, A2 is the single
remaining free coupling, and soliton physics depends only on the dimensionless
ratio **A4/A2** plus the overall scale (set by A1).

- The Virial `E_A1 − E_A2 + 3E_A4 = 0` is **identically satisfied at every relaxed
  soliton** — it is what "energy minimum" means, not an extra equation. So it
  yields **no condition on A2**. This is precisely why Task B's iteration was
  seed-dependent and returned a whole family (A2 ≈ 3.4–6.9).
- The four floating values are therefore **not** competing measurements of one
  quantity; they are different choices of the last free coupling.

## What A2 controls (Derrick-optimal on the exact H=1 Hopfion shape, A4=3.5553)
| A2 | A4/A2 | E_sol/m_p (upper bound) |
|----|-------|--------------------------|
| 0.327 (FN, untrusted) | 10.9 | 13.6 |
| 4.0 (Task B) | 0.89 | 58 |
| 6.9 (Task B) | 0.52 | 82 |
| 8.971 (superseded) | 0.40 | 97 |
| 37.4 (v3.1 core) | 0.10 | 254 |

Absolute values are loose (fixed exact-Hopfion shape; the optimal tanh ring lowers
the A2=0.327 case to 2.77×). The **monotonic trend is robust: larger A2 ⇒ heavier
soliton.** No A2 reaches m_p; the gap is least violated at small A2, but A2→0
removes the stabiliser (Derrick collapse) ⇒ a floor near **2.8×m_p**.

## The one principled reference value
Faddeev–Niemi self-balancing (gradient energy = Skyrme energy on the Hopf shape):
**A2_FN = E_A1/E_A2 ≈ 2.7** (consistent with the resume's "1.97–2.9 on the Hopf").
A natural anchor, but it is the A4→0 limit and shape-dependent — not a unique pin.

## Conclusion / next action
A2 must be fixed by an **independent principle**, not soliton self-consistency:
1. **RG fixed point** β(A2)=0 — the same route that fixed A3 (Task A). *[recommended next]*
2. self-duality / BPS condition, or
3. a normalisation axiom (as for A1, Zt).

The resume's logic "Task C pins A4 → Virial pins A2" is therefore **void**;
A2 remains [OPEN] pending one of the above.

*Script: shape integrals via `ccef3d.py` (gradients FD-verified to 1e-8).*
