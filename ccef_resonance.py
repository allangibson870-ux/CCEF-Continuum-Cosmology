"""
ccef_resonance.py — Complex scaling eigenproblem for L̂_m
Searches for quasinormal resonances of the Hopf soliton in CCEF.

Theory:
  Under uniform complex scaling  r → r e^{iθ}  the cylindrical Laplacian
  transforms exactly as  Δ_m → e^{-2iθ} Δ_m  (for a uniform dilation of
  both ρ and z).  The fluctuation operator becomes:

      L̂_m(θ) = A3 e^{-4iθ} Δ_m²  −  A1 e^{-2iθ} Δ_m  +  V_bg

  Eigenvalues λ = ω² split into three classes:
    · Bound states  : λ real, λ < ω_c²               (none — proven)
    · Continuum     : λ traces curve from A4 to ∞     (moves with θ)
    · Resonances    : isolated λ with Im(λ)<0,        θ-INDEPENDENT

  Physical resonance observables:
    m_res = Re(√λ_res) × E0     [MeV]
    Γ_res = −2 Im(√λ_res) × E0  [MeV]

Fixed-point parameters (LOCKED — never altered):
  A1=1.000, A3=1.684, A4=0.542, E0=311.73 MeV/CCEF
"""

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import warnings

# ── Fixed-point parameters (LOCKED) ─────────────────────────────────────────
A1, A3, A4 = 1.000, 1.684, 0.542
E0 = 311.73                          # MeV / CCEF
omega_c = np.sqrt(A4 - A1**2 / (4*A3))   # continuum threshold  = 0.6273 CCEF
m_p_ccef = 938.272 / E0             # proton mass in CCEF    = 3.010 CCEF

print(f"A1={A1}  A3={A3}  A4={A4}")
print(f"ω_c  = {omega_c:.4f} CCEF = {omega_c*E0:.1f} MeV")
print(f"m_p  = {m_p_ccef:.4f} CCEF = {m_p_ccef*E0:.1f} MeV")
print(f"Self-dual check: A1 = {A1:.4f}, A3×A4 = {A3*A4:.4f}  (diff {abs(A1-A3*A4)/A1*100:.1f}%)")
print()

# ── Grid (same as ccef_modeshapes to reuse intuition) ───────────────────────
NR, NZ     = 46, 78
RMAX, ZMAX = 16., 14.
dr = RMAX / (NR - 1)
dz = 2*ZMAX / (NZ - 1)
rho_1d = np.linspace(0, RMAX, NR)
z_1d   = np.linspace(-ZMAX, ZMAX, NZ)
RHO, Z = np.meshgrid(rho_1d, z_1d, indexing='ij')
N = NR * NZ

# ── Hopf soliton profile (toroidal Gaussian) ─────────────────────────────────
R_EFF, R_TUBE = 5.0, 2.8
r_tor = np.sqrt((RHO - R_EFF)**2 + Z**2)
Theta = np.pi * np.exp(-r_tor**2 / R_TUBE**2)
sinT  = np.sin(Theta)

# ── Build Δ_m (real, vectorised — no Python loops) ──────────────────────────
def build_Dm(m):
    """Cylindrical Laplacian  Δ_m = ∂²_ρ + (1/ρ)∂_ρ + ∂²_z − m²/ρ²
    with Dirichlet BC on all boundary cells."""
    ii, jj = np.meshgrid(np.arange(1, NR-1), np.arange(1, NZ-1), indexing='ij')
    ii = ii.ravel().astype(np.int64)
    jj = jj.ravel().astype(np.int64)
    idx  = ii * NZ + jj
    rho  = np.maximum(rho_1d[ii], 1e-8)
    n    = len(idx)
    rows, cols, data = [], [], []

    # ∂²/∂ρ²
    rows.append(np.tile(idx, 3))
    cols.append(np.concatenate([(ii-1)*NZ+jj, idx, (ii+1)*NZ+jj]))
    data.append(np.concatenate([np.full(n, 1/dr**2),
                                 np.full(n,-2/dr**2),
                                 np.full(n, 1/dr**2)]))
    # (1/ρ) ∂/∂ρ  (central difference)
    rows.append(np.tile(idx, 2))
    cols.append(np.concatenate([(ii-1)*NZ+jj, (ii+1)*NZ+jj]))
    data.append(np.concatenate([-1/(2*rho*dr), 1/(2*rho*dr)]))

    # ∂²/∂z²
    rows.append(np.tile(idx, 3))
    cols.append(np.concatenate([ii*NZ+(jj-1), idx, ii*NZ+(jj+1)]))
    data.append(np.concatenate([np.full(n, 1/dz**2),
                                 np.full(n,-2/dz**2),
                                 np.full(n, 1/dz**2)]))
    # −m²/ρ²
    if m:
        rows.append(idx); cols.append(idx)
        data.append(-float(m)**2 / rho**2)

    # Boundary rows → zero (Dirichlet)
    bnd = np.concatenate([
        np.arange(NZ, dtype=np.int64),
        np.arange((NR-1)*NZ, NR*NZ, dtype=np.int64),
        np.arange(1, NR-1, dtype=np.int64) * NZ,
        np.arange(1, NR-1, dtype=np.int64) * NZ + (NZ-1)
    ])
    rows.append(bnd); cols.append(bnd); data.append(np.zeros(len(bnd)))

    return sp.csr_matrix(
        (np.concatenate(data), (np.concatenate(rows), np.concatenate(cols))),
        shape=(N, N), dtype=float)

# ── Self-consistent V_bg from  L̂_1 sinΘ = 0 ────────────────────────────────
print("Computing V_bg ...")
D1    = build_Dm(1)
sT    = sinT.ravel()
l1    = D1 @ sT
l2    = D1 @ l1
denom = np.where(np.abs(sT) > 8e-3, sT, np.nan)
with np.errstate(invalid='ignore', divide='ignore'):
    Vbg = np.where(np.isfinite(denom), (A1*l1 - A3*l2) / denom, A4)
Vbg = np.clip(Vbg, -2*A4, 4*A4)
Vbg_sp = sp.diags(Vbg, format='csr')
print(f"  V_bg range: [{Vbg.min():.3f}, {Vbg.max():.3f}] CCEF  (A4={A4})")

# ── Complex-scaled operator ──────────────────────────────────────────────────
def make_Lm_complex(m, theta):
    """
    L̂_m(θ) = A3·e^{-4iθ}·Δ_m²  −  A1·e^{-2iθ}·Δ_m  +  V_bg

    V_bg kept real (valid because V_bg → A4 is short-ranged;
    the only analytic continuation needed is in the asymptotically flat region).
    """
    Dm  = build_Dm(m)
    Dm2 = Dm @ Dm
    p2  = np.exp(-2j * theta)
    p4  = np.exp(-4j * theta)
    return (A3 * p4 * Dm2.astype(complex)
            - A1 * p2 * Dm.astype(complex)
            + Vbg_sp.astype(complex))

# ── Eigenvalue sweep ─────────────────────────────────────────────────────────
# Use three θ values; resonances appear at the SAME λ regardless of θ.
# Continuum eigenvalues rotate as θ changes.
THETAS  = [0.15, 0.25, 0.35]
M_VALS  = [0, 1, 2, 3]
N_EIG   = 20      # eigenvalues per sigma per θ per m

# sigma targets: shift-invert so ARPACK finds eigenvalues nearest to sigma.
# Spread across threshold, intermediate, proton-mass, high-energy.
sigma_targets = [
    omega_c**2 + 0.05j,         # near continuum threshold
    1.0       + 0.20j,          # intermediate range
    m_p_ccef**2 + 0.50j,        # at proton mass scale  (~9.06 CCEF²)
    15.0      + 1.00j,          # above proton mass
]

# Storage: all_lam[m][theta] = array of complex eigenvalues λ
all_lam = {m: {th: [] for th in THETAS} for m in M_VALS}

for m in M_VALS:
    print(f"\n── Sector m = {m} ──")
    for theta in THETAS:
        print(f"  θ = {theta:.2f} rad")
        Lm = make_Lm_complex(m, theta)
        collected = []
        for sigma in sigma_targets:
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore')
                    vals, _ = spla.eigs(Lm, k=N_EIG, sigma=sigma,
                                        which='LM', tol=1e-7, maxiter=5000)
                collected.append(vals)
                print(f"    σ ≈ {sigma:.3f}:  {len(vals)} eigenvalues")
            except Exception as exc:
                print(f"    σ ≈ {sigma:.3f}:  FAILED ({exc})")
        if collected:
            all_lam[m][theta] = np.concatenate(collected)
        else:
            all_lam[m][theta] = np.array([], dtype=complex)

# ── Convert λ → ω (branch: Re(ω) ≥ 0) ──────────────────────────────────────
def lam_to_omega(lam):
    om = np.sqrt(np.asarray(lam, dtype=complex))
    return np.where(np.real(om) < 0, -om, om)

# ── Identify resonances: θ-stable eigenvalues with Im(λ) < 0 ────────────────
# A resonance must appear within RTOL in all three θ sweeps.
RTOL = 0.08   # CCEF² matching radius in λ-space

resonances = {}   # m → list of complex λ
for m in M_VALS:
    sets = [all_lam[m][th] for th in THETAS if len(all_lam[m][th]) > 0]
    if len(sets) < 2:
        resonances[m] = np.array([], dtype=complex)
        continue

    # Start from the first θ, then intersect with subsequent θ sets
    candidates = sets[0]
    for other in sets[1:]:
        stable = []
        for lam in candidates:
            if len(other) == 0: continue
            if np.min(np.abs(other - lam)) < RTOL:
                stable.append(lam)
        candidates = np.array(stable, dtype=complex)

    # Keep only those with Im(λ) < 0 (physical decaying resonances)
    # and Re(λ) > 0 (above the origin)
    if len(candidates) > 0:
        mask = (np.imag(candidates) < -0.001) & (np.real(candidates) > 0)
        resonances[m] = candidates[mask]
    else:
        resonances[m] = np.array([], dtype=complex)

# ── Plot: complex ω-plane for each sector ────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(
    'CCEF Quasinormal Resonances — Complex Scaling Method\n'
    f'A1={A1}  A3={A3}  A4={A4}  |  '
    f'ω_c={omega_c:.4f} CCEF  |  Grid {NR}×{NZ}',
    fontsize=11, fontweight='bold')

th_colors = {0.15: '#2196F3', 0.25: '#FF9800', 0.35: '#9C27B0'}

for ax, m in zip(axes.ravel(), M_VALS):
    # Draw continuum ray (asymptotic, large-k limit): arg(λ) = −4θ for each θ
    for theta in THETAS:
        # Manually trace the theoretical continuum curve λ(k)
        k_vals = np.linspace(0.0, 2.5, 200)
        lam_cont = (A4
                    + A1 * k_vals**2 * np.exp(-2j*theta)
                    + A3 * k_vals**4 * np.exp(-4j*theta))
        om_cont  = lam_to_omega(lam_cont)
        ax.plot(np.real(om_cont), np.imag(om_cont),
                color=th_colors[theta], lw=1.2, alpha=0.35,
                label=f'continuum θ={theta:.2f}' if m == 0 else '')

    # Scatter: all numerical eigenvalues for each θ
    for theta in THETAS:
        lam = all_lam[m][theta]
        if len(lam) == 0: continue
        om = lam_to_omega(lam)
        # Only plot in the physical quadrant / near-physical region
        mask = (np.real(om) >= -0.1) & (np.imag(om) <= 0.3)
        ax.scatter(np.real(om[mask]), np.imag(om[mask]),
                   s=22, alpha=0.65, color=th_colors[theta],
                   label=f'θ={theta:.2f}' if m == 0 else '',
                   zorder=3)

    # Highlight resonances
    res = resonances[m]
    n_res = len(res)
    if n_res > 0:
        om_res = lam_to_omega(res)
        ax.scatter(np.real(om_res), np.imag(om_res),
                   s=120, marker='*', color='red', zorder=6,
                   label=f'{n_res} resonance(s)' if m == 0 else '')
        for i, om in enumerate(sorted(om_res, key=np.real)):
            ax.annotate(
                f'  {np.real(om):.3f}−{abs(np.imag(om)):.3f}i',
                xy=(np.real(om), np.imag(om)),
                fontsize=7.5, va='center', color='darkred')

    # Reference verticals
    ax.axvline(omega_c, ls='--', color='gray', lw=0.9,
               alpha=0.8, label=f'ω_c={omega_c:.3f}' if m == 0 else '')
    ax.axvline(m_p_ccef, ls=':', color='green', lw=1.2,
               alpha=0.85, label=f'm_p={m_p_ccef:.3f}' if m == 0 else '')
    ax.axhline(0, color='k', lw=0.4)

    ax.set_xlabel('Re(ω)  [CCEF]', fontsize=9)
    ax.set_ylabel('Im(ω)  [CCEF]', fontsize=9)
    ax.set_title(f'Sector  m = {m}  |  {n_res} resonance(s) found', fontsize=10)
    ax.set_xlim(-0.2, max(5.0, m_p_ccef + 1.0))
    ax.set_ylim(-2.0, 0.5)
    ax.tick_params(labelsize=8)
    if m == 0:
        ax.legend(fontsize=7, loc='lower right', ncol=2)

plt.tight_layout()
out_png = '/sessions/elegant-great-hypatia/mnt/outputs/ccef_resonance.png'
plt.savefig(out_png, dpi=150, bbox_inches='tight')
plt.close()
print(f"\n✓  Saved {out_png}")

# ── Text report ───────────────────────────────────────────────────────────────
print()
print('='*62)
print('CCEF QUASINORMAL RESONANCES — Complex Scaling Report')
print('='*62)
print(f'Grid       : NR={NR}, NZ={NZ}, RMAX={RMAX}, ZMAX={ZMAX} CCEF')
print(f'θ values   : {THETAS}')
print(f'Stability  : |Δλ| < {RTOL} CCEF² across all θ, Im(λ)<0')
print(f'ω_c        : {omega_c:.4f} CCEF = {omega_c*E0:.2f} MeV')
print(f'm_p (expt) : {m_p_ccef:.4f} CCEF = {m_p_ccef*E0:.2f} MeV')
print(f'Self-dual  : A1={A1:.4f}, A3×A4={A3*A4:.4f}  (Δ={abs(A1-A3*A4)/A1*100:.1f}%)')
print()

any_found = False
for m in M_VALS:
    res  = resonances[m]
    n_r  = len(res)
    print(f'Sector m={m}:  {n_r} resonance(s)')
    if n_r > 0:
        any_found = True
        om_res = lam_to_omega(res)
        for k, om in enumerate(sorted(om_res, key=np.real)):
            mass  = np.real(om) * E0
            width = -2 * np.imag(om) * E0
            ratio_p = np.real(om) / m_p_ccef
            ratio_c = np.real(om) / omega_c
            tag = ''
            if abs(mass - 938.3) < 150:
                tag = '  ← NEAR PROTON MASS'
            elif abs(mass - 134.9) < 50:
                tag = '  ← NEAR PION MASS'
            elif abs(mass - 547.9) < 80:
                tag = '  ← NEAR ETA MASS'
            print(f'  [{k+1}] ω_res = {np.real(om):.4f} − {abs(np.imag(om)):.4f}i CCEF')
            print(f'       m_res = {mass:.1f} MeV    Γ = {width:.1f} MeV{tag}')
            print(f'       ω_res/ω_c = {ratio_c:.3f}    ω_res/m_p = {ratio_p:.4f}')

if not any_found:
    print()
    print('NO θ-stable resonances found in the searched region.')
    print('Possible reasons:')
    print('  · Resonances exist but lie outside the sigma search grid')
    print('  · V_bg potential too shallow to support quasi-bound states')
    print('  · Matching tolerance RTOL too tight — try relaxing to 0.15')
    print('  · Grid too coarse to resolve narrow resonances (large Γ)')

print()
print('Status: [OPEN] — first exploration of resonance spectrum')
print(f'Next:   widen sigma_targets or vary RTOL if no resonances found')
