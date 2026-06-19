import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import make_interp_spline
from scipy.special import spherical_jn, spherical_yn
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

A1=1.000; A2=8.971; A4=0.542; E0=311.73
# A3 dropped: H2 approximation — eliminates spurious fast-growing mode
# Valid near threshold (k^4 corrections are subleading at small k)

r_min=0.5   # avoid origin singularity from centrifugal 1/r^2 and sin^2F/r^4
r_max=25.0

print("=== CCEF K=1 Phase Shift — H2 (2nd-order) operator, Radau ===")
print("=== ell=1 centrifugal included; coupling g channel dropped (1-channel) ===")

# ── Background profile ────────────────────────────────────────────────────────
try:
    data=np.load('F0.npy')
    r_grid,F0,dF0=data[0],data[1],data[2]
    idx=np.argsort(r_grid); r_grid,F0,dF0=r_grid[idx],F0[idx],dF0[idx]
    print("Loaded F0.npy.")
except Exception:
    print("Frobenius fallback.")
    r_grid=np.linspace(r_min,r_max,3000)
    a,b=0.836548,-0.018511
    F0=np.pi-a*r_grid+b*r_grid**3*np.exp(-0.8*r_grid)
    dF0=np.gradient(F0,r_grid)

F_sp =make_interp_spline(r_grid,F0, k=3,bc_type='natural')
dF_sp=make_interp_spline(r_grid,dF0,k=3,bc_type='natural')
# F'' from spline derivative
ddF_sp=F_sp.derivative(nu=2)

# ── H2 operator for K=1 (1-channel) ──────────────────────────────────────────
# L2_ell=1  eta = omega^2 W eta
#
# L2_ell = -1/r^2 d/dr [ r^2 P2 d/dr ] + Q_K1
#
# P2(r) = A1 + 2*A2*(F'^ + sin^2F/r^2)    [full stiffness, from H2 spectral]
# Q_K1  = Q_diag(r) + A1*ell(ell+1)/r^2   [diagonal pot + centrifugal]
# W(r)  = A1 + 2*A2*F'^2                  [kinetic weight]
#
# Expanding: P2 eta'' + (2P2/r + P2') eta' - Q_K1 eta = -omega^2 W eta
# => eta'' = -(2/r + P2'/P2) eta' + (Q_K1 - omega^2 W)/P2 * eta

def rhs_H2(r, y, omega2):
    eta, deta = y
    F  = F_sp(r);  Fp = dF_sp(r);  Fpp = ddF_sp(r)
    sF = np.sin(F); cF = np.cos(F)
    r2 = r*r; r4 = r2*r2

    # Stiffness P2 and its derivative
    P2  = A1 + 2*A2*(Fp**2 + sF**2/r2)
    dP2 = 2*A2*(2*Fp*Fpp
                + 2*sF*cF*Fp/r2
                - 2*sF**2/r**3)

    # Diagonal potential (same as L=0 operator)
    Q_diag = (A1*(2*cF - 1 + np.cos(2*F))/r2
              + 2*A2*(Fp**2*(cF**2 - sF**2) + sF**2*(1 - sF**2)/r4)
              + A4*cF)

    # Add ell(ell+1)=2 centrifugal (from A1 gradient term)
    Q_K1 = Q_diag + A1*2.0/r2

    W = A1 + 2*A2*Fp**2

    # Second derivative
    d2eta = (-(2.0/r + dP2/P2)*deta + (Q_K1 - omega2*W)*eta/P2)
    return [deta, d2eta]

# ── Phase shift via two-point amplitude matching ──────────────────────────────
# At large r (F->0): P2->A1, Q_K1->A4+0, W->A1
# Equation -> eta'' + 2/r eta' + (omega^2-A4-2/r^2) eta = 0
# => eta = C*j1(k*r) + D*n1(k*r)   with k=sqrt(omega^2-A4)
# Phase shift: tan(delta) = D/C

def get_phase_shift(omega2):
    k2 = omega2 - A4
    if k2 <= 0:
        return None   # below threshold

    k = np.sqrt(k2)

    # Regular IC at r_min for ell=1: eta ~ r, eta' ~ 1
    y0 = [r_min, 1.0]

    sol = solve_ivp(
        lambda r, y: rhs_H2(r, y, omega2),
        [r_min, r_max], y0,
        method='Radau',
        rtol=1e-10, atol=1e-12,
        dense_output=True,
        max_step=0.1
    )

    if not sol.success:
        return None

    # Two-point matching deep in the tail (well past soliton)
    r1, r2 = r_max - 3.0, r_max - 0.5
    e1 = sol.sol(r1)[0];  e2 = sol.sol(r2)[0]
    x1, x2 = k*r1, k*r2

    j1_1 = spherical_jn(1, x1); n1_1 = spherical_yn(1, x1)
    j1_2 = spherical_jn(1, x2); n1_2 = spherical_yn(1, x2)

    # [ j1(x1) n1(x1) ] [C]   [e1]
    # [ j1(x2) n1(x2) ] [D] = [e2]
    denom = j1_1*n1_2 - j1_2*n1_1
    if abs(denom) < 1e-14:
        return None

    C = (e1*n1_2 - e2*n1_1) / denom
    D = (j1_1*e2 - j1_2*e1) / denom

    if abs(C) < 1e-14:
        return None

    delta = np.arctan2(D, C)
    return delta, k, sol

# ── Scan ─────────────────────────────────────────────────────────────────────
omega_pi = np.sqrt(A4)*E0
print(f"\nPion threshold omega_pi = {omega_pi:.2f} MeV")
print(f"Scanning 230 to 450 MeV ...\n")
print(f"{'omega':>8} {'k':>8} {'delta':>10}  notes")
print("-"*50)

omega_scan  = np.linspace(232, 450, 44)
omega2_scan = (omega_scan/E0)**2

omegas_ok   = []
deltas_ok   = []

for o_mev, o2 in zip(omega_scan, omega2_scan):
    res = get_phase_shift(o2)
    if res is None:
        print(f"{o_mev:8.1f}  FAIL")
        continue
    delta, k, _ = res
    d_deg = np.degrees(delta)
    omegas_ok.append(o_mev)
    deltas_ok.append(d_deg)
    print(f"{o_mev:8.1f} {k:8.4f} {d_deg:+10.3f}°")

# ── Resonance detection ───────────────────────────────────────────────────────
print()
if len(deltas_ok) >= 3:
    d_arr = np.array(deltas_ok)
    diffs = np.diff(d_arr)
    res_idx = np.where(np.abs(diffs) > 25)[0]
    if len(res_idx):
        for ri in res_idx:
            print(f">>> Possible resonance near omega ~ "
                  f"{omegas_ok[ri]:.0f}–{omegas_ok[ri+1]:.0f} MeV  "
                  f"(Delta delta = {diffs[ri]:+.1f} deg)")
    else:
        print("No rapid phase-shift variation detected (|Delta delta| < 25 deg everywhere).")
        print("Consistent with WKB prediction: smooth continuum, no K=1 resonance. [SOLID]")
else:
    print("Too few converged points.")

# ── Plot ──────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

if omegas_ok:
    axes[0].plot(omegas_ok, deltas_ok, 'b-o', ms=4, label='delta(omega) K=1')
    axes[0].axhline( 90, color='r',      ls='--', lw=0.8, label='90 deg (resonance)')
    axes[0].axhline(-90, color='r',      ls='--', lw=0.8)
    axes[0].axhline(  0, color='gray',   ls=':',  lw=0.8)
    axes[0].axvline(omega_pi, color='green', ls=':', lw=1, label='omega_pi')
    axes[0].set_xlabel('omega (MeV)'); axes[0].set_ylabel('delta (degrees)')
    axes[0].set_title('K=1 Phase Shift delta(omega)  [H2, ell=1]')
    axes[0].legend(); axes[0].grid(True)

# V_eff comparison: L=0 vs K=1
r_v  = np.linspace(0.5, 10, 300)
F_v  = F_sp(r_v);  Fp_v = dF_sp(r_v)
sF_v = np.sin(F_v); cF_v = np.cos(F_v)
W_v  = A1 + 2*A2*Fp_v**2

Q_diag_v = (A1*(2*cF_v-1+np.cos(2*F_v))/r_v**2
            + 2*A2*(Fp_v**2*(cF_v**2-sF_v**2) + sF_v**2*(1-sF_v**2)/r_v**4)
            + A4*cF_v)
Q_K1_v = Q_diag_v + A1*2.0/r_v**2
P2_v   = A1 + 2*A2*(Fp_v**2 + sF_v**2/r_v**2)

V_L0 = Q_diag_v / W_v
V_K1 = Q_K1_v   / P2_v

axes[1].plot(r_v, V_L0, 'b-',  lw=1.5, label='V_eff L=0 (breathing)')
axes[1].plot(r_v, V_K1, 'r--', lw=1.5, label='V_eff K=1 (+centrifugal)')
axes[1].axhline(A4,     color='green',  ls=':', lw=1, label=f'omega^2_pi={A4}')
axes[1].axhline(0.3935, color='orange', ls=':', lw=1, label='omega^2_crit (L=0)')
axes[1].set_ylim(-1.5, 2.5); axes[1].set_xlim(0, 10)
axes[1].set_xlabel('r / L0'); axes[1].set_ylabel('V_eff(r)')
axes[1].set_title('Effective potentials: L=0 vs K=1')
axes[1].legend(fontsize=8); axes[1].grid(True)

plt.suptitle('CCEF K=1 Grand-Spin Phase Shift (H2 operator, Radau)')
plt.tight_layout()
plt.savefig('ccef_K1_H2_phase_shift.png', dpi=200)
print("\nFigure saved: ccef_K1_H2_phase_shift.png")
print("DONE.")
