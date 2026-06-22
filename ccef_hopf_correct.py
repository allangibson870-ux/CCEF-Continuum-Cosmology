"""
ccef_hopf_correct.py — Hopf soliton relaxation with CORRECTED parameters
Based on ccef_hopf_relax3.py structure from GitHub working branch.

CORRECTIONS vs prior session:
  A2/4 coefficient (was A2/2) — action coefficient fixed
  A3 = 1e-6 (was 1.684) — Task A IR limit
  A4 = 3.5553 (was 0.542) — original doc value restored
  E0 = 30.608 MeV/CCEF (was 311.73) — Task C calibration
  A2 Faddeev-Skyrme gradient added to EL equations
"""

import numpy as np
from scipy.optimize import minimize

A1   = 1.0
A2   = 0.3268     # Faddeev-Skyrme (original doc); coefficient A2/4 in action
A3   = 1e-6       # UV bilaplacian — negligible in IR (Task A)
A4   = 3.5553     # Vacuum mass gap (original doc)
E0   = 30.608     # MeV / CCEF  (Task C)
mp   = 938.3 / E0 # = 30.65 CCEF

Nr, Nz   = 55, 110
rho_max  = 14.0; z_max = 14.0
rho = np.linspace(1e-3, rho_max, Nr)
z   = np.linspace(-z_max, z_max, Nz)
drho = rho[1]-rho[0]; dz = z[1]-z[0]
RHO, Z = np.meshgrid(rho, z, indexing='ij')
inv_rho = 1.0 / np.maximum(RHO, 1e-8)

# ── differential operators ────────────────────────────────────────────────────
def lap(f):
    fr = np.gradient(f, drho, axis=0)
    return np.gradient(fr, drho, axis=0) + fr*inv_rho + \
           np.gradient(np.gradient(f, dz, axis=1), dz, axis=1)

def div(P, Q):          # cylindrical: ∂_ρP + P/ρ + ∂_zQ
    return np.gradient(P, drho, axis=0) + P*inv_rho + np.gradient(Q, dz, axis=1)

def Phgrad(Ph):         # gauge-safe ∂Φ via sin/cos
    sP, cP = np.sin(Ph), np.cos(Ph)
    return (cP*np.gradient(sP, drho, axis=0) - sP*np.gradient(cP, drho, axis=0),
            cP*np.gradient(sP, dz,   axis=1) - sP*np.gradient(cP, dz,   axis=1))

# ── energy + analytic gradient ────────────────────────────────────────────────
def energy_and_grad(x):
    Th = x[:Nr*Nz].reshape(Nr, Nz)
    Ph = x[Nr*Nz:].reshape(Nr, Nz)
    sT, cT  = np.sin(Th), np.cos(Th)
    Tr = np.gradient(Th, drho, axis=0)
    Tz = np.gradient(Th, dz,   axis=1)
    Pr, Pz  = Phgrad(Ph)
    gT2 = Tr**2 + Tz**2
    gP2 = Pr**2 + Pz**2
    gTP = Tr*Pr + Tz*Pz
    g2  = gT2 + gP2 + inv_rho**2
    DT  = lap(Th); DP = div(Pr, Pz)
    Ac  = cT*DT  - sT*g2
    Bc  = sT*DP  + 2*cT*gTP
    Cc  = -sT*DT - cT*gT2

    # Faddeev-Skyrme field strengths
    Jac   = Tr*Pz - Tz*Pr
    F_rz  = sT * Jac
    F_rph = sT * Tr
    F_zph = sT * Tz

    # Energy densities
    e1 = (A1/2) * (gT2 + sT**2*(gP2 + inv_rho**2))
    e2 = (A2/4) * (F_rz**2 + (F_rph**2 + F_zph**2)*inv_rho**2)   # A2/4 CORRECT
    e3 = (A3/2) * (Ac**2 + Bc**2 + Cc**2)
    e4 = (A4/2) * (1 - cT)**2

    w = 2*np.pi*RHO
    I = lambda f: float(np.trapezoid(np.trapezoid(w*f, z, axis=1), rho))
    E_A1=I(e1); E_A2=I(e2); E_A3=I(e3); E_A4=I(e4)
    E = E_A1+E_A2+E_A3+E_A4

    # ── gradient wrt Θ ──────────────────────────────────────────────────────
    # A1 + A4 + A3 (from relax3.py, unchanged)
    gTh = (
        A1*(-DT + sT*cT*(gP2 + inv_rho**2))
        + A4*sT*(1 - cT)
        + A3*(Ac*(-sT*DT - cT*g2)
              + Bc*(cT*DP - 2*sT*gTP)
              + Cc*(-cT*DT + sT*gT2)
              + lap(Ac*cT - Cc*sT)
              + 2*div(Ac*sT*Tr, Ac*sT*Tz)
              - 2*div(Bc*cT*Pr, Bc*cT*Pz)
              + 2*div(Cc*cT*Tr, Cc*cT*Tz))
        # A2 Faddeev-Skyrme contribution (derived via IBP):
        #   from F_rz²: local + -(1/ρ)∂_ρ(2ρ F sT Pz) + ∂_z(2 F sT Pr)
        #   from (F_rph²+F_zph²)/ρ²: local + -(1/ρ)∂_ρ(2sT²Θ_ρ/ρ) + -∂_z(2sT²Θ_z)/ρ²
        + (A2/4)*(
            2*F_rz*cT*Jac
            - inv_rho*np.gradient(2*RHO*F_rz*sT*Pz, drho, axis=0)
            + 2*np.gradient(F_rz*sT*Pr, dz, axis=1)
            + 2*sT*cT*(Tr**2+Tz**2)*inv_rho**2
            - inv_rho*np.gradient(2*sT**2*Tr*inv_rho, drho, axis=0)
            - 2*np.gradient(sT**2*Tz, dz, axis=1)*inv_rho**2
        )
    )

    # ── gradient wrt Φ ──────────────────────────────────────────────────────
    gPh = (
        -A1*div(sT**2*Pr, sT**2*Pz)
        + A3*(2*div(Ac*sT*Pr, Ac*sT*Pz)
              + lap(Bc*sT)
              - 2*div(Bc*cT*Tr, Bc*cT*Tz))
        # A2: gPh = (A2/2) × div_cyl(F_rz sT Tz, -F_rz sT Tr)
        + (A2/2)*div(F_rz*sT*Tz, -F_rz*sT*Tr)
    )

    # zero-gradient at all boundaries (Dirichlet)
    for g in [gTh, gPh]:
        g[0,:]=0; g[-1,:]=0; g[:,0]=0; g[:,-1]=0

    return E, np.concatenate([gTh.ravel(), gPh.ravel()])

# ── initial Hopf ansatz ───────────────────────────────────────────────────────
def make_ansatz(R0, rt):
    U = RHO-R0; V = Z
    d = np.sqrt(U**2+V**2+1e-14)
    Th = np.pi*(1.0 - np.tanh(d/rt))
    Ph = np.arctan2(V, U)
    for f in [Th, Ph]:
        f[0,:]=0; f[-1,:]=0; f[:,0]=0; f[:,-1]=0
    return Th, Ph

def eval_energy(R0, rt):
    Th, Ph = make_ansatz(R0, rt)
    x = np.concatenate([Th.ravel(), Ph.ravel()])
    E, _ = energy_and_grad(x)
    return E

# ── find best starting point with quick scan ─────────────────────────────────
print("Corrected parameters: A1=1, A2=0.3268 (A2/4), A3=1e-6, A4=3.5553, E0=30.608 MeV")
print(f"Target: m_p = {mp:.3f} CCEF  ({E0}×{mp:.2f} = {E0*mp:.1f} MeV)\n")
print("Quick scan to find best starting ring geometry...")
best_E, best_R, best_rt = 1e30, 3.0, 1.5
for R0 in [0.5, 1.0, 2.0, 3.0, 4.0]:
    for rt in [0.5, 1.0, 1.5, 2.0]:
        E = eval_energy(R0, rt)
        flag = " ←" if E < best_E else ""
        print(f"  R={R0:.1f}  rt={rt:.1f}  E={E:.1f} CCEF ({E/mp:.0f}×m_p){flag}")
        if E < best_E:
            best_E, best_R, best_rt = E, R0, rt

print(f"\nBest start: R={best_R}, rt={best_rt}, E={best_E:.2f} CCEF = {best_E/mp:.1f}×m_p")

# ── L-BFGS-B relaxation ───────────────────────────────────────────────────────
Th0, Ph0 = make_ansatz(best_R, best_rt)
x0 = np.concatenate([Th0.ravel(), Ph0.ravel()])
bds = [(0, np.pi)]*Nr*Nz + [(None, None)]*Nr*Nz

call=[0]
energies=[]
def cb(xk):
    call[0]+=1
    if call[0]%5==0:
        Ev,_=energy_and_grad(xk)
        energies.append(Ev)
        print(f"  iter {call[0]:3d}: E={Ev:.3f} CCEF  ({Ev/mp:.1f}×m_p)")

print(f"\nRunning L-BFGS-B (maxiter=20, grid {Nr}×{Nz})...")
res = minimize(energy_and_grad, x0, method='L-BFGS-B', jac=True,
               bounds=bds, callback=cb,
               options={'maxiter':20,'ftol':1e-14,'gtol':1e-9,'maxfun':2000})

# ── final analysis ────────────────────────────────────────────────────────────
Ef, _ = energy_and_grad(res.x)
Th_f = res.x[:Nr*Nz].reshape(Nr, Nz)
Ph_f = res.x[Nr*Nz:].reshape(Nr, Nz)
sT_f, cT_f = np.sin(Th_f), np.cos(Th_f)
Tr_f = np.gradient(Th_f, drho, axis=0); Tz_f = np.gradient(Th_f, dz, axis=1)
Pr_f, Pz_f = Phgrad(Ph_f)
gT2_f = Tr_f**2+Tz_f**2; gP2_f = Pr_f**2+Pz_f**2
Jac_f = Tr_f*Pz_f-Tz_f*Pr_f
F_rz_f = sT_f*Jac_f; F_rph_f = sT_f*Tr_f; F_zph_f = sT_f*Tz_f
wf = 2*np.pi*RHO
If = lambda f: float(np.trapezoid(np.trapezoid(wf*f, z, axis=1), rho))
EA1f = If((A1/2)*(gT2_f+sT_f**2*(gP2_f+inv_rho**2)))
EA2f = If((A2/4)*(F_rz_f**2+(F_rph_f**2+F_zph_f**2)*inv_rho**2))
EA4f = If((A4/2)*(1-cT_f)**2)
virf = EA1f - EA2f + 3*EA4f

# Hopf charge
Q = float(np.trapezoid(np.trapezoid(
    sT_f*(Tr_f*np.gradient(Ph_f, dz, axis=1) - Tz_f*np.gradient(Ph_f, drho, axis=0)),
    z, axis=1), rho)) / (4*np.pi)

R_eff = rho[np.argmax(np.trapezoid(sT_f, z, axis=1))]

print(f"\n{'='*55}")
print(f"FINAL RESULT  ({res.nit} L-BFGS iterations)")
print(f"{'='*55}")
print(f"  E_A1  = {EA1f:.4f} CCEF")
print(f"  E_A2  = {EA2f:.4f} CCEF  (A2/4 coefficient, CORRECT)")
print(f"  E_A4  = {EA4f:.4f} CCEF")
print(f"  E_tot = {Ef:.4f} CCEF = {Ef*E0:.1f} MeV")
print(f"  Virial (E_A1-E_A2+3E_A4) = {virf:.4f}  |v/E| = {abs(virf/Ef):.5f}")
print(f"  Hopf charge Q ≈ {Q:.3f}  (should be 1)")
print(f"  R_eff = {R_eff:.3f} CCEF  (torus ring radius)")
print(f"")
print(f"  E_sol / m_p = {Ef/mp:.2f}×")
print(f"  E_sol (MeV) = {Ef*E0:.1f}")
print(f"  m_p (MeV)   = {mp*E0:.1f}")
print(f"  Ratio:        {Ef/mp:.2f}×  [THEORY SPEAKS FOR ITSELF]")
print(f"{'='*55}")
print(f"  {res.message}")
