# Primordial ripples in the grain universe (no inflation) (2026-10-12)

**Code:** `ccef_ripples.py` → `ccef_ripples_output.txt` (order-of-magnitude estimates). This is CCEF's biggest open hole (`CCEF_V5_Grain_Universe.md` §13).

**Targets** (Planck and others):
- A_s = 2.1×10⁻⁹;
- n_s = 0.965 ± 0.004;
- running ≈ 0;
- Gaussian (f_NL ≈ 0 ± 5);
- statistically isotropic;
- **super-horizon and phase-coherent** (the acoustic peaks);
- r < 0.036.

**Prior art this builds on:**
- string-gas cosmology (Brandenberger & Vafa 1989; Nayeri, Brandenberger & Vafa 2006): thermal fluctuations with an area-scaling heat capacity give a scale-invariant spectrum;
- holographic fluctuations (Magueijo, Smolin & Contaldi 2007);
- critical-geometry Big Bang (Afshordi & Magueijo 2016);
- disordered locality (Markopoulou & Smolin 2007; Prescod-Weinstein & Smolin 2009).

## Candidates
| Mechanism | Shape | Amplitude | Other | Verdict |
|---|---|---|---|---|
| **M1** Poisson noise in the grain count | Δ² ∝ k³ (white noise, "n_s = 4") | ~10⁻⁹⁰ on cosmic scales | — | ❌ |
| **M2** Area-law thermal fluctuations, frozen when non-local grain links disappear | **scale-invariant automatically**: Φ² = c (T_f/M)²/(16η²), independent of scale | right if **T_f ≈ 2.6×10¹⁴ GeV/√c** | Gaussian (many grains); tilt needs extra physics | ⚠️ **partial** |
| **M3** Roughness of the crystallisation front (ζ = H·δt) | Edwards–Wilkinson front: scale-invariant (log-rough). Generic KPZ front: n_s − 1 ≈ −0.8 | ~1 unless the front is smoother than ~5×10⁻⁵ Planck times per scale | a single propagating front makes cosmic modes ~10⁶⁰× longer than wide (extreme anisotropy); KPZ is non-Gaussian | ❌ |

## The surviving idea (M2), in CCEF terms [COND]
1. **Super-horizon coherence.**
   - Before and during crystallisation, the grain tangle is non-local: every grain is a few links from every other. Thermal correlations can span what will later be vastly super-horizon scales; this is CCEF's answer to the horizon problem.
   - For M2, some **residual non-local links must persist after crystallisation** ("disordered locality") until a freeze-out temperature T_f. **[ASSUMED]**
2. **Why scale-invariant:**
   - Gravity in CCEF comes from an **entanglement area law**. If the heat capacity of a region likewise scales with its *area*, its energy fluctuates by δM ∝ R, its gravitational potential Φ = GδM/R is the same on every scale, and the spectrum is flat.
   - Here the same law that gives gravity gives the shape of the ripples (the string-gas logic, with grains).
3. **Amplitude:**
   - Δ²_Φ = 4.39·c·(T_f/M)², with η = N_eff/24π, N_eff = 9.
   - Matching A_s needs T_f ≈ 2.6×10¹⁴ GeV for c = 1; 8×10¹⁴ for c = 0.1; 2.6×10¹⁵ for c = 0.01.

| If the ripples froze at | A_s (× c) | |
|---|---|---|
| crystallisation (T_RH ~ 0.5 M) | ~2 | far too big |
| **Branch L₃ switch-on** (Λ* ≈ 8×10¹⁰ GeV) | ~2×10⁻¹⁶ | far too small |
| **Branch M switch-on** (Λ* ≥ 4×10¹⁵ GeV) | ≥ 5×10⁻⁷ | right for c ≈ 0.004–0.01 |

4. **Tilt:** not derived. Exact flatness is excluded (8σ), so larger scales must freeze slightly hotter.
   - **Example form (assumed, not derived):** T_f ∝ [ln(R/ℓ)]^q gives n_s − 1 = −2q/ln(R/ℓ) ≈ −0.036 for q = 2.5, with running ≈ −3×10⁻⁴ (allowed).
   - This mirrors inflation's n_s − 1 ≈ −2/N, with the log of the scale ratio in place of the number of e-folds.
5. **Tensors:** thermal area-law mechanisms predict a slightly **blue** gravitational-wave tilt (n_t > 0), unlike inflation's red tilt. That would be a sharp test if r is ever measured.

## The tension this exposes
- **If the ripples come from M2 frozen at the matter switch-on, they point to Branch M, not L₃.**
  - **Branch M (proton decay possible):** Λ* ≈ 4×10¹⁵ GeV with c ≈ 0.004 gives the right A_s *and* puts proton decay right at Hyper-Kamiokande's reach. But then the L₃ package (Dirac neutrinos via dilution, the 74 μeV axion at f_a ≈ Λ*, no 0νββ) does not hold. A post-inflation axion at f_a ≈ 4×10¹⁵ would vastly overproduce dark matter, so dark matter would need another source.
  - **Branch L₃:** keeps its package but needs a separate freeze-out scale near 10¹⁴–10¹⁵ GeV that nothing in the framework provides.
- So the two most data-relevant open problems, **primordial ripples** and **matter/antimatter**, both lean toward **Branch M**, while neutrinos, the axion and proton stability lean toward L₃. **The fork is now the central question.**

## Verdict
- **CCEF can produce the *shape* of the primordial ripples without inflation**, using its own ingredients: pre-geometric non-locality for super-horizon coherence, and the entanglement area law for scale invariance. This is essentially the string-gas mechanism transplanted onto grains.
- It does **not yet derive the tilt.** The amplitude **fixes a freeze-out scale** (~10¹⁴–10¹⁵ GeV) that matches Branch M's crossover, not L₃'s.
- **New requirements:**
  - residual non-local links until freeze-out [assumed];
  - a mechanism for the slow scale-dependence of the freeze-out temperature [open].
- **Distinctive predictions, if this is the route:**
  - no inflationary tensor signal (r small), with any tensors **blue-tilted**;
  - proton decay near Hyper-K's reach (Branch M);
  - Gaussian, adiabatic perturbations.
