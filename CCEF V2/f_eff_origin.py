"""
CCEF v3.3 -- ORIGIN OF THE EXIT DRAIN SCALE (no fitting)
The Kubo verdict (kubo_exit.py) leaves the f_eff exit channel as the required fix.
Task: let f_eff come from a scale ALREADY in the theory, not a free parameter.

Claim: the drain is a TREE-LEVEL flavor-singlet portal a (d chi)^2 / f, with the
decay constant equal to the theory's own intermediate seesaw / inflation scale
        f = V^(1/4) = sqrt(M * Lambda)   (Sec 17.3, "the CC-residue scale")
which is fixed entirely by M (Newton matching) and Lambda (proton calibration).
Nothing is tuned.
"""
import numpy as np
pi=np.pi

# ---- inputs, all previously FIXED (no new dials) ----
Lam   = 0.231           # gap  = sqrt(A4) E0   (proton calibration)   [GeV]
M     = 1.77e19         # non-locality/compositeness scale (Newton)   [GeV]  N_eff=9
M_Pl  = 2.435e18        # reduced Planck                               [GeV]
e_B2  = 0.765           # 1/(4 A2)
N     = 9               # N_eff
m_a   = Lam             # inflaton mass = M Lam / f  with f=M  (Sec 17.6)
H_inf = 1.0             # de Sitter rate during inflation             [GeV]
BBN   = 1.1e-23         # required disposal rate before BBN           [GeV]
gstar = 10.75

# ---- the derived intermediate scale (the ONLY flavor-singlet scale between Lam and M)
V4   = np.sqrt(M*Lam)              # = V^(1/4), inflation / CC-residue scale
rho4 = np.sqrt(Lam*M_Pl)           # = rho_osc^(1/4), the leftover-condensate scale
print("Seesaw scales the theory already delivers (geometric means of gap & UV):")
print(f"  V^(1/4)      = sqrt(M*Lam)    = {V4:.3e} GeV   (inflation scale, Sec 17.3)")
print(f"  rho_osc^(1/4)= sqrt(Lam*M_Pl) = {rho4:.3e} GeV   (Sec 17.6)")
print(f"  (target 2.0e9 and 7.5e8 -- both reproduced)")
print()

# ---- two realizations of the a -> melt channel ----
# (i) anomaly/loop (what Sec 17.6 computed):  g = e_B^2 N/(8 pi^2 f)
def Gamma_anom(f):
    g = e_B2*N/(8*pi**2*f)
    return g**2 * m_a**3/(64*pi)
# (ii) tree-level flavor-singlet portal a (d chi)^2 / f  (the psi-sector portal)
def Gamma_tree(f):
    return m_a**3/(32*pi*f**2)

# thresholds (solve Gamma = BBN)
f_anom_thr = e_B2*N/(8*pi**2) * np.sqrt(m_a**3/(64*pi*BBN))
f_tree_thr = np.sqrt(m_a**3/(32*pi*BBN))
print("BBN thresholds on the decay constant:")
print(f"  anomaly channel : f_eff <= {f_anom_thr:.2e} GeV   (Sec 17.6 quote ~2e7-2e8)")
print(f"  tree portal     : f_eff <= {f_tree_thr:.2e} GeV")
print()

# ---- the derived value ----
print("Using the DERIVED scale f = V^(1/4) = sqrt(M Lam):")
G = Gamma_tree(V4)
print(f"  Gamma(a->chi chi) = m_a^3/(32 pi V4^2) = {G:.2e} GeV")
print(f"  BBN needs         >= {BBN:.2e} GeV      ->  clears by x{G/BBN:.1f}")
print()

# ---- consistency: immortal during inflation, decays just before BBN ----
print("Consistency of the SAME rate:")
print(f"  during inflation : Gamma/H_inf = {G/H_inf:.1e}  (<<1 -> inflaton immortal, Sec 17.6 intact)")
T_dec = np.sqrt(G*M_Pl/(1.66*np.sqrt(gstar)))*1e3   # MeV
print(f"  decay completes  : H=Gamma at T ~ {T_dec:.1f} MeV  (BBN ~1 MeV -> dumps just in time)")
print()
print("No parameter was fitted: f = sqrt(M*Lam), with M from Newton and Lam from the")
print("proton radius. The exit drain scale is the theory's own inflation scale.")
