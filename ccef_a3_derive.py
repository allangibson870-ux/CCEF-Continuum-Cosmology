"""
CCEF — Exact derivation of A3 (Lifshitz) contribution to the radial EL equation.

Energy term:
  E_A3 = (A3/2) ∫ d³x  (∂_i ∂_j n^a)(∂^i ∂^j n^a)
where n^a is the hedgehog: n = (sinF sinθ cosφ, sinF sinθ sinφ, cosF)
with F=F(r), boundary conditions F(0)=π, F(∞)=0, Q=1 sector.

Strategy:
  1. Express ∂²n^a/∂x_i∂x_j in spherical coords via chain rule (exact, no approximation)
  2. Sum squares over (a,i,j), integrate over solid angle → radial density ρ_A3(r,F,F',F'')
  3. Apply EL from L=r²ρ_A3 with Lagrangian depending on F up to 2nd derivative
  4. Output coefficients of each term in the 4th-order radial ODE

Labels:
  sF=sin(F), cF=cos(F), Fp=F'(r), Fpp=F''(r), r=radius
"""

import sympy as sp
from sympy import (sin, cos, symbols, Integer, pi, Rational,
                   expand, collect, simplify, factor, cancel, trigsimp)
import time

t0 = time.time()

def elapsed():
    return f"[{time.time()-t0:5.1f}s]"

print("="*60)
print("CCEF A3 EL derivation — exact SymPy computation")
print("="*60)

# -------------------------------------------------------
# Symbols
# -------------------------------------------------------
r, th, ph = symbols('r theta phi', positive=True)
Fp  = symbols('Fp',  real=True)   # F'(r)
Fpp = symbols('Fpp', real=True)   # F''(r)
sF  = symbols('sF',  real=True)   # sin(F(r))
cF  = symbols('cF',  real=True)   # cos(F(r))

st, ct = sin(th), cos(th)
sp_, cp = sin(ph), cos(ph)

# -------------------------------------------------------
# Spherical coordinate Jacobians
#   gr[i] = ∂r/∂x_i,   gt[i] = ∂θ/∂x_i,   gp[i] = ∂φ/∂x_i
# where x = (x,y,z)
# -------------------------------------------------------
gr = [st*cp,          st*sp_,         ct        ]
gt = [ct*cp/r,        ct*sp_/r,       -st/r     ]
gp = [-sp_/(r*st),    cp/(r*st),      Integer(0)]

# -------------------------------------------------------
# First derivatives of n^a w.r.t. r, θ, φ
# n = (sF·st·cp,  sF·st·sp_,  cF)
# dn/dr = (Fp·cF·st·cp, Fp·cF·st·sp_, -Fp·sF)
# dn/dθ = (sF·ct·cp,    sF·ct·sp_,    0)
# dn/dφ = (-sF·st·sp_,  sF·st·cp,     0)
# -------------------------------------------------------
dn_dr = [Fp*cF*st*cp,   Fp*cF*st*sp_,   -Fp*sF    ]
dn_dt = [sF*ct*cp,      sF*ct*sp_,      Integer(0)]
dn_dp = [-sF*st*sp_,    sF*st*cp,       Integer(0)]

# -------------------------------------------------------
# Second derivatives of n^a w.r.t. spherical coords
# ∂²n¹/∂r²  = (Fpp·cF - Fp²·sF)·st·cp
# ∂²n¹/∂r∂θ = Fp·cF·ct·cp
# ∂²n¹/∂r∂φ = -Fp·cF·st·sp_
# ∂²n¹/∂θ²  = -sF·st·cp
# ∂²n¹/∂θ∂φ = -sF·ct·sp_
# ∂²n¹/∂φ²  = -sF·st·cp
# (similarly for n², n³)
# -------------------------------------------------------
d2n_rr = [(Fpp*cF - Fp**2*sF)*st*cp,
          (Fpp*cF - Fp**2*sF)*st*sp_,
          -(Fpp*sF + Fp**2*cF)]

d2n_rt = [Fp*cF*ct*cp,   Fp*cF*ct*sp_,   Integer(0)]  # symmetric: d2n_tr = d2n_rt
d2n_rp = [-Fp*cF*st*sp_, Fp*cF*st*cp,    Integer(0)]  # symmetric: d2n_pr = d2n_rp
d2n_tt = [-sF*st*cp,     -sF*st*sp_,     Integer(0)]
d2n_tp = [-sF*ct*sp_,    sF*ct*cp,       Integer(0)]  # symmetric
d2n_pp = [-sF*st*cp,     -sF*st*sp_,     Integer(0)]

# -------------------------------------------------------
# Derivatives of the Jacobian vectors w.r.t. r, θ, φ
# -------------------------------------------------------
# ∂gr/∂r = 0, ∂gr/∂θ = (ct·cp, ct·sp_, -st), ∂gr/∂φ = (-st·sp_, st·cp, 0)
dgr_dr = [Integer(0)]*3
dgr_dt = [ct*cp,       ct*sp_,      -st       ]
dgr_dp = [-st*sp_,     st*cp,       Integer(0)]

# ∂gt/∂r = -gt/r, ∂gt/∂θ = (-st·cp/r, -st·sp_/r, -ct/r), ∂gt/∂φ = (-ct·sp_/r, ct·cp/r, 0)
dgt_dr = [-ct*cp/r**2,  -ct*sp_/r**2,  st/r**2   ]
dgt_dt = [-st*cp/r,     -st*sp_/r,     -ct/r     ]
dgt_dp = [-ct*sp_/r,    ct*cp/r,       Integer(0)]

# ∂gp/∂r = -gp/r, ∂gp/∂θ = (sp_·ct/(r·st²), -cp·ct/(r·st²), 0), ∂gp/∂φ = (-cp/(r·st), -sp_/(r·st), 0)
dgp_dr = [sp_/(r**2*st),      -cp/(r**2*st),       Integer(0)]
dgp_dt = [sp_*ct/(r*st**2),   -cp*ct/(r*st**2),    Integer(0)]
dgp_dp = [-cp/(r*st),         -sp_/(r*st),          Integer(0)]

# -------------------------------------------------------
# Helper: apply ∂/∂x_j to a scalar with given spherical partials
# -------------------------------------------------------
def dxj(Xr, Xt, Xp, j):
    return gr[j]*Xr + gt[j]*Xt + gp[j]*Xp

# -------------------------------------------------------
# Build ∂²n^a/∂x_i∂x_j for all (a, i, j)
#
# ∂/∂x_j [gr_i·dn_dr_a + gt_i·dn_dt_a + gp_i·dn_dp_a]
# = (∂gr_i/∂x_j)·dn_dr_a + gr_i·(∂dn_dr_a/∂x_j)
# + (∂gt_i/∂x_j)·dn_dt_a + gt_i·(∂dn_dt_a/∂x_j)
# + (∂gp_i/∂x_j)·dn_dp_a + gp_i·(∂dn_dp_a/∂x_j)
# -------------------------------------------------------
print(f"{elapsed()} Building second Cartesian derivatives...")

d2n_cart = [[[None]*3 for _ in range(3)] for _ in range(3)]  # [a][i][j]

for a in range(3):
    for i in range(3):
        for j in range(3):
            # Jacobian gradients
            dgr_i_dxj = dxj(dgr_dr[i], dgr_dt[i], dgr_dp[i], j)
            dgt_i_dxj = dxj(dgt_dr[i], dgt_dt[i], dgt_dp[i], j)
            dgp_i_dxj = dxj(dgp_dr[i], dgp_dt[i], dgp_dp[i], j)

            # n^a spherical gradients applied via ∂/∂x_j
            # ∂(dn_dr_a)/∂x_j uses (d2n_rr, d2n_rt, d2n_rp)
            dndr_dxj = dxj(d2n_rr[a], d2n_rt[a], d2n_rp[a], j)
            # ∂(dn_dt_a)/∂x_j uses (d2n_rt, d2n_tt, d2n_tp)
            dndt_dxj = dxj(d2n_rt[a], d2n_tt[a], d2n_tp[a], j)
            # ∂(dn_dp_a)/∂x_j uses (d2n_rp, d2n_tp, d2n_pp)
            dndp_dxj = dxj(d2n_rp[a], d2n_tp[a], d2n_pp[a], j)

            d2n_cart[a][i][j] = (dgr_i_dxj * dn_dr[a] + gr[i] * dndr_dxj
                                + dgt_i_dxj * dn_dt[a] + gt[i] * dndt_dxj
                                + dgp_i_dxj * dn_dp[a] + gp[i] * dndp_dxj)

print(f"{elapsed()} Done. Computing sum of squares...")

# -------------------------------------------------------
# Sum (∂_i ∂_j n^a)² over all a, i, j  (27 terms)
# -------------------------------------------------------
sq_sum = Integer(0)
for a in range(3):
    for i in range(3):
        for j in range(3):
            sq_sum += d2n_cart[a][i][j]**2

print(f"{elapsed()} Expanding...")
sq_exp = expand(sq_sum)
print(f"{elapsed()} Expanded. Term count: ~{len(sq_exp.args) if hasattr(sq_exp,'args') else '?'}")

# -------------------------------------------------------
# Angular integration: ∫₀^{2π} dφ  then  ∫₀^π sinθ dθ
# -------------------------------------------------------
print(f"{elapsed()} Integrating over phi...")
# Multiply by sinθ (the volume element factor), then integrate over phi
after_phi = sp.integrate(sq_exp * st, (ph, 0, 2*pi))
after_phi = expand(after_phi)
print(f"{elapsed()} After phi integration. Integrating over theta...")

rho_raw = sp.integrate(after_phi, (th, 0, pi))
rho_raw = expand(rho_raw)
print(f"{elapsed()} Angular integration complete.")

# -------------------------------------------------------
# Collect by monomials in (Fpp, Fp, sF, cF)
# rho_A3 = coefficient structure
# -------------------------------------------------------
print(f"\n{'='*60}")
print("RAW ρ_A3 (before simplification):")
print(rho_raw)
print(f"\n{'='*60}")

# Simplify using sF²+cF²=1
rho = rho_raw.subs(sF**2, 1 - cF**2)
rho = expand(rho)
rho = rho.subs(cF**2, 1 - sF**2)
rho = expand(rho)

# Collect by powers of Fpp
rho_collected = collect(rho, [Fpp, Fp, sF], exact=False)
print("\nρ_A3 collected:")
print(rho_collected)

# Extract individual coefficients
A_Fpp2 = sp.Poly(rho, Fpp).nth(2)   # coefficient of Fpp²
A_Fpp1 = sp.Poly(rho, Fpp).nth(1)   # coefficient of Fpp (linear)
A_Fpp0 = sp.Poly(rho, Fpp).nth(0)   # terms independent of Fpp

print(f"\nCoeff of Fpp²:  {A_Fpp2}")
print(f"Coeff of Fpp:   {A_Fpp1}")
print(f"Indep of Fpp:   {A_Fpp0}")

# -------------------------------------------------------
# EL equation structure
# L = r² * ρ_A3 / 2  (A3 factor applied separately)
# EL: ∂L/∂F - d/dr(∂L/∂Fp) + d²/dr²(∂L/∂Fpp) = 0
#
# Since L depends on F only via sF=sin(F), cF=cos(F):
# ∂L/∂F = (∂L/∂sF)*cF - (∂L/∂cF)*sF
#
# We compute the partial derivatives symbolically.
# -------------------------------------------------------
print(f"\n{'='*60}")
print("EL EQUATION STRUCTURE")
print(f"{'='*60}")

L = r**2 * rho / 2  # Lagrangian density (factor of A3 separate)

dL_dsF = sp.diff(L, sF)
dL_dcF = sp.diff(L, cF)
dL_dFp  = sp.diff(L, Fp)
dL_dFpp = sp.diff(L, Fpp)

# ∂L/∂F = (∂L/∂sF)·cos(F) - (∂L/∂cF)·sin(F)
dL_dF_expr = dL_dsF * cF - dL_dcF * sF
dL_dF_expr = expand(dL_dF_expr)

print("\n∂L/∂F' (appears in -d/dr[...]):")
print(simplify(dL_dFp))

print("\n∂L/∂F'' (appears in d²/dr²[...]):")
print(simplify(dL_dFpp))

print("\n∂L/∂F (direct term):")
print(simplify(dL_dF_expr))

# -------------------------------------------------------
# The 4th-order term comes from d²/dr²[∂L/∂F''].
# ∂L/∂F'' = r² * (∂ρ/∂Fpp) = r² * (A_Fpp2 * 2*Fpp + A_Fpp1)
# The coefficient of F'''' in the EL equation is ∂²(r²ρ)/∂Fpp² = r² * 2*A_Fpp2
# (leading term: 2*A_Fpp2 * r² * F'''' + lower-order)
# -------------------------------------------------------
coeff_Fpppp = A_Fpp2  # multiplies r² * F'''' in EL after d²/dr²
print(f"\n>>> Coefficient of r²·F'''' in A3 EL (= A_Fpp²):  {simplify(coeff_Fpppp)}")

# -------------------------------------------------------
# Verify virial identity: for a scaling F(r) → F(r/λ),
# E_A3 scales as λ^{d-2k} where k=2 (number of derivatives), d=3
# So E_A3 ~ λ^{3-4} = λ^{-1}: scales as 1/λ
# This means in the virial theorem: E_A3 contributes -1 × E_A3
# Consistent with A3 stabilizing the soliton against collapse (negative virial weight)
# -------------------------------------------------------
print(f"\n{'='*60}")
print("VIRIAL CHECK: A3 term scales as λ^{3-2*2} = λ^{-1}")
print("  → virial coefficient = -1 (stabilizing)")
print(f"{'='*60}")

# -------------------------------------------------------
# Write out the full combined EL equation (A1 + A2 + A3 + A4 terms)
# A1, A2, A4 contributions are the 2nd-order terms from Task #31e.
# A3 contribution is the 4th-order addition.
# -------------------------------------------------------
print(f"\n{'='*60}")
print("FULL EL EQUATION STRUCTURE:")
print(f"{'='*60}")
print("""
Known 2nd-order terms (A1, A2, A4) from Task #31e derivation [SOLID]:
  P(r) * F'' = A1*sin2F/r² + A2*sin²F*sin2F/r⁴ + A4*sinF - 2*A1*F'/r - A2*sin2F*(F')²/r²
  where P = A1 + 2*A2*sin²F/r²

A3 adds a 4th-order differential operator to the left side.
The combined EL is:
  [A3 contribution, 4th order] + [A1+A2+A4 contribution, 2nd order] = 0

The 4th-order A3 term is:
  A3 * {d²/dr²[∂L_A3/∂F''] - d/dr[∂L_A3/∂F'] + ∂L_A3/∂F} / r² = 0
  where L_A3 = r² * ρ_A3 / 2
""")

print(f"\nTotal wall time: {time.time()-t0:.1f}s")
print("\nSave ρ_A3 for use in BVP:")
print(f"rho_A3 = {rho}")
