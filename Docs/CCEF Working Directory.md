# CCEF — Continuum-Coupled Emergent Framework
### Complete Theory Document · 15 June 2026 · Rev. 22 June 2026

> Revision note (22 June 2026). The emergent-gravity / Lifshitz-cosmology spine (§6–§10)
> is unchanged and SOLID. Four things changed in the matter sector: (1) the easy-axis
> potential is (A4/2)(1−n₃²), not (1−n·ê_z)²; (2) the written "(A2/2)(n·∇n)²" term is
> identically zero — the real 4th-order term is Faddeev/Skyrme; (3) the baryon is NOT an
> S² hedgehog (that map has Hopf number 0 and is invalid) — it is a Skyrmion of an
> S³=SU(2) order parameter; (4) the unit calibration is now derived: E₀·L₀ = ħc
> (coefficient 1), giving E₀ = 122.5 MeV. Fixed-point values A2*=8.971, A3*=1.684,
> A4*=0.542 and E₀=311.73 are superseded. Numbers in §9–§12 that depend on A3, A4 must be
> recomputed at the corrected parameters (flagged inline).

---

## Table of Contents
1. Overview and Philosophy
2. The Field
3. Action and Parameters
4. Dispersion Relation and Momentum Scales
5. Topological Structure — Baryons (Skyrmions) and Leptons
6. Emergent Metric and Spacetime
7. Riemann Tensor Check — Does CCEF Reduce to GR?
8. Lifshitz z=2 UV Structure
9. Gravitational Slip and Lensing — Falsifiable Departure from GR
10. Topological Susceptibility
11. Baryogenesis — Gap B
12. The θ_CCEF Result
13. Sakharov Conditions — Status
14. Bell Correlations — Gap 2 (Open)
15. Unit Conversions and Physical Scales
16. Master Results Table
17. Open Problems and Next Steps

---

## 1. Overview and Philosophy
CCEF is a classical field theory of an emergent order parameter. There is no external
spacetime — the metric, gravity, and low-energy structure emerge from correlations in the
field. The order parameter is a unit vector n ∈ S² in the gravity/cosmology sector; the
baryon (matter) sector requires its natural extension to φ ∈ S³ = SU(2) (§2, §5).

Working principle: The theory speaks for itself, right or wrong. If it fails, it fails.
No hand-fitting to produce convenient results. Every result is labelled SOLID (derived from
the action), CONJECT (motivated, derivation pending), or ANSATZ (assumed form).

---

## 2. The Field
    n(x,t) ∈ S²,   |n| = 1         (gravity/cosmology sector: 2 dof)
    φ(x,t) ∈ S³ = SU(2), |φ| = 1   (baryon sector: 3 dof; n is the projection)

- Spacetime geometry is emergent (§6); there is no a-priori metric.
- Baryons = topological solitons. On S² the Q=1 "hedgehog" is invalid (not a unit vector;
  Hopf number 0). The correct baryon is the degree-1 Skyrmion of S³, π₃(S³)=ℤ — the hedgehog
  ansatz becomes legitimate on S³ and carries the right quantum numbers (spin-½, isospin-½
  p/n doublet; fermionic by π₄(S³)=ℤ₂). [SOLID]
- Leptons = Q=0 surface/Goldstone modes (open; to be re-examined on S³).

---

## 3. Action and Parameters
Euclidean action (S³ form; the S² sector that carries gravity is the projection):

    S = ∫ d³x dt [ (Zt/2)(∂_t φ)²
                 + (A1/2)(∇φ)²
                 + (A2/4)|∂_i φ × ∂_j φ|²     (Faddeev/Skyrme — see note)
                 + (A3/2)(∇²φ)²               (Lifshitz bilaplacian — UV regulator)
                 + (A4/2)(1 − φ₃²) ]          (easy-axis potential)

Corrections [SOLID]: the easy-axis term is (A4/2)(1−n₃²)=(A4/2)sin²Θ — only this form gives
the IR mass Λ=√(A4/A1) used in calibration. The previously written (A2/2)(n·∇n)² is
identically zero for |n|=1; the genuine 4th-order O(3)/O(4) invariant is the Faddeev/Skyrme
term above.

Parameters (current best):

    A1   = 1.0        gradient coupling (sets units)             SOLID (axiom)
    Zt   = 1.0        temporal renormalisation                   SOLID (axiom)
    A4   = 3.5553     easy-axis / mass; proton-radius calib §15  SOLID (given calib)
    A3   ≈ 1×10⁻⁶     Lifshitz (∇²)² regulator; high UV crossover SOLID
    A2   ≈ 0.057      baryon stabiliser; one-loop induced         OPEN
    m_σ  = c·Λ, c<1   amplitude (radial) stiffness; core melting  CONJECT

  Superseded: A2*=8.971, A3*=1.684, A4*=0.542 (15-June fixed-point set) and the "self-dual"
  A3=A1²/A4=0.281 — the baryon requires the small-A3 regime.

---

## 4. Dispersion Relation and Momentum Scales
From quadratic fluctuations about the ordered vacuum (each S³ pion has the same form):

    ω_k² = (1/Zt)[ A4 + A1 k² + A3 k⁴ ]

    k_IR = Λ = √(A4/A1) = 1.886 CCEF⁻¹      IR mass gap (≈ 231 MeV)
    k_UV     = √(A1/A3) ≈ 10³ CCEF⁻¹        Lifshitz z=1→z=2 crossover (now far UV)

For k ≪ k_UV: ω ∝ k → z=1 (emergent Lorentz). For k ≫ k_UV: ω ∝ k² → z=2 (Lifshitz).
Because A3 is now small, the z=2 onset moves to high energy; the IR (hadronic/cosmological)
physics is firmly z=1.

---

## 5. Topological Structure — Baryons (Skyrmions) and Leptons

### 5.1 Baryon = S³ Skyrmion (Q=1)
Hedgehog φ = (cosF(r), sinF(r) r̂), F(0)=π, F(∞)=0, degree
B = (1/24π²)∫ ε_ijk Tr(L_i L_j L_k) = 1. Stabilised in the z=1 regime by the gradient (A1)
and Skyrme (A2) terms; the bilaplacian A3 is dynamically negligible at the soliton scale. [SOLID]

Baryon mass — the calibration-free test. The dimensionless product E_sol·R_sol = (mass×size)
is unit-independent; for the proton m_p·r_p/ħc = 4.06, and all hadrons lie in the band 0.5–6.
  - S² Hopf soliton: E·R = 79–1061 → falsified as a hadron. [SOLID]
  - S³ Skyrmion, frozen |φ|=1: E·R ≈ 9–13 → 2–3× too heavy. [SOLID]
  - S³ Skyrmion, dressed (core melting): the |φ|=1 constraint is a projection, not
    fundamental; the real defect lets the amplitude χ collapse in its core (χ→0.1 in a shell,
    degree preserved), relieving the gradient pile-up. This gives E·R ≈ 5 → ~1.25–1.4× the
    proton. [SOLID, quick]

The dressing magnitude is set by the amplitude stiffness m_σ = c·Λ. Integrating out the
established modes (Coleman–Weinberg) shows c < 1 (radiative softening below the naive 1);
a clean derivation of c is open.

### 5.2 Leptons (Q=0 surface modes)
Goldstone modes of the broken rotational symmetry — identified with leptons. [OPEN; re-examine on S³]

### 5.3 Topological charge and CP
Pontryagin term S_θ = −iθ Q[n], the CCEF analog of the QCD θ-term; θ is derived, not
inserted (§12). The gauge/instanton θ that controls baryon statistics and baryogenesis must
be recomputed at the corrected A3, A4.

---

## 6. Emergent Metric and Spacetime — SOLID (3 independent derivations)
No input metric; geometry emerges from field correlations via three convergent routes
(eikonal null-cone, geodesic deviation, Noether energy–momentum):

    ds² = −(A1/Zt) dt² + a²(t) δ_ij dxⁱdxʲ ,    c_eff = √(A1/Zt) = 1.000

Lorentz invariance is exact at IR scales (k ≪ k_UV), emergent rather than assumed.

### 6.2 Scale factor / Hubble
Homogeneous sector gives ρ_eff = (Zt/2)φ̇² + (A4/2)sin²φ; the overdamped attractor drives
φ→0, ρ_eff→A4/2. (Unchanged.)

---

## 7. Riemann Tensor Check — Does CCEF Reduce to GR? — SOLID (5.8×10⁻¹⁶)
Flat FRW (k=0): Γ⁰_ij = a ȧ δ_ij, Γⁱ_0j = H δⁱ_j. Einstein tensor G⁰₀ = 3H²,
Gⁱ_j = −(2ä/a + H²)δⁱ_j. Friedmann equations recovered from n(x,t):

    3H² = 8πG ρ_eff ,    2ä/a + H² = −8πG p_eff

Verified numerically to 5.8×10⁻¹⁶. CCEF is not "just GR": both sides derive from the field;
GR is emergent at background level and departs at the perturbation level (§9). (Unchanged.)

---

## 8. Lifshitz z=2 UV Structure — SOLID
- k ≪ k_UV: ω ∝ k → z=1 (emergent Lorentz). k ≫ k_UV: ω ∝ k² → z=2 (Lifshitz).
- Effective spacetime dimension d_eff = d + z = 3 + 2 = 5.
- The z=2 sector transforms differently under T → a structural source of CP violation.
With A3 ≈ 10⁻⁶ the crossover k_UV ≈ 10³ CCEF⁻¹ (≫ the 15-June value 0.77); the z=2
fingerprint is a high-energy prediction.

---

## 9. Gravitational Slip and Lensing — Falsifiable Departure from GR — SOLID (structure)

    η(k) = (A4 − A1 k² − A3 k⁴)/(A1 k² + A3 k⁴)

- η = 0 (sign change) at k* with A4 = A1k*² + A3k*⁴ → k* ≈ Λ = 1.886 CCEF⁻¹ (corrected
  from 0.586; falsifiable). Solitons sit in the η < 0 sector.
- Lensing ratio Σ(k) < 1 (suppression vs GR), testable with Euclid / LSST.
The η=0 location and Σ(k) shift under the corrected (A4=3.5553, A3≈10⁻⁶) parameters; the
qualitative falsifiable features (sign change, lensing suppression) survive. Recompute Σ.

---

## 10. Topological Susceptibility — SOLID (structure)

    χ_top = (1/2π²) ∫₀^∞ dk k⁴ G(k)² ,   G(k) = 1/(A3k⁴ + A1k² + A4)

Numerical value (15 June: 0.006174 CCEF³) must be recomputed at the corrected A3, A4.

---

## 11. Baryogenesis — Gap B
Mechanism: Lifshitz topological anomaly + KZM at the z=2→z=1 crossover (T_c). The required
asymmetry θ_required ≈ 2×10⁻⁹. At risk / recompute: the 15-June result used A3/A4 = 3.107;
the corrected parameters give a very different ratio, and in the emergent-gauge language
baryon violation is monopole-mediated with rate ∝ exp(−c√A3)·θ_CP. The Sakharov structure
(B-violation, CP, non-equilibrium) survives; the numbers do not carry over.

---

## 12. The θ_CCEF Result — RECOMPUTE
The 15-June formulas (θ_bary = 2.017×10⁻⁹, θ_CP = 4.08×10⁻¹¹) used A3/A4 = 3.107,
m_dp/k_UV = 0.0253 at the legacy parameters. These ratios change at A3 ≈ 10⁻⁶, A4 = 3.5553,
so both θ values must be re-derived. The hierarchy argument (two formulas differing by one
power of m_dp/k_UV) is structural and may survive; the magnitudes are not preserved. [OPEN]

---

## 13. Sakharov Conditions — Status
    1. B violation       topological (degree / Hopf), monopole-mediated   ✓ SOLID (structure)
    2. CP structural     Lifshitz T-mismatch at k_UV                       ✓ SOLID (structure)
    3. Non-equilibrium   KZM + z=2→z=1 at T_c                              ✓ SOLID
Magnitudes (2a/2b) pending the §12 recompute.

---

## 14. Bell Correlations — Gap 2 (Open)
Product-state result C(θ_A,θ_B) = −cos(Δ)/3 (structural 1/3 suppression). Target −cos(Δ).
Path: V_int pair-production vertex at k_UV → entangled phases → cos(Δ) recovered. The Hopf
sector gives a genuine Z₂ statistics structure (π₄(S²)=Z₂; π₄(S³)=Z₂ for the Skyrmion), so
the spin-singlet/fermion content is available. [OPEN]

---

## 15. Unit Conversions and Physical Scales — UPDATED
Two conditions fix the two units; the baryon mass is then a prediction:

    L₀ = r_p · √(A4/A1) = 1.610 fm/CCEF       (screening length 1/Λ = proton charge radius)
    E₀ · L₀ = ħc   (coefficient 1, DERIVED)   ⇒   E₀ = ħc/L₀ = 122.5 MeV/CCEF

Independent support: gap = √A4·E₀ = 231 MeV ≈ the quasinormal-resonance cluster 233–298 MeV.
Superseded: L₀ = 0.633 fm, E₀ = 311.73 MeV (and the earlier 30.6 MeV).

    Λ = k_IR              1.886 CCEF⁻¹    231 MeV (mass gap)
    m_p                   7.66 CCEF       938 MeV (calibration target)
    Baryon (S³, dressed)  E·R ≈ 5         mass+radius to ~25–30%

Known tension: the nucleon mass is reproduced to a factor ~1.25–1.4 (calibration-free),
pending the amplitude-stiffness derivation (§5, §17).

---

## 16. Master Results Table
    Emergent metric ds²        −(A1/Zt)dt²+a²δ        SOLID
    c_eff                      1.000                  SOLID
    G_μν = 8πG T_μν            to 5.8×10⁻¹⁶           SOLID
    Lifshitz z=2; d_eff        5                      SOLID
    η sign change              k* ≈ Λ = 1.886         SOLID (structure)
    Lensing Σ < 1              recompute              SOLID (structure)
    χ_top                      recompute              SOLID (structure)
    Calibration E₀·L₀          = ħc (coeff 1)         SOLID
    Baryon = S³ Skyrmion       spin-½, isospin-½      SOLID
    Baryon mass (dressed)      ~1.25–1.4 × m_p        SOLID (quick)
    θ_bary, θ_CP               recompute (A3/A4)      OPEN
    Bell C                     −cos(Δ)/3 → target     OPEN

---

## 17. Open Problems and Next Steps
1. Amplitude stiffness m_σ = c·Λ. Derive c from the one-loop amplitude effective potential
   with the full induced 4-derivative operator + a proper renormalization condition. (Toy CW
   shows only c<1.) Decisive for the exact nucleon mass.
2. Skyrme coupling A2. Confirm/replace the one-loop-induced value (mixed operator
   (2/3)S²+(1/3)TrT² with a log); B2 = 9/16π² was numerology.
3. Dressed Skyrmion with the true operator (not the pure-Skyrme proxy); then collective
   quantization → n–p splitting, Δ–N gap, g_A, magnetic moments.
4. Recompute §9–§12 numbers (Σ, χ_top, θ_bary, θ_CP) at the corrected A3, A4.
5. Lepton sector on S³; Bell Gap 2 via V_int.

Falsifiable predictions (recompute magnitudes; signs/structure stand):
    Gravitational-slip sign change at k* ≈ Λ    SOLID structure   ELT lensing
    Lensing suppression Σ < 1                   SOLID structure   Euclid, LSST
    Modified dispersion (z=2) above k_UV        SOLID             UHE cosmic rays
    Neutron EDM (θ_CP)                          recompute         nEDM@PSI, SNS

---
Rev. 22 June 2026 · Working principle: derive, label, do not fit.
