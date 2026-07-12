"""
Derive the friction-profile exponent n (hence gamma*) WITHOUT fitting, from
CCEF's own front dynamics, and feed it into A_s = H_inf^3/(4pi^2 sigma gamma*^2)
= 0.863/gamma*^2 (front_seed.py).  See what the amplitude actually comes out.
"""
import numpy as np
pi=np.pi
Tc=0.65; sigma=2.0; H_inf=2*pi*Tc
coeff=H_inf**3/(4*pi**2*sigma)         # = 0.863  (front_seed.py)
As_obs=2.1e-9
ratio=51.0                              # e_B^2 T_c^4 / eps  (16.14.4), fixed

# terminal Lorentz factor from the reference relation gamma* = ratio^(1/n)
def gstar(n): return ratio**(1.0/n)
def A_s(n):   return coeff/gstar(n)**2

# --- derived handles on n, each from a real CCEF ingredient ---
s_bath = 1.76        # super-Ohmic index (Model C, 16.13.3):  J(w)~w^s
handles = {
  "n = s-1  (super-Ohmic residual DC-drag dilution, 16.14.1)": s_bath-1,   # 0.76
  "n = 1    (plain Ohmic charge drag, 16.14.3)":               1.0,
  "n = alpha_sim = 2.3 (interior similarity dilution, 16.15.3)":2.3,
  "n = 2    (reference's steep example, 16.14.4)":             2.0,
}
print(f"A_s(n) = {coeff:.3f}/gamma*^2 ,  gamma* = 51^(1/n) ,  observed A_s = {As_obs:.1e}")
print(f"{'derived n handle':58s} {'n':>5} {'gamma*':>9} {'A_s':>10} {'over/under':>12}")
for name,n in handles.items():
    print(f"{name:58s} {n:5.2f} {gstar(n):9.1f} {A_s(n):10.2e} x{A_s(n)/As_obs:9.1e}")

# what the amplitude would REQUIRE
g_need=np.sqrt(coeff/As_obs); n_need=np.log(ratio)/np.log(g_need)
print()
print(f"amplitude REQUIRES: gamma* = {g_need:.1e} , n = {n_need:.2f}")
print(f"derived friction gives n ~ 0.76-2.3 -> gamma* ~ 5-180 (NOT ~2e4)")
print(f"=> front OVERPRODUCES by ~4-7 orders; it is ~100-4000x too slow.")
