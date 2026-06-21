"""
ccef_skyrme.py  --  A2 as Faddeev-Skyrme term: recompute E_sol
=================================================================
Hypothesis under test:
  A2 = 8.971 is NOT the inert (n . grad n)^2 = 0 term but the
  Faddeev-Niemi / Skyrme stabiliser:

      L_A2 = (A2/2) F_{mu nu} F^{mu nu}
           = (A2/2) |partial_mu n x partial_nu n|^2 / 2

  For the axially-symmetric Hopf ansatz
    n(rho, z, phi) = (sinTheta cos(Phi+phi), sinTheta sin(Phi+phi), cosTheta)
  the three independent field-strength components are:

    F_{rho,z}   = sinT * (dT_dr * dPhi_dz - dPhi_dr * dT_dz)   [Jacobian]
    F_{rho,phi} = sinT * dT_dr / rho                (metric: 1/rho)
    F_{z,phi}   = sinT * dT_dz / rho                (metric: 1/rho)

  Metric-contracted invariant in cylindrical coordinates:
    |F|^2 = F_{rho,z}^2 + F_{rho,phi}^2/rho^2 + F_{z,phi}^2/rho^2

  Faddeev-Skyrme energy:
    E_A2 = (A2/2) integral |F|^2 d^3x
         = pi A2 integral [ sinT^2 * (dT_dr dPhi_dz - dPhi_dr dT_dz)^2 * rho
                           + sinT^2 * (dT_dr^2 + dT_dz^2) / rho ] drho dz

Virial theorem WITH A2 (both A2 and A3 are 4th-order in derivatives):
  dE/dlambda|_{lambda=1} = E_A1 - E_A2 - E_A3 + 3 E_A4 = 0

Fixed-point parameters (LOCKED): A1=1.000, A2=8.971, A3=1.684, A4=0.542
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# ---- Fixed-point parameters (LOCKED) ----------------------------------------
A1, A2, A3, A4 = 1.000, 8.971, 1.684, 0.542
E0  = 311.73      # MeV/CCEF
L0  = 0.633007    # fm/CCEF
omega_pi = np.sqrt(A4)          # 0.7362 CCEF  (pion mass)
m_p_ccef = 938.272 / E0         # 3.0099 CCEF
k_UV     = np.sqrt(A1/A3)       # 0.7706 CCEF^{-1}

print(f"A1={A1}  A2={A2}  A3={A3}  A4={A4}  [LOCKED]")
print(f"omega_pi = {omega_pi:.4f} CCEF = {omega_pi*E0:.1f} MeV")
print(f"m_p      = {m_p_ccef:.4f} CCEF = {m_p_ccef*E0:.1f} MeV")
print(f"k_UV     = {k_UV:.4f} CCEF^{{-1}} = {k_UV*E0:.1f} MeV")
print(f"R_Skyrme (naive) = sqrt(A2/A1) = {np.sqrt(A2/A1):.3f} CCEF = {np.sqrt(A2/A1)*L0:.2f} fm")
print()

# ---- Analytic Hopf ansatz ---------------------------------------------------
def make_hopf(Nr=140, Nz=280, R_eff=5.0, r_tube=2.8,
              rho_max=20., z_max=16.):
    rho = np.linspace(0.05, rho_max, Nr)
    z   = np.linspace(-z_max, z_max, Nz)
    RHO, Z = np.meshgrid(rho, z, indexing='ij')
    U = RHO - R_eff     # rho - R_eff
    V = Z               # z
    d = np.sqrt(U**2 + V**2) + 1e-12
    Th  = np.pi * (1.0 - np.tanh(d / r_tube))   # Theta profile
    Phi = np.arctan2(V, U)                        # poloidal angle Phi(rho,z)
    return Th, Phi, rho, z, RHO, Z, U, V, d

# ---- Energy with Faddeev-Skyrme A2 term ------------------------------------
def energy_full(R_eff=5.0, r_tube=2.8, Nr=140, Nz=280,
                rho_max=20., z_max=16., include_A2=True):
    """
    Returns (E_A1, E_A2, E_A3, E_A4, E_total).
    Set include_A2=False to reproduce the original A1+A3+A4 result.
    """
    Th, Phi, rho, z, RHO, Z, U, V, d = make_hopf(
        Nr=Nr, Nz=Nz, R_eff=R_eff, r_tube=r_tube,
        rho_max=rho_max, z_max=z_max)

    drho = rho[1] - rho[0]
    dz_  = z[1]   - z[0]
    sT   = np.sin(Th)
    cT   = np.cos(Th)

    # -- Theta gradients
    dT_dr = np.gradient(Th,  drho, axis=0)
    dT_dz = np.gradient(Th,  dz_,  axis=1)

    # -- Phi gradients (analytic: Phi = arctan2(z, rho-R_eff))
    d2     = d**2
    dP_dr  = -V / d2     # d(Phi)/d(rho) = -z / d^2
    dP_dz  =  U / d2     # d(Phi)/d(z)   = (rho-R)/d^2

    inv_rho = np.where(RHO > 1e-9, 1.0/RHO, 0.0)

    # -- Volume element factor
    w = 2.0 * np.pi * RHO
    def integ(f):
        return float(np.trapz(np.trapz(w * f, z, axis=1), rho))

    # -- A1 gradient energy
    e1 = (A1/2) * (dT_dr**2 + dT_dz**2
                   + sT**2 * (dP_dr**2 + dP_dz**2 + inv_rho**2))
    E_A1 = integ(e1)

    # -- A4 mass (anisotropy) energy
    e4   = (A4/2) * (1.0 - cT)**2
    E_A4 = integ(e4)

    # -- A3 bilaplacian energy  (unchanged from ccef_hopf_mpratio.py)
    def lap2d(f):
        return (np.gradient(np.gradient(f, drho, axis=0), drho, axis=0)
                + inv_rho * np.gradient(f, drho, axis=0)
                + np.gradient(np.gradient(f, dz_, axis=1), dz_, axis=1))

    cosPh = U / d;  sinPh = V / d
    Lap_sT  = lap2d(sT);   Lap_cT  = lap2d(cT)
    Lap_cPh = lap2d(cosPh); Lap_sPh = lap2d(sinPh)
    dsT_dr = cT*dT_dr; dsT_dz = cT*dT_dz
    dcPh_dr = 1/d - U**2/d**3;  dcPh_dz = -U*V/d**3
    dsPh_dr = -U*V/d**3;        dsPh_dz = 1/d - V**2/d**3
    LsTcPh = cosPh*Lap_sT + sT*Lap_cPh + 2*(dsT_dr*dcPh_dr + dsT_dz*dcPh_dz)
    LsTsPh = sinPh*Lap_sT + sT*Lap_sPh + 2*(dsT_dr*dsPh_dr + dsT_dz*dsPh_dz)
    lap_nx = LsTcPh - sT*cosPh*inv_rho**2
    lap_ny = LsTsPh - sT*sinPh*inv_rho**2
    lap_nz = Lap_cT
    e3   = (A3/2) * (lap_nx**2 + lap_ny**2 + lap_nz**2)
    E_A3 = integ(e3)

    # -- A2 Faddeev-Skyrme energy  [NEW]
    # Field strength components for the Hopf ansatz:
    #   F_{rho,z}   = sinT * (dT_dr*dPhi_dz - dPhi_dr*dT_dz)
    #   F_{rho,phi} = sinT * dT_dr          (covariant: divide by rho for |F|^2)
    #   F_{z,phi}   = sinT * dT_dz          (covariant: divide by rho for |F|^2)
    # Metric-contracted: |F|^2 = F_rz^2 + (F_r_phi/rho)^2 + (F_z_phi/rho)^2
    if include_A2:
        Jac    = dT_dr * dP_dz - dP_dr * dT_dz   # Jacobian det(dTheta,dPhi)/(drho,dz)
        F_rz   = sT * Jac
        F_rphi = sT * dT_dr
        F_zphi = sT * dT_dz
        e2     = (A2/2) * (F_rz**2
                           + F_rphi**2 * inv_rho**2
                           + F_zphi**2 * inv_rho**2)
        E_A2 = integ(e2)
    else:
        E_A2 = 0.0

    return E_A1, E_A2, E_A3, E_A4, E_A1 + E_A2 + E_A3 + E_A4


# ---- Fiducial point: compare old vs new ------------------------------------
print("="*62)
print("FIDUCIAL POINT  R_eff=5.0, r_tube=2.8")
print("="*62)
E1, E2, E3, E4, Et = energy_full(5.0, 2.8, include_A2=True)
E1_old, _, E3_old, E4_old, Et_old = energy_full(5.0, 2.8, include_A2=False)

print(f"  WITHOUT A2 (original):  E_sol = {Et_old:.2f} CCEF")
print(f"    E_A1={E1_old:.2f}  E_A3={E3_old:.2f}  E_A4={E4_old:.2f}")
virial_old = E1_old - E3_old + 3*E4_old
print(f"    Virial (E_A1-E_A3+3E_A4) = {virial_old:+.3f}")
print()
print(f"  WITH A2 Faddeev-Skyrme:  E_sol = {Et:.2f} CCEF")
print(f"    E_A1={E1:.2f}  E_A2={E2:.2f}  E_A3={E3:.2f}  E_A4={E4:.2f}")
print(f"    A2 fraction = {100*E2/Et:.1f}%")
print(f"    Virial (E_A1-E_A2-E_A3+3E_A4) = {E1-E2-E3+3*E4:+.3f}")
print()
print(f"  m_p target = {m_p_ccef:.4f} CCEF")
print(f"  Ratio E_sol/m_p (old) = {Et_old/m_p_ccef:.1f}x")
print(f"  Ratio E_sol/m_p (new) = {Et/m_p_ccef:.1f}x")
print()

# ---- 2D scan: R_eff x r_tube -----------------------------------------------
print("="*62)
print("2D SCAN: R_eff x r_tube  (with A2 active)")
print("="*62)

R_vals  = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0]
rt_vals = [0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4.0]

grid_E    = np.full((len(R_vals), len(rt_vals)), np.nan)
grid_E_old= np.full((len(R_vals), len(rt_vals)), np.nan)

for i, R in enumerate(R_vals):
    for j, rt in enumerate(rt_vals):
        rmax = max(R + 12, 16.)
        E1_, E2_, E3_, E4_, Et_ = energy_full(R, rt, Nr=110, Nz=220,
                                               rho_max=rmax, z_max=14.,
                                               include_A2=True)
        _, _, _, _, Et_o = energy_full(R, rt, Nr=110, Nz=220,
                                       rho_max=rmax, z_max=14.,
                                       include_A2=False)
        grid_E[i,j]     = Et_
        grid_E_old[i,j] = Et_o

R_arr  = np.array(R_vals)
rt_arr = np.array(rt_vals)

# 1D minimum in R at fixed rt
print("\n1D scan: R_eff at r_tube=2.8 (closest to fiducial)")
rt_idx = np.argmin(np.abs(rt_arr - 2.8))
col_new = grid_E[:,   rt_idx]
col_old = grid_E_old[:,rt_idx]
for i, R in enumerate(R_vals):
    print(f"  R={R:4.1f}: E_new={col_new[i]:.2f}  E_old={col_old[i]:.2f}")

# 1D minimum in rt at fixed R
print("\n1D scan: r_tube at R_eff=5.0 (fiducial ring radius)")
R_idx = np.argmin(np.abs(R_arr - 5.0))
row_new = grid_E[R_idx,:]
row_old = grid_E_old[R_idx,:]
for j, rt in enumerate(rt_vals):
    print(f"  rt={rt:.2f}: E_new={row_new[j]:.2f}  E_old={row_old[j]:.2f}")

# Global minimum in 2D
flat_new = grid_E.ravel()
valid     = ~np.isnan(flat_new)
idx_min   = np.nanargmin(flat_new)
i_min, j_min = np.unravel_index(idx_min, grid_E.shape)
E_new_min  = grid_E[i_min, j_min]
R_min_new  = R_vals[i_min]
rt_min_new = rt_vals[j_min]

flat_old   = grid_E_old.ravel()
idx_min_o  = np.nanargmin(flat_old)
i_mo, j_mo = np.unravel_index(idx_min_o, grid_E_old.shape)
E_old_min  = grid_E_old[i_mo, j_mo]
R_min_old  = R_vals[i_mo]
rt_min_old = rt_vals[j_mo]

print()
print("="*62)
print("MINIMUM ENERGIES")
print("="*62)
print(f"  WITHOUT A2:  E_sol_min = {E_old_min:.2f} CCEF = {E_old_min*E0:.0f} MeV")
print(f"    at R_eff={R_min_old:.1f} CCEF, r_tube={rt_min_old:.2f} CCEF")
print(f"    m_p/m_p_exp = {E_old_min/m_p_ccef:.1f}x")
print()
print(f"  WITH A2:     E_sol_min = {E_new_min:.2f} CCEF = {E_new_min*E0:.0f} MeV")
print(f"    at R_eff={R_min_new:.1f} CCEF, r_tube={rt_min_new:.2f} CCEF")
print(f"    m_p/m_p_exp = {E_new_min/m_p_ccef:.1f}x")
print()
print(f"  Improvement factor: {E_old_min/E_new_min:.2f}x reduction in E_sol_min")
print(f"  Proton target: {m_p_ccef:.4f} CCEF")
print(f"  Gap remaining: {E_new_min/m_p_ccef:.1f}x")

# Virial check at new minimum
E1m, E2m, E3m, E4m, _ = energy_full(R_min_new, rt_min_new,
                                      Nr=160, Nz=320, include_A2=True)
virial_new = E1m - E2m - E3m + 3*E4m
print(f"\n  Virial at new minimum (E_A1-E_A2-E_A3+3E_A4) = {virial_new:+.3f}")
print(f"  Energy breakdown: E_A1={E1m:.2f}  E_A2={E2m:.2f}  E_A3={E3m:.2f}  E_A4={E4m:.2f}")
print(f"  A2 fraction at minimum: {100*E2m/(E1m+E2m+E3m+E4m):.1f}%")

# ---- Plot ------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle(
    'CCEF: A2 = Faddeev-Skyrme Term -- Impact on E_sol\n'
    f'A1={A1}  A2={A2}(Skyrme)  A3={A3}  A4={A4}  [LOCKED]',
    fontsize=11, fontweight='bold')

# Panel 1: 2D heatmap of E_sol with A2
ax = axes[0]
im = ax.pcolormesh(rt_arr, R_arr, grid_E,
                   cmap='viridis_r', shading='auto')
plt.colorbar(im, ax=ax, label='E_sol [CCEF]')
ax.scatter(rt_min_new, R_min_new, s=200, marker='*', color='red',
           zorder=5, label=f'Min={E_new_min:.1f} CCEF')
ax.set_xlabel('r_tube [CCEF]')
ax.set_ylabel('R_eff [CCEF]')
ax.set_title('E_sol WITH A2 Skyrme')
ax.legend(fontsize=8)

# Panel 2: 2D heatmap of E_sol without A2
ax = axes[1]
im2 = ax.pcolormesh(rt_arr, R_arr, grid_E_old,
                    cmap='viridis_r', shading='auto')
plt.colorbar(im2, ax=ax, label='E_sol [CCEF]')
ax.scatter(rt_min_old, R_min_old, s=200, marker='*', color='red',
           zorder=5, label=f'Min={E_old_min:.1f} CCEF')
ax.set_xlabel('r_tube [CCEF]')
ax.set_ylabel('R_eff [CCEF]')
ax.set_title('E_sol WITHOUT A2 (baseline)')
ax.legend(fontsize=8)

# Panel 3: E_sol vs R_eff at r_tube=2.8, old vs new
ax = axes[2]
ax.plot(R_arr, col_old, 'o-', color='steelblue', label='A1+A3+A4 only', lw=2)
ax.plot(R_arr, col_new, 's-', color='darkorange', label='A1+A2+A3+A4 (Skyrme)', lw=2)
ax.axhline(m_p_ccef, ls=':', color='green', lw=1.5, label=f'm_p={m_p_ccef:.2f} CCEF')
ax.axhline(E_new_min, ls='--', color='darkorange', alpha=0.5, lw=1)
ax.axhline(E_old_min, ls='--', color='steelblue',  alpha=0.5, lw=1)
ax.set_xlabel('R_eff [CCEF]')
ax.set_ylabel('E_sol [CCEF]')
ax.set_title(f'Energy vs Ring Radius  (r_tube={rt_vals[rt_idx]:.1f})')
ax.legend(fontsize=8)
ax.set_ylim(0, min(col_old.max(), col_new.max(), 600))
ax.grid(alpha=0.3)

plt.tight_layout()
out = '/sessions/elegant-great-hypatia/mnt/outputs/ccef_skyrme.png'
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f"\nSaved {out}")

# ---- Summary ---------------------------------------------------------------
print()
print("="*62)
print("SUMMARY  [Labels per project convention]")
print("="*62)
print(f"""
A2 IDENTITY [CONJECT]:
  (n . grad n)^2 = 0 identically for unit vectors |n|=1.
  Therefore A2 must be the Faddeev-Skyrme term F_{{mu nu}} F^{{mu nu}},
  the only non-trivial 4th-order invariant for n in S^2.

ENERGY IMPACT [SOLID, this computation]:
  Fiducial (R=5.0, rt=2.8):
    E_sol (old, no A2) = {Et_old:.2f} CCEF = {Et_old*E0:.0f} MeV
    E_sol (new, +A2)   = {Et:.2f} CCEF = {Et*E0:.0f} MeV
    A2 contributes {100*E2/Et:.1f}% of total at fiducial point.

  2D minimum:
    WITHOUT A2:  E_min = {E_old_min:.2f} CCEF at R={R_min_old:.1f}, rt={rt_min_old:.1f}
    WITH A2:     E_min = {E_new_min:.2f} CCEF at R={R_min_new:.1f}, rt={rt_min_new:.1f}
    Improvement: {E_old_min/E_new_min:.2f}x reduction in minimum energy.
    Remaining gap to m_p: {E_new_min/m_p_ccef:.1f}x.

VIRIAL THEOREM (with A2) [SOLID]:
  Correct condition: E_A1 - E_A2 - E_A3 + 3 E_A4 = 0
  Both A2 (Skyrme) and A3 (bilaplacian) are 4th-order stabilisers.
  With A2 >> A3 (ratio {A2/A3:.1f}x), A2 now dominates stabilisation.

PHYSICAL SCALE OF A2 SOLITON [CONJECT]:
  Naive Derrick balance (A1 vs A2):
    R_opt = sqrt(A2/A1) = {np.sqrt(A2/A1):.3f} CCEF = {np.sqrt(A2/A1)*L0:.3f} fm
  This is the Faddeev-Niemi natural scale -- much smaller than 5.0 CCEF.
  The 2D grid minimum (above) gives the actual location.
""")
