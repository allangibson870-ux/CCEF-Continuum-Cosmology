import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
from scipy.special import k0,k1
c=299792.458  # km/s

# ================= 1. COSMIC CHRONOMETER H(z) =================
# Moresco-compilation representative (z, H, sigmaH)
cc=np.array([
(0.07,69,19.6),(0.09,69,12),(0.12,68.6,26.2),(0.17,83,8),(0.179,75,4),(0.199,75,5),
(0.2,72.9,29.6),(0.27,77,14),(0.28,88.8,36.6),(0.352,83,14),(0.38,83,13.5),(0.4,95,17),
(0.4004,77,10.2),(0.425,87.1,11.2),(0.445,92.8,12.9),(0.47,89,49.6),(0.4783,80.9,9),
(0.48,97,62),(0.593,104,13),(0.68,92,8),(0.75,98.8,33.6),(0.781,105,12),(0.875,125,17),
(0.88,90,40),(0.9,117,23),(1.037,154,20),(1.3,168,17),(1.363,160,33.6),(1.43,177,18),
(1.53,140,14),(1.75,202,40),(1.965,186.5,50.4)])
zc,Hc,eHc=cc.T

def E_lcdm(z,Om): return np.sqrt(Om*(1+z)**3+(1-Om))

def chi2_cc_coast():
    # H=H0(1+z); best H0 analytic (linear)
    x=(1+zc)
    H0=np.sum(x*Hc/eHc**2)/np.sum(x**2/eHc**2)
    return np.sum(((H0*x-Hc)/eHc)**2),H0
def chi2_cc_lcdm(Om):
    x=E_lcdm(zc,Om)
    H0=np.sum(x*Hc/eHc**2)/np.sum(x**2/eHc**2)
    return np.sum(((H0*x-Hc)/eHc)**2),H0

x2c,H0c=chi2_cc_coast()
x2l,H0l=chi2_cc_lcdm(0.31)
rl=minimize_scalar(lambda Om:chi2_cc_lcdm(Om)[0],bounds=(0.1,0.6),method='bounded')
x2lf,H0lf=chi2_cc_lcdm(rl.x)
print("=== H(z) cosmic chronometers (%d pts) ==="%len(zc))
print(f" coasting H=H0(1+z): H0={H0c:.1f}, chi2={x2c:.1f}, chi2/dof={x2c/(len(zc)-1):.2f}")
print(f" LCDM Om=0.31      : H0={H0l:.1f}, chi2={x2l:.1f}, chi2/dof={x2l/(len(zc)-1):.2f}")
print(f" LCDM Om free={rl.x:.3f}: H0={H0lf:.1f}, chi2={x2lf:.1f}")
print(f" -> coasting overshoot vs LCDM: H_coast/H_lcdm at z=0.5,1,2 = "
      f"{1.5/E_lcdm(0.5,0.31):.2f}, {2.0/E_lcdm(1,0.31):.2f}, {3.0/E_lcdm(2,0.31):.2f}")

# ================= 2. BAO nuisance-free Alcock-Paczynski F_AP = D_M/D_H = D_M*H/c =================
# DR12+eBOSS consensus (z, D_M/r_d, D_H/r_d) approx
bao=np.array([
(0.38,10.23,25.00),(0.51,13.36,22.33),(0.70,17.86,19.33),(1.48,30.69,13.26),(2.33,37.6,8.93)])
zb=bao[:,0]; FAP_obs=bao[:,1]/bao[:,2]
eFAP=0.045*FAP_obs   # ~4.5% indicative (propagated DR16 errors)
def FAP_coast(z): return np.log(1+z)*(1+z)
def FAP_lcdm(z,Om):
    dc=np.array([quad(lambda zz:1/E_lcdm(zz,Om),0,zi)[0] for zi in np.atleast_1d(z)])
    return E_lcdm(z,Om)*dc
x2b_c=np.sum(((FAP_coast(zb)-FAP_obs)/eFAP)**2)
x2b_l=np.sum(((FAP_lcdm(zb,0.31)-FAP_obs)/eFAP)**2)
print("\n=== BAO Alcock-Paczynski F_AP=D_M/D_H (nuisance-free, %d pts) ==="%len(zb))
print(" z    :"," ".join(f"{z:5.2f}" for z in zb))
print(" obs  :"," ".join(f"{v:5.3f}" for v in FAP_obs))
print(" coast:"," ".join(f"{v:5.3f}" for v in FAP_coast(zb)))
print(" lcdm :"," ".join(f"{v:5.3f}" for v in FAP_lcdm(zb,0.31)))
print(f" chi2: coasting={x2b_c:.1f}, LCDM={x2b_l:.1f}  (dof={len(zb)})")

# ================= 3. GROWTH (from prior note) + DESI/Euclid forecast =================
def coast_fs8(z,Om0,s80):
    b=np.sqrt(6*Om0); return s80*(b/2)*(1+z)*k0(b*np.sqrt(1+z))/k1(b)
# LCDM fs8
from scipy.integrate import solve_ivp
def lcdm_fs8(z,Om0,s80):
    def E2(a): return Om0*a**-3+(1-Om0)
    def dl(a): return (-3*Om0*a**-4)/E2(a)*a
    def rhs(N,Y):
        a=np.exp(N);D,dD=Y; return[dD,-(2+0.5*dl(a))*dD+1.5*(Om0*a**-3/E2(a))*D]
    s=solve_ivp(rhs,[np.log(1/1001.),0.],[1e-3,1e-3],dense_output=True,rtol=1e-9,atol=1e-12)
    N=-np.log(1+np.atleast_1d(z)); D=s.sol(N)[0];dD=s.sol(N)[1];D0=s.sol(0.)[0]
    return s80*(dD/D)*D/D0
# best-fit norms from prior RSD fit:
s80_c,Om_c=0.848,0.31; s80_l,Om_l=0.784,0.315
zf=np.array([0.5,0.8,1.1,1.4,1.7,2.0])
fc=coast_fs8(zf,Om_c,s80_c); fl=lcdm_fs8(zf,Om_l,s80_l)
print("\n=== DESI/Euclid high-z fs8 forecast ===")
print(" assume ~2.5% fs8 measurement (DESI/Euclid target). separation in sigma:")
print(" z    :"," ".join(f"{z:5.2f}" for z in zf))
print(" coast:"," ".join(f"{v:5.3f}" for v in fc))
print(" lcdm :"," ".join(f"{v:5.3f}" for v in fl))
sep=np.abs(fc-fl)/(0.025*0.5*(fc+fl))
print(" |Δ|/σ:"," ".join(f"{v:5.1f}" for v in sep))
print(f" combined (quadrature) separation over 6 bins: {np.sqrt(np.sum(sep**2)):.1f} sigma")
