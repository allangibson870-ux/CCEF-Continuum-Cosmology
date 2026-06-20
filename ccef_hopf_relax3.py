"""
ccef_hopf_relax3.py  — CCEF Hopf soliton relaxation, Step 3b
Load best field (120x240), interpolate to 160x320, run L-BFGS-B.
Target: |virial/E_tot| < 0.01

Parameters: A1=1.000, A3=1.684, A4=0.542
Virial theorem: E_A1 - E_A3 + 3*E_A4 = 0 at minimum
"""

import numpy as np
from scipy.optimize import minimize
from scipy.interpolate import RegularGridInterpolator

# ── parameters ──────────────────────────────────────────────────────────────
A1, A3, A4 = 1.000, 1.684, 0.542

OUTDIR = '/sessions/eager-dreamy-hopper/mnt/outputs/'

# ── load previous best field (120x240, domain 0..16 x -16..16) ──────────────
Th_old  = np.load(OUTDIR + 'hopf_converged_Theta.npy')
Ph_old  = np.load(OUTDIR + 'hopf_converged_Phi.npy')
rho_old = np.load(OUTDIR + 'hopf_converged_rho.npy')
z_old   = np.load(OUTDIR + 'hopf_converged_z.npy')
print(f"Loaded: Theta {Th_old.shape}, rho [{rho_old[0]:.4f},{rho_old[-1]:.4f}]"
      f"  z [{z_old[0]:.4f},{z_old[-1]:.4f}]")

# ── new 160x320 grid — same domain ──────────────────────────────────────────
Nr, Nz   = 160, 320
rho_max  = 16.0
z_max    = 16.0
rho = np.linspace(1e-3, rho_max, Nr)
z   = np.linspace(-z_max, z_max, Nz)
drho = rho[1] - rho[0]
dz   = z[1]   - z[0]
RHO, Z = np.meshgrid(rho, z, indexing='ij')
pts = np.stack([RHO.ravel(), Z.ravel()], axis=1)

print(f"New grid: {Nr}x{Nz}, drho={drho:.4f}, dz={dz:.4f}")

# ── interpolate Theta (scalar) ───────────────────────────────────────────────
Th0 = RegularGridInterpolator(
    (rho_old, z_old), Th_old, method='linear',
    bounds_error=False, fill_value=0.0
)(pts).reshape(Nr, Nz)

# ── interpolate Phi via cos/sin to avoid branch-cut wrapping ────────────────
cP_i = RegularGridInterpolator(
    (rho_old, z_old), np.cos(Ph_old), method='linear',
    bounds_error=False, fill_value=1.0
)(pts).reshape(Nr, Nz)
sP_i = RegularGridInterpolator(
    (rho_old, z_old), np.sin(Ph_old), method='linear',
    bounds_error=False, fill_value=0.0
)(pts).reshape(Nr, Nz)
Ph0 = np.arctan2(sP_i, cP_i)

# ── enforce axis BC: sinΘ(0,z) = 0 via soft mask re-application ─────────────
# The mask was b=0.8 in the original ansatz; we re-enforce it on the
# interpolated field so the boundary condition is clean on the new grid.
# Do NOT re-apply if the field already has sinΘ near 0 on axis (it should).
axis_sin = np.abs(np.sin(Th0[0, :]))
print(f"sinΘ on axis (row 0): max={axis_sin.max():.2e}  mean={axis_sin.mean():.2e}")

# boundary: set Θ to 0 at rho_max and z boundaries (field → vacuum)
Th0[0,  :] = 0.0   # axis (sin=0 there anyway)
Th0[-1, :] = 0.0   # rho_max
Th0[:,  0] = 0.0   # z_min
Th0[:, -1] = 0.0   # z_max

# ── differential operators ───────────────────────────────────────────────────
def lap(f):
    fr = np.gradient(f, drho, axis=0)
    return np.gradient(fr, drho, axis=0) + fr / RHO + np.gradient(
        np.gradient(f, dz, axis=1), dz, axis=1)

def div(P, Q):
    return np.gradient(P, drho, axis=0) + P / RHO + np.gradient(Q, dz, axis=1)

def Phgrad(Ph):
    sP, cP = np.sin(Ph), np.cos(Ph)
    return (cP * np.gradient(sP, drho, axis=0) - sP * np.gradient(cP, drho, axis=0),
            cP * np.gradient(sP, dz,  axis=1) - sP * np.gradient(cP, dz,  axis=1))

# ── energy + gradient function ───────────────────────────────────────────────
def energy_and_grad(x):
    Th = x[:Nr*Nz].reshape(Nr, Nz)
    Ph = x[Nr*Nz:].reshape(Nr, Nz)
    sT, cT = np.sin(Th), np.cos(Th)
    Tr = np.gradient(Th, drho, axis=0)
    Tz = np.gradient(Th, dz,   axis=1)
    Pr, Pz = Phgrad(Ph)
    gT2 = Tr**2 + Tz**2
    gP2 = Pr**2 + Pz**2
    gTP = Tr*Pr + Tz*Pz
    g2  = gT2 + gP2 + 1.0/RHO**2
    DT  = lap(Th)
    DP  = div(Pr, Pz)
    Ac  = cT*DT - sT*g2
    Bc  = sT*DP + 2.0*cT*gTP
    Cc  = -sT*DT - cT*gT2

    # energy density
    e_A1 = (A1/2.0) * (gT2 + sT**2 * (gP2 + 1.0/RHO**2))
    e_A3 = (A3/2.0) * (Ac**2 + Bc**2 + Cc**2)
    e_A4 = (A4/2.0) * (1.0 - cT)**2

    w = 2.0 * np.pi * RHO
    E_A1 = float(np.trapezoid(np.trapezoid(w * e_A1, z, axis=1), rho))
    E_A3 = float(np.trapezoid(np.trapezoid(w * e_A3, z, axis=1), rho))
    E_A4 = float(np.trapezoid(np.trapezoid(w * e_A4, z, axis=1), rho))
    E    = E_A1 + E_A3 + E_A4

    # functional derivatives δE/δΘ, δE/δΦ (derived via IBP)
    gTh = (A1 * (-DT + sT*cT*(gP2 + 1.0/RHO**2)) + A4 * sT*(1.0 - cT)
           + A3 * (Ac*(-sT*DT - cT*g2)
                   + Bc*(cT*DP - 2.0*sT*gTP)
                   + Cc*(-cT*DT + sT*gT2)
                   + lap(Ac*cT - Cc*sT)
                   + 2.0*div(Ac*sT*Tr, Ac*sT*Tz)
                   - 2.0*div(Bc*cT*Pr, Bc*cT*Pz)
                   + 2.0*div(Cc*cT*Tr, Cc*cT*Tz)))

    gPh = (-A1 * div(sT**2*Pr, sT**2*Pz)
           + A3 * (2.0*div(Ac*sT*Pr, Ac*sT*Pz)
                   + lap(Bc*sT)
                   - 2.0*div(Bc*cT*Tr, Bc*cT*Tz)))

    # zero gradients at all boundaries (Dirichlet enforcement)
    for g in (gTh, gPh):
        g[0,  :] = 0.0
        g[-1, :] = 0.0
        g[:,  0] = 0.0
        g[:, -1] = 0.0

    return E, np.concatenate([gTh.ravel(), gPh.ravel()])

# ── Hopf charge diagnostic ────────────────────────────────────────────────────
def hopf_charge(Th, Ph_r, Ph_z):
    """Q via 2D cylindrical Jacobian integral."""
    Tr = np.gradient(Th, drho, axis=0)
    Tz = np.gradient(Th, dz,   axis=1)
    sT = np.sin(Th)
    jac = sT * (Tr*Ph_z - Tz*Ph_r)
    return float(np.trapezoid(np.trapezoid(jac, z, axis=1), rho)) / (4.0*np.pi)

# ── initial energy and virial ────────────────────────────────────────────────
x0 = np.concatenate([Th0.ravel(), Ph0.ravel()])
E0, _ = energy_and_grad(x0)

# quick decomposition for virial at start
Th_t = Th0; Ph_t = Ph0
sT = np.sin(Th_t); cT = np.cos(Th_t)
Tr = np.gradient(Th_t, drho, axis=0); Tz = np.gradient(Th_t, dz, axis=1)
Pr, Pz = Phgrad(Ph_t)
gT2 = Tr**2+Tz**2; gP2 = Pr**2+Pz**2; g2 = gT2+gP2+1/RHO**2
DT = lap(Th_t); DP = div(Pr,Pz)
Ac = cT*DT-sT*g2; Bc = sT*DP+2*cT*(Tr*Pr+Tz*Pz); Cc = -sT*DT-cT*gT2
w = 2*np.pi*RHO
EA1 = float(np.trapezoid(np.trapezoid(w*(A1/2)*(gT2+sT**2*(gP2+1/RHO**2)),z,axis=1),rho))
EA3 = float(np.trapezoid(np.trapezoid(w*(A3/2)*(Ac**2+Bc**2+Cc**2),z,axis=1),rho))
EA4 = float(np.trapezoid(np.trapezoid(w*(A4/2)*(1-cT)**2,z,axis=1),rho))
virial0 = EA1 - EA3 + 3*EA4
print(f"\nInitial state on 160x320 grid:")
print(f"  E_tot = {E0:.4f}   E_A1={EA1:.2f}  E_A3={EA3:.2f}  E_A4={EA4:.2f}")
print(f"  Virial = {virial0:.4f}  |virial/E| = {abs(virial0/E0):.4f}")

# Hopf charge
Ph_r_0 = Z / ((RHO - 4.0)**2 + Z**2 + 1e-8)   # initial analytic estimate (will be off)
Pr2, Pz2 = Phgrad(Ph0)
Q0 = float(np.trapezoid(np.trapezoid(np.sin(Th0)*(
    np.gradient(Th0,drho,axis=0)*Pz2 - np.gradient(Th0,dz,axis=1)*Pr2),
    z, axis=1), rho)) / (4*np.pi)
print(f"  Q = {Q0:.5f}")

# ── L-BFGS-B minimisation ────────────────────────────────────────────────────
print("\nRunning L-BFGS-B (maxiter=500)...")
bds = ([(0, np.pi)] * Nr * Nz) + ([(None, None)] * Nr * Nz)

call_count = [0]
best = {'E': E0, 'x': x0.copy(), 'virial': virial0}

def callback(xk):
    call_count[0] += 1
    if call_count[0] % 50 == 0:
        E, _ = energy_and_grad(xk)
        Th_ = xk[:Nr*Nz].reshape(Nr,Nz); Ph_ = xk[Nr*Nz:].reshape(Nr,Nz)
        sT_ = np.sin(Th_); cT_ = np.cos(Th_)
        Tr_ = np.gradient(Th_,drho,axis=0); Tz_ = np.gradient(Th_,dz,axis=1)
        Pr_,Pz_ = Phgrad(Ph_)
        gT2_ = Tr_**2+Tz_**2; gP2_ = Pr_**2+Pz_**2
        DT_ = lap(Th_); DP_ = div(Pr_,Pz_)
        Ac_ = cT_*DT_-sT_*(gT2_+gP2_+1/RHO**2)
        Bc_ = sT_*DP_+2*cT_*(Tr_*Pr_+Tz_*Pz_)
        Cc_ = -sT_*DT_-cT_*gT2_
        w_ = 2*np.pi*RHO
        EA1_ = float(np.trapezoid(np.trapezoid(w_*(A1/2)*(gT2_+sT_**2*(gP2_+1/RHO**2)),z,axis=1),rho))
        EA3_ = float(np.trapezoid(np.trapezoid(w_*(A3/2)*(Ac_**2+Bc_**2+Cc_**2),z,axis=1),rho))
        EA4_ = float(np.trapezoid(np.trapezoid(w_*(A4/2)*(1-cT_)**2,z,axis=1),rho))
        vir_ = EA1_ - EA3_ + 3*EA4_
        Pr2_,Pz2_ = Phgrad(Ph_)
        Q_ = float(np.trapezoid(np.trapezoid(np.sin(Th_)*(
            np.gradient(Th_,drho,axis=0)*Pz2_-np.gradient(Th_,dz,axis=1)*Pr2_),
            z,axis=1),rho))/(4*np.pi)
        print(f"  iter {call_count[0]:4d}: E={E:.4f}  EA1={EA1_:.2f} EA3={EA3_:.2f} EA4={EA4_:.2f}"
              f"  virial={vir_:.2f}  |v/E|={abs(vir_/E):.4f}  Q={Q_:.4f}")
        if abs(vir_) < abs(best['virial']):
            best['E'] = E; best['x'] = xk.copy(); best['virial'] = vir_

res = minimize(
    energy_and_grad, x0,
    method='L-BFGS-B',
    jac=True,
    bounds=bds,
    callback=callback,
    options={'maxiter': 500, 'ftol': 1e-15, 'gtol': 1e-10, 'maxfun': 50000}
)

print(f"\nL-BFGS-B finished: {res.message}")
print(f"  Iterations: {res.nit}   Func evals: {res.nfev}")

# ── final diagnostics ────────────────────────────────────────────────────────
x_fin = res.x
E_fin, _ = energy_and_grad(x_fin)
Th_f = x_fin[:Nr*Nz].reshape(Nr, Nz)
Ph_f = x_fin[Nr*Nz:].reshape(Nr, Nz)
sT_f = np.sin(Th_f); cT_f = np.cos(Th_f)
Tr_f = np.gradient(Th_f, drho, axis=0); Tz_f = np.gradient(Th_f, dz, axis=1)
Pr_f, Pz_f = Phgrad(Ph_f)
gT2_f = Tr_f**2+Tz_f**2; gP2_f = Pr_f**2+Pz_f**2
DT_f = lap(Th_f); DP_f = div(Pr_f, Pz_f)
Ac_f = cT_f*DT_f - sT_f*(gT2_f+gP2_f+1/RHO**2)
Bc_f = sT_f*DP_f + 2*cT_f*(Tr_f*Pr_f+Tz_f*Pz_f)
Cc_f = -sT_f*DT_f - cT_f*gT2_f
w_f  = 2*np.pi*RHO
EA1_f = float(np.trapezoid(np.trapezoid(w_f*(A1/2)*(gT2_f+sT_f**2*(gP2_f+1/RHO**2)),z,axis=1),rho))
EA3_f = float(np.trapezoid(np.trapezoid(w_f*(A3/2)*(Ac_f**2+Bc_f**2+Cc_f**2),z,axis=1),rho))
EA4_f = float(np.trapezoid(np.trapezoid(w_f*(A4/2)*(1-cT_f)**2,z,axis=1),rho))
virial_f = EA1_f - EA3_f + 3*EA4_f

Pr2_f, Pz2_f = Phgrad(Ph_f)
Q_f = float(np.trapezoid(np.trapezoid(np.sin(Th_f)*(
    np.gradient(Th_f,drho,axis=0)*Pz2_f - np.gradient(Th_f,dz,axis=1)*Pr2_f),
    z,axis=1),rho)) / (4*np.pi)

# Torus core radius: ρ where ∫sinΘ dz is maximum
sin_int = np.trapezoid(np.sin(Th_f), z, axis=1)
R_eff   = rho[np.argmax(sin_int)]

print(f"\n=== FINAL RESULTS (160x320 grid) ===")
print(f"  E_tot = {E_fin:.6f} CCEF")
print(f"  E_A1  = {EA1_f:.6f}")
print(f"  E_A3  = {EA3_f:.6f}")
print(f"  E_A4  = {EA4_f:.6f}")
print(f"  Virial (E_A1 - E_A3 + 3*E_A4) = {virial_f:.6f}")
print(f"  |virial/E_tot| = {abs(virial_f/E_fin):.6f}")
print(f"  Q = {Q_f:.5f}")
print(f"  R_eff = {R_eff:.4f} L0   (torus core radius)")
print(f"  sinΘ at axis (max) = {np.max(np.abs(sT_f[0,:])):.2e}")
print(f"  Theta max = {Th_f.max():.6f}  (target ~π = {np.pi:.6f})")

virial_ok = abs(virial_f/E_fin) < 0.01
print(f"\n  |virial/E_tot| < 0.01 : {'YES ✓' if virial_ok else 'NO — need more iterations'}")

# ── save ──────────────────────────────────────────────────────────────────────
np.save(OUTDIR + 'hopf_converged_Theta.npy', Th_f)
np.save(OUTDIR + 'hopf_converged_Phi.npy',   Ph_f)
np.save(OUTDIR + 'hopf_converged_rho.npy',   rho)
np.save(OUTDIR + 'hopf_converged_z.npy',     z)
print(f"\nSaved hopf_converged_{{Theta,Phi,rho,z}}.npy  (160x320 grid)")
print("Done.")
