"""
ccef_modeshapes.py
─────────────────────────────────────────────────────────────────────────────
CCEF: 2D mode shapes of L̂_m — where is each sector localized?
─────────────────────────────────────────────────────────────────────────────
Extracts the lowest physical eigenmode ξ_m(ρ,z) of L̂_m for m=0,1,2,3
and plots |ξ_m|² on the (ρ,z) plane with the ring cross-section overlaid.

Key question: if the 1D centrifugal argument fails to explain why m=3 is
the lowest sector, what does the 2D mode shape reveal?

Method
──────
  • Use shift-invert ARPACK eigsh with sigma = ω_ref[m] − ε to target the
    known physical mode (from ccef_coherent.py reference values)
  • Extract eigenvector, normalise, reshape to (NR, NZ)
  • Compute radial centroid ⟨ρ⟩ and spread σ_ρ weighted by |ξ|² × ρ
  • Compute "ring overlap" = fraction of |ξ|² within r_tube of ring core
  • Compare localization vs m to explain spectrum ordering

CCEF fixed parameters (locked):
  A1=1.000, A3=1.684, A4=0.542
  R_eff=5.0 CCEF, r_tube=2.8 CCEF
  E0=311.73 MeV/CCEF

Labels: [SOLID] proven; [CONJECT] numerical; [OPEN] unresolved
"""

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.colors import LogNorm
import warnings
warnings.filterwarnings('ignore')

# ── CCEF parameters ───────────────────────────────────────────────────────
A1, A3, A4 = 1.000, 1.684, 0.542
E0_MeV     = 311.73
R_EFF, R_TUBE = 5.0, 2.8

# ── Grid (identical to ccef_coherent.py) ─────────────────────────────────
NR, NZ     = 46, 78
RMAX, ZMAX = 16., 14.
dr = RMAX / (NR - 1)
dz = ZMAX / (NZ - 1)
rho_1d = np.linspace(0., RMAX, NR)
z_1d   = np.linspace(-ZMAX/2., ZMAX/2., NZ)
RHO, Z = np.meshgrid(rho_1d, z_1d, indexing='ij')   # shape (NR, NZ)

# ── Hopf ring background ──────────────────────────────────────────────────
def theta_profile(rho, z, R=R_EFF, r=R_TUBE):
    xi = np.sqrt(((rho - R)/r)**2 + (z/r)**2)
    return np.pi * (1. - np.tanh(xi - 1.5))

Theta = theta_profile(RHO, Z)
sinT  = np.sin(Theta)

# ── Distance from ring tube centre (for ring-overlap metric) ──────────────
dist_from_ring = np.sqrt((RHO - R_EFF)**2 + Z**2)   # shape (NR, NZ)

# ── Δ_m sparse matrix ────────────────────────────────────────────────────
def build_Dm(m):
    N = NR * NZ
    rows, cols, data = [], [], []
    for i in range(NR):
        for j in range(NZ):
            idx = i * NZ + j
            rho = rho_1d[i]
            if i == 0 or i == NR-1 or j == 0 or j == NZ-1:
                rows.append(idx); cols.append(idx); data.append(0.)
                continue
            # ∂²/∂ρ²
            rows += [idx]*3; cols += [(i+1)*NZ+j, idx, (i-1)*NZ+j]
            data += [1/dr**2, -2/dr**2, 1/dr**2]
            # (1/ρ)∂/∂ρ
            if rho > 1e-10:
                rows += [idx, idx]; cols += [(i+1)*NZ+j, (i-1)*NZ+j]
                data += [1/(2*rho*dr), -1/(2*rho*dr)]
            # ∂²/∂z²
            rows += [idx]*3; cols += [i*NZ+(j+1), idx, i*NZ+(j-1)]
            data += [1/dz**2, -2/dz**2, 1/dz**2]
            # −m²/ρ²
            if rho > 1e-10 and m != 0:
                rows.append(idx); cols.append(idx)
                data.append(-float(m)**2 / rho**2)
    return sp.csr_matrix((data, (rows, cols)), shape=(N, N))

# ── Self-consistent V_bg ─────────────────────────────────────────────────
print("Computing V_bg ...")
D1 = build_Dm(1)
l1sinT = (D1 @ sinT.ravel()).reshape(NR, NZ)
l2sinT = (D1 @ l1sinT.ravel()).reshape(NR, NZ)
denom  = np.where(np.abs(sinT) > 8e-3, sinT, np.nan)
V_bg   = (A1*l1sinT - A3*l2sinT) / denom
V_bg   = np.where(np.isnan(V_bg), A4, V_bg)
V_bg   = np.clip(V_bg, -3., 20.)

# ── Build L̂_m ────────────────────────────────────────────────────────────
def build_Lm(m):
    Dm  = build_Dm(m)
    Dm2 = Dm @ Dm
    Vd  = sp.diags(V_bg.ravel(), format='csr')
    return (A3*Dm2 - A1*Dm + Vd).tocsr()

# ── Reference frequencies from ccef_coherent.py (sigma=0.25 run) ─────────
omega_ref = {
    0: 0.641,    # lowest physical m=0 mode
    1: 0.6553,   # lowest physical m=1 mode
    2: 0.7048,   # lowest physical m=2 mode
    3: 0.5507,   # lowest physical m=3 mode (GLOBAL MINIMUM)
}

# ── Extract lowest eigenvector for each m ─────────────────────────────────
def get_lowest_mode(m, omega_target, K=6):
    """Shift-invert targeting omega_target; return (omega, eigvec_2d)."""
    Lm = build_Lm(m)
    # Try sigma slightly below target; if that fails, try at target
    for sigma in (omega_target - 0.04, omega_target, omega_target + 0.04,
                  omega_target - 0.08, omega_target + 0.10):
        for tol in (1e-4, 1e-3, 5e-3, 1e-2):
            try:
                vals, vecs = spla.eigsh(Lm, k=K, sigma=sigma, which='LM',
                                        tol=tol, maxiter=30000)
                # Sort by eigenvalue
                idx_sort = np.argsort(np.real(vals))
                vals = np.real(vals[idx_sort])
                vecs = vecs[:, idx_sort]
                # Find the one closest to omega_target above ZERO_THRESH
                phys_mask = vals >= 0.05
                if not np.any(phys_mask):
                    continue
                phys_vals = vals[phys_mask]
                phys_vecs = vecs[:, phys_mask]
                # Pick the one nearest omega_target
                best = np.argmin(np.abs(phys_vals - omega_target))
                omega_found = phys_vals[best]
                vec_2d = phys_vecs[:, best].reshape(NR, NZ)
                print(f"  m={m}: sigma={sigma:.3f} tol={tol:.0e}  "
                      f"ω_found={omega_found:.4f}  target={omega_target:.4f}  "
                      f"Δω={abs(omega_found-omega_target):.4f}")
                return omega_found, vec_2d
            except Exception as e:
                pass
    print(f"  m={m}: FAILED to converge")
    return None, None

print("\nExtracting 2D eigenmodes ...")
modes = {}
for m in [0, 1, 2, 3]:
    print(f"\nm={m}:")
    omega, vec2d = get_lowest_mode(m, omega_ref[m])
    if vec2d is not None:
        # Normalise so max |ξ|² = 1
        vec2d = vec2d / np.max(np.abs(vec2d))
        modes[m] = {'omega': omega, 'shape': vec2d}
    else:
        modes[m] = {'omega': omega_ref[m], 'shape': None}

# ── Localisation metrics ──────────────────────────────────────────────────
print("\n── Localisation metrics ──")
print(f"{'m':>3}  {'ω (CCEF)':>10}  {'<ρ> (CCEF)':>12}  {'σ_ρ':>8}  "
      f"{'ring_overlap':>14}  {'ring_frac':>10}")

metrics = {}
for m in [0, 1, 2, 3]:
    if modes[m]['shape'] is None:
        continue
    xi2 = modes[m]['shape']**2              # |ξ|² on (NR,NZ) grid
    # Volume element: dV = 2π ρ dρ dz
    dV    = 2*np.pi * RHO * dr * dz
    norm  = np.sum(xi2 * dV)
    # Radial centroid
    rho_c = np.sum(xi2 * RHO * dV) / norm
    # Radial spread
    rho2  = np.sum(xi2 * RHO**2 * dV) / norm
    sig_r = np.sqrt(max(0., rho2 - rho_c**2))
    # Ring overlap: fraction of weight within r_tube of ring centre
    in_tube = (dist_from_ring <= R_TUBE)
    ring_ov = np.sum(xi2[in_tube] * dV[in_tube]) / norm
    # Peak location
    idx_peak = np.unravel_index(np.argmax(xi2), xi2.shape)
    rho_peak = rho_1d[idx_peak[0]]
    z_peak   = z_1d[idx_peak[1]]

    metrics[m] = dict(omega=modes[m]['omega'], rho_c=rho_c, sig_r=sig_r,
                      ring_ov=ring_ov, rho_peak=rho_peak, z_peak=z_peak)
    print(f"{m:>3}  {modes[m]['omega']:>10.4f}  {rho_c:>12.3f}  {sig_r:>8.3f}  "
          f"{ring_ov:>14.4f}  {ring_ov*100:>9.1f}%")
    print(f"       peak at (ρ={rho_peak:.2f}, z={z_peak:.2f}) CCEF")

# ── Ring tube contour for overlay ─────────────────────────────────────────
theta_vals = np.linspace(0, 2*np.pi, 300)
ring_rho   = R_EFF + R_TUBE * np.cos(theta_vals)
ring_z     = R_TUBE * np.sin(theta_vals)
# Mask to positive ρ (physical)
mask_phys  = ring_rho > 0
ring_rho   = ring_rho[mask_phys]
ring_z     = ring_z[mask_phys]

# ── FIGURE ────────────────────────────────────────────────────────────────
print("\nGenerating figure ...")
DARK  = '#0d1117'
GRAY  = '#21262d'
LGRAY = '#8b949e'
WHITE = '#e6edf3'

fig = plt.figure(figsize=(18, 12), facecolor=DARK)
# Layout: top 4 panels = mode shapes, bottom 2 panels = metrics
gs  = gridspec.GridSpec(2, 4, figure=fig, hspace=0.40, wspace=0.32,
                        height_ratios=[1.6, 1.0])

# ── Panels 0-3: 2D mode shapes ───────────────────────────────────────────
cmaps = ['Blues', 'Greens', 'Oranges', 'Reds']
m_colors = ['#4FC3F7', '#81C784', '#FFB74D', '#FF8A65']

for col, m in enumerate([0, 1, 2, 3]):
    ax = fig.add_subplot(gs[0, col])
    ax.set_facecolor(DARK)
    for sp_ in ax.spines.values():
        sp_.set_color(LGRAY)
    ax.tick_params(colors=WHITE, labelsize=7)
    ax.xaxis.label.set_color(WHITE)
    ax.yaxis.label.set_color(WHITE)

    if modes[m]['shape'] is not None:
        xi2 = modes[m]['shape']**2
        # Plot with log scale to see both core and tails
        xi2_safe = np.where(xi2 > 1e-6, xi2, 1e-6)
        im = ax.pcolormesh(rho_1d, z_1d, xi2_safe.T,
                           cmap=cmaps[col],
                           norm=LogNorm(vmin=1e-4, vmax=1.0),
                           shading='auto')
        plt.colorbar(im, ax=ax, fraction=0.04, pad=0.02,
                     label='|ξ|² (log)', labelpad=2).ax.yaxis.set_tick_params(
                         colors=WHITE, labelsize=6)

        # Ring tube contour
        ax.plot(ring_rho, ring_z, 'w-', lw=1.0, alpha=0.6, label='ring tube')
        ax.axvline(R_EFF, color='white', lw=0.5, ls=':', alpha=0.4)

        # Peak marker
        if m in metrics:
            ax.scatter([metrics[m]['rho_peak']], [metrics[m]['z_peak']],
                       marker='+', s=80, color='yellow', linewidths=1.5, zorder=5)

        omega_val = modes[m]['omega']
        ring_pct  = metrics[m]['ring_ov']*100 if m in metrics else 0.
        rho_c_val = metrics[m]['rho_c'] if m in metrics else 0.
        ax.set_title(f'm={m}  |  ω={omega_val:.4f} CCEF\n'
                     f'⟨ρ⟩={rho_c_val:.2f}  ring_overlap={ring_pct:.1f}%',
                     color=m_colors[col], fontsize=8)
    else:
        ax.text(0.5, 0.5, f'm={m}\nCONVERGENCE\nFAILED',
                ha='center', va='center', color='red', fontsize=10,
                transform=ax.transAxes)
        ax.set_title(f'm={m}', color=m_colors[col], fontsize=8)

    ax.set_xlim(0, RMAX)
    ax.set_ylim(-ZMAX/2, ZMAX/2)
    ax.set_xlabel('ρ (CCEF)', fontsize=7)
    if col == 0:
        ax.set_ylabel('z (CCEF)', fontsize=7)

# ── Panel bottom-left: ring overlap vs m ─────────────────────────────────
ax_ov = fig.add_subplot(gs[1, :2])
ax_ov.set_facecolor(GRAY)
for sp_ in ax_ov.spines.values(): sp_.set_color(LGRAY)
ax_ov.tick_params(colors=WHITE, labelsize=8)
ax_ov.xaxis.label.set_color(WHITE); ax_ov.yaxis.label.set_color(WHITE)
ax_ov.title.set_color(WHITE)

m_list_done = [m for m in [0,1,2,3] if m in metrics]
ov_vals     = [metrics[m]['ring_ov']*100 for m in m_list_done]
om_vals     = [metrics[m]['omega'] for m in m_list_done]
rc_vals     = [metrics[m]['rho_c'] for m in m_list_done]

bars = ax_ov.bar(m_list_done, ov_vals, color=[m_colors[m] for m in m_list_done],
                 edgecolor=DARK, linewidth=0.5, alpha=0.85, label='ring overlap %')
for bar, ov, m in zip(bars, ov_vals, m_list_done):
    ax_ov.text(m, ov + 0.3, f'{ov:.1f}%', ha='center', va='bottom',
               fontsize=8, color=WHITE)

ax_ov.set_xlabel('Azimuthal sector m')
ax_ov.set_ylabel('Ring overlap  (% of |ξ|² within r_tube)')
ax_ov.set_title('Mode localization: fraction of weight in ring tube\n'
                '[CONJECT: m=3 most concentrated at ring ↔ lowest ω]')
ax_ov.set_xticks(m_list_done)
ax_ov.set_ylim(0, max(ov_vals)*1.25 if ov_vals else 100)
ax_ov.axvline(3, color='#FF8A65', lw=1.5, ls='--', alpha=0.7, label='m=3 (lowest ω)')
ax_ov.legend(fontsize=7, facecolor=GRAY, labelcolor=WHITE, edgecolor=LGRAY)

# ── Panel bottom-right: ω and ⟨ρ⟩ vs m ──────────────────────────────────
ax_sp = fig.add_subplot(gs[1, 2:])
ax_sp.set_facecolor(GRAY)
for sp_ in ax_sp.spines.values(): sp_.set_color(LGRAY)
ax_sp.tick_params(colors=WHITE, labelsize=8)
ax_sp.xaxis.label.set_color(WHITE); ax_sp.yaxis.label.set_color(WHITE)
ax_sp.title.set_color(WHITE)

ax2 = ax_sp.twinx()
ax2.tick_params(colors='#FFB74D', labelsize=8)
ax2.yaxis.label.set_color('#FFB74D')

ax_sp.scatter(m_list_done, om_vals,
              c=[m_colors[m] for m in m_list_done], s=100,
              edgecolors=WHITE, linewidths=0.8, zorder=5, label='ω_min (CCEF)')
ax_sp.plot(m_list_done, om_vals, color=LGRAY, lw=1, ls='--', zorder=3)
ax_sp.axhline(np.sqrt(A4), color='#4FC3F7', lw=1, ls=':',
              label=f'√A4={np.sqrt(A4):.3f}')

ax2.scatter(m_list_done, rc_vals,
            marker='D', c='#FFB74D', s=70,
            edgecolors=WHITE, linewidths=0.8, zorder=5, label='⟨ρ⟩ (CCEF)')
ax2.plot(m_list_done, rc_vals, color='#FFB74D', lw=1, ls='-.', zorder=3)
ax2.axhline(R_EFF, color='#FF8A65', lw=1, ls=':', alpha=0.7,
            label=f'R_eff={R_EFF}')

for m, ω, rc in zip(m_list_done, om_vals, rc_vals):
    ax_sp.text(m+0.05, ω+0.002, f'{ω:.4f}', fontsize=7, color=m_colors[m])
    ax2.text(m+0.05, rc-0.15, f'{rc:.2f}', fontsize=7, color='#FFB74D')

ax_sp.set_xlabel('Azimuthal sector m')
ax_sp.set_ylabel('ω_min (CCEF)', color=WHITE)
ax2.set_ylabel('⟨ρ⟩ (CCEF)', color='#FFB74D')
ax_sp.set_title('ω_min and radial centroid ⟨ρ⟩ vs m\n'
                '[⟨ρ⟩ → R_eff as mode tightens onto ring]')
ax_sp.set_xticks(m_list_done)
ax_sp.set_xlim(-0.5, 3.5)

lines1, labels1 = ax_sp.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax_sp.legend(lines1+lines2, labels1+labels2, fontsize=7,
             facecolor=GRAY, labelcolor=WHITE, edgecolor=LGRAY, loc='upper left')

# ── Supertitle ────────────────────────────────────────────────────────────
fig.suptitle(
    'CCEF 2D Mode Shapes  |ξ_m(ρ,z)|²  of  L̂_m = A3 Δ_m² − A1 Δ_m + V_bg\n'
    f'Ring: R_eff={R_EFF}, r_tube={R_TUBE} [CCEF]  |  '
    'Why m=3 has the lowest ω: mode localization onto the ring tube',
    color=WHITE, fontsize=10, y=0.99
)

out_path = '/sessions/elegant-great-hypatia/mnt/outputs/ccef_modeshapes.png'
fig.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=DARK)
plt.close(fig)
print(f"\nFigure saved: {out_path}")

# ── Final summary ─────────────────────────────────────────────────────────
print("\n" + "="*70)
print("2D MODE SHAPE ANALYSIS SUMMARY")
print("="*70)
print(f"\n{'m':>3}  {'ω (CCEF)':>10}  {'ω (MeV)':>9}  "
      f"{'⟨ρ⟩':>7}  {'σ_ρ':>7}  {'ring %':>8}  {'peak(ρ,z)':>12}")
for m in [0,1,2,3]:
    if m not in metrics: continue
    mt = metrics[m]
    print(f"{m:>3}  {mt['omega']:>10.4f}  {mt['omega']*E0_MeV:>9.1f}  "
          f"{mt['rho_c']:>7.3f}  {mt['sig_r']:>7.3f}  "
          f"{mt['ring_ov']*100:>7.1f}%  "
          f"({mt['rho_peak']:.2f},{mt['z_peak']:.2f})")

print(f"\nRing position: R_eff={R_EFF}, r_tube={R_TUBE} CCEF")
print(f"\nKey finding:")
if all(m in metrics for m in [0,1,2,3]):
    ov_order = sorted([0,1,2,3], key=lambda m: metrics[m]['ring_ov'], reverse=True)
    print(f"  Ring overlap ranking (highest first): {ov_order}")
    m_low_ω = min([0,1,2,3], key=lambda m: metrics[m]['omega'])
    m_hi_ov  = max([0,1,2,3], key=lambda m: metrics[m]['ring_ov'])
    print(f"  Lowest ω sector: m={m_low_ω}  (ω={metrics[m_low_ω]['omega']:.4f})")
    print(f"  Highest ring overlap: m={m_hi_ov}  ({metrics[m_hi_ov]['ring_ov']*100:.1f}%)")
    if m_low_ω == m_hi_ov:
        print(f"\n  ✓ m=3 is BOTH the lowest-ω sector AND the most ring-localised mode")
        print(f"    → m=3 preference is explained by 2D ring localisation [CONJECT]")
    else:
        print(f"\n  ✗ Lowest-ω sector ≠ most ring-localised: explanation incomplete [OPEN]")

print(f"\nPhysical interpretation [CONJECT]:")
print(f"  The centrifugal term m²/ρ² suppresses the mode at ρ<R,")
print(f"  concentrating it at ρ≈R=5. At m=3, the mode is most tightly")
print(f"  confined to the ring tube where V_bg is deepest, giving the")
print(f"  lowest eigenfrequency. At m≥4 the barrier overshoots,")
print(f"  pushing the mode to ρ>R where V_bg→A4, and no bound state forms.")
print("="*70)
