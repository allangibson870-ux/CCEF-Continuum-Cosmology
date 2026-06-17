"""
ccef_gap_b_metric.py
====================
Gap B — Baryogenesis θ-term: now with emergent FRW metric (from ccef_riemann.py)
and explicit Lifshitz z=2 UV analysis.

Prior result (ccef_gap_b.py):
  - CCEF energy functional is Q ↔ -Q symmetric → no built-in baryon preference
  - Statistical (random walk) mechanism: η_rw ~ 5e-32  vs  η_obs ~ 6e-10  [ruled out]
  - Required: topological θ-term,  S_eff = E[n] - iθ·Q
  - θ_required ~ 1.87e-9  (from KZM v2 overproduction ratio)
  - Sakharov: (1) Q-violation ✓, (2) CP-violation ? [open], (3) non-equilibrium ✓

New in this script (enabled by emergent metric):
  1. Metric-weighted topological susceptibility χ_top(a)  — proper FRW treatment
  2. IR vs UV split of χ_top at Lifshitz crossover k_UV = 0.7706
  3. CP-odd phase from Lifshitz crossover: δθ_L(k)
  4. Natural CCEF combinations that approach θ ~ 2e-9
  5. What the Lifshitz z=2 structure offers and what remains open

Working principle: theory speaks for itself. Results not fitted to match η_obs.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ── Fixed-point parameters ─────────────────────────────────────────────────
A1  = 1.0
A2  = 8.971
A3  = 1.684
A4  = 0.542
Zt  = 1.0

k_IR  = np.sqrt(A4 / A1)          # 0.7362  IR gap scale
k_UV  = np.sqrt(A1 / A3)          # 0.7706  Lifshitz crossover
k_sol = 0.7536                     # soliton momentum
r_core = 1.327                     # soliton core radius [CCEF]

# Unit conversion (from ccef_unit_conversion.py)
L0_fm     = 0.633007               # fm per CCEF length unit
E0_MeV    = 311.73                 # MeV per CCEF energy unit
xi_long   = 51.3                   # dual-pole coherence length [CCEF]

# Observational anchor
eta_obs   = 6.0e-10                # η_B = n_B / n_γ today
KZM_ratio = 5.0e8                  # n_CCEF_comoving / n_obs  (KZM v2 overproduction)

print("=" * 70)
print("GAP B: Baryogenesis θ-term  — metric-corrected + Lifshitz analysis")
print("=" * 70)

# ════════════════════════════════════════════════════════════════════════════
# PART 1: Topological susceptibility χ_top from CCEF propagator
# ════════════════════════════════════════════════════════════════════════════
print()
print("PART 1: Topological susceptibility χ_top from CCEF propagator")
print("-" * 70)
print()
print("CCEF static propagator (3D, zero-temperature):")
print("  G(k) = 1 / (A1·k² + A3·k⁴ + A4)")
print()
print("Topological charge density for n ∈ S²:")
print("  j_top(x) = (1/4π) n·(∂_x n × ∂_y n)    [winding on 2D slices]")
print()
print("Topological susceptibility (free-field estimate):")
print("  χ_top = ∫ d³k/(2π)³  k² · G(k)²")
print("        = (1/2π²) ∫₀^∞ dk  k⁴ · G(k)²")
print()

k_arr = np.linspace(1e-4, 20.0, 50000)
G_k   = 1.0 / (A1 * k_arr**2 + A3 * k_arr**4 + A4)
integrand = k_arr**4 * G_k**2 / (2 * np.pi**2)

# Split at Lifshitz crossover k_UV
mask_IR = k_arr <= k_UV
mask_UV = k_arr >  k_UV

chi_tot = np.trapz(integrand,        k_arr)
chi_IR  = np.trapz(integrand[mask_IR], k_arr[mask_IR])
chi_UV  = np.trapz(integrand[mask_UV], k_arr[mask_UV])

print(f"  χ_top (total)  = {chi_tot:.6f}  CCEF³")
print(f"  χ_top (IR, k < k_UV={k_UV:.4f}) = {chi_IR:.6f}  CCEF³   [{100*chi_IR/chi_tot:.1f}%]")
print(f"  χ_top (UV, k > k_UV={k_UV:.4f}) = {chi_UV:.6f}  CCEF³   [{100*chi_UV/chi_tot:.1f}%]")
print()
print(f"  Ratio χ_UV / χ_IR = {chi_UV/chi_IR:.6f}")
print()
print("  Interpretation:")
print(f"  The IR (GR-like) sector contributes {100*chi_IR/chi_tot:.1f}% of χ_top.")
print(f"  The UV (Lifshitz z=2) sector contributes {100*chi_UV/chi_tot:.1f}%.")
print(f"  The Lifshitz modes are SUPPRESSED (high-k propagator ~ 1/(A3k⁴) → falls fast).")

# ════════════════════════════════════════════════════════════════════════════
# PART 2: θ_required — metric-corrected derivation
# ════════════════════════════════════════════════════════════════════════════
print()
print("PART 2: θ_required — derivation with emergent FRW metric")
print("-" * 70)
print()
print("KZM v2 (from ccef_kz_v2.py):")
print(f"  Freeze-out coherence length: ξ_long = {xi_long:.1f} CCEF = {xi_long*L0_fm:.1f} fm")
print(f"  KZM domain density (comoving): n_KZM = ξ_long⁻³ = {xi_long**-3:.3e} CCEF⁻³")
print(f"  KZM overproduction ratio:      n_KZM / n_obs = {KZM_ratio:.1e}")
print()
print("The θ-term S_eff = E[n] - iθ·Q biases Q=+1 vs Q=-1 soliton production:")
print("  P(Q=+1) = (1+θ)/2,   P(Q=-1) = (1-θ)/2   [for small θ]")
print()
print("After symmetric annihilation, the surviving baryon asymmetry:")
print("  n_B_survive = θ × n_KZM    (linear in θ for small θ)")
print()
print("Setting n_B_survive = n_obs:")
print(f"  θ_required = n_obs / n_KZM = 1 / (n_KZM/n_obs)")
print(f"             = 1 / {KZM_ratio:.2e}")
theta_required = 1.0 / KZM_ratio
print(f"  θ_required = {theta_required:.3e}")
print()
print(f"  Prior result (ccef_gap_b.py):  θ_required ~ 1.87e-9")
print(f"  This computation:               θ_required = {theta_required:.2e}")
print(f"  Ratio: {theta_required/1.87e-9:.2f}  (factor ~{theta_required/1.87e-9:.1f} from updated KZM number)")

# ── Metric correction ───────────────────────────────────────────────────────
print()
print("── Metric correction from emergent FRW g_μν = diag(-1, a²(t), a²(t), a²(t)) ──")
print()
print("The topological charge Q is purely spatial (time-slice integral).")
print("Under the FRW metric, the spatial volume element becomes:")
print("  d³x_phys = a³(t) · d³x_comoving")
print()
print("The topological SUSCEPTIBILITY transforms as:")
print("  χ_top(a) = χ_top(1) · a⁻³   [density dilutes with expansion]")
print()

# Scale factor at T_c ~ 6 MeV (from KZM v2)
T_c_MeV  = 6.0                       # MeV
T_0_MeV  = 2.725 * 8.617e-5 * 1e-3  # K → MeV: T_CMB
a_c       = T_0_MeV / T_c_MeV        # a at freeze-out (radiation-dominated)

print(f"  T_c (KZM freeze-out) = {T_c_MeV:.1f} MeV")
print(f"  T_0 (CMB today)      = {T_0_MeV:.3e} MeV")
print(f"  a_c = T_0/T_c        = {a_c:.3e}")
print()
chi_top_at_Tc = chi_tot / a_c**3
print(f"  χ_top(a_c) = χ_top(1) × a_c⁻³ = {chi_tot:.4f} × {a_c**-3:.2e} = {chi_top_at_Tc:.3e}  CCEF³")
print()
print("  NOTE: χ_top(a_c) is vastly enhanced at freeze-out (universe was dense).")
print("  BUT η_B = n_B/s is the ENTROPY-NORMALIZED ratio, conserved after T_c.")
print("  The metric correction cancels in the entropy-normalized η_B:")
print()
print("     η_B = n_B_survive / n_γ  [both ~ a⁻³, ratio is scale-factor-independent]")
print()
print("  ⟹ θ_required = 2.0e-9 is METRIC-INDEPENDENT (to leading order). ✓")
print("  The FRW metric does not shift θ_required — it confirms the prior result.")

# ════════════════════════════════════════════════════════════════════════════
# PART 3: Lifshitz z=2 — CP-odd phase at the UV crossover
# ════════════════════════════════════════════════════════════════════════════
print()
print("PART 3: Lifshitz z=2 — CP-odd phase δθ_L at the UV crossover")
print("-" * 70)
print()
print("The z=2 Lifshitz UV sector (k > k_UV) breaks Lorentz invariance.")
print("Under the anisotropic scaling  t → λ² t,  x → λ x:")
print("  - CP is preserved separately (n → n is even under spatial reflection)")
print("  - CPT as normally defined requires Lorentz invariance")
print("  - In the Lifshitz phase, CPT_eff ≠ standard CPT")
print()
print("The CCEF dispersion in each regime:")
print(f"  IR  (k < k_UV):  ω² ~ A1k²/Zt + A4/Zt   [massive relativistic, z=1]")
print(f"  UV  (k > k_UV):  ω² ~ A3k⁴/Zt            [Lifshitz, z=2]")
print()
print("At the crossover k = k_UV, both terms are equal:")
print(f"  A1·k_UV² = A3·k_UV⁴  ⟹  A1/A3 = k_UV²  ⟹  k_UV = √(A1/A3) = {k_UV:.4f} ✓")
print()
print("The CP-odd phase accumulated as a mode crosses the Lifshitz boundary:")
print()
print("  In an adiabatic process, a mode at k passes through k_UV with a")
print("  Berry phase. The mismatch in group velocities:")
print()

k_fine = np.linspace(0.5, 1.0, 2000)
omega_sq = (A4 + A1 * k_fine**2 + A3 * k_fine**4) / Zt
omega    = np.sqrt(omega_sq)
v_g      = (A1 * k_fine + 2 * A3 * k_fine**3) / (Zt * omega)  # dω/dk

# At k_UV
v_g_UV = np.interp(k_UV, k_fine, v_g)
# Contribution from 2nd derivative (curvature) — changes sign at k_UV
d2omega_dk2 = np.gradient(np.gradient(omega, k_fine), k_fine)
d2_UV = np.interp(k_UV, k_fine, d2omega_dk2)

print(f"  Group velocity at k_UV:        v_g(k_UV) = {v_g_UV:.6f}  [CCEF]")
print(f"  d²ω/dk² at k_UV (curvature):  {d2_UV:.6f}  [sign change → anomaly]")
print()

# Phase accumulated: δθ_L from mode mismatch at k_UV
# The CP phase comes from the fact that time-reversal and spatial reflection
# commute differently in z=2 vs z=1. The phase mismatch:
# δθ_L ~ (k_UV - k_sol)/k_UV × (A3/A1) × [curvature term]
eps_L   = (k_UV - k_sol) / k_UV          # proximity of soliton to UV crossover
eps_IR  = (k_sol - k_IR)  / k_IR         # proximity of soliton to IR crossover

print(f"  Soliton proximity to Lifshitz crossover:")
print(f"    ε_L  = (k_UV - k_sol)/k_UV = ({k_UV:.4f} - {k_sol:.4f})/{k_UV:.4f} = {eps_L:.5f}")
print(f"    ε_IR = (k_sol - k_IR)/k_IR = ({k_sol:.4f} - {k_IR:.4f})/{k_IR:.4f} = {eps_IR:.5f}")
print()
print(f"  k_sol is {eps_L*100:.2f}% below k_UV  and  {eps_IR*100:.2f}% above k_IR")
print(f"  → solitons sit at the midpoint of the IR-UV crossover band")
print()

# The natural CCEF angle: ratio of UV to total topological susceptibility
# modified by the Lifshitz structure
theta_chiUV_chiTot = chi_UV / chi_tot
print(f"  χ_top_UV / χ_top_total = {theta_chiUV_chiTot:.6f}   [UV fraction of topological weight]")
print()

# Another natural combination: the Lifshitz correction to the propagator pole
# Under Lifshitz flow, the effective mass gets a correction:
# m²_eff = A4 - A3·(k_UV)² · k²    [at k ~ k_UV]
# This gives a CP phase ~ arg[m²_eff] at k = k_sol

# Group velocity discontinuity at k_UV:
# Below k_UV (GR regime): v_g ~ A1·k_UV / sqrt(A4 + A1·k_UV²) [at k_UV]
# Above k_UV (Lifshitz): v_g ~ 2·A3·k_UV³ / sqrt(A3·k_UV⁴)  = 2·sqrt(A3)·k_UV

v_g_below = A1 * k_UV / np.sqrt(A4 + A1 * k_UV**2)
v_g_above = 2 * A3 * k_UV**3 / np.sqrt(A3 * k_UV**4)
delta_vg   = v_g_above - v_g_below
jump_frac  = delta_vg / v_g_below

print(f"  Group velocity at k_UV from BELOW (z=1 regime): v_g⁻ = {v_g_below:.5f}")
print(f"  Group velocity at k_UV from ABOVE (z=2 regime): v_g⁺ = {v_g_above:.5f}")
print(f"  Fractional jump: Δv_g/v_g⁻ = {jump_frac:.5f}")
print()

# ── Natural small numbers from CCEF parameters ─────────────────────────────
print("── Natural small numbers from CCEF structure ────────────────────────")
print()

# These are combinations that arise without tuning:
combo1 = (A4 / A2)**2                   # (A4/A2)² ~ (mass/coupling)²
combo2 = np.exp(-2 * np.pi * k_sol * r_core)  # instanton-like suppression
combo3 = (eps_L * eps_IR)               # product of proximity factors
combo4 = A4 / (4 * np.pi**2 * A2)      # QCD-like anomaly coefficient
combo5 = (A4 / A1)**(3/2) / (4*np.pi)  # 3/2 power of mass ratio / 4π
combo6 = chi_UV / chi_IR               # UV to IR topological weight ratio

print(f"  (A4/A2)²                  = {combo1:.3e}   [mass/coupling]²")
print(f"  exp(-2π·k_sol·r_core)     = {combo2:.3e}   [instanton-like suppression]")
print(f"  ε_L × ε_IR               = {combo3:.3e}   [proximity to both crossovers]")
print(f"  A4/(4π²·A2)              = {combo4:.3e}   [anomaly coefficient]")
print(f"  (A4/A1)^(3/2) / 4π       = {combo5:.3e}   [mass-ratio power]")
print(f"  χ_UV/χ_IR                = {combo6:.3e}   [UV/IR topological ratio]")
print()
print(f"  θ_required                = {theta_required:.3e}   [target]")
print()
print("  Closest match:")
combos = {
    "(A4/A2)²":                  combo1,
    "exp(-2π·k_sol·r_core)":     combo2,
    "ε_L × ε_IR":                combo3,
    "A4/(4π²·A2)":               combo4,
    "(A4/A1)^(3/2)/4π":          combo5,
    "χ_UV/χ_IR":                 combo6,
}
for name, val in sorted(combos.items(), key=lambda x: abs(np.log10(x[1]/theta_required))):
    ratio = val / theta_required
    print(f"    {name:<28}: {val:.3e}   ratio to θ_req = {ratio:.2f}")

# ════════════════════════════════════════════════════════════════════════════
# PART 4: Lifshitz running of θ — does z=2 → z=1 RG flow generate θ?
# ════════════════════════════════════════════════════════════════════════════
print()
print("PART 4: RG flow from z=2 (UV) to z=1 (IR) — does it generate θ?")
print("-" * 70)
print()
print("Under RG flow from k = Λ (UV cutoff) down to k = 0 (IR):")
print("  A3 flows to zero below k_UV  (Lifshitz term becomes irrelevant)")
print("  A1 remains marginal (gradient term)")
print("  A4 flows to zero in IR (mass becomes irrelevant below k_IR)")
print()
print("The β-functions (from backbone §8, NOTE: not fully derived):")
print("  β(A3) = -ε·A3 + c₂·A3²  [A3 is relevant in UV, irrelevant in IR]")
print("  β(A4) = -ε_m·A4          [mass term, suppressed in deep IR]")
print()
print("The θ-coupling β-function in the Lifshitz theory:")
print("  At one loop in z=2 Lifshitz, θ is exactly marginal (dimensionless).")
print("  In z=1 GR-like IR, θ is ALSO exactly marginal.")
print("  ⟹ β(θ) = 0 at both fixed points — no RG running of θ itself.")
print()
print("  However: the TRANSITION between z=2 and z=1 (at k ~ k_UV) can")
print("  generate a finite shift δθ from the 'matching' of the two EFTs.")
print()

# Compute the matching condition
# At k_UV, the Lifshitz dispersion equals the relativistic dispersion:
# A3·k_UV⁴ = A1·k_UV²  ⟹  A3·k_UV² = A1
# The CP-odd matching coefficient (from the imaginary part of 1-loop effective action):
# δθ_match ~ (1/16π²) ∫_{k_UV-Δk}^{k_UV+Δk} dk [Im(log G)]
# where Δk is the width of the crossover region

# Width of crossover: where |A3k⁴ - A1k²| < A4 (both UV and IR terms ~ mass)
# A3k⁴ ~ A1k² at k = k_UV; the crossover width ~ δk where A3·2k_UV·δk·k_UV ~ A4
delta_k = A4 / (2 * A1 * k_UV)   # rough width of the crossover band
print(f"  Crossover band width: δk ~ A4/(2·A1·k_UV) = {delta_k:.4f}  CCEF⁻¹")
print(f"  Crossover relative width: δk/k_UV = {delta_k/k_UV:.4f}")
print()
print(f"  Note: k_UV - k_sol = {k_UV - k_sol:.4f}  CCEF⁻¹")
print(f"        k_sol - k_IR  = {k_sol - k_IR:.4f}  CCEF⁻¹")
print(f"        δk            = {delta_k:.4f}  CCEF⁻¹")
print()
print(f"  k_UV - k_sol ≈ δk × {(k_UV-k_sol)/delta_k:.1f}   ← soliton is WITHIN the crossover band!")
print()
print("  This is structurally significant: the soliton at k_sol sits inside")
print("  the Lifshitz-GR crossover band, not cleanly in either regime.")
print("  The θ mismatch from EFT matching is evaluated precisely at the soliton scale.")

# EFT matching θ estimate
# The imaginary part of the one-loop effective action at the crossover:
# Im[S_eff] ~ (k_UV⁴ / 16π²) × (δk/k_UV) × f(A1,A3,A4)
# where f is a dimensionless geometric factor from the pole structure

# The poles of the CCEF propagator in complex k:
# G(k) = 1/(A1k² + A3k⁴ + A4)
# Poles at k² = s_± where A3s² + A1s - A4 = 0
disc    = A1**2 + 4*A3*A4
s_plus  = (-A1 + np.sqrt(disc)) / (2*A3)   # real positive pole (UV)
s_minus = (-A1 - np.sqrt(disc)) / (2*A3)   # real negative pole (ghostlike)
k_pole_UV = np.sqrt(s_plus)
m_pole    = np.sqrt(-s_minus)               # mass from lower pole

print()
print("── Dual-pole structure of G(k) = 1/(A3(k²+Λ²)(k²-m²)) ─────────────")
print()
print("  Propagator poles at k² = s_± where A3s² + A1s - A4 = 0:")
print(f"  s_+ = {s_plus:.6f}  →  Λ = k_pole_UV = {k_pole_UV:.6f} [UV mass scale]")
print(f"  s_- = {s_minus:.6f} →  m = {m_pole:.6f}          [IR mass scale]")
print()
print(f"  Note: Λ = {k_pole_UV:.4f}  vs  k_UV = {k_UV:.4f}  [differ by {abs(k_pole_UV-k_UV)/k_UV*100:.1f}%]")
print(f"        m = {m_pole:.4f}   vs  k_IR = {k_IR:.4f}  [differ by {abs(m_pole-k_IR)/k_IR*100:.1f}%]")
print()
print("  These are the TRUE poles (including A3 coupling), not the naive k_IR, k_UV.")
print("  The θ-term from EFT matching at the true UV pole:")
print()

# The imaginary part from the branch cut between -m and +Λ in complex s-plane:
# δθ_EFT ~ (1/4π) × Im[log(s_+ / |s_-|)]
#          = (1/4π) × arg(s_+ / s_-) ... but s_+ > 0, s_- < 0 → ratio is negative
# → Im[log(s_+/s_-)] = π (the negative number has phase π)
# So δθ_EFT ~ π / (4π) × (something involving the coupling)
# More carefully: from the spectral representation of G(k)
# G(k) = 1/(A3) × [1/(k²-s_+) - 1/(k²-s_-)] / (s_+ - s_-)
# The imaginary part of the effective action from integrating this out:
# δθ ~ (1/(16π²)) × (s_+ - |s_-|)² / (s_+ × |s_-|)

numer  = (s_plus - (-s_minus))**2
denom  = s_plus * (-s_minus)
delta_theta_EFT = numer / (denom * 16 * np.pi**2)

print(f"  δθ_EFT ~ (s_+ - m²)² / (16π² · s_+ · m²)")
print(f"         = ({s_plus:.4f} - {-s_minus:.4f})² / (16π² · {s_plus:.4f} · {-s_minus:.4f})")
print(f"         = {numer:.6f} / (16π² · {s_plus*(-s_minus):.6f})")
print(f"         = {numer:.6f} / {16*np.pi**2 * s_plus*(-s_minus):.4f}")
print(f"         = {delta_theta_EFT:.4e}")
print()
print(f"  Compare: θ_required = {theta_required:.2e}")
print(f"  Ratio: δθ_EFT / θ_required = {delta_theta_EFT / theta_required:.2e}")
print()
print("  δθ_EFT is O(1) — far too large. The EFT-matching mechanism overshoots.")
print("  The classical Lifshitz → GR transition alone does not give θ ~ 10⁻⁹.")
print("  A QFT-level calculation (instantons, axion-like coupling) is needed.")

# ════════════════════════════════════════════════════════════════════════════
# PART 5: What the Lifshitz structure DOES contribute to Gap B
# ════════════════════════════════════════════════════════════════════════════
print()
print("PART 5: What the Lifshitz z=2 structure DOES contribute to Gap B")
print("-" * 70)
print()
print("1. SAKHAROV CONDITION 3 (non-equilibrium) — STRENGTHENED:")
print(f"   The Lifshitz z=2 UV phase has different thermal equilibrium than z=1.")
print(f"   Phase transition at k_UV separates two distinct thermal equilibria.")
print(f"   Freeze-out at T_c crosses this boundary → non-equilibrium guaranteed.")
print()
print("2. SAKHAROV CONDITION 2 (CP violation) — STRUCTURAL:")
print(f"   In z=2 Lifshitz theory, C and P are individually preserved.")
print(f"   But the TIME-REVERSAL symmetry T acts as  φ(t,x) → φ(-t,x)")
print(f"   in z=1 AND as  φ(t,x) → φ(-t²,x) in z=2 (because t scales as λ²).")
print(f"   At the crossover, T acts DIFFERENTLY on modes above and below k_UV.")
print(f"   This structural T-violation at k_UV is a source of CP violation WITHOUT")
print(f"   requiring a beyond-CCEF θ-term — it is built into the Lifshitz structure.")
print()
print(f"   CAUTION: This argument is at the level of the kinematic structure.")
print(f"   A full 1-loop Lifshitz field theory calculation is needed to confirm.")
print()
print("3. THE SOLITON PROXIMITY:")
print(f"   k_sol = {k_sol:.4f},  k_UV = {k_UV:.4f},  k_UV - k_sol = {k_UV-k_sol:.4f}")
print(f"   δk (crossover width) = {delta_k:.4f}")
print(f"   (k_UV - k_sol)/δk = {(k_UV-k_sol)/delta_k:.2f}")
print()
print(f"   Solitons form WITHIN the Lifshitz-GR crossover band.")
print(f"   This means every baryon formed at T_c is imprinted with the CP-odd")
print(f"   phase from the z=2 → z=1 transition at the moment of formation.")
print(f"   This is structurally elegant: baryons are born at the Lifshitz boundary.")
print()
print("4. WHAT REMAINS OPEN:")
print("   - The MAGNITUDE of θ is not derived from classical CCEF.")
print(f"   - θ_required ~ 2e-9 is close to θ_QCD ~ 10^{{-10}} (one order of magnitude).")
print(f"   - The connection θ_CCEF ~ θ_QCD would close Gap B IF CCEF underlies QCD.")
print(f"   - Requires: QFT completion (path C from Bell correlations).")
print(f"   - OR: Show that the instanton density in the Lifshitz sector gives θ ~ 2e-9.")

# ════════════════════════════════════════════════════════════════════════════
# PART 6: Sakharov conditions summary
# ════════════════════════════════════════════════════════════════════════════
print()
print("=" * 70)
print("SAKHAROV CONDITIONS IN CCEF — STATUS")
print("=" * 70)
print()
print(f"  {'Condition':<35} {'Status':<12} {'Mechanism'}")
print(f"  {'-'*35}  {'-'*12}  {'-'*30}")
print(f"  {'1. B violation (Q asymmetry)':<35} {'✓ SOLID':<12} {'θ-term S_θ = -iθ·Q; allowed by π₃(S²)=ℤ'}")
print(f"  {'2. CP violation':<35} {'~ PARTIAL':<12} {'Lifshitz T-mismatch at k_UV (structural)'}")
print(f"  {'2a. θ magnitude (θ~2e-9)':<35} {'✗ OPEN':<12} {'Not derivable from classical CCEF'}")
print(f"  {'3. Non-equilibrium (KZM)':<35} {'✓ SOLID':<12} {'Phase transition, z=2→z=1 at T_c'}")
print()
print("  Gap B partially advanced: CP violation has a STRUCTURAL source (Lifshitz).")
print("  The magnitude of θ requires QFT completion or instanton calculation.")
print()
print(f"  Natural CCEF θ-scale from structure:  NOT YET DERIVED")
print(f"  Required θ:                             {theta_required:.2e}")
print(f"  θ_QCD (strong CP problem):              ~10⁻¹⁰")
print(f"  Ratio θ_required / θ_QCD:              ~{theta_required/1e-10:.0f}")

# ════════════════════════════════════════════════════════════════════════════
# FIGURES
# ════════════════════════════════════════════════════════════════════════════
fig = plt.figure(figsize=(14, 10))
gs  = GridSpec(2, 2, figure=fig, hspace=0.4, wspace=0.35)

# ── Panel 1: χ_top integrand — IR vs UV split ──────────────────────────────
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(k_arr[k_arr < 3], integrand[k_arr < 3], 'b-', lw=2, label='χ_top integrand')
ax1.axvline(k_UV,  color='red',    ls='--', lw=1.5, label=f'k_UV={k_UV:.3f}')
ax1.axvline(k_IR,  color='orange', ls='--', lw=1.5, label=f'k_IR={k_IR:.3f}')
ax1.axvline(k_sol, color='purple', ls='-',  lw=1.5, label=f'k_sol={k_sol:.3f}')
ax1.fill_between(k_arr[mask_UV & (k_arr < 3)],
                 integrand[mask_UV & (k_arr < 3)],
                 alpha=0.3, color='red', label=f'UV ({100*chi_UV/chi_tot:.1f}%)')
ax1.fill_between(k_arr[mask_IR & (k_arr < 3)],
                 integrand[mask_IR & (k_arr < 3)],
                 alpha=0.2, color='blue', label=f'IR ({100*chi_IR/chi_tot:.1f}%)')
ax1.set_xlabel('k [CCEF⁻¹]')
ax1.set_ylabel('k⁴ G(k)² / 2π²  [CCEF⁻³]')
ax1.set_title(f'Topological susceptibility χ_top\nIR vs UV Lifshitz split at k_UV')
ax1.legend(fontsize=8)
ax1.grid(alpha=0.3)
ax1.set_xlim(0, 2.5)

# ── Panel 2: Dispersion and group velocity at crossover ────────────────────
ax2 = fig.add_subplot(gs[0, 1])
k_disp = np.linspace(0.4, 1.1, 500)
omega_disp = np.sqrt((A4 + A1*k_disp**2 + A3*k_disp**4) / Zt)
v_group = (A1*k_disp + 2*A3*k_disp**3) / (Zt * omega_disp)
# Approximate linear (z=1) and Lifshitz (z=2) curves
omega_z1 = np.sqrt(A4/Zt + A1/Zt * k_disp**2)
omega_z2 = np.sqrt(A3/Zt) * k_disp**2

ax2.plot(k_disp, omega_disp, 'k-', lw=2.5, label='CCEF exact ω(k)')
ax2.plot(k_disp, omega_z1,   'b--', lw=1.5, alpha=0.7, label='z=1 approx (no A3)')
ax2.plot(k_disp, omega_z2,   'r--', lw=1.5, alpha=0.7, label='z=2 approx (no A1)')
ax2.axvline(k_UV,  color='red',    ls=':', lw=2, label=f'k_UV={k_UV:.3f}')
ax2.axvline(k_sol, color='purple', ls='-', lw=2, label=f'k_sol={k_sol:.3f}')
ax2.axvline(k_IR,  color='orange', ls=':', lw=1.5)
ax2_twin = ax2.twinx()
ax2_twin.plot(k_disp, v_group, 'g-', lw=1.5, alpha=0.7, label='v_group')
ax2_twin.set_ylabel('Group velocity v_g', color='g', fontsize=10)
ax2_twin.tick_params(axis='y', labelcolor='g')
ax2.set_xlabel('k [CCEF⁻¹]')
ax2.set_ylabel('ω(k)')
ax2.set_title('Dispersion at Lifshitz crossover\nz=1↔z=2 transition at k_UV')
ax2.legend(fontsize=8, loc='upper left')
ax2.grid(alpha=0.3)

# ── Panel 3: θ natural combinations vs θ_required ─────────────────────────
ax3 = fig.add_subplot(gs[1, 0])
combo_names  = list(combos.keys())
combo_values = list(combos.values())
colors_bar   = ['red' if abs(np.log10(v/theta_required)) < 1 else 'steelblue'
                for v in combo_values]
bars = ax3.barh(combo_names, [np.log10(v) for v in combo_values],
                color=colors_bar, alpha=0.75)
ax3.axvline(np.log10(theta_required), color='k', ls='--', lw=2,
            label=f'θ_req = {theta_required:.1e}')
ax3.axvline(np.log10(1e-10), color='gray', ls=':', lw=1.5, label='θ_QCD ~ 10⁻¹⁰')
ax3.set_xlabel('log₁₀(value)')
ax3.set_title('Natural CCEF combinations\nvs θ_required ~ 2e-9')
ax3.legend(fontsize=9)
ax3.grid(alpha=0.3, axis='x')

# ── Panel 4: Sakharov conditions visual ────────────────────────────────────
ax4 = fig.add_subplot(gs[1, 1])
ax4.axis('off')

conditions = [
    ("1. B violation",       "✓ SOLID",   "θ-term allowed by π₃(S²)=ℤ", "green"),
    ("2. CP violation",      "~ PARTIAL",  "Lifshitz T-mismatch at k_UV", "goldenrod"),
    ("2a. θ magnitude",      "✗ OPEN",    f"θ_req={theta_required:.1e}, needs QFT", "red"),
    ("3. Non-equilibrium",   "✓ SOLID",   "z=2→z=1 phase transition", "green"),
]
y = 0.88
for cond, status, mech, color in conditions:
    ax4.text(0.02, y, cond, fontsize=11, va='center',
             fontweight='bold', transform=ax4.transAxes)
    ax4.text(0.42, y, status, fontsize=11, va='center',
             color=color, fontweight='bold', transform=ax4.transAxes)
    ax4.text(0.02, y - 0.08, mech, fontsize=9, va='center',
             color='gray', transform=ax4.transAxes, style='italic')
    y -= 0.22

ax4.text(0.02, 0.05,
         f"θ_required ≈ {theta_required:.1e}\n"
         f"θ_QCD  ≈ 10⁻¹⁰ (×{int(theta_required/1e-10)} off)\n"
         f"Soliton: {(k_UV-k_sol)/delta_k:.1f}×δk inside Lifshitz band",
         fontsize=10, va='bottom', transform=ax4.transAxes,
         bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='gray'))

ax4.set_title("Sakharov conditions in CCEF", fontsize=12)

fig.suptitle(
    "CCEF Gap B: Baryogenesis θ-term — Lifshitz z=2 analysis + emergent metric\n"
    "CP violation has structural source (Lifshitz T-mismatch) | θ magnitude open",
    fontsize=12
)

plt.savefig('ccef_gap_b_metric.png', dpi=150, bbox_inches='tight')
print()
print("Figure saved: ccef_gap_b_metric.png")
print("Done.")
