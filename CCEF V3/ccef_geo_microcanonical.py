#!/usr/bin/env python3
"""
ccef_geo_microcanonical.py  --  can space crystallise from one seed when ENERGY IS CONSERVED and light is the only sink?

The earlier seed growth (ccef_geo_template.py) used Metropolis at a fixed temperature: an external heat bath.  The
grain rules are reversible events (CCEF_grain_rules.md, CCEF_geometry_events.md): no outside bath exists.  Here the
light sector IS the bath:
  * every junction v carries a light-energy reservoir D_v >= 0 with c light modes (classical heat capacity c per
    junction; light temperature T = <D>/c);
  * a geometry move (star template or single swap) with energy change dE is paid from / paid into the light in its
    own footprint S (pool P = sum_S D_v, k = c|S| modes).  Exact microcanonical rule: accept with
    min(1, ((P - dE)/P)^(k-1))  (ratio of the light's densities of states), then the pool P - dE is re-shared among S
    (light thermalises locally).  Total energy E_geo + sum D is conserved exactly.
  * light events move energy along grains: (D_u, D_v) -> (s x, s (1-x)), x ~ Beta(c, c) (energy-conserving,
    Kipnis-Marchioro-Presutti); stationary state Gamma(c, T) at every junction.
Start: the TINY seed (one cubic cell of crystal in a fully tangled 1,728-junction universe, E/N = -0.03), light COLD.
Runs: c = 1, 3, 9, 30 light modes per junction (4 cores).  Same template proposals as before (non-equilibrium growth
rule); only the acceptance is changed from 'external bath' to 'energy conserved, light absorbs'.
"""

import json
import math
import random
import sys
import time
from multiprocessing import Pool

import numpy as np

from ccef_geo_template import GT, front, make_start, template_set


def micro_composite(g, steps, D, c, nrng):
    done, touched = [], set()
    for st in steps:
        a = st()
        if a is not None:
            done.append(a)
            touched.update(a[2:])
    if not done:
        return False
    S_after = g.ball2(tuple(touched))
    for a in reversed(done):
        g.undo(a)
    S = S_after | g.ball2(tuple(touched))
    for a in done:
        g._swap(*a)
    new = {v: g.vstats_e(v) for v in S}
    dE = sum(new[v] - g.ev[v] for v in S)
    Sl = list(S)
    P = float(sum(D[v] for v in Sl))
    k = c * len(Sl)
    if dE <= 0:
        acc = True
    elif dE >= P:
        acc = False
    else:
        acc = random.random() < math.exp((k - 1) * math.log1p(-dE / P))
    if not acc:
        for a in reversed(done):
            g.undo(a)
        return False
    for v, e in new.items():
        g.ev[v] = e
    g.E += dE
    w = nrng.gamma(c, 1.0, len(Sl))
    w *= (P - dE) / w.sum()
    for v, x in zip(Sl, w):
        D[v] = float(x)
    return True


def job(spec):
    name, c, n_coll, n_single, n_light = spec
    rng = random.Random(5)
    random.seed(17)
    nrng = np.random.default_rng(23)
    N, edges, tmpl, nA, xs = make_start("tiny", 1)
    g = GT(N, edges, 1, 8, 4)
    g.setup(tmpl, nA)
    D = [0.0] * N
    Etot0 = g.E + sum(D)
    fr, f0, _ = front(g)
    perf = lambda: float(np.mean([g.perfect(v) for v in range(N)]))
    track = [(0, g.E / N, f0, perf(), 0.0, 0)]
    acc = 0
    t0 = time.time()
    for it in range(1, n_coll + 1):
        if fr:
            u = rng.choice(fr)
            steps = []
            for v in sorted(template_set(g, u, 2), key=lambda _: rng.random()):
                for t in g.tmpl[v]:
                    steps.append(lambda v=v, t=t: (g.directed(v, t, rng) if t not in g.adj[v] else None))
            acc += micro_composite(g, steps, D, c, nrng)
        for _ in range(n_single):
            i, j = rng.randrange(len(g.edges)), rng.randrange(len(g.edges))
            (a, b), (cc, d) = g.edges[i], g.edges[j]
            if a == cc or b == d or d in g.adj[a] or b in g.adj[cc]:
                continue
            micro_composite(g, [lambda i=i, j=j, a=a, b=b, cc=cc, d=d: (g._swap(i, j, a, b, cc, d) or
                                                                        (i, j, a, b, cc, d))], D, c, nrng)
        for _ in range(n_light):
            a, b = g.edges[rng.randrange(len(g.edges))]
            s = D[a] + D[b]
            x = rng.betavariate(c, c)
            D[a], D[b] = s * x, s * (1 - x)
        if it % 50 == 0:
            fr, f, _ = front(g)
        if it % (n_coll // 8) == 0:
            fr, f, _ = front(g)
            track.append((it, g.E / N, f, perf(), float(np.mean(D)) / c, acc))
    drift = (g.E + sum(D)) - Etot0
    return name, c, track, drift, time.time() - t0


if __name__ == "__main__":
    n_coll = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    cs = [float(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else (1, 3, 9, 30)
    tag = sys.argv[3] if len(sys.argv) > 3 else ""
    specs = [(f"c={c:g}", c, n_coll, 3, 200) for c in cs]
    with Pool(4) as pool:
        res = pool.map(job, specs)
    out = []
    print("TINY seed, 1,728 junctions, light starts cold; energy conserved (geometry + light)")
    for name, c, track, drift, dt in res:
        print(f"\nlight modes per junction {name}   ({dt:.0f} s; total-energy drift {drift:+.1e})")
        for it, E, f, pf, T, acc in track:
            print(f"   {it:5d} star moves (accepted {acc:4d}): E_geo/N = {E:+8.3f}  in registry {100 * f:5.1f}%  "
                  f"perfect {100 * pf:5.1f}%   light temperature T = {T:6.3f}")
        out.append(dict(name=name, c=c, track=track, drift=drift))
    json.dump(out, open(f"ccef_geo_microcanonical{tag}.json", "w"), indent=1)
