# CCEF — S^2 -> S^3 Promotion, Phase 0 Setup
**2026-06-22. No hand-fitting.** Goal: lift the order parameter to S^3 (Skyrme baryon)
and PROVE the emergent-gravity spine is unaffected. Labels: [SOLID]/[CONJECT]/[OPEN].

================================================================================
## 1. The field
Promote n in S^2 (2 dof) to  phi = (phi0, phi1, phi2, phi3) in S^3,  |phi|^2 = 1  (3 dof),
equivalently U = phi0 + i phi_vec . sigma  in SU(2).
  - Baryon number = DEGREE, pi_3(S^3) = Z  (NOT the Hopf linking of S^2):
      B = (1/2pi^2) INT (1/12) eps^{abcd} eps^{ijk} phi_a d_i phi_b d_j phi_c d_k phi_d  d^3x
  - The hedgehog phi = (cos F(r), sin F(r) r_hat), F(0)=pi, F(inf)=0, has B=1.
    This is now a VALID, stable Skyrmion (the S^2 hedgehog was illegal; here it is correct).

## 2. The action (O(4) form) and the parameter map A -> B
S[phi] = INT d^3x dt [ (Zt/2)(d_t phi)^2
                     + (B1/2)|grad phi|^2                         (gradient; relevant)
                     + (B2/4)[ (d_i phi.d_i phi)(d_j phi.d_j phi) - (d_i phi.d_j phi)^2 ]  (Skyrme; irrelevant)
                     + (B3/2)(lap phi)^2                          (Lifshitz bilaplacian; marginal/runs)
                     + B4 (1 - phi0) ]                            (pion-mass potential; relevant)
Roles map one-to-one to the S^2 couplings:
  B1 <-> A1 (=1, axiom)   Zt (=1, axiom)
  B2 <-> A2  but now a GENUINE Skyrme term (the S^2 'A2' Faddeev term is its reduction)
  B3 <-> A3  (same bilaplacian / UV regulator role)
  B4 <-> A4  (sets the gap Lambda = sqrt(B4/B1) and the calibration)
Calibration structure is unchanged: L0 = r_p sqrt(B4/B1),  E0 = hbar c / L0.

## 3. *** GRAVITY SPINE PRESERVED *** [SOLID, verified symbolically]
Vacuum (potential B4(1-phi0) minimised): phi = (1,0,0,0), i.e. U = 1.
Fluctuations: phi = (sqrt(1-pi^2), pi1, pi2, pi3) -> THREE pion fields pi_a.
Quadratic expansion (sympy-verified):
  - |grad phi|^2  = |grad pi|^2 + O(pi^4)      (phi0 part is higher order)
  - (lap phi)^2   = (lap pi)^2  + O(pi^4)
  - B4(1-phi0)    = (B4/2) pi^2 + O(pi^4)       (mass^2 = B4 per pion)
=> quadratic action per pion:
     (Zt/2)(d_t pi)^2 + (B1/2)(grad pi)^2 + (B3/2)(lap pi)^2 + (B4/2) pi^2
=> DISPERSION (each of the 3 pions):
     omega^2 = (1/Zt)( B4 + B1 k^2 + B3 k^4 )
This is IDENTICAL IN FORM to the S^2 magnon dispersion omega^2=(1/Zt)(A4+A1k^2+A3k^4).
The Skyrme term B2 starts at quartic order in pi -> does NOT touch the quadratic spectrum.

Consequences (everything that defines the gravity spine derives from THIS dispersion):
  - Emergent metric  ds^2 = -(B1/Zt)dt^2 + a^2 delta_ij dx^i dx^j : UNCHANGED.
  - c_eff = sqrt(B1/Zt) = 1 : UNCHANGED.
  - Lifshitz z=2 UV / z=1 IR, d_eff = d+z = 5 : UNCHANGED.
  - Friedmann / Riemann (G_mu_nu = 8 pi G T_mu_nu to 5.8e-16): UNCHANGED in structure
    (a tensor identity; insensitive to the NUMBER of matter modes; G absorbs the
     mode-count factor).
  - Gravitational slip eta(k), lensing Sigma(k): same functional form H(k)=B4-B1k^2-B3k^4;
    numbers shift only through B4 vs A4 (recalibration), the falsifiable structure stays.

The ONLY spectral change: 3 light pion modes instead of 2 magnon modes.

## 4. What changes (matter sector) -- and why it is a FEATURE
The potential B4(1-phi0) breaks O(4) -> O(3). The unbroken O(3) ~= SU(2) is ISOSPIN:
  - the 3 pions form an isospin TRIPLET (pi^+, pi^0, pi^-) -- the physical pions;
  - the B=1 Skyrmion, collective-quantised, is an isospin-1/2, spin-1/2 NUCLEON DOUBLET
    (proton, neutron) -- exactly the multiplet structure S^2 could never provide.
  - Fermionic statistics are automatic: pi_4(S^3) = Z_2 -> odd-B Skyrmions are fermions
    (Finkelstein-Rubinstein / Witten). No sign ambiguity (unlike the S^2 case).
So the extra degree of freedom is the physical third pion + isospin; baryons coming in
isospin multiplets is independent evidence the target should be S^3.

## 5. RG / scaling dimensions (target-independent -> same as S^2) [SOLID]
[phi]=1/2 (bilaplacian marginal). [B1]=+2 relevant, [B4]=+4 relevant,
[B3]=0 marginal (runs), [B2]=-1 IRRELEVANT. Same structure as (A1,A4,A3,A2).
=> the Phase-3 RG risk recurs and is the same one: does the Skyrmion sit at a scale where
   the irrelevant Skyrme / marginal bilaplacian dominate? (Decided in Phase 1/3.)

## 6. Status & next
[SOLID] Gravity/cosmology spine is provably preserved under S^2 -> S^3 (dispersion identical,
        3 pions vs 2; isospin SO(3) and fermionic nucleon doublet emerge as bonuses).
[OPEN]  Whether the S^3 Skyrmion lands in the hadronic naturalness band (m*R/hbar c ~ O(1))
        -- the calibration-free GO/NO-GO -- is Phase 1 (the 1-D radial hedgehog ODE +
        the E_sol*R_sol test). Standard Skyrme content should give ~3-4 (in band); the
        risk is the Lifshitz B3 pushing it out, with the BPS-Skyrme limit as the fallback.

Phase 0 conclusion: the promotion is SAFE for gravity and STRUCTURALLY MOTIVATED by isospin.
Proceed to Phase 1 (calibration-free band test) when ready.
