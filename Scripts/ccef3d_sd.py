"""Self-dual fixed-point Hopf relaxation: full action incl. finite A3.
Semi-implicit: linear (A1 k^2 + A3 k^4) implicit in Fourier, A2+A4 explicit.
"""
import sys, time, json, numpy as np, ccef3d as M

A1=1.0; A4=3.5553; A3=A1**2/A4; A2=A4**-1.5   # self-dual fixed point
E0=30.608; MP=938.272/E0
L,N=2.2,96
box=M.Box(L=L,N=N)
Lhat=A1*box.K2 + A3*box.K2**2                 # linear operator symbol

def seed(scale):
    x,y,z=box.X/scale,box.Y/scale,box.Z/scale; r2=x*x+y*y+z*z
    den=2*z+1j*(r2-1.0); den=den+1e-9*(np.abs(den)<1e-9)
    w=2*(x+1j*y)/den; aw2=np.abs(w)**2; dd=aw2+1.0
    return M.renorm(np.stack([2*np.real(w)/dd,2*np.imag(w)/dd,(aw2-1.0)/dd]))

def E_A3term(n):
    return 0.5*A3*float(sum((M.lap(box,n[a])**2).sum() for a in range(3)))*box.dx**3

def energies(n):
    e=M.energies(box,n,A1,A2,A4); e['E_A3']=E_A3term(n); e['E']+=e['E_A3']; return e

def nonlin_grad(n):
    # explicit part: A2 Faddeev + A4 potential (NO A1,A3 -> those go implicit)
    g=M.raw_grad(box,n,0.0,A2,A4)
    # project to tangent
    ndg=sum(n[a]*g[a] for a in range(3))
    return np.stack([g[a]-ndg*n[a] for a in range(3)])

def step(n,dt):
    Nexp=nonlin_grad(n)
    rhs=n-dt*Nexp
    out=np.empty_like(n)
    for a in range(3):
        out[a]=np.real(np.fft.ifftn(np.fft.fftn(rhs[a])/(1.0+dt*Lhat)))
    return M.renorm(out)

def virial(e):  # E1 - (E2+E3) + 3 E4   (A2,A3 both ~1/lambda)
    return e['E_A1'] - (e['E_A2']+e['E_A3']) + 3*e['E_A4']
