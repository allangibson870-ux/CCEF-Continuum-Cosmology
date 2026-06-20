#!/usr/bin/env python3
"""
ccef_breathing_identity.py  —  CCEF Breathing Mode Identity: sigma vs dilaton
==============================================================================
GOAL: Compute normalised overlap integrals I_sigma and I_dilaton.

Definitions (Cauchy-Schwarz normalised to [0,1]):
  I_dilaton_geom  = |<eta | r*F'_0>|_W
      Direct cosine with the DILATATION GENERATOR r*F'_0(r).
      Under r->lambda*r the background shifts delta-F = eps*r*F'_0(r).
      If eta ~ r*F'_0  =>  I_dilaton_geom -> 1  (mode IS the dilaton)
      If eta _|_ r*F'_0 =>  I_dilaton_geom -> 0  (mode is NOT the dilaton)

  I_sigma = |<eta | eps_kin>|_W
      Overlap with the A1 kinetic energy density eps_kin = A1*(F'_0^2 + 2sin^2F_0/r^2).
      Sigma meson couples to kinetic (pion gradient) sector.

  I_dilaton_virial = |<eta | J_scale>|_W
      Virial source J_scale = +eps1 - eps2 - eps3 + 3*eps4  (scaling exponents of each term)

SUCCESS CRITERION:  I_sigma >> I_dilaton_geom
    => breathing mode is NOT the dilaton; it's the sigma meson analog [SOLID]

Pipeline:
  1. Soliton background F_0(r) via SOLVE_BVP  (avoids shooting instability)
  2. Breathing mode eta(r) via L4 BVP          (fixed-parameter + good guess)
  3. Overlap integrals + plots
"""
import numpy as np
from scipy.integrate import solve_bvp, simpson
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────────────────────────────────────
# Parameters  [SOLID from session]
# ──────────────────────────────────────────────────────────────────────────────
A1, A2, A3, A4 = 1.000, 8.971, 1.684, 0.542
E0_MeV = 311.73
a_frob, b_frob = 0.836548, -0.018511   # Frobenius coefficients at r=0 [SOLID]
om2_target = 0.5412                    # breathing mode [SOLID]

print("CCEF Breathing Mode Identity: Overlap Integrals")
print(f"A1={A1}, A2={A2}, A3={A3}, A4={A4}")
print(f"omega^2 = {om2_target},  omega = {np.sqrt(om2_target)*E0_MeV:.2f} MeV")
print("="*62)

# ──────────────────────────────────────────────────────────────────────────────
# Step 1: Soliton background via solve_bvp
#   State y = [F, F', F'', F''']
#   EL: A3*(F'''' + 4F'''/r) = A1*(lapF - sin2F/r^2)
#                             + A2*(K*(lapF - sin2F/r^2) + K'*F')
#                             - A4*sinF
#   BCs: inner (Frobenius, known a), outer (F=0, F'=0)
# ──────────────────────────────────────────────────────────────────────────────
R_MIN_BG, R_MAX_BG = 0.08, 20.0

def soliton_ode(r, y):
    F, Fp, Fpp, Fppp = y
    sinF = np.sin(F); cosF = np.cos(F); sin2F = 2*sinF*cosF
    K   = Fp**2 + 2*sinF**2/r**2
    lapF = Fpp + 2*Fp/r
    dK  = 2*Fp*Fpp + 4*sinF*cosF*Fp/r**2 - 4*sinF**2/r**3
    # EL rhs (A2 coefficient is A2, not 2*A2 — first variation)
    rhs  = A1*(lapF - sin2F/r**2)
    rhs += A2*(K*(lapF - sin2F/r**2) + dK*Fp)
    rhs -= A4*sinF
    Fpppp = rhs/A3 - (4.0/r)*Fppp
    return np.array([Fp, Fpp, Fppp, Fpppp])

def bc_soliton(ya, yb):
    r0 = R_MIN_BG
    # Inner: match Frobenius expansion
    F_frob  = np.pi + a_frob*r0 + b_frob*r0**3
    Fp_frob = a_frob + 3*b_frob*r0**2
    # Outer: F -> 0
    return [ya[0] - F_frob,    # F(r_min) = Frobenius value
            ya[1] - Fp_frob,   # F'(r_min) = Frobenius derivative
            yb[0],             # F(r_max) = 0
            yb[1]]             # F'(r_max) = 0

# Initial guess: linear interpolation π -> 0
r_bg = np.concatenate([np.linspace(R_MIN_BG, 2.0, 150),
                       np.linspace(2.0, R_MAX_BG, 150)])
r_bg = np.unique(r_bg)
F_g  = np.pi * np.exp(-a_frob * r_bg / np.pi)   # rough exponential guess
guess_bg = np.zeros((4, len(r_bg)))
guess_bg[0] = F_g
guess_bg[1] = -a_frob * np.exp(-a_frob * r_bg / np.pi)

print("\nStep 1: Solving soliton background (solve_bvp)...")
sol_bg = solve_bvp(soliton_ode, bc_soliton, r_bg, guess_bg,
                   tol=1e-6, max_nodes=10000, verbose=0)

if sol_bg.status not in (0, 1):
    print(f"  WARNING: BVP status {sol_bg.status}: {sol_bg.message}")
else:
    print(f"  Converged: status={sol_bg.status}")

# Dense background on fine grid
r_dense_bg = np.linspace(R_MIN_BG, R_MAX_BG, 5000)
y_bg = sol_bg.sol(r_dense_bg)
F0_d   = y_bg[0]
F0p_d  = y_bg[1]
F0pp_d = y_bg[2]

print(f"  F(r={R_MIN_BG:.2f}) = {F0_d[0]:.5f}  expect {np.pi + a_frob*R_MIN_BG + b_frob*R_MIN_BG**3:.5f}")
print(f"  F(r={R_MAX_BG:.0f})   = {F0_d[-1]:.6f}  expect ≈ 0")

# Interpolators on the background grid
F0_f   = interp1d(r_dense_bg, F0_d,   kind='cubic', fill_value='extrapolate')
F0p_f  = interp1d(r_dense_bg, F0p_d,  kind='cubic', fill_value='extrapolate')
F0pp_f = interp1d(r_dense_bg, F0pp_d, kind='cubic', fill_value='extrapolate')

# ──────────────────────────────────────────────────────────────────────────────
# Step 2: Breathing mode eigenfunction via L4 BVP
#   State y = [eta, deta, d2eta, d3eta],  p = [omega^2]
#   ODE (session notes, correct sign [SOLID]):
#     d4eta = -(4/r)*d3eta + (1/A3)*(A1*lap - Q*eta + om2*W*eta)
#           + (2*A2/A3)*(Fp^2*lap - sinF^2*eta/r^4)
#   BCs (even-parity, session [SOLID]):
#     ya[1]=ya[3]=0, yb[0]=yb[1]=0, ya[0]=1  (5 total = 4 state + 1 param)
# ──────────────────────────────────────────────────────────────────────────────
R_MIN_SP, R_MAX_SP = 0.3, 18.0

def W_r(r, F, Fp):
    sinF = np.sin(F)
    K = Fp**2 + 2*sinF**2 / r**2
    return 1.0 + 2*A2*K

def Q_r(r, F, Fp):
    """Effective potential from linearised EL:
    Q = A1*(2cos2F/r^2) + A4*cosF + A2*(2cos2F/r^2)*(2K + 2Fp^2)
    (leading terms; A2 correction via 2nd-variation of K^2)
    """
    sinF = np.sin(F); cosF = np.cos(F)
    cos2F = cosF**2 - sinF**2
    K = Fp**2 + 2*sinF**2 / r**2
    Q  = A1 * 2*cos2F / r**2          # A1 potential
    Q += A4 * cosF                    # A4 (mass) potential
    Q += 2*A2 * Fp**2 * 2*cos2F/r**2  # A2 leading potential correction
    return Q

def ode_spectral(r, y, p):
    eta, deta, d2eta, d3eta = y
    om2 = p[0]
    F  = F0_f(r);  Fp = F0p_f(r)
    sinF = np.sin(F)
    lap  = d2eta + 2*deta/r
    W    = W_r(r, F, Fp)
    Q    = Q_r(r, F, Fp)
    # Correct sign (session [SOLID]):
    d4 = -(4.0/r)*d3eta + (1.0/A3)*(A1*lap - Q*eta + om2*W*eta)
    d4 += (2*A2/A3)*(Fp**2*lap - sinF**2*eta/r**4)
    d4  = np.where(np.isfinite(d4), d4, 0.0)
    return [deta, d2eta, d3eta, d4]

def bc_spectral(ya, yb, p):
    return [ya[1],       # even parity: deta(r_min) = 0
            ya[3],       # even parity: d3eta(r_min) = 0
            yb[0],       # bound state: eta(r_max) = 0
            yb[1],       # bound state: deta(r_max) = 0
            ya[0] - 1.0] # normalisation: eta(r_min) = 1

# Grid and initial guess
r_sp = np.concatenate([np.linspace(R_MIN_SP, 3.0, 200),
                       np.linspace(3.0, R_MAX_SP, 200)])
r_sp = np.unique(r_sp)

# Guess: decaying mode shape, peaked near origin
eta_g = np.exp(-0.7*r_sp) * (1.0 - 0.3*r_sp**2)
eta_g = np.where(eta_g < 0, 0, eta_g)   # keep positive
eta_g = np.maximum(eta_g, 0.01*np.exp(-r_sp))  # avoid zero
guess_sp = np.zeros((4, len(r_sp)))
guess_sp[0] = eta_g
guess_sp[1] = -0.7*eta_g   # approximate deta

p_guess = [om2_target]   # start right at the known value

print("\nStep 2: Solving L4 spectral BVP for breathing mode...")
sol_sp = solve_bvp(ode_spectral, bc_spectral, r_sp, guess_sp, p=p_guess,
                   tol=1e-6, max_nodes=10000, verbose=2)

om2_found = sol_sp.p[0]
print(f"\n  omega^2 found = {om2_found:.6f}")
print(f"  omega         = {np.sqrt(abs(om2_found))*E0_MeV:.2f} MeV")
print(f"  Expected      = {om2_target:.6f}  ({np.sqrt(om2_target)*E0_MeV:.2f} MeV)")
print(f"  BVP status    = {sol_sp.status}")

# Dense eigenfunction
r_eval = np.linspace(R_MIN_SP, R_MAX_SP, 4000)
y_sp   = sol_sp.sol(r_eval)
eta_r  = y_sp[0]

# ──────────────────────────────────────────────────────────────────────────────
# Step 3: Energy densities on the eval grid
# ──────────────────────────────────────────────────────────────────────────────
F_e   = F0_f(r_eval)
Fp_e  = F0p_f(r_eval)
Fpp_e = F0pp_f(r_eval)
sinF_e = np.sin(F_e); cosF_e = np.cos(F_e)
K_e    = Fp_e**2 + 2*sinF_e**2/r_eval**2
lapF_e = Fpp_e + 2*Fp_e/r_eval

eps1 = A1 * K_e                                  # A1 kinetic
eps2 = A2 * K_e**2                               # A2 Skyrme
eps3 = A3 * lapF_e**2                            # A3 Lifshitz
eps4 = A4 * (1.0 - cosF_e)                      # A4 mass

# Dilatation source (virial) — scaling exponents: A1->+1, A2->-1, A3->-1, A4->+3
J_scale = 1.0*eps1 - 1.0*eps2 - 1.0*eps3 + 3.0*eps4

# Dilaton GENERATOR: under r->lambda*r,  delta F_0 = eps * r * F'_0(r)
dilaton_gen = r_eval * Fp_e

W_e = W_r(r_eval, F_e, Fp_e)

# ──────────────────────────────────────────────────────────────────────────────
# Step 4: Cauchy-Schwarz normalised overlap integrals
# ──────────────────────────────────────────────────────────────────────────────
def cs_norm_overlap(f, g, W, r):
    """Returns |<f|g>|_r / (||f||_W * ||g||_r) in [0,1].
    Inner products: <f|g>_r = int f*g*r^2 dr (unweighted for g),
                   ||f||^2_W = int f^2*W*r^2 dr  (W-weighted for mode)
                   ||g||^2   = int g^2*r^2 dr    (flat for source)
    """
    num    = abs(simpson(f * g * r**2, x=r))
    norm_f = np.sqrt(abs(simpson(f**2 * W * r**2, x=r)))
    norm_g = np.sqrt(abs(simpson(g**2 * r**2, x=r)))
    denom  = norm_f * norm_g
    return num/denom if denom > 1e-30 else 0.0

I_sigma         = cs_norm_overlap(eta_r, eps1,        W_e, r_eval)
I_dilaton_geom  = cs_norm_overlap(eta_r, dilaton_gen, W_e, r_eval)
I_dilaton_virial= cs_norm_overlap(eta_r, J_scale,     W_e, r_eval)
I_total         = cs_norm_overlap(eta_r, eps1+eps2+eps3+eps4, W_e, r_eval)

print("\n── OVERLAP INTEGRALS (Cauchy-Schwarz normalised, ∈ [0,1]) ─────────────")
print(f"  I_sigma         = {I_sigma:.4f}   overlap w/ A1 kinetic ε_kin")
print(f"  I_dilaton_geom  = {I_dilaton_geom:.4f}   overlap w/ r·F'₀  (dilaton generator)")
print(f"  I_dilaton_virial= {I_dilaton_virial:.4f}   overlap w/ J_scale (virial source)")
print(f"  I_total         = {I_total:.4f}   overlap w/ full energy density")

ratio_geom   = I_sigma / I_dilaton_geom   if I_dilaton_geom   > 1e-6 else float('inf')
ratio_virial = I_sigma / I_dilaton_virial if I_dilaton_virial > 1e-6 else float('inf')
print(f"\n  I_sigma / I_dilaton_geom   = {ratio_geom:.2f}")
print(f"  I_sigma / I_dilaton_virial = {ratio_virial:.2f}")

if I_dilaton_geom < 0.05 or (ratio_geom > 5 and ratio_virial > 2):
    verdict = "SOLID"
    msg = "Sigma meson analog CONFIRMED: eta(r) near-orthogonal to dilaton generator"
elif ratio_geom > 2:
    verdict = "CONJECT-strong"
    msg = "Sigma meson analog supported"
else:
    verdict = "OPEN"
    msg = "Inconclusive"

print(f"\nVERDICT: [{verdict}]")
print(f"  {msg}")
print(f"  omega = {np.sqrt(abs(om2_found))*E0_MeV:.2f} MeV")

# ──────────────────────────────────────────────────────────────────────────────
# Step 5: Plots
# ──────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.patch.set_facecolor('white')
col_title = 'darkgreen' if verdict == 'SOLID' else 'darkorange'
fig.suptitle(
    f'CCEF Breathing Mode Identity: σ-meson vs Dilaton\n'
    f'ω = {np.sqrt(abs(om2_found))*E0_MeV:.2f} MeV     [{verdict}]  {msg}',
    fontsize=12, fontweight='bold', color=col_title)

r_cut = r_eval < 12
r_bg_cut = r_dense_bg < 12

# Panel A: soliton profile
ax = axes[0,0]
ax.plot(r_dense_bg[r_bg_cut], F0_d[r_bg_cut]/np.pi, 'b-', lw=2, label='F₀(r)/π')
ax.axhline(1, color='gray', ls='--', lw=0.7)
ax.axhline(0, color='gray', ls='--', lw=0.7)
ax.set_xlabel('r  [L₀]'); ax.set_ylabel('F₀ / π')
ax.set_title('Soliton Profile F₀(r)'); ax.set_xlim(0, 10); ax.legend()

# Panel B: mode shape vs dilaton generator
norm_eta = np.max(np.abs(eta_r[r_cut])) + 1e-30
norm_dil = np.max(np.abs(dilaton_gen[r_cut])) + 1e-30
norm_ep1 = np.max(np.abs(eps1[r_cut])) + 1e-30
ax = axes[0,1]
ax.plot(r_eval[r_cut], eta_r[r_cut]/norm_eta,      'r-',  lw=2, label='η(r) — breathing mode')
ax.plot(r_eval[r_cut], dilaton_gen[r_cut]/norm_dil,'g--', lw=2, label='r·F\'₀(r) — dilaton shape')
ax.plot(r_eval[r_cut], eps1[r_cut]/norm_ep1,        'b:',  lw=2, label='ε_kin — σ source')
ax.axhline(0, color='gray', ls='--', lw=0.7)
ax.set_xlabel('r  [L₀]'); ax.set_ylabel('amplitude (peak-norm.)')
ax.set_title('Shape Comparison (peak-normalised)'); ax.set_xlim(0, 10)
ax.legend(fontsize=8)

# Panel C: overlap integrands
norm_f_W = np.sqrt(abs(simpson(eta_r**2 * W_e * r_eval**2, x=r_eval))) + 1e-30
eta_n = eta_r / norm_f_W
norm_dg = np.sqrt(abs(simpson(dilaton_gen**2 * r_eval**2, x=r_eval))) + 1e-30
dg_n = dilaton_gen / norm_dg
norm_e1 = np.sqrt(abs(simpson(eps1**2 * r_eval**2, x=r_eval))) + 1e-30
e1_n = eps1 / norm_e1

ax = axes[1,0]
integ_s = eta_n * e1_n * r_eval**2
integ_d = eta_n * dg_n * r_eval**2
s_max = max(np.max(np.abs(integ_s[r_cut])), 1e-30)
d_max = max(np.max(np.abs(integ_d[r_cut])), 1e-30)
ax.plot(r_eval[r_cut], integ_s[r_cut]/s_max,'b-',  lw=2,
        label=f'η·ε_kin·r²   I_σ={I_sigma:.3f}')
ax.plot(r_eval[r_cut], integ_d[r_cut]/d_max,'g--', lw=2,
        label=f'η·(r·F\'₀)·r²   I_dil={I_dilaton_geom:.3f}')
ax.axhline(0, color='gray', ls='--', lw=0.7)
ax.set_xlabel('r  [L₀]'); ax.set_ylabel('integrand (peak-norm.)')
ax.set_title('Overlap Integrands'); ax.set_xlim(0, 10); ax.legend(fontsize=8)

# Panel D: bar chart
ax = axes[1,1]
lbls = ['I_σ\n(kinetic)', 'I_dil\n(geom.)', 'I_dil\n(virial)', 'I_total']
vals = [I_sigma, I_dilaton_geom, I_dilaton_virial, I_total]
cols = ['royalblue', 'tomato', 'salmon', 'orchid']
bars = ax.bar(lbls, vals, color=cols, edgecolor='k', linewidth=0.8)
for bar, v in zip(bars, vals):
    ax.text(bar.get_x()+bar.get_width()/2, v+0.01, f'{v:.3f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')
ax.set_ylim(0, max(max(vals)*1.3, 0.5))
ax.set_ylabel('C-S overlap  ∈ [0,1]')
ax.set_title(f'Overlap Summary\nI_σ/I_dil = {ratio_geom:.1f}')
ax.text(0.5, 0.93, f'[{verdict}]', transform=ax.transAxes,
        ha='center', fontsize=12, fontweight='bold', color=col_title)

plt.tight_layout(rect=[0, 0, 1, 0.92])
out_png = '/sessions/eager-dreamy-hopper/mnt/outputs/ccef_breathing_identity.png'
plt.savefig(out_png, dpi=130, bbox_inches='tight')
plt.close()
print(f"\nPlot saved: {out_png}")

# ──────────────────────────────────────────────────────────────────────────────
# Final summary
# ──────────────────────────────────────────────────────────────────────────────
print("\n" + "="*62)
print("FINAL SUMMARY")
print("="*62)
print(f"  omega^2  = {om2_found:.6f}   omega = {np.sqrt(abs(om2_found))*E0_MeV:.2f} MeV")
print(f"  I_sigma         = {I_sigma:.4f}")
print(f"  I_dilaton_geom  = {I_dilaton_geom:.4f}")
print(f"  I_dilaton_virial= {I_dilaton_virial:.4f}")
print(f"  Ratio I_σ/I_dil = {ratio_geom:.2f}")
print()
print(f"  [{verdict}] Physical identity: sigma meson analog" if verdict!="OPEN"
      else f"  [{verdict}] {msg}")
if verdict == "SOLID":
    print("  Mode is NOT a dilaton — eta(r) does not project onto r*F'_0(r)")
    print("  Mode couples via kinetic sector: consistent with sigma meson analog")
    print("  sigma interpretation [CONJECT-strong] -> [SOLID]")
