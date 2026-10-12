#!/usr/bin/env python3
"""
ccef_geo_seed.py  --  can 3-D space GROW from a seed?  (nucleation-and-growth test, angle rule on)

Start: 3x3x3 diamond torus (216 junctions, a proven ground state) with the grains in one half of the box
randomly rewired (no energy check) -> half crystal, half tangle.  Then hold a fixed temperature T and track the
fraction of perfect (diamond) junctions.  Front advances -> space can nucleate and grow; retreats -> it melts.
"""

import random
from multiprocessing import Pool

import numpy as np

from ccef_geo_dynamics import Graph2, anatomy
from ccef_grain_hamiltonian_mc import diamond


def scrambled_start(seed):
    rng = random.Random(seed)
    N, edges = diamond(3)
    n = N // 2
    half = [k for k, (a, b) in enumerate(edges) if a < n // 2]           # A sites are ordered by x: first half of box
    adj = [set() for _ in range(N)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    done = 0
    while done < 4 * len(half):
        i, j = rng.choice(half), rng.choice(half)
        (a, b), (c, d) = edges[i], edges[j]
        if a == c or b == d or d in adj[a] or b in adj[c]:
            continue
        adj[a].remove(b); adj[b].remove(a); adj[c].remove(d); adj[d].remove(c)
        adj[a].add(d); adj[d].add(a); adj[c].add(b); adj[b].add(c)
        edges[i], edges[j] = (a, d), (c, b)
        done += 1
    return N, edges


def job(T):
    rng = random.Random(int(T * 100))
    N, edges = scrambled_start(1)
    g = Graph2(N, edges, 1, 8, 4)
    track = []
    for s in range(12):
        for _ in range(12 * N):
            g.try_move(T, rng)
        cats, _ = anatomy(g)
        track.append((12 * (s + 1), g.E / N, cats["perfect (diamond)"] / N))
    return T, track


if __name__ == "__main__":
    N, e = scrambled_start(1)
    g0 = Graph2(N, e, 1, 8, 4)
    c0, _ = anatomy(g0)
    print(f"start: E/N = {g0.E / N:+.2f}, perfect junctions {100 * c0['perfect (diamond)'] / N:.0f}%")
    with Pool(4) as pool:
        res = pool.map(job, [0.3, 0.6, 1.0, 1.5])
    for T, track in res:
        print(f"T = {T}: " + "  ".join(f"{sw}sw:{E:+.2f}/{100 * f:.0f}%" for sw, E, f in track[::2]))
