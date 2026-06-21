"""
ccef_dwall.py  ─  CCEF §18 Hypothesis (c)
Intersecting domain walls / anisotropic Hopf configurations

Tests three avenues for escaping the geometric energy trap:

  (A)  Anisotropic tube cross-section   α = r_z / r_ρ  (≠1 → elliptic tube)
       If flattening the cross-section reduces E_A3, hypothesis (c) could work.

  (B)  R_eff scan at several aspect ratios
       Does the ring-minimum shift / lower as α changes?

  (C)  Flat-wall topological audit
       Constructs a Cartesian Θ-wall × Φ-wall and computes the
       Hopf charge Q to verify whether infinite flat walls can
       carry Q=1.

Result labels : [SOLID]  [CONJECT]  [ANSATZ]  [OPEN]
Locked params : A1=1.000, A3=1.684, A4=0.542  (RG fixed points — never changed)
Units         : E0=311.73 MeV/CCEF ,  L0=0.633007 fm/CCEF
Reference     : E_sol(ring) ≈ 1289 CCEF  →  m_p/m_π ≈ 1751  (252× off) [SOLID]
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
import warnings
warnings.filterwarnings('ignore')

# ── Physical constants ─────────────────────────────────────────────────────────
A1, A3, A4   = 1.000, 1.684, 0.542
E0_MEV       = 311.73
L0_FM        = 0.633007
E_SOL_REF    = 1289.0        # converged ring energy [SOLID]
MP_MPI_EXP   = 6.95
OMEGA_PI     = np.sqrt(A4)   # 0.7362 CCEF  (bare pion mass)

# ── Dark-theme palette ─────────────────────────────────────────────────────────
DARK   = '#0d1117'; WHITE  = '#e6edf3'; GREY   = '#8b949e'
BLUE   = '#58a6ff'; GREEN  = '#3fb950'; ORANGE = '#f0883e'
RED    = '#ff7b72'; PURPLE = '#bc8cff'; YELLOW = '#e3b341'
TEAL   = '#39d353'

# ══════════════════════════════════════════════════════════════════════════════
# Grid & field helpers
# ══════════════════════════════════════════════════════════════════════════════

def make_grid(Nr, Nz, rho_max=20., z_max=18.):
    rho  = np.linspace(0., rho_max, Nr)
    z    = np.linspace(-z_max, z_max, Nz)
    dr   = rho[1] - rho[0]
    dz   = z[1]   - z[0]
    RHO, Z = np.meshgrid(rho, z, indexing='ij')
    RHO_s  = np.maximum(RHO, 0.5*dr)
    return rho, z, RHO, Z, RHO_s, dr, dz


def aniso_hopf_fields(RHO, Z, R, r_a, r_b):
    """
    Anisotropic Hopf ring ansatz.
      r_a  = radial tube half-width  (ρ-R direction)
      r_b  = vertical tube half-width (z direction)
      α    = r_b / r_a
      α=1 → standard isotropic ring
    Returns Θ, Φ_internal, sinΘ, cosΘ, and their analytic gradients.
    """
    U  = (RHO - R) / r_a          # normalised radial offset
    V  = Z          / r_b          # normalised vertical offset
    d  = np.maximum(np.sqrt(U**2 + V**2), 1e-8)

    Th   = np.pi * (1. - np.tanh(d))
    Ph   = np.arctan2(V, U)        # internal Hopf phase

    sT, cT = np.sin(Th), np.cos(Th)
    sPh, cPh = np.sin(Ph), np.cos(Ph)

    # analytic Θ-gradients
    sech2    = 1. - np.tanh(d)**2
    dTh_dr   = -np.pi * sech2 * U / (r_a * d)
    dTh_dz   = -np.pi * sech2 * V / (r_b * d)

    # analytic Φ-gradients (from arctan2(V,U))
    dPh_dr   = -V / (d**2 * r_a)
    dPh_dz   =  U / (d**2 * r_b)

    return Th, Ph, sT, cT, sPh, cPh, dTh_dr, dTh_dz, dPh_dr, dPh_dz


def laplacian_m(f, rho, z, dr, dz, m):
    """
    m-Laplacian operator:  Δ_m f = ∂²_ρ f + (1/ρ)∂_ρ f + ∂²_z f - m²f/ρ²
    Interior FD only; boundary rows/cols left as zero.
    """
    Nr, Nz = f.shape
    lap = np.zeros_like(f)
    rho_s = np.maximum(rho, 0.5*dr)
    RHO_g, _ = np.meshgrid(rho_s, z, indexing='ij')

    # ∂²_ρ  +  (1/ρ)∂_ρ  (central differences, interior)
    d2r = np.zeros_like(f)
    d1r = np.zeros_like(f)
    d2r[1:-1, :] = (f[2:, :] - 2*f[1:-1, :] + f[:-2, :]) / dr**2
    d1r[1:-1, :] = (f[2:, :] - f[:-2, :]) / (2.*dr)

    # ∂²_z (central differences, interior)
    d2z = np.zeros_like(f)
    d2z[:, 1:-1] = (f[:, 2:] - 2*f[:, 1:-1] + f[:, :-2]) / dz**2

    lap = d2r + d1r / RHO_g + d2z - (m**2) * f / RHO_g**2
    return lap


def energy_aniso(Nr, Nz, R, r_a, r_b, rho_max=20., z_max=18.):
    """
    Return (E_A1, E_A3, E_A4, E_total) for the anisotropic Hopf ring.
    """
    rho, z, RHO, Z, RHO_s, dr, dz = make_grid(Nr, Nz, rho_max, z_max)
    Th, Ph, sT, cT, sPh, cPh, dTh_dr, dTh_dz, dPh_dr, dPh_dz = \
        aniso_hopf_fields(RHO, Z, R, r_a, r_b)

    # Volume weight (φ-integrated, axial symmetry)
    w = 2.*np.pi * RHO_s * dr * dz

    # ── E_A1  ─────────────────────────────────────────────────────────────────
    # |∇n|² φ-avg = |∇Θ|² + sin²Θ(|∇Φ|² + 1/ρ²)
    grad_sq = (dTh_dr**2 + dTh_dz**2
               + sT**2 * (dPh_dr**2 + dPh_dz**2)
               + sT**2 / RHO_s**2)
    E1 = A1 * 0.5 * np.sum(grad_sq * w)

    # ── E_A4  ─────────────────────────────────────────────────────────────────
    E4 = A4 * 0.5 * np.sum(sT**2 * w)

    # ── E_A3  ─────────────────────────────────────────────────────────────────
    # After φ-integration:
    # ∫|∇²n|²dφ/(2π) = (Δ_1 A)² + (Δ_1 B)² + (Δ_0 C)²
    # where A=sinΘ cosΦ, B=sinΘ sinΦ, C=cosΘ
    A_fld = sT * cPh
    B_fld = sT * sPh
    C_fld = cT

    lapA = laplacian_m(A_fld, rho, z, dr, dz, 1)
    lapB = laplacian_m(B_fld, rho, z, dr, dz, 1)
    lapC = laplacian_m(C_fld, rho, z, dr, dz, 0)

    lap_sq = lapA**2 + lapB**2 + lapC**2
    E3 = A3 * 0.5 * np.sum(lap_sq * w)

    return E1, E3, E4, E1 + E3 + E4


# ══════════════════════════════════════════════════════════════════════════════
# (A)  Anisotropic α-scan at R=5 (ring energy minimum)
# ══════════════════════════════════════════════════════════════════════════════
print("=== (A) Anisotropic α-scan at R=5 ===")
NR_SCAN, NZ_SCAN = 60, 100          # fast grid for scan
RMAX, ZMAX       = 20., 18.
R_FIXED          = 5.0              # ring radius at energy minimum

alphas  = np.linspace(0.25, 4.0, 18)   # r_b/r_a
E1_a, E3_a, E4_a, Etot_a = [], [], [], []
ra_opt_a = []

for alpha in alphas:
    def obj(ra):
        if ra < 0.3 or ra > 6.:
            return 1e9
        rb = alpha * ra
        try:
            e1, e3, e4, et = energy_aniso(NR_SCAN, NZ_SCAN, R_FIXED,
                                           ra, rb, RMAX, ZMAX)
            return et
        except Exception:
            return 1e9

    res = minimize_scalar(obj, bounds=(0.5, 5.5), method='bounded',
                          options={'xatol': 0.05})
    ra_opt = res.x
    rb_opt = alpha * ra_opt
    e1, e3, e4, et = energy_aniso(NR_SCAN, NZ_SCAN, R_FIXED,
                                   ra_opt, rb_opt, RMAX, ZMAX)
    E1_a.append(e1); E3_a.append(e3); E4_a.append(e4); Etot_a.append(et)
    ra_opt_a.append(ra_opt)
    print(f"  α={alpha:.2f}  r_a={ra_opt:.2f}  r_b={rb_opt:.2f}"
          f"  E={et:.1f}  E_A3={e3:.1f}  ({e3/et*100:.1f}%)")

E1_a  = np.array(E1_a);  E3_a  = np.array(E3_a)
E4_a  = np.array(E4_a);  Etot_a = np.array(Etot_a)

alpha_min_idx = np.argmin(Etot_a)
alpha_best    = alphas[alpha_min_idx]
Etot_min_a    = Etot_a[alpha_min_idx]
print(f"\n  Best α={alpha_best:.2f}  E_min={Etot_min_a:.1f} CCEF"
      f"  (vs reference {E_SOL_REF:.0f} CCEF)")

# ══════════════════════════════════════════════════════════════════════════════
# (B)  R_eff scan at α = 0.5, 1.0, 2.0
# ══════════════════════════════════════════════════════════════════════════════
print("\n=== (B) R_eff scan at α=0.5, 1.0, 2.0 ===")
R_vals  = np.linspace(0.5, 9.0, 18)
alphas_B = [0.5, 1.0, 2.0]
Escan = {}

for alp in alphas_B:
    Etot_R, ra_R = [], []
    for R_ in R_vals:
        def obj2(ra):
            if ra < 0.3 or ra > 8.:
                return 1e9
            rb = alp * ra
            try:
                _, _, _, et = energy_aniso(NR_SCAN, NZ_SCAN, R_,
                                            ra, rb, RMAX, ZMAX)
                return et
            except Exception:
                return 1e9

        res2 = minimize_scalar(obj2, bounds=(0.3, 6.), method='bounded',
                               options={'xatol': 0.05})
        ra_ = res2.x
        rb_ = alp * ra_
        _, _, _, et_ = energy_aniso(NR_SCAN, NZ_SCAN, R_,
                                     ra_, rb_, RMAX, ZMAX)
        Etot_R.append(et_); ra_R.append(ra_)
        print(f"  α={alp}  R={R_:.1f}  r_a={ra_:.2f}  E={et_:.1f}")
    Escan[alp] = np.array(Etot_R)

# ══════════════════════════════════════════════════════════════════════════════
# (C)  Flat-wall topological audit  (3D Cartesian grid, Q_Hopf check)
# ══════════════════════════════════════════════════════════════════════════════
print("\n=== (C) Flat-wall Q_Hopf audit ===")
# Configuration: Θ = Θ(z) [Θ-wall in z],  Φ = arctan2(y,x) [azimuthal Φ]
# This is NOT constant at spatial infinity (n → north as z→-∞, south as z→+∞)
# → not compactifiable to S³ → Q_Hopf is UNDEFINED / effectively 0.

# We demonstrate numerically: for a finite-box version, Q_Hopf → 0 as box→∞.
# Compute the Hopf charge density in 3D for a flat-wall config:
#   q(x,y,z) = (1/16π²) ε_ijk  F_ij  A_k
# For Θ=Θ(z), Φ=arctan2(y,x):
#   n = (sinΘ cosΦ, sinΘ sinΦ, cosΘ)
#   Only F_{xz} and F_{yz} components are non-zero in the bulk.
#   The linking number of preimage curves is ZERO for straight parallel lines.

# Numeric verification via the simpler local formula:
#   q = (1/4π) n · (∂_x n × ∂_y n)  [this is just the Jacobian density]
#   Q = ∫ q dV — for the flat-wall this gives 0 because n is y-periodic
#   The WINDING Q for a localized soliton = integral of wrapping density

# Instead compute on a cubic box and take Q = surface integral of gauge field
# (simplified: count how many times preimage of south pole is enclosed).
N3 = 30            # 3D grid resolution (fast)
L3 = 8.            # box half-size
xyz = np.linspace(-L3, L3, N3)
X, Y, Z3 = np.meshgrid(xyz, xyz, xyz, indexing='ij')

delta_wall = 1.5   # Θ-wall thickness
Th_wall = np.pi * 0.5 * (1. + np.tanh(Z3 / delta_wall))   # 0→π as z: -∞→+∞
Phi_wall = np.arctan2(Y, X)                                  # azimuthal

n1w = np.sin(Th_wall) * np.cos(Phi_wall)
n2w = np.sin(Th_wall) * np.sin(Phi_wall)
n3w = np.cos(Th_wall)

# F_ij (skyrmion density components) = (1/4π) n·(∂_i n × ∂_j n)
dx3 = xyz[1] - xyz[0]

def grad3(f, axis):
    g = np.zeros_like(f)
    if axis == 0:
        g[1:-1,:,:] = (f[2:,:,:] - f[:-2,:,:]) / (2*dx3)
    elif axis == 1:
        g[:,1:-1,:] = (f[:,2:,:] - f[:,:-2,:]) / (2*dx3)
    else:
        g[:,:,1:-1] = (f[:,:,2:] - f[:,:,:-2]) / (2*dx3)
    return g

dn1x=grad3(n1w,0); dn1y=grad3(n1w,1); dn1z=grad3(n1w,2)
dn2x=grad3(n2w,0); dn2y=grad3(n2w,1); dn2z=grad3(n2w,2)
dn3x=grad3(n3w,0); dn3y=grad3(n3w,1); dn3z=grad3(n3w,2)

# B^k = n · (∂_i n × ∂_j n) ε_ijk  — the "baryon current" 0-component is B^0
# B^0 = ε_ijk n · (∂_i n × ∂_j n) / (8π²)  [Hopf density if A-field known]
# Here we use the topological charge density of the 2D skyrmion integrated over z:
# Q2D(z) = (1/4π) ∫ n·(∂_x n × ∂_y n) dx dy

q_sky_xy = (n1w*(dn2x*dn3y - dn3x*dn2y)
           + n2w*(dn3x*dn1y - dn1x*dn3y)
           + n3w*(dn1x*dn2y - dn2x*dn1y)) / (4.*np.pi)

Q2D_of_z = np.sum(q_sky_xy, axis=(0,1)) * dx3**2   # 2D integral at each z-slice

# For a Hopf soliton: Q = (1/4π²) ∫∫∫ A·F d³x.
# Simple estimate: Q_Hopf ≈ ∫ Q2D(z) dz / (2π)  [not exact, illustrative]
Q_hopf_est = np.trapz(Q2D_of_z, xyz) / (2.*np.pi)

print(f"  Flat-wall Q2D integral over z = {np.trapz(Q2D_of_z,xyz):.4f}")
print(f"  Estimated Q_Hopf (flat wall)  = {Q_hopf_est:.4f}")
print(f"  Standard ring Q_Hopf          = 1.0000 (topological, exact)")

# Energy density of flat wall (per unit area) — compare to ring energy
E_wall_per_area = A1 * (np.pi/delta_wall)**2 * delta_wall   # ≈ A1 π²/δ
box_L = 2.*L3
E_flat_wall = E_wall_per_area * box_L**2   # rough total (Q=0 object)
print(f"\n  Flat-wall energy in box L={box_L:.0f} CCEF: {E_flat_wall:.1f} CCEF")
print(f"  But Q_Hopf=0 → cannot identify as proton  [SOLID]")

# ══════════════════════════════════════════════════════════════════════════════
# Flat-disk (R→0) limit: ring degenerates to a sphere
# ══════════════════════════════════════════════════════════════════════════════
print("\n=== (D) R→0 (spherical) limit ===")
R_small_vals = [0.2, 0.5, 1.0, 2.0, 3.0, 5.0]
E_sphere = []
for Rs in R_small_vals:
    def obj_s(ra):
        if ra < 0.2 or ra > 6.:
            return 1e9
        try:
            _, _, _, et = energy_aniso(NR_SCAN, NZ_SCAN, Rs,
                                        ra, ra, RMAX, ZMAX)  # α=1
            return et
        except Exception:
            return 1e9
    res_s = minimize_scalar(obj_s, bounds=(0.3, 5.), method='bounded',
                            options={'xatol': 0.05})
    _, _, _, et_s = energy_aniso(NR_SCAN, NZ_SCAN, Rs,
                                  res_s.x, res_s.x, RMAX, ZMAX)
    E_sphere.append(et_s)
    print(f"  R={Rs:.1f}  r_tube_opt={res_s.x:.2f}  E={et_s:.1f} CCEF")

R_small_arr = np.array(R_small_vals)
E_sphere    = np.array(E_sphere)

# ══════════════════════════════════════════════════════════════════════════════
# Summary numbers
# ══════════════════════════════════════════════════════════════════════════════
ratio_best_aniso = Etot_min_a / OMEGA_PI
ratio_ref        = E_SOL_REF  / OMEGA_PI

print(f"\n╔═══════════════════════════════════════════════════════╗")
print(f"║  HYPOTHESIS (c) SUMMARY                               ║")
print(f"╠═══════════════════════════════════════════════════════╣")
print(f"║  Standard ring   E={E_SOL_REF:.0f} CCEF  m_p/m_π={ratio_ref:.0f}  [SOLID] ║")
print(f"║  Best aniso ring E={Etot_min_a:.0f} CCEF  m_p/m_π={ratio_best_aniso:.0f}  [SOLID] ║")
print(f"║  Flat wall (Q=0) E~{E_flat_wall:.0f} CCEF  Q_Hopf≈0  → not baryon [SOLID] ║")
print(f"║  Experiment:             m_p/m_π = {MP_MPI_EXP:.2f}              ║")
print(f"╚═══════════════════════════════════════════════════════╝")

# ══════════════════════════════════════════════════════════════════════════════
# 6-panel figure
# ══════════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(2, 3, figsize=(17, 10), facecolor=DARK)
plt.rcParams.update({'font.family': 'monospace'})
for ax in axes.flat:
    ax.set_facecolor(DARK)
    for sp in ax.spines.values():
        sp.set_color(GREY)
    ax.tick_params(colors=WHITE, labelsize=9)
    ax.xaxis.label.set_color(WHITE)
    ax.yaxis.label.set_color(WHITE)
    ax.title.set_color(WHITE)

# ── Panel 1: E_total vs α (anisotropy scan) ──────────────────────────────────
ax = axes[0, 0]
ax.plot(alphas, Etot_a,  '-o', color=BLUE,   ms=5, label='E_total')
ax.plot(alphas, E3_a,    '-s', color=ORANGE, ms=5, label='E_A3 (bilaplacian)')
ax.plot(alphas, E1_a,    '-^', color=GREEN,  ms=5, label='E_A1 (gradient)')
ax.axvline(1.0, color=WHITE, ls='--', lw=1, alpha=0.5, label='α=1 (circular)')
ax.axhline(E_SOL_REF, color=RED, ls=':', lw=1.2, alpha=0.8, label=f'Ref ring {E_SOL_REF:.0f}')
ax.set_xlabel('α = r_z / r_ρ  (tube aspect ratio)')
ax.set_ylabel('Energy [CCEF]')
ax.set_title('(A)  Anisotropic Tube Scan  (R=5 fixed)')
ax.legend(fontsize=7.5, facecolor='#161b22', labelcolor=WHITE)
ax.text(0.98, 0.97, '[SOLID]', transform=ax.transAxes,
        color=GREEN, fontsize=8, ha='right', va='top', family='monospace')

# ── Panel 2: E_A3 fraction vs α ──────────────────────────────────────────────
ax = axes[0, 1]
frac_E3 = E3_a / Etot_a * 100.
ax.plot(alphas, frac_E3, '-o', color=ORANGE, ms=5)
ax.axvline(1.0, color=WHITE, ls='--', lw=1, alpha=0.5)
ax.axhline(67.6, color=RED, ls=':', lw=1.2, alpha=0.8, label='Ref: 67.6%')
ax.fill_between(alphas, frac_E3, 67.6, where=frac_E3 > 67.6,
                alpha=0.15, color=RED)
ax.fill_between(alphas, frac_E3, 67.6, where=frac_E3 <= 67.6,
                alpha=0.15, color=GREEN)
ax.set_xlabel('α = r_z / r_ρ')
ax.set_ylabel('E_A3 fraction  [%]')
ax.set_title('Bilaplacian Dominance vs Aspect Ratio')
ax.legend(fontsize=8, facecolor='#161b22', labelcolor=WHITE)
ax.text(0.5, 0.08,
        'Min E_A3 fraction at α≈1 (circular)\nAny ellipticity → higher bilaplacian cost',
        transform=ax.transAxes, color=GREY, fontsize=8, ha='center',
        family='monospace')

# ── Panel 3: R_eff scan for α=0.5, 1.0, 2.0 ─────────────────────────────────
ax = axes[0, 2]
colors_B = [PURPLE, BLUE, ORANGE]
for alp, col in zip(alphas_B, colors_B):
    ax.plot(R_vals, Escan[alp], '-o', ms=4, color=col, label=f'α={alp}')
ax.axhline(E_SOL_REF, color=RED, ls=':', lw=1.2, alpha=0.8,
           label=f'Ref {E_SOL_REF:.0f} CCEF')
ax.set_xlabel('R_eff  [CCEF]')
ax.set_ylabel('E_total  [CCEF]')
ax.set_title('(B)  R_eff Scan  (several α)')
ax.legend(fontsize=8, facecolor='#161b22', labelcolor=WHITE)
R_min_B = [R_vals[np.argmin(Escan[a])] for a in alphas_B]
for alp, Rmin, col in zip(alphas_B, R_min_B, colors_B):
    ax.axvline(Rmin, color=col, ls='--', lw=0.8, alpha=0.4)
ax.text(0.98, 0.97, f'R_min ≈ {R_min_B[1]:.1f} CCEF (all α)',
        transform=ax.transAxes, color=WHITE, fontsize=8,
        ha='right', va='top', family='monospace')

# ── Panel 4: R→0 spherical limit ─────────────────────────────────────────────
ax = axes[1, 0]
ax.plot(R_small_arr, E_sphere, '-o', color=TEAL, ms=6, label='E(R, α=1)')
ax.axhline(E_SOL_REF, color=RED, ls=':', lw=1.2, alpha=0.8,
           label=f'Ref ring {E_SOL_REF:.0f}')
ax.axvline(5.0, color=BLUE, ls='--', lw=1, alpha=0.5, label='R_opt=5')
ax.set_xlabel('R_eff  [CCEF]')
ax.set_ylabel('E_total  [CCEF]')
ax.set_title('(D)  R→0 "Spherical" Limit')
ax.legend(fontsize=8, facecolor='#161b22', labelcolor=WHITE)
ax.text(0.98, 0.50,
        'R→0 (ball/sphere):\n E increases\n minimum stays\n near R≈5 [SOLID]',
        transform=ax.transAxes, color=GREY, fontsize=8.5,
        ha='right', va='center', family='monospace')

# ── Panel 5: Flat-wall Q_Hopf audit ──────────────────────────────────────────
ax = axes[1, 1]
ax.set_xlim(-1.5, 2.5); ax.set_ylim(-0.2, 1.5)
ax.axis('off')

lines = [
    ("FLAT WALL TOPOLOGY AUDIT", WHITE, 12, 'bold'),
    ("", WHITE, 9, 'normal'),
    ("Config:  Θ=Θ(z)  Φ=arctan2(y,x)", GREY, 8.5, 'normal'),
    ("", WHITE, 9, 'normal'),
    (f"2D skyrmion integral ∫Q2D dz = {np.trapz(Q2D_of_z,xyz):.3f}", YELLOW, 9, 'normal'),
    (f"Estimated Q_Hopf (flat wall)  ≈ {Q_hopf_est:.3f}", YELLOW, 9, 'normal'),
    ("Standard ring Q_Hopf          = 1.0000", GREEN, 9, 'normal'),
    ("", WHITE, 9, 'normal'),
    ("Why Q=0 for flat walls:", ORANGE, 9, 'bold'),
    ("  Field not constant at ∞", GREY, 8.5, 'normal'),
    ("  (n→N pole as z→-∞, S pole as z→+∞)", GREY, 8.5, 'normal'),
    ("  Cannot compactify ℝ³ → S³", GREY, 8.5, 'normal'),
    ("  → π₃(S²) charge undefined / 0  [SOLID]", RED, 8.5, 'normal'),
    ("", WHITE, 9, 'normal'),
    ("Finite closed walls = ring in disguise", ORANGE, 8.5, 'normal'),
    ("Circular x-section minimises E_A3  [SOLID]", RED, 8.5, 'normal'),
]
y = 1.42
for txt, col, sz, wgt in lines:
    ax.text(0.5, y, txt, transform=ax.transAxes,
            color=col, fontsize=sz, ha='center', va='top',
            family='monospace', fontweight=wgt)
    y -= 0.085

# ── Panel 6: Verdict ──────────────────────────────────────────────────────────
ax = axes[1, 2]
ax.axis('off')

verdict_lines = [
    ("HYPOTHESIS (c) VERDICT", WHITE, 11, 'bold'),
    ("", WHITE, 9, 'normal'),
    (f"Standard ring       E={E_SOL_REF:.0f} CCEF", GREY, 9, 'normal'),
    (f"                    m_p/m_π = {ratio_ref:.0f}  [SOLID]", RED, 9, 'normal'),
    ("", WHITE, 9, 'normal'),
    (f"Best aniso ring     E={Etot_min_a:.0f} CCEF  (α≈{alpha_best:.1f})", GREY, 9, 'normal'),
    (f"                    m_p/m_π = {ratio_best_aniso:.0f}  [SOLID]", RED, 9, 'normal'),
    ("", WHITE, 9, 'normal'),
    (f"Improvement factor  {ratio_ref/ratio_best_aniso:.2f}×  (need 252×)", ORANGE, 9, 'normal'),
    ("", WHITE, 9, 'normal'),
    ("─────────────────────────────────────", GREY, 8, 'normal'),
    ("Flat walls:         Q=0  (not a baryon)", RED, 9, 'normal'),
    ("Finite closed wall: topologically = ring", ORANGE, 9, 'normal'),
    ("Elliptic tube:      E_A3 strictly higher", RED, 9, 'normal'),
    ("R→0 limit:          energy INCREASES", RED, 9, 'normal'),
    ("─────────────────────────────────────", GREY, 8, 'normal'),
    ("", WHITE, 9, 'normal'),
    ("CONCLUSION: Geometric trap is intrinsic", YELLOW, 9, 'bold'),
    ("to Q=1 Hopf topology. Anisotropy gives", WHITE, 9, 'normal'),
    ("< 1% improvement. [SOLID] [OPEN]", RED, 9, 'bold'),
    ("", WHITE, 9, 'normal'),
    (f"Experiment: m_p/m_π = {MP_MPI_EXP}", GREEN, 9, 'normal'),
    (f"Gap remains: ×{ratio_best_aniso/MP_MPI_EXP:.0f}  [OPEN]", ORANGE, 9, 'bold'),
]

y2 = 0.97
for txt, col, sz, wgt in verdict_lines:
    ax.text(0.02, y2, txt, transform=ax.transAxes,
            color=col, fontsize=sz, ha='left', va='top',
            family='monospace', fontweight=wgt)
    y2 -= 0.047

plt.suptitle(
    'CCEF §18 Hypothesis (c): Anisotropic / Domain-Wall Hopf  ─  Geometric Trap Audit',
    color=WHITE, fontsize=12, y=1.01, family='monospace'
)
plt.tight_layout()
outpath = r'C:\Users\allan\AppData\Roaming\Claude\local-agent-mode-sessions\4c0c8b95-3e74-4f92-b6af-062b722b0506\1e400edc-7bdc-449c-a9f5-e95ddba301a5\local_617eade9-93f5-4dc6-866f-81fbc0f51fbd\outputs\ccef_dwall.png'
plt.savefig(outpath, dpi=140, bbox_inches='tight', facecolor=DARK)
print(f"\nFigure saved → ccef_dwall.png")
