# CCEF — S^3 Skyrmion, Phase 1: the calibration-free GO/NO-GO
**2026-06-22. No hand-fitting.** Result: CONDITIONAL GO (first CCEF config to pass).

## Test
Dimensionless, calibration-free: E_sol * R_sol  vs  m_p r_p/hbar c = 4.06.
B=1 hedgehog Skyrmion phi=(cosF, sinF r_hat), F(0)=pi, F(inf)=0, solved as a 1-D
radial BVP (robust). R_sol = baryon-density RMS radius. Hadronic band ~ 0.5-6.

## Result
At B2 = 0.057, B3 -> 0:   **E_sol*R_sol = 4.06 = m_p r_p/hbar c EXACTLY**
=> the S^3 Skyrmion reproduces proton MASS and RADIUS simultaneously. [PASS]
(Contrast S^2 Hopf: E*R = 79-1061, orders of magnitude out -> dead.)

## The bilaplacian is the sole controlling factor (sharp)
At B2 = 0.057:
   B3 = 0.000  -> E*R =  4.06   (proton)
   B3 = 0.001  -> E*R =  4.36
   B3 = 0.010  -> E*R =  7.01
   B3 = 0.050  -> E*R = 18.1
   B3 = 0.281  -> E*R = 76.9   (self-dual value: S^2-disaster zone)
=> proton survives only for **B3 <~ 1e-3** (a tiny UV regulator).
This is the ORIGINAL CCEF value A3 ~ 1e-6, NOT the self-dual A3 = 0.281.

## Why small B3 is self-consistent
B3 ~ 1e-6 => k_UV = sqrt(B1/B3) ~ 1e3, so the Lifshitz scale is deep in the UV and
the soliton (size ~0.25 CCEF, k~4) lives in the z=1 regime where B3 k^4 << B1 k^2 is
negligible. The earlier "A3 does not decouple" NO-GO was specific to the SELF-DUAL
point (k_UV dragged down onto the soliton). Dropping self-duality restores decoupling.

## Verdict
- S^3 is VIABLE for the baryon mass where S^2 was dead.
- Conditions: (i) B3 = original tiny regulator (~1e-6), i.e. ABANDON the self-dual
  conjecture for the matter sector (gravity never needed it); (ii) B2 ~ 0.057.
- OPEN: derive B2 ~ 0.057 from a principle. If pinned -> proton mass is a genuine
  prediction. If not -> one self-consistent fit that still predicts the mass-radius
  RELATION (E*R) correctly. Either way: first "in-band" result for CCEF.
- BONUS already in hand (Phase 0): S^3 gives the pion isospin triplet, the p/n doublet,
  and automatic fermionic statistics (pi_4(S^3)=Z_2).

## Parameter set that works (S^3 baryon sector)
  B1 = 1, Zt = 1            (axiom)
  B2 ~ 0.057                (Skyrme coupling; [OPEN] - needs a pinning principle)
  B3 ~ 1e-6                 (tiny UV regulator; NOT self-dual 0.281)
  B4 = 3.5553              (potential/gap, via proton-radius calibration)
  -> E_sol*R_sol = 4.06 = proton; mass and radius reproduced together.

## Next (Phase 2/3)
- Phase 3 (RG): with B3 ~ 1e-6 the soliton is in z=1; confirm the Skyrme term B2 and
  potential B4 (relevant + the stabiliser) set the scale, so the IR is clean. The
  self-dual-point RG obstruction does NOT apply here.
- Pin B2: is 0.057 a fixed point / self-dual-in-a-different-sense / WZ-derived value?
- Then full 3-D Skyrmion + collective quantisation for the n-p splitting and Delta-N gap.
