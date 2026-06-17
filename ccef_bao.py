"""
CCEF BAO Angular Shift Prediction
===================================
The CCEF H(z) formula (Task 24) modifies the comoving distance chi(z)
at z < z_trans = 0.181. Since r_s (sound horizon) is set at z_drag ~ 1060
(well before G_eff activates at z_onset ~ 10 and before z_trans ~ 0.18),
r_s^CCEF = r_s^LCDM  [SOLID].

But D_A(z) = chi(z)/(1+z) IS modified because chi(z) integrates 1/H(z')
from 0 to z, and H_CCEF(z<z_trans) > H_LCDM(z<z_trans).

Result: apparent BAO angle theta_BAO = r_s/D_A is LARGER in CCEF at z < z_trans
(smaller D_A -> larger apparent angle -> BAO peak shifts to larger angles).
This is a testable prediction for DESI/Euclid.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

Omega_r  = 5.4e-5
Omega_b  = 0.049
Omega_DM = 0.268
Omega_m  = Omega_b + Omega_DM
Omega_L  = 0.683
H0_CMB   = 67.4     # km/s/Mpc
z_trans  = 0.181
a_trans  = 1.0 / (1.0 + z_trans)
Omega_cond_DE = Omega_DM*(1+z_trans)**3 + Omega_L

# H(z) in units of H0_CMB
def E_LCDM(z):
    a = 1/(1+z)
    return np.sqrt(Omega_r/a**4 + Omega_m/a**3 + Omega_L)

def E_CCEF(z):
    a = 1/(1+z)
    if z > z_trans:
        return np.sqrt(Omega_r/a**4 + Omega_m/a**3 + Omega_L)
    else:
        return np.sqrt(Omega_r/a**4 + Omega_b/a**3 + Omega_cond_DE)

# Comoving distance chi(z) = c/H0 * int_0^z dz'/E(z')
# in units of c/H0  (= 1 unit)
def chi(z_max, E_func, N=5000):
    z_arr = np.linspace(0, z_max, N)
    integrand = np.array([1.0/E_func(zz) for zz in z_arr])
    return np.trapz(integrand, z_arr)

# Sound horizon at drag epoch (z_drag ~ 1060), same for both
# r_s ~ 147.09 Mpc (Planck 2018) [SOLID, G_eff inactive at z_drag]
r_s_Mpc = 147.09   # Mpc

# c/H0 in Mpc
c_H0_Mpc = 3e5 / H0_CMB   # = 4451 Mpc

print("="*60)
print("CCEF BAO ANGULAR SHIFT PREDICTION")
print("="*60)
print(f"[SOLID]   r_s = {r_s_Mpc:.2f} Mpc  (unchanged from LCDM)")
print(f"[CONJECT] z_trans = {z_trans}  (H_CCEF > H_LCDM at z < z_trans)")
print(f"  H_CCEF(z=0) / H_LCDM(z=0) = {E_CCEF(0)/E_LCDM(0):.4f}")
print(f"  (= sqrt(Omega_cond_DE) = sqrt({Omega_cond_DE:.3f}) / sqrt(Omega_L) ratio)")

# BAO redshifts (DESI survey bins)
z_bao = np.array([0.15, 0.38, 0.51, 0.70, 0.85, 1.10, 1.48, 2.33])
print(f"\n{'z':>5} {'chi_LCDM':>10} {'chi_CCEF':>10} {'D_A_L':>9} {'D_A_C':>9} {'delta_theta/theta':>17} note")
print("-"*80)
for z in z_bao:
    cl = chi(z, E_LCDM) * c_H0_Mpc
    cc = chi(z, E_CCEF) * c_H0_Mpc
    DA_l = cl / (1+z)
    DA_c = cc / (1+z)
    theta_l = r_s_Mpc / DA_l
    theta_c = r_s_Mpc / DA_c
    dtheta = (theta_c - theta_l) / theta_l * 100
    note = "<z_trans" if z < z_trans else ">z_trans"
    print(f"  {z:.2f}  {cl:9.1f}  {cc:9.1f}  {DA_l:8.1f}  {DA_c:8.1f}  {dtheta:+.3f}%   {note}")

# Full curve
z_arr = np.linspace(0.01, 3.0, 300)
chi_L = np.array([chi(z, E_LCDM)*c_H0_Mpc for z in z_arr])
chi_C = np.array([chi(z, E_CCEF)*c_H0_Mpc for z in z_arr])
DA_L  = chi_L / (1 + z_arr)
DA_C  = chi_C / (1 + z_arr)
theta_L = r_s_Mpc / DA_L
theta_C = r_s_Mpc / DA_C
dtheta_pct = (theta_C - theta_L) / theta_L * 100

# H(z) ratio
E_L = np.array([E_LCDM(z) for z in z_arr])
E_C = np.array([E_CCEF(z) for z in z_arr])
H_ratio = E_C / E_L

print(f"\n[CONJECT] Max angular shift (z < z_trans): {max(dtheta_pct[z_arr<z_trans]):+.3f}%")
print(f"[CONJECT] Angular shift at z=0.15: {np.interp(0.15, z_arr, dtheta_pct):+.3f}%")
print(f"[CONJECT] Angular shift at z=0.38: {np.interp(0.38, z_arr, dtheta_pct):+.3f}%  (> z_trans, small)")
print(f"[CONJECT] Angular shift at z=1.0:  {np.interp(1.0,  z_arr, dtheta_pct):+.3f}%  (> z_trans, ~const)")
print(f"\n[SOLID]   r_s^CCEF = r_s^LCDM = {r_s_Mpc} Mpc  (G_eff inactive at z_drag~1060)")
print(f"[CONJECT] Apparent BAO angle LARGER at z < z_trans (smaller D_A)")
print(f"[CONJECT] Asymptotic shift at z >> z_trans: {np.mean(dtheta_pct[z_arr>1.0]):+.3f}%  (from chi offset at z_trans)")
print(f"[OPEN]    DESI/Euclid can test this: ~{abs(np.interp(0.15, z_arr, dtheta_pct)):.2f}% shift at z~0.15")

# Figure
fig, axes = plt.subplots(1, 3, figsize=(15, 5), facecolor='#0d1117')
fig.suptitle('CCEF BAO Angular Shift Prediction  [CONJECT]\n'
             r'$r_s^{\rm CCEF}=r_s^{\rm LCDM}$ (sound horizon unchanged), '
             r'$D_A$ modified at $z < z_{\rm trans}=0.181$',
             color='white', fontsize=11, y=1.02)

C_PURPLE='#d2a8ff'; C_CYAN='#79c0ff'; C_GOLD='#f1e05a'
C_GREEN='#56d364'; C_RED='#f85149'; C_ORANGE='#ffa657'

for ax in axes:
    ax.set_facecolor('#161b22')
    ax.tick_params(colors='white', labelsize=9)
    for sp in ax.spines.values(): sp.set_edgecolor('#30363d')
    ax.xaxis.label.set_color('white'); ax.yaxis.label.set_color('white')
    ax.title.set_color('white')

# Panel 1: H(z)/H_LCDM(z)
axes[0].plot(z_arr, H_ratio, color=C_CYAN, lw=2.5)
axes[0].axhline(1.0, color='white', lw=0.8, ls='--', alpha=0.4)
axes[0].axvline(z_trans, color=C_GOLD, lw=1.5, ls=':', alpha=0.8)
axes[0].fill_between(z_arr[z_arr<=z_trans], 1.0,
                     H_ratio[z_arr<=z_trans], alpha=0.25, color=C_CYAN)
axes[0].text(0.04, 0.85, f'H_CCEF/H_LCDM at z=0\n= {E_CCEF(0)/E_LCDM(0):.4f}',
             transform=axes[0].transAxes, color=C_CYAN, fontsize=8.5,
             bbox=dict(facecolor='#21262d', alpha=0.7, edgecolor='none', pad=3))
axes[0].text(z_trans+0.01, 1.015, f'$z_{{\\rm trans}}={z_trans}$', color=C_GOLD, fontsize=8.5)
axes[0].set_xlabel('Redshift $z$', fontsize=9)
axes[0].set_ylabel('$H_{\\rm CCEF}(z)/H_{\\rm LCDM}(z)$', fontsize=9)
axes[0].set_title('(a) Hubble Rate Ratio', fontsize=10)
axes[0].set_xlim(0, 3); axes[0].set_ylim(0.95, 1.10)

# Panel 2: D_A(z) comparison
axes[1].plot(z_arr, DA_L/1000, color=C_PURPLE, lw=2.5, label='LCDM')
axes[1].plot(z_arr, DA_C/1000, color=C_CYAN, lw=2.5, ls='--',
             label='CCEF  [CONJECT]')
axes[1].axvline(z_trans, color=C_GOLD, lw=1.5, ls=':', alpha=0.8)
for z in z_bao[:4]:
    da_l = np.interp(z, z_arr, DA_L)
    da_c = np.interp(z, z_arr, DA_C)
    axes[1].annotate('', xy=(z, da_c/1000), xytext=(z, da_l/1000),
                     arrowprops=dict(arrowstyle='<->', color=C_ORANGE, lw=1.2))
axes[1].legend(fontsize=8.5, facecolor='#21262d', labelcolor='white', framealpha=0.8)
axes[1].set_xlabel('Redshift $z$', fontsize=9)
axes[1].set_ylabel('$D_A(z)$ [Gpc]', fontsize=9)
axes[1].set_title('(b) Angular Diameter Distance', fontsize=10)
axes[1].set_xlim(0, 3)

# Panel 3: delta theta / theta
axes[2].plot(z_arr, dtheta_pct, color=C_GREEN, lw=2.5,
             label=r'$\delta\theta_{\rm BAO}/\theta_{\rm BAO}$  [CONJECT]')
axes[2].axhline(0, color='white', lw=0.8, ls='--', alpha=0.4)
axes[2].axvline(z_trans, color=C_GOLD, lw=1.5, ls=':', alpha=0.8,
                label=f'$z_{{\\rm trans}}={z_trans}$')
axes[2].fill_between(z_arr, 0, dtheta_pct, where=(dtheta_pct>0),
                     alpha=0.2, color=C_GREEN)
# DESI survey bins
for z in z_bao:
    dt = np.interp(z, z_arr, dtheta_pct)
    axes[2].scatter(z, dt, color=C_ORANGE, s=60, zorder=5)
axes[2].text(0.04, 0.85, '[CONJECT]\nBAO peak shifts to\nlarger angles at z<z_trans',
             transform=axes[2].transAxes, color=C_GREEN, fontsize=8,
             bbox=dict(facecolor='#21262d', alpha=0.7, edgecolor='none', pad=3))
axes[2].set_xlabel('Redshift $z$', fontsize=9)
axes[2].set_ylabel(r'$\delta\theta_{\rm BAO}/\theta_{\rm BAO}$ [%]', fontsize=9)
axes[2].set_title('(c) Apparent BAO Angular Shift', fontsize=10)
axes[2].legend(fontsize=8.5, facecolor='#21262d', labelcolor='white', framealpha=0.8)
axes[2].set_xlim(0, 3)

plt.tight_layout()
plt.savefig('/sessions/confident-inspiring-knuth/mnt/outputs/ccef_bao.png',
            dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.close()
print("\nFigure saved.")
