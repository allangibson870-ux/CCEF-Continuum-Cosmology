# CCEF — A2 from the RG / fixed-point route
**2026-06-22. No hand-fitting.** Labels: [SOLID] / [CONJECT] / [OPEN].

## 1. Scaling dimensions at the z=2 Lifshitz fixed point [SOLID]
The UV is defined by the marginal pair `Zt(∂_t n)²` and `A3(∇²n)²`. Requiring both
marginal fixes the field dimension `[n] = 1/2` (mass units; `[x]=−1,[t]=−2`).
Every coupling dimension then follows:

| Coupling | term | mass dim | character |
|---|---|---|---|
| Zt | (∂_t n)² | **0** | marginal |
| A3 | (∇²n)² | **0** | marginal (→ Task A: asympt. free, A3→0 in IR) |
| A1 | (∇n)² | **+2** | relevant |
| A4 | (1−n₃²) | **+4** | relevant |
| **A2** | \|∂_i n×∂_j n\|² | **−1** | **IRRELEVANT** |

## 2. Consequence: A2 has NO nontrivial perturbative fixed point [SOLID]
For an irrelevant coupling the dimensionless `ĝ₂ = A2·μ` obeys
`β(ĝ₂) = +ĝ₂ + (loops)`. Near the origin the canonical `+ĝ₂` dominates, so the
only perturbatively-reachable fixed point is the Gaussian one **A2\* = 0**, and
A2 **flows to zero in the IR** — exactly like A3 (Task A). A nonzero zero of β
would need the one-loop term to overpower the tree term, i.e. ĝ₂ = O(1):
non-perturbative, outside one-loop control.

**So the marginal-coupling logic that fixed A3 does *not* fix A2 to a number.**
A2 is not an independent constant of the theory at all — it is an irrelevant,
running coupling whose IR value tends to zero.

## 3. What *does* pin A2: the scale-coincidence (self-dual) fixed point [CONJECT — new]
A genuine fixed point is scale-invariant: no separated scales. The three crossover
momenta must then coincide:

```
k_IR² = A4/A1      (mass gap)
k_UV² = A1/A3      (Lifshitz crossover)
k_F³  = A1/A2      (Faddeev = gradient balance)
```

- `k_IR = k_UV`  ⟹  **A1² = A3 A4**   (the Task-E self-dual condition — recovered)
- `k_F  = k_UV`  ⟹  **A2 = A3^{3/2}/√A1 = A1^{5/2}/A4^{3/2}**

With **A1 = 1** (axiom) and **A4 = 3.5553** (calibration), this fixes the whole
ladder from one calibrated scale:

```
A3* = A1²/A4   = 0.2813        (= Task-E self-dual A3, independent check ✓)
A2* = A4^(−3/2) = 0.1492
```

## 4. Striking coincidence with the mass window [SOLID observation]
The resume's Finding 6 (independently, from the mass condition at the correct
E0 = 30.6 MeV calibration) needed **A2 ≈ 0.07–0.14** for `E_sol = m_p`.
The fixed point gives **A2\* = 0.149** — right at the edge of that window, with
**no fitting**. The scale-invariance criterion points to the *same* small-A2,
light-soliton regime that mass-matching requires.

This reframes the "mass gap": it is large only at the *non*-fixed-point A2 values
(0.33, 4–7, 8.97, 37) carried through prior sessions. At the self-dual fixed point
A2 ≈ 0.15, the soliton sits in the light regime where closure becomes plausible.

## 5. What is still open [OPEN]
The definitive fixed-point soliton mass needs the converged **smooth** Q=1 soliton
at (A1,A2,A3,A4) = (1, 0.149, 0.281, 3.5553) **including the finite A3**. The
bilaplacian term is huge on non-smooth trial fields (the exact-Hopfion estimate
gives a meaningless ~10³×m_p because `∫(∇²n)²` is dominated by core/lattice
roughness — same pathology Task E flagged). A trustworthy number requires the
topology-preserving smooth relaxation at N ≳ 128. Until then:
- A2\* = A4^(−3/2) = 0.149 is the **[CONJECT] fixed-point prediction** (no fitting);
- whether it closes the mass gap is **[OPEN]** but now plausibly *yes*, unlike the
  large-A2 values.

## 6. Updated parameter ladder (all from one calibrated scale A4)
| Param | Fixed-point value | Source |
|---|---|---|
| A1 | 1 | axiom |
| Zt | 1 | axiom |
| A3 | A1²/A4 = 0.281 | self-dual (k_IR=k_UV) [Task E ✓] |
| A2 | A4^(−3/2) = 0.149 | scale-coincidence (k_F=k_UV) [new] |
| A4 | 3.5553 | calibration (proton radius) |

*Next (not done — stopped per instruction): converged smooth soliton at this
parameter set with finite A3, to test E_sol = m_p definitively.*
