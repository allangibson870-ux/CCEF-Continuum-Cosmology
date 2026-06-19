import numpy as np
from scipy.integrate import solve_bvp
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

print("=== CCEF L4 Spectral BVP Eigenvalue (A3-corrected, exact sign) ===")

# Protected profile
try:
    data = np.load('F0.npy')
    r_grid = data[0]
    F0    = data[1]
    dF0   = data[2]
    idx   = np.argsort(r_grid)
    r_grid, F0, dF0 = r_grid[idx], F0[idx], dF0[idx]
    print("Loaded BVP profile.")
except Exception:
    print("Frobenius fallback profile.")
    r_grid = np.linspace(r_min, r_max, 2000)
    a, b   = 0.836548, -0.018511
    F0     = np.pi - a*r_grid + b*r_grid**3 * np.exp(-0.8*r_grid)
    dF0    = np.gradient(F0, r_grid)
    np.save('F0.npy', np.column_stack((r_grid, F0, dF0)))

F_interp  = make_interp_spline(r_grid, F0,  k=3, bc_type='natural')
dF_interp = make_interp_spline(r_grid, dF0, k=3, bc_type='natural')

def ode(r, y, p):
    omega2 = p[0]
    eta, deta, d2eta, d3eta = y
    F  = F_interp(r)
    Fp = dF_interp(r)
    sF = np.sin(F);  cF = np.cos(F)
    r2 = r**2;  sF2 = sF**2;  cF2 = cF**2

    Q = (A1 * (2*cF - 1 + np.cos(2*F)) / r2
         + 2*A2 * (Fp**2 * (cF2 - sF2) + sF2*(1 - sF2) / r**4)
         + A4 * cF)
    W   = A1 + 2*A2 * Fp**2
    lap = d2eta + 2*deta / r

    # Correct sign: from n̈ = P⊥(A1∇²n - A3∇⁴n + ...) → L4η = ω²Wη
    d4eta  = -(4.0/r)*d3eta + (1.0/A3)*(A1*lap - Q*eta + omega2*W*eta)
    d4eta += (2*A2/A3) * (Fp**2 * lap - sF2*eta / r**4)

    return np.vstack([deta, d2eta, d3eta, d4eta])

def bc(ya, yb, p):
    # Even-parity regularity at r_min, decay at r_max, normalisation
    # 4 states + 1 free parameter → 5 BCs
    return np.array([
        ya[1],        # η'(r_min)  = 0  (even parity)
        ya[3],        # η'''(r_min)= 0  (even parity)
        yb[0],        # η(r_max)   = 0  (decay)
        yb[1],        # η'(r_max)  = 0  (decay)
        ya[0] - 1.0,  # normalisation
    ])

# Initial mesh and guess (Gaussian breathing shape)
x   = np.linspace(r_min, r_max, 300)
mu  = 2.0;  sig = 1.5
g   =  np.exp(-(x-mu)**2 / (2*sig**2))
dg  = -(x-mu)/sig**2 * g
d2g = ((x-mu)**2/sig**4 - 1/sig**2) * g
d3g = (-(x-mu)/sig**2) * ((x-mu)**2/sig**4 - 3/sig**2) * g

y_guess = np.vstack([g, dg, d2g, d3g])
p_guess = [0.542]   # near pion threshold — good starting point

print("Solving BVP eigenvalue problem...")
sol = solve_bvp(ode, bc, x, y_guess, p=p_guess,
                tol=1e-6, max_nodes=50000, verbose=2)

print(f"\nConverged : {sol.success}")
if sol.success:
    omega2 = sol.p[0]
    omega  = np.sqrt(abs(omega2)) * E0
    print(f"ω²  = {omega2:.6f}")
    print(f"ω   = {omega:.2f} MeV   (reference: 229.42 MeV)")

    disc = A1**2 - 4*A3*(A4 - omega2)
    if disc >= 0:
        k1 = np.sqrt((A1 + np.sqrt(disc)) / (2*A3))
        k2sq = (A1 - np.sqrt(disc)) / (2*A3)
        k2 = np.sqrt(k2sq) if k2sq > 0 else 0.0
        print(f"Lifshitz κ₁ = {k1:.4f}, κ₂ = {k2:.4f}")
    else:
        print("Lifshitz: oscillatory-decaying regime (disc < 0)")

    r_plot   = np.linspace(r_min, 12, 500)
    eta_plot = sol.sol(r_plot)[0]

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.plot(r_grid, F0, 'b-', label='F₀(r)')
    plt.plot(r_plot, eta_plot, 'r--', label=f'η(r)  ω={omega:.1f} MeV')
    plt.axvline(2.039, color='gray', ls=':', label='r_half')
    plt.xlabel('r / L₀'); plt.legend(); plt.grid(True)
    plt.title('Breathing mode wavefunction')

    plt.subplot(2, 2, 2)
    plt.plot(r_plot, sol.sol(r_plot)[1], 'g-', label="η'(r)")
    plt.xlabel('r / L₀'); plt.legend(); plt.grid(True)
    plt.title("First derivative")

    plt.subplot(2, 2, 3)
    plt.axvline(0.3935, color='orange', label='ω²_crit (Lifshitz)')
    plt.axvline(0.542,  color='green',  label='pion threshold')
    plt.axvline(omega2, color='red',    label=f'result ω²={omega2:.4f}')
    plt.xlim(0.35, 0.56)
    plt.legend(); plt.grid(True); plt.title('Spectral window')

    plt.subplot(2, 2, 4)
    r_v = np.linspace(0.5, 8, 300)
    F_v  = F_interp(r_v);  Fp_v = dF_interp(r_v)
    sF_v = np.sin(F_v);   cF_v  = np.cos(F_v)
    W_v  = A1 + 2*A2*Fp_v**2
    Q_v  = (A1*(2*cF_v - 1 + np.cos(2*F_v))/r_v**2
            + 2*A2*(Fp_v**2*(cF_v**2-sF_v**2) + sF_v**2*(1-sF_v**2)/r_v**4)
            + A4*cF_v)
    Veff = Q_v / W_v
    plt.plot(r_v, Veff, 'k-', label='V_eff = Q/W')
    plt.axhline(omega2, color='red', ls='--', label=f'ω²={omega2:.4f}')
    plt.axhline(A4, color='green', ls=':', label='pion threshold')
    plt.xlabel('r / L₀'); plt.legend(); plt.grid(True)
    plt.title('Effective potential')

    plt.tight_layout()
    plt.savefig('ccef_a3_spectral_L4_bvp.png', dpi=200)
    print("Figure saved: ccef_a3_spectral_L4_bvp.png")
else:
    print(f"Failed: {sol.message}")
    print("Try adjusting p_guess or initial mesh density.")
