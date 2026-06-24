"""
ccef_fd_check.py -- finite-difference verification of analytic gradients.
Verifies grad_phys (energy) and hopf_Q_grad_flat (charge) against FD of E and Q.
Analytic energy grad is in PHYSICAL metric: g_phys * w = dE/dfield|_flat ~ dE/d(field_ij).
"""
import numpy as np
from ccef_hopf_core import (Grid, energy, grad_phys, hopf_Q, hopf_Q_grad_flat,
                            energy_components, virial, seed_ring)

A1, A2, A4 = 1.0, 0.3268, 3.5553
rng = np.random.default_rng(0)

# small grid for FD
g = Grid(rho_max=5.0, z_max=5.0, Nr=40, Nz=80)
T0, P0 = seed_ring(g, R0=2.0, width=1.0)
# add smooth random perturbation so we test a generic (non-symmetric) point
T = T0 + 0.15 * np.sin(2 * g.RHO) * np.cos(g.Z)
P = P0 + 0.10 * np.cos(g.RHO) * np.sin(1.5 * g.Z)

comp = energy_components(g, T, P, A1, A2, A4)
print("Energy at test point:", {k: round(v, 4) for k, v in comp.items()})
print("Virial E1-E2+3E4 =", round(virial(comp), 4))
print("Q =", round(hopf_Q(g, T, P), 5))

gT, gP = grad_phys(g, T, P, A1, A2, A4)
qT, qP = hopf_Q_grad_flat(g, T, P)
w = g.w
eps = 1e-6
cell = g.drho * g.dz   # trapezoid cell-area weight: d(discrete E)/dfield_ij = (delta E/delta field)*cell
# energy analytic functional-deriv density is g_phys; flat density = g_phys*w;
# discrete partial = flat_density * cell
wcell = w * cell

# pick interior points (avoid the forced boundaries)
idx = [(i, j) for i in rng.integers(3, g.Nr - 3, 12)
       for j in [int(k) for k in rng.integers(3, g.Nz - 3, 1)]]
idx = idx[:12]

print("\n--- dE/dTheta : analytic (g*w) vs FD ---")
maxrelE = 0.0
for (i, j) in idx:
    Tp = T.copy(); Tp[i, j] += eps
    Tm = T.copy(); Tm[i, j] -= eps
    fd = (energy(g, Tp, P, A1, A2, A4) - energy(g, Tm, P, A1, A2, A4)) / (2 * eps)
    an = gT[i, j] * wcell[i, j]
    rel = abs(an - fd) / (abs(fd) + 1e-12)
    maxrelE = max(maxrelE, rel)
    print(f"  ({i:3d},{j:3d}) an={an:+.6e} fd={fd:+.6e} rel={rel:.2e}")

print("\n--- dE/dPhi : analytic (g*w) vs FD ---")
maxrelP = 0.0
for (i, j) in idx:
    Pp = P.copy(); Pp[i, j] += eps
    Pm = P.copy(); Pm[i, j] -= eps
    fd = (energy(g, T, Pp, A1, A2, A4) - energy(g, T, Pm, A1, A2, A4)) / (2 * eps)
    an = gP[i, j] * wcell[i, j]
    rel = abs(an - fd) / (abs(fd) + 1e-12)
    maxrelP = max(maxrelP, rel)
    print(f"  ({i:3d},{j:3d}) an={an:+.6e} fd={fd:+.6e} rel={rel:.2e}")

print("\n--- dQ/dTheta : analytic (flat) vs FD ---")
maxrelQT = 0.0
for (i, j) in idx:
    Tp = T.copy(); Tp[i, j] += eps
    Tm = T.copy(); Tm[i, j] -= eps
    fd = (hopf_Q(g, Tp, P) - hopf_Q(g, Tm, P)) / (2 * eps)
    an = qT[i, j] * cell
    rel = abs(an - fd) / (abs(fd) + 1e-9)
    maxrelQT = max(maxrelQT, rel)
    print(f"  ({i:3d},{j:3d}) an={an:+.6e} fd={fd:+.6e} rel={rel:.2e}")

print("\n--- dQ/dPhi : analytic (flat) vs FD ---")
maxrelQP = 0.0
for (i, j) in idx:
    Pp = P.copy(); Pp[i, j] += eps
    Pm = P.copy(); Pm[i, j] -= eps
    fd = (hopf_Q(g, T, Pp) - hopf_Q(g, T, Pm)) / (2 * eps)
    an = qP[i, j] * cell
    rel = abs(an - fd) / (abs(fd) + 1e-9)
    maxrelQP = max(maxrelQP, rel)
    print(f"  ({i:3d},{j:3d}) an={an:+.6e} fd={fd:+.6e} rel={rel:.2e}")

print("\n=== MAX RELATIVE ERRORS ===")
print(f"  dE/dT : {maxrelE:.2e}")
