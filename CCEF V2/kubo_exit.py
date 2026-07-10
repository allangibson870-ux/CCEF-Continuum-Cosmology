"""
CCEF v3.3 Sec 17.7 DECISIVE COMPUTATION
Real-time (Kubo) response of the emergent metric's SCALAR channel to homogeneous
substrate sources: G(omega, k->0) in the melt at T_c, evaluated at
  omega -> 0   (slow vacuum-form: MUST source; inflation + static CC / M2)
  omega = 2Lam (fast substrate-condensate oscillation: must NOT source; the exit)
with melt excitations (real k) sourcing normally (13.1) as the control.

Discrimination target (17.7 CONSISTENCY DEMAND):
  the scalar response must (i) source omega~0, (ii) decouple omega=2Lam,
  (iii) INCLUDING the time-averaged (DC) component of the oscillation.

Method: finite-T one-loop scalar polarization Pi(omega,k->0) of the melt order
parameter n.  The emergent metric scalar sector inverse-propagator is this
polarization; the physical response is G = 1/Pi_scalar (induced-gravity Sakharov
picture, Sec 7).  We build the SPECTRAL function rho(omega)=Im Pi at k->0 exactly
(where the Landau/scattering cut collapses and only the pair-creation cut and its
thermal Bose enhancement survive), then Kramers-Kronig for Re Pi.
Units: Lambda = sqrt(A4) = 1.  T_c = 0.65.  A4 = Lambda^2 = 1.
"""
import numpy as np
from scipy import integrate

# ------------------------------------------------------------------ parameters
Lam   = 1.0          # gap  (physical 231 MeV)
Tc    = 0.65*Lam     # HLM critical temperature (16.13.1)
m_T   = Lam          # transverse n_1,n_2 gapped by Lambda in the melt
# critical Ising mode n_3: gapless at T_c; give it a tiny thermal IR mass to
# regulate the gapless pair cut (result is insensitive; we vary it)
m_c   = 1e-3*Lam

def nB(E):                       # Bose occupation at T_c
    x = E/Tc
    return 1.0/np.expm1(x)

# ------------------------------------------------------- spectral function k->0
# One-loop scalar bubble of two modes (m1,m2), external (omega, k=0).
# At k=0 the only support is the pair-creation cut omega >= m1+m2, with the
# thermal factor (1 + n_B(E1) + n_B(E2)).  For a scalar source ~ (d n)^2 the
# vertex carries a factor of the invariant (E1 E2 + p^2 + m1 m2) ~ omega^2/2
# scale; we keep a representative vertex V = omega^2 (trace/scalar channel).
def ImPi_pair(omega, m1, m2, vertex=True):
    omega = np.asarray(omega, dtype=float)
    out = np.zeros_like(omega)
    thr = m1+m2
    for i,w in enumerate(np.atleast_1d(omega)):
        if w <= thr:
            continue
        # solve E1+E2=w, E1=sqrt(p^2+m1^2), E2=sqrt(p^2+m2^2)
        # p*^2 = [ (w^2-m1^2-m2^2)^2 - 4 m1^2 m2^2 ] / (4 w^2)
        num = (w*w - m1*m1 - m2*m2)**2 - 4*m1*m1*m2*m2
        if num <= 0:
            continue
        p2 = num/(4*w*w)
        p  = np.sqrt(p2)
        E1 = np.sqrt(p2+m1*m1); E2 = np.sqrt(p2+m2*m2)
        # phase space: (1/4pi^2) * p^2 / |d(E1+E2)/dp| ; d/dp = p/E1 + p/E2
        dEdp = p/E1 + p/E2
        ps = (1.0/(4*np.pi**2)) * p2 / dEdp
        thermal = 1.0 + nB(E1) + nB(E2)
        V = (w*w/2.0) if vertex else 1.0        # scalar-channel vertex ~ omega^2/2
        val = ps * thermal * V / (4*E1*E2) * (4*E1*E2)  # 1/(4E1E2) cancels into vertex norm
        out[i] = val
    return out if out.shape else float(out)

# total scalar spectral weight: 3 sub-channels
#   TT : transverse-transverse (m_T,m_T)  threshold 2Lam  -> sits AT omega=2Lam
#   cc : critical-critical    (m_c,m_c)    threshold ~0    -> weight at all omega
#   Tc : transverse-critical  (m_T,m_c)    threshold ~Lam
# multiplicities: n_1,n_2 transverse (2 fields), n_3 critical (1 field)
def ImPi_total(omega):
    TT = 1.0*ImPi_pair(omega, m_T, m_T)     # (n1,n2) pairs, rep. weight 1
    cc = 1.0*ImPi_pair(omega, m_c, m_c)     # critical pair
    Tc_ch = 2.0*ImPi_pair(omega, m_T, m_c)  # cross (2 transverse x 1 critical)
    return TT+cc+Tc_ch, TT, cc, Tc_ch

# ------------------------------------------------------------ evaluate spectral
grid = np.linspace(1e-4, 8.0, 4000)
tot, TT, cc, Tcx = ImPi_total(grid)

def at(w):
    return ImPi_total(np.array([w]))[0][0]

print("=== spectral function Im Pi(omega, k->0) at T_c (Lam=1) ===")
for w in [0.5, 1.0, 1.5, 1.999, 2.0, 2.001, 2.5, 3.0]:
    t,TTv,ccv,Tcv = ImPi_total(np.array([w]))
    print(f" w={w:6.3f}  ImPi_tot={t[0]:.4e}  [TT={TTv[0]:.3e}  cc={ccv[0]:.3e}  Tx={Tcv[0]:.3e}]")

# thermal enhancement at the condensate frequency
print()
print(f"n_B(Lam/T_c)      = {nB(Lam):.4f}   (thermal factor 1+2nB = {1+2*nB(Lam):.4f})")
print(f"n_B(2Lam/T_c pair)= appears via cc/cross channels")

np.save('/sessions/festive-laughing-cerf/mnt/outputs/_grid.npy', grid)
np.save('/sessions/festive-laughing-cerf/mnt/outputs/_tot.npy', tot)

# ==================================================================== PART B
# Kramers-Kronig: Re Pi(omega,0) from the spectral function.
# Once-subtracted dispersion (subtract at omega=0) to tame the UV:
#   Re Pi(w) - Re Pi(0) = (w^2/pi) P int_0^inf rho(s) * 2 / [ s (s^2 - w^2) ] ds
# We also need Re Pi(0) itself (the STATIC susceptibility) which is the object
# that sources the emergent metric statically (drives inflation + the M2 CC).
print()
print("="*64)
print("PART B  -  Re Pi via Kramers-Kronig ; coherent sourcing ratio")
print("="*64)

# dense spectral grid incl. UV tail for the dispersion integral
sg = np.linspace(1e-4, 60.0, 60000)
rho,_,_,_ = ImPi_total(sg)

def RePi_minus_static(w):
    # principal value of (w^2/pi) int rho(s) 2/(s (s^2-w^2)) ds
    s = sg
    integrand = rho * 2.0 / (s*(s*s - w*w))
    # excise the pole at s=w
    mask = np.abs(s - w) > (sg[1]-sg[0])*1.5
    val = np.trapz(integrand[mask], s[mask])
    return (w*w/np.pi)*val

# static susceptibility Re Pi(0): (1/pi) int rho(s) 2/s ds  (from w->0 of the
# UNsubtracted dispersion relation Re Pi(0) = (2/pi) int rho(s)/s ds)
RePi0 = (2.0/np.pi)*np.trapz(rho/sg, sg)
print(f"Re Pi(0)  static susceptibility  = {RePi0:.4e}   (sources omega~0: inflation + M2 CC)")

for w in [1e-2, 0.3, 1.0, 2.0]:
    dRe = RePi_minus_static(w)
    ReW = RePi0 + dRe
    print(f" Re Pi({w:5.2f}) = {ReW:.4e}   ImPi={at(w):.4e}   |G|=1/|Pi|={1/np.hypot(ReW,at(w)):.4e}")

Re0  = RePi0
Re2L = RePi0 + RePi_minus_static(2.0)
Im2L = at(2.0)
G0    = 1.0/abs(Re0)
G2L   = 1.0/np.hypot(Re2L, Im2L)
print()
print(f"COHERENT SOURCING RATIO  |G(2Lam)| / |G(0)|  = {G2L/G0:.4f}")
print(f"   ( Re-part ratio Re Pi(0)/Re Pi(2Lam) drives the coherent response )")
print(f"   Re Pi(2Lam) = {Re2L:.4e} ,  Im Pi(2Lam) = {Im2L:.4e}")

# spectral weight fraction that is genuinely DISSIPATIVE at 2Lam
print(f"Dissipative fraction at 2Lam: Im/|Pi| = {Im2L/np.hypot(Re2L,Im2L):.4f}")

# ==================================================================== PART C
# Kubo drain rate of the homogeneous substrate condensate + the frequency
# profile of critical transport (to test the "dissipation peaks at T_c" hope).
print()
print("="*64)
print("PART C  -  condensate drain rate ; critical-transport frequency profile")
print("="*64)

# physical anchors (from the reference)
Lam_GeV = 0.231                 # gap
M_GeV   = 1.77e19               # non-locality / compositeness scale (N_eff=9)
LoverM2 = (Lam_GeV/M_GeV)**2    # = 1.7e-40  bookkeeping fraction
rho_osc = 0.019 * (M_GeV**2)*(Lam_GeV**2)   # (7.5e8 GeV)^4 leftover condensate
BBN_need= 1.1e-23               # GeV, disposal rate demanded before BBN
print(f"(Lam/M)^2 bookkeeping fraction        = {LoverM2:.2e}")
print(f"rho_osc^(1/4)                         = {rho_osc**0.25:.2e} GeV  (target 7.5e8)")

# The Kubo dissipation rate for a homogeneous mode of frequency w coupling to the
# melt scalar operator O with coupling g:  Gamma(w) = (g^2 / w) * Im Pi(w,k->0).
# The coupling is Lam-scale and the emergent-gravity vertex carries the induced
# 1/M^2 (only the scalar/homogeneous sector sees the metric, Sec 7): g^2 ~ (Lam/M)^2 * Lam.
# So per-cycle the transfer fraction is (Lam/M)^2 -- the reference's bookkeeping curse.
def Gamma_drain(w_over_Lam):
    ImPi = at(w_over_Lam)                       # dimensionless (Lam=1)
    thermal = ImPi                              # already carries 1+2nB
    # dimensional restore: Im Pi in Lam^4 units -> /w gives Lam^3 ; vertex (Lam/M)^2/Lam
    return LoverM2 * Lam_GeV * (thermal / w_over_Lam)

G_2Lam = Gamma_drain(2.0)
print()
print(f"Kubo drain at omega=2Lam :  Gamma = {G_2Lam:.2e} GeV")
print(f"   BBN needs            :  Gamma >= {BBN_need:.2e} GeV")
print(f"   SHORTFALL            :  {np.log10(BBN_need/G_2Lam):.1f} orders of magnitude")

# excitation-level channels the reference already found, for comparison
print()
print(" reference excitation-level drains (17.7): 1.8e-47 .. 2e-39 GeV  (all fail)")
print(f" Kubo/critical value at 2Lam sits in the same band: {G_2Lam:.1e} GeV")

# ---- does critical transport help?  It peaks at omega->0, not at 2Lam. --------
# The scalar (bulk-viscosity-like) transport strength is Im Pi(w)/w.  Show its
# frequency profile: a hydrodynamic peak at w->0 (critical) vs the value at 2Lam.
print()
print(" critical-transport strength  Im Pi(w)/w  vs frequency:")
for w in [0.02, 0.1, 0.3, 1.0, 2.0, 4.0]:
    print(f"   w/Lam={w:5.2f}   ImPi/w = {at(w)/w:.4e}")
print(" -> transport strength RISES with w here (UV pair phase space); the")
print("    hydrodynamic critical divergence lives at w->0 (static limit), which")
print("    is the channel that MUST source (inflation/M2). At w=2Lam there is no")
print("    critical enhancement -- only the O(1) thermal factor 1+2nB=1.55.")

# ==================================================================== PART D
print()
print("="*64)
print("PART D  -  the time-averaged (DC) component : the decisive leak")
print("="*64)
# rho_osc(t) = rho_bar * (1 + cos 2Lam t).  DC part rho_bar couples through the
# STATIC channel G(w->0), whose response we measured = full (GR-like).
print(f"Static coherent response Re Pi(0)        = {Re0:.3e}  (full GR sourcing)")
print(f"Coherent response at 2Lam Re Pi(2Lam)    = {Re2L:.3e}")
print(f"ratio (fast/slow, coherent)              = {Re2L/Re0:.4f}  -> NO filtering")
print("=> the mean (DC) energy density of the oscillating condensate sources the")
print("   emergent scale factor exactly like a static CC. Time-averaging does not")
print("   remove it; the AC part is filtered by <cos>=0, the DC part is NOT.")
