import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import k0,k1
from scipy.optimize import minimize

# ---- representative RSD f*sigma8 compilation (z, fs8, err) ----
data = np.array([
 (0.02,0.428,0.0465),(0.067,0.423,0.055),(0.10,0.37,0.13),(0.15,0.49,0.145),
 (0.17,0.51,0.06),(0.18,0.36,0.09),(0.38,0.44,0.06),(0.51,0.46,0.05),
 (0.60,0.39,0.063),(0.61,0.44,0.057),(0.73,0.437,0.072),(0.85,0.315,0.095),
 (1.0,0.36,0.09),(1.48,0.46,0.045)])
z=data[:,0]; y=data[:,1]; e=data[:,2]

# ---- CCEF coasting closed form: fs8 = s80 * (b/2)(1+z) K0(b*sqrt(1+z))/K1(b), b=sqrt(6 Om0) ----
def coast_fs8(z, Om0, s80):
    b=np.sqrt(6*Om0)
    return s80*(b/2)*(1+z)*k0(b*np.sqrt(1+z))/k1(b)

# best-fit s80 at fixed Om0 (linear -> closed form), then chi2
def coast_chi2(Om0):
    shape=coast_fs8(z,Om0,1.0)
    s80=np.sum(shape*y/e**2)/np.sum(shape**2/e**2)  # analytic linear best fit
    chi2=np.sum(((s80*shape-y)/e)**2)
    return chi2,s80

# joint best Om0
from scipy.optimize import minimize_scalar
r=minimize_scalar(lambda Om:coast_chi2(Om)[0],bounds=(0.02,2.0),method='bounded')
Om_best=r.x; chi2_c,s80_c=coast_chi2(Om_best)
chi2_031,s80_031=coast_chi2(0.31)

# ---- LCDM growth for comparison ----
def lcdm_fs8(z,Om0,s80):
    # D''+ (2+Hdot/H2)D' = 1.5 Om(a) D ; E2=Om0 a^-3+(1-Om0)
    def E2(a): return Om0*a**-3+(1-Om0)
    def dlnE2(a): return (-3*Om0*a**-4)/E2(a)*a  # d lnE2/dlna
    def rhs(N,Y):
        a=np.exp(N); D,dD=Y
        fric=2+0.5*dlnE2(a)
        src=1.5*(Om0*a**-3/E2(a))
        return [dD,-fric*dD+src*D]
    Ni=np.log(1/1001.); 
    sol=solve_ivp(rhs,[Ni,0.0],[1e-3,1e-3],dense_output=True,rtol=1e-9,atol=1e-12)
    N=-np.log(1+z)
    D=sol.sol(N)[0]; dD=sol.sol(N)[1]
    f=dD/D
    D0=sol.sol(0.0)[0]
    return s80*f*D/D0
def lcdm_chi2(Om0):
    shape=lcdm_fs8(z,Om0,1.0)
    s80=np.sum(shape*y/e**2)/np.sum(shape**2/e**2)
    return np.sum(((s80*shape-y)/e)**2),s80
chi2_l,s80_l=lcdm_chi2(0.315)

print("=== CCEF COASTING (a~t, GR-like subhorizon growth) ===")
print(f" fixed Om0=0.31 : best-fit sigma8(0)={s80_031:.3f}, chi2={chi2_031:.2f}, chi2/dof={chi2_031/(len(z)-1):.2f}")
print(f" free  Om0={Om_best:.3f} : sigma8(0)={s80_c:.3f}, chi2={chi2_c:.2f}, chi2/dof={chi2_c/(len(z)-2):.2f}")
print("=== LCDM (Planck Om=0.315) ===")
print(f" sigma8(0)={s80_l:.3f}, chi2={chi2_l:.2f}, chi2/dof={chi2_l/(len(z)-1):.2f}")

print()
print("model fs8 at data z (coasting Om0=0.31, s80=%.3f):"%s80_031)
print(" z   :", " ".join(f"{zz:5.2f}" for zz in z))
print(" data:", " ".join(f"{v:5.2f}" for v in y))
print(" coas:", " ".join(f"{v:5.2f}" for v in coast_fs8(z,0.31,s80_031)))
print(" lcdm:", " ".join(f"{v:5.2f}" for v in lcdm_fs8(z,0.315,s80_l)))
print()
print("f(z=0):  coasting Om0=0.31 -> %.3f ; LCDM Om0=0.315 -> %.3f"%(
    coast_fs8(0,0.31,1.0)/coast_fs8(0,0.31,1.0)*( (np.sqrt(6*0.31)/2)*k0(np.sqrt(6*0.31))/k1(np.sqrt(6*0.31)) ),
    lcdm_fs8(np.array([0.0]),0.315,1.0)[0]/(lcdm_fs8(np.array([0.0]),0.315,1.0)[0])* (0.315**0.55) ))

print("\n=== HIGH-Z DISCRIMINATOR: fs8(z) coasting vs LCDM (both normalized to their best fit) ===")
zhi=np.array([0.5,1.0,1.5,2.0,2.5,3.0,4.0,5.0])
c=coast_fs8(zhi,0.31,0.848)
l=lcdm_fs8(zhi,0.315,0.784)
print(" z    :", " ".join(f"{zz:5.1f}" for zz in zhi))
print(" coast:", " ".join(f"{v:5.3f}" for v in c))
print(" lcdm :", " ".join(f"{v:5.3f}" for v in l))
print(" ratio:", " ".join(f"{cc/ll:5.2f}" for cc,ll in zip(c,l)))

# clean f(z=0) both
b=np.sqrt(6*0.31); f0c=(b/2)*k0(b)/k1(b)
f0l=lcdm_fs8(np.array([0.0]),0.315,1.0)[0]/ (lcdm_fs8(np.array([1e-6]),0.315,1.0)[0]) # ~ f since D~D0
# proper LCDM f0:
def lcdm_f(z,Om0):
    def E2(a): return Om0*a**-3+(1-Om0)
    def dlnE2(a): return (-3*Om0*a**-4)/E2(a)*a
    def rhs(N,Y):
        a=np.exp(N); D,dD=Y
        return [dD,-(2+0.5*dlnE2(a))*dD+1.5*(Om0*a**-3/E2(a))*D]
    sol=solve_ivp(rhs,[np.log(1/1001.),0.0],[1e-3,1e-3],dense_output=True,rtol=1e-9,atol=1e-12)
    N=-np.log(1+z); return (sol.sol(N)[1]/sol.sol(N)[0])
print(f"\n f(0): coasting={f0c:.3f} (Om0=0.31), LCDM={lcdm_f(0.0,0.315):.3f}, Om^0.55={0.315**0.55:.3f}")
