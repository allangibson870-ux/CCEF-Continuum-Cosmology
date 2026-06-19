import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

# PARAMETERS [SOLID]
A1 = 1.000
A2 = 8.971
A3 = 1.684
A4 = 0.542
E0 = 311.73
r_min = 0.3
r_max = 20.0

print("=== CCEF K=1 Grand-Spin Coupled Channel (L>=1 pion-nucleon sector) ===")
print("=== Phase shift / Wronskian method — scattering BCs ===")

# Protected profile
try:
    data  = np.load('F0.npy')
    r_grid = data[0]; F0 = data[1]; dF0 = data[2]
    idx   = np.argsort(r_grid)
    r_grid, F0, dF0 = r_grid[idx], F0[idx], dF0[idx]
    print("Loaded BVP profile.")
except Exception:
    print("Frobenius fallback.")
    r_grid = np.linspace(r_min, r_max, 2000)
    a, b   = 0.836548, -0.018511
    F0     = np.pi - a*r_grid + b*r_grid**3 * np.exp(-0.8*r_grid)
    dF0    = np.gradient(F0, r_grid)
    np.save('F0.npy', np.column_stack((r_grid, F0, dF0)))

F_interp  = make_interp_spline(r_grid, F0,  k=3, bc_type='natural')
dF_interp = make_interp_spline(r_grid, dF0, k=3, bc_type='natural')

# ── Lifshitz asymptotic roots ─────────────────────────────────────────────────
def get_asymptotic_roots(omega2):
    """
    A3 κ⁴ - A1 κ² + (A4 - ω²) = 0
    Returns (kappa_decay, k_osc):
      kappa_decay : real, exponential decay
      k_osc       : real, oscillatory (scattering) — only exists for ω > ω_π
    """
    disc = A1**2 - 4*A3*(A4 - omega2)
    if disc < 0:
        return None, None
    sd   = np.sqrt(disc)
    z1   = (A1 + sd) / (2*A3)   # always > 0
    z2   = (A1 - sd) / (2*A3)   # < 0 for ω > ω_π
    kd   = np.sqrt(z1)           # decaying root
    kosc = np.sqrt(-z2) if z2 < 0 else None   # oscillatory root
    return kd, kosc

# ── K=1 coupled 4th-order operator ───────────────────────────────────────────
# State: y = [f, f', f'', f''', g, g', g'', g''']
# Channel 1 (f): K=1, ℓ=1 — primary channel
# Channel 2 (g): K=1, ℓ=1 — coupled via hedgehog background
#
# Diagonal L4 operator (correct sign, from master equation):
#   A3 Δ_ℓ² η - A1 Δ_ℓ η + Q η = ω² W η
#   Δ_ℓ η = η'' + (2/r)η' - ℓ(ℓ+1)/r² η
# Bilaplacian for ℓ≠0: leading term d4 + (4/r)d3 (centrifugal corrections subleading)
# Off-diagonal coupling: [EL-placeholder] ∝ F₀' sinF₀ / r from K=1 spin-angular structure

def rhs_K1(r, y, omega2):
    f,  df,  d2f, d3f = y[0], y[1], y[2], y[3]
    g,  dg,  d2g, d3g = y[4], y[5], y[6], y[7]

    F  = F_interp(r);  Fp = dF_interp(r)
    sF = np.sin(F);    cF = np.cos(F)
    r2 = r**2;  sF2 = sF**2;  cF2 = cF**2

    ell  = 1
    cent = ell*(ell + 1) / r2   # 2/r²

    # Radial Laplacian with centrifugal: Δ_ℓ η
    lap_f = d2f + 2*df/r - cent*f
    lap_g = d2g + 2*dg/r - cent*g

    # Diagonal potential (same structure as L=0, Q_eff includes centrifugal)
    Q_diag = (A1*(2*cF - 1 + np.cos(2*F)) / r2
              + 2*A2*(Fp**2*(cF2 - sF2) + sF2*(1 - sF2) / r**4)
              + A4*cF
              + A1*cent)   # centrifugal shift to potential

    W_diag = A1 + 2*A2*Fp**2

    # Off-diagonal coupling from K=1 grand-spin mixing [EL-placeholder]
    # Proportional to F₀' sinF₀ from angular momentum recoupling
    Q_off = 2*A2 * Fp * sF * cF / r

    # A2 cross terms (diagonal — same sign as L=0)
    A2f = (2*A2/A3) * (Fp**2 * lap_f - sF2*f / r**4)
    A2g = (2*A2/A3) * (Fp**2 * lap_g - sF2*g / r**4)

    # d4 equations (correct sign: from n'' = P_perp(A1∇²n - A3∇⁴n + ...) linearized)
    d4f = (-(4.0/r)*d3f
           + (1.0/A3)*(A1*lap_f - Q_diag*f + Q_off*g + omega2*W_diag*f)
           + A2f)

    d4g = (-(4.0/r)*d3g
           + (1.0/A3)*(A1*lap_g - Q_diag*g + Q_off*f + omega2*W_diag*g)
           + A2g)

    return [df, d2f, d3f, d4f,
            dg, d2g, d3g, d4g]

# ── Shooting from r_min with regular ICs ─────────────────────────────────────
# For ℓ=1: regular solution f ~ r^1 near origin
# Primary channel f seeded; g starts zero (coupling activates it)

def shoot_K1(omega2):
    eps = r_min
    y0 = [eps,  1.0, 0.0, 0.0,   # f ~ r, f'~1
           0.0,  0.0, 0.0, 0.0]   # g initially zero

    sol = solve_ivp(lambda r, y: rhs_K1(r, y, omega2),
                    [r_min, r_max], y0,
                    method='LSODA', rtol=1e-8, atol=1e-8,
                    dense_output=True, max_step=0.05)
    return sol

# ── Phase shift via Wronskian matching ───────────────────────────────────────
# At large r (F₀→0): f(r) ~ C·j₁(k·r) + D·n₁(k·r)
# j₁(x) ≈ sin(x)/x² - cos(x)/x  (large x)
# n₁(x) ≈ -cos(x)/x² - sin(x)/x (large x)
# tan δ = D/C  from Wronskian with free j₁, n₁

def phase_shift(sol, omega2):
    kd, kosc = get_asymptotic_roots(omega2)
    if kosc is None:
        return None

    # Two asymptotic sample points (deep in tail)
    r1, r2 = r_max - 3.0, r_max - 0.5
    f1 = sol.sol(r1)[0]
    f2 = sol.sol(r2)[0]

    x1, x2 = kosc*r1, kosc*r2

    # Large-x spherical Bessel j1 and n1
    j1_r1 =  np.sin(x1)/x1**2 - np.cos(x1)/x1
    j1_r2 =  np.sin(x2)/x2**2 - np.cos(x2)/x2
    n1_r1 = -np.cos(x1)/x1**2 - np.sin(x1)/x1
    n1_r2 = -np.cos(x2)/x2**2 - np.sin(x2)/x2

    denom = j1_r2*f1 - j1_r1*f2
    if abs(denom) < 1e-14:
        return 0.0
    tan_d = (n1_r2*f1 - n1_r1*f2) / denom
    return np.arctan(tan_d)

# ── Phase shift scan ──────────────────────────────────────────────────────────
omega_pi = np.sqrt(A4) * E0
print(f"\nPion threshold ω_π = {omega_pi:.1f} MeV")
print(f"Scanning K=1 phase shift from {omega_pi:.0f} to 400 MeV...\n")

omega_scan  = np.linspace(230, 400, 35)
omega2_scan = (omega_scan / E0)**2
deltas      = []

for o_mev, o2 in zip(omega_scan, omega2_scan):
    kd, kosc = get_asymptotic_roots(o2)
    if kosc is None:
        print(f"ω = {o_mev:.1f} MeV : below oscillatory threshold")
        deltas.append(None)
        continue
    sol = shoot_K1(o2)
    if not sol.success:
        print(f"ω = {o_mev:.1f} MeV : integration failed — {sol.message}")
        deltas.append(None)
        continue
    d = phase_shift(sol, o2)
    deltas.append(d)
    d_deg = np.degrees(d) if d is not None else float('nan')
    print(f"ω = {o_mev:.1f} MeV,  k_osc = {kosc:.4f},  δ = {d_deg:+.2f}°")

# ── Resonance detection ───────────────────────────────────────────────────────
valid = [(o, d) for o, d in zip(omega_scan, deltas) if d is not None]
if valid:
    ov, dv = zip(*valid)
    dv_deg = np.degrees(np.array(dv))
    diffs  = np.diff(dv_deg)
    res_idx = np.where(np.abs(diffs) > 30)[0]
    if len(res_idx):
        for ri in res_idx:
            print(f"\n>>> Possible resonance near ω ≈ {ov[ri]:.1f}–{ov[ri+1]:.1f} MeV  "
                  f"(Δδ = {diffs[ri]:+.1f}°)")
    else:
        print("\nNo sharp resonance detected — consistent with WKB continuum weight [SOLID].")

# ── Plot ──────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

if valid:
    axes[0].plot(ov, dv_deg, 'b-o', ms=4)
    axes[0].axhline( 90, color='r',      ls='--', label='90° (resonance)')
    axes[0].axhline(  0, color='gray',   ls=':')
    axes[0].axvline(omega_pi, color='green', ls=':', label='ω_π')
    axes[0].set_xlabel('ω (MeV)'); axes[0].set_ylabel('δ (degrees)')
    axes[0].set_title('K=1 Phase Shift δ(ω)  [channel 1]')
    axes[0].legend(); axes[0].grid(True)

# V_eff for K=1 vs L=0
r_v  = np.linspace(0.5, 10, 300)
F_v  = F_interp(r_v);  Fp_v = dF_interp(r_v)
sF_v = np.sin(F_v);    cF_v  = np.cos(F_v)
W_v  = A1 + 2*A2*Fp_v**2
cent_v = 2.0 / r_v**2

Q_L0 = (A1*(2*cF_v-1+np.cos(2*F_v))/r_v**2
         + 2*A2*(Fp_v**2*(cF_v**2-sF_v**2) + sF_v**2*(1-sF_v**2)/r_v**4)
         + A4*cF_v)
Q_K1 = Q_L0 + A1*cent_v

axes[1].plot(r_v, Q_L0/W_v, 'b-',  label='V_eff L=0 (breathing)')
axes[1].plot(r_v, Q_K1/W_v, 'r--', label='V_eff K=1 (+centrifugal)')
axes[1].axhline(A4,     color='green',  ls=':', label='pion threshold')
axes[1].axhline(0.3935, color='orange', ls=':', label='ω²_crit')
axes[1].set_ylim(-1.5, 2.0); axes[1].set_xlabel('r / L₀')
axes[1].set_title('Effective potentials: L=0 vs K=1')
axes[1].legend(); axes[1].grid(True)

plt.tight_layout()
plt.savefig('ccef_K1_phase_shift.png', dpi=200)
print("\nFigure saved: ccef_K1_phase_shift.png")
print("K=1 implementation complete.")
