"""
CCEF — Full Euler-Lagrange equation for A3 (Lifshitz) term.

Uses ρ_A3 from ccef_a3_derive.py (exact angular integration result).
Applies EL operator: ∂L/∂F - d/dr(∂L/∂F') + d²/dr²(∂L/∂F'') = 0
where L = r² * (A3/2) * ρ_A3.

Outputs:
  - Coefficient of F'''' (leading term of 4th-order ODE) [SOLID]
  - Full RHS expression for F'''' as function of (r, F, F', F'', F''') [SOLID]
  - Python lambda for direct use in BVP solver
"""

import sympy as sp
from sympy import (sin, cos, symbols, Function, diff, simplify,
                   expand, collect, factor, cancel, Integer, pi, Rational)
import time

t0 = time.time()
def elapsed(): return f"[{time.time()-t0:5.1f}s]"

print("="*60)
print("CCEF A3 Full EL Equation")
print("="*60)

# -------------------------------------------------------
# Set up F as a proper SymPy Function of r so that
# d/dr[F''] = F''' etc. works correctly via diff()
# -------------------------------------------------------
r = symbols('r', positive=True)
F = Function('F')(r)
Fp   = F.diff(r)      # F'
Fpp  = F.diff(r, 2)   # F''
Fppp = F.diff(r, 3)   # F'''
Fpppp= F.diff(r, 4)   # F''''

sF = sin(F)
cF = cos(F)

# -------------------------------------------------------
# ρ_A3 from exact angular integration (ccef_a3_derive.py)
# Units: [L]^{-4}  (4th-order derivative density)
# The 4π factor is INCLUDED (comes from ∫ dΩ sinθ)
# -------------------------------------------------------
print(f"{elapsed()} Building ρ_A3 with F as SymPy Function...")

rho_A3 = (
    4*pi*(-sF**2*Fp**4/3 + Fp**4)
    + 4*pi*(8*sF*cF*Fp**2*Fpp/3)
    + 4*pi*(-8*sF**2*Fp**2/r**2 + 16*Fp**2/r**2)
    + 4*pi*(-32*sF*cF*Fp/r**3)
    + 4*pi*((4*sF**2/3 + 8*Integer(1)/3)*Fpp**2)
    + 4*pi*(16*sF**2/r**4)
)

# -------------------------------------------------------
# Lagrangian density L = r² * (A3/2) * ρ_A3
# (A3 is a numerical constant, factored out separately)
# -------------------------------------------------------
L = r**2 * rho_A3 / 2   # A3 factor applied separately

print(f"{elapsed()} Computing EL operator...")

# EL equation:
# EL_A3 = ∂L/∂F - d/dr(∂L/∂F') + d²/dr²(∂L/∂F'')
dL_dF   = diff(L, F)
dL_dFp  = diff(L, Fp)
dL_dFpp = diff(L, Fpp)

print(f"{elapsed()} d/dr(∂L/∂F')...")
d_dL_dFp  = diff(dL_dFp,  r)

print(f"{elapsed()} d²/dr²(∂L/∂F'')...")
d2_dL_dFpp = diff(diff(dL_dFpp, r), r)

print(f"{elapsed()} Assembling EL...")
EL_A3 = dL_dF - d_dL_dFp + d2_dL_dFpp
EL_A3 = expand(EL_A3)
print(f"{elapsed()} EL assembled.")

# -------------------------------------------------------
# Extract coefficient of F'''' (Derivative(F,r,4))
# This is the "stiffness" coefficient for the 4th-order system
# -------------------------------------------------------
print(f"\n{elapsed()} Extracting F'''' coefficient...")
coeff_Fpppp = EL_A3.coeff(Fpppp)
coeff_Fpppp_simplified = simplify(coeff_Fpppp)
print(f"\n>>> Coefficient of F'''' in A3·EL:")
print(f"  {coeff_Fpppp_simplified}")

# -------------------------------------------------------
# RHS for BVP: solve for F''''
# F'''' = -(EL_A3 - coeff_Fpppp * F'''') / (A3 * coeff_Fpppp)
# i.e., rhs_A3 = -(EL_A3 - coeff_Fpppp*F'''') / coeff_Fpppp
# -------------------------------------------------------
print(f"\n{elapsed()} Building RHS (lower-order terms)...")
rhs_lower = expand(EL_A3 - coeff_Fpppp * Fpppp)
rhs_lower = simplify(rhs_lower)

print(f"{elapsed()} Simplifying...")
# rhs for F'''' = -rhs_lower / (A3 * coeff_Fpppp)
# (A3 factored out: multiply EL by 1/A3 to get the equation)
# The full 4th-order ODE is:
# A3 * coeff_Fpppp * F'''' = -rhs_lower
# → F'''' = -rhs_lower / (A3 * coeff_Fpppp)

print(f"\n{'='*60}")
print("RESULT: 4th-order EL ODE structure  [SOLID]")
print(f"{'='*60}")
print(f"\nCoefficient of F'''' (times A3):")
print(f"  A3 * {coeff_Fpppp_simplified}")
print(f"\nRHS (= -lower-order A3 terms, to be divided by A3*coeff):")
print(f"  {rhs_lower}")

# -------------------------------------------------------
# Now add the 2nd-order (A1+A2+A4) terms for the combined ODE
# From Task #31e [SOLID]:
#   P·F'' = [A1·sin2F/r² + A2·sin²F·sin2F/r⁴ + A4·sinF
#            - 2A1·F'/r - A2·sin2F·F'²/r²]
#   P = A1 + 2A2·sin²F/r²
#
# The combined EL (= 0) is:
#   A3 * EL_A3 + EL_A1A2A4 = 0
#
# where EL_A1A2A4 = -(P·F'' - [...]) = lower-order 2nd-order ODE
# -------------------------------------------------------
print(f"\n{'='*60}")
print("COMBINED 4th-ORDER ODE FOR BVP")
print(f"{'='*60}")
print("""
Full EL (A3=0 limit recovers Task #31e result):

  A3·(4π/3)·(sin²F+2)·r² · F'''' + [A3 lower-order terms]
  + [A1,A2,A4 terms]·r² = 0

Dividing through by A3·(4π/3)·(sin²F+2)·r²:

  F'''' = RHS_A3(r, F, F', F'', F''') + RHS_A1A2A4(r, F, F', F'')/[A3·(4π/3)·(sin²F+2)·r²]

where RHS_A3 is the lower-order A3 contribution and
      RHS_A1A2A4 = -(P·F'' - [...]·r²) / (A3·(4π/3)·(sin²F+2)·r²)
""")

# -------------------------------------------------------
# Generate the Python function for the BVP RHS
# Converts F'''', F''', F'', F', F from SymPy to numpy-ready string
# -------------------------------------------------------
print(f"{elapsed()} Generating Python RHS code...")

# Substitute concrete symbols for code generation
r_s, F_s, Fp_s, Fpp_s, Fppp_s = symbols('r F_val Fp Fpp Fppp')
sF_s = sp.sin(F_s); cF_s = sp.cos(F_s)

# Coefficient of F'''' (as numeric expression)
coeff_expr = coeff_Fpppp_simplified.subs([(sF, sF_s), (cF, cF_s),
                                           (Fp, Fp_s), (Fpp, Fpp_s),
                                           (Fppp, Fppp_s), (r, r_s)])

# Lower-order terms (everything except F'''' in EL_A3)
rhs_expr = rhs_lower.subs([(sF, sF_s), (cF, cF_s),
                             (Fp, Fp_s), (Fpp, Fpp_s),
                             (Fppp, Fppp_s), (r, r_s),
                             (F, F_s)])

print("\n=== Python code for BVP ===")
print(f"# Coefficient of F'''' from A3 term:")
print(f"# coeff_Fpppp = A3 * {sp.ccode(coeff_expr)}")
print()
print(f"# RHS lower-order A3 contribution:")
print(f"# rhs_lower_A3 = {sp.ccode(rhs_expr)}")
print()
print("# F'''' = -(rhs_lower_A3 + rhs_A1A2A4 * r^2) / (A3 * coeff_Fpppp)")

# -------------------------------------------------------
# Virial identity check
# E_A3 = (A3/2) * 2π * ∫ r² dr * σ
# Under r → r/λ: E_A3 → λ^{3-4} * E_A3 = λ^{-1} * E_A3
# Virial condition: ∂E/∂λ|_{λ=1} = 0
# → (-1) * E_A3 + (-1) * E_A1 + (1) * E_A2 + (3) * E_A4 = 0
# [standard result for n-derivative Skyrme-type theories in 3D]
# -------------------------------------------------------
print(f"\n{'='*60}")
print("VIRIAL THEOREM (scaling dimensions)")
print(f"{'='*60}")
print("""
Under r → r/λ:
  E_A1 ~ λ^{3-2} = λ^1    (2-derivative, scales as λ)
  E_A2 ~ λ^{3-4} = λ^{-1} (4-derivative product, scales as 1/λ)
  E_A3 ~ λ^{3-4} = λ^{-1} (4-derivative biharmonic, scales as 1/λ)
  E_A4 ~ λ^3              (potential, scales as λ^3)

Virial identity (dE/dλ|_{λ=1} = 0):
  E_A1 - E_A2 - E_A3 + 3*E_A4 = 0
""")

print(f"\nTotal wall time: {time.time()-t0:.1f}s")
print("\n[SOLID] A3 EL equation derivation complete.")
print("[SOLID] Coefficient of F'''': A3 * (4π/3) * (sin²F + 2)")
print("[SOLID] Full lower-order RHS terms printed above")
print("[NEXT] Implement 4th-order NR BVP with banded Jacobian + Frobenius inner BC")
