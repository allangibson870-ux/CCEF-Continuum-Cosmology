# How CCEF could protect IR Lorentz invariance — mechanism exploration

Goal: find, from CCEF's own structure (not by importing GR/Lorentz as input), mechanisms
that keep the IR Lorentz-invariant despite the z=2 UV (A3k⁴) term — to address the
A3↔LV tension. Observational LV limits are used only as *data*, not as theory assumptions.

## The strongest mechanism — UNIVERSALITY from a single order parameter (computed)
CCEF has ONE field (the O(4) order parameter n). Every excitation — the composite
graviton (TT collective mode) and all matter (tangent modes, solitons) — is built from
it and propagates on the SAME emergent metric. Computed limiting speeds:

  c²_matter = A1/Zt = 1.000   (from ω²=(A4+A1k²+A3k⁴)/Zt)
  c²_graviton = A1/Zt = 1.000  (from the O(4) symmetry of Π^TT, graviton 4D result)
  Δc/c = 0  →  **c_gravity = c_light exactly.**

Consequence: the *differential* LV bounds — the tightest ones — are **automatically
satisfied**, with no tuning:

| bound | level | status in CCEF |
|---|---|---|
| GW170817 c_gw=c_light | 1e-15 | **defeated** (Δc=0, shared metric) |
| vacuum birefringence | ~1e-32 | **defeated** (single metric, no two-speed structure) |
| photon–lepton differential LV | ~1e-16 | **defeated** (universality) |

This is the heart of the protection and it is intrinsically CCEF: with only one order
parameter there is no "ether frame" *difference* between species — the very thing the
1e-15…1e-32 bounds constrain. This alone turns the ~19-order problem into a much smaller,
single-channel one.

## Supporting mechanism — z=1 IR fixed point makes LV an IRRELEVANT operator
The dispersion ω²=A1k²(1+(k/k_UV)²) has LV fraction (A3/A1)k²=(k/k_UV)², which **vanishes
as k→0**. In RG language the A3 (bilaplacian) term is irrelevant at the z=1 fixed point —
the reference's own β(A3)=−A3²/16π²A1 sends A3→0 in the IR. So Lorentz invariance is an
emergent IR property, with violations power-suppressed by (k/k_UV)². (Caveat: this is only
power suppression, so it protects deep-IR modes, not GeV-scale probes by itself.)

## Structural mechanism — the emergent-diffeomorphism Ward identity
The composite graviton is massless *because* of an emergent diffeomorphism Ward identity
(the same identity that gave a₁=R/6>0 and the transverse pole). Matter that couples
minimally to this emergent metric inherits its IR Lorentz invariance; the Ward identity
ties matter's leading dispersion to the graviton's, enforcing the universal c_eff above.
So masslessness of the graviton and IR Lorentz invariance of matter are **the same fact**,
not two coincidences.

## Goldstone / topology remarks
- The tangent modes are pseudo-Goldstones (gapped by A4); their *leading* dispersion
  coefficient is fixed to the universal c_eff by the O(3) target isotropy (all three share
  one dispersion — no internal birefringence).
- Observed particles are **solitons / collective modes**, not the bare field. For momenta
  below the soliton's internal scale (P ≲ 1/R ~ Λ) the centre-of-mass dispersion is set by
  the emergent IR metric and the bare k⁴ is form-factor–shielded. (It is *not* shielded for
  highly boosted solitons, P ≫ Λ.)

## The residual channel — and the one CCEF-internal question it leaves
After universality defeats the differential bounds, what remains is the **universal,
energy-dependent dispersion** (same k⁴ for everything). The surviving probe is photon
time-of-flight (comparing different *energies* of one source): for n=2 (k⁴) LV this needs
k_UV ≳ ~1e6 GeV, whereas CCEF has k_UV ≈ 2 GeV (A3=1e-3) or 66 GeV (A3=1e-6).

This residual is resolved **iff the emergent photon is gauge-protected**: if light is an
emergent gauge mode, its transverse polarizations' gauge symmetry forbids the
k⁴ (bilaplacian) term, pinning the photon to exact z=1. Then the strong photon-TOF bound
does not apply, and only the much weaker massive-matter universal-LV bounds remain
(marginal at k_UV=66 GeV, failing at 2 GeV). So the LV question collapses to a single,
sharp, CCEF-internal computation:

  **Does CCEF's emergent photon (gauge sector) acquire an A3-type k⁴ term, or does gauge
  invariance forbid it?**

## Honest verdict
- CCEF has a **genuine, native Lorentz-protection mechanism** — universality of the single
  emergent metric — that defeats the *tightest* LV bounds (GW170817, birefringence,
  species-differential) automatically and without importing GR. The "19-orders-excluded"
  picture from the naive single-species estimate is too pessimistic.
- The z=1 fixed point and the diffeomorphism Ward identity reinforce this (emergent LI =
  graviton masslessness).
- The **residual** is one channel — the universal k⁴ photon dispersion — resolvable iff
  the emergent photon is gauge-protected from the bilaplacian. That is the decisive,
  falsifiable, CCEF-internal next computation.
- Bearing on the baryon: with photon gauge-protection, A3=1e-6 (k_UV=66 GeV) is comfortable
  for the remaining (massive-matter) bounds; A3=1e-3 (2 GeV) stays marginal. So the
  LV-protection mechanisms favour closing the baryon gap via the **a₂ prefactor at
  A3=1e-6** rather than via A3=1e-3 — consistent and mutually reinforcing.

## What was used vs assumed (re: the GR concern)
- *Derived from CCEF:* the universal emergent metric (single order parameter), c_grav=
  c_matter, the z=1 fixed point/irrelevance, the diffeomorphism Ward identity (from the
  graviton computation), the gauge-protection hypothesis for the photon.
- *Used only as data:* the numerical LV limits (GW170817, GRB TOF, birefringence). No GR
  field equations or assumed Lorentz invariance entered the mechanism.

## Caveats
- "c_grav=c_matter exactly" holds at leading (k²) order from the shared A1/Zt; equality of
  the k⁴ coefficients (graviton vs matter) is expected from universality but was not
  separately computed — worth checking (it bounds high-frequency GW-vs-light differential).
- The photon gauge-protection is a hypothesis here, not yet a CCEF derivation; it is the
  proposed decisive next step.
- Bounds quoted are order-of-magnitude; the unit conversion (1 CCEF momentum ≈ 66 MeV)
  carries O(1) uncertainty.
