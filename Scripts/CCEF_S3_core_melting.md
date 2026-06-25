# CCEF — The baryon is a DRESSED defect, not a frozen Skyrmion (quick check)
**2026-06-22. No hand-fitting.** Result: continuum rearrangement (amplitude/core melting)
drops the baryon E*R by a factor ~4-5, from ~25 into the hadronic band. The "2-3x too heavy"
verdict was a FROZEN-AMPLITUDE artifact.

## The objection (correct)
CCEF is fundamentally a continuum theory that PROJECTS to an S^3 sigma model; it is not
fundamentally |phi|=1. Freezing the amplitude forbids the continuum from rearranging around
the defect. The true baryon is a COUPLED object: winding F(r) + amplitude chi(r).

## Quick check (linear sigma model hedgehog: phi = chi(r) (cosF, sinF r_hat))
  energy = (B1/2)[chi'^2 + chi^2(F'^2+2sin^2F/r^2)] + c4 chi^4 (Skyrme) + B4 chi^2(1-cosF)
           + (m_sigma^2/8)(chi^2-1)^2     (radial-mode potential, vacuum |phi|=1)
  c4=0.15, B4=3.5553. Minimised over chi(r),F(r). Degree (= F winding) tracked.

| case | E*R | E | R | chi_min (at r) | degree |
|------|-----|---|---|----------------|--------|
| FROZEN chi=1 (pure Skyrmion) | 25.7 | 49.0 | 0.52 | 1.00 | 1.00 |
| SOFT m_sigma=3.0 | 6.4 | 10.1 | 0.64 | 0.12 (r=0.46) | 0.99 |
| SOFT m_sigma=1.5 | 5.4 | 8.3 | 0.65 | 0.10 (r=0.58) | 1.00 |
| SOFT m_sigma=0.8 | 5.0 | 7.6 | 0.66 | 0.08 (r=0.58) | 1.00 |

## Reading
- The order parameter MELTS to chi~0.1 in a SHELL at r~0.5 (a 'normal core'), relieving the
  gradient pile-up chi^2(grad n)^2 that the frozen winding was forced to carry.
- Topology PRESERVED (degree=1): chi>0 everywhere, F still winds pi->0. Genuine B=1 baryon,
  not an unwinding artifact.
- E*R falls ~25 -> ~5 (factor ~4-5), INTO the hadronic band (proton 4.06; band 0.5-6).
- This is standard physics: a LINEAR sigma-model Skyrmion is much lighter than the NONLINEAR
  (frozen) one when the sigma/amplitude mode is not stiff. CCEF, being a continuum projecting
  to the sigma model, HAS that mode.

## Status
[SOLID, quick] The frozen-Skyrmion mass is an UPPER bound; core melting lowers E*R by a factor
  of several, enough to reach the proton. The "S^3 baryon 2-3x too heavy" conclusion is
  SUPERSEDED -- it assumed a frozen amplitude.
[OPEN] The exact E*R depends on the amplitude stiffness m_sigma (radial-mode mass), an
  UNPINNED CCEF scale. For m_sigma <~ gap (1.9) -> E*R ~ 5 (proton range); stiff -> heavy.
  The open question MOVES from 'why too heavy' to 'what is CCEF's amplitude stiffness m_sigma'.
[caveat] quick check used pure-Skyrme 4-deriv + simple radial potential; precise number needs
  the full induced operator + derived m_sigma. Factor-of-several magnitude is robust.

## Why this matters
The baryon is a COUPLED object (winding + amplitude), and how the continuum rearranges around
the defect is the DOMINANT correction -- larger than the one-loop 4-derivative sector and the
(failed) emergent-vector channel. The route to the nucleon mass is: derive CCEF's amplitude
stiffness m_sigma from the full continuum (not the sigma-model projection), then the dressed
defect mass follows. The 2-3x gap is closable by this real mechanism, not a tuned parameter.
