"""
ccef3d.py -- Full 3D CCEF Faddeev-Skyrme Hopf soliton (corrected action).
============================================================================
Field n(x) in S^2 on a periodic cubic box (background n=e_z).
Energy density (A3 -> 0 in IR, dropped):
  e = (A1/2) sum_a |grad n_a|^2
    + (A2/4) sum_{i,j} |d_i n x d_j n|^2          (Faddeev-Skyrme)
    + (A4/2) (1 - n_z^2)                            (= (A4/2)(1-n3^2))
Faddeev term via  |F_i x F_j|^2 = |F_i|^2|F_j|^2 - (F_i.F_j)^2,  F_i = d_i n.

Raw variation (before tangent projection):
  dE/dn_a =  -A1 lap(n_a)
            - A4 n_z delta_{a,z}
            - A2 sum_k d_k[ F_{k,a} (sum_j|F_j|^2) - sum_j (F_k.F_j) F_{j,a} ]
Gradient FLOW uses the tangent-projected force; |n|=1 renormalised each step.

Whitehead Hopf charge (FFT):  f_i = (1/8pi) eps_{ijk} n.(d_j n x d_k n)  (so
  integral of f over a 2-plane = degree).  B = 2*f  is the field strength vector;
  A from B=curl A via A_hat = i (k x B_hat)/k^2 ;  H = integral A . f  d^3x.
Normalisation calibrated so the analytic H=1 ring seed gives H≈1.
"""
import numpy as np

D = None  # derivative spacing set by Box


class Box:
    def __init__(self, L=2.2, N=64):
        self.N = N
        self.L = L
        self.x = np.linspace(-L, L, N, endpoint=False)
        self.dx = self.x[1] - self.x[0]
        X, Y, Z = np.meshgrid(self.x, self.x, self.x, indexing='ij')
        self.X, self.Y, self.Z = X, Y, Z
        self.RHO = np.sqrt(X**2 + Y**2)
        self.PHI = np.arctan2(Y, X)
        k = 2*np.pi*np.fft.fftfreq(N, d=self.dx)
        KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
        self.KX, self.KY, self.KZ = KX, KY, KZ
        self.K2 = KX**2 + KY**2 + KZ**2
        self.K2[0, 0, 0] = 1.0  # avoid /0


def d(box, f, ax):
    return (np.roll(f, -1, ax) - np.roll(f, 1, ax)) / (2*box.dx)


def lap(box, f):
    s = -6.0*f
    for ax in range(3):
        s = s + np.roll(f, 1, ax) + np.roll(f, -1, ax)
    return s/box.dx**2


def grads(box, n):
    """return F[i][a] = d_i n_a, list of 3 arrays each shape (3,N,N,N)."""
    return [np.stack([d(box, n[a], i) for a in range(3)]) for i in range(3)]


def energy_density(box, n, A1, A2, A4):
    F = grads(box, n)                      # F[i] shape (3,...)
    # A1
    gn2 = sum(np.sum(F[i]**2, axis=0) for i in range(3))
    e1 = 0.5*A1*gn2
    # A2  Faddeev
    e2 = np.zeros_like(n[0])
    for i in range(3):
        for j in range(3):
            Fi = F[i]; Fj = F[j]
            FiFi = np.sum(Fi*Fi, axis=0)
            FjFj = np.sum(Fj*Fj, axis=0)
            FiFj = np.sum(Fi*Fj, axis=0)
            e2 += FiFi*FjFj - FiFj**2
    e2 = 0.25*A2*e2
    # A4
    e4 = 0.5*A4*(1.0 - n[2]**2)
    return e1, e2, e4, F


def energies(box, n, A1, A2, A4):
    e1, e2, e4, _ = energy_density(box, n, A1, A2, A4)
    dV = box.dx**3
    return dict(E_A1=float(e1.sum()*dV), E_A2=float(e2.sum()*dV),
                E_A4=float(e4.sum()*dV),
                E=float((e1+e2+e4).sum()*dV))


def raw_grad(box, n, A1, A2, A4):
    """dE/dn_a (before projection), shape (3,N,N,N)."""
    F = grads(box, n)
    sumFj2 = sum(np.sum(F[j]**2, axis=0) for j in range(3))   # scalar field
    g = np.zeros_like(n)
    # A1 : exact discrete adjoint of central-diff gradient => -A1 sum_i d_i d_i
    for a in range(3):
        lap_d = sum(d(box, d(box, n[a], i), i) for i in range(3))
        g[a] += -A1*lap_d
    # A4
    g[2] += -A4*n[2]
    # A2 :  - A2 sum_k d_k[ F_k_a * sumFj2 - sum_j (F_k.F_j) F_j_a ]
    FkFj = [[np.sum(F[k]*F[j], axis=0) for j in range(3)] for k in range(3)]
    for a in range(3):
        for k in range(3):
            term = F[k][a]*sumFj2 - sum(FkFj[k][j]*F[j][a] for j in range(3))
            g[a] += -A2*d(box, term, k)
    return g


def proj_force(box, n, A1, A2, A4):
    """tangent-projected -dE/dn (descent direction)."""
    g = raw_grad(box, n, A1, A2, A4)
    ndotg = sum(n[a]*g[a] for a in range(3))
    f = np.empty_like(g)
    for a in range(3):
        f[a] = -(g[a] - ndotg*n[a])
    return f


def renorm(n):
    nn = np.sqrt(sum(n[a]**2 for a in range(3)))
    return n/nn


# ---- Whitehead Hopf charge -------------------------------------------------
def hopf_charge(box, n):
    F = grads(box, n)
    # f_i = (1/8pi) eps_ijk n.(d_j n x d_k n)
    def triple(j, k):   # n . (d_j n x d_k n)
        a, b = F[j], F[k]
        cx = a[1]*b[2]-a[2]*b[1]
        cy = a[2]*b[0]-a[0]*b[2]
        cz = a[0]*b[1]-a[1]*b[0]
        return n[0]*cx + n[1]*cy + n[2]*cz
    f = np.stack([triple(1, 2), triple(2, 0), triple(0, 1)])/(8*np.pi)
    B = 2.0*f
    Bx, By, Bz = np.fft.fftn(B[0]), np.fft.fftn(B[1]), np.fft.fftn(B[2])
    KX, KY, KZ, K2 = box.KX, box.KY, box.KZ, box.K2
    # A_hat = i (k x B_hat)/k^2
    Ax = 1j*(KY*Bz - KZ*By)/K2
    Ay = 1j*(KZ*Bx - KX*Bz)/K2
    Az = 1j*(KX*By - KY*Bx)/K2
    Ax[0,0,0]=Ay[0,0,0]=Az[0,0,0]=0
    A = [np.real(np.fft.ifftn(Ax)), np.real(np.fft.ifftn(Ay)), np.real(np.fft.ifftn(Az))]
    H = sum((A[i]*f[i]).sum() for i in range(3))*box.dx**3
    return float(H)


# ---- analytic H=1 ring seed ------------------------------------------------
def seed_ring(box, R0=0.8, width=0.5):
    dR = box.RHO - R0
    s = np.sqrt(dR**2 + box.Z**2)
    Th = np.pi*np.exp(-(s/width)**2)
    Phi = np.arctan2(box.Z, dR)
    ang = box.PHI + Phi
    n = np.stack([np.sin(Th)*np.cos(ang), np.sin(Th)*np.sin(ang), np.cos(Th)])
    return renorm(n)


def virial(comp):
    """E_A1 - E_A2 + 3 E_A4 (A3 dropped). Zero at minimum."""
    return comp['E_A1'] - comp['E_A2'] + 3.0*comp['E_A4']
