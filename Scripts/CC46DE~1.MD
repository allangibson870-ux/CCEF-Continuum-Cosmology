# UV re-pin refinement + Lifshitz effects on the soliton (#5) — refined

**Correction first:** last session I reported a Lifshitz re-pin factor ≈0.66 (→ frozen
E·R≈6). That was a coarse 2D-grid artifact. Doing the frequency integral **analytically**
and the radial integral at high resolution gives **0.95** — a ~5% effect, not 35%. The
optimistic "Lifshitz → E·R≈6" conclusion is **withdrawn**. Details below.

## (a) Refined Lifshitz re-pin factor for the induced Skyrme coefficient
Induced 4-derivative coeff ∝ ∫d³k dω/(ω²+A1k²+A3k⁴+m²)². The ω-integral is exact:
∫dω/(ω²+X)² = π/(2X^{3/2}), leaving a 1D radial integral
∝ ∫k²dk/(A1k²+A3k⁴+m²)^{3/2} (m²=A4=3.555). Ratio of the Lifshitz value (A3≠0, UV-finite)
to the relativistic value (A3=0, hard cutoff k_UV=√(A1/A3)):

| A3 | k_UV | ratio z2/z1 |
|---|---|---|
| 0.281 (self-dual) | 1.9 | 1.55 |
| 1e-2 | 10 | 0.87 |
| 1e-4 | 100 | 0.92 |
| **1e-6 (baryon regime)** | 1000 | **0.949** (converged, grid-independent) |

So in the baryon regime the genuine Lifshitz UV suppresses the induced Skyrme coefficient
by only ≈5%: B2 ≈ 0.020 → 0.019. Frozen E·R moves from ≈9 to ≈8.8 — **negligible**.
(At self-dual A3 the factor is >1, i.e. it would *increase* B2, but self-dual is
independently disfavored — see (b).)

## (b) Lifshitz on the static soliton = the A3 spatial bilaplacian
The z=2 time-dispersion does not enter a *static* classical soliton; the only Lifshitz
term in the static energy is the spatial bilaplacian (A3/2)(∇²n)². Computed on the
relaxed frozen S³ hedgehog (induced operator, B2=0.02, E=24.3):

| A3 | E_A3 / E |
|---|---|
| **1e-6 (baryon regime)** | **3.5e-5** |
| 1e-4 | 3.5e-3 |
| 1e-2 | 0.35 |
| 0.281 (self-dual) | 9.8 |

This confirms the reference's "E_A3/E ~ 4e-5": at the baryon-regime A3~1e-6 the
bilaplacian is **dynamically dead** (the soliton is z=1, profile unaffected). It only
matters for A3 ≳ 1e-2, and at the self-dual point it would carry ~10× the rest of the
energy — quantitatively explaining why self-dual A3 makes the baryon enormously heavy
(reference E·R ~ 77–1061) and is disfavored. Note the bilaplacian only ever **stiffens**
(adds positive energy); it never softens the soliton, so "Lifshitz on the profile" cannot
lower E·R.

## Net result of #5 (honest, corrected)
Neither lever helps in the baryon regime:
- **Re-pin:** ~5% (factor 0.95), not 35%. Frozen induced E·R ≈ 9 → ≈ 8.8.
- **Bilaplacian:** dead (E_A3/E ~ 3.5e-5) at A3~1e-6; only stiffens.

So #5 does **not** close the matter-sector gap. The frozen induced S³ baryon stays at
E·R ≈ 9–11 (~2–3× the proton's 4.06), reaffirming CC694B. The previous session's
suggestion that UV re-pinning brings frozen E·R to ~6 was wrong (the 0.66 artifact);
the corrected factor leaves it essentially unchanged.

## Where this leaves the matter sector
With melting ruled out (collapses/stays heavy; FRG doesn't rescue — prior session) and
UV re-pin now shown negligible, the only remaining lever is **collective quantization**
(resume #2). Acting on an E·R≈9–11 soliton, even a generous 20–40% mass reduction lands
at E·R ≈ 5.4–8.8 — closer to, but likely still above, the proton (4.06). Honest current
assessment: the S³ nucleon mass-radius is ~1.3–2× too heavy and is **not** clearly
closed by any parameter-free effect computed so far; quantization may narrow but not
eliminate the gap. The gravity/cosmology spine remains unaffected throughout.

## Caveats
- Re-pin factor is a one-loop scalar-bubble proxy (the dominant structure for the
  leading coefficient); the full anisotropic a₂ tensor structure could shift the O(1)
  but not the conclusion that it is ~5% at tiny A3.
- Bilaplacian E_A3/E at A3≥1e-2 is a post-hoc estimate on the A3=0 profile (not
  self-consistently re-relaxed); fine for the "dead at 1e-6" conclusion, the only one
  that matters for the baryon.
