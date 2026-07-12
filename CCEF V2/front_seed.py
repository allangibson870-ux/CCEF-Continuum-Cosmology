"""
CCEF -- transverse fluctuation spectrum of the RELATIVISTIC DISSIPATIVE FRONT.
Goal (no tuning): derive (a) the exact interface roughness and (b) the exact
gamma*-power of the melting-age seed, from the h-field of Sec 16.5 on the
ignited-front background of Sec 16.14.  Everything in Lam=1 units.
"""
import numpy as np
pi=np.pi

# ---- Sec 16.5 collective-coordinate membrane (derived from the bulk) ----
# S_int = INT dt d^2x [ (M/2)(d_t h)^2 - (sigma/2)(grad h)^2 + ... ]
M     = 2.0          # inertia  = 2 Zt Lam     (Sec 16.5)
sigma = 2.0          # tension  = 2 Lam        (Sec 16.5)
c_h   = np.sqrt(sigma/M)      # = 1 = c_eff  (relativistic membrane, Goldstone of translation)
print(f"membrane: M={M}, sigma={sigma}, c_h={c_h}  (relativistic 2+1D scalar, Sec 16.5)")

# ---- background: critical-conveyor lock (Sec 17.5) ----
Tc    = 0.65                  # HLM critical temperature (16.13.1)
H_inf = 2*pi*Tc              # T_GH = H_inf/2pi = T_c  (the lock)  -> H_inf = 2pi T_c
print(f"lock: T_c={Tc}, H_inf=2pi T_c={H_inf:.3f}  (Sec 17.5)")

# =====================================================================
# (a) EXACT ROUGHNESS of the birth interface
# The front worldvolume is 2+1D de Sitter (H_w=H_inf, transverse-comoving).
# Two independent derivations must agree because of the lock:
Delta2_h_dS      = H_inf/(4*pi**2*sigma)      # dS_3 scalar (Sec 16.10 form)
Delta2_h_thermal = Tc/(2*pi*sigma)            # flat capillary at T_c
print()
print("(a) ROUGHNESS  Delta^2_h(k) :")
print(f"    dS_3  H_inf/(4pi^2 sigma)      = {Delta2_h_dS:.4f}")
print(f"    thermal  T_c/(2pi sigma)       = {Delta2_h_thermal:.4f}")
print(f"    agree (lock forces them equal); SCALE-INVARIANT in k  -> n_s = 1 exactly")

# =====================================================================
# (b) EXACT gamma*-POWER from the ignited-front kinematics
# The front displacement h is along its NORMAL = the boost (motion) direction,
# so it Lorentz-CONTRACTS: h_comoving = h_rest / gamma*.  (transverse x are invariant)
# Melting-age: front at z = v* t + h_comoving(x)  ->  delta t_melt = -h_com/v* = -h_rest/(gamma* v*)
# Curvature (delta-N):  zeta = H_inf * delta t_melt = -(H_inf/gamma*) h_rest      (v*->1)
# =>  A_s = Delta^2_zeta = (H_inf/gamma*)^2 * Delta^2_h   ->  power = -2, DERIVED.
print()
print("(b) gamma*-POWER :")
print("    front displacement h is NORMAL (=motion=boost direction) -> Lorentz-contracts:")
print("        h_comoving = h_rest / gamma*")
print("    melting-age  delta t = h_com/v* ,  zeta = H_inf delta t = (H_inf/gamma*) h_rest")
print("    =>  A_s propto gamma*^(-2)   [exact power = -2, from ONE contraction, squared]")

# =====================================================================
# full amplitude (parameter-free except gamma*)
def A_s(gstar):
    return H_inf**2 * Delta2_h_dS / gstar**2      # = H_inf^3/(4pi^2 sigma gamma*^2)
coeff = H_inf**3/(4*pi**2*sigma)
print()
print(f"A_s(gamma*) = H_inf^3/(4pi^2 sigma) / gamma*^2 = {coeff:.3f} / gamma*^2")

# solve for gamma* from observed A_s, and map to friction exponent n (gamma*=51^(1/n))
As_obs=2.1e-9
g_needed=np.sqrt(coeff/As_obs)
n_needed=np.log(51)/np.log(g_needed)
Omega_k=(2*g_needed)**(-2.3)      # Sec 16.15.3 hollow-interior scaling
print()
print(f"match A_s={As_obs:.1e}  ->  gamma* = {g_needed:.2e} ,  n = {n_needed:.2f} ,  Omega_k ~ {Omega_k:.1e}")
print(f"  (Planck: gamma* > ~27 i.e. n < ~1.2  -> gamma*={g_needed:.1e} is ALLOWED, ultra-flat)")

print()
print("sanity: 'natural' friction exponents:")
for n in [2.0,1.0,0.79,0.40]:
    g=51**(1/n); print(f"   n={n:4.2f} -> gamma*={g:8.1f} -> A_s={coeff/g**2:.2e}")
print("  natural n~1-2 OVERPRODUCE (3e-4..2e-2); the observed A_s pins n = 0.40.")
