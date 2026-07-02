import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import kv, k0, k1
from scipy.optimize import minimize_scalar

# Growth on CCEF coasting background a ~ t, H = H0/a = H0(1+z).
# Sub-horizon, induced-Einstein (eta=Sigma=1) Poisson source.
# Growth eq in N=ln a:  D'' + (2 + Hdot/H^2) D' = (4 pi G rho_m/H^2) D
# Coasting: Hdot/H^2 = -1 -> friction coeff = 1
#           4 pi G rho_m/H^2 = (3/2) Om0 e^{-N}
# => D'' + D' = (3/2) Om0 e^{-N} D

def growth_numeric(Om0, z_grid):
    # integrate from high z (N small) to z=0 (N=0). Growing-mode IC deep in past.
    Ni = np.log(1/(1+1000.0)); Nf = 0.0
    # growing-mode seed from analytic small-a (large ξ) form D ~ sqrt(ξ) exp(-b ξ), b=sqrt(6 Om0)
    b = np.sqrt(6*Om0); xi_i = np.sqrt(1+1000.0)
    D_i = np.sqrt(xi_i)*np.exp(-b*xi_i)
    # dD/dN at start from f = bξ/2 - 1/4 (large-ξ asymptote)
    f_i = b*xi_i/2 - 0.25
    dD_i = f_i*D_i
    def rhs(N,y):
        D,dD = y
        return [dD, -dD + 1.5*Om0*np.exp(-N)*D]
    Ns = -np.log(1+z_grid)
    sol = solve_ivp(rhs,[Ni,Nf],[D_i,dD_i],t_eval=np.sort(Ns),rtol=1e-10,atol=1e-30,dense_output=True)
    return sol

def D_closed(Om0, z):
    b=np.sqrt(6*Om0); xi=np.sqrt(1+z)
    return xi*k1(b*xi)
def f_closed(Om0, z):
    b=np.sqrt(6*Om0); xi=np.sqrt(1+z)
    return (b*xi/2)*k0(b*xi)/k1(b*xi)
def fs8_over_s80(Om0, z):
    b=np.sqrt(6*Om0)
    return (b/2)*(1+z)*k0(b*np.sqrt(1+z))/k1(b)  # = f * D(z)/D(0)

# --- verify closed form vs numeric ---
for Om0 in [0.31,0.05,1.0]:
    zt=np.array([0.0,0.2,0.5,1.0,2.0])
    sol=growth_numeric(Om0,zt)
    Dc=np.array([D_closed(Om0,z) for z in zt])
    # numeric D sorted in N ascending = z descending
    order=np.argsort(-zt)
    Dn=sol.y[0]  # matches sorted N (ascending) -> z descending
    Dn_z = Dn[::-1]  # now z ascending
    # normalize both to z=0
    Dn_z=Dn_z/Dn_z[0]; Dc=Dc/Dc[0]
    print(f"Om0={Om0}: closed/numeric D(z)/D0 ratio max dev = {np.max(np.abs(Dn_z-Dc)):.2e}")

print()
print("fsigma8(z)/sigma8(0) shape:")
zs=np.array([0.0,0.15,0.38,0.51,0.61,0.85,1.0,1.48])
for Om0 in [0.31,0.05,1.0]:
    vals=[fs8_over_s80(Om0,z) for z in zs]
    print(f" Om0={Om0}: ", " ".join(f"{v:.3f}" for v in vals))

print()
print("f(z=0):")
for Om0 in [0.31,0.05,1.0]:
    print(f" Om0={Om0}: f0={f_closed(Om0,0):.3f}")
