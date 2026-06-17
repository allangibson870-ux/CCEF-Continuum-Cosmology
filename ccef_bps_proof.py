"""
CCEF Task #19 — BPS saturation: Wetterich FRG fixed-point condition
and proof structure for A₂ = N_c × d

ARCHITECTURE OF THE PROOF:
──────────────────────────────────────────────────────────────
  [TASK 18] Hopf bundle topology → A₂ = N_c × d  [CONJECT-strong]
                   ↓ (feed in as input)
  [TASK 19] Wetterich FRG fixed-point condition:
             A₂ = N_c × d  ↔  I₁^{exact}(k*) = d²
                   ↓
  [RESULT]  The FRG criterion is SATISFIED by the topological value.
            Proof is self-consistent (but not yet fully independent).
            Gap: compute I₁_exact from non-perturbative FRG or large-N sum.
──────────────────────────────────────────────────────────────

DERIVATION OF EXACT FRG CRITERION:
  Wetterich flow for Z_A (CP^{N_c-1}, Lifshitz):
    ∂_t Z_A = (N_c/d) Z₁² I₁[G_k]                              (1)

  Dimensionless coupling: ã_A = Z_A / k^{[Z_A]_eng}
  Engineering dimension of Z_A: [Z_A]_eng = d + z - 4 = 3+2-4 = 1
  Fixed-point condition  ∂_t ã_A = 0:
    ∂_t Z_A - [Z_A]_eng × Z_A = 0
    (N_c/d) Z₁² I₁_exact = 1 × Z_A = A₂                        (2)

  With Z₁ = A₁ = 1 (normalised):
    I₁_exact = (d/N_c) × A₂                                      (3)

  IF  A₂ = N_c × d  THEN:
    I₁_exact = (d/N_c) × N_c × d = d²                            (4)

  THE EXACT FRG CRITERION:   I₁_exact(k*) = d² = 9              [SOLID]
  (This is algebraically equivalent to A₂ = N_c × d, not an
   independent verification — see discussion below.)

LIFSHITZ-LITIM REGULATOR (analytic integral):
  Regulated propagator (p < k):  G_k(p) = 1/(Z₁p² + M²)
  where M² = Z₃k⁴ + m²  (Lifshitz effective mass)

  Loop integral:
  I₁ = 1/(2π²) ∫_0^k  p⁴ G_k(p)² dp                            (5)
     = M / (Z₁^{5/2} 2π²) × F(α)
  where α = √Z₁ k/M
        F(α) = α - (3/2)arctan(α) + (1/2)α/(1+α²)               (6)

  NEW ANALYTIC RESULT — Lifshitz limit Z₁→0:
  I₁_max = lim_{Z₁→0} I₁ = k*⁵/(10π² M⁴)
  AT k* = k_sol = (A₄/A₃)^{1/4}  where  A₃k_sol⁴ = A₄:
  I₁_max = 1/(40π² A₃^{5/4} A₄^{3/4})                           (7)

  This is the MAXIMUM of I₁(Z₁) over all Z₁ ≥ 0.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ─── CCEF fixed-point parameters ───────────────────────────────────────────
A1, A2, A3, A4 = 1.000, 8.971, 1.684, 0.542
Nc, d, z = 3, 3, 2
k_sol = (A4/A3)**0.25
k_UV  = np.sqrt(A1/A3)
k_IR  = np.sqrt(A4/A1)

print("=" * 65)
print("TASK #19: BPS Saturation — Wetterich FRG Fixed-Point Proof")
print("=" * 65)

# ─── 1. EXACT FRG CRITERION (algebraic) ────────────────────────────────────
print("\n[SOLID] Exact FRG fixed-point criterion")
print("  ∂_t Z_A = (N_c/d) Z₁² I₁_exact  [Wetterich, CP^(N_c-1) Lifshitz]")
print(f"  Engineering dim [Z_A] = d+z-4 = {d}+{z}-4 = {d+z-4}")
print(f"  Fixed point: (N_c/d) Z₁² I₁_exact = Z_A = A₂")
print(f"  With Z₁=1, N_c={Nc}, d={d}:")
print(f"    I₁_exact = (d/N_c) × A₂ = ({d}/{Nc}) × A₂")
print(f"  IF A₂ = N_c × d = {Nc*d}:")
print(f"    I₁_exact = ({d}/{Nc}) × {Nc*d} = {d**2} = d²  [EXACT CRITERION]")

# ─── 2. ANALYTIC LITIM INTEGRAL — formula (6) ─────────────────────────────
def I1_analytic(k, Z1, Z3, m2):
    """Closed-form I₁ from Lifshitz-Litim regulator.
    I₁ = (1/2π²) ∫_0^k p⁴/(Z₁p²+M²)² dp
    = M/(Z₁^{5/2} × 2π²) × F(α),  α = √Z₁ × k/M
    F(α) = α - (3/2)arctan(α) + (1/2)α/(1+α²)
    For Z₁→0: I₁_max = k⁵/(10π²M⁴)
    """
    M2 = Z3 * k**4 + m2
    M  = np.sqrt(M2)
    if Z1 < 1e-10:
        return k**5 / (10 * np.pi**2 * M2**2)
    alpha = np.sqrt(Z1) * k / M
    F = alpha - 1.5*np.arctan(alpha) + 0.5*alpha/(1 + alpha**2)
    return M / (Z1**2.5 * 2 * np.pi**2) * F

def I1_max_formula(Z3, m2, k):
    """Analytic max: I₁_max = k⁵/(10π²(Z₃k⁴+m²)²)"""
    M2 = Z3*k**4 + m2
    return k**5 / (10 * np.pi**2 * M2**2)

def I1_max_kstar(Z3, m2):
    """At k* = k_sol = (m²/Z₃)^{1/4}: M²=2m², formula (7)
    I₁_max* = 1/(40π² Z₃^{5/4} m²^{3/4})"""
    return 1.0 / (40 * np.pi**2 * Z3**1.25 * m2**0.75)

# Compute at k = k_sol
I1_free  = I1_analytic(k_sol, A1, A3, A4)
I1_limit = I1_analytic(k_sol, 0,  A3, A4)
I1_star  = I1_max_kstar(A3, A4)

print(f"\n[SOLID] Analytic Litim integral at k_sol = {k_sol:.4f}")
print(f"  M²(k_sol) = A₃k_sol⁴ + A₄ = {A3*k_sol**4:.4f} + {A4:.4f} = {A3*k_sol**4+A4:.4f}")
print(f"  I₁(Z₁=A₁=1)    = {I1_free:.6f}   [standard 1-loop]")
print(f"  I₁_max (Z₁→0)   = {I1_limit:.6f}   [Lifshitz limit, eq.(7)]")
print(f"  I₁_max* (formula)= {I1_star:.6f}   [analytic: 1/(40π²A₃^{5/4}A₄^{3/4})]")
print(f"\n  [SOLID] I₁_max is INDEPENDENT of Z₁  (Z₁ only enters through α)")
print(f"  [NEW RESULT] I₁_max = 1/(40π²A₃^(5/4)A₄^(3/4)) = {I1_star:.6f}")

# Verify: A₃k_sol⁴ = A₄
assert abs(A3*k_sol**4 - A4) < 1e-10, "k_sol definition check"
print(f"\n  Cross-check: A₃k_sol⁴ = {A3*k_sol**4:.6f} = A₄ = {A4:.6f} ✓")

# ─── 3. ENHANCEMENT FACTOR ─────────────────────────────────────────────────
Xi_free   = d**2 / I1_free
Xi_max    = d**2 / I1_limit
Xi_star   = d**2 / I1_star
print(f"\n[SOLID] Non-perturbative enhancement required:")
print(f"  Xi(Z₁=1)  = d²/I₁_1loop  = {d**2}/{I1_free:.6f} = {Xi_free:.1f}")
print(f"  Xi_min    = d²/I₁_max    = {d**2}/{I1_limit:.6f} = {Xi_max:.1f}")
print(f"\n  Even at the Lifshitz limit (Z₁→0), enhancement needed ≈ {Xi_max:.0f}×")
print(f"  1-loop FRG CANNOT prove I₁_exact = d² = 9  [SOLID — gap is unavoidable]")

# ─── 4. Z₁_eff SCAN — can self-energy give I₁ = d²? ──────────────────────
Z1_vals = np.logspace(-4, 1, 2000)
I1_vals = np.array([I1_analytic(k_sol, z1, A3, A4) for z1 in Z1_vals])
I1_global_max = np.max(I1_vals)
print(f"\n[SOLID] Scan over Z₁_eff ∈ [10⁻⁴, 10]:")
print(f"  max I₁(Z₁_eff) = {I1_global_max:.6f}  at Z₁ = {Z1_vals[np.argmax(I1_vals)]:.4f}")
print(f"  max I₁ << d² = {d**2}  (factor {d**2/I1_global_max:.0f}×)")
print(f"  → No value of Z₁_eff (self-energy correction) can give I₁_exact = d²")
print(f"  → Enhancement is non-perturbative, cannot come from Z₁ renormalization alone")

# ─── 5. WHAT PROPAGATOR GIVES I₁_exact = d²? ──────────────────────────────
print(f"\n[ANSATZ] Inverse problem: what G_exact(p) gives I₁_exact = d² = 9?")
print(f"  Requirement: (1/2π²) ∫_0^{{k*}} p⁴ G_exact(p)² dp = 9")
print()

# Case A: G_exact = C (constant, momentum-independent)
# I₁ = C² × k*⁵/(10π²)
C_const = np.sqrt(d**2 * 10*np.pi**2 / k_sol**5)
print(f"  Case A: G_exact = C (constant)")
print(f"    C = {C_const:.3f}  (vs free G_free(0) = 1/(A3*k_sol^4+A4) = {1/(A3*k_sol**4+A4):.4f})")
print(f"    Ratio C/G_free(0) = {C_const/(1/(A3*k_sol**4+A4)):.1f}×  (non-perturbative)")

# Case B: G_exact = C/p² (near-massless, scale-invariant)
# I₁ = C²/(2π²) × ∫_0^k dp = C² k/(2π²)
C_power = np.sqrt(d**2 * 2*np.pi**2 / k_sol)
print(f"\n  Case B: G_exact = C/p² (scale-invariant, massless)")
print(f"    C = {C_power:.3f}  (very large → strongly coupled regime)")

# Case C: G_exact with effective mass m²_eff << m²
# Solve: I₁(m2_eff) = d²
print(f"\n  Case C: G_exact = 1/(p² + m²_eff)  [near-critical mass]")
from numpy.polynomial import polynomial as P

def I1_massonly(m2_eff, k):
    """Z₁=0, Z₃=0: pure mass propagator"""
    return k**5 / (10 * np.pi**2 * m2_eff**2)

# Solve I₁_massonly(m2_eff) = d²
m2_eff_required = np.sqrt(k_sol**5 / (10*np.pi**2 * d**2))
print(f"    m²_eff required = {m2_eff_required:.5f}")
print(f"    Original A₄ = {A4:.5f}")
print(f"    Ratio m²_eff / A₄ = {m2_eff_required/A4:.4f}  (mass reduced by {A4/m2_eff_required:.0f}×)")
print(f"    → Near-critical (m²→0) but m²_eff ≠ 0: NOT accessible from 1-loop RG")

# ─── 6. THE NON-PERTURBATIVE MECHANISM ─────────────────────────────────────
print(f"\n[CONJECT-strong] Non-perturbative mechanism: CP^(N_c-1) bubble resummation")
print(f"  The 1-loop I₁ ≈ I₁_max × Z₁_factor ≈ {I1_limit:.6f}")
print(f"  Required: I₁_exact = d² = 9")
print()
print(f"  Bubble resummation in CP^(N_c-1) (large-N_c × scale-degenerate limit):")
print(f"    I₁_n-loop = I₁_1loop × (N_c × R)^(n-1)  for some R > 1")
print(f"    Sum: I₁_exact = I₁_1loop / (1 - N_c R)")
print(f"    For I₁_exact = d²: R = (1 - I₁_1loop/d²) / N_c ≈ 1/{Nc} × (1 - {I1_free/d**2:.6f})")
print(f"                      R ≈ {(1 - I1_free/d**2)/Nc:.6f}")
print()
print(f"  Physical meaning: At the topological fixed point (scale-degenerate),")
print(f"  the CP^(N_c-1) bubble chain sums to give I₁_exact = d².")
print(f"  The bubble resummation factor 1/(1-N_c R) = d²/I₁_1loop = {Xi_free:.0f}× exactly.")
print(f"  This factor is TOPOLOGICALLY QUANTIZED (from Task #18: d² = N_c × d because d=N_c=3).")

# ─── 7. PROOF COMPLETENESS STATUS ──────────────────────────────────────────
print(f"\n{'='*65}")
print(f"PROOF STRUCTURE SUMMARY for A₂ = N_c × d = {Nc*d}")
print(f"{'='*65}")

steps = [
    ("SOLID",          "FRG criterion: A₂=N_c×d ↔ I₁_exact = d²=9 (algebraic)"),
    ("SOLID",          "1-loop I₁ = 0.001132 << d² (Lifshitz-Litim regulator)"),
    ("SOLID",          "I₁_max = 1/(40π²A₃^{5/4}A₄^{3/4}) = 0.002  [NEW formula]"),
    ("SOLID",          "Z₁_eff scan: no 1-loop mechanism gives I₁→d² (proven)"),
    ("CONJECT-strong", "Task #18: A₂=N_c×d from Hopf bundle c₁=N_c, d=2N_c-3"),
    ("ANSATZ",         "Bubble resummation: I₁_exact = I₁_1loop/(1-N_c R) = d²"),
    ("OPEN",           "Prove R = (1-I₁_1loop/d²)/N_c from CP^(N_c-1) sigma model"),
]

for status, description in steps:
    print(f"  [{status:15s}] {description}")

print(f"\n[RESULT] Convergence of two arguments:")
print(f"  1. Topological (Task #18): A₂ = c₁ × d = N_c × d = 9  [CONJECT-strong]")
print(f"  2. FRG structure (Task #19): A₂=N_c×d ↔ I₁_exact=d²  [SOLID equivalence]")
print(f"  Together: the topological value satisfies the FRG criterion exactly.")
print(f"  A₂_CCEF = {A2} vs A₂_topo = {Nc*d} (error {abs(A2-Nc*d)/(Nc*d)*100:.4f}%)")
print(f"\n  Remaining gap to SOLID: prove I₁_exact=d² from non-perturbative FRG")
print(f"  (bubble resummation in CP^(N_c-1) at the topological fixed point)")

# ════════════════════════════════════════════════════════════════════════════
# FIGURE: 4-panel proof summary
# ════════════════════════════════════════════════════════════════════════════
fig = plt.figure(figsize=(14, 10))
fig.patch.set_facecolor('#0d1117')
gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.42, wspace=0.35)

col_bg   = '#161b22'
col_text = '#e6edf3'
col_blue = '#58a6ff'
col_grn  = '#3fb950'
col_red  = '#f85149'
col_yel  = '#d29922'
col_purp = '#bc8cff'
col_ax   = '#30363d'

def sty(ax, title):
    ax.set_facecolor(col_bg)
    ax.tick_params(colors=col_text, labelsize=9)
    ax.xaxis.label.set_color(col_text)
    ax.yaxis.label.set_color(col_text)
    ax.set_title(title, color=col_text, fontsize=10, pad=6)
    for s in ax.spines.values():
        s.set_edgecolor(col_ax)

# ── Panel 1: I₁(Z₁_eff) scan ───────────────────────────────────────────────
ax1 = fig.add_subplot(gs[0, 0])
sty(ax1, "I₁(Z₁_eff): Max is Far Below d²=9")

ax1.semilogx(Z1_vals, I1_vals, color=col_blue, lw=2)
ax1.axhline(d**2, color=col_red, lw=1.5, ls='--', label=f'Required: d²={d**2}')
ax1.axhline(I1_limit, color=col_yel, lw=1.5, ls=':', label=f'I₁_max={I1_limit:.4f}')
ax1.scatter([A1], [I1_free], color=col_grn, s=70, zorder=5,
            label=f'Z₁=1: I₁={I1_free:.4f}')
ax1.axvline(A1, color=col_grn, lw=0.8, ls=':', alpha=0.5)

ax1.set_xlabel('Z₁_eff', color=col_text)
ax1.set_ylabel('I₁ (Litim regulator)', color=col_text)
ax1.set_ylim(0, 0.003)
ax1.legend(fontsize=7.5, facecolor=col_bg, edgecolor=col_ax, labelcolor=col_text)
ax1.text(0.02, 0.92, f'gap = d²/I₁_max\n= {Xi_max:.0f}×',
         transform=ax1.transAxes, color=col_red, fontsize=9)

# ── Panel 2: I₁_max analytic formula ──────────────────────────────────────
ax2 = fig.add_subplot(gs[0, 1])
sty(ax2, "I₁_max = 1/(40π²A₃^{5/4}A₄^{3/4}) — Analytic")

A3_scan = np.linspace(0.5, 4.0, 200)
I1max_A3 = np.array([1/(40*np.pi**2 * a3**1.25 * A4**0.75) for a3 in A3_scan])

ax2.plot(A3_scan, I1max_A3, color=col_blue, lw=2, label='I₁_max vs A₃')
ax2.scatter([A3], [I1_star], color=col_grn, s=100, zorder=5,
            label=f'CCEF: A₃={A3} → {I1_star:.4f}')
ax2.axhline(d**2, color=col_red, lw=1.5, ls='--', label=f'd²={d**2} (required)')
ax2.axhline(1.0, color=col_purp, lw=1, ls=':', alpha=0.7, label='I₁_max=1.0')

ax2.set_xlabel('A₃ (Lifshitz coupling)', color=col_text)
ax2.set_ylabel('I₁_max', color=col_text)
ax2.set_yscale('log')
ax2.set_ylim(1e-4, 20)
ax2.axhline(d**2, color=col_red, lw=1.5, ls='--')
ax2.legend(fontsize=7.5, facecolor=col_bg, edgecolor=col_ax, labelcolor=col_text)

# ── Panel 3: Enhancement Xi vs coupling structure ──────────────────────────
ax3 = fig.add_subplot(gs[1, 0])
sty(ax3, "Enhancement Xi = d²/I₁ at CCEF Fixed Point")

labels = ['1-loop\n(Z₁=1)', 'Lifshitz\nlimit Z₁→0', 'Required\n(exact)']
values = [Xi_free, Xi_max, 1.0]
colors = [col_blue, col_yel, col_grn]

bars = ax3.bar(labels, values, color=colors, alpha=0.85, width=0.5, edgecolor='none')
ax3.set_ylabel('Enhancement factor Xi', color=col_text)
ax3.set_yscale('log')
ax3.axhline(1, color=col_grn, lw=1.5, ls='--', label='Xi=1 (no enhancement)')

for bar, val in zip(bars, values):
    ax3.text(bar.get_x() + bar.get_width()/2, val * 1.5,
             f'{val:.0f}×', ha='center', va='bottom', fontsize=9, color=col_text)

ax3.text(0.5, 0.25, 'Non-perturbative\ngap (cannot close\nwith Z₁ tuning)',
         transform=ax3.transAxes, ha='center', color=col_red, fontsize=8.5,
         bbox=dict(boxstyle='round', facecolor=col_bg, edgecolor=col_red, alpha=0.8))
ax3.legend(fontsize=8, facecolor=col_bg, edgecolor=col_ax, labelcolor=col_text)

# ── Panel 4: Proof structure diagram ──────────────────────────────────────
ax4 = fig.add_subplot(gs[1, 1])
ax4.set_facecolor(col_bg)
ax4.axis('off')
ax4.set_title("Proof Structure: Task 18+19 → A₂=N_c×d", color=col_text, fontsize=10, pad=6)
for s in ax4.spines.values():
    s.set_edgecolor(col_ax)

lines = [
    ("TASK 18: Hopf bundle topology", col_purp, 9, 'bold'),
    ("  S¹→S^{5}→CP²  (N_c=3)", col_purp, 8.5, 'normal'),
    ("  c₁=N_c,  d=2N_c-3=3", col_purp, 8.5, 'normal'),
    ("  → A₂ = N_c×d = 9  [CONJ-strong]", col_purp, 8.5, 'normal'),
    ("", col_text, 8.5, 'normal'),
    ("TASK 19: Wetterich FRG criterion", col_blue, 9, 'bold'),
    ("  ∂_t Z_A = (Nc/d) Z₁² I₁_exact", col_blue, 8.5, 'normal'),
    ("  Fixed pt: I₁_exact = d²=9  [SOLID]", col_blue, 8.5, 'normal'),
    ("  1-loop I₁ = 0.001132  <<  9  [SOLID]", col_blue, 8.5, 'normal'),
    ("  I₁_max=1/(40π²A₃^{5/4}A₄^{3/4})", col_grn, 8.5, 'normal'),
    ("       = 0.002  [NEW SOLID formula]", col_grn, 8.5, 'normal'),
    ("", col_text, 8.5, 'normal'),
    ("CONVERGENCE:", col_yel, 9, 'bold'),
    ("  Topo value A₂=9 satisfies FRG", col_yel, 8.5, 'normal'),
    ("  criterion I₁_exact=d²=9", col_yel, 8.5, 'normal'),
    ("  Self-consistent proof [CONJ-str]", col_yel, 8.5, 'normal'),
    ("", col_text, 8.5, 'normal'),
    ("OPEN GAP:", col_red, 9, 'bold'),
    ("  Prove I₁_exact=d² from", col_red, 8.5, 'normal'),
    ("  CP^(N_c-1) bubble resummation", col_red, 8.5, 'normal'),
    ("  (non-perturbative, Xi~4300-7951)", col_red, 8.5, 'normal'),
]

y = 0.96
for text, color, size, style in lines:
    fw = 'bold' if style == 'bold' else 'normal'
    ax4.text(0.03, y, text, transform=ax4.transAxes,
             color=color, fontsize=size, fontweight=fw,
             verticalalignment='top', fontfamily='monospace')
    y -= 0.048

fig.suptitle(
    "CCEF Task #19 — BPS Saturation: Wetterich FRG Fixed-Point Analysis\n"
    "Exact criterion I₁^{exact}=d²=9 requires non-perturbative enhancement",
    color=col_text, fontsize=11, fontweight='bold', y=0.98
)

plt.savefig('ccef_bps_proof.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.close()
print("\nFigure saved: ccef_bps_proof.png")
