# Anisotropic Lifshitz heat-kernel for the 4-derivative term + normalization/radius

Re-derive the induced Skyrme coefficient with the full anisotropic (z=2) operator,
check operator normalizations, and re-run the converged soliton. Couplings A1=1,
A4=3.5553, m²=A4, baryon-regime A3=1e-6.

## Part A — Anisotropic heat-kernel coefficient: NO O(1) shift
The induced 4-derivative coefficient is B2 = g · I, with
I = ∫dω d³k/(2π)⁴ /(ω²+A1k²+A3k⁴+m²)²  =  ∫₀^∞ ds·s·K(s)  (proper-time identity).
Because ∫ds·s·K(s) already contains the full anisotropic measure/prefactor, this single
integral *is* the whole Lifshitz correction. ω-integral done analytically:

| | value |
|---|---|
| I_z1 (relativistic, cutoff k_UV=1000) | 7.557e-2 |
| I_z2 (Lifshitz, A3=1e-6, UV-finite) | 7.168e-2 |
| **ratio z2/z1** | **0.949** |

So matching g to CC694B's z1 value 0.020 gives **B2_z2 = 0.019** — a 5% shift, not O(1).
The 2:1 (S²:TrT2) operator structure is a property of the S³ *target* geometry and is
unchanged by base-space anisotropy. **The anisotropic Lifshitz re-derivation does not
provide the hoped O(1) reduction.** (Confirms last session's corrected 0.95; the original
0.66 was a grid artifact.)

## Part B — The real O(1) levers: operator normalization AND radius convention
Well-converged frozen 2:1 soliton (virial→0, degree=1.000):

| B2 | E | R_energy | R_baryon | E·R_energy | E·R_baryon |
|---|---|---|---|---|---|
| 0.020 (CC694B) | 24.2 | 0.376 | 0.280 | 9.09 | **6.77** |
| 0.012 | 18.4 | 0.327 | 0.226 | 6.02 | **4.16** |
| 0.009 | 15.8 | 0.307 | 0.200 | 4.84 | 3.16 |

Two O(1) findings:

1. **Radius convention matters (~30%).** The proton's 4.06 = m_p·r_charge/ℏc uses the
   *charge* radius. The Skyrme analog is the **baryon-charge rms radius**, not the
   energy rms (which the docs used, giving the larger "E·R~9–13"). With the physically
   correct baryon radius, the nominal B2=0.02 soliton is **E·R_baryon = 6.8**, i.e.
   ~1.7× the proton — not ~2.3×.

2. **Operator normalization is the lever (CC694B's flagged a₂ ambiguity).** Reaching
   E·R≈4–6 needs effective B2 ≈ 0.011–0.012 (≈0.6× the 0.02 estimate). At B2=0.012 the
   **baryon-radius E·R = 4.16 ≈ proton**. Operator *structure* (2:1 vs 1:2 vs pure
   Skyrme) independently spreads E·R by ~30–50%. None of this is the anisotropy.

## Synthesis — honest, and slightly more hopeful than pure pessimism
- The Lifshitz anisotropy itself: ~5%, not the lever.
- Using the **physically correct charge (baryon) radius**, the frozen baryon is only
  ~**1.7×** too heavy at the nominal coefficient (E·R_b=6.8), not ~2–3×.
- An O(1) reduction of the induced coefficient to B2≈0.012 — within CC694B's own stated
  normalization uncertainty (the 2:1-vs-1:2 / overall-factor ambiguity) — gives
  **E·R_baryon ≈ 4.2 ≈ proton**, at the classical level.
- Quantization adds ~+9% (prior result), so it does not help and slightly hurts; the
  negative Casimir term (uncomputed) would need to offset it.

**Verdict.** The proton mass-radius is **not closed by the anisotropic re-derivation**
(that's a 5% effect), but it is **not excluded**: with the correct charge-radius
convention the gap is ~1.7×, and a factor-~1.7 first-principles fixing of the a₂
normalization (the genuine open computation flagged in CC694B) would close it at the
classical level. The decisive remaining task is to **pin the a₂ normalization from
first principles** (overall factor + 2:1-vs-1:2 mixing), not further anisotropy or
quantum corrections.

## Caveats
- Ratio 0.949 is analytic and robust; the absolute g (hence B2) carries the CC694B O(1)
  normalization uncertainty — which is exactly the point.
- E·R values are virial-converged (|vir|<0.02, degree=1.000); energy-rms vs baryon-rms
  differ by ~30% and both are reported.
- Quantization/Casimir as in `CCEF_S3_quantization_results.md` (rotational+breathing add
  ~9%; Casimir negative but uncomputed).
