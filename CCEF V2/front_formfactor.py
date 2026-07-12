"""
Unavoidable averaging between the microscopic interface field h(x) and the
cosmological delta-N field: the FINITE WALL THICKNESS.
The Sec 16.5 membrane (rigid profile n_bar(z-h)) is the thin-wall / long-wavelength
limit, valid only for transverse k << Lambda (wall thickness delta = 1/Lambda).
A wall cannot hold a corrugation finer than its own thickness -> the melting-age
is SMEARED over the wall profile -> a derived form factor F(k) cutting off at k~Lambda.
Crucially: modes cross the (quasi-dS) horizon at k_phys = H_inf, and H_inf = 2pi T_c.
"""
import numpy as np
pi=np.pi
Tc=0.65; Lam=1.0; sigma=2.0
H_inf=2*pi*Tc                 # the lock (17.5)
x=H_inf/Lam                   # = 2pi T_c / Lam  -- DERIVED, no fit
print(f"H_inf/Lam = 2pi T_c/Lam = {x:.3f}   (all observable modes cross here -> uniform, keeps n_s=1)")
print()

# candidate finite-thickness form factors (zero-mode of theta(z)=2 arctan(e^{Lam z}))
# amplitude form factors F(k); power suppression = F^2
FFs = {
 "sech(pi k/2Lam)  (sech zero-mode FT)": 1/np.cosh(pi*x/2),
 "(pi k/2Lam)/sinh(pi k/2Lam)":          (pi*x/2)/np.sinh(pi*x/2),
 "exp(-k/Lam)      (simple exp tail)":   np.exp(-x),
 "exp(-(k/Lam)^2/2) (gaussian smear)":   np.exp(-x**2/2),
}
print(f"{'form factor F(H_inf)':40s} {'F':>10} {'F^2 (power)':>12}")
for name,F in FFs.items():
    print(f"{name:40s} {F:10.2e} {F**2:12.2e}")
print()

# combine with the friction-derived amplitude A_s = 0.863/gamma*^2 (front_seed/front_n)
coeff=H_inf**3/(4*pi**2*sigma)   # 0.863
As_obs=2.1e-9
print(f"A_s = {coeff:.3f}/gamma*^2 * F^2   (F^2 = the unavoidable averaging)")
print(f"{'n (friction)':>12} {'gamma*':>8} {'bare A_s':>10}   then x F^2 for each form factor:")
for n in [0.76,1.0]:
    g=51**(1/n); bare=coeff/g**2
    row=f"{n:12.2f} {g:8.1f} {bare:10.2e}   "
    for name,F in FFs.items():
        row+=f"{bare*F**2:9.1e} "
    print(row)
print(f"   (target A_s = {As_obs:.1e})")
print()
# what F^2 exactly cancels the overproduction, for each n
for n in [0.76,1.0,2.0]:
    g=51**(1/n); need=As_obs/(coeff/g**2)
    alpha=-np.log(np.sqrt(need))/x    # F=exp(-alpha x)
    print(f"n={n:4.2f}: needed F^2={need:.1e} -> F=exp(-alpha*{x:.2f}) with alpha={alpha:.2f} (O(1))")
