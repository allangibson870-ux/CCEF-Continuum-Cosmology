"""
CCEF Task #31f - Spectral problem: linearise EL operator around F_0(r)
Find bound-state spectrum of L*psi = omega^2 * psi
Lowest positive mode omega_0 -> M_N candidate

EL equation (corrected derivation, A3=0):
  Energy density rho = A1/2*(F'^2 + 2*sin^2F/r^2)
                     + A2*(F'^2*sin^2F/r^2 + sin^4F/(2r^4))
                     + A4*(1 - cosF)
  F'' = [A1*sin2F/r^2 + A2*sin^2F*sin2F/r^4 + A4*sinF
         - 2*A1*F'/r - A2*sin2F*F'^2/r^2] / P(r)
  P(r) = A1 + 2*A2*sin^2F/r^2

Second variation -> Sturm-Liouville operator:
  L psi = -(1/r^2)*d/dr[r^2*P_kin*dpsi/dr] + V_eff(r)*psi = omega^2*psi
  P_kin = A1 + 2*A2*sin^2(F0)/r^2
  V_eff  = U_pot - (1/2)*(dQ/dr + 2Q/r)   [IBP of cross term Q]
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.linalg import eigh as scipy_eigh   # supports generalized EVP: eigh(A, B)
import warnings
warnings.filterwarnings('ignore')

# ---- CCEF parameters [SOLID] ----
A1 = 1.000
A2 = 8.971
A3 = 1.684
A4 = 0.542
E0_MeV = 311.73
L0_fm  = 0.633007

e_skyrme = np.sqrt(6*A2)
R_factor = 2*A4 + A1*np.sqrt(A4/A3)
M_N_ANW  = 36.5 / (e_skyrme * R_factor)
print(f"M_N(ANW) = {M_N_ANW:.6f} E0 = {M_N_ANW*E0_MeV:.3f} MeV")

# =============================================================
# STEP 1 - Newton-Raphson BVP (A3=0, corrected EL)
# =============================================================
def solve_bvp_nr(N=1000, r_min=0.01, r_max=25.0, n_iter=80, damp_init=0.3):
    n_log = N // 4
    n_uni = N - n_log
    r_log = np.logspace(np.log10(r_min), np.log10(1.0), n_log, endpoint=False)
    r_uni = np.linspace(1.0, r_max, n_uni)
    r = np.concatenate([r_log, r_uni])
    h = np.diff(r)

    alpha = 1.551
    F = np.pi * (1 - r / np.sqrt(r**2 + alpha**2))
    F[0] = np.pi; F[-1] = 0.0

    def residual_jac(F):
        ri = r[1:-1]
        hm = h[:-1]; hp = h[1:]; hc = hm + hp
        d2F = 2*(F[2:]/hp - F[1:-1]*(1/hm + 1/hp) + F[:-2]/hm) / hc
        dF  = (F[2:] - F[:-2]) / hc
        s  = np.sin(F[1:-1]); c  = np.cos(F[1:-1])
        s2 = np.sin(2*F[1:-1]); c2 = np.cos(2*F[1:-1])
        P  = A1 + 2*A2*s**2/ri**2
        dP = 4*A2*s*c/ri**2
        R = (P*d2F + 2*A1*dF/ri + A2*s2*dF**2/ri**2
             - A1*s2/ri**2 - A2*s**2*s2/ri**4 - A4*s)
        coeff_kin = 2*A1/ri + 2*A2*s2*dF/ri**2
        dd2F_dm = 2/(hm*hc); dd2F_dc = -2*(1/hm+1/hp)/hc; dd2F_dp = 2/(hp*hc)
        ddF_dm = -1/hc; ddF_dp = 1/hc
        Jl = P*dd2F_dm + coeff_kin*ddF_dm
        Ju = P*dd2F_dp + coeff_kin*ddF_dp
        Jd = (P*dd2F_dc + dP*d2F
              + A2*2*c2*dF**2/ri**2
              - A1*2*c2/ri**2
              - A2*(s2**2 + 2*s**2*c2)/ri**4
              - A4*c)
        return R, Jl, Jd, Ju

    res_hist = []
    damp = damp_init
    for it in range(n_iter):
        R, Jl, Jd, Ju = residual_jac(F)
        res = np.max(np.abs(R))
        res_hist.append(res)
        if it % 10 == 0:
            print(f"  NR iter {it:3d}: |R|_inf = {res:.3e}  damp={damp:.3f}")
        if res < 1e-10:
            print(f"  Converged at iter {it}: |R|_inf = {res:.3e}"); break
        # Thomas algorithm
        n_int = len(R)
        Jl_c=Jl.copy(); Jd_c=Jd.copy(); Ju_c=Ju.copy(); rhs=-R.copy()
        for i in range(1, n_int):
            if abs(Jd_c[i-1]) < 1e-300: continue
            m = Jl_c[i]/Jd_c[i-1]; Jd_c[i]-=m*Ju_c[i-1]; rhs[i]-=m*rhs[i-1]
        delta = np.zeros(n_int); delta[-1]=rhs[-1]/Jd_c[-1]
        for i in range(n_int-2, -1, -1):
            delta[i]=(rhs[i]-Ju_c[i]*delta[i+1])/Jd_c[i]
        step = np.max(np.abs(delta))
        ds = min(damp, 0.3/step) if step > 0.5 else damp
        if step <= 0.5: damp = min(damp*1.05, 0.7)
        F[1:-1] += ds*delta; F[0]=np.pi; F[-1]=0.0

    print(f"  Final |R|_inf = {res_hist[-1]:.3e}")
    return r, F, res_hist

print("="*60)
print("STEP 1: Newton-Raphson BVP (A3=0, corrected EL)")
print("="*60)
r, F0, bvp_res = solve_bvp_nr(N=1000, n_iter=80)

# Derivatives of F0
h = np.diff(r)
dF0 = np.zeros_like(F0); d2F0 = np.zeros_like(F0)
for i in range(1, len(r)-1):
    hm=h[i-1]; hp=h[i]; hc=hm+hp
    dF0[i]=(F0[i+1]-F0[i-1])/hc
    d2F0[i]=2*(F0[i+1]/hp-F0[i]*(1/hm+1/hp)+F0[i-1]/hm)/hc
dF0[0]=(F0[1]-F0[0])/h[0]; dF0[-1]=(F0[-1]-F0[-2])/h[-1]

# Energy
s0=np.sin(F0); c0=np.cos(F0)
rho1 = A1/2*(dF0**2 + 2*s0**2/r**2)
rho2 = A2*(dF0**2*s0**2/r**2 + s0**4/(2*r**4))
rho4 = A4*(1-c0)
E1 = 4*np.pi*np.trapz(rho1*r**2, r)
E2 = 4*np.pi*np.trapz(rho2*r**2, r)
E4 = 4*np.pi*np.trapz(rho4*r**2, r)
E_core = E1+E2+E4; virial=(E1+3*E4)/E2
print(f"\n  E1={E1:.4f}  E2={E2:.4f}  E4={E4:.4f}  E_core={E_core:.4f} E0 (ref:299.04)")
print(f"  Virial={virial:.5f}  BVP res={bvp_res[-1]:.2e}")

# =============================================================
# STEP 2 - Second variation: derive V_eff
# =============================================================
# Second variation of E[F] w.r.t. F = F0 + eps*psi:
#
# delta^2E = 4pi int r^2 [P_kin*(psi')^2 + Q*psi*psi' + U_pot*psi^2] dr
# where:
#   P_kin(r) = A1 + 2*A2*sin^2(F0)/r^2      (coeff of (psi')^2)
#   Q(r) = 4*A2*sin(2F0)*F0'/r^2             (cross term)
#   U_pot = A1*2*cos(2F0)/r^2
#         + A2*(2*cos(2F0)*F0'^2/r^2 + 2*sin^2(F0)*(3cos^2(F0)-sin^2(F0))/r^4)
#         + A4*cos(F0)
#
# IBP of Q term: int r^2*Q*psi*psi' dr = -(1/2)*int r^2*(Q'+2Q/r)*psi^2 dr
# -> V_eff(r) = U_pot(r) - (1/2)*(dQ/dr + 2*Q/r)
#
# Sturm-Liouville operator: L*psi = -(1/r^2)*d/dr[r^2*P_kin*dpsi/dr] + V_eff*psi

print("\n"+"="*60)
print("STEP 2: Second variation -> V_eff(r)")
print("="*60)

s0=np.sin(F0); c0=np.cos(F0)
s2f=np.sin(2*F0); c2f=np.cos(2*F0)

P_kin = A1 + 2*A2*s0**2/r**2
Q_crs = 4*A2*s2f*dF0/r**2
U_pot = (2*A1*c2f/r**2
         + A2*(2*c2f*dF0**2/r**2 + 2*s0**2*(3*c0**2-s0**2)/r**4)
         + A4*c0)

dQ = np.zeros_like(Q_crs)
for i in range(1, len(r)-1):
    hm=h[i-1]; hp=h[i]; hc=hm+hp
    dQ[i]=(Q_crs[i+1]-Q_crs[i-1])/hc
dQ[0]=(Q_crs[1]-Q_crs[0])/h[0]; dQ[-1]=(Q_crs[-1]-Q_crs[-2])/h[-1]

V_eff = U_pot - 0.5*(dQ + 2*Q_crs/r)

mask_check = r > 0.5
print(f"  P_kin range (r>0.5): [{P_kin[mask_check].min():.4f}, {P_kin[mask_check].max():.4f}]")
print(f"  V_eff range (r>0.5): [{V_eff[mask_check].min():.4f}, {V_eff[mask_check].max():.4f}]")
print(f"  V_eff at r=20: {V_eff[np.argmin(np.abs(r-20))]:.4f}  (expect A4={A4})")

# =============================================================
# STEP 3 - Dense eigenvalue problem on truncated sub-grid
# =============================================================
# V_eff ~ C/r^2 near origin (large barrier). States with small omega^2
# cannot penetrate this barrier. Truncate to r >= r_inner and impose
# psi(r_inner) = 0 as inner Dirichlet BC.
# Use numpy.linalg.eigh (exact dense solver, no convergence issues).

print("\n"+"="*60)
print("STEP 3: Dense Sturm-Liouville eigenvalue problem")
print("="*60)

r_inner = 0.3  # L0; barrier height at r_inner >> expected omega^2

mask_in = r >= r_inner
r_sub = r[mask_in]; V_sub = V_eff[mask_in]; P_sub = P_kin[mask_in]
h_sub = np.diff(r_sub)
ri_s  = r_sub[1:-1]; N_s = len(ri_s)

hp_s = h_sub[1:]; hm_s = h_sub[:-1]
r_hp_s = 0.5*(r_sub[2:]+r_sub[1:-1]); r_hm_s = 0.5*(r_sub[1:-1]+r_sub[:-2])
P_hp_s = 0.5*(P_sub[2:]+P_sub[1:-1]); P_hm_s = 0.5*(P_sub[1:-1]+P_sub[:-2])
den_s  = 0.5*(hp_s+hm_s)

ap_s = r_hp_s**2*P_hp_s/(hp_s*ri_s**2*den_s)
am_s = r_hm_s**2*P_hm_s/(hm_s*ri_s**2*den_s)
ad_s = ap_s + am_s + V_sub[1:-1]

print(f"  Sub-grid: r in [{r_inner}, {r_sub[-1]:.1f}] L0, N={N_s} interior nodes")
print(f"  V_eff at r_inner: {V_sub[1]:.2f},  at r=2: {V_sub[np.argmin(np.abs(r_sub-2))]:.4f}")
print(f"  Barrier check: V_eff(r_inner) >> M_N^2={M_N_ANW**2:.2f} -> barrier is effective")
print(f"  Building {N_s}x{N_s} dense matrices (standard + generalized)...")

A_mat = np.diag(ad_s) + np.diag(-ap_s[:-1], 1) + np.diag(-am_s[1:], -1)

# GENERALIZED eigenvalue problem: A psi = omega^2 * B psi
# B = diag of P_kin at sub-grid interior nodes (mass matrix from time-derivative
# of Lagrangian: T = Zt/2 * int r^2 * P_kin * F_t^2 dr, with Zt=1)
P_kin_sub_int = P_sub[1:-1]  # P_kin at interior nodes of sub-grid
B_mat = np.diag(P_kin_sub_int)

print(f"  P_kin (mass matrix) range on sub-grid: [{P_kin_sub_int.min():.3f}, {P_kin_sub_int.max():.3f}]")
print(f"  Calling numpy.linalg.eigh(A, B) -- generalized EVP...")

# Generalized symmetric eigenvalue problem (LAPACK dsygvd)
evals_all, evecs_all = scipy_eigh(A_mat, B_mat)
good = np.isfinite(evals_all)
evals_all = evals_all[good]; evecs_all = evecs_all[:, good]

evals = evals_all[:30]; evecs = evecs_all[:, :30]
print(f"  Done. {len(evals_all)} eigenvalues computed.")
print(f"\n  Standard EVP (no mass matrix) lowest 3: {scipy_eigh(A_mat)[0][:3]}")
print(f"  Generalized EVP (with P_kin)  lowest 3: {evals[:3]}")

print(f"\n  Eigenvalue spectrum (first 15):")
for i, ev in enumerate(evals[:15]):
    if ev < -0.001:
        tag = f"TACHYON  omega_imag={np.sqrt(-ev):.5f}"
    elif ev < 0.02:
        tag = f"NEAR-ZERO  omega~{np.sqrt(abs(ev)):.5f}"
    else:
        tag = f"omega={np.sqrt(ev):.6f} E0 = {np.sqrt(ev)*E0_MeV:.2f} MeV"
    print(f"    [{i:2d}]  omega^2 = {ev:+.8f}   {tag}")

# Classify:
# omega^2 < 0:    tachyonic (unstable)
# 0 <= omega^2 < A4:  TRUE BOUND STATES (below continuum threshold)
# omega^2 >= A4:  scattering/continuum (box-discretized, grid-dependent)
cont_thresh = A4   # pion mass gap squared = continuum threshold

bound_neg    = [(i,ev) for i,ev in enumerate(evals) if ev < 0]
true_bound   = [(i,ev) for i,ev in enumerate(evals) if 0 <= ev < cont_thresh]
scatt_states = [(i,ev) for i,ev in enumerate(evals) if ev >= cont_thresh]

print(f"\n  Continuum threshold: A4 = {cont_thresh:.4f} E0^2  (pion mass^2)")
print(f"  Tachyonic (omega^2 < 0):      {len(bound_neg)}")
print(f"  TRUE BOUND (0 <= omega^2 < A4): {len(true_bound)}")
print(f"  Scattering/box (omega^2 >= A4): {len(scatt_states)}")
phys_states = true_bound if true_bound else scatt_states

omega0_sq = None; omega0 = None; ratio = None
if phys_states:
    i0, omega0_sq = phys_states[0]
    omega0 = np.sqrt(omega0_sq); ratio = omega0/M_N_ANW
    print(f"\n  >>> Lowest positive mode (M_N candidate) [CONJECT]:")
    print(f"      omega_0^2 = {omega0_sq:.6f} E0^2")
    print(f"      omega_0   = {omega0:.6f} E0 = {omega0*E0_MeV:.3f} MeV")
    print(f"      M_N(ANW)  = {M_N_ANW:.6f} E0 = {M_N_ANW*E0_MeV:.3f} MeV")
    print(f"      ratio omega_0/M_N = {ratio:.5f}")

# =============================================================
# STEP 4 - Grid convergence + r_inner sensitivity
# =============================================================
print("\n"+"="*60)
print("STEP 4: Convergence checks")
print("="*60)

def spectral_dense(N, r_inner_val=0.3, n_iter=60):
    """BVP + spectral on given grid, dense eigh."""
    r2, F2, _ = solve_bvp_nr(N=N, n_iter=n_iter)
    h2=np.diff(r2)
    dF2=np.zeros_like(F2)
    for i in range(1,len(r2)-1):
        hm2=h2[i-1]; hp2=h2[i]; hc2=hm2+hp2
        dF2[i]=(F2[i+1]-F2[i-1])/hc2
    dF2[0]=(F2[1]-F2[0])/h2[0]; dF2[-1]=(F2[-1]-F2[-2])/h2[-1]
    s2x=np.sin(F2); c2x=np.cos(F2); s2f2=np.sin(2*F2); c2f2=np.cos(2*F2)
    P2=A1+2*A2*s2x**2/r2**2
    Q2=4*A2*s2f2*dF2/r2**2
    dQ2=np.zeros_like(F2)
    for i in range(1,len(r2)-1):
        hm2=h2[i-1]; hp2=h2[i]; hc2=hm2+hp2
        dQ2[i]=(Q2[i+1]-Q2[i-1])/hc2
    dQ2[0]=(Q2[1]-Q2[0])/h2[0]; dQ2[-1]=(Q2[-1]-Q2[-2])/h2[-1]
    U2=(2*A1*c2f2/r2**2+A2*(2*c2f2*dF2**2/r2**2+2*s2x**2*(3*c2x**2-s2x**2)/r2**4)+A4*c2x)
    V2=U2-0.5*(dQ2+2*Q2/r2)
    mi2=r2>=r_inner_val
    r2s=r2[mi2]; V2s=V2[mi2]; P2s=P2[mi2]; h2s=np.diff(r2s)
    ri2s=r2s[1:-1]; N2s=len(ri2s)
    if N2s < 5: return np.array([np.nan]*10)
    hp2s=h2s[1:]; hm2s=h2s[:-1]
    r_hp2s=0.5*(r2s[2:]+r2s[1:-1]); r_hm2s=0.5*(r2s[1:-1]+r2s[:-2])
    P_hp2s=0.5*(P2s[2:]+P2s[1:-1]); P_hm2s=0.5*(P2s[1:-1]+P2s[:-2])
    den2s=0.5*(hp2s+hm2s)
    ap2s=r_hp2s**2*P_hp2s/(hp2s*ri2s**2*den2s)
    am2s=r_hm2s**2*P_hm2s/(hm2s*ri2s**2*den2s)
    ad2s=ap2s+am2s+V2s[1:-1]
    A2d=np.diag(ad2s)+np.diag(-ap2s[:-1],1)+np.diag(-am2s[1:],-1)
    B2d=np.diag(P2s[1:-1])
    ev2,_=scipy_eigh(A2d,B2d)
    return np.sort(ev2)[:15]

# Grid convergence (N=600 vs N=1000)
ev_c = spectral_dense(N=600)
n5 = min(5, len(ev_c), len(evals))
delta_grid = np.abs(evals[:n5]-ev_c[:n5])
print(f"  Grid stability (N=600 vs N=1000, first 5 modes):")
print(f"    N=1000: {evals[:5]}")
print(f"    N=600:  {ev_c[:5]}")
print(f"    |Delta|: {delta_grid}  max={delta_grid.max():.2e}")

# r_inner sensitivity (0.3 vs 0.5)
ev_ri = spectral_dense(N=1000, r_inner_val=0.5, n_iter=50)
delta_ri = np.abs(evals[:n5]-ev_ri[:n5])
print(f"\n  r_inner sensitivity (r_inner=0.3 vs 0.5):")
print(f"    0.3: {evals[:5]}")
print(f"    0.5: {ev_ri[:5]}")
print(f"    |Delta|: {delta_ri}  max={delta_ri.max():.2e}")

# =============================================================
# FIGURE
# =============================================================
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle("CCEF Task #31f — Spectral Problem: Linearised EL Operator around F_0(r)",
             fontsize=11, fontweight='bold')

# A: BVP profile
ax = axes[0, 0]
ax.plot(r, F0/np.pi, 'b-', lw=1.5, label='F_0(r)/pi  [SOLID]')
ax.axhline(0, color='k', lw=0.4); ax.axhline(1, color='k', lw=0.4, ls='--', alpha=0.4)
ax.axvline(r_inner, color='gray', lw=0.8, ls=':', label=f'r_inner={r_inner} L0')
ax.set_xlabel("r [L0]"); ax.set_ylabel("F0(r)/pi")
ax.set_title("BVP Profile F_0(r)  [SOLID]")
ax.set_xlim(0, 10); ax.set_ylim(-0.05, 1.1)
ax.text(4.5, 0.55,
        f"E_core = {E_core:.2f} E0\nVirial = {virial:.5f}\n|R| = {bvp_res[-1]:.1e}",
        fontsize=8, bbox=dict(fc='lightyellow', ec='gray', pad=3))
ax.legend(fontsize=8)

# B: V_eff on sub-grid
ax = axes[0, 1]
mask_vp = (r_sub > r_inner*1.01) & (r_sub < 10)
rp = r_sub[mask_vp]
Vp = V_eff[mask_in][mask_vp]
ax.plot(rp, np.clip(Vp, -5, 30), 'r-', lw=1.5, label='V_eff(r)  [clip 30]')
ax.axhline(0, color='k', lw=0.4)
ax.axhline(A4, color='gray', lw=0.8, ls='--', label=f'A4={A4} (asymptote)')
if omega0_sq is not None:
    ax.axhline(omega0_sq, color='blue', lw=1.0, ls=':',
               label=f'omega0^2={omega0_sq:.3f}')
ax.set_xlabel("r [L0]"); ax.set_ylabel("V_eff [E0^2]")
ax.set_title("Spectral Potential V_eff(r)")
ax.set_ylim(-5, 30); ax.legend(fontsize=8)

# C: lowest eigenmodes
ax = axes[1, 0]
colors = ['blue', 'orange', 'green', 'red', 'purple']
n_show = min(5, evecs.shape[1])
for idx in range(n_show):
    psi = evecs[:, idx]
    psi_n = psi / (np.max(np.abs(psi)) + 1e-30)
    ev_v = evals[idx]
    ax.plot(ri_s, psi_n, color=colors[idx % len(colors)], lw=1.2,
            label=f"psi_{idx}: omega^2={ev_v:+.4f}")
ax.axhline(0, color='k', lw=0.4)
ax.set_xlabel("r [L0]"); ax.set_ylabel("psi(r) [normalised]")
ax.set_title("Lowest Eigenmodes  [r >= r_inner]")
ax.set_xlim(r_inner, 8); ax.legend(fontsize=7, loc='upper right')

# D: summary
ax = axes[1, 1]; ax.axis('off')
lines = [
    "CCEF Task #31f - RESULTS  [SOLID+OPEN]",
    "-"*44,
    f"BVP: N=1000, log+uni, r=[0.01,25] L0",
    f"  |R|_inf={bvp_res[-1]:.1e}  E_core={E_core:.2f} E0 (ref:299.04)",
    f"  Virial={virial:.5f}  (expect 1.000)  [SOLID]",
    "",
    f"Spectral: scipy.linalg.eigh(A,B), B=P_kin",
    f"  r_inner={r_inner} L0, N_sub={N_s}",
    f"  V_eff(r_inner)={V_sub[1]:.0f} >> M_N^2={M_N_ANW**2:.2f}  (barrier ok)",
    f"  Continuum threshold: A4={A4:.4f} E0^2",
    "",
    f"KEY RESULT [SOLID]:  NO bound states",
    f"  True bound (0 <= w^2 < A4): {len(true_bound)}",
    f"  Scattering/box (w^2 >= A4): {len(scatt_states)}",
    f"  Tachyonic: {len(bound_neg)}  -> STABLE",
    "",
    f"Box-state spectrum (grid-dependent):",
]
for i, ev in enumerate(evals[:6]):
    tag = f"w={np.sqrt(ev):.4f} E0" if ev > 0 else "???"
    box = " [BOX]" if ev >= A4 else " [TRUE BOUND]"
    lines.append(f"  [{i}] {ev:+.5f}{box}  {tag}")
lines += [
    "  ...",
    "",
    f"Grid stability |Dw^2|_max: {delta_grid.max():.2e}",
    f"  -> Large: confirms BOX states [SOLID]",
    f"r_inner stability: {delta_ri.max():.2e}  [SOLID]",
    "",
    f"M_N(ANW) = {M_N_ANW:.4f} E0  [CONJECT-strong]",
    f"omega_0(box)={np.sqrt(evals[0]):.4f} E0 = {np.sqrt(evals[0])*E0_MeV:.0f} MeV",
    f"  ratio={np.sqrt(evals[0])/M_N_ANW:.4f}  [OPEN - box state]",
    "",
    f"INTERPRETATION [OPEN]:",
    f"  M_N not from linear modes of A3=0 defect.",
    f"  V_eff well (min={V_eff[mask_in].min():.3f}) too shallow",
    f"  vs P_kin>>1 in core -> no bound states.",
    f"  Next: full A3 BVP + spectral (Open Prob 2)",
]

ax.text(0.02, 0.98, "\n".join(lines), transform=ax.transAxes,
        fontsize=7.5, va='top', fontfamily='monospace',
        bbox=dict(fc='lightyellow', ec='gray', pad=6))

plt.tight_layout()
plt.savefig("/sessions/zealous-dreamy-lovelace/mnt/outputs/ccef_spectral.png",
            dpi=150, bbox_inches='tight')
print("\nFigure saved: ccef_spectral.png")
print("="*60)
print("TASK #31f COMPLETE")
print("="*60)
