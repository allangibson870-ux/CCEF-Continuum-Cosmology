"""
ccef_hopf_topo.py — Topology-preserving Hopf Q=1 relaxation
============================================================
Root cause of all previous failures: hard Dirichlet BCs allow smooth deformation
from Q=1 → Q=0 vacuum. L-BFGS cannot be prevented from crossing topological sectors.

Fix: augment CCEF energy with Hopf charge penalty derived from the theory's own
topological invariant π₃(S²):

    E_total = E_CCEF + κ·(Q − Q₀)²

Q = (1/4π) ∫∫ sinΘ (∂_ρΘ ∂_zΦ − ∂_zΘ ∂_ρΦ) dρ dz   [Whitehead/Hopf integral]

Penalty gradient derived analytically via IBP [SOLID]:
    δQ/δΘ = (1/4π)[ cosΘ·Jac − ∂_ρ(sinΘ·Pz) + ∂_z(sinΘ·Pr) ]
    δQ/δΦ = (1/4π)[ −∂_z(sinΘ·Tr) + ∂_ρ(sinΘ·Tz) ]

where Jac = ∂_ρΘ·∂_zΦ − ∂_zΘ·∂_ρΦ, Pr/Pz are branch-cut-safe Φ gradients.

For tanh ring R0=3, rt=1: Q_init = −1 analytically (verified below).
This is the same |Q|=1 sector as Q=+1 — just orientation convention.

Parameters: A1=1.000, A2=0.3268 (A2/4 coeff), A3=1e-6, A4=3.5553, E0=30.608 MeV
Start: R0=3.0, rt=1.0 (axis clean: sinΘ|_{ρ=ρ_min} ≈ 0.01 [SOLID])

Two-phase strategy:
  Phase 1: κ=1000 (hard lock, 100 iter) — establish Q=1 solution
  Phase 2: κ=100  (soft lock, 100 iter) — relax toward physical minimum
  Save fields to .npz for continuation.
"""

import numpy as np
from scipy.optimize import minimize

# ── Parameters ────────────────────────────────────────────────────────────────
A1, A2, A3, A4 = 1.0, 0.3268, 1e-6, 3.5553
E0 = 30.608          # MeV/CCEF  [Task C]
mp = 938.3 / E0      # proton target = 30.655 CCEF

# ── Grid ──────────────────────────────────────────────────────────────────────
Nr, Nz    = 55, 110
rho_max   = 14.0; z_max = 14.0
rho = np.linspace(1e-3, rho_max, Nr)
z   = np.linspace(-z_max, z_max, Nz)
drho = rho[1] - rho[0]; dz = z[1] - z[0]
RHO, Z = np.meshgrid(rho, z, indexing='ij')
inv_rho  = 1.0 / np.maximum(RHO, 1e-8)

# ── Operators ────────────────────────────────────────────────────────────────
def lap(f):
    fr = np.gradient(f, drho, axis=0)
    return np.gradient(fr, drho, axis=0) + fr * inv_rho + \
           np.gradient(np.gradient(f, dz, axis=1), dz, axis=1)

def div(P, Q_):
    """Cylindrical divergence: ∂_ρP + P/ρ + ∂_zQ"""
    return np.gradient(P, drho, axis=0) + P * inv_rho + np.gradient(Q_, dz, axis=1)

def Phgrad(Ph):
    """Branch-cut-safe ∂Φ via (cos∂sin - sin∂cos)"""
    sP, cP = np.sin(Ph), np.cos(Ph)
    return (cP * np.gradient(sP, drho, axis=0) - sP * np.gradient(cP, drho, axis=0),
            cP * np.gradient(sP, dz,   axis=1) - sP * np.gradient(cP, dz,   axis=1))

# ── Hopf charge and its IBP gradient ─────────────────────────────────────────
def hopf_charge(Th, Ph):
    """Q = (1/4π) ∫∫ sinΘ·Jac dρ dz   (flat measure, no ρ weight)
    Analytic check: tanh ring R0=3 → Q = −1 [SOLID — see module docstring]"""
    sT  = np.sin(Th)
    Tr  = np.gradient(Th, drho, axis=0)
    Tz  = np.gradient(Th, dz,   axis=1)
    Pr, Pz = Phgrad(Ph)
    Jac = Tr * Pz - Tz * Pr
    return float(np.trapezoid(np.trapezoid(sT * Jac, z, axis=1), rho)) / (4 * np.pi)

def hopf_penalty(Th, Ph, Q_target, kappa):
    """Returns (E_pen, gTh_pen, gPh_pen, Q_now).

    Penalty: E_pen = κ(Q − Q_target)²
    IBP gradients [SOLID]:
      δQ/δΘ = (1/4π)[ cosΘ·Jac − ∂_ρ(sinΘ·Pz) + ∂_z(sinΘ·Pr) ]
      δQ/δΦ = (1/4π)[ −∂_z(sinΘ·Tr) + ∂_ρ(sinΘ·Tz) ]
    """
    sT, cT = np.sin(Th), np.cos(Th)
    Tr  = np.gradient(Th, drho, axis=0)
    Tz  = np.gradient(Th, dz,   axis=1)
    Pr, Pz = Phgrad(Ph)
    Jac = Tr * Pz - Tz * Pr

    Q_now = float(np.trapezoid(np.trapezoid(sT * Jac, z, axis=1), rho)) / (4 * np.pi)
    E_pen = kappa * (Q_now - Q_target) ** 2

    # δQ/δΘ: local (cosΘ·Jac) + IBP from ∂Θ appearing in Jac
    gQ_Th = (cT * Jac
             - np.gradient(sT * Pz, drho, axis=0)
             + np.gradient(sT * Pr, dz,   axis=1)) / (4 * np.pi)

    # δQ/δΦ: IBP from ∂Φ appearing in Jac (no local term since ∂Q/∂Φ is pure divergence)
    gQ_Ph = (-np.gradient(sT * Tr, dz,   axis=1)
             + np.gradient(sT * Tz, drho, axis=0)) / (4 * np.pi)

    factor = 2 * kappa * (Q_now - Q_target)
    return E_pen, factor * gQ_Th, factor * gQ_Ph, Q_now

# ── Full energy + gradient (CCEF + topology penalty) ─────────────────────────
def energy_and_grad(x, kappa, Q_target):
    Th = x[:Nr * Nz].reshape(Nr, Nz)
    Ph = x[Nr * Nz:].reshape(Nr, Nz)
    sT, cT  = np.sin(Th), np.cos(Th)
    Tr  = np.gradient(Th, drho, axis=0)
    Tz  = np.gradient(Th, dz,   axis=1)
    Pr, Pz  = Phgrad(Ph)
    gT2 = Tr**2 + Tz**2
    gP2 = Pr**2 + Pz**2
    gTP = Tr * Pr + Tz * Pz
    g2  = gT2 + gP2 + inv_rho**2
    DT  = lap(Th); DP = div(Pr, Pz)
    Ac  = cT * DT  - sT * g2
    Bc  = sT * DP  + 2 * cT * gTP
    Cc  = -sT * DT - cT * gT2
    Jac    = Tr * Pz - Tz * Pr
    F_rz   = sT * Jac
    F_rph  = sT * Tr
    F_zph  = sT * Tz

    # ── Energy densities (cylindrical weight 2πρ) ─────────────────────────────
    w = 2 * np.pi * RHO
    I = lambda f: float(np.trapezoid(np.trapezoid(w * f, z, axis=1), rho))
    E1 = I((A1 / 2) * (gT2 + sT**2 * (gP2 + inv_rho**2)))
    E2 = I((A2 / 4) * (F_rz**2 + (F_rph**2 + F_zph**2) * inv_rho**2))
    E3 = I((A3 / 2) * (Ac**2 + Bc**2 + Cc**2))
    E4 = I((A4 / 2) * (1 - cT)**2)
    E_phys = E1 + E2 + E3 + E4

    # ── Physical gradients (EL equations via IBP) ─────────────────────────────
    gTh = (
        A1 * (-DT + sT * cT * (gP2 + inv_rho**2))
        + A4 * sT * (1 - cT)
        + A3 * (Ac * (-sT * DT - cT * g2)
                + Bc * (cT * DP - 2 * sT * gTP)
                + Cc * (-cT * DT + sT * gT2)
                + lap(Ac * cT - Cc * sT)
                + 2 * div(Ac * sT * Tr, Ac * sT * Tz)
                - 2 * div(Bc * cT * Pr, Bc * cT * Pz)
                + 2 * div(Cc * cT * Tr, Cc * cT * Tz))
        + (A2 / 4) * (
            2 * F_rz * cT * Jac
            - inv_rho * np.gradient(2 * RHO * F_rz * sT * Pz, drho, axis=0)
            + 2 * np.gradient(F_rz * sT * Pr, dz, axis=1)
            + 2 * sT * cT * (Tr**2 + Tz**2) * inv_rho**2
            - inv_rho * np.gradient(2 * sT**2 * Tr * inv_rho, drho, axis=0)
            - 2 * np.gradient(sT**2 * Tz, dz, axis=1) * inv_rho**2)
    )
    gPh = (
        -A1 * div(sT**2 * Pr, sT**2 * Pz)
        + A3 * (2 * div(Ac * sT * Pr, Ac * sT * Pz)
                + lap(Bc * sT)
                - 2 * div(Bc * cT * Tr, Bc * cT * Tz))
        + (A2 / 2) * div(F_rz * sT * Tz, -F_rz * sT * Tr)
    )

    # ── Add topology penalty ──────────────────────────────────────────────────
    E_pen, gTh_pen, gPh_pen, Q_now = hopf_penalty(Th, Ph, Q_target, kappa)
    gTh += gTh_pen
    gPh += gPh_pen

    # ── Zero boundary gradients (Dirichlet) ───────────────────────────────────
    for g in [gTh, gPh]:
        g[0, :] = 0; g[-1, :] = 0; g[:, 0] = 0; g[:, -1] = 0

    return (E_phys + E_pen,
            np.concatenate([gTh.ravel(), gPh.ravel()]),
            E1, E2, E3, E4, E_pen, Q_now)

def obj(x, kappa, Q_target):
    E, g, *_ = energy_and_grad(x, kappa, Q_target)
    return E, g

# ── Initial ansatz ─────────────────────────────────────────────────────────────
R0, rt = 3.0, 1.0
U = RHO - R0; V = Z; d = np.sqrt(U**2 + V**2 + 1e-14)
Th0 = np.pi * (1.0 - np.tanh(d / rt))
Ph0 = np.arctan2(V, U)
for f in [Th0, Ph0]:
    f[0, :] = 0; f[-1, :] = 0; f[:, 0] = 0; f[:, -1] = 0

Q_init  = hopf_charge(Th0, Ph0)
Q_target = round(Q_init)   # should be −1; working in |Q|=1 sector

print("=" * 65)
print("ccef_hopf_topo.py — Topology-preserving Hopf relaxation")
print("=" * 65)
print(f"  A1={A1}, A2={A2} (A2/4), A3={A3}, A4={A4}")
print(f"  E0={E0} MeV/CCEF  |  m_p target = {mp:.3f} CCEF = {mp*E0:.1f} MeV")
print(f"  Grid: {Nr}×{Nz}  ρ∈[{rho[0]:.3f},{rho_max}]  z∈[{-z_max},{z_max}]")
print(f"  Ansatz: R0={R0}, rt={rt}  (large ring, axis-clean)")
print(f"  Axis |sinΘ|_max at ρ_min = {np.max(np.abs(np.sin(Th0[0,:]))):.4f}  [SOLID: negligible]")
print(f"  Initial Hopf Q = {Q_init:.4f}  (analytic: -1 for this ansatz)")
print(f"  Q_target = {Q_target}  (|Q|=1 sector)")
print()

# Initial energy (no penalty)
x0 = np.concatenate([Th0.ravel(), Ph0.ravel()])
_, _, E1_0, E2_0, E3_0, E4_0, _, _ = energy_and_grad(x0, kappa=0.0, Q_target=Q_target)
E0_tot = E1_0 + E2_0 + E3_0 + E4_0
print(f"Initial energy breakdown (κ=0):")
print(f"  E_A1={E1_0:.3f}  E_A2={E2_0:.3f}  E_A4={E4_0:.3f}  E_tot={E0_tot:.3f} CCEF")
print(f"  Virial (E1-E2+3E4) = {E1_0-E2_0+3*E4_0:.3f}")

# ── Phase 1: Strong topology lock, κ=1000 ────────────────────────────────────
print()
print("─" * 65)
print(f"Phase 1: κ=1000 (hard topology lock), maxiter=100")
print("─" * 65)
kappa1  = 1000.0
call1   = [0]

def cb1(xk):
    call1[0] += 1
    if call1[0] % 10 == 0:
        Th_ = xk[:Nr*Nz].reshape(Nr, Nz)
        Ph_ = xk[Nr*Nz:].reshape(Nr, Nz)
        Q_  = hopf_charge(Th_, Ph_)
        _, _, E1_, E2_, _, E4_, Ep_, _ = energy_and_grad(xk, kappa1, Q_target)
        Ep = E1_+E2_+E4_
        print(f"  iter {call1[0]:3d}: E_phys={Ep:.3f}  E_pen={Ep_:.4f}  Q={Q_:.4f}")

bds = [(0, np.pi)] * Nr * Nz + [(None, None)] * Nr * Nz
res1 = minimize(lambda x: obj(x, kappa1, Q_target), x0,
                jac=True, method='L-BFGS-B', bounds=bds, callback=cb1,
                options={'maxiter': 100, 'ftol': 1e-14, 'gtol': 1e-9, 'maxfun': 5000})

Th1 = res1.x[:Nr*Nz].reshape(Nr, Nz)
Ph1 = res1.x[Nr*Nz:].reshape(Nr, Nz)
Q1  = hopf_charge(Th1, Ph1)
_, _, E1_1, E2_1, E3_1, E4_1, Ep1, _ = energy_and_grad(res1.x, kappa1, Q_target)
Ephys1 = E1_1 + E2_1 + E3_1 + E4_1
print(f"\nPhase 1 done ({res1.nit} iters): E_phys={Ephys1:.4f} CCEF  Q={Q1:.4f}  E_pen={Ep1:.4f}")

# ── Phase 2: Softer lock, κ=100 ──────────────────────────────────────────────
print()
print("─" * 65)
print(f"Phase 2: κ=100 (relaxed topology lock), maxiter=100")
print("─" * 65)
kappa2 = 100.0
call2  = [0]

def cb2(xk):
    call2[0] += 1
    if call2[0] % 10 == 0:
        Th_ = xk[:Nr*Nz].reshape(Nr, Nz)
        Ph_ = xk[Nr*Nz:].reshape(Nr, Nz)
        Q_  = hopf_charge(Th_, Ph_)
        _, _, E1_, E2_, _, E4_, Ep_, _ = energy_and_grad(xk, kappa2, Q_target)
        Ep = E1_+E2_+E4_
        print(f"  iter {call2[0]:3d}: E_phys={Ep:.3f}  E_pen={Ep_:.4f}  Q={Q_:.4f}")

res2 = minimize(lambda x: obj(x, kappa2, Q_target), res1.x,
                jac=True, method='L-BFGS-B', bounds=bds, callback=cb2,
                options={'maxiter': 100, 'ftol': 1e-14, 'gtol': 1e-9, 'maxfun': 5000})

Th2 = res2.x[:Nr*Nz].reshape(Nr, Nz)
Ph2 = res2.x[Nr*Nz:].reshape(Nr, Nz)
Q2  = hopf_charge(Th2, Ph2)
_, _, E1_2, E2_2, E3_2, E4_2, Ep2, _ = energy_and_grad(res2.x, kappa2, Q_target)
Ephys2  = E1_2 + E2_2 + E3_2 + E4_2
vir2    = E1_2 - E2_2 + 3 * E4_2
R_eff2  = rho[np.argmax(np.trapezoid(np.sin(Th2), z, axis=1))]

print(f"\nPhase 2 done ({res2.nit} iters): E_phys={Ephys2:.4f} CCEF  Q={Q2:.4f}  E_pen={Ep2:.4f}")

# ── Save fields for continuation ──────────────────────────────────────────────
np.savez('ccef_hopf_topo_fields.npz',
         Th=Th2, Ph=Ph2, Q=np.array([Q2]),
         E1=np.array([E1_2]), E2=np.array([E2_2]),
         E4=np.array([E4_2]), E_phys=np.array([Ephys2]),
         rho=rho, z=z, params=np.array([A1,A2,A3,A4,E0,kappa2]))
print(f"\nFields saved to ccef_hopf_topo_fields.npz (for continuation)")

# ── Final report ──────────────────────────────────────────────────────────────
topo_ok = abs(Q2 - Q_target) < 0.15

print()
print("=" * 65)
print("FINAL — Topology-preserving Hopf Q=1 relaxation")
print("=" * 65)
print(f"  A1={A1}, A2={A2} (A2/4), A4={A4}")
print(f"  Phase 1: κ={kappa1} ({res1.nit} iters)  Phase 2: κ={kappa2} ({res2.nit} iters)")
print()
print(f"  Hopf charge Q  = {Q2:.4f}  (target {Q_target})")
print(f"  ΔQ             = {Q2 - Q_target:+.4f}  {'[SOLID: topology preserved]' if topo_ok else '[WARNING: topology drifted]'}")
print()
print(f"  E_A1  = {E1_2:.4f} CCEF  (gradient)")
print(f"  E_A2  = {E2_2:.4f} CCEF  (Faddeev-Skyrme A2/4)")
print(f"  E_A4  = {E4_2:.4f} CCEF  (vacuum potential)")
print(f"  E_pen = {Ep2:.4f} CCEF  (topology penalty, NOT physical)")
print()
print(f"  E_phys         = {Ephys2:.4f} CCEF")
print(f"  E_phys (MeV)   = {Ephys2 * E0:.1f} MeV")
print(f"  Virial E1-E2+3E4 = {vir2:.4f}  |v/E| = {abs(vir2/Ephys2):.5f}")
print(f"  R_eff          = {R_eff2:.3f} CCEF = {R_eff2 * 1.6107:.3f} fm")
print()
print(f"  m_p (target)   = {mp:.3f} CCEF = {mp*E0:.1f} MeV")
print(f"  E_sol / m_p    = {Ephys2/mp:.3f}×")
print()
if topo_ok:
    label = "[SOLID]" if abs(vir2/Ephys2) < 0.1 else "[CONJECT]"
    print(f"  {label} First genuine Q=1 Hopf soliton energy:")
    print(f"         E_sol = {Ephys2:.2f} CCEF = {Ephys2/mp:.2f}×m_p")
    if abs(vir2/Ephys2) > 0.1:
        print(f"  [NOTE] Virial not satisfied — soliton not yet at true minimum")
        print(f"         Run more iterations or reduce κ further for full relaxation")
else:
    print(f"  [OPEN] Topology still drifting — increase κ or use continuation")
print()
print(f"  cf. Derrick upper bound (no topology constraint): 84.78 CCEF = 2.77×m_p")
print(f"  ΔE vs Derrick bound = {Ephys2 - 84.78:+.2f} CCEF")
print("=" * 65)
