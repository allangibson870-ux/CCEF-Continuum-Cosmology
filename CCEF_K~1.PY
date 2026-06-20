import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

# ── Parameters [SOLID] ────────────────────────────────────────────────────────
A1 = 1.000; A2 = 8.971; A3 = 1.684; A4 = 0.542; E0 = 311.73

r_min = 0.3
r_max = 35.0

print("=== CCEF K=1 L4 Bound-State BVP (A3-corrected, grand-spin K=1, ell=1) ===")
print(f"Domain: [{r_min}, {r_max}]  L0 units")
print(f"Threshold: omega^2_pi = A4 = {A4}")
print(f"Search range: 0 < omega^2 < {A4}")

# ── Soliton background ────────────────────────────────────────────────────────
# Load F0.npy; clip F0 >= 0 (Frobenius approx goes negative for r > 3.7;
# true profile decays to zero). Extend grid to r_max with zero tail.
try:
    data = np.load('/sessions/eager-dreamy-hopper/mnt/outputs/F0.npy')
    r_npy = data[0]; F_npy = data[1]; dF_npy = data[2]
    idx = np.argsort(r_npy)
    r_npy, F_npy, dF_npy = r_npy[idx], F_npy[idx], dF_npy[idx]
    # Clip: F0 should decay to 0, not go negative
    F_npy  = np.maximum(F_npy,  0.0)
    dF_npy = np.gradient(F_npy, r_npy)   # recompute dF after clip
    # Zero-tail extension to r_max
    r_tail  = np.linspace(r_npy[-1] + 1.0, r_max + 5.0, 12)
    r_grid  = np.concatenate([r_npy,  r_tail])
    F_grid  = np.concatenate([F_npy,  np.zeros(len(r_tail))])
    dF_grid = np.concatenate([dF_npy, np.zeros(len(r_tail))])
    print(f"Loaded F0.npy (clipped F>=0) + zero tail. r: {r_grid[0]:.1f}–{r_grid[-1]:.1f}")
except Exception as ex:
    print(f"Frobenius fallback ({ex}).")
    r_grid = np.linspace(r_min, r_max + 5.0, 4000)
    a, b   = 0.836548, -0.018511
    F_grid  = np.maximum(0.0, np.pi - a*r_grid + b*r_grid**3*np.exp(-0.8*r_grid))
    dF_grid = np.gradient(F_grid, r_grid)

F_sp  = make_interp_spline(r_grid, F_grid,  k=3, bc_type='natural')
dF_sp = make_interp_spline(r_grid, dF_grid, k=3, bc_type='natural')

# ── K=1 L4 ODE (vectorised for solve_bvp) ────────────────────────────────────
# State y = [eta, eta', eta'', eta''']
# Free parameter p[0] = omega^2
#
# Operator derivation:
#   L4_{K=1} eta = -A3 Delta^2_{ell=1} eta + A1 Delta_{ell=1} eta
#                  - Q_{K=1} eta + 2A2(F'^2 Delta_{ell=1} eta - sin^2F/r^4 eta)
#
# SymPy-verified bilaplacian (ell=1):
#   Delta^2_{ell=1} eta = eta'''' + 4/r eta''' - 4/r^2 eta''
# => d4eta = -(4/r) d3eta + (4/r^2) d2eta
#          + (1/A3)(A1 lap_K1 - Q_K1 eta + omega^2 W eta)
#          + (2A2/A3)(F'^2 lap_K1 - sin^2F/r^4 eta)
#
# where lap_K1 = d2eta + 2/r deta - 2/r^2 eta  (ell=1 Laplacian)
#       Q_K1   = Q_diag + A1*2/r^2              (diagonal + centrifugal ell(ell+1)=2)
#       W      = A1 + 2*A2*F'^2                 (kinetic weight, no sin^2F/r^2 term)
#
# Regularity check at r->0 with F->pi:
#   2cF - 1 + cos(2F) -> 2(-1) - 1 + 1 = -2 => Q_diag -> -2A1/r^2
#   Q_K1 = -2A1/r^2 + 2A1/r^2 = 0  [centrifugal cancels diagonal divergence] ✓

def ode_K1_L4(r, y, p):
    omega2              = p[0]
    eta, deta, d2eta, d3eta = y[0], y[1], y[2], y[3]

    F  = F_sp(r);  Fp = dF_sp(r)
    sF = np.sin(F); cF = np.cos(F)
    r2 = r**2; sF2 = sF**2; cF2 = cF**2

    # Diagonal potential (same structure as L=0 BVP)
    Q_diag = (A1*(2*cF - 1 + np.cos(2*F)) / r2
              + 2*A2*(Fp**2*(cF2 - sF2) + sF2*(1 - sF2) / r**4)
              + A4*cF)
    # K=1 centrifugal: ell(ell+1)/r^2 = 2/r^2, coupled to A1 gradient
    Q_K1   = Q_diag + A1*2.0 / r2

    W = A1 + 2*A2*Fp**2

    # ell=1 Laplacian
    lap_K1 = d2eta + 2.0*deta/r - 2.0*eta/r2

    # 4th derivative (Δ²_{ell=1} bilaplacian + remaining terms)
    d4eta  = -(4.0/r)*d3eta + (4.0/r2)*d2eta
    d4eta += (1.0/A3)*(A1*lap_K1 - Q_K1*eta + omega2*W*eta)
    d4eta += (2.0*A2/A3)*(Fp**2*lap_K1 - sF2*eta/r**4)

    return np.vstack([deta, d2eta, d3eta, d4eta])

# ── Boundary conditions ───────────────────────────────────────────────────────
# ell=1 (odd parity): eta ~ r near origin => eta(0)=0, eta''(0)=0
# Decay at r_max: eta(r_max)=0, eta'(r_max)=0
# Normalisation: eta'(r_min) = 1
# Total: 5 BCs for 4 state variables + 1 free parameter [ω²]
def bc_K1(ya, yb, p):
    return np.array([
        ya[0],          # eta(r_min) = 0      (odd parity)
        ya[2],          # eta''(r_min) = 0    (odd parity, Frobenius)
        ya[1] - 1.0,    # eta'(r_min) = 1     (normalisation)
        yb[0],          # eta(r_max) = 0      (decay)
        yb[1],          # eta'(r_max) = 0     (decay)
    ])

# ── Initial mesh and guess ────────────────────────────────────────────────────
# Near-threshold guess: eta_g = r * exp(-kappa * r)
# For ω² close to threshold, kappa is small (extended state)
def make_guess(kappa, n_pts=400):
    x   = np.linspace(r_min, r_max, n_pts)
    g   = x * np.exp(-kappa * x)
    dg  = (1 - kappa*x) * np.exp(-kappa*x)
    d2g = kappa*(kappa*x - 2) * np.exp(-kappa*x)
    d3g = kappa**2*(3 - kappa*x) * np.exp(-kappa*x)
    # Normalise so eta'(r_min) = 1
    scale = 1.0 / dg[0] if abs(dg[0]) > 1e-12 else 1.0
    return x, np.vstack([g*scale, dg*scale, d2g*scale, d3g*scale])

# Decay constants for each guess (from Lifshitz: A3κ⁴ - A1κ² + (A4-ω²) = 0)
def kappa_estimate(omega2):
    disc = A1**2 - 4*A3*(A4 - omega2)
    if disc < 0: return 0.05
    k2_small = (A1 - np.sqrt(disc)) / (2*A3)
    return np.sqrt(max(k2_small, 1e-4))

# ── Sweep p_guess ─────────────────────────────────────────────────────────────
guesses = [0.540, 0.538, 0.535, 0.530]
result  = None

for pg in guesses:
    kappa_g = kappa_estimate(pg)
    x, y_g  = make_guess(kappa_g)

    print(f"\nTrying p_guess = {pg:.3f}  (kappa_est = {kappa_g:.4f},  "
          f"decay_length ~ {1/kappa_g:.1f} L0)")

    try:
        sol = solve_bvp(ode_K1_L4, bc_K1, x, y_g, p=[pg],
                        tol=1e-6, max_nodes=80000, verbose=2)
    except Exception as e:
        print(f"  ERROR: {e}")
        continue

    print(f"  Converged: {sol.success}   msg: {sol.message}")
    if sol.success:
        omega2_found = sol.p[0]
        print(f"  omega^2 = {omega2_found:.6f}   (threshold = {A4})")
        if 0.0 < omega2_found < A4:
            result = sol
            print(f"  *** BOUND STATE FOUND ***")
            break
        else:
            print(f"  Eigenvalue outside (0, A4) — not a physical K=1 bound state.")
    else:
        print(f"  Did not converge; trying next guess.")

# ── Report ────────────────────────────────────────────────────────────────────
print("\n" + "="*60)
if result is None:
    print("No K=1 L4 bound state found in sweep.")
    print("Possible reasons:")
    print("  1. State is very shallow (ω² > 0.540) — needs larger r_max")
    print("  2. State does not exist in L4 (H2 Levinson was approximate)")
    print("  3. Starting guess too far from eigenvalue")
else:
    omega2 = result.p[0]
    omega  = np.sqrt(omega2) * E0
    omega_pi = np.sqrt(A4) * E0
    gap  = omega_pi - omega

    print(f"K=1 L4 BOUND STATE [CONJECT → verify]:")
    print(f"  omega^2_K1 = {omega2:.6f}  (threshold = {A4:.4f})")
    print(f"  omega_K1   = {omega:.2f} MeV")
    print(f"  omega_pi   = {omega_pi:.2f} MeV")
    print(f"  gap        = {gap:.2f} MeV below pion threshold")

    # Lifshitz decay constants
    disc = A1**2 - 4*A3*(A4 - omega2)
    if disc >= 0:
        k1 = np.sqrt((A1 + np.sqrt(disc))/(2*A3))
        k2sq = (A1 - np.sqrt(disc))/(2*A3)
        k2 = np.sqrt(k2sq) if k2sq > 0 else 0.0
        print(f"  Lifshitz kappa1 = {k1:.4f}, kappa2 = {k2:.4f}")
        print(f"  Decay lengths: 1/kappa1 = {1/k1:.2f} L0, 1/kappa2 = {1/k2:.2f} L0")
    else:
        print("  Lifshitz: oscillatory-decaying (disc < 0)")

    # Plot
    r_plot = np.linspace(r_min, min(r_max, 25), 600)
    eta_pl = result.sol(r_plot)[0]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    ax = axes[0]
    ax.plot(r_plot, eta_pl, 'r-', lw=2, label=f'eta_K1(r)  omega={omega:.2f} MeV')
    F_pl = F_sp(r_plot)
    ax.plot(r_plot, F_pl/np.pi, 'b--', lw=1, label='F0/pi (soliton)')
    ax.axhline(0, color='k', lw=0.5)
    ax.set_xlim(0, 20); ax.set_xlabel('r / L0')
    ax.set_title('K=1 L4 Bound-State Wavefunction'); ax.legend(); ax.grid(True)

    ax = axes[1]
    r_v  = np.linspace(0.5, 10, 300)
    F_v  = F_sp(r_v); Fp_v = dF_sp(r_v)
    sF_v = np.sin(F_v); cF_v = np.cos(F_v)
    W_v  = A1 + 2*A2*Fp_v**2
    Q_diag_v = (A1*(2*cF_v - 1 + np.cos(2*F_v))/r_v**2
                + 2*A2*(Fp_v**2*(cF_v**2-sF_v**2) + sF_v**2*(1-sF_v**2)/r_v**4)
                + A4*cF_v)
    Q_K1_v = Q_diag_v + A1*2.0/r_v**2
    Veff_K1 = Q_K1_v / W_v
    ax.plot(r_v, Veff_K1, 'r-',  label='V_eff K=1')
    ax.axhline(A4,     color='green', ls='--', label=f'threshold = {A4}')
    ax.axhline(omega2, color='red',   ls=':',  label=f'omega^2_K1 = {omega2:.4f}')
    ax.set_ylim(-0.5, 1.5); ax.set_xlim(0, 10)
    ax.set_xlabel('r / L0'); ax.set_title('K=1 Effective Potential'); ax.legend(); ax.grid(True)

    ax = axes[2]
    ax.axvspan(0.3935, A4, alpha=0.2, color='green', label='Lifshitz window')
    ax.axvline(0.5412,  color='blue',  lw=2,  label='breathing omega^2=0.5412')
    ax.axvline(A4,      color='green', lw=1.5, ls='--', label='threshold=0.542')
    ax.axvline(omega2,  color='red',   lw=2,  label=f'K=1 omega^2={omega2:.4f}')
    ax.set_xlim(0.38, 0.55)
    ax.set_xlabel('omega^2'); ax.set_title('Spectral window')
    ax.legend(fontsize=8); ax.grid(True); ax.set_yticks([])

    plt.suptitle(f'CCEF K=1 L4 Bound State  omega = {omega:.2f} MeV  '
                 f'(gap = {gap:.2f} MeV below pi threshold)', fontsize=11)
    plt.tight_layout()
    plt.savefig('/sessions/eager-dreamy-hopper/mnt/outputs/ccef_K1_L4_bound_state.png', dpi=200)
    print("\nFigure saved: ccef_K1_L4_bound_state.png")

print("\nDONE.")
