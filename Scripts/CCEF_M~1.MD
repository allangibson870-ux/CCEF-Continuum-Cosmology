# CCEF — Mass Gap: does it close at the fixed point? **No.**
**2026-06-22. No hand-fitting.** Labels: [SOLID] / [OPEN].

## Question
Does the Q=1 Hopf soliton mass equal m_p at the self-dual RG fixed point
(A1=1, A2=A4^−3/2=0.149, A3=A1²/A4=0.281, A4=3.5553; E0=30.6 MeV ⟹ m_p=30.65 CCEF)?

## Answer: the gap does NOT close [SOLID]
Direct 3-D variational computation (smooth ring ansatz, all terms, finite-A3
machinery FD-verified to 1e-9), Derrick-optimised over scale and shape:

| Treatment of A3 | best E_sol / m_p |
|---|---|
| A3 → 0 (IR limit — Task A: A3 irrelevant, "drop for soliton mass") | **≈ 4.3×** (crude ansatz; optimised shape ~2.8–4×) |
| A3 = 0.281 retained (self-dual UV value) | **≈ 24×** (bilaplacian dominates) |

Neither reaches 1.0. The soliton is robustly **several × too heavy**.

## Why the earlier "it might close" was wrong [SOLID]
The resume's Finding 6 ("A2 ≈ 0.07–0.14 ⟹ E_sol = m_p") came from the **flawed
2-D axial estimate** (charge leaks to the axis; energy mismeasured). Recomputed
properly in 3-D at the fixed-point A2 = 0.149, E_sol ≈ 4.3 m_p, not m_p. The
numerical coincidence between the fixed-point A2 and that window was therefore a
coincidence of a bad estimate, not physics.

## Two-scale tension (the genuine remaining subtlety) [OPEN]
A2 and A3 are **both IR-irrelevant** (flow to 0 at long distance). A static energy
with fixed couplings is thus ambiguous:
- drop them → soliton wants to collapse (need a stabiliser);
- keep the self-dual values → A3 bilaplacian makes it heavy (24×).
The honest soliton mass needs the **running** A2(k), A3(k) evaluated at the soliton
scale (the resume's unfinished "two-scale" programme). But the *spread* of
defensible answers (≈3× to ≈24×) is **entirely above** m_p — closing to 1.0 is not
within reach of any non-fitting choice.

## What closing the gap would require (and why it's not allowed)
From the calibration identity `m_sol/m_p = (E_sol/√A4)·ħc/(4 r_p m_p)`:
- the soliton sector would have to deliver `E_sol/√A4 = 16.2` — but it delivers ≈45–250; or
- the conjectured **1/4** in `E0·L0 = ħc/4` would have to be ≈ **1/17** (a factor ~4).
Either is a tuning to the answer ⟹ forbidden by the no-fit rule.

## Conclusion [SOLID]
**The CCEF Q=1 Hopf baryon does not reproduce the proton mass.** It is a genuine,
falsifiable prediction of the theory + calibration, and it comes out ≈3–24×
(best-case ≈3–4×) too heavy. This is not an optimiser failure, a sector error, or
a calibration freedom — it is structural.

The constructive reading (consistent with the theory's own logic): the calibration
fixes the proton **radius** and the **ħc** relation; the **mass** is then a
*prediction*, and the theory currently predicts a baryon several times too heavy.
The correct next move is **not** to keep hunting parameters but to either (a) derive
the ħc coefficient from first principles (it may not be 1/4), or (b) accept that
M_soliton ≠ m_p is what this action predicts and report it as such.

*Methods: ccef3d.py (3-D energy, projected gradient, Whitehead charge, finite-A3
bilaplacian; all gradients FD-verified ≤1e-8). Variational bounds use smooth ring
ansatze; full topology-preserving relaxation at small A2 unwinds on affordable
lattices because the light-soliton regime has a low topological barrier — itself
consistent with "no light, strongly-bound Hopf baryon exists here."*
