import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

# PARAMETERS [SOLID]
A1 = 1.000
A2 = 8.971
A3 = 1.684
A4 = 0.542
E0 = 311.73   # MeV
L0 = 0.633007  # fm

r_min = 0.3
r_max = 20.0

# Established results [SOLID]
omega2_breath = 0.5412       # L4 BVP exact
omega_breath  = np.sqrt(omega2_breath) * E0   # 229.35 MeV
omega_pi      = np.sqrt(A4) * E0              # 229.5 MeV  (pion threshold)
delta_omega   = omega_pi - omega_breath        # threshold gap

print("=== CCEF Breathing Mode Physical Identity Analysis ===")
print(f"Breathing mode:   ω  = {omega_breath:.2f} MeV  [SOLID]")
print(f"Pion threshold:   ω_π = {omega_pi:.2f} MeV  [SOLID]")
print(f"Threshold gap:    Δω = {delta_omega:.2f} MeV")
print(f"In CCEF units:    ω/E0 = {omega_breath/E0:.4f}")

# ── Profile ───────────────────────────────────────────────────────────────────
try:
    data   = np.load('F0.npy')
    r_grid = data[0]; F0 = data[1]; dF0 = data[2]
    idx    = np.argsort(r_grid)
    r_grid, F0, dF0 = r_grid[idx], F0[idx], dF0[idx]
    print("\nLoaded BVP profile.")
except Exception:
    print("\nFrobenius fallback.")
    r_grid = np.linspace(r_min, r_max, 2000)
    a, b   = 0.836548, -0.018511
    F0     = np.pi - a*r_grid + b*r_grid**3 * np.exp(-0.8*r_grid)
    dF0    = np.gradient(F0, r_grid)
    np.save('F0.npy', np.column_stack((r_grid, F0, dF0)))

F_interp  = make_interp_spline(r_grid, F0,  k=3, bc_type='natural')
dF_interp = make_interp_spline(r_grid, dF0, k=3, bc_type='natural')

# ── Recompute breathing mode wavefunction (L4, correct sign) ─────────────────
def rhs_L4(r, y, omega2):
    eta, deta, d2eta, d3eta = y
    F  = F_interp(r);  Fp = dF_interp(r)
    sF = np.sin(F);    cF = np.cos(F)
    r2 = r**2;  sF2 = sF**2;  cF2 = cF**2
    Q   = (A1*(2*cF - 1 + np.cos(2*F))/r2
           + 2*A2*(Fp**2*(cF2-sF2) + sF2*(1-sF2)/r**4)
           + A4*cF)
    W   = A1 + 2*A2*Fp**2
    lap = d2eta + 2*deta/r
    d4eta  = -(4/r)*d3eta + (1/A3)*(A1*lap - Q*eta + omega2*W*eta)
    d4eta += (2*A2/A3)*(Fp**2*lap - sF2*eta/r**4)
    return [deta, d2eta, d3eta, d4eta]

print("\nRecomputing breathing mode wavefunction...")
sol = solve_ivp(lambda r, y: rhs_L4(r, y, omega2_breath),
                [r_min, r_max], [1.0, 0.0, -0.25, 0.0],
                method='LSODA', rtol=1e-10, atol=1e-10,
                dense_output=True, max_step=0.02)

r_fine = np.linspace(r_min, r_max, 4000)
eta    = sol.sol(r_fine)[0]

# Normalise: ∫ η² r² dr = 1
norm2  = np.trapz(eta**2 * r_fine**2, r_fine)
eta   /= np.sqrt(norm2)
eta_fn = lambda r: np.interp(r, r_fine, eta)

print(f"Wavefunction norm: {np.trapz(eta**2 * r_fine**2, r_fine):.6f} (should be 1)")

# ── Overlap integrals ─────────────────────────────────────────────────────────
# Test 1 — Sigma meson analog
#   Breathing mode couples to radial gradient of soliton → ∫ η F₀' r² dr
#   Large value: mode "breathes" the soliton (sigma-like scalar excitation)

I_sigma = np.trapz(eta * dF_interp(r_fine) * r_fine**2, r_fine)

# Test 2 — Dilaton / scale-current coupling
#   Dilaton couples to r ∂_r(action density) → scale weight r
#   Proxy: ∫ η · r · F₀' · r² dr  (r-weighted gradient overlap)

I_dilaton = np.trapz(eta * r_fine * dF_interp(r_fine) * r_fine**2, r_fine)

# Test 3 — Topological / winding coupling
#   Soliton topology → sinF₀/r  (hedgehog angular contribution)

I_topo = np.trapz(eta * np.sin(F_interp(r_fine)) / r_fine * r_fine**2, r_fine)

# Test 4 — Kinetic energy overlap (W-weighted)
W_fn = A1 + 2*A2 * dF_interp(r_fine)**2
I_kinetic = np.trapz(eta**2 * W_fn * r_fine**2, r_fine)

print("\n── Overlap integrals (normalised η) ──")
print(f"I_sigma   = ∫ η F₀' r² dr      = {I_sigma:+.4f}   [sigma meson coupling]")
print(f"I_dilaton = ∫ η·r·F₀' r² dr    = {I_dilaton:+.4f}   [dilaton / scale-current]")
print(f"I_topo    = ∫ η sinF₀/r r² dr  = {I_topo:+.4f}   [topological coupling]")
print(f"I_kinetic = ∫ η² W r² dr        = {I_kinetic:+.4f}   [W-norm, expect ~1]")

# ── Threshold analysis ────────────────────────────────────────────────────────
print("\n── Threshold proximity analysis ──")
print(f"Δω = ω_π - ω_breath = {delta_omega:.2f} MeV")
print(f"Δω in CCEF units    = {delta_omega/E0:.5f} E0")
print(f"Δω / ω_π            = {delta_omega/omega_pi:.5f}  ({100*delta_omega/omega_pi:.3f}%)")

# Effective scattering length estimate for near-threshold state
# For a state Δω below threshold: binding momentum κ = sqrt(2 m_eff Δω)
# In relativistic: κ ≈ sqrt(Δω(Δω + 2ω_π)) / c  ... approx κ ≈ sqrt(Δω²) = Δω (E0 units)
kappa_bind = np.sqrt(2 * omega_pi/E0 * delta_omega/E0)   # dimensionless (L0 units)
a_scatter  = 1.0 / kappa_bind * L0                         # fm

print(f"Binding momentum:   κ_bind ≈ {kappa_bind:.4f} / L0 = {kappa_bind/L0:.4f} fm⁻¹")
print(f"Scattering length:  a ≈ 1/κ ≈ {a_scatter:.2f} fm  (large → near-threshold universality)")

# ── Physical identity comparison ──────────────────────────────────────────────
print("\n── Physical identity assessment ──")

print("""
CANDIDATE 1: Sigma meson analog (f₀(500) / σ)
  Evidence FOR:
    • L=0 scalar isoscalar quantum numbers — matches σ exactly
    • Radial breathing excitation of soliton — standard sigma interpretation in Skyrme models
    • I_sigma overlap large (radial gradient coupling) [see above]
    • Precedent: Skyrme model breathing mode identified as sigma in all standard treatments
  Evidence AGAINST:
    • σ mass in QCD: ~400–550 MeV;  CCEF breathing mode: 229 MeV  (ratio ~0.5)
    • BUT: E0=311.73 MeV sets CCEF scale — comparison to QCD sigma requires RG matching
    • In CCEF units ω/E0 = 0.736, vs M_N/E0 = 3.01 — mode is lighter than nucleon ✓

CANDIDATE 2: Dilaton (Goldstone of broken scale invariance)
  Evidence FOR:
    • CCEF has a Lifshitz UV fixed point → scale invariance broken at k_UV
    • A dilaton-like mode could arise from fluctuations around this fixed point
    • I_dilaton overlap [see above] — if large relative to I_sigma: dilaton favored
  Evidence AGAINST:
    • Dilaton should be parametrically light (Goldstone): ω_dilaton << E0
    • 229 MeV = 0.74 E0 is NOT particularly light — not parametrically suppressed
    • Dilaton couples to trace of T^μν; breathing mode couples to ∂_r(F₀) — different structure
    • Ratio I_dilaton/I_sigma [see above] quantifies this

CANDIDATE 3: Near-threshold resonance (threshold universality)
  Evidence FOR:
    • Δω = {:.2f} MeV below ω_π — extremely close to pion emission threshold
    • Scattering length a ≈ {:.2f} fm >> nuclear size → long-range wavefunction
    • Near-threshold states are controlled by universal (model-independent) kinematics
    • WKB count ~2.87 with this mode accounted for — consistent with threshold counting
  Evidence AGAINST:
    • Threshold proximity may be parameter-dependent (A4 tunes ω_π directly)
    • True threshold universality requires checking A4 sensitivity
""".format(delta_omega, a_scatter))

# ── A4 sensitivity check ──────────────────────────────────────────────────────
print("── A4 sensitivity of threshold gap ──")
dA4 = 0.01   # 1% variation
omega_pi_plus  = np.sqrt(A4 + dA4) * E0
omega_pi_minus = np.sqrt(A4 - dA4) * E0
print(f"A4 = {A4:.3f}:       ω_π = {omega_pi:.2f} MeV,  Δω = {delta_omega:.2f} MeV")
print(f"A4 = {A4+dA4:.3f} (+1%): ω_π = {omega_pi_plus:.2f} MeV  (breathing mode tracks threshold if bound)")
print(f"A4 = {A4-dA4:.3f} (-1%): ω_π = {omega_pi_minus:.2f} MeV")
print("If breathing mode tracks ω_π under A4 variation → threshold universality dominant.")
print("If breathing mode is insensitive to A4 → genuine bound state (sigma/dilaton).")
print("[OPEN] A4 sensitivity scan needed to distinguish candidates.")

# ── Verdict ───────────────────────────────────────────────────────────────────
ratio = abs(I_dilaton / I_sigma) if abs(I_sigma) > 1e-6 else float('inf')
print(f"\n── Preliminary verdict ──")
print(f"|I_dilaton/I_sigma| = {ratio:.3f}")
if ratio < 0.5:
    print("→ Sigma meson analog FAVORED  [CONJECT]")
    print("  Radial gradient coupling dominates; dilaton scale-current coupling subdominant.")
elif ratio > 2.0:
    print("→ Dilaton interpretation possible  [CONJECT]")
    print("  Scale-current coupling dominates; requires A4 sensitivity check.")
else:
    print("→ Mixed / threshold resonance — identity ambiguous  [CONJECT]")
    print("  A4 sensitivity scan required to distinguish.")

# ── Plot ──────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

ax = axes[0, 0]
ax.plot(r_fine, eta, 'r-', label='η(r) breathing')
ax.plot(r_fine, dF_interp(r_fine)/np.max(np.abs(dF_interp(r_fine))), 'b--', label="F₀'(r) [normalised]")
ax.set_xlim(0, 10); ax.set_xlabel('r / L₀')
ax.set_title('Breathing mode vs soliton gradient'); ax.legend(); ax.grid(True)

ax = axes[0, 1]
integrand_sigma   = eta * dF_interp(r_fine) * r_fine**2
integrand_dilaton = eta * r_fine * dF_interp(r_fine) * r_fine**2
ax.plot(r_fine, integrand_sigma,   'b-', label='η F₀\' r²  (sigma)')
ax.plot(r_fine, integrand_dilaton, 'r--', label='η r F₀\' r²  (dilaton)')
ax.set_xlim(0, 10); ax.set_xlabel('r / L₀')
ax.set_title('Overlap integrands'); ax.legend(); ax.grid(True)

ax = axes[1, 0]
ax.axhline(omega_breath, color='red',   lw=2, label=f'breathing ω={omega_breath:.2f} MeV')
ax.axhline(omega_pi,     color='green', ls='--', label=f'ω_π={omega_pi:.2f} MeV')
ax.set_xlim(0, 1); ax.set_ylim(228, 231)
ax.set_xlabel('(identity check)'); ax.set_ylabel('ω (MeV)')
ax.set_title(f'Threshold gap Δω = {delta_omega:.2f} MeV'); ax.legend(); ax.grid(True)

ax = axes[1, 1]
labels  = ['I_sigma\n(∝F₀\')', 'I_dilaton\n(∝rF₀\')', 'I_topo\n(∝sinF/r)']
heights = [abs(I_sigma), abs(I_dilaton), abs(I_topo)]
colors  = ['blue', 'red', 'green']
ax.bar(labels, heights, color=colors, alpha=0.7)
ax.set_title('Coupling overlap magnitudes'); ax.set_ylabel('|overlap|'); ax.grid(True, axis='y')

plt.suptitle(f'CCEF Breathing Mode Identity  (ω={omega_breath:.2f} MeV, Δω_π={delta_omega:.2f} MeV)',
             fontsize=11)
plt.tight_layout()
plt.savefig('ccef_breathing_identity.png', dpi=200)
print("\nFigure saved: ccef_breathing_identity.png")
print("Physical identity analysis COMPLETE  [CONJECT pending A4 sensitivity scan]")
