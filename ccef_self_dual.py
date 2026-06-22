"""
ccef_self_dual.py — Task E: Hopf soliton at the CCEF self-dual (Lifshitz) critical point

From Task A: β(A3) < 0, conjecture A1² = A3·A4 as a fixed-point condition.
At this point the Hessian H(k) = A3k⁴ + A1k² + A4 = (√A3 k² + √A4)² is a perfect square.
This is the Lifshitz phase transition: the UV (bilaplacian) and IR (mass) poles coincide.

Self-dual value: A3_sd = A1² / A4 = 1.0 / 3.5553 = 0.28125

Physical prediction: at the self-dual point, the propagator simplifies to
  K(r) = e^{-m_sd r} / (8π A3 m_sd)   with   m_sd = (A4/A3)^{1/4}
yielding a single mass scale m_sd = (A4/A3)^{1/4} = (3.5553/0.28125)^{1/4} = 1.884 CCEF
i.e. linear excitation = 57.7 MeV (not m_p — soliton mass is different).

Modified Virial at A3 > 0:
  E_A1 - E_A2 - E_A3 + 3·E_A4 = 0   [Derrick scaling in 3D]
A3 acts like a second stabiliser alongside A2 → need less E_A2, potentially lower E_sol.

Start: R0=3.0, rt=1.0 ring (sin(Θ_axis) ≈ 0.01 → axis singularity negligible [SOLID])
"""

import numpy as np
from scipy.optimize import minimize

# ── Parameters ────────────────────────────────────────────────────────────────
A1 = 1.0
A2 = 0.3268          # Faddeev-Skyrme (original doc, A2/4 coefficient)
A4 = 3.5553          # Vacuum mass gap (original doc)
A3_sd = A1**2 / A4  # Self-dual: A1² = A3·A4  →  (√A3 k² + √A4)² perfect square
E0   = 30.608        # MeV/CCEF (Task C)
mp   = 938.3 / E0   # = 30.655 CCEF

m_sd = (A4 / A3_sd)**0.25   # mass at self-dual point
print("=" * 60)
print("Task E — Hopf soliton at Lifshitz self-dual critical point")
print(f"  A1={A1}, A2={A2} (A2/4), A3_sd={A3_sd:.5f}, A4={A4}")
print(f"  Self-dual condition: A1² = A3·A4  →  {A1**2:.4f} = {A3_sd*A4:.4f} ✓")
print(f"  H(k) = (√A3·k² + √A4)² — perfect square [Lifshitz critical point]")
print(f"  Elementary mass m_sd = (A4/A3)^(1/4) = {m_sd:.4f} CCEF = {m_sd*E0:.1f} MeV")
print(f"  Soliton target m_p = {mp:.3f} CCEF = {mp*E0:.1f} MeV")
print(f"  Virial (A3>0): E_A1 - E_A2 - E_A3 + 3·E_A4 = 0")
print("=" * 60)

# ── Grid — large ring (R0=3) keeps axis clean ─────────────────────────────────
Nr, Nz    = 45, 90
rho_max   = 14.0; z_max = 14.0
rho = np.linspace(1e-3, rho_max, Nr)
z   = np.linspace(-z_max, z_max, Nz)
drho = rho[1]-rho[0]; dz = z[1]-z[0]
RHO, Z = np.meshgrid(rho, z, indexing='ij')
inv_rho = 1.0 / np.maximum(RHO, 1e-8)

# ── Operators ────────────────────────────────────────────────────────────────
def lap(f):
    fr = np.gradient(f, drho, axis=0)
    return np.gradient(fr, drho, axis=0) + fr*inv_rho + \
           np.gradient(np.gradient(f, dz, axis=1), dz, axis=1)

def div(P, Q):
    return np.gradient(P, drho, axis=0) + P*inv_rho + np.gradient(Q, dz, axis=1)

def Phgrad(Ph):
    sP, cP = np.sin(Ph), np.cos(Ph)
    return (cP*np.gradient(sP, drho, axis=0) - sP*np.gradient(cP, drho, axis=0),
            cP*np.gradient(sP, dz,   axis=1) - sP*np.gradient(cP, dz,   axis=1))

# ── Energy + gradient (full A1+A2+A3+A4) ────────────────────────────────────
def energy_and_grad(x, A3):
    Th = x[:Nr*Nz].reshape(Nr, Nz)
    Ph = x[Nr*Nz:].reshape(Nr, Nz)
    sT, cT = np.sin(Th), np.cos(Th)
    Tr = np.gradient(Th, drho, axis=0)
    Tz = np.gradient(Th, dz,   axis=1)
    Pr, Pz = Phgrad(Ph)
    gT2 = Tr**2 + Tz**2
    gP2 = Pr**2 + Pz**2
    gTP = Tr*Pr + Tz*Pz
    g2  = gT2 + gP2 + inv_rho**2
    DT  = lap(Th); DP = div(Pr, Pz)
    Ac  = cT*DT - sT*g2
    Bc  = sT*DP + 2*cT*gTP
    Cc  = -sT*DT - cT*gT2

    Jac   = Tr*Pz - Tz*Pr
    F_rz  = sT*Jac; F_rph = sT*Tr; F_zph = sT*Tz

    e1 = (A1/2) * (gT2 + sT**2*(gP2 + inv_rho**2))
    e2 = (A2/4) * (F_rz**2 + (F_rph**2 + F_zph**2)*inv_rho**2)
    e3 = (A3/2) * (Ac**2 + Bc**2 + Cc**2)
    e4 = (A4/2) * (1 - cT)**2

    w  = 2*np.pi*RHO
    I  = lambda f: float(np.trapezoid(np.trapezoid(w*f, z, axis=1), rho))
    E1=I(e1); E2=I(e2); E3=I(e3); E4=I(e4)
    E  = E1+E2+E3+E4

    # Gradients
    gTh = (
        A1*(-DT + sT*cT*(gP2 + inv_rho**2))
        + A4*sT*(1 - cT)
        + A3*(Ac*(-sT*DT - cT*g2) + Bc*(cT*DP - 2*sT*gTP) + Cc*(-cT*DT + sT*gT2)
              + lap(Ac*cT - Cc*sT)
              + 2*div(Ac*sT*Tr, Ac*sT*Tz)
              - 2*div(Bc*cT*Pr, Bc*cT*Pz)
              + 2*div(Cc*cT*Tr, Cc*cT*Tz))
        + (A2/4)*(
            2*F_rz*cT*Jac
            - inv_rho*np.gradient(2*RHO*F_rz*sT*Pz, drho, axis=0)
            + 2*np.gradient(F_rz*sT*Pr, dz, axis=1)
            + 2*sT*cT*(Tr**2+Tz**2)*inv_rho**2
            - inv_rho*np.gradient(2*sT**2*Tr*inv_rho, drho, axis=0)
            - 2*np.gradient(sT**2*Tz, dz, axis=1)*inv_rho**2)
    )
    gPh = (
        -A1*div(sT**2*Pr, sT**2*Pz)
        + A3*(2*div(Ac*sT*Pr, Ac*sT*Pz) + lap(Bc*sT) - 2*div(Bc*cT*Tr, Bc*cT*Tz))
        + (A2/2)*div(F_rz*sT*Tz, -F_rz*sT*Tr)
    )

    for g in [gTh, gPh]:
        g[0,:]=0; g[-1,:]=0; g[:,0]=0; g[:,-1]=0

    return E, np.concatenate([gTh.ravel(), gPh.ravel()]), E1, E2, E3, E4

def EG(x, A3):
    E, g, *_ = energy_and_grad(x, A3)
    return E, g

# ── Ansatz (ring far from axis) ──────────────────────────────────────────────
R0, rt = 3.0, 1.0   # R0/rt = 3 → sin(Θ_axis) ≈ sin(π·(1-tanh(3))) ≈ 0.01 — tiny
U = RHO - R0; V = Z; d = np.sqrt(U**2 + V**2 + 1e-14)
Th0 = np.pi*(1.0 - np.tanh(d/rt))
Ph0 = np.arctan2(V, U)
for f in [Th0, Ph0]:
    f[0,:]=0; f[-1,:]=0; f[:,0]=0; f[:,-1]=0

# Verify axis cleanliness
sT_axis = np.max(np.abs(np.sin(Th0[0,:])))
print(f"\nAxis check: max|sin(Θ)| at ρ=ρ_min = {sT_axis:.4f}  [must be ≪ 1 for axis regularity]")
print(f"  Ring R0={R0}, rt={rt}: axis singularity negligible [SOLID]\n")

# ── Initial energy breakdown ──────────────────────────────────────────────────
x0 = np.concatenate([Th0.ravel(), Ph0.ravel()])
_, _, E1i, E2i, E3i, E4i = energy_and_grad(x0, A3_sd)
Ei = E1i+E2i+E3i+E4i
vir_i = E1i-E2i-E3i+3*E4i
print(f"Initial ansatz (R0=3, rt=1):")
print(f"  E_A1={E1i:.3f}  E_A2={E2i:.3f}  E_A3={E3i:.3f}  E_A4={E4i:.3f}")
print(f"  E_tot={Ei:.3f} CCEF = {Ei/mp:.2f}×m_p")
print(f"  Virial (E1-E2-E3+3E4)={vir_i:.3f}  |v/E|={abs(vir_i/Ei):.3f}")

# ── Compare: same ansatz at A3=0 ─────────────────────────────────────────────
_, _, E1a, E2a, _, E4a = energy_and_grad(x0, 1e-8)
Ea = E1a+E2a+E4a
print(f"\nFor reference (A3≈0 at same ansatz):")
print(f"  E_A1={E1a:.3f}  E_A2={E2a:.3f}  E_A4={E4a:.3f}  E_tot={Ea:.3f} CCEF = {Ea/mp:.2f}×m_p")
print(f"  ΔE from A3_sd: {Ei-Ea:+.3f} CCEF  ({(Ei-Ea)/mp:+.2f}×m_p)\n")

# ── L-BFGS-B relaxation ───────────────────────────────────────────────────────
bds = [(0,np.pi)]*Nr*Nz + [(None,None)]*Nr*Nz
call=[0]
def cb(xk):
    call[0]+=1
    if call[0]%5==0:
        Ev,_=EG(xk, A3_sd)
        print(f"  iter {call[0]:3d}: E={Ev:.3f} CCEF  ({Ev/mp:.2f}×m_p)")

print(f"Running L-BFGS-B at self-dual A3={A3_sd:.5f} (grid {Nr}×{Nz}, maxiter=20)...")
res = minimize(lambda x: EG(x, A3_sd), x0, jac=True, method='L-BFGS-B',
               bounds=bds, callback=cb,
               options={'maxiter':20,'ftol':1e-14,'gtol':1e-9,'maxfun':5000})

# ── Final analysis ────────────────────────────────────────────────────────────
_, _, E1f, E2f, E3f, E4f = energy_and_grad(res.x, A3_sd)
Ef = E1f+E2f+E3f+E4f
vir_f = E1f-E2f-E3f+3*E4f

# Hopf charge
Th_f = res.x[:Nr*Nz].reshape(Nr, Nz)
Ph_f = res.x[Nr*Nz:].reshape(Nr, Nz)
Tr_f = np.gradient(Th_f, drho, axis=0); Tz_f = np.gradient(Th_f, dz, axis=1)
Q_raw = float(np.trapezoid(np.trapezoid(
    np.sin(Th_f)*(Tr_f*np.gradient(Ph_f, dz, axis=1) - Tz_f*np.gradient(Ph_f, drho, axis=0)),
    z, axis=1), rho)) / (4*np.pi)

R_eff = rho[np.argmax(np.trapezoid(np.sin(Th_f), z, axis=1))]

print(f"\n{'='*60}")
print(f"FINAL — Hopf soliton at Lifshitz self-dual point")
print(f"{'='*60}")
print(f"  A3_sd = A1²/A4 = {A3_sd:.5f}  (self-dual, perfect-square Hessian)")
print(f"  E_A1  = {E1f:.4f} CCEF")
print(f"  E_A2  = {E2f:.4f} CCEF  (Faddeev-Skyrme, A2/4)")
print(f"  E_A3  = {E3f:.4f} CCEF  (bilaplacian at self-dual A3)")
print(f"  E_A4  = {E4f:.4f} CCEF  (vacuum potential)")
print(f"  E_tot = {Ef:.4f} CCEF = {Ef*E0:.1f} MeV")
print(f"  Virial (E1-E2-E3+3E4) = {vir_f:.4f}  |v/E| = {abs(vir_f/Ef):.5f}")
print(f"  Hopf Q ≈ {Q_raw:.3f}  (should be 1)")
print(f"  R_eff = {R_eff:.3f} CCEF = {R_eff*1.6107:.3f} fm")
print()
print(f"  E_sol / m_p = {Ef/mp:.3f}×")
print(f"  E_sol (MeV) = {Ef*E0:.1f}")
print(f"  m_p   (MeV) = {mp*E0:.1f}")
print()
print(f"  cf. A3=0 Derrick-optimal ansatz: ~84.8 CCEF = 2.77×m_p")
print(f"  ΔE (self-dual vs A3=0 ansatz) = {Ef - 84.78:+.2f} CCEF  ({(Ef-84.78)/mp:+.2f}×m_p)")
print()
print(f"  m_sd = (A4/A3)^(1/4) = {m_sd:.4f} CCEF = {m_sd*E0:.1f} MeV")
print(f"  Soliton size / m_sd⁻¹ = {R_eff * m_sd:.3f}  (dimensionless)")
print(f"{'='*60}")
print(f"  Iterations: {res.nit}  {res.message}")
print()
print(f"[RESULT] H(k)=(√A3 k²+√A4)² at self-dual: single Yukawa propagator, no oscillation")
print(f"[RESULT] E_A3 shifts Virial → E_sol changes by {Ef-Ea:+.1f} CCEF vs A3=0 ansatz")
