"""
CCEF Task #31d — 4th-order BVP Soliton ODE with A3
====================================================
Hedgehog ansatz:  n = (sinF sinθ cosφ, sinF sinθ sinφ, cosF)
BC:  F(0)=π,  F(∞)=0

CCEF static energy (dimensionless, E in E0, r in L0):
  E[F] = 4π ∫ r² { A1·e1 + A2·e2 + A3·e3 + A4·e4 } dr
  e1 = (F')²+2sin²F/r²    [O(∂²) sigma]
  e2 = sin²F(F')²/r²      [O(∂⁴) Skyrme]
  e3 = (2/3)A²+B²         [O(∂⁴) Lifshitz]
  e4 = sin²F              [mass]
  A = F″cosF−(F')²sinF+2F'cosF/r−2sinF/r²
  B = −(F″+2F'/r)sinF−(F')²cosF

Method: Atiyah-Manton variational scan + perturbative A3 correction.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

hbar_c=197.3269804; L0=0.633007; E0=hbar_c/L0
A1=1.000; A2=8.971042; A3=1.684; A4=0.542
e_hop=np.sqrt(6*A2); R_scl=2*A4+A1*np.sqrt(A4/A3)
M_N_ANW=36.5*E0/(e_hop*R_scl)

print("="*65)
print("CCEF Task #31d  Hedgehog Soliton BVP with A3 Lifshitz")
print("="*65)
print(f"  E0={E0:.3f} MeV  L0={L0:.6f} fm")
print(f"  A1={A1}  A2={A2:.4f}  A3={A3}  A4={A4}")
print(f"  e=√(6A2)={e_hop:.4f}  R={R_scl:.4f}")
print(f"  M_N(ANW)=36.5 E0/(eR)={M_N_ANW:.3f} MeV={M_N_ANW/E0:.4f} E0")

# ------------------------------------------------------------------
print("\n--- SECTION 1  EL ODE structure ---")
print("""
2nd-order Skyrme ODE (no A3):
  (A1r²+A2sin²F)F″ = 2A1sinFcosF − A2sinFcosF(F')²
                   + A4r²sinFcosF − 2A1rF'

A3 Lifshitz adds 4th-order term (∂A/∂F″=cosF, ∂B/∂F″=−sinF):
  A3[(4/3)cos²F+2sin²F]F⁽⁴⁾ + lower order = 0

4 BCs: F(0)=π, F'(0)=a [shoot], F(∞)=0, F'(∞)=0

Shooting failure: profile traps at F≈π/2 for all a∈[0.5,30]
  because sinFcosF→0 kills all EL restoring force there.
  Full Newton-Raphson BVP needed → Task #31e.
""")

# ------------------------------------------------------------------
print("--- SECTION 2  AM variational scan ---")
r=np.linspace(1e-6,100,200000)

def comps(alpha, with_A3=True):
    F=np.pi*(1-r/np.sqrt(r**2+alpha**2))
    Fp=-np.pi*alpha**2/(r**2+alpha**2)**1.5
    s=np.sin(F); c=np.cos(F); s2=s*s
    E1=4*np.pi*np.trapz(r**2*A1*(Fp**2+2*s2/r**2),r)
    E2=4*np.pi*np.trapz(r**2*A2*s2*Fp**2/r**2,r)
    E4=4*np.pi*np.trapz(r**2*A4*s2,r)
    if with_A3:
        Fpp=np.gradient(Fp,r)
        Av=Fpp*c-Fp**2*s+2*Fp*c/r-2*s/r**2
        Bv=-(Fpp+2*Fp/r)*s-Fp**2*c
        E3=4*np.pi*np.trapz(r**2*A3*((2/3)*Av**2+Bv**2),r)
    else:
        E3=0.
    return E1,E2,E3,E4,F,Fp

alphas=np.logspace(-1,1,300)
E_tot=np.zeros(len(alphas))
E1a=np.zeros_like(E_tot); E2a=np.zeros_like(E_tot); E4a=np.zeros_like(E_tot)
for i,a in enumerate(alphas):
    E1,E2,_,E4,_,_=comps(a,False)
    E_tot[i]=E1+E2+E4; E1a[i]=E1; E2a[i]=E2; E4a[i]=E4

idx=np.argmin(E_tot); aopt=alphas[idx]; Emin=E_tot[idx]
E1o,E2o,_,E4o,Fo,Fpo=comps(aopt,False)
print(f"  α_opt={aopt:.4f} L0={aopt*L0:.4f} fm")
print(f"  E_min(noA3)={Emin:.4f} E0={Emin*E0:.1f} MeV")
print(f"  E1={E1o:.4f}  E2={E2o:.4f}  E4={E4o:.4f}")
print(f"  Virial: E1+3E4={E1o+3*E4o:.4f} vs E2={E2o:.4f} (ratio={(E1o+3*E4o)/E2o:.4f})")

# ------------------------------------------------------------------
print("\n--- SECTION 3  A3 perturbative correction ---")
_,_,E3o,_,_,_=comps(aopt,True)
print(f"  δM_N^(1)=A3 E3[F_opt]={E3o:.4f} E0={E3o*E0:.2f} MeV")
print(f"  E_tot(A3 pert)={Emin+E3o:.4f} E0={( Emin+E3o)*E0:.1f} MeV")

# ------------------------------------------------------------------
k_star=np.sqrt(A1/(2*A3)); r_star=1/k_star
idx_half=np.argmin(np.abs(Fo-np.pi/2))
r_half=r[idx_half]
ratio=Emin/(M_N_ANW/E0)
print(f"\n--- SECTION 4  Scales and normalisation ---")
print(f"  k*=√(A1/2A3)={k_star:.4f} L0⁻¹  r*={r_star:.4f} L0={r_star*L0:.4f} fm")
print(f"  r_half(F=π/2)={r_half:.4f} L0={r_half*L0:.4f} fm")
print(f"  M_N(ANW)={M_N_ANW/E0:.4f} E0")
print(f"  E_var_min={Emin:.4f} E0")
print(f"  Ratio E_var/M_ANW={ratio:.2f}  (normalisation question → Task #31e)")

# ------------------------------------------------------------------
DARK='#0d1117'; PBG='#161b22'; G='#f0c040'; C='#58d6f0'
Gr='#3fb950'; R='#f85149'; Bl='#79c0ff'; Pu='#d2a8ff'; Or='#ffa657'; W='#e6edf3'
fig=plt.figure(figsize=(18,12))
gs_=gridspec.GridSpec(2,3,figure=fig,hspace=0.44,wspace=0.36)
fig.patch.set_facecolor(DARK)
def axp(pos,ttl):
    a=fig.add_subplot(pos); a.set_facecolor(PBG)
    for s in a.spines.values(): s.set_edgecolor(G); s.set_linewidth(1.1)
    a.set_title(ttl,color=G,fontsize=10,fontweight='bold',pad=5)
    a.tick_params(colors=W,labelsize=8); return a

r_fm=r*L0

ax1=axp(gs_[0,0],'Variational Energy E(α) — log-log')
ax1.loglog(alphas*L0,E_tot,'-',color=Gr,lw=2.5,label='E_total')
ax1.loglog(alphas*L0,E1a,'--',color=Bl,lw=1.5,label='A1·E1 (∝α)')
ax1.loglog(alphas*L0,E2a,'--',color=C,lw=1.5,label='A2·E2 (∝1/α)')
ax1.loglog(alphas*L0,E4a,'--',color=Pu,lw=1.5,label='A4·E4 (∝α³)')
ax1.axvline(aopt*L0,color=Or,ls='--',lw=2,label=f'α_opt={aopt*L0:.3f} fm')
ax1.set_xlabel('α (fm)',color=W,fontsize=9); ax1.set_ylabel('E (E₀)',color=W,fontsize=9)
ax1.legend(fontsize=7.5,facecolor=PBG,edgecolor=G,labelcolor=W)
ax1.text(0.04,0.06,f'E_min={Emin:.1f} E₀',transform=ax1.transAxes,color=Or,fontsize=9)

ax2=axp(gs_[0,1],f'AM Profile  α_opt={aopt:.3f} L₀={aopt*L0:.3f} fm')
ax2.plot(r_fm[:20000],Fo[:20000]/np.pi,'-',color=Gr,lw=2.5,label='F(r)/π')
ax2.axhline(0.5,color=W,ls=':',lw=0.8)
ax2.axvline(r_half*L0,color=Or,ls='--',lw=1.5,label=f'r½={r_half:.3f} L₀')
ax2.axvline(r_star*L0,color=Pu,ls='--',lw=1.5,label=f'r*={r_star:.3f} L₀')
ax2.set_xlabel('r (fm)',color=W,fontsize=9); ax2.set_ylabel('F/π',color=W,fontsize=9)
ax2.set_xlim(0,4); ax2.set_ylim(-0.05,1.05)
ax2.legend(fontsize=8,facecolor=PBG,edgecolor=G,labelcolor=W)

ax3=axp(gs_[0,2],'Radial Energy Density 4πr²ε at α_opt')
wg=4*np.pi*r**2
d1=wg*A1*(Fpo**2+2*np.sin(Fo)**2/r**2)
d2=wg*A2*np.sin(Fo)**2*Fpo**2/r**2
d4=wg*A4*np.sin(Fo)**2
ax3.plot(r_fm[:20000],(d1+d2+d4)[:20000],color=Gr,lw=2.5,label=f'Total={Emin:.1f}')
ax3.plot(r_fm[:20000],d1[:20000],'--',color=Bl,lw=1.5,label=f'A1·e1={E1o:.1f}')
ax3.plot(r_fm[:20000],d2[:20000],'--',color=C,lw=1.5,label=f'A2·e2={E2o:.1f}')
ax3.plot(r_fm[:20000],d4[:20000],'--',color=Pu,lw=1.5,label=f'A4·e4={E4o:.1f}')
ax3.set_xlabel('r (fm)',color=W,fontsize=9); ax3.set_ylabel('4πr²ε',color=W,fontsize=9)
ax3.legend(fontsize=7.5,facecolor=PBG,edgecolor=G,labelcolor=W)
ax3.set_xlim(0,4); ax3.set_ylim(bottom=0)

ax4=axp(gs_[1,0],'EL ODE Structure (2nd+4th order)')
ax4.axis('off'); ax4.set_xlim(0,1); ax4.set_ylim(0,1)
txts=[
  ('2nd-order Skyrme ODE (A3=0):', G,9.5),
  ('  (A1r²+A2sin²F)F″ = 2A1sinFcosF',W,8.5),
  ('    −A2sinFcosF(F\')²+A4r²sinFcosF−2A1rF\'',W,8.5),
  ('',W,7),
  ('4th-order A3 contribution:',G,9.5),
  ('  ∂A/∂F″=cosF,  ∂B/∂F″=−sinF',W,8.5),
  ('  A3[(4/3)cos²F+2sin²F]F⁽⁴⁾+…=0',W,8.5),
  ('',W,7),
  ('BCs: F(0)=π, F\'(0)=a, F(∞)=F\'(∞)=0',G,9.5),
  ('',W,7),
  ('Shooting failure:',G,9.5),
  ('  sinFcosF=0 at F=π/2 kills restoring force',R,8.5),
  ('  → profile trapped at F≈π/2 for all a',R,8.5),
  ('  → Newton-Raphson on full EL ODE needed',Or,8.5),
  ('     (Task #31e)',Or,8.5),
  ('',W,7),
  ('Lifshitz preferred scale:',G,9.5),
  (f'  k*=√(A1/2A3)={k_star:.3f} L0⁻¹',C,8.5),
  (f'  r*=1/k*={r_star:.3f} L0={r_star*L0:.3f} fm',C,8.5),
]
yy=0.98
for txt,col,fs in txts:
    ax4.text(0.02,yy,txt,transform=ax4.transAxes,color=col,fontsize=fs,va='top',fontfamily='monospace')
    yy-=0.047

Fppo=np.gradient(Fpo,r)
cFo=np.cos(Fo); sFo=np.sin(Fo)
Av=Fppo*cFo-Fpo**2*sFo+2*Fpo*cFo/r-2*sFo/r**2
Bv=-(Fppo+2*Fpo/r)*sFo-Fpo**2*cFo
e3_a=(2/3)*Av**2+Bv**2

ax5=axp(gs_[1,1],'Lifshitz Density e₃(r)  [perturbative A3]')
d3=4*np.pi*r**2*A3*e3_a
ax5.plot(r_fm[:20000],d3[:20000],color=Or,lw=2.2,label=f'A3·e3: E3={E3o:.3f} E₀')
ax5.plot(r_fm[:20000],4*np.pi*r[:20000]**2*np.abs(Av[:20000]),'--',color=Bl,lw=1.3,label='4πr²|A(r)|')
ax5.plot(r_fm[:20000],4*np.pi*r[:20000]**2*np.abs(Bv[:20000]),'--',color=Pu,lw=1.3,label='4πr²|B(r)|')
ax5.axvline(r_star*L0,color=Or,ls=':',lw=1.2,alpha=0.7,label='r*')
ax5.set_xlabel('r (fm)',color=W,fontsize=9); ax5.set_ylabel('density',color=W,fontsize=9)
ax5.legend(fontsize=8,facecolor=PBG,edgecolor=G,labelcolor=W)
ax5.set_xlim(0,4); ax5.set_ylim(bottom=0)

ax6=axp(gs_[1,2],'Mass / Energy Summary')
lbls=['M_N(ANW)\nformula','E_var\nnoA3','E_var\n+δA3','M_N\nexp']
vals=[M_N_ANW/E0,Emin,Emin+E3o,938.9/E0]
cols=[Bl,Gr,Or,R]
bars=ax6.bar(lbls,vals,color=cols,edgecolor=G,lw=1.2,width=0.5)
ax6.set_ylabel('E (E₀)',color=W,fontsize=9); ax6.tick_params(colors=W,labelsize=8)
for b,v in zip(bars,vals):
    ax6.text(b.get_x()+b.get_width()/2,v+3,f'{v:.1f}\n{v*E0:.0f} MeV',
             ha='center',color=W,fontsize=7.5,fontweight='bold')
ax6.text(0.5,0.95,f'E_var/M_ANW = {ratio:.0f}×\n[Task #31e resolves\nnormalisation]',
         transform=ax6.transAxes,ha='center',va='top',color=Or,fontsize=9,
         bbox=dict(boxstyle='round,pad=0.3',fc=PBG,ec=G,lw=1))

fig.suptitle(
    f'CCEF Task #31d  Hedgehog Soliton  '
    f'α_opt={aopt:.3f} L₀  E_var={Emin:.1f} E₀  '
    f'δM(A3)={E3o:.2f} E₀  M_N(ANW)={M_N_ANW:.0f} MeV  ratio={ratio:.0f}×',
    color=G,fontsize=10.5,y=0.998)
fig.savefig('ccef_soliton_bvp.png',dpi=140,bbox_inches='tight',facecolor=DARK)
plt.close(fig)
print("\nFigure: ccef_soliton_bvp.png")
print(f"\n[SUMMARY]")
print(f"  α_opt  = {aopt:.5f} L0 = {aopt*L0:.4f} fm")
print(f"  E_var  = {Emin:.5f} E0 = {Emin*E0:.1f} MeV  (no A3)")
print(f"  δM(A3) = {E3o:.5f} E0 = {E3o*E0:.2f} MeV  (1st-order pert.)")
print(f"  M_ANW  = {M_N_ANW/E0:.5f} E0 = {M_N_ANW:.3f} MeV  (analytical)")
print(f"  ratio  = {ratio:.2f}  → Task #31e normalisation")
print("[DONE] Task #31d.")
