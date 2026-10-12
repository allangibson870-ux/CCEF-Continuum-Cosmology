#!/usr/bin/env python3
"""
ccef_geo_template.py  --  can COLLECTIVE 'template' moves grow 3-D space from a seed?  (angle rule on)

Template move (a growth rule, like epitaxy): pick a junction u on the crystal front (not perfect, a perfect junction
within 2 steps); rewire ALL of u's grains in one go so its neighbours continue the crystal's registry (diamond is
locally rigid, so the registry is fixed by the seed; here taken from the seed's lattice).  Each missing link u-t is made
by a degree-preserving swap (u,x),(y,t) -> (u,t),(y,x) with x, y chosen among non-registry neighbours.  The whole
composite move is accepted or rejected by Metropolis on the total energy change.  Not exact detailed balance:
a non-equilibrium growth dynamics.  Interleaved with ordinary single swaps (the tangle keeps relaxing).

Runs (1728-junction 6x6x6 torus):
  BIG_T0.6, BIG_T1.5 : 4-cell crystal + 2-cell tangle (as ccef_geo_seed_big.py), template + single moves
  TINY_T0.6          : one-cell seed (~8 junctions' worth of registry) in an otherwise fully tangled universe
  CTRL_T0.6          : big seed, same budget, UNGUIDED composite moves (4 random swaps near the front at once)
"""

import json
import math
import random
import sys
import time
from multiprocessing import Pool

import numpy as np

from ccef_geo_dynamics import Graph2
from ccef_geo_seed_big import diamond_xyz, L

BOX = 4 * L


class GT(Graph2):
    def setup(self, tmpl, nA):
        self.tmpl, self.nA = tmpl, nA
        self.eidx = {e: i for i, e in enumerate(self.edges)}

    def _swap(self, i, j, a, b, c, d):
        del self.eidx[(a, b)], self.eidx[(c, d)]
        super()._swap(i, j, a, b, c, d)
        self.eidx[(a, d)], self.eidx[(c, b)] = i, j

    def perfect(self, v):
        return self.full_stats(v) == (0, 12, 0, 0)

    def directed(self, u, t, rng):
        """make u-t adjacent by one swap; return (i, j, a, b, c, d) for undo, or None"""
        xs = [x for x in self.adj[u] if x not in self.tmpl[u]]
        ys = [y for y in self.adj[t] if y not in self.tmpl[t] and y != u] or [y for y in self.adj[t] if y != u]
        if not xs or not ys:
            return None
        x, y = rng.choice(xs), rng.choice(ys)
        if x in self.adj[y] or x == t:
            return None
        if u < self.nA:
            i, j = self.eidx[(u, x)], self.eidx[(y, t)]
            args = (i, j, u, x, y, t)
        else:
            i, j = self.eidx[(x, u)], self.eidx[(t, y)]
            args = (i, j, x, u, t, y)
        self._swap(*args)
        return args

    def undo(self, args):
        i, j, a, b, c, d = args
        self._swap(i, j, a, d, c, b)

    def composite(self, steps, T):
        """steps: list of callables performing one swap and returning args (or None). Metropolis on the whole."""
        done, touched = [], set()
        for st in steps:
            a = st()
            if a is not None:
                done.append(a)
                touched.update(a[2:])
        if not done:
            return False
        S_after = self.ball2(tuple(touched))
        for a in reversed(done):
            self.undo(a)
        S = S_after | self.ball2(tuple(touched))
        for a in done:
            self._swap(*a)
        new = {v: self.vstats_e(v) for v in S}
        dE = sum(new[v] - self.ev[v] for v in S)
        if dE <= 0 or random.random() < math.exp(-dE / T):
            for v, e in new.items():
                self.ev[v] = e
            self.E += dE
            return True
        for a in reversed(done):
            self.undo(a)
        return False


def make_start(kind, seed):
    rng = random.Random(seed)
    N, ideal, xs, n = diamond_xyz()
    A = [(x, y, z) for x in range(0, BOX, 2) for y in range(0, BOX, 2) for z in range(0, BOX, 2) if (x + y + z) % 4 == 0]
    pos = np.array(A + [((x + 1) % BOX, (y + 1) % BOX, (z + 1) % BOX) for x, y, z in A])
    if kind == "big":
        keep = lambda a, b: not (pos[a][0] < 8)
    else:   # tiny: keep only grains with both ends inside one conventional cube (plus its boundary)
        inside = lambda v: all(8 <= pos[v][k] <= 13 for k in range(3))
        keep = lambda a, b: inside(a) and inside(b)
    edges = list(ideal)
    free = [k for k, (a, b) in enumerate(edges) if not keep(a, b)]
    adj = [set() for _ in range(N)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    done = 0
    while done < 4 * len(free):
        i, j = rng.choice(free), rng.choice(free)
        (a, b), (c, d) = edges[i], edges[j]
        if a == c or b == d or d in adj[a] or b in adj[c]:
            continue
        adj[a].remove(b); adj[b].remove(a); adj[c].remove(d); adj[d].remove(c)
        adj[a].add(d); adj[d].add(a); adj[c].add(b); adj[b].add(c)
        edges[i], edges[j] = (a, d), (c, b)
        done += 1
    tmpl = [set() for _ in range(N)]
    for a, b in ideal:
        tmpl[a].add(b)
        tmpl[b].add(a)
    return N, edges, tmpl, n, xs


def front(g):
    """registry front: not in registry (neighbours != template) but touching a junction that is"""
    reg = [set(g.adj[v]) == g.tmpl[v] for v in range(g.N)]
    fr = [v for v in range(g.N) if not reg[v] and any(reg[w] for w in g.adj[v] + list(g.tmpl[v]))]
    return fr, float(np.mean(reg)), reg


def template_set(g, u, size=2):
    S = {u}
    for _ in range(size - 1):
        S |= {t for v in S for t in g.tmpl[v]}
    return S


def job(spec):
    name, kind, T, mode, n_coll, n_single_per = spec
    rng = random.Random(hash(name) % 1000)
    random.seed(hash(name) % 997)
    N, edges, tmpl, nA, xs = make_start(kind, 1)
    g = GT(N, edges, 1, 8, 4)
    g.setup(tmpl, nA)
    fr, f0, reg = front(g)
    bins = (xs // 4).astype(int)
    prof = lambda flags: [round(float(np.mean(np.array(flags)[bins == b])), 2) for b in range(L)]
    perf0 = [g.perfect(v) for v in range(N)]
    track = [(0, g.E / N, f0, float(np.mean(perf0)), prof(perf0), 0)]
    t0 = time.time()
    acc = 0
    for c in range(1, n_coll + 1):
        if fr:
            u = rng.choice(fr)
            if mode == "template":
                steps = []
                for v in sorted(template_set(g, u, 2), key=lambda _: rng.random()):
                    for t in g.tmpl[v]:
                        steps.append(lambda v=v, t=t: (g.directed(v, t, rng) if t not in g.adj[v] else None))
            else:
                ball = list(g.ball2((u,)))
                cand = [g.eidx[(a, b)] for a in ball for b in g.adj[a] if a < nA]

                def rnd():
                    i, j = rng.choice(cand), rng.choice(cand)
                    (a, b), (cc, d) = g.edges[i], g.edges[j]
                    if a == cc or b == d or d in g.adj[a] or b in g.adj[cc]:
                        return None
                    g._swap(i, j, a, b, cc, d)
                    return (i, j, a, b, cc, d)
                steps = [rnd] * 8                      # same number of rewirings as a star template (~8)
            acc += g.composite(steps, T)
        for _ in range(n_single_per):
            i, j = rng.randrange(len(g.edges)), rng.randrange(len(g.edges))
            (a, b), (cc, d) = g.edges[i], g.edges[j]
            if a == cc or b == d or d in g.adj[a] or b in g.adj[cc]:
                continue
            g.composite([lambda i=i, j=j, a=a, b=b, cc=cc, d=d: (g._swap(i, j, a, b, cc, d) or (i, j, a, b, cc, d))], T)
        if c % 50 == 0:
            fr, f, reg = front(g)
        if c % (n_coll // 6) == 0:
            fr, f, reg = front(g)
            perf = [g.perfect(v) for v in range(N)]
            track.append((c, g.E / N, f, float(np.mean(perf)), prof(perf), acc))
    return name, track, time.time() - t0


if __name__ == "__main__":
    n_coll = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    specs = [("BIG_T0.6", "big", 0.6, "template", n_coll, 3), ("BIG_T1.5", "big", 1.5, "template", n_coll, 3),
             ("TINY_T0.6", "tiny", 0.6, "template", n_coll, 3), ("CTRL_T0.6", "big", 0.6, "random", n_coll, 3)]
    with Pool(4) as pool:
        res = pool.map(job, specs)
    out = []
    for name, track, dt in res:
        print(f"\n{name}  ({dt:.0f}s)")
        for c, E, f, pf, p, acc in track:
            print(f"   {c:5d} collective moves (accepted {acc:4d}): E/N = {E:+.3f}  in registry {100 * f:5.1f}%  "
                  f"perfect {100 * pf:5.1f}%  perfect-profile {p}")
        out.append(dict(name=name, track=track))
    json.dump(out, open("ccef_geo_template.json", "w"), indent=1)
