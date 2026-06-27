# Reformulating the UV regulator: a Lorentz-invariant completion

Replace/augment the Lifshitz A3(∇²n)² with a Lorentz-invariant UV completion, and check
the four requirements (solitons, graviton, z=1 IR, baryon mass) and the LV problem.
Result: **the reformulation passes three-and-a-half of four requirements and fully cures
LV — but the baryon mass relocates the UV pathology rather than removing it.**

## Candidate A — covariant local (□n)²
Inverse propagator becomes A1p² + A3p⁴ + A4 with p²=−ω²+k² (Lorentz invariant).

**[1] Solitons / baryon — PRESERVED EXACTLY.** A static soliton has ∂_t n=0, so
□n=−∇²n ⇒ **(□n)² = (∇²n)² identically**. The soliton energy functional, E·R, matched
B2, virial are *unchanged*. The entire matter-mass analysis carries over verbatim.

**[2] Dispersion — LV CURED, but a GHOST appears.** The light pole gives ω²=k²+m_light²
(m_light≈1.886 CCEF) — **exactly relativistic, zero Lorentz violation at any k.** The
price is a second (Ostrogradsky/Lee-Wick) pole — a **ghost** — at m_ghost≈√(A1/A3)=k_UV
(2.1 GeV at A3=1e-3; 66 GeV at A3=1e-6).

**[3] Emergent metric + graviton — PRESERVED, improved.** The graviton's O(4) symmetry,
which was *emergent* (only below threshold) in the Lifshitz case, becomes **exact** with
the covariant propagator. Massless, healthy, z=1 graviton retained; the ghost acts as a
Pauli–Villars subtraction in the induction loop (M*² stays finite).

**[4] z=1 IR fixed point — EXACT** (whole theory Lorentz invariant; A3p⁴ is irrelevant).

## Candidate B — non-local ghost-free form factor (e.g. e^{□/M²})
Lorentz-invariant **and** ghost-free **and** UV-regulating (entire form factor, no new
poles). Solitons preserved (form factor ≈1 below M), graviton preserved, z=1 exact, no LV,
no ghost. The cleanest on paper.

## The catch — the baryon ties the pathology to ~GeV (computed)
The proton needs the induced-Skyrme coefficient B2≈0.012, which by the soliton-scale
matching means the **UV completion scale k_UV must sit just above the hadronic scale (~few
GeV)** — the induced Skyrme is a *log* of that scale. Then, whatever the completion:

| A3 (k_UV) | matched B2 | baryon E·R | completion pathology at k_UV |
|---|---|---|---|
| 1e-3 (2 GeV) | 0.014 | **4.6 ≈ proton** | LV (Lifshitz) / **2 GeV ghost** (covariant) — excluded |
| 4e-9 (1 TeV) | 0.051 | 16.5 | ghost at ~TeV (safe-ish) → baryon ~4× heavy |
| 1e-15 (2e6 GeV) | 0.097 | 30.8 | safe → baryon ~7× heavy |

**Root insight:** ANY UV completion placed at ~GeV produces new physics there — Lifshitz→
Lorentz violation, covariant→a light ghost, non-local→acausality at the non-locality
scale. **Reformulating the regulator relocates the pathology; it does not remove it,
because the baryon mass is tied to the UV scale through the induced-Skyrme log.** Curing LV
(candidate A) trades it for a ghost with the *same* A3 dependence — though the tension
softens (ghost bounds ~TeV are weaker than the photon-LV bound ~1e6 GeV, so the squeeze
goes from ~13 orders to ~5).

## The genuine escape — decouple the baryon from the UV scale
Add a **fundamental, tree-level, Lorentz-invariant Skyrme term** for S³ (coefficient
≈0.012), instead of relying on the induced (log) Skyrme. Then:
- the baryon mass is set by that tree coefficient, **independent of the UV scale**;
- the UV regulator (covariant or non-local) can sit at a **high scale** (ghost/LV/causality
  all safe);
- solitons, graviton, z=1 IR all still hold.

**Cost:** one free parameter — it gives up the "baryon mass fully derived/parameter-free"
ambition, but it makes the theory *consistent* (Lorentz-invariant, ghost-free, light
baryon) at the price of that single input. The alternative is to keep the induced baryon
and accept it as a **~4× near-miss** with a high-scale safe regulator.

## Verdict on the task
- A Lorentz-invariant UV completion **exists and works** for three of the four requirements
  outright (solitons exactly, graviton exactly-LI, z=1 exact) and **cures LV completely**.
- The fourth (parameter-free baryon mass) is the obstruction, and it is now understood at
  the root: the induced-Skyrme mechanism *requires* a ~GeV UV scale, which is where any
  completion misbehaves.
- The clean, consistent CCEF is therefore: **covariant (□n)² or non-local regulator at a
  high scale + a fundamental tree-level Skyrme coefficient.** This is Lorentz-invariant,
  ghost-free (non-local version), preserves gravity/cosmology, and reproduces the baryon —
  at the cost of one undetermined coupling.

## Closing synthesis of the whole investigation
- **Gravity/cosmology spine: solid and robust** — composite graviton (massless, healthy,
  z=1), emergent metric, intact slip/lensing, universality giving c_gw=c_light. Independent
  of all the matter-sector difficulties.
- **Matter sector: the nucleon mass-radius is the hard problem**, and it traces to ONE
  quantity — the induced-Skyrme coefficient / UV scale (A3). Through it the baryon mass,
  Lorentz violation (or ghost, or acausality), and the UV completion are all linked.
- **The cleanest consistent CCEF** keeps the spine, adopts a high-scale Lorentz-invariant
  (ideally non-local, ghost-free) UV completion, and pays one parameter (tree Skyrme) for
  the baryon — turning a multi-front tension into a single, honest free coupling.

## Caveats
- (□n)² ghost masses from the propagator roots; ghost-safety scale (~TeV) is an estimate.
- "Baryon needs k_UV~GeV" uses the soliton-matched B2 and converged E·R(B2).
- The non-local form factor's preservation of the graviton/soliton was argued structurally
  (form factor ≈1 below M), not separately recomputed.
- Adding a tree Skyrme is a model choice; its compatibility with CCEF's deeper axioms (is a
  fundamental 4-derivative S³ term allowed?) should be examined.
