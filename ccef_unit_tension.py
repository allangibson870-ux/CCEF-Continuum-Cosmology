"""
ccef_unit_tension.py
CCEF Unit Conversion Tension Analysis
m_p / m_pi = 12.19 (CCEF) vs 6.72 (experiment)

Strategy:
  1. Solve the hedgehog soliton ODE numerically (shooting method, RK4)
  2. Integrate the soliton energy -> M_sol in CCEF units
  3. Identify m_pi analog (mass gap k_IR)
  4. Compute ratio M_sol / k_IR and trace where 12.19 comes from
  5. Assess what would be needed to hit 6.72
  6. Diagnose: is the problem in M_sol, m_pi, or units?

Labels: SOLID = proven, CONJECT = plausible but unproven, ANSATZ = assumed input
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ============================================================
# FIXED-POINT PARAMETERS (SOLID - from RG fixed point)
# ============================================================
A1 = 1.000    # gradient coefficient
A2 = 8.971    # nonlinear gradient (n.grad n)^2
A3 = 1.684    # Lifshitz (grad^2 n)^2
A4 = 0.542    # easy-axis mass term
Zt = 1.000    # field renormalisation

# Derived scales (SOLID)
k_IR  = np.sqrt(A4 / A1)          # IR mass gap = sqrt(A4) = 0.7362
k_UV  = np.sqrt(A1 / A3)          # Lifshitz crossover = 0.7706
k_sol = np.sqrt(0.5*(k_IR**2 + k_UV**2))  # soliton momentum (ANSATZ from prior work)

# Unit conversion (SOLID - from ħc consistency)
L0_fm = 0.633007      # fm per CCEF
E0_MeV = 197.3269 / L0_fm   # MeV per CCEF   = 311.73

# Physical masses (experimental, PDG)
m_p_MeV  = 938.272   # proton
m_pi_MeV = 139.570   # pion (pi^0 ~ 134.98, pi^+- ~ 139.57, use charged)

ratio_exp = m_p_MeV / m_pi_MeV

print("=" * 65)
print("CCEF UNIT CONVERSION TENSION -- DIAGNOSTIC")
print("=" * 65)
print(f"\n--- Fixed-point parameters ---")
print(f"  A1={A1}, A2={A2}, A3={A3}, A4={A4}, Zt={Zt}")
print(f"\n--- Derived momentum scales ---")
print(f"  k_IR  = sqrt(A4/A1) = {k_IR:.6f} CCEF^-1  [IR gap / pion analog]")
print(f"  k_UV  = sqrt(A1/A3) = {k_UV:.6f} CCEF^-1  [Lifshitz crossover]")
print(f"  k_sol = {k_sol:.6f} CCEF^-1  [soliton scale, ANSATZ]")
print(f"\n--- Unit conversion ---")
print(f"  L0 = {L0_fm:.6f} fm/CCEF")
print(f"  E0 = hbar*c / L0 = {E0_MeV:.4f} MeV/CCEF")
print(f"\n--- Experimental target ---")
print(f"  m_p  = {m_p_MeV:.3f} MeV")
print(f"  m_pi = {m_pi_MeV:.3f} MeV")
print(f"  m_p / m_pi (exp) = {ratio_exp:.4f}")


# ============================================================
# SECTION 1: PION MASS ANALOG IN CCEF
# ============================================================
# The A4 term (A4/2)(1 - n_z)^2 breaks O(3) -> O(2).
# It gives the Q=0 field a mass gap at k=0:
#   omega^2(k=0) = A4 / Zt  =>  m_pi_CCEF = sqrt(A4/Zt)
# In physical units: m_pi_phys = m_pi_CCEF * E0

m_pi_CCEF = np.sqrt(A4 / Zt)
m_pi_phys_from_A4 = m_pi_CCEF * E0_MeV

print(f"\n{'='*65}")
print("SECTION 1: Pion mass analog [SOLID derivation, CONJECT identification]")
print(f"{'='*65}")
print(f"  m_pi_CCEF = sqrt(A4/Zt) = {m_pi_CCEF:.6f} CCEF")
print(f"  In physical units: {m_pi_phys_from_A4:.2f} MeV")
print(f"  Experimental m_pi = {m_pi_MeV:.2f} MeV")
print(f"  Ratio (CCEF/exp): {m_pi_phys_from_A4/m_pi_MeV:.4f}  (1.00 = perfect)")
print(f"  Discrepancy: {(m_pi_phys_from_A4/m_pi_MeV - 1)*100:.1f}%")
print(f"\n  CONJECT: The CCEF 'pion' is the lightest Q=0 excitation,")
print(f"  identified with the physical pion. k_IR = {k_IR:.4f} CCEF.")
print(f"  If correct: m_pi prediction = {m_pi_phys_from_A4:.1f} MeV (exp: {m_pi_MeV:.1f} MeV)")


# ============================================================
# SECTION 2: SOLITON MASS -- numerical ODE solution
# ============================================================
# Hedgehog ansatz for a spherically symmetric Q=1 soliton:
#
#   n(r, theta, phi) = (sin F(r) sin theta cos phi,
#                       sin F(r) sin theta sin phi,
#                       cos F(r))
#
# Note: this is a map S^2 -> S^2 via r*hat -> (theta, phi) embedding.
# The constraint |n|^2 = 1 is satisfied only in the equatorial plane;
# the standard treatment integrates over all angles to get an EFFECTIVE
# 1D energy (ANSATZ -- full spherically symmetric soliton in O(3) NLS).
#
# Energy of hedgehog (from angular integration of |grad n|^2):
#
#   E = 4*pi * INT_0^inf r^2 dr {
#         (A1/2) [ F'^2 + 2*sin^2(F)/r^2 ]
#       + (A3/2) * B_Lifshitz(F, F', F'', r)   [to be added]
#       + (A4/2) * (1 - cos F)^2
#       }
#
# This is the ANSATZ for the 3D hedgehog profile (it is the standard
# form used in the Skyrme model literature; Adkins-Nappi-Witten 1983).
#
# Note: A2 term (n . grad n)^2 = 0 identically on S^1-valued field.
#
# EL equation (from varying F):
#   F'' + (2/r)*F' - sin(2F)/r^2 - (A4/A1)*sin(F)*(1-cos(F)) = 0
#
# BCs: F(0) = pi, F(inf) = 0.
# (A4/A1)*sin(F)*(1-cos(F)) restores F -> 0.
#
# LABEL: ANSATZ (hedgehog form) + SOLID (EL derivation)

print(f"\n{'='*65}")
print("SECTION 2: Soliton profile -- shooting ODE [ANSATZ hedgehog + SOLID EL]")
print(f"{'='*65}")

# ---- RK4 integration of the ODE ----
# State: y = [F, F']
# ODE (singular at r=0, use Taylor start):
#
# Near r=0 with F = pi - c*r + O(r^3):
#   F'(0) = -c   (shooting parameter)
#
# At r -> inf: F -> 0 exponentially (mass gap ensures decay).

def ode_rhs(r, y):
    """
    EL equation: F'' + (2/r)*F' - sin(2F)/r^2 - (A4/A1)*sin(F)*(1-cos(F)) = 0
    y = [F, F']
    """
    F, Fp = y
    if r < 1e-12:
        return [Fp, 0.0]
    Fpp = (-2.0/r)*Fp + np.sin(2*F)/r**2 + (A4/A1)*np.sin(F)*(1 - np.cos(F))
    return [Fp, Fpp]

def rk4_step(r, y, h, rhs):
    k1 = np.array(rhs(r, y))
    k2 = np.array(rhs(r + h/2, y + h*k1/2))
    k3 = np.array(rhs(r + h/2, y + h*k2/2))
    k4 = np.array(rhs(r + h, y + h*k3))
    return y + h*(k1 + 2*k2 + 2*k3 + k4)/6.0

def shoot(c_init, r_end=80.0, N=40000):
    """
    Shoot from r=eps with F(eps) = pi - c*eps, F'(eps) = -c.
    Return (r_arr, F_arr, F_end).
    """
    eps = 1e-3
    y = np.array([np.pi - c_init*eps, -c_init])
    h = (r_end - eps) / N
    r_arr = [eps]
    F_arr = [y[0]]
    r = eps
    for _ in range(N):
        y = rk4_step(r, y, h, ode_rhs)
        r += h
        r_arr.append(r)
        F_arr.append(y[0])
    return np.array(r_arr), np.array(F_arr), y[0]

# ---- Bisection on shooting parameter c ----
# Correct solution has F(inf) -> 0.
# Large c: too steep -> F undershoots (goes negative)
# Small c: too shallow -> F stays too large (doesn't reach 0)

print(f"\nBisection search for shooting parameter c (F'(0) = -c)...")

c_lo, c_hi = 0.1, 3.0

# Determine sign convention at endpoint
def endpoint(c):
    _, _, Fend = shoot(c, r_end=60.0, N=20000)
    return Fend

# Find bracket
val_lo = endpoint(c_lo)
val_hi = endpoint(c_hi)
print(f"  c={c_lo}: F(end)={val_lo:.4f}")
print(f"  c={c_hi}: F(end)={val_hi:.4f}")

# Bisect
for _ in range(60):
    c_mid = 0.5*(c_lo + c_hi)
    val_mid = endpoint(c_mid)
    if val_mid * val_lo > 0:
        c_lo = c_mid
        val_lo = val_mid
    else:
        c_hi = c_mid
        val_hi = val_mid

c_sol = 0.5*(c_lo + c_hi)
print(f"\n  Converged: c_sol = {c_sol:.8f}")
print(f"  Check F(r=60) = {endpoint(c_sol):.2e}  (should be ~0)")

# Final profile
r_arr, F_arr, _ = shoot(c_sol, r_end=50.0, N=100000)

print(f"  F(r=0)  = {F_arr[0]:.6f}  (should be pi = {np.pi:.6f})")
print(f"  F(r=50) = {F_arr[-1]:.2e}  (should be ~0)")


# ============================================================
# SECTION 3: Soliton mass integral
# ============================================================
# M_sol = 4*pi * INT r^2 [ (A1/2)(F'^2 + 2 sin^2(F)/r^2)
#                         + (A4/2)(1-cos F)^2 ] dr
#
# We compute F' numerically (finite differences).

print(f"\n{'='*65}")
print("SECTION 3: Soliton mass integral [ANSATZ hedgehog form]")
print(f"{'='*65}")

dr = r_arr[1:] - r_arr[:-1]
r_mid  = 0.5*(r_arr[1:] + r_arr[:-1])
F_mid  = 0.5*(F_arr[1:] + F_arr[:-1])
Fp_mid = (F_arr[1:] - F_arr[:-1]) / dr

# Energy density components (at midpoints)
grad_term = (A1/2) * (Fp_mid**2 + 2*np.sin(F_mid)**2 / r_mid**2)
mass_term = (A4/2) * (1 - np.cos(F_mid))**2
epsilon   = grad_term + mass_term     # total energy density

# Radial integrand for E = 4*pi * INT r^2 epsilon dr
integrand = 4*np.pi * r_mid**2 * epsilon

M_A1 = 4*np.pi * np.trapz(r_mid**2 * (A1/2)*(Fp_mid**2 + 2*np.sin(F_mid)**2/r_mid**2), r_mid)
M_A4 = 4*np.pi * np.trapz(r_mid**2 * (A4/2)*(1-np.cos(F_mid))**2, r_mid)
M_sol = M_A1 + M_A4

print(f"\n  M_A1 (gradient)  = {M_A1:.6f} CCEF  [A1*Gradient energy]")
print(f"  M_A4 (potential) = {M_A4:.6f} CCEF  [A4*Potential energy]")
print(f"  M_sol (total)    = {M_sol:.6f} CCEF")

# In physical units
M_sol_MeV = M_sol * E0_MeV
print(f"\n  M_sol = {M_sol:.4f} CCEF = {M_sol_MeV:.1f} MeV")
print(f"  (experimental m_p = {m_p_MeV:.1f} MeV)")
print(f"\n  Discrepancy: {(M_sol_MeV/m_p_MeV - 1)*100:.0f}%")

# A3 Lifshitz correction estimate
# For the A3 term, (grad^2 n)^2 ~ (F'' + 2F'/r - 2 sin(F)cos(F)/r^2)^2
# Near the soliton core, k^2 ~ k_sol^2, so (k^2)^2 A3 ~ A3 * k_sol^4
# Perturbative estimate: M_A3 ~ A3 * k_sol^4 * (volume) = A3 * k_sol^4 / k_sol^3
#                              = A3 * k_sol ~ 1.684 * 0.754 ~ 1.27 CCEF
# This is ROUGH -- just to check sign of correction

M_A3_estimate = A3 * k_sol
print(f"\n  A3 Lifshitz correction (rough estimate): ~{M_A3_estimate:.2f} CCEF")
print(f"  (stabilises soliton but < 20% of M_A1+M_A4 -> subdominant)")


# ============================================================
# SECTION 4: Mass ratio analysis
# ============================================================
print(f"\n{'='*65}")
print("SECTION 4: Mass ratio analysis")
print(f"{'='*65}")

ratio_CCEF_computed = M_sol / m_pi_CCEF
print(f"\n  m_pi_CCEF = sqrt(A4) = {m_pi_CCEF:.6f} CCEF")
print(f"  M_sol     = {M_sol:.6f} CCEF")
print(f"  Ratio M_sol / m_pi_CCEF = {ratio_CCEF_computed:.4f}")
print(f"\n  Reference: m_p/m_pi (exp)   = {ratio_exp:.4f}")
print(f"             m_p/m_pi (CCEF)   = {ratio_CCEF_computed:.4f}")
print(f"             Discrepancy       = {(ratio_CCEF_computed/ratio_exp - 1)*100:.1f}%")

# Decompose into two sub-problems:
# Problem A: Is M_sol in CCEF units correct?
# Problem B: Is m_pi_CCEF the right identification?

ratio_A = M_sol_MeV / m_p_MeV   # want = 1
ratio_B = m_pi_phys_from_A4 / m_pi_MeV  # want = 1

print(f"\n--- Decomposition ---")
print(f"  M_sol / m_p    = {ratio_A:.4f}  (want 1.00)")
print(f"  m_pi(A4) / m_pi_exp = {ratio_B:.4f}  (want 1.00)")
print(f"  Product = {ratio_A/ratio_B:.4f}  (= m_p/m_pi(CCEF) / m_p/m_pi(exp))")
print(f"\n  >> Both M_sol and m_pi(A4) are OVER-predicted, but m_pi(A4)")
print(f"     is 64% too large while M_sol is {(ratio_A-1)*100:.0f}% too large.")
print(f"     These partial cancellations lead to ratio error of {(ratio_CCEF_computed/ratio_exp-1)*100:.0f}%.")


# ============================================================
# SECTION 5: What unit conversion would fix the masses?
# ============================================================
print(f"\n{'='*65}")
print("SECTION 5: What would fix the unit conversion?")
print(f"{'='*65}")

# If we anchor E0 on the proton: E0_p = m_p / M_sol
E0_from_proton = m_p_MeV / M_sol
m_pi_from_proton_anchor = m_pi_CCEF * E0_from_proton
print(f"\n  --- Anchor E0 on proton (E0 = m_p / M_sol) ---")
print(f"  E0 = {E0_from_proton:.2f} MeV/CCEF  (current: {E0_MeV:.2f})")
print(f"  Predicts m_pi = {m_pi_from_proton_anchor:.2f} MeV  (exp: {m_pi_MeV:.2f} MeV)")
print(f"  m_pi discrepancy: {(m_pi_from_proton_anchor/m_pi_MeV - 1)*100:.1f}%")

# If we anchor E0 on the pion: E0_pi = m_pi / m_pi_CCEF
E0_from_pion = m_pi_MeV / m_pi_CCEF
m_p_from_pion_anchor = M_sol * E0_from_pion
print(f"\n  --- Anchor E0 on pion (E0 = m_pi / k_IR) ---")
print(f"  E0 = {E0_from_pion:.2f} MeV/CCEF  (current: {E0_MeV:.2f})")
print(f"  Predicts m_p = {m_p_from_pion_anchor:.2f} MeV  (exp: {m_p_MeV:.2f} MeV)")
print(f"  m_p discrepancy: {(m_p_from_pion_anchor/m_p_MeV - 1)*100:.1f}%")

# Geometric mean anchor
E0_geom = np.sqrt(E0_from_proton * E0_from_pion)
m_p_geom  = M_sol * E0_geom
m_pi_geom = m_pi_CCEF * E0_geom
ratio_geom = m_p_geom / m_pi_geom  # same as M_sol/m_pi_CCEF = ratio_CCEF_computed
print(f"\n  --- Geometric mean E0 ---")
print(f"  E0 = {E0_geom:.2f} MeV/CCEF")
print(f"  m_p  = {m_p_geom:.1f} MeV  (exp: {m_p_MeV:.1f})")
print(f"  m_pi = {m_pi_geom:.1f} MeV  (exp: {m_pi_MeV:.1f})")
print(f"  Ratio still = {ratio_geom:.4f}  (no help: ratio is determined by theory)")


# ============================================================
# SECTION 6: ROOT CAUSE ANALYSIS
# ============================================================
print(f"\n{'='*65}")
print("SECTION 6: Root cause analysis -- where does 12.19 come from?")
print(f"{'='*65}")

# In the Skyrme model the dimensionless ratio is controlled by:
#   M_N / m_pi = (numerical factor from ODE) * sqrt(A1/A4)
# The numerical factor comes from the ODE solution.
# In CCEF: M_sol = M_A1 + M_A4. The pion mass m_pi = sqrt(A4).
# The ratio:
#   M_sol / m_pi = (M_A1 + M_A4) / sqrt(A4)
#   = M_A1/sqrt(A4) + M_A4/sqrt(A4)
#   = M_A1/sqrt(A4) + sqrt(A4) * M_A4/A4

# Dimensionless ratio from the ODE (should equal M_sol / m_pi):
print(f"\n  M_sol/m_pi = {ratio_CCEF_computed:.4f}")

# The Skyrme model (Adkins-Nappi-Witten 1983) gives M_N/m_pi ~ 36.5/(e*f_pi)
# For CCEF: the analog would involve A1, A4. Let's check the Derrick scaling:
# At the stable soliton, Virial theorem:
#   (D-2) E_grad = D E_pot  for D=3:  E_grad = 3 E_pot
# BUT this requires ONLY (grad n)^2 and potential terms.
# Check our solution:
virial_check = M_A1 / M_A4 if M_A4 > 0 else float('inf')
print(f"\n  Virial ratio M_A1/M_A4 = {virial_check:.4f}")
print(f"  Virial theorem (pure A1+A4 in 3D): expects M_A1/M_A4 = 3")
print(f"  Deviation: {(virial_check/3 - 1)*100:.1f}%")

# A rough analytic estimate: the soliton size r_sol ~ 1/(k_IR) = 1/sqrt(A4)
# M_A1 ~ A1 * (1/r_sol) * (pi^2) * 4pi = 4*pi^2 * A1 * sqrt(A4) [rough]
# M_A4 ~ A4 * r_sol^3 * (pi^2/3) * 4pi = 4*pi^3/3 * A4 / A4^(3/2) = 4*pi^3/(3*sqrt(A4))
# Ratio M_sol/m_pi ~ (4*pi^2*A1*sqrt(A4) + 4*pi^3/3/sqrt(A4)) / sqrt(A4)
#                  = 4*pi^2*A1 + 4*pi^3/(3*A4)
r_sol_est = 1.0 / k_IR
M_A1_est = 4*np.pi * A1 * (np.pi/r_sol_est)   # rough
M_A4_est = 4*np.pi * A4 * r_sol_est**3 * np.pi**2 / 3  # rough
M_sol_est = M_A1_est + M_A4_est
print(f"\n  Rough analytic estimate:")
print(f"    r_sol ~ 1/k_IR = {r_sol_est:.4f} CCEF")
print(f"    M_A1 (rough)  ~ {M_A1_est:.2f} CCEF")
print(f"    M_A4 (rough)  ~ {M_A4_est:.2f} CCEF")
print(f"    M_sol (rough) ~ {M_sol_est:.2f} CCEF  (numerical: {M_sol:.2f})")

# Scaling analysis: ratio M_sol/m_pi as function of lambda = A4/A1
print(f"\n  --- Scaling analysis: how ratio changes with A4/A1 ---")
print(f"  Current A4/A1 = {A4/A1:.4f}")
print(f"  To get ratio = 6.72, would need M_sol/m_pi = 6.72")
print(f"  Current: {ratio_CCEF_computed:.2f}. Need ratio = 6.72.")
print(f"  Factor to reduce: {ratio_CCEF_computed/6.72:.4f}")
print(f"  If M_sol scales as A4^alpha and m_pi as A4^(1/2):")
print(f"  ratio ~ A4^(alpha - 1/2). Cannot be fixed by A4 alone without")
print(f"  breaking the fixed-point constraint.")


# ============================================================
# SECTION 7: Skyrme-term stabilisation vs Lifshitz stabilisation
# ============================================================
print(f"\n{'='*65}")
print("SECTION 7: Stabilisation mechanism comparison")
print(f"{'='*65}")

# Standard Skyrme model (Skyrme 1961):
#   E = f_pi^2/2 * INT |grad n|^2 + 1/(4e^2) * INT |n x grad n|^2
#   Stable soliton from Derrick balance: E_grad ~ lambda, E_Skyrme ~ lambda^{3-4} = lambda^{-1}
#   Soliton mass: M_N = 12*pi^2 * f_pi / e (Adkins-Nappi-Witten)
#   Pion mass from separate potential term.
#
# CCEF:
#   E = A1/2 * INT |grad n|^2 + A3/2 * INT |grad^2 n|^2 + A4/2 * INT (1-n_z)^2
#   Derrick balance: E_A1 ~ lambda, E_A3 ~ lambda^{3-4} = lambda^{-1} (like Skyrme)
#   Key difference: A3 stabilises at r_min = (A3/A1)^{1/2} = k_UV^{-1}
#   vs Skyrme: r_min = 1/(f_pi * e)
#
# The A3 term contributes to M_sol but we excluded it from the ODE.
# Let us estimate the FULL soliton mass including A3.

# A3 Lifshitz term: density ~ A3 * (nabla^2 n)^2 ~ A3 * k^4 * (delta n)^2
# For a soliton of size r_s, dominant k ~ pi/r_s:
# E_A3 ~ A3 * (pi/r_s)^4 * (pi/r_s)^(-3) * (profile) ~ A3 * pi / r_s
# At the A1+A4 soliton r_s ~ 1/k_IR:
E_A3_at_rA4sol = A3 * np.pi * k_IR
print(f"\n  A3 Lifshitz energy at the A1+A4 soliton scale:")
print(f"  E_A3 ~ A3 * pi * k_IR = {E_A3_at_rA4sol:.4f} CCEF")
print(f"  vs M_sol(A1+A4) = {M_sol:.4f} CCEF")
print(f"  A3 adds ~{E_A3_at_rA4sol/M_sol*100:.1f}% to the soliton mass")

# Virial theorem with A3 included: in D=3 with (grad n)^2 + (grad^2 n)^2 + V:
# 0 = dE/d_lambda = E_A1 - E_A3 - 3*E_A4  [scaling derivatives]
# Wait: (grad^2 n)^2 has 4 derivatives, scales as lambda^{D-4}=lambda^{-1}
# d/d_lambda[(lambda^{-1} E_A3)] = -lambda^{-2} E_A3 [at lambda=1]
# Full virial: E_A1 = E_A3 + 3*E_A4
print(f"\n  Virial theorem with A3: E_A1 = E_A3 + 3*E_A4")
print(f"  If we include A3: the soliton SIZE shifts to minimise E_A1 - E_A3 - 3*E_A4 = 0")
print(f"  Competing: A1 gradient wants r ~ 1/sqrt(A1) = 1")
print(f"             A3 Lifshitz wants r ~ k_UV^{-1} = {1/k_UV:.4f}")
print(f"             A4 potential wants r ~ k_IR^{-1} = {1/k_IR:.4f}")
print(f"  k_UV ~ k_IR ~ k_sol (all near 0.74-0.77) -> nearly identical scales!")
print(f"  This clustering is a special feature of the CCEF fixed point.")


# ============================================================
# SECTION 8: Is the A2 term relevant?
# ============================================================
print(f"\n{'='*65}")
print("SECTION 8: Does A2 contribute? [SOLID: no for |n|=1 soliton]")
print(f"{'='*65}")

# A2 term: (A2/2) * (n . grad_i n)^2 = (A2/2) * sum_i (n . partial_i n)^2
# Since |n|^2 = 1 => n . partial_i n = (1/2) partial_i |n|^2 = 0.
# Therefore A2 contribution is IDENTICALLY zero for unit-sphere-valued fields.
# A2 would contribute in a LINEAR sigma model where |n| != 1 (sigma field).

print(f"\n  A2 = {A2} term: (A2/2)(n.grad n)^2 = 0 identically for |n|=1.")
print(f"  Proof: n.partial_i n = (1/2)partial_i|n|^2 = 0  [SOLID]")
print(f"  => A2 does NOT contribute to soliton mass.")
print(f"  => A2 only affects the KINETIC sector (q=0 dispersion, cosmological constant).")
print(f"  => The ratio M_sol/m_pi depends only on A1, A3, A4.")


# ============================================================
# SECTION 9: Candidate resolutions
# ============================================================
print(f"\n{'='*65}")
print("SECTION 9: Candidate resolutions of the 81% discrepancy")
print(f"{'='*65}")

print(f"""
  OBSERVATION: ratio_CCEF = {ratio_CCEF_computed:.4f}, ratio_exp = {ratio_exp:.4f}
  Factor of {ratio_CCEF_computed/ratio_exp:.4f} too large.

  CANDIDATE A: Wrong soliton ansatz [CONJECT]
    The hedgehog n = (sinF sin theta cos phi, sinF sin theta sin phi, cos F)
    is the standard Skyrme form but may not be the lowest-energy Q=1
    configuration in CCEF. The Hopf soliton (knotted field line) could
    have a different mass. True minimum requires full 3D variational calculation.
    Direction: lower-energy soliton -> smaller M_sol -> smaller ratio.

  CANDIDATE B: Pion identification is wrong [CONJECT]
    The CCEF 'pion' (mass gap sqrt(A4)={m_pi_CCEF:.4f} CCEF = {m_pi_phys_from_A4:.0f} MeV)
    is 64% heavier than the physical pion (140 MeV).
    The physical pion is pseudo-Goldstone from chiral symmetry breaking.
    CCEF breaks O(3)->O(2) via A4, NOT chiral symmetry.
    A lighter CCEF mode (e.g., the dual-pole mode m_dp={0.0195:.4f} CCEF)
    may be a better identification. If m_pi = m_dp = 0.0195 CCEF:
      ratio = M_sol / m_dp = {M_sol/0.0195:.1f}   [way too large]
    So m_dp is ruled out as pion.

  CANDIDATE C: Lattice renormalisation [CONJECT]
    The A1,A3,A4 values are at the UV Lifshitz fixed point.
    Physical observables require RG running to the IR (proton/pion scale).
    If A4 runs up (becomes larger) toward the IR, k_IR increases ->
    m_pi increases -> ratio decreases.
    If M_sol is set by the UV fixed-point but m_pi is an IR quantity,
    their ratio depends on the RG trajectory, not just fixed-point values.
    This is the most physically motivated resolution.

  CANDIDATE D: Wrong unit normalisation for L0 [CONJECT]
    L0 = 0.633 fm was obtained by matching to some hadronic scale.
    If L0 is matched to a different observable (e.g., nucleon charge radius
    r_p = 0.879 fm -> L0 = 0.879/sqrt(A1/A4)... different value),
    both m_pi and M_sol shift together but the RATIO is unchanged.
    => Unit normalisation cannot fix the ratio.

  CANDIDATE E: Missing loop corrections [CONJECT]
    M_sol computed here is CLASSICAL (tree-level).
    1-loop quantum corrections (zero-point energy, Casimir) can shift M_sol.
    In the Skyrme model, quantum corrections can shift M_N by 10-30%.
    An 81% correction from loops is possible but large.

  VERDICT [CONJECT]:
    The tension is most likely STRUCTURAL: the CCEF fixed-point parameters
    A1, A3, A4 give a soliton that is too heavy relative to the pion
    because the Lifshitz sector (A3) provides soliton stabilisation that
    happens at a scale close to (but not equal to) the pion mass scale.
    The near-degeneracy k_IR ~ k_UV ~ k_sol is a coincidence of the
    fixed point that does NOT reproduce the QCD hierarchy m_p >> m_pi.
    CCEF cannot simultaneously fit m_p and m_pi with a single unit
    conversion without additional dynamics (RG running, higher-order loops).
""")


# ============================================================
# SECTION 10: Summary table
# ============================================================
print(f"\n{'='*65}")
print("SECTION 10: Summary")
print(f"{'='*65}")
print(f"""
  Quantity           | CCEF (natural)  | CCEF (MeV)   | Exp (MeV) | Status
  -------------------|-----------------|--------------|-----------|----------
  m_pi analog        | {m_pi_CCEF:.4f} CCEF    | {m_pi_phys_from_A4:.1f}       | {m_pi_MeV:.1f}    | CONJECT
  M_sol (soliton)    | {M_sol:.4f} CCEF    | {M_sol_MeV:.1f}       | {m_p_MeV:.1f}     | ANSATZ+SOLID
  M_sol / m_pi       | {ratio_CCEF_computed:.4f}          | --           | {ratio_exp:.4f}   | CONJECT

  Unit scale E0      | {E0_MeV:.2f} MeV/CCEF | --           | --        | SOLID(ħc)

  m_p/m_pi discrepancy: {(ratio_CCEF_computed/ratio_exp-1)*100:.0f}%  -- OPEN PROBLEM

  Most likely cause: k_IR ~ k_UV ~ k_sol (scale degeneracy at fixed point)
  means CCEF cannot reproduce the 6.72 ratio without IR running or new dynamics.
  LABEL: CONJECT
""")


# ============================================================
# PLOTS
# ============================================================
fig = plt.figure(figsize=(14, 10))
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.45, wspace=0.35)

# Panel 1: Soliton profile
ax1 = fig.add_subplot(gs[0, 0])
mask = r_arr < 20
ax1.plot(r_arr[mask], F_arr[mask], 'C0', lw=2)
ax1.axhline(np.pi, color='k', ls='--', lw=0.8, alpha=0.5, label='F(0)=pi')
ax1.axhline(0.0,   color='k', ls='--', lw=0.8, alpha=0.5, label='F(inf)=0')
ax1.axvline(1.0/k_IR, color='C3', ls=':', lw=1.5, label='r=1/k_IR')
ax1.set_xlabel('r (CCEF)')
ax1.set_ylabel('F(r) (rad)')
ax1.set_title('Soliton profile F(r)\n[ANSATZ hedgehog, SOLID EL eq]', fontsize=9)
ax1.legend(fontsize=7)
ax1.set_ylim(-0.3, np.pi+0.5)
ax1.grid(True, alpha=0.3)

# Panel 2: Energy density
ax2 = fig.add_subplot(gs[0, 1])
r_mid2 = r_mid[r_mid < 15]
idx = r_mid < 15
g2 = (A1/2)*(Fp_mid[idx]**2 + 2*np.sin(F_mid[idx])**2/r_mid[idx]**2)
m2 = (A4/2)*(1 - np.cos(F_mid[idx]))**2
ax2.plot(r_mid2, r_mid2**2 * g2 * 4*np.pi, 'C0', lw=2, label='A1 gradient')
ax2.plot(r_mid2, r_mid2**2 * m2 * 4*np.pi, 'C1', lw=2, label='A4 potential')
ax2.plot(r_mid2, r_mid2**2 * (g2+m2) * 4*np.pi, 'k', lw=2, ls='--', label='total')
ax2.set_xlabel('r (CCEF)')
ax2.set_ylabel('4*pi*r^2 * epsilon(r)')
ax2.set_title('Soliton energy density\nM_sol = area under black curve', fontsize=9)
ax2.legend(fontsize=7)
ax2.grid(True, alpha=0.3)

# Panel 3: Mass ratio bar chart
ax3 = fig.add_subplot(gs[0, 2])
categories = ['m_pi (CCEF)\n*E0', 'M_sol (CCEF)\n*E0', 'Ratio\nM_sol/m_pi']
ccef_vals  = [m_pi_phys_from_A4,  M_sol_MeV,  ratio_CCEF_computed]
exp_vals   = [m_pi_MeV,           m_p_MeV,    ratio_exp]
x = np.arange(len(categories))
w = 0.35
bars1 = ax3.bar(x - w/2, ccef_vals, w, label='CCEF (this work)', color='C0')
bars2 = ax3.bar(x + w/2, exp_vals,  w, label='Experiment', color='C2')
ax3.set_xticks(x)
ax3.set_xticklabels(categories, fontsize=8)
ax3.set_title('CCEF vs experiment', fontsize=9)
ax3.legend(fontsize=8)
for bar in bars1:
    ax3.text(bar.get_x()+bar.get_width()/2, bar.get_height()*1.02,
             f'{bar.get_height():.1f}', ha='center', va='bottom', fontsize=7)
for bar in bars2:
    ax3.text(bar.get_x()+bar.get_width()/2, bar.get_height()*1.02,
             f'{bar.get_height():.1f}', ha='center', va='bottom', fontsize=7)
ax3.grid(True, alpha=0.3, axis='y')

# Panel 4: Scale clustering
ax4 = fig.add_subplot(gs[1, 0])
scales_CCEF = {'k_IR':k_IR, 'k_sol':k_sol, 'k_UV':k_UV}
scales_MeV  = {k: v*E0_MeV for k,v in scales_CCEF.items()}
scales_MeV['m_pi(exp)'] = m_pi_MeV
scales_MeV['m_p(exp)/13'] = m_p_MeV/ratio_CCEF_computed  # same reference
colors_bar = ['C0', 'C1', 'C4', 'C2', 'C3']
bars_k = ax4.bar(range(len(scales_MeV)), list(scales_MeV.values()), color=colors_bar)
ax4.set_xticks(range(len(scales_MeV)))
ax4.set_xticklabels(list(scales_MeV.keys()), rotation=20, fontsize=8)
ax4.set_ylabel('MeV')
ax4.set_title('Scale clustering at fixed point\n(k_IR~k_UV~k_sol all near 230 MeV)', fontsize=8)
ax4.grid(True, alpha=0.3, axis='y')
ax4.axhline(m_pi_MeV, color='C2', ls='--', lw=1.2, label='m_pi exp')
ax4.legend(fontsize=7)

# Panel 5: Virial decomposition
ax5 = fig.add_subplot(gs[1, 1])
components = ['E_grad\n(A1)', 'E_pot\n(A4)', 'M_sol\ntotal']
vals = [M_A1, M_A4, M_sol]
colors5 = ['C0', 'C1', 'k']
ax5.bar(components, vals, color=colors5)
ax5.axhline(M_sol/4, ls=':', color='gray', lw=1, label='M_sol/4')
for i, v in enumerate(vals):
    ax5.text(i, v*1.02, f'{v:.2f}', ha='center', va='bottom', fontsize=9)
ax5.set_ylabel('CCEF units')
ax5.set_title(f'Soliton mass decomposition\nVirial ratio M_A1/M_A4={virial_check:.2f} (expect 3)', fontsize=8)
ax5.grid(True, alpha=0.3, axis='y')

# Panel 6: Summary - candidate resolutions
ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')
summary_text = (
    f"UNIT TENSION SUMMARY\n"
    f"{'_'*32}\n\n"
    f"m_p/m_pi:\n"
    f"  CCEF: {ratio_CCEF_computed:.2f}\n"
    f"  Exp:  {ratio_exp:.2f}\n"
    f"  Error: {(ratio_CCEF_computed/ratio_exp-1)*100:.0f}%\n\n"
    f"Root cause [CONJECT]:\n"
    f"  k_IR ~ k_UV ~ k_sol\n"
    f"  Scale degeneracy at RG\n"
    f"  fixed point prevents\n"
    f"  QCD-like hierarchy.\n\n"
    f"Cannot fix with unit rescaling\n"
    f"(ratio is unit-free).\n\n"
    f"Candidates:\n"
    f"  A. Wrong soliton ansatz\n"
    f"  B. RG running A4(IR)>A4(UV)\n"
    f"  C. 1-loop quantum corr.\n\n"
    f"STATUS: OPEN PROBLEM"
)
ax6.text(0.05, 0.95, summary_text, va='top', ha='left',
         fontsize=8, fontfamily='monospace', transform=ax6.transAxes,
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

fig.suptitle(
    f'CCEF Unit Conversion Tension: m_p/m_pi = {ratio_CCEF_computed:.2f} (CCEF) vs {ratio_exp:.2f} (exp)\n'
    f'A1={A1}, A2={A2}, A3={A3}, A4={A4}  |  E0={E0_MeV:.1f} MeV/CCEF',
    fontsize=11, y=0.98
)

plt.savefig(
    r'C:\Users\allan\AppData\Roaming\Claude\local-agent-mode-sessions'
    r'\4c0c8b95-3e74-4f92-b6af-062b722b0506\1e400edc-7bdc-449c-a9f5-e95ddba301a5'
    r'\local_4d5ad3aa-c826-4981-b1de-730c3eea9640\outputs\ccef_unit_tension.png',
    dpi=150, bbox_inches='tight'
)
print("\nPlot saved: ccef_unit_tension.png")
print("\nDone.")
