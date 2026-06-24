"""Diagnostic figure for the Task F retry (3D topology-preserving relaxation)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import ccef3d as M

E0 = 30.608
MP = 938.272 / E0           # 30.65 CCEF
A1, A2, A4 = 1.0, 0.3268, 3.5553

d = np.load("r96_state.npz")
traj = np.array(d["traj"])          # step,E,E1,E2,E4,vir/E,Hcal
n = d["n"]
box = M.Box(L=2.6, N=96)

# Derrick-optimal bound along the trajectory
def derrick(E1, E2, E4):
    u = (-E1 + np.sqrt(E1*E1 + 12*E2*E4)) / (6*E4)
    lam = np.sqrt(u)
    return lam*E1 + E2/lam + lam**3*E4

steps = traj[:, 0]
E = traj[:, 1]
Eder = np.array([derrick(*traj[i, 2:5]) for i in range(len(traj))])
Hcal = traj[:, 6]

fig = plt.figure(figsize=(15, 9))
gs = fig.add_gridspec(2, 3, hspace=0.32, wspace=0.30)

# (1) energy trajectory
ax = fig.add_subplot(gs[0, 0])
ax.plot(steps, E/MP, 'o-', ms=3, label='raw E(field)/m_p')
ax.plot(steps, Eder/MP, 's-', ms=3, color='C1', label='Derrick-optimal E/m_p')
ax.axhline(2.77, ls='--', color='green', label='tanh-ring Derrick bound 2.77')
ax.axhline(1.0, ls=':', color='k', label='target m_p')
ax.set_xlabel('gradient-flow step'); ax.set_ylabel('E / m_p')
ax.set_yscale('log'); ax.legend(fontsize=8); ax.set_title('3D relaxation: energy descends, stays >> m_p')

# (2) topology preserved
ax = fig.add_subplot(gs[0, 1])
ax.plot(steps, Hcal, 'o-', ms=3, color='purple')
ax.axhline(1.0, ls=':', color='k')
ax.set_ylim(0, 1.4); ax.set_xlabel('step'); ax.set_ylabel('calibrated Hopf charge H')
ax.set_title('Topology preserved (H~1) under pure flow\n(Adam/L-BFGS unwound to H=0)')

# (3) virial imbalance
ax = fig.add_subplot(gs[0, 2])
ax.plot(steps, traj[:, 5], 'o-', ms=3, color='brown')
ax.axhline(0.15, ls='--', color='green', label='converged threshold')
ax.set_xlabel('step'); ax.set_ylabel('|E1-E2+3E4|/E'); ax.legend(fontsize=8)
ax.set_title('Virial imbalance (shape not fully converged)')

# (4) field slice: n_z in y=0 plane
ax = fig.add_subplot(gs[1, 0])
j0 = box.N//2
im = ax.imshow(n[2][:, j0, :].T, origin='lower', cmap='RdBu', vmin=-1, vmax=1,
               extent=[-box.L, box.L, -box.L, box.L])
ax.set_xlabel('x'); ax.set_ylabel('z'); ax.set_title('n_z in y=0 plane (relaxed Q=1 field)')
plt.colorbar(im, ax=ax, shrink=0.8)

# (5) energy density slice
ax = fig.add_subplot(gs[1, 1])
e1, e2, e4, _ = M.energy_density(box, n, A1, A2, A4)
ed = (e1+e2+e4)[:, j0, :].T
im = ax.imshow(ed, origin='lower', cmap='inferno',
               extent=[-box.L, box.L, -box.L, box.L])
ax.set_xlabel('x'); ax.set_ylabel('z'); ax.set_title('energy density (toroidal localization)')
plt.colorbar(im, ax=ax, shrink=0.8)

# (6) comparison bar
ax = fig.add_subplot(gs[1, 2])
labels = ['target\nm_p', 'hedgehog\n(wrong sector)', 'tanh-ring\nDerrick', '3D flow\nDerrick (this)']
vals = [1.0, 7.7, 2.77, Eder[-1]/MP]
colors = ['k', 'gray', 'green', 'C1']
ax.bar(labels, vals, color=colors, alpha=0.8)
ax.set_ylabel('E_sol / m_p'); ax.set_yscale('log')
ax.axhline(1.0, ls=':', color='k')
for i, v in enumerate(vals):
    ax.text(i, v*1.1, f'{v:.2f}x', ha='center', fontsize=9)
ax.set_title('Q=1 soliton mass vs proton: gap does NOT close')

fig.suptitle('CCEF Task F (retry): full-3D topology-preserving Hopf relaxation\n'
             'corrected action (A4/2)(1-n3^2), Faddeev A2 stabiliser, A3->0 IR; '
             'gradients FD-verified to 1e-8',
             fontsize=12, fontweight='bold')
plt.savefig("ccef_taskf_3d.png", dpi=140, bbox_inches='tight')
print("saved ccef_taskf_3d.png")
print(f"final raw E/mp={E[-1]/MP:.2f}  Derrick E/mp={Eder[-1]/MP:.2f}  Hcal={Hcal[-1]:.3f}")
