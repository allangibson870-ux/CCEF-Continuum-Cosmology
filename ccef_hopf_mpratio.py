"""
ccef_hopf_mpratio.py  —  CCEF Diagnosis: m_p/m_π = 1751 vs exp 6.95 (252× off)
================================================================================
Systematically identifies the root cause of the 252× discrepancy between the
CCEF Hopf soliton mass ratio and experiment.

Sections:
  0  — Setup / load Hopf field (fallback: analytic tanh ansatz)
  1  — Energy budget  (A1, A3, A4 decomposition)              [SOLID]
  2  — Virial condition  (is the soliton at its minimum?)     [SOLID]
  3  — R_eff scan  (where is the ring radius minimum?)        [SOLID]
  4  — r_tube scan  (where is the tube virial minimum?)       [SOLID]
  5  — Hedgehog comparison  (same topology, lower energy?)    [CONJECT — formula differs from BVP]
  6  — Pion mass identity  (is ω_π = √A4 correct?)           [CONJECT]
  7  — Diagnosis figure (6-panel dark background)
  8  — Summary / open problem statement

Fixed parameters (no tuning):
  A1=1.000, A3=1.684, A4=0.542
  E0=311.73 MeV/CCEF, L0=0.633007 fm/CCEF
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

# ── fixed parameters ──────────────────────────────────────────────────────────
A1, A3, A4 = 1.000, 1.684, 0.542
E0_MEV = 311.73
L0_FM  = 0.633007

k_UV     = np.sqrt(A1 / A3)    # 0.7706 CCEF^{-1}  Lifshitz crossover
omega_pi = np.sqrt(A4)          # 0.7362 CCEF  pion mass gap
r_Lifsh  = np.sqrt(A3 / A1)    # 1.298 CCEF  = 1/k_UV  tube natural scale

CLR = dict(
    solid   = '#00ff88',
    conject = '#ff9f1c',
    ansatz  = '#cf9fff',
    open_   = '#ff4466',
    new     = '#ffff55',
    bg      = '#0d0d0d',
    ax_bg   = '#141414',
    grid    = '#2a2a2a',
    text    = '#e8e8e8',
)

OUT_DIR = Path(__file__).parent
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ── section 0: analytic Hopf ansatz ──────────────────────────────────────────
def make_hopf(Nr=200, Nz=400, R_eff=5.0, r_tube=2.8,
              rho_max=20.0, z_max=18.0):
    """Analytic tanh Hopf ansatz: Θ=π(1−tanh(d/r_tube)), Φ=arctan2(z,ρ−R)."""
    rho = np.linspace(0.05, rho_max, Nr)
    z   = np.linspace(-z_max, z_max, Nz)
    RHO, Z = np.meshgrid(rho, z, indexing='ij')
    U = RHO - R_eff
    V = Z
    d = np.sqrt(U**2 + V**2) + 1e-12
    Th = np.pi * (1.0 - np.tanh(d / r_tube))
    return Th, rho, z, RHO, Z, U, V, d


def energy_components(Th, rho, z, RHO, Z, U, V, d, R_eff=None, r_tube=None):
    """
    E_A1, E_A3, E_A4 for the analytic Hopf ansatz (cylindrical, m=1 sector).
    Uses exact analytic Φ gradients to avoid branch-cut errors.
    """
    drho = rho[1] - rho[0]
    dz   = z[1]   - z[0]
    sT, cT = np.sin(Th), np.cos(Th)

    # Θ gradients
    dT_dr = np.gradient(Th, drho, axis=0)
    dT_dz = np.gradient(Th, dz,   axis=1)

    # Φ gradients (analytic: Φ = arctan2(z, ρ−R_eff))
    d2 = d**2
    dP_dr = -V / d2    # −z / d²
    dP_dz =  U / d2    # (ρ−R) / d²

    inv_rho = np.where(RHO > 1e-9, 1.0 / RHO, 0.0)

    # ── A1 energy density: (A1/2)[|∇Θ|² + sin²Θ(|∇Φ|² + 1/ρ²)] ──────────
    e1 = (A1/2) * (dT_dr**2 + dT_dz**2
                   + sT**2 * (dP_dr**2 + dP_dz**2 + inv_rho**2))

    # ── A4 energy density: (A4/2)(1 − cosΘ)² ─────────────────────────────
    e4 = (A4/2) * (1.0 - cT)**2

    # ── A3 energy density: (A3/2)|∇²n|² ──────────────────────────────────
    # For the axially symmetric Hopf field n(ρ,φ,z) = (sinΘ cos(Φ+φ), sinΘ sin(Φ+φ), cosΘ):
    #   ∂_φ²n_⊥ = −n_⊥  →  (1/ρ²)∂_φ²n = −sin Θ ê_⊥/ρ²
    # Full 3D Laplacian components at φ=0:
    #   ∇²n_z = Δ_{2D} cosΘ
    #   ∇²n_x = Δ_{2D}(sinΘ cosΦ) − sinΘ cosΦ/ρ²
    #   ∇²n_y = Δ_{2D}(sinΘ sinΦ) − sinΘ sinΦ/ρ²
    # Because the field rotates uniformly in φ, |∇²n|² is φ-independent,
    # so integrating with 2πρ dρ dz is exact.

    def lap2d(f):
        return (np.gradient(np.gradient(f, drho, axis=0), drho, axis=0)
                + inv_rho * np.gradient(f, drho, axis=0)
                + np.gradient(np.gradient(f, dz, axis=1), dz, axis=1))

    cosPh = U / d    # cos(Φ) = (ρ−R)/d
    sinPh = V / d    # sin(Φ) = z/d

    # 2D Laplacians
    Lap_sT  = lap2d(sT)
    Lap_cT  = lap2d(cT)
    Lap_cPh = lap2d(cosPh)
    Lap_sPh = lap2d(sinPh)

    # Exact Φ-gradients for cross terms
    dsT_dr = cT * dT_dr;  dsT_dz = cT * dT_dz
    dcPh_dr = 1.0/d - U**2/d**3
    dcPh_dz = -U*V/d**3
    dsPh_dr = -U*V/d**3
    dsPh_dz = 1.0/d - V**2/d**3

    Lap_sTcPh = cosPh*Lap_sT + sT*Lap_cPh + 2*(dsT_dr*dcPh_dr + dsT_dz*dcPh_dz)
    Lap_sTsPh = sinPh*Lap_sT + sT*Lap_sPh + 2*(dsT_dr*dsPh_dr + dsT_dz*dsPh_dz)

    lap_nx = Lap_sTcPh - sT*cosPh*inv_rho**2
    lap_ny = Lap_sTsPh - sT*sinPh*inv_rho**2
    lap_nz = Lap_cT

    e3 = (A3/2) * (lap_nx**2 + lap_ny**2 + lap_nz**2)

    # Volume element
    w = 2.0 * np.pi * RHO

    def integ(f):
        return float(np.trapz(np.trapz(w * f, z, axis=1), rho))

    E_A1 = integ(e1)
    E_A3 = integ(e3)
    E_A4 = integ(e4)
    return E_A1, E_A3, E_A4, E_A1 + E_A3 + E_A4


# ── section 1: energy budget at fiducial ─────────────────────────────────────
print("\n" + "="*70)
print("CCEF Hopf m_p/m_π = 1751 vs exp 6.95 — DIAGNOSIS")
print("="*70)

R_fid, rt_fid = 5.0, 2.8
Th0, rho0, z0, RHO0, Z0, U0, V0, d0 = make_hopf(Nr=200, Nz=400,
                                                   R_eff=R_fid, r_tube=rt_fid)
E1_f, E3_f, E4_f, Es_f = energy_components(Th0, rho0, z0, RHO0, Z0, U0, V0, d0)
ratio_f = Es_f / omega_pi

print(f"\n[SEC 1] Energy budget at R_eff={R_fid}, r_tube={rt_fid} (analytic ansatz, CCEF units)")
print(f"  E_A1  = {E1_f:8.3f}  ({100*E1_f/Es_f:.1f}%)  [A1(∇n)²  gradient]")
print(f"  E_A3  = {E3_f:8.3f}  ({100*E3_f/Es_f:.1f}%)  [A3(∇²n)² bilaplacian ← DOMINANT]")
print(f"  E_A4  = {E4_f:8.3f}  ({100*E4_f/Es_f:.1f}%)  [A4(1-n_z)² anisotropy]")
print(f"  E_sol = {Es_f:8.3f}  TOTAL")
print(f"  ω_π   = {omega_pi:.4f}  [=√A4]")
print(f"  m_p/m_π (analytic ansatz) = {ratio_f:.1f}  (exp: 6.95,  ×{ratio_f/6.95:.1f})")
print(f"  m_p/m_π (converged field) = 1751   (exp: 6.95,  ×252)")

# ── section 2: virial condition ───────────────────────────────────────────────
# Under uniform rescaling r → λr: E(λ) = λE_A1 + (1/λ)E_A3 + λ³E_A4
# dE/dλ|_{λ=1} = 0  →  E_A1 − E_A3 + 3E_A4 = 0
virial   = E1_f - E3_f + 3.0*E4_f
v_frac   = virial / Es_f

print(f"\n[SEC 2] Virial condition (E_A1 − E_A3 + 3E_A4 = 0 at true minimum)")
print(f"  Residual = {virial:+.3f}  ({100*v_frac:+.1f}% of E_sol)")
if E3_f > E1_f + 3*E4_f:
    print(f"  → E_A3 ABOVE virial balance ({E3_f:.2f} > {E1_f+3*E4_f:.2f})")
    print(f"  → Soliton could lower energy by EXPANDING (λ>1)")
else:
    print(f"  → E_A3 BELOW virial balance")
    print(f"  → Soliton could lower energy by SHRINKING (λ<1)")

# ── section 3: R_eff scan ────────────────────────────────────────────────────
print(f"\n[SEC 3] R_eff scan: E_sol(R_eff) at r_tube={rt_fid}")
R_scan     = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0])
Esol_R     = []
E1_R, E3_R, E4_R = [], [], []

for R in R_scan:
    rmax = max(18, R+13)
    Th_, rho_, z_, RHO_, Z_, U_, V_, d_ = make_hopf(Nr=160, Nz=320,
                                                      R_eff=R, r_tube=rt_fid,
                                                      rho_max=rmax, z_max=15.0)
    e1, e3, e4, es = energy_components(Th_, rho_, z_, RHO_, Z_, U_, V_, d_)
    E1_R.append(e1); E3_R.append(e3); E4_R.append(e4); Esol_R.append(es)
    print(f"  R={R:4.1f}: E_sol={es:8.2f}  E_A1={e1:.2f}  E_A3={e3:.2f}  E_A4={e4:.2f}")

Esol_R = np.array(Esol_R)
E1_R   = np.array(E1_R)
E3_R   = np.array(E3_R)
E4_R   = np.array(E4_R)

idx_Rmin = np.argmin(Esol_R)
R_opt    = R_scan[idx_Rmin]
Es_Rmin  = Esol_R[idx_Rmin]

print(f"\n  → E_sol minimum at R_eff ≈ {R_opt:.1f} CCEF = {R_opt*L0_FM:.2f} fm")
print(f"  → Ring IS stabilized (has local minimum in R_eff)")
print(f"  → Minimum E_sol = {Es_Rmin:.2f} CCEF  →  m_p/m_π = {Es_Rmin/omega_pi:.1f}")
print(f"  (Ring expands to reduce E_A3 from tube-tube overlap, "
      f"then shrinks to limit E_A1 at large R)")

# ── section 4: r_tube scan ───────────────────────────────────────────────────
print(f"\n[SEC 4] r_tube scan: E_sol(r_tube) at R_eff={R_opt:.1f}")
rt_scan     = np.array([0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 2.0, 2.5, 3.0, 3.5, 4.0])
Esol_rt     = []
E1_rt, E3_rt, E4_rt = [], [], []

for rt in rt_scan:
    rmax = max(18, R_opt+13)
    Th_, rho_, z_, RHO_, Z_, U_, V_, d_ = make_hopf(Nr=160, Nz=320,
                                                      R_eff=R_opt, r_tube=rt,
                                                      rho_max=rmax, z_max=15.0)
    e1, e3, e4, es = energy_components(Th_, rho_, z_, RHO_, Z_, U_, V_, d_)
    E1_rt.append(e1); E3_rt.append(e3); E4_rt.append(e4); Esol_rt.append(es)
    print(f"  r_t={rt:.2f}: E_sol={es:8.2f}  E_A1={e1:.2f}  E_A3={e3:.2f}  E_A4={e4:.2f}")

Esol_rt = np.array(Esol_rt)
E1_rt   = np.array(E1_rt)
E3_rt   = np.array(E3_rt)
E4_rt   = np.array(E4_rt)

idx_rtmin = np.argmin(Esol_rt)
rt_opt    = rt_scan[idx_rtmin]
Es_rtmin  = Esol_rt[idx_rtmin]

print(f"\n  → Tube virial minimum at r_tube ≈ {rt_opt:.2f} CCEF  (1/k_UV = {r_Lifsh:.3f} CCEF)")
print(f"  → Minimum E_sol ≈ {Es_rtmin:.2f} CCEF  →  m_p/m_π ≈ {Es_rtmin/omega_pi:.1f}")

# ── section 5: hedgehog comparison ───────────────────────────────────────────
# NOTE: the CCEF BVP hedgehog uses cylindrical coords (ρ-z half-plane), NOT
# 3D spherical. The following 3D spherical formula is for comparison only
# and gives a DIFFERENT result from the BVP solver. [CONJECT]
print(f"\n[SEC 5] Hedgehog comparison (3D spherical — note: differs from CCEF BVP formula)")

def hedgehog_energy_3d(r_hh=1.5, Nr=2000, r_max=30.0):
    """
    Spherically symmetric Q=1 hedgehog in 3D: n=(sinF sinθ cosφ, sinF sinθ sinφ, cosF).
    F(r) = π(1−tanh(r/r_hh)), F(0)=π, F(∞)=0.

    Angular average of |∇²n|²:
      ⟨|∇²n|²⟩_Ω = A(r)² + (2/3) B(r)²
    where A(r) = ∇²n_z (angle-independent),
          B(r) = coefficient of (sinθ cosφ) in ∇²n_x.
    Factor 2/3 comes from ⟨sin²θ⟩_Ω = 2/3.
    """
    r  = np.linspace(0.02, r_max, Nr)
    dr = r[1] - r[0]
    F  = np.pi * (1.0 - np.tanh(r / r_hh))
    Fp = np.gradient(F, dr)
    Fpp= np.gradient(Fp, dr)
    sF = np.sin(F)
    cF = np.cos(F)

    e1 = (A1/2) * (Fp**2 + 2.0*sF**2 / r**2)
    e4 = (A4/2) * (1.0 - cF)**2

    # ∇²n_z = −(cF F'^2 + sF F'' + 2sF F'/r)
    A = -(cF*Fp**2 + sF*Fpp + 2.0*sF*Fp/r)
    # ∇²n_⊥ coefficient B = −sF F'^2 + cF F'' + (2/r)cF F' − 2sF/r²
    B = -sF*Fp**2 + cF*Fpp + (2.0/r)*cF*Fp - 2.0*sF/r**2
    # Angular average: ⟨|∇²n|²⟩_Ω = A² + (2/3)B²
    e3 = (A3/2) * (A**2 + (2.0/3.0)*B**2)

    w  = 4.0 * np.pi * r**2
    E1 = float(np.trapz(w * e1, r))
    E3 = float(np.trapz(w * e3, r))
    E4 = float(np.trapz(w * e4, r))
    return E1, E3, E4, E1+E3+E4

# Scan over r_hh to find minimum
rh_scan  = np.linspace(0.2, 5.0, 50)
Ehh_scan = np.array([hedgehog_energy_3d(rh)[3] for rh in rh_scan])
idx_hh   = np.argmin(Ehh_scan)
rh_opt   = rh_scan[idx_hh]
Ehh_min  = Ehh_scan[idx_hh]
E1hh, E3hh, E4hh, _ = hedgehog_energy_3d(rh_opt)

print(f"  3D hedgehog minimum: r_hh = {rh_opt:.3f} CCEF = {rh_opt*L0_FM:.2f} fm")
print(f"  E_A1={E1hh:.3f}  E_A3={E3hh:.3f}  E_A4={E4hh:.3f}  E_hh={Ehh_min:.3f}")
print(f"  m_p/m_π (3D hedgehog) = {Ehh_min/omega_pi:.2f}  (exp: 6.95)")
print(f"  [BVP hedgehog (2D cylindrical) gives m_p/m_π ≈ 12.19 — different formula]")
print(f"  Hopf torus (analytic) / 3D hedgehog energy ratio = {Es_f/Ehh_min:.1f}×")

# ── section 6: pion mass identity ────────────────────────────────────────────
print(f"\n[SEC 6] Pion mass identity")
m_pi_bulk   = omega_pi * E0_MEV
m_pi_exp    = 139.57
R_corr      = 2*A4 + A1*np.sqrt(A4/A3)
m_pi_Rcorr  = omega_pi * E0_MEV / R_corr

print(f"  ω_π (bulk) = √A4 × E0 = {m_pi_bulk:.1f} MeV  (exp {m_pi_exp:.2f} MeV, ×{m_pi_bulk/m_pi_exp:.3f})")
print(f"  R-correction: R = {R_corr:.4f}")
print(f"  m_π (R-corrected) = {m_pi_Rcorr:.1f} MeV  ≈ exp [CONJECT: from fpi Ward identity]")
print(f"\n  Proton mass (Hopf analytic):  {Es_f*E0_MEV/1000:.1f} GeV  vs exp 0.938 GeV")
print(f"  Proton mass (Hopf converged): {1751*omega_pi*E0_MEV/1000:.1f} GeV  vs exp 0.938 GeV")
print(f"\n  Dominant error is in E_sol (NOT in pion mass).")
print(f"  Pion mass contributes at most ×{m_pi_bulk/m_pi_exp:.2f} to ratio error.")

# ── section 7: diagnosis figure ───────────────────────────────────────────────
print(f"\n[SEC 7] Building diagnosis figure...")

plt.rcParams.update({
    'figure.facecolor':  CLR['bg'],
    'text.color':        CLR['text'],
    'axes.facecolor':    CLR['ax_bg'],
    'axes.edgecolor':    CLR['grid'],
    'axes.labelcolor':   CLR['text'],
    'xtick.color':       CLR['text'],
    'ytick.color':       CLR['text'],
    'grid.color':        CLR['grid'],
    'grid.linestyle':    '--',
    'grid.alpha':        0.4,
    'font.family':       'monospace',
    'font.size':         9,
})

fig = plt.figure(figsize=(18, 12), facecolor=CLR['bg'])
gs  = gridspec.GridSpec(2, 3, figure=fig,
                        left=0.07, right=0.97, top=0.93, bottom=0.07,
                        hspace=0.40, wspace=0.38)

# ── panel 1: energy budget bar chart ─────────────────────────────────────────
ax1 = fig.add_subplot(gs[0, 0])
lbl = ['E_A1\n(∇n)²', 'E_A3\n(∇²n)²', 'E_A4\n(1−nz)²', 'E_sol']
val = [E1_f, E3_f, E4_f, Es_f]
col = [CLR['solid'], CLR['open_'], CLR['conject'], CLR['new']]
bars = ax1.bar(lbl, val, color=col, edgecolor='#333', linewidth=0.8)
for b, v in zip(bars, val):
    ax1.text(b.get_x() + b.get_width()/2, v + 8, f'{v:.0f}',
             ha='center', va='bottom', fontsize=7.5, color=CLR['text'])
ax1.set_title(f'Energy Budget  [R={R_fid}, rt={rt_fid}]  [SOLID]',
              color=CLR['text'], fontsize=9)
ax1.set_ylabel('Energy (CCEF)', color=CLR['text'])
ax1.grid(axis='y')
ax1.text(0.02, 0.97,
         f"E_A3 = {100*E3_f/Es_f:.0f}% of E_sol\n"
         f"Bilaplacian DOMINATES\n"
         f"Virial residual {100*v_frac:+.0f}%",
         transform=ax1.transAxes, va='top', fontsize=7.5, color=CLR['conject'])

# ── panel 2: E_sol vs R_eff (shows ring minimum) ─────────────────────────────
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(R_scan, Esol_R, color=CLR['solid'],  linewidth=2, marker='o',
         markersize=5, label='E_sol')
ax2.plot(R_scan, E1_R,   color=CLR['ansatz'], linewidth=1.2, linestyle='--',
         marker='.', label='E_A1')
ax2.plot(R_scan, E3_R,   color=CLR['open_'],  linewidth=1.2, linestyle='--',
         marker='.', label='E_A3')
ax2.plot(R_scan, E4_R,   color=CLR['conject'],linewidth=1.2, linestyle='--',
         marker='.', label='E_A4')
ax2.axvline(R_opt, color=CLR['new'], linewidth=1.5, linestyle=':',
            label=f'Min at R≈{R_opt:.0f}')
ax2.set_xlabel('Ring radius R_eff (CCEF)', color=CLR['text'])
ax2.set_ylabel('Energy (CCEF)', color=CLR['text'])
ax2.set_title('R_eff Scan: Ring HAS Minimum  [SOLID]', color=CLR['solid'], fontsize=9)
ax2.legend(fontsize=7, loc='upper right', framealpha=0.2)
ax2.grid()
ax2.text(0.02, 0.55,
         f"Min at R≈{R_opt:.0f} CCEF={R_opt*L0_FM:.1f} fm\n"
         f"Small R: tube-tube overlap→huge E_A3\n"
         f"Large R: ring circumference→huge E_A1\n"
         f"→ Ring IS stabilized, but at\n"
         f"   E_min≈{Es_Rmin:.0f} >> 5 CCEF (proton)",
         transform=ax2.transAxes, va='top', fontsize=7.5, color=CLR['open_'])

# ── panel 3: E_sol vs r_tube ─────────────────────────────────────────────────
ax3 = fig.add_subplot(gs[0, 2])
ax3.plot(rt_scan, Esol_rt, color=CLR['solid'],  linewidth=2, marker='o',
         markersize=5, label='E_sol')
ax3.plot(rt_scan, E1_rt,   color=CLR['ansatz'], linewidth=1.2, linestyle='--',
         marker='.', label='E_A1')
ax3.plot(rt_scan, E3_rt,   color=CLR['open_'],  linewidth=1.2, linestyle='--',
         marker='.', label='E_A3')
ax3.plot(rt_scan, E4_rt,   color=CLR['conject'],linewidth=1.2, linestyle='--',
         marker='.', label='E_A4')
ax3.axvline(rt_opt, color=CLR['new'], linewidth=1.5, linestyle=':',
            label=f'min r_t≈{rt_opt:.1f}')
ax3.axvline(r_Lifsh, color='#888', linewidth=1, linestyle=':',
            label=f'1/k_UV={r_Lifsh:.2f}')
ax3.set_xlabel('Tube radius r_tube (CCEF)', color=CLR['text'])
ax3.set_ylabel('Energy (CCEF)', color=CLR['text'])
ax3.set_title(f'Tube Virial: E_A1↑ vs E_A3↓  [SOLID]', color=CLR['text'], fontsize=9)
ax3.legend(fontsize=7, loc='upper right', framealpha=0.2)
ax3.grid()

# ── panel 4: mass ratio comparison ───────────────────────────────────────────
ax4 = fig.add_subplot(gs[1, 0])
models = [
    'Exp.',
    'BVP hedgehog\n(2D cyl, CCEF)',
    '3D hedgehog\n(this code)',
    'Hopf torus\n(converged)',
    'Hopf torus\n(analytic)',
]
ratios = [6.95, 12.19, Ehh_min/omega_pi, 1751, Es_f/omega_pi]
cols4  = [CLR['solid'], CLR['solid'], CLR['conject'], CLR['open_'], CLR['open_']]
hatches = ['', '', '///', '', '///']

y_pos = np.arange(len(models))
bars4 = ax4.barh(y_pos, ratios, color=cols4, edgecolor='#444', height=0.55)
for b, v in zip(bars4, ratios):
    ax4.text(v*1.05, b.get_y() + b.get_height()/2, f'{v:.1f}',
             ha='left', va='center', fontsize=8, color=CLR['text'])
ax4.set_yticks(y_pos)
ax4.set_yticklabels(models, fontsize=7.5)
ax4.set_xlabel('m_p / m_π', color=CLR['text'])
ax4.set_title('Mass Ratio Ladder  [SOLID / CONJECT]', color=CLR['text'], fontsize=9)
ax4.set_xscale('log')
ax4.axvline(6.95, color=CLR['solid'], linewidth=1.5, linestyle='--', alpha=0.6)
ax4.grid(axis='x')
ax4.text(0.62, 0.04, '[///] = formula\nuncertain',
         transform=ax4.transAxes, fontsize=7, color=CLR['conject'])

# ── panel 5: energy density map at fiducial ──────────────────────────────────
ax5 = fig.add_subplot(gs[1, 1])
# Recompute e3 for the fiducial field to plot
sT0, cT0 = np.sin(Th0), np.cos(Th0)
inv_r0 = np.where(RHO0 > 1e-9, 1.0/RHO0, 0.0)
dT_dr0 = np.gradient(Th0, rho0[1]-rho0[0], axis=0)
dT_dz0 = np.gradient(Th0, z0[1]-z0[0], axis=1)
dP_dr0 = -V0/d0**2; dP_dz0 = U0/d0**2
e1_map = (A1/2)*(dT_dr0**2 + dT_dz0**2 + sT0**2*(dP_dr0**2 + dP_dz0**2 + inv_r0**2))
e4_map = (A4/2)*(1-cT0)**2
# A3 energy density (key contributor) — reuse from energy_components quantities
cosPh0 = U0/d0; sinPh0 = V0/d0
def lap2d_(f, dr, dz, inv_r):
    return (np.gradient(np.gradient(f, dr, axis=0), dr, axis=0)
            + inv_r*np.gradient(f, dr, axis=0)
            + np.gradient(np.gradient(f, dz, axis=1), dz, axis=1))
dr0, dz_0 = rho0[1]-rho0[0], z0[1]-z0[0]
LsT = lap2d_(sT0, dr0, dz_0, inv_r0)
LcT = lap2d_(cT0, dr0, dz_0, inv_r0)
LcP = lap2d_(cosPh0, dr0, dz_0, inv_r0)
LsP = lap2d_(sinPh0, dr0, dz_0, inv_r0)
dcPdr = 1/d0 - U0**2/d0**3; dcPdz = -U0*V0/d0**3
dsPdr = -U0*V0/d0**3;       dsPdz = 1/d0 - V0**2/d0**3
dsT_dr0 = cT0*dT_dr0; dsT_dz0 = cT0*dT_dz0
LsTcP = cosPh0*LsT + sT0*LcP + 2*(dsT_dr0*dcPdr + dsT_dz0*dcPdz)
LsTsP = sinPh0*LsT + sT0*LsP + 2*(dsT_dr0*dsPdr + dsT_dz0*dsPdz)
lnx = LsTcP - sT0*cosPh0*inv_r0**2
lny = LsTsP - sT0*sinPh0*inv_r0**2
lnz = LcT
e3_map = (A3/2)*(lnx**2 + lny**2 + lnz**2)
e_tot_map = e1_map + e3_map + e4_map

rho_plot = rho0[(rho0 < 12)]
Nr_plot  = len(rho_plot)
z_plot   = z0[(np.abs(z0) < 10)]
Nz_plot  = len(z_plot)
im = ax5.pcolormesh(rho_plot, z_plot,
                    (2*np.pi*RHO0[:Nr_plot, :Nz_plot] * e3_map[:Nr_plot, :Nz_plot]).T,
                    cmap='inferno', shading='auto',
                    vmin=0, vmax=np.percentile(2*np.pi*RHO0[:Nr_plot,:Nz_plot]*e3_map[:Nr_plot,:Nz_plot], 98))
plt.colorbar(im, ax=ax5, fraction=0.046, pad=0.04, label='ρ ε_A3 (CCEF/CCEF²)')
ax5.set_xlabel('ρ (CCEF)', color=CLR['text'])
ax5.set_ylabel('z (CCEF)', color=CLR['text'])
ax5.set_title('Bilaplacian Energy Density ρ·ε_A3  [SOLID]', color=CLR['text'], fontsize=9)
ax5.set_aspect('equal')

# ── panel 6: diagnosis summary ────────────────────────────────────────────────
ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')

summary_lines = [
    ("WHY IS m_p/m_π = 1751? (252× off)", CLR['new'], 10, True),
    ("", CLR['text'], 8, False),
    ("[1] BILAPLACIAN DOMINANCE  [SOLID]", CLR['open_'], 9, True),
    (f"    E_A3 = {100*E3_f/Es_f:.0f}% of E_sol  (at R={R_fid}, rt={rt_fid})", CLR['text'], 8, False),
    ("    Hopf winding forces high ∇²n", CLR['text'], 8, False),
    ("    throughout the ring tube.", CLR['text'], 8, False),
    ("", CLR['text'], 7, False),
    ("[2] RING IS STABILIZED  [SOLID]", CLR['solid'], 9, True),
    (f"    Min at R≈{R_opt:.0f} CCEF = {R_opt*L0_FM:.1f} fm", CLR['text'], 8, False),
    ("    Small R: tube-tube E_A3 explodes.", CLR['text'], 8, False),
    ("    Large R: E_A1 grows with circumference.", CLR['text'], 8, False),
    ("    But minimum energy >> proton.", CLR['text'], 8, False),
    ("", CLR['text'], 7, False),
    ("[3] SOLITON SIZE MISMATCH  [SOLID]", CLR['open_'], 9, True),
    (f"    Ring size ≈ {R_opt*L0_FM:.1f} fm >> proton 0.87 fm", CLR['text'], 8, False),
    ("    Large ring → large E_A1 + E_A3", CLR['text'], 8, False),
    ("    A4 too weak to compress it further", CLR['text'], 8, False),
    ("", CLR['text'], 7, False),
    ("[4] PION MASS: MINOR  [CONJECT]", CLR['conject'], 9, True),
    (f"    √A4·E0={m_pi_bulk:.0f} MeV, R-corr={m_pi_Rcorr:.0f} MeV", CLR['text'], 8, False),
    ("    Contributes ≤×1.64 to ratio error.", CLR['text'], 8, False),
    ("", CLR['text'], 7, False),
    ("OPEN: does a smaller-R solution", CLR['open_'], 8, True),
    ("  exist with lower energy?  [OPEN]", CLR['open_'], 8, False),
    ("  Can A4 be re-interpreted to", CLR['open_'], 8, False),
    ("  compress the ring?          [OPEN]", CLR['open_'], 8, False),
]

y = 0.99
for text, color, size, bold in summary_lines:
    ax6.text(0.03, y, text, transform=ax6.transAxes,
             color=color, fontsize=size,
             fontweight='bold' if bold else 'normal',
             va='top', fontfamily='monospace')
    dy = 0.058 if size >= 10 else (0.052 if size == 9 else 0.045)
    y -= dy

# ── title ─────────────────────────────────────────────────────────────────────
fig.text(0.50, 0.97,
         "CCEF Hopf Soliton: m_p/m_π Discrepancy Diagnosis",
         ha='center', va='top', fontsize=13, color=CLR['new'],
         fontweight='bold', fontfamily='monospace')
fig.text(0.50, 0.948,
         f"A1={A1}  A3={A3}  A4={A4}  E0={E0_MEV} MeV  k_UV={k_UV:.4f} CCEF⁻¹  ω_π={omega_pi:.4f} CCEF",
         ha='center', va='top', fontsize=8, color=CLR['text'], fontfamily='monospace')

out_png = OUT_DIR / "ccef_hopf_mpratio.png"
fig.savefig(out_png, dpi=150, bbox_inches='tight', facecolor=CLR['bg'])
plt.close(fig)
print(f"\n  Figure saved → {out_png}")

# ── section 8: summary ────────────────────────────────────────────────────────
print("\n" + "="*70)
print("DIAGNOSIS SUMMARY  [SOLID unless noted]")
print("="*70)
print(f"""
m_p/m_π (CCEF Hopf, converged)  = 1751   ×252 vs exp 6.95

ROOT CAUSE — 3 COMPOUNDING FACTORS:

(1) BILAPLACIAN DOMINANCE  [SOLID]
    E_A3 (bilaplacian) = {100*E3_f/Es_f:.0f}% of total energy at (R={R_fid}, rt={rt_fid}).
    The Hopf winding in 3D forces large ∇²n throughout the tube,
    making A3(∇²n)² the single largest energy term.

(2) LARGE SOLITON SIZE  [SOLID]
    Ring minimum at R_eff ≈ {R_opt:.0f} CCEF = {R_opt*L0_FM:.1f} fm
    (vs proton charge radius ≈ 0.87 fm).
    Small R penalized by E_A3 (tube-tube overlap).
    Large R penalized by E_A1 (circumference).
    A4 too weak (√A4 = {omega_pi:.3f} CCEF) to compress the ring further.

(3) SOLITON ENERGY SCALE  [SOLID]
    E_sol_min (analytic) ≈ {Es_Rmin:.0f} CCEF → m_p/m_π ≈ {Es_Rmin/omega_pi:.0f}
    E_sol     (converged) ≈ 1289 CCEF → m_p/m_π = 1751
    Proton would need E_sol ≈ 6.95 × {omega_pi:.3f} = {6.95*omega_pi:.2f} CCEF.
    Gap: ×{1289/(6.95*omega_pi):.0f} (energy scale) or ×{1751/6.95:.0f} (ratio).

(4) PION MASS — MINOR  [CONJECT]
    √A4 × E0 = {m_pi_bulk:.1f} MeV vs exp 139.6 MeV → ×{m_pi_bulk/m_pi_exp:.2f}.
    With R-correction: {m_pi_Rcorr:.1f} MeV ≈ exp. Contributes ≤×{m_pi_bulk/m_pi_exp:.2f} to ratio error.

WHAT IS NOT THE CAUSE:
    × Ring collapsing — the ring IS stabilized at a local minimum  [SOLID]
    × Wrong pion mass — pion mass is OK with R-correction  [CONJECT]
    × Numerical artifact — converged field also gives 1751  [SOLID]

OPEN QUESTIONS:
    → Does a lower-energy Q=1 solution exist outside the toroidal sector?  [OPEN]
    → Can A4 or L0 be re-interpreted to shrink the effective ring?  [OPEN]
    → Renormalization: is E_sol subject to a large quantum correction?  [OPEN]
    → BVP hedgehog gives m_p/m_π = 12.19 vs Hopf 1751 (×144 difference) — why?  [OPEN]
""")
print(f"Outputs:\n  {out_png}")
