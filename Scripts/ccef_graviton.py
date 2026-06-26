"""
ccef_graviton.py -- Composite (collective) spin-2 graviton from CCEF.
Action 1 of the roadmap: linearize delta-n about n=e_z and extract the
transverse-traceless (helicity +-2) part of the induced metric delta_g.

Uses the real CCEF action/coefficients and the ccef3d.py discretization.
Run:  python3 ccef_graviton.py      (needs ccef3d.py alongside)
"""
import numpy as np
import ccef3d as M

A1, A2, A4, Zt = 1.0, 0.3268, 3.5553, 1.0      # r3d96.py / reference sec 9
LAMBDA = np.sqrt(A4/A1)                          # IR gap ~1.886

# ---------------------------------------------------------------- A. dispersion
def dispersion(A3, N=64, L=2.6):
    box = M.Box(L=L, N=N); dx = box.dx
    print("[A] matter dispersion w^2=(A4+A1 k^2+A3 k^4)/Zt  (A3=%.4g)" % A3)
    print("     k      w2_lattice  w2_cont   z_local")
    for k in [0.3, 0.6, 1.0, 1.886, 3.0, 5.0]:
        kap2 = (2.0/dx**2)*(1.0-np.cos(k*dx))             # discrete -lap eig
        wl = (A4+A1*kap2+A3*kap2**2)/Zt
        wc = (A4+A1*k*k+A3*k**4)/Zt
        e = 1e-3*k; wcp = (A4+A1*(k+e)**2+A3*(k+e)**4)/Zt
        z = 0.5*(np.log(wcp)-np.log(wc))/(np.log(k+e)-np.log(k))
        print("   %6.3f  %9.4f  %8.4f   %.3f" % (k, wl, wc, z))
    print("     k_UV=sqrt(A1/A3)=%.4g  (z=1 below, z=2 above)\n" % np.sqrt(A1/A3))
    return box

# ---------------------------------------------- B. TT projection of induced dg
def tt_extract(box):
    print("[B] induced delta_g_ij = A1 sum_a d_i n_a d_j n_a -> TT (helicity +-2)")
    # each tangent component is a SUM of non-collinear waves, so the stress
    # d_i n d_j n has transverse (off-diagonal-direction) structure -> real TT part
    g=2*np.pi/box.L; X,Y,Z=box.X,box.Y,box.Z; eps=0.05
    def wave(K): return np.cos(K[0]*X+K[1]*Y+K[2]*Z)
    dn1=eps*(wave((2*g,1*g,0))+wave((0,2*g,1*g)))
    dn2=eps*(wave((1*g,0,2*g))+wave((1*g,-2*g,1*g)))
    n = M.renorm(np.stack([dn1, dn2, np.ones_like(X)]))
    F = M.grads(box, n)
    dg = np.zeros((3,3)+X.shape)
    for i in range(3):
        for j in range(3):
            dg[i,j] = A1*sum(F[i][a]*F[j][a] for a in range(3))
    dgk = np.fft.fftn(dg, axes=(2,3,4))
    kx,ky,kz = box.KX,box.KY,box.KZ
    k2f = kx**2+ky**2+kz**2; k2s = np.where(k2f==0,1.0,k2f)
    kv = np.stack([kx,ky,kz]); P = np.zeros((3,3)+kx.shape)
    for i in range(3):
        for j in range(3):
            P[i,j] = (1.0 if i==j else 0.0) - kv[i]*kv[j]/k2s
    Ph = np.einsum('ik...,kl...->il...', P, dgk)
    dgTT = np.einsum('il...,jl...->ij...', Ph, P) \
         - 0.5*np.einsum('ij...,...->ij...', P, np.einsum('kl...,kl...->...', P, dgk))
    m = k2f > 1e-12                                   # drop DC (TT ill-defined at k=0)
    div = np.stack([sum(kv[i]*dgTT[i,j] for i in range(3)) for j in range(3)])
    tr = sum(dgTT[i,i] for i in range(3))
    pTT = np.sum(np.abs(dgTT[:,:,m])**2); pTot = np.sum(np.abs(dgk[:,:,m])**2)
    print("     helicity +-2 fraction = %.3f" % np.sqrt(pTT/pTot))
    print("     transversality |k.dgTT|/||.|| = %.1e" % (np.max(np.abs(div[:,m]))/np.sqrt(pTT)))
    print("     tracelessness  |tr|/||.||     = %.1e\n" % (np.max(np.abs(tr[m]))/np.sqrt(pTT)))

# --------------------------------------- C. induced graviton kinetic stiffness
def induced(A3, Lq=24.0, nq=64, Wm=24.0, nw=96):
    q = np.linspace(-Lq,Lq,nq,endpoint=False)+Lq/nq; dq = q[1]-q[0]
    ws = np.linspace(-Wm,Wm,nw,endpoint=False)+Wm/nw; dw = ws[1]-ws[0]
    QX,QY,QZ = np.meshgrid(q,q,q,indexing='ij'); q2 = QX**2+QY**2+QZ**2
    Eq2 = A4+A1*q2+A3*q2**2
    W = 0.5*A1**2*(QX**2+QY**2)**2                    # TT-contracted A1 vertex
    pref = dq**3*dw/(2*np.pi)**4
    def Pi(pw, pz):
        p2 = QX**2+QY**2+(QZ+pz)**2; Ep2 = A4+A1*p2+A3*p2**2
        return pref*sum(np.sum(W/((w*w+Eq2)*((w+pw)**2+Ep2))) for w in ws)
    h = 0.2; base = Pi(0,0); stiff = (Pi(h,0)-base)/h**2
    print("[C] induced graviton (Sakharov bubble)  A3=%.3g" % A3)
    print("     Pi^TT(0)               = %.4e" % base)
    print("     |kinetic stiffness|    = %.4e   (finite => spin-2 propagates)" % abs(stiff))
    print("     k_UV = %.4g\n" % np.sqrt(A1/A3))
    return base, stiff

if __name__ == "__main__":
    box = dispersion(0.281); tt_extract(box)
    induced(0.281); induced(1e-6)
