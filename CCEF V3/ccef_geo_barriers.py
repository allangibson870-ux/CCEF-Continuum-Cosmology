#!/usr/bin/env python3
"""
ccef_geo_barriers.py  --  energy landscape around diamond and around the frozen (glassy) states.

1. Diamond's excitation gap: energy cost of single rewiring moves (random sample of valid swaps).
2. Frozen state (from ccef_geo_dynamics.py): are its defects healable by 1 or 2 rewiring moves?
   For 2-move paths: first move anywhere near a defect, second move among nearby grains; record net dE and the
   intermediate barrier (dE after the first move).  Quantum tunnelling through a 2-move path scales like
   Gamma^2 / barrier; thermal hopping like exp(-barrier / T).  Defects that need many coordinated moves are extended.
"""

import json
import random
import sys

import numpy as np

from ccef_geo_dynamics import Graph2
from ccef_grain_hamiltonian_mc import diamond


def swap_dE(g, i, j):
    (a, b), (c, d) = g.edges[i], g.edges[j]
    if a == c or b == d or d in g.adj[a] or b in g.adj[c]:
        return None
    S_ = g.ball2((a, b, c, d))
    g._swap(i, j, a, b, c, d)
    S_ |= g.ball2((a, b, c, d))
    new = {v: g.vstats_e(v) for v in S_}
    dE = sum(new[v] - g.ev[v] for v in S_)
    return dE, new, (a, b, c, d)


def undo(g, i, j, abcd):
    a, b, c, d = abcd
    g._swap(i, j, a, d, c, b)


def commit(g, new, dE):
    for v, e in new.items():
        g.ev[v] = e
    g.E += dE


rng = random.Random(5)
N, e = diamond(3)
g = Graph2(N, e, 1, 8, 4)
dEs = []
while len(dEs) < 1500:
    i, j = rng.randrange(len(g.edges)), rng.randrange(len(g.edges))
    r = swap_dE(g, i, j)
    if r is None:
        continue
    dEs.append(r[0])
    undo(g, i, j, r[2])
dEs = np.array(dEs)
print(f"1. DIAMOND: single rewiring moves (1500 sampled): min dE = {dEs.min():.1f}, median {np.median(dEs):.1f}, "
      f"max {dEs.max():.1f}  (every move costs energy: diamond is locally stable with gap {dEs.min():.0f})")

name = sys.argv[1] if len(sys.argv) > 1 else "SA30"
edges = [tuple(x) for x in json.load(open(f"ccef_geo_final_{name}.json"))["edges"]]
g = Graph2(216, edges, 1, 8, 4)
bad = [v for v in range(g.N) if g.full_stats(v) != (0, 12, 0, 0)]
badset = set(bad)
print(f"\n2. FROZEN STATE {name}: E/N = {g.E / g.N:+.3f}, {len(bad)} defective junctions")
near = [k for k, (a, b) in enumerate(g.edges) if a in badset or b in badset]
one_down, one = 0, []
for _ in range(1500):
    i, j = rng.choice(near), rng.randrange(len(g.edges))
    r = swap_dE(g, i, j)
    if r is None:
        continue
    one.append(r[0])
    one_down += r[0] < 0
    undo(g, i, j, r[2])
one = np.array(one)
print(f"   single moves touching defects ({len(one)}): downhill {one_down}; smallest cost {one.min():.1f}, median {np.median(one):.1f}")
two_paths = []
tries = 0
for _ in range(250):
    i, j = rng.choice(near), rng.choice(near)
    r1 = swap_dE(g, i, j)
    if r1 is None:
        continue
    dE1, new1, abcd1 = r1
    commit(g, new1, dE1)
    a, b, c, d = abcd1
    loc = g.ball2((a, b, c, d))
    cand = [k for k, (x, y) in enumerate(g.edges) if x in loc or y in loc]
    for _ in range(40):
        k1, k2 = rng.choice(cand), rng.choice(cand)
        r2 = swap_dE(g, k1, k2)
        if r2 is None:
            continue
        tries += 1
        if dE1 + r2[0] < -1e-9:
            two_paths.append((dE1, dE1 + r2[0]))
        undo(g, k1, k2, r2[2])
    # revert first move
    old = {}
    undo(g, i, j, abcd1)
    S_ = g.ball2((a, b, c, d)) | g.ball2((a, d, c, b))
    for v in S_:
        g.ev[v] = g.vstats_e(v)
    g.E -= dE1
print(f"   two-move paths tested: {tries}; net-downhill paths found: {len(two_paths)}")
if two_paths:
    bar = np.array([p[0] for p in two_paths])
    gain = np.array([p[1] for p in two_paths])
    print(f"   their intermediate barriers: min {bar.min():.1f}, median {np.median(bar):.1f}; net gains: best {gain.min():.1f}")
