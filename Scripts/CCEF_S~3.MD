# Skyrme stabilization from collective/induced effects — test result

Test of the proposal: dress the Skyrme coefficient B2→B2(χ) (or add a 6-derivative
term ∝χ⁶|∂n|⁶) so stabilization survives the melt region and resurrects a stable
dressed baryon. Script: `ccef_s3_dressedB2.py` (induced 2:1 operator, analytic
gradient verified 1e-10). Parametrized by the **amplitude power** of each
stabilizer: e4 = B2·χ^q·K4(F),  e6 = c6·χ^p·(baryon density)².

## Headline: the mechanism works for STABILITY, not for MASS
A stabilizer that **survives the melt** (low χ-power) removes the collapse and gives
a clean, virial-stable, degree-1 soliton — but its E·R stays ≈13, **not** the
proton's 4.06.

### Skyrme amplitude power q (induced operator, B2=0.025)
| c=m_σ/Λ | q | E | R | E·R | χ_min | degree | virial |
|---|---|---|---|---|---|---|---|
| 0.70 | 4 (φ-form, dies in melt) | 0.5 | 1.45 | 0.7 | 0.00 | 0.99 | **1.07 (not stationary)** |
| 0.70 | 2 | 2.4 | 0.66 | 1.6 | 0.00 | 0.99 | 1.10 (not stationary) |
| 0.70 | **0 (n-form, survives)** | 17.1 | 0.78 | **13.4** | 0.00 | 1.00 | **−0.00 (stable)** |
| 0.50 | 0 | 16.4 | 0.99 | **16.2** | 0.00 | 1.00 | 0.00 (stable) |

### 6-derivative term (added to the collapsing q=4 baseline, c=0.70)
| config | E | R | E·R | virial |
|---|---|---|---|---|
| none | 0.5 | 1.45 | 0.7 | 1.07 (collapsed) |
| 6-deriv **p=6 (∝χ⁶, literal)** | 0.5 | 1.43 | 0.7 | 1.07 (collapsed) |
| 6-deriv **p=0 (survives)** | 20.0 | 0.68 | 13.6 | −0.25 (stabilized) |
| 6-deriv p=0, stronger | 32.1 | 0.86 | 27.7 | −0.24 (stabilized) |

## Two key conclusions

**1. My earlier "collapse" was an amplitude-power artifact.** The collapse occurred
only for the φ-form Skyrme term (q=4, i.e. χ⁴|∂φ|⁴). The physically-correct CCEF
Faddeev term acts on the **unit direction n** (as coded in `ccef3d.py`), i.e. q=0 /
χ-independent — and that term does **not** collapse. So the optimistic core-melting
docs' E·R≈5 corresponds to the *partially-collapsed* φ-form branch, which is not the
stable physical soliton; the stable soliton has E·R≈13.

**2. There is a structural trade-off — you cannot melt-and-lighten and stay stable.**
- To *lower* E·R by melting, the stabilizer must **die** in the melt (high χ-power)
  → but then it cannot stabilize → collapse (unphysical).
- To *stabilize*, the stabilizer must **survive** the melt (low χ-power, the literal
  ∝χ⁶ **fails** here — it dies; you need ∝χ⁰) → but then it is melt-independent, so
  melting can no longer reduce the dominant energy → E·R stays ≈13.

A single amplitude power cannot give both. Dressing B2→B2(χ) toward a melt-surviving
form resurrects a **stable** baryon but leaves it ~3× too heavy-for-its-size.

## Verdict
The collective/induced Skyrme dressing **does** resurrect stabilization (this is the
correct fix for the collapse, and clarifies that the collapse was a wrong-amplitude
artifact), but it does **not** bring E·R to the proton. With the genuine induced 2:1
operator the stable dressed baryon sits at E·R≈13 — consistent with CC694B. Amplitude
dressing therefore stabilizes the soliton but does not close the nucleon mass-radius
gap; the residual factor of ~3 is real, not an artifact of collapse.

What this leaves: the gap is not closable by (i) a richer χ-potential (sextic test,
failed) nor (ii) melt-surviving stabilizers (this test — stabilizes but stays heavy).
The honest standing of the matter sector is CC694B's: S³ baryon ~2–3× too heavy-for-
its-size at one loop, while the gravity/cosmology spine is unaffected.
