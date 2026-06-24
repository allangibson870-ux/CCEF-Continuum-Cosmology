"""
ccef_hopf_core.py  -- Corrected CCEF Hopf Q=1 energy + gradients (Task F retry)
==============================================================================
Axially-symmetric reduction:  n = (sinT cos(phi+P), sinT sin(phi+P), cosT)
  T = Theta(rho,z),  P = Phi(rho,z),  phi = physical azimuth, toroidal winding m=1.

CORRECTED action (per 22-June resume, supersedes GitHub doc):
  e_A1 = (A1/2)[ |grad T|^2 + sin^2 T ( |grad P|^2 + 1/rho^2 ) ]
  e_A2 = (A2/2) sin^2 T [ K^2 + |grad T|^2 / rho^2 ],   K = T_r P_z - T_z P_r
         (Faddeev-Skyrme; action coeff A2/4 of |d_i n x d_j n|^2 -> A2/2 * sum_{i<j})
  e_A4 = (A4/2) sin^2 T            ==  (A4/2)(1 - n3^2)   [NOT (1-cosT)^2]
  A3 (bilaplacian) -> 0 in the IR (Task A); dropped here.

E = integral 2*pi*rho ( e_A1 + e_A2 + e_A4 ) drho dz.

Gradients are returned in the PHYSICAL metric  L^2(2*pi*rho drho dz),
i.e.  g = (1/w) * dE/dfield|_flat ,  with w = 2*pi*rho.
This matches the convention of the validated session A1/A4 gradient code.

Hopf-charge diagnostic (degree functional, flat measure):
  Q = (1/4pi) integral sinT ( T_r P_z - T_z P_r ) drho dz
"""
import numpy as np

try:
    trapz = np.trapezoid
except AttributeError:
    trapz = np.trapz


class Grid:
    def __init__(self, rho_max=6.0, z_max=6.0, Nr=120, Nz=240, rho_min=1e-3):
        self.rho = np.linspace(rho_min, rho_max, Nr)
        self.z = np.linspace(-z_max, z_max, Nz)
        self.Nr, self.Nz = Nr, Nz
        self.drho = self.rho[1] - self.rho[0]
        self.dz = self.z[1] - self.z[0]
        self.RHO, self.Z = np.meshgrid(self.rho, self.z, indexing='ij')
        self.w = 2.0 * np.pi * self.RHO            # physical measure
        self.inv_rho2 = 1.0 / self.RHO**2

    def dr(self, f):
        return np.gradient(f, self.drho, axis=0)

    def dzf(self, f):
        return np.gradient(f, self.dz, axis=1)


def _phgrad(g, P):
    """grad of Phi computed via cos/sin differencing (branch-cut safe)."""
    sP, cP = np.sin(P), np.cos(P)
    Pr = cP * g.dr(sP) - sP * g.dr(cP)
    Pz = cP * g.dzf(sP) - sP * g.dzf(cP)
    return Pr, Pz


def energy_components(g, T, P, A1, A2, A4):
    sT, cT = np.sin(T), np.cos(T)
    Tr, Tz = g.dr(T), g.dzf(T)
    Pr, Pz = _phgrad(g, P)
    gT2 = Tr**2 + Tz**2
    gP2 = Pr**2 + Pz**2
    K = Tr * Pz - Tz * Pr
    inv = g.inv_rho2

    e_A1 = 0.5 * A1 * (gT2 + sT**2 * (gP2 + inv))
    e_A2 = 0.5 * A2 * sT**2 * (K**2 + gT2 * inv)
    e_A4 = 0.5 * A4 * sT**2

    w = g.w
    E_A1 = float(trapz(trapz(w * e_A1, g.z, axis=1), g.rho))
    E_A2 = float(trapz(trapz(w * e_A2, g.z, axis=1), g.rho))
    E_A4 = float(trapz(trapz(w * e_A4, g.z, axis=1), g.rho))
    return dict(E_A1=E_A1, E_A2=E_A2, E_A4=E_A4, E=E_A1 + E_A2 + E_A4)


def energy(g, T, P, A1, A2, A4):
    return energy_components(g, T, P, A1, A2, A4)['E']


def grad_phys(g, T, P, A1, A2, A4):
    """Analytic dE/dfield in physical metric (divided by w). Returns gT, gP.

    Euler-Lagrange:  dE/dT|_flat = d(e_w)/dT - d_r(d e_w/dT_r) - d_z(d e_w/dT_z)
    with e_w = w * (e_A1+e_A2+e_A4), then divide by w.
    """
    sT, cT = np.sin(T), np.cos(T)
    Tr, Tz = g.dr(T), g.dzf(T)
    Pr, Pz = _phgrad(g, P)
    gT2 = Tr**2 + Tz**2
    gP2 = Pr**2 + Pz**2
    K = Tr * Pz - Tz * Pr
    inv = g.inv_rho2
    w = g.w
    s2 = sT**2

    # ---- partial derivatives of e_w = w*e  w.r.t. fields and their grads ----
    # A1
    dT_A1 = w * A1 * sT * cT * (gP2 + inv)
    dTr_A1 = w * A1 * Tr
    dTz_A1 = w * A1 * Tz
    dPr_A1 = w * A1 * s2 * Pr
    dPz_A1 = w * A1 * s2 * Pz
    # A4  (V = (A4/2) sin^2 T)
    dT_A4 = w * A4 * sT * cT
    # A2  e = (A2/2) s2 (K^2 + gT2*inv)
    c2 = w * 0.5 * A2
    dT_A2 = c2 * 2.0 * sT * cT * (K**2 + gT2 * inv)
    # dK/dTr = Pz ; dK/dTz = -Pr ; dK/dPr = -Tz ; dK/dPz = Tr
    dTr_A2 = c2 * s2 * (2.0 * K * Pz + 2.0 * Tr * inv)
    dTz_A2 = c2 * s2 * (2.0 * K * (-Pr) + 2.0 * Tz * inv)
    dPr_A2 = c2 * s2 * (2.0 * K * (-Tz))
    dPz_A2 = c2 * s2 * (2.0 * K * (Tr))

    dT = dT_A1 + dT_A4 + dT_A2
    dTr = dTr_A1 + dTr_A2
    dTz = dTz_A1 + dTz_A2
    dPr = dPr_A1 + dPr_A2
    dPz = dPz_A1 + dPz_A2

    gT_flat = dT - g.dr(dTr) - g.dzf(dTz)
    gP_flat = -g.dr(dPr) - g.dzf(dPz)

    gT = gT_flat / w
    gP = gP_flat / w
    return gT, gP


def hopf_Q(g, T, P):
    Tr, Tz = g.dr(T), g.dzf(T)
    Pr, Pz = _phgrad(g, P)
    sT = np.sin(T)
    q = sT * (Tr * Pz - Tz * Pr)
    return float(trapz(trapz(q, g.z, axis=1), g.rho)) / (4.0 * np.pi)


def hopf_Q_grad_flat(g, T, P):
    """dQ/dfield in FLAT L^2(drho dz)."""
    sT, cT = np.sin(T), np.cos(T)
    Tr, Tz = g.dr(T), g.dzf(T)
    Pr, Pz = _phgrad(g, P)
    K = Tr * Pz - Tz * Pr
    f = 1.0 / (4.0 * np.pi)
    # dq/dT = cT K ; dq/dT_r = sT Pz ; dq/dT_z = -sT Pr
    gT = f * (cT * K - g.dr(sT * Pz) - g.dzf(-sT * Pr))
    # dq/dP_r = -sT Tz ; dq/dP_z = sT Tr
    gP = f * (-g.dr(-sT * Tz) - g.dzf(sT * Tr))
    return gT, gP


def virial(comp):
    """E_A1 - E_A2 + 3 E_A4 ; zero at the minimum (A3 dropped)."""
    return comp['E_A1'] - comp['E_A2'] + 3.0 * comp['E_A4']


# ---------------------------------------------------------------------------
#  Initial condition: standard A_{1,1} axial Hopfion ring
# ---------------------------------------------------------------------------
def seed_ring(g, R0=2.0, width=1.0):
    """Theta = pi at ring core (rho=R0,z=0) -> 0 outside (quadratic flat top so
    sinTheta ~ s^2 near core => finite energy). Phi = poloidal angle around ring."""
    dR = g.RHO - R0
    s = np.sqrt(dR**2 + g.Z**2)
    prof = np.exp(-(s / width)**2)          # 1 at core, ->0 outside, flat top
    T = np.pi * prof
    P = np.arctan2(g.Z, dR)                  # poloidal angle, winds 2pi around ring
    T[0, :] = 0.0
    T[-1, :] = 0.0
    T[:, 0] = 0.0
    T[:, -1] = 0.0
    return T, P
