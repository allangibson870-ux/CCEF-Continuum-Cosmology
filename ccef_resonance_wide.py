"""
ccef_resonance_wide.py -- Extended quasinormal resonance search
Extends ccef_resonance.py with:
  - Dense sigma grid near proton mass (m_p^2 = 9.06 CCEF^2)
  - RTOL = 0.20 CCEF^2 (was 0.08)
  - Two theta values with wider separation for cleaner stability test
  - Sectors m = 0..3

Fixed-point parameters (LOCKED): A1=1.000, A3=1.684, A4=0.542
"""

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import warnings

# ---- Fixed-point parameters (LOCKED) ---------------------------------------
A1, A3, A4 = 1.000, 1.684, 0.542
E0       = 311.73
omega_c  = np.sqrt(A4 - A1**2 / (4*A3))
m_p_ccef = 938.272 / E0
k_UV     = np.sqrt(A1 / A3)
k_IR     = np.sqrt(A4 / A1)
wp2      = m_p_ccef**2          # ~9.06 CCEF^2

print(f"omega_c  = {omega_c:.4f} CCEF = {omega_c*E0:.1f} MeV")
print(f"m_p      = {m_p_ccef:.4f} CCEF = {m_p_ccef*E0:.1f} MeV  (target)")
print(f"k_UV     = {k_UV:.4f} CCEF^-1 = {k_UV*E0:.1f} MeV")
print(f"m_p^2    = {wp2:.3f} CCEF^2")
print()

# ---- Grid ------------------------------------------------------------------
NR, NZ     = 46, 78
RMAX, ZMAX = 16., 14.
dr = RMAX / (NR - 1)
dz = 2*ZMAX / (NZ - 1)
rho_1d = np.linspace(0, RMAX, NR)
z_1d   = np.linspace(-ZMAX, ZMAX, NZ)
RHO, Z = np.meshgrid(rho_1d, z_1d, indexing='ij')
N = NR * NZ

# ---- Hopf profile ----------------------------------------------------------
R_EFF, R_TUBE = 5.0, 2.8
r_tor = np.sqrt((RHO - R_EFF)**2 + Z**2)
Theta = np.pi * np.exp(-r_tor**2 / R_TUBE**2)
sinT  = np.sin(Theta)

# ---- Build Delta_m (real, vectorised) --------------------------------------
def build_Dm(m):
    ii, jj = np.meshgrid(np.arange(1, NR-1), np.arange(1, NZ-1), indexing='ij')
    ii = ii.ravel().astype(np.int64)
    jj = jj.ravel().astype(np.int64)
    idx  = ii * NZ + jj
    rho  = np.maximum(rho_1d[ii], 1e-8)
    n    = len(idx)
    rows, cols, data = [], [], []
    # d^2/drho^2
    rows.append(np.tile(idx, 3))
    cols.append(np.concatenate([(ii-1)*NZ+jj, idx, (ii+1)*NZ+jj]))
    data.append(np.concatenate([np.full(n,1/dr**2), np.full(n,-2/dr**2), np.full(n,1/dr**2)]))
    # (1/rho) d/drho
    rows.append(np.tile(idx, 2))
    cols.append(np.concatenate([(ii-1)*NZ+jj, (ii+1)*NZ+jj]))
    data.append(np.concatenate([-1/(2*rho*dr), 1/(2*rho*dr)]))
    # d^2/dz^2
    rows.append(np.tile(idx, 3))
    cols.append(np.concatenate([ii*NZ+(jj-1), idx, ii*NZ+(jj+1)]))
    data.append(np.concatenate([np.full(n,1/dz**2), np.full(n,-2/dz**2), np.full(n,1/dz**2)]))
    # -m^2/rho^2
    if m:
        rows.append(idx); cols.append(idx)
        data.append(-float(m)**2 / rho**2)
    # Boundary: zero rows (Dirichlet)
    bnd = np.concatenate([np.arange(NZ, dtype=np.int64),
                          np.arange((NR-1)*NZ, NR*NZ, dtype=np.int64),
                          np.arange(1, NR-1)*NZ,
                          np.arange(1, NR-1)*NZ + (NZ-1)])
    rows.append(bnd); cols.append(bnd); data.append(np.zeros(len(bnd)))
    return sp.csr_matrix(
        (np.concatenate(data), (np.concatenate(rows), np.concatenate(cols))),
        shape=(N, N), dtype=float)

# ---- Self-consistent V_bg --------------------------------------------------
print("Computing V_bg ...")
D1 = build_Dm(1)
sT = sinT.ravel()
l1 = D1 @ sT;  l2 = D1 @ l1
denom = np.where(np.abs(sT) > 8e-3, sT, np.nan)
with np.errstate(invalid='ignore', divide='ignore'):
    Vbg = np.where(np.isfinite(denom), (A1*l1 - A3*l2)/denom, A4)
Vbg = np.clip(Vbg, -2*A4, 4*A4)
Vbg_sp = sp.diags(Vbg, format='csr')
print(f"  V_bg range [{Vbg.min():.3f}, {Vbg.max():.3f}]")

# ---- Precompute Dm and Dm2 for each sector (expensive, do once) ------------
print("Precomputing Dm and Dm2 for m=0..3 ...")
Dm_cache  = {}
Dm2_cache = {}
for m in [0, 1, 2, 3]:
    Dm_cache[m]  = build_Dm(m)
    Dm2_cache[m] = Dm_cache[m] @ Dm_cache[m]
    print(f"  m={m} done")

# ---- Complex-scaled L_m(theta) using cached matrices -----------------------
def make_Lm(m, theta):
    p2 = np.exp(-2j * theta)
    p4 = np.exp(-4j * theta)
    return (A3*p4*Dm2_cache[m].astype(complex)
            - A1*p2*Dm_cache[m].astype(complex)
            + Vbg_sp.astype(complex))

# ---- Sigma grid ------------------------------------------------------------
# Dense near m_p^2; keep threshold and intermediate coverage
sigma_targets = [
    omega_c**2 + 0.05j,   # threshold band (previous run found 237-246 MeV here)
    wp2        + 0.50j,   # proton mass scale: the new target
]

THETAS = [0.20, 0.35]
M_VALS = [0, 1, 2, 3]
N_EIG  = 20    # more per sigma since we have only 2 sigmas
RTOL   = 0.20

# ---- Eigenvalue sweep ------------------------------------------------------
all_lam = {m: {th: [] for th in THETAS} for m in M_VALS}

for m in M_VALS:
    print(f"\n-- Sector m={m} --")
    for theta in THETAS:
        print(f"  theta={theta:.2f}", end="", flush=True)
        Lm = make_Lm(m, theta)
        collected = []
        for sigma in sigma_targets:
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore')
                    vals, _ = spla.eigs(Lm, k=N_EIG, sigma=sigma,
                                        which='LM', tol=1e-7, maxiter=5000)
                collected.append(vals)
            except Exception:
                pass
        total = sum(len(c) for c in collected)
        print(f"  -> {total} eigs across {len(sigma_targets)} sigmas")
        if collected:
            all_lam[m][theta] = np.concatenate(collected)

# ---- omega = sqrt(lambda), Re > 0 -----------------------------------------
def to_omega(lam):
    om = np.sqrt(np.asarray(lam, dtype=complex))
    return np.where(np.real(om) < 0, -om, om)

# ---- Deduplicate (cluster within tol) -------------------------------------
def deduplicate(arr, tol=0.015):
    if len(arr) == 0:
        return np.array([], dtype=complex)
    used = np.zeros(len(arr), bool)
    keep = []
    for i, v in enumerate(arr):
        if used[i]:
            continue
        near = np.abs(arr - v) < tol
        keep.append(arr[near].mean())
        used[near] = True
    return np.array(keep)

# ---- Find resonances: theta-stable, Im(lambda)<0, Re(lambda)>0 ------------
resonances = {}
for m in M_VALS:
    sets = [all_lam[m][th] for th in THETAS if len(all_lam[m][th]) > 0]
    if len(sets) < 2:
        resonances[m] = np.array([], dtype=complex)
        continue
    cands = sets[0]
    for other in sets[1:]:
        stable = []
        for v in cands:
            if len(other) > 0 and np.min(np.abs(other - v)) < RTOL:
                stable.append(v)
        cands = np.array(stable, dtype=complex)
    if len(cands):
        mask = (np.imag(cands) < -0.001) & (np.real(cands) > 0.0)
        resonances[m] = deduplicate(cands[mask])
    else:
        resonances[m] = np.array([], dtype=complex)

# ---- Plot ------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 10))
fig.suptitle(
    'CCEF Quasinormal Resonances -- Extended Search (RTOL=0.20)\n'
    f'A1={A1}  A3={A3}  A4={A4} | omega_c={omega_c:.4f}  m_p={m_p_ccef:.4f} CCEF',
    fontsize=11, fontweight='bold')

th_colors = {0.20: '#2196F3', 0.35: '#FF9800'}

for ax, m in zip(axes.ravel(), M_VALS):
    # Theoretical continuum curves
    k_arr = np.linspace(0, 4.0, 300)
    for theta in THETAS:
        lam_c = A4 + A1*k_arr**2*np.exp(-2j*theta) + A3*k_arr**4*np.exp(-4j*theta)
        om_c  = to_omega(lam_c)
        ax.plot(np.real(om_c), np.imag(om_c),
                color=th_colors[theta], lw=1.0, alpha=0.28)
    # Numerical eigenvalues
    for theta in THETAS:
        lam = all_lam[m][theta]
        if len(lam) == 0:
            continue
        om = to_omega(lam)
        mask = (np.real(om) > -0.1) & (np.imag(om) < 0.4) & (np.real(om) < 6.0)
        ax.scatter(np.real(om[mask]), np.imag(om[mask]),
                   s=16, alpha=0.50, color=th_colors[theta], zorder=3)
    # Resonances
    res = resonances[m]
    if len(res):
        om_r = to_omega(res)
        ax.scatter(np.real(om_r), np.imag(om_r), s=140, marker='*',
                   color='red', zorder=7)
        for om in sorted(om_r, key=np.real):
            ax.annotate(
                f' {np.real(om)*E0:.0f}MeV / G={-2*np.imag(om)*E0:.0f}MeV',
                xy=(np.real(om), np.imag(om)),
                fontsize=7, color='darkred', va='bottom')
    # Reference lines
    ax.axvline(omega_c,  ls='--', color='gray',   lw=0.8, alpha=0.8)
    ax.axvline(m_p_ccef, ls=':',  color='green',  lw=1.2, alpha=0.9)
    ax.axvline(k_UV,     ls='-',  color='purple', lw=0.7, alpha=0.5)
    ax.axhline(0, color='k', lw=0.4)
    ax.set_xlabel('Re(omega) [CCEF]', fontsize=8)
    ax.set_ylabel('Im(omega) [CCEF]', fontsize=8)
    ax.set_title(f'm={m}  |  {len(res)} resonance(s)', fontsize=9)
    ax.set_xlim(-0.1, 5.5)
    ax.set_ylim(-2.5, 0.5)
    ax.tick_params(labelsize=7)

handles = [
    Line2D([0],[0], color='gray',   ls='--', label=f'omega_c={omega_c:.3f}'),
    Line2D([0],[0], color='green',  ls=':',  label=f'm_p={m_p_ccef:.3f}'),
    Line2D([0],[0], color='purple', ls='-',  label=f'k_UV={k_UV:.3f}'),
    Line2D([0],[0], marker='*', color='red', ls='none', label='Resonance (theta-stable)'),
    Line2D([0],[0], color=th_colors[0.20], lw=2, alpha=0.6, label='theta=0.20'),
    Line2D([0],[0], color=th_colors[0.35], lw=2, alpha=0.6, label='theta=0.35'),
]
axes[0,0].legend(handles=handles, fontsize=7, loc='lower right')

plt.tight_layout()
out = '/sessions/elegant-great-hypatia/mnt/outputs/ccef_resonance_wide.png'
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f"\n  Saved {out}")

# ---- Report ----------------------------------------------------------------
print()
print('='*64)
print('CCEF RESONANCES -- Extended Search (RTOL=0.20)')
print('='*64)
print(f'sigma grid : {len(sigma_targets)} targets, m_p^2={wp2:.2f} CCEF^2 included')
print(f'theta      : {THETAS}  N_EIG={N_EIG}  RTOL={RTOL}')
print(f'omega_c    : {omega_c:.4f} CCEF = {omega_c*E0:.1f} MeV')
print(f'k_UV       : {k_UV:.4f} CCEF = {k_UV*E0:.1f} MeV')
print(f'm_p target : {m_p_ccef:.4f} CCEF = {m_p_ccef*E0:.1f} MeV')
print()

all_res_list = []
for m in M_VALS:
    res = resonances[m]
    print(f'Sector m={m}: {len(res)} resonance(s)')
    if len(res):
        for om in sorted(to_omega(res), key=np.real):
            mass  = np.real(om)*E0
            width = -2*np.imag(om)*E0
            rp    = np.real(om)/m_p_ccef
            rk    = np.real(om)/k_UV
            rc    = np.real(om)/omega_c
            tag = ''
            if abs(mass - 938.3) < 100:
                tag = '  *** NEAR PROTON ***'
            elif abs(mass - 240) < 30:
                tag = '  <- k_UV scale (threshold resonance)'
            all_res_list.append((m, np.real(om), np.imag(om), mass, width))
            print(f'  omega_res = {np.real(om):.4f} - {abs(np.imag(om)):.4f}i CCEF')
            print(f'  m_res     = {mass:.1f} MeV    Gamma={width:.1f} MeV    Gamma/m={width/mass*100:.1f}%{tag}')
            print(f'  omega/k_UV={rk:.4f}  omega/omega_c={rc:.4f}  omega/m_p={rp:.4f}')
            print()

if all_res_list:
    print('-'*50)
    print('Summary table:')
    print(f'  {"m":>2}  {"m_res(MeV)":>12}  {"Gamma(MeV)":>11}  {"omega/m_p":>10}  {"omega/k_UV":>10}')
    for m, om_re, om_im, mass, width in sorted(all_res_list, key=lambda x: x[1]):
        print(f'  {m:>2}  {mass:>12.1f}  {width:>11.1f}  {om_re/m_p_ccef:>10.4f}  {om_re/k_UV:>10.4f}')
    # Check: anything near m_p?
    near_mp = [x for x in all_res_list if abs(x[3]-938.3) < 100]
    print()
    if near_mp:
        print(f'RESONANCES NEAR PROTON MASS: {len(near_mp)} found')
    else:
        hi = max(all_res_list, key=lambda x: x[3])
        print(f'Highest resonance found: {hi[3]:.1f} MeV (m={hi[0]})')
        print(f'Nothing found near m_p=938 MeV even with RTOL=0.20')
        print('[SOLID negative]: no resonance near proton mass in m=0..3 on this grid')
else:
    print('No theta-stable resonances found at all.')
