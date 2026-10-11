#!/usr/bin/env python3
"""
ccef_grain_fermion_bands.py  --  are the junction fermions LIGHT?  Smooth band-structure test with twisted boundaries.

H(theta) = -t sum_<uv> s_uv e^{i theta . w_uv / n} (c_u^+ c_v + h.c.) on the L = 4 diamond torus (512 junctions),
where w_uv is the edge's winding across the box; averaging over a grid of twists theta samples momentum space
continuously.  Background flux through every 6-ring: 0 (s = +1) or pi (s from GF(2), ccef_grain_fermions.py).
Cumulative low-energy state count N(|E| < e) ~ e^p at half filling:
   p = 3: isolated Dirac points (massless relativistic electrons; count of cones from the coefficient)
   p = 2: nodal lines      p = 1: Fermi surface / flat-ish     gap: heavy
"""

import os
from multiprocessing import Pool

import numpy as np

from ccef_grain_lattice import pi_flux_signs, build

DELTAS = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]


def windings(L):
    box = 4 * L
    A = [(x, y, z) for x in range(0, box, 2) for y in range(0, box, 2) for z in range(0, box, 2) if (x + y + z) % 4 == 0]
    return np.array([[(r[k] + d[k]) // box for k in range(3)] for r in A for d in DELTAS])


L = 4
N, edges, inc, hexes = build(L)
W = windings(L)
ea = np.array([a for a, b in edges])
eb = np.array([b for a, b in edges])
S = {"0": np.ones(len(edges)), "pi": pi_flux_signs(edges, hexes)}


def spectrum(args):
    flux, tx, ty, tz = args
    ph = np.exp(1j * (W @ np.array([tx, ty, tz])))
    H = np.zeros((N, N), dtype=complex)
    H[ea, eb] = -S[flux] * ph
    H[eb, ea] = -S[flux] * np.conj(ph)
    return np.linalg.eigvalsh(H)


if __name__ == "__main__":
  os.environ["OMP_NUM_THREADS"] = "1"
  out = {}
  tw = np.linspace(0, 2 * np.pi, 8, endpoint=False) + np.pi / 8
  with Pool(4) as pool:
   for flux in ("0", "pi"):
    evs = pool.map(spectrum, [(flux, a, b, c) for a in tw for b in tw for c in tw], chunksize=16)
    ev = np.abs(np.concatenate(evs))
    es = np.array([0.05, 0.08, 0.12, 0.18, 0.25])
    Ns = np.array([np.mean(ev < e) for e in es])
    p = np.polyfit(np.log(es), np.log(Ns), 1)[0]
    out[flux] = (Ns, p, ev.min())
    print(f"flux {flux:>2s}: N(|E|<e) for e = {list(es)}: {['%.2e' % x for x in Ns]}  ->  N ~ e^{p:.2f};"
          f"  smallest |E| over all twists = {ev.min():.4f}", flush=True)
  p0, ppi = out["0"][1], out["pi"][1]
  print(f"\nzero flux: exponent {p0:.2f} -> {'nodal lines (not relativistic)' if 1.5 < p0 < 2.5 else 'see value'}")
  print(f"pi flux:   exponent {ppi:.2f} -> {'isolated Dirac points: massless relativistic electrons' if ppi > 2.5 else 'not point nodes'}")
