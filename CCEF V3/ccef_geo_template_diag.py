#!/usr/bin/env python3
"""
ccef_geo_template_diag.py  --  how big must a template move be before it pays?  (big seed, angle rule on)

Front (registry-based): junctions whose 4 neighbours are not all in the crystal registry but that touch a junction
whose neighbours are.  For 120 random front junctions, measure the energy change dE of templating
  size 1: the junction itself;  size 2: the junction + its 4 registry neighbours ('star');
  size 3: star + the registry neighbours of those (2 registry steps)
without accepting.  Negative dE -> the move would be taken at low T.
"""

import random

import numpy as np

import ccef_geo_template as m


def in_reg(g, v):
    return set(g.adj[v]) == g.tmpl[v]


def reg_front(g):
    reg = [in_reg(g, v) for v in range(g.N)]
    return [v for v in range(g.N) if not reg[v] and any(reg[w] for w in g.adj[v] + list(g.tmpl[v]))], np.mean(reg)


def template_set(g, u, size):
    S = {u}
    for _ in range(size - 1):
        S |= {t for v in S for t in g.tmpl[v]}
    return S


def trial_dE(g, S, rng):
    done, touched = [], set()
    for v in sorted(S, key=lambda _: rng.random()):
        for t in list(g.tmpl[v] - set(g.adj[v])):
            a = g.directed(v, t, rng)
            if a is not None:
                done.append(a)
                touched.update(a[2:])
    if not done:
        return None, 0
    S_after = g.ball2(tuple(touched))
    for a in reversed(done):
        g.undo(a)
    Sb = S_after | g.ball2(tuple(touched))
    old = sum(g.ev[v] for v in Sb)
    for a in done:
        g._swap(*a)
    new = sum(g.vstats_e(v) for v in Sb)
    for a in reversed(done):
        g.undo(a)
    return new - old, len(done)


if __name__ == "__main__":
    rng = random.Random(3)
    N, e, tm, nA, xs = m.make_start("big", 1)
    g = m.GT(N, e, 1, 8, 4)
    g.setup(tm, nA)
    fr, freg = reg_front(g)
    print(f"big seed: {100 * freg:.0f}% of junctions in registry; registry front {len(fr)} junctions")
    for size in (1, 2, 3):
        dEs, nsw = [], []
        for u in rng.sample(fr, 120):
            dE, k = trial_dE(g, template_set(g, u, size), rng)
            if dE is not None:
                dEs.append(dE)
                nsw.append(k)
        dEs = np.array(dEs)
        print(f"  template size {size}: {len(dEs)} trials, swaps per move ~{np.mean(nsw):.1f}; dE median {np.median(dEs):+.0f},"
              f" min {dEs.min():+.0f}; fraction downhill {np.mean(dEs < 0):.2f}")
