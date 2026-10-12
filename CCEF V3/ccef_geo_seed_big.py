#!/usr/bin/env python3
"""
ccef_geo_seed_big.py  --  can 3-D space grow from a seed?  Bigger universe (angle rule on).

6x6x6 conventional-cube diamond torus = 1728 junctions (a proven ground state, E/N = -12).
A slab 2 cells thick (x in [0, 8) of a 24-unit box) is randomly rewired -> 4-cell-thick crystal + 2-cell tangle.
At fixed temperature T, track energy, the perfect-junction fraction and its PROFILE across x (6 bins of one cell):
crystal advancing into the tangle = space can grow from a nucleus; retreating = it melts/dissolves.
"""

import json
import random
import sys
import time
from multiprocessing import Pool

import numpy as np

from ccef_geo_dynamics import Graph2

DELTAS = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
L = 6
BOX = 4 * L


def diamond_xyz():
    A = [(x, y, z) for x in range(0, BOX, 2) for y in range(0, BOX, 2) for z in range(0, BOX, 2) if (x + y + z) % 4 == 0]
    ia = {r: i for i, r in enumerate(A)}
    n = len(A)
    edges = []
    for r in A:
        for d in DELTAS:
            b = tuple((r[k] + d[k]) % BOX for k in range(3))
            bb = tuple((b[k] - 1) % BOX for k in range(3))
            edges.append((ia[r], n + ia[bb]))
    xs = [r[0] for r in A] + [(r[0] + 1) % BOX for r in A]
    return 2 * n, edges, np.array(xs), n


def scrambled(seed):
    rng = random.Random(seed)
    N, edges, xs, n = diamond_xyz()
    slab = [k for k, (a, b) in enumerate(edges) if xs[a] < 8]
    adj = [set() for _ in range(N)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    done = 0
    while done < 4 * len(slab):
        i, j = rng.choice(slab), rng.choice(slab)
        (a, b), (c, d) = edges[i], edges[j]
        if a == c or b == d or d in adj[a] or b in adj[c]:
            continue
        adj[a].remove(b); adj[b].remove(a); adj[c].remove(d); adj[d].remove(c)
        adj[a].add(d); adj[d].add(a); adj[c].add(b); adj[b].add(c)
        edges[i], edges[j] = (a, d), (c, b)
        done += 1
    return N, edges, xs


def profile(g, xs):
    perf = np.array([g.full_stats(v) == (0, 12, 0, 0) for v in range(g.N)])
    bins = (xs // 4).astype(int)
    return perf.mean(), [round(float(perf[bins == b].mean()), 2) for b in range(L)]


def job(args):
    T, sweeps, checks = args
    rng = random.Random(int(T * 1000) + 3)
    N, edges, xs = scrambled(1)
    g = Graph2(N, edges, 1, 8, 4)
    f0, p0 = profile(g, xs)
    track = [(0, g.E / N, f0, p0)]
    t0 = time.time()
    per = int(sweeps * N) // checks
    for c in range(checks):
        for _ in range(per):
            g.try_move(T, rng)
        f, p = profile(g, xs)
        track.append(((c + 1) * sweeps / checks, g.E / N, f, p))
    return T, track, time.time() - t0


if __name__ == "__main__":
    sweeps = float(sys.argv[1]) if len(sys.argv) > 1 else 30
    temps = [0.3, 0.6, 1.0, 1.5]
    with Pool(4) as pool:
        res = pool.map(job, [(T, sweeps, 6) for T in temps])
    out = []
    print(f"universe: {L}x{L}x{L} diamond torus, 1728 junctions; tangle = cells 0-1, crystal = cells 2-5")
    for T, track, dt in res:
        print(f"\nT = {T}  ({dt:.0f}s)")
        for sw, E, f, p in track:
            print(f"   {sw:5.1f} sweeps: E/N = {E:+.3f}  perfect {100 * f:4.1f}%  profile by cell {p}")
        out.append(dict(T=T, track=track))
    json.dump(out, open("ccef_geo_seed_big.json", "w"), indent=1)
