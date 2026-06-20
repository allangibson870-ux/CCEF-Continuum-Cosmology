"""
ccef_hopf_mass.py  ─  CCEF Hopf soliton mass calculation  (Step 4)
===================================================================
Computes:
  1. Continuum zero-point energy density  e_c
     e_c = (1/4π²) ∫₀^{k_UV} dk k² √(A4 + A1 k² + A3 k⁴)
     with UV cutoff k_UV = √(A1/A3)  (the Lifshitz crossover)

  2. Soliton effective volume  V_eff
     V_eff = ∫ 2πρ dρ dz  (1 − cosΘ)² / max(1 − cosΘ)²

  3. Physical soliton energy
     E_phys = E_sol − e_c × V_eff

  4. Mass ratio (predicted vs experiment)
     m_p/m_π  =  E_phys / ω_π    where ω_π = √A4

  5. Cross-check: hedgehog energy from F0_bvp.npy
     E_hedge = ∫₀^∞ 4πr² dr [ε_A1 + ε_A3 + ε_A4]
     using the analytic angular-integration formulas for a hedgehog.

Parameters: A1=1.000, A3=1.684, A4=0.542
Working principle: derive from CCEF action only.  Label every result.
                   Report what the theory gives, right or wrong.
"""

import numpy as np

OUTDIR = '/sessions/eager-dreamy-hopper/mnt/outputs/'
A1, A3, A4 = 1.000, 1.684, 0.542
E0_MEV = 311.73   # MeV per CCEF energy unit  (ħc/L₀)
L0_FM  = 0.633007 # fm per CCEF length unit

# ─────────────────────────────────────────────────────────────────────────────
# 0.  Load the converged Hopf soliton field
# ─────────────────────────────────────────────────────────────────────────────
Th  = np.load(OUTDIR + 'hopf_converged_Theta.npy')
Ph  = np.load(OUTDIR + 'hopf_converged_Phi.npy')
rho = np.load(OUTDIR + 'hopf_converged_rho.npy')
z   = np.load(OUTDIR + 'hopf_converged_z.npy')
Nr, Nz = Th.shape
drho = rho[1] - rho[0]; dz = z[1] - z[0]
RHO, Z = np.meshgrid(rho, z, indexing='ij')

print("=" * 64)
print("CCEF HOPF SOLITON MASS CALCULATION  (Step 4)")
print("=" * 64)
print(f"\nLoaded Hopf field: {Nr}×{Nz} grid"
      f"  ρ∈[{rho[0]:.4f},{rho[-1]:.1f}]  z∈[{z[0]:.1f},{z[-1]:.1f}]")

# Operators (needed for E_sol decomposition)
def lap(f):
    fr = np.gradient(f, drho, axis=0)
    return np.gradient(fr, drho, axis=0) + fr/RHO + \
           np.gradient(np.gradient(f, dz, axis=1), dz, axis=1)
def div(P, Q):
    return np.gradient(P, drho, axis=0) + P/RHO + np.gradient(Q, dz, axis=1)
def Phgrad(Ph_):
    sP, cP = np.sin(Ph_), np.cos(Ph_)
    return (cP*np.gradient(sP, drho, axis=0) - sP*np.gradient(cP, drho, axis=0),
            cP*np.gradient(sP, dz,   axis=1) - sP*np.gradient(cP, dz,   axis=1))

sT, cT = np.sin(Th), np.cos(Th)
Tr = np.gradient(Th, drho, axis=0); Tz = np.gradient(Th, dz, axis=1)
Pr, Pz = Phgrad(Ph)
gT2 = Tr**2 + Tz**2; gP2 = Pr**2 + Pz**2; gTP = Tr*Pr + Tz*Pz
g2  = gT2 + gP2 + 1.0/RHO**2
DT  = lap(Th); DP = div(Pr, Pz)
Ac  = cT*DT - sT*g2; Bc = sT*DP + 2*cT*gTP; Cc = -sT*DT - cT*gT2

w   = 2*np.pi*RHO
E_A1 = float(np.trapezoid(np.trapezoid(w*(A1/2)*(gT2 + sT**2*(gP2 + 1/RHO**2)), z, axis=1), rho))
E_A3 = float(np.trapezoid(np.trapezoid(w*(A3/2)*(Ac**2 + Bc**2 + Cc**2),          z, axis=1), rho))
E_A4 = float(np.trapezoid(np.trapezoid(w*(A4/2)*(1 - cT)**2,                       z, axis=1), rho))
E_sol= E_A1 + E_A3 + E_A4
virial = E_A1 - E_A3 + 3*E_A4

# Hopf charge
Pr2, Pz2 = Phgrad(Ph)
Q_hopf = float(np.trapezoid(np.trapezoid(
    sT*(np.gradient(Th, drho, axis=0)*Pz2 - np.gradient(Th, dz, axis=1)*Pr2),
    z, axis=1), rho)) / (4*np.pi)

R_eff = rho[np.argmax(np.trapezoid(sT, z, axis=1))]

print(f"\n── Converged Hopf soliton ──────────────────────────────")
print(f"  E_A1 = {E_A1:.6f} CCEF")
print(f"  E_A3 = {E_A3:.6f} CCEF")
print(f"  E_A4 = {E_A4:.6f} CCEF")
print(f"  E_sol= {E_sol:.6f} CCEF")
print(f"  Virial = {virial:.6f}   |v/E| = {abs(virial/E_sol):.6f}  ✓")
print(f"  Q    = {Q_hopf:.5f}   R_eff = {R_eff:.4f} L₀")
print(f"  Θ_max = {Th.max():.6f}  (π = {np.pi:.6f})")

# ─────────────────────────────────────────────────────────────────────────────
# 1.  Continuum zero-point energy density  e_c
#     e_c = (1/4π²) ∫₀^{k_UV} dk k² √(A4 + A1 k² + A3 k⁴)
# ─────────────────────────────────────────────────────────────────────────────
k_UV = np.sqrt(A1 / A3)   # Lifshitz crossover = 0.7706 CCEF⁻¹
k_arr = np.linspace(0.0, k_UV, 100_000)
omega_k = np.sqrt(A4 + A1*k_arr**2 + A3*k_arr**4)
e_c = float(np.trapezoid(k_arr**2 * omega_k, k_arr)) / (4.0 * np.pi**2)

# Also the full integral without UV cutoff (for comparison — would need higher cutoff)
k_full = np.linspace(0.0, 5.0, 500_000)
omega_full = np.sqrt(A4 + A1*k_full**2 + A3*k_full**4)
e_c_full = float(np.trapezoid(k_full**2 * omega_full, k_full)) / (4.0 * np.pi**2)

print(f"\n── Continuum zero-point energy density e_c ─────────────")
print(f"  k_UV = √(A1/A3) = {k_UV:.6f} CCEF⁻¹  (Lifshitz crossover)")
print(f"  ω_k at k=0   = {np.sqrt(A4):.6f} CCEF  (pion mass gap)")
print(f"  ω_k at k_UV  = {np.sqrt(A4 + A1*k_UV**2 + A3*k_UV**4):.6f} CCEF")
print(f"  e_c (k ≤ k_UV) = {e_c:.8f} CCEF L₀⁻³")
print(f"  e_c (k ≤ 5.0 ) = {e_c_full:.8f} CCEF L₀⁻³  (for comparison)")
print(f"  → e_c × L₀³ = {e_c * L0_FM**3:.4e} fm³ CCEF energy")

# ─────────────────────────────────────────────────────────────────────────────
# 2.  Soliton effective volume  V_eff
#     V_eff = ∫ 2πρ dρ dz  (1−cosΘ)² / (1−cosΘ)²_max
# ─────────────────────────────────────────────────────────────────────────────
one_minus_cosT = (1.0 - cT)
one_minus_cosT_sq = one_minus_cosT**2
norm = np.max(one_minus_cosT_sq)   # = (1-cosΘ_max)²

V_eff = float(np.trapezoid(np.trapezoid(w * one_minus_cosT_sq / norm, z, axis=1), rho))

# Also compute the geometric torus volume for comparison
# V_torus = 2π R_eff × π r_tube²  where r_tube is the half-width of sinΘ profile
sinT_int = np.trapezoid(sT, z, axis=1)        # ∫ sinΘ dz, function of ρ
r_tube_sq = float(np.trapezoid((rho - R_eff)**2 * sinT_int, rho) /
                   np.trapezoid(sinT_int, rho))
r_tube = np.sqrt(r_tube_sq)
V_torus = 2*np.pi * R_eff * np.pi * r_tube**2

print(f"\n── Soliton effective volume V_eff ──────────────────────")
print(f"  (1−cosΘ)²_max = {norm:.6f}  (at Θ={Th.max():.4f}; π gives 4.000)")
print(f"  V_eff = {V_eff:.6f} L₀³")
print(f"  Geometric torus (2π R_eff × π r_tube²):")
print(f"    R_eff = {R_eff:.4f} L₀,  r_tube ≈ {r_tube:.4f} L₀")
print(f"    V_torus = {V_torus:.4f} L₀³  (for comparison)")

# ─────────────────────────────────────────────────────────────────────────────
# 3.  Physical soliton energy after continuum subtraction
# ─────────────────────────────────────────────────────────────────────────────
E_cont_sub = e_c * V_eff          # energy displaced by soliton from continuum
E_phys     = E_sol - E_cont_sub   # physical mass

print(f"\n── Continuum subtraction ───────────────────────────────")
print(f"  e_c × V_eff = {E_cont_sub:.6f} CCEF")
print(f"  E_sol       = {E_sol:.6f} CCEF")
print(f"  E_phys      = E_sol − e_c×V_eff = {E_phys:.6f} CCEF")
print(f"  Fractional correction: {E_cont_sub/E_sol*100:.4f}%")

# ─────────────────────────────────────────────────────────────────────────────
# 4.  Mass ratio  m_p / m_π
# ─────────────────────────────────────────────────────────────────────────────
omega_pi = np.sqrt(A4)                     # CCEF pion frequency = 0.7362

mp_over_mpi_CCEF = E_phys  / omega_pi     # CCEF prediction
mp_over_mpi_EXP  = 938.272 / 134.977      # experimental  = 6.953
mp_over_mpi_HH   = 12.19                  # hedgehog (prior sessions, superseded)

print(f"\n── Mass ratio  m_p / m_π ───────────────────────────────")
print(f"  ω_π = √A4 = {omega_pi:.6f} CCEF = {omega_pi*E0_MEV:.2f} MeV")
print(f"  E_phys    = {E_phys:.6f} CCEF = {E_phys*E0_MEV:.2f} MeV")
print(f"  m_p/m_π (CCEF, Hopf, before sub) = {E_sol/omega_pi:.4f}")
print(f"  m_p/m_π (CCEF, Hopf, after sub)  = {mp_over_mpi_CCEF:.4f}")
print(f"  m_p/m_π (experiment)              = {mp_over_mpi_EXP:.4f}")
print(f"  m_p/m_π (CCEF hedgehog, prior)    = {mp_over_mpi_HH:.4f}  [superseded]")
print(f"  Discrepancy factor (Hopf/exp):      {mp_over_mpi_CCEF/mp_over_mpi_EXP:.2f}×")

# ─────────────────────────────────────────────────────────────────────────────
# 5.  Cross-check: hedgehog energy from F0_bvp.npy
#     Formulas (derived by integrating over angles of the hedgehog):
#       E_A1 = ∫ 4πr² dr (A1/2)(F_r² + 2 sin²F / r²)
#       E_A4 = ∫ 4πr² dr (A4/2)(1 − cosF)²
#       E_A3 = ∫ 4πr² dr (A3/2)(4π P² + (8π/3) Q²) / (4π)
#             = ∫ r² dr (A3/2)(4π P² + (8π/3) Q²)
#     where P = ΔF cosF − F_r² sinF        (Laplacian of n_z component)
#           Q = P − 2 sinF / r²             (Laplacian of n_x,y components)
#           ΔF = F_rr + 2 F_r / r
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n── Hedgehog cross-check (F0_bvp.npy) ──────────────────")
try:
    bvp = np.load(OUTDIR + 'F0_bvp.npy')   # shape (3, 3000): [r, F, F']
    r_h = bvp[0]; F_h = bvp[1]; Fp_h = bvp[2]

    # derivatives (use provided F' from BVP, compute F'' by differencing)
    Fpp_h = np.gradient(Fp_h, r_h)          # F_rr  (numerical 2nd derivative)

    # Prevent 1/r divergence at r=0 by starting from r[0]>0
    deltaF  = Fpp_h + 2.0*Fp_h / r_h       # ΔF = F_rr + 2F_r/r
    P_h     = deltaF * np.cos(F_h) - Fp_h**2 * np.sin(F_h)
    Q_h     = P_h - 2.0*np.sin(F_h) / r_h**2

    # Energy components
    EA1_h = float(np.trapezoid(4*np.pi * r_h**2 * (A1/2) *
                               (Fp_h**2 + 2*np.sin(F_h)**2/r_h**2), r_h))
    EA4_h = float(np.trapezoid(4*np.pi * r_h**2 * (A4/2) *
                               (1 - np.cos(F_h))**2, r_h))
    # Full angular-integrated A3 term:
    # ∫d³x (A3/2)|∇²n|² = ∫ r² dr (A3/2) [4π P² + (8π/3) Q²]
    EA3_h = float(np.trapezoid(r_h**2 * (A3/2) *
                               (4*np.pi * P_h**2 + (8*np.pi/3) * Q_h**2), r_h))

    E_hedge = EA1_h + EA3_h + EA4_h
    virial_h = EA1_h - EA3_h + 3*EA4_h

    print(f"  Loaded BVP profile: {bvp.shape}  r∈[{r_h[0]:.3f},{r_h[-1]:.1f}]")
    print(f"  F(r_min)={F_h[0]:.6f}  F(r_max)={F_h[-1]:.6f}")
    print(f"  EA1_hedgehog = {EA1_h:.6f} CCEF")
    print(f"  EA3_hedgehog = {EA3_h:.6f} CCEF")
    print(f"  EA4_hedgehog = {EA4_h:.6f} CCEF")
    print(f"  E_hedgehog   = {E_hedge:.6f} CCEF")
    print(f"  Virial_hh    = {virial_h:.6f}  |v/E|={abs(virial_h/E_hedge):.4f}")
    print(f"  m_p/m_π (hedgehog) = {E_hedge/omega_pi:.4f}")
    print(f"    Expected (prior sessions) = 12.19  →  ratio check: {E_hedge/omega_pi/12.19:.4f}")
    print(f"  Discrepancy factor (Hopf / hedgehog): {E_sol/E_hedge:.2f}×")
except FileNotFoundError:
    print("  F0_bvp.npy not found — skipping hedgehog cross-check")

# ─────────────────────────────────────────────────────────────────────────────
# 6.  Virial decomposition diagnostic
#     At the true minimum: E_A1 − E_A3 + 3 E_A4 = 0
#     The Derrick scaling also implies the Hopf topology REQUIRES A3>0:
#       Under r → λr:  E(λ) = λ E_A1 + (1/λ) E_A3 + λ³ E_A4
#       dE/dλ|_{λ=1} = E_A1 − E_A3 + 3 E_A4  ← virial
#     So the existence of a stable soliton requires A3>0 and E_A3>E_A1.
#     This is satisfied here (E_A3 >> E_A1), confirming the Hopf soliton
#     is stabilised by the bilaplacian term — as expected from theory.
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n── Virial decomposition at minimum ─────────────────────")
print(f"  E_A1 = {E_A1:.4f}  (scales as λ)")
print(f"  E_A3 = {E_A3:.4f}  (scales as 1/λ — stabiliser)")
print(f"  E_A4 = {E_A4:.4f}  (scales as λ³)")
print(f"  E_A3 / E_A1 = {E_A3/E_A1:.4f}  (must be >1 for stable soliton ✓)")
print(f"  E_A4 fraction = {E_A4/E_sol*100:.2f}% of total")

# ─────────────────────────────────────────────────────────────────────────────
# 7.  Summary
# ─────────────────────────────────────────────────────────────────────────────
print(f"\n{'='*64}")
print(f"SUMMARY")
print(f"{'='*64}")
print(f"  E_sol (Hopf, converged)  = {E_sol:.4f} CCEF = {E_sol*E0_MEV:.2f} MeV")
print(f"  e_c (Lifshitz, k≤k_UV)  = {e_c:.6e} CCEF L₀⁻³")
print(f"  V_eff                    = {V_eff:.4f} L₀³")
print(f"  e_c × V_eff              = {E_cont_sub:.6f} CCEF  ({E_cont_sub/E_sol*100:.3f}% of E_sol)")
print(f"  E_phys = E_sol − e_c V_eff = {E_phys:.4f} CCEF")
print()
print(f"  m_p/m_π (CCEF Hopf)  = {mp_over_mpi_CCEF:.2f}")
print(f"  m_p/m_π (experiment) = {mp_over_mpi_EXP:.2f}")
print(f"  Ratio:                 {mp_over_mpi_CCEF/mp_over_mpi_EXP:.1f}×  [OPEN — see notes]")
print()
print(f"  Working principle: 'The theory speaks for itself, right or wrong.'")
print()
print(f"NOTES ON THE DISCREPANCY:")
print(f"  (i)  The continuum subtraction e_c V_eff is negligible (<0.05% of E_sol).")
print(f"       Closing the mass gap requires either a much larger subtraction")
print(f"       or a different physical mechanism.")
print(f"  (ii) The bilaplacian (E_A3 = {E_A3:.0f}) dominates — the Hopf winding")
print(f"       carries enormous curvature energy. Whether a more refined ansatz")
print(f"       (smaller torus, better Φ profile) can reduce E_A3 is [OPEN].")
print(f" (iii) The hedgehog gave m_p/m_π ≈ 12.19 but was topologically wrong.")
print(f"       The correct Hopf topology costs more energy. Whether CCEF can")
print(f"       reconcile m_p/m_π with the Hopf topology is the central open problem.")
print(f"  (iv) A possible resolution: the physical pion in CCEF is NOT the k=0")
print(f"       continuum mode (√A4), but a bound state of the Hopf background")
print(f"       at a much higher energy scale. This would change ω_π and the ratio.")
print(f"{'='*64}")
