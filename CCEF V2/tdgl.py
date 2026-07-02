import numpy as np

# Cold check: Model A (non-conserved) TDGL from the IR Landau-Ginzburg free energy
#   F = INT [ (A1/2)|grad chi|^2 + U(chi) ],  U = (r/2)chi^2 + (u/4)chi^4,  r<0
#   Model A EOM (overdamped, mobility Gamma=1/gamma):
#   d_t chi = Gamma[ A1 lap chi - U'(chi) ],  U'(chi)= r chi + u chi^3
# Claim to verify: coarsening domain size L(t) ~ t^(1/2)
#   tested via excess free-energy density  f_exc(t) ~ sigma/L ~ t^(-1/2).

np.random.seed(0)
N   = 256
A1  = 1.0
r   = -1.0      # ordered (double well); chi0 = sqrt(-r/u)=1
u   = 1.0
Gam = 1.0       # = 1/gamma
dx  = 1.0
dt  = 0.05
nsteps = 60000

chi = 0.05*(np.random.rand(N,N)-0.5)   # small random init (disordered)

def lap(f):
    return (np.roll(f,1,0)+np.roll(f,-1,0)+np.roll(f,1,1)+np.roll(f,-1,1)-4*f)/dx**2

def excess_energy(f):
    # gradient energy density (vanishes inside domains, lives on walls -> ~ sigma * wall_len/area ~ sigma/L)
    gx=(np.roll(f,-1,0)-f)/dx; gy=(np.roll(f,-1,1)-f)/dx
    grad=0.5*A1*(gx*gx+gy*gy)
    return grad.mean()

ts=[]; es=[]
for s in range(nsteps):
    Up = r*chi + u*chi**3
    chi += dt*Gam*(A1*lap(chi) - Up)
    if s>0 and s%500==0:
        t=s*dt
        ts.append(t); es.append(excess_energy(chi))

ts=np.array(ts); es=np.array(es)
# fit in the scaling window (late times, after transient)
mask = ts> ts[-1]*0.15
p=np.polyfit(np.log(ts[mask]), np.log(es[mask]),1)
print("fitted slope d ln(f_exc)/d ln t =", round(p[0],4), " (Allen-Cahn predicts -0.5)")
print("=> L(t) ~ f_exc^-1 ~ t^", round(-p[0],4), " (predicts +0.5)")
# also fit a couple of windows to show robustness
for lo in (0.1,0.2,0.3):
    m=ts>ts[-1]*lo
    q=np.polyfit(np.log(ts[m]),np.log(es[m]),1)
    print(f"  window t>{lo:.0%}*tmax: L exponent = {-q[0]:.3f}")
