#!/usr/bin/env python3
"""
ccef_geometry_events.py  --  geometry rewiring as local, reversible (unitary) update events.

The state is a quantum superposition of grain networks (with the light/spin-ice qubit on every grain):
    |psi> = sum_x amp(x) |graph_x, spins_x>
Each grain is a relation with a fixed A-end and a movable B-end (P7: one grain type; the network IS the geometry).

GEOMETRY EVENT R(g1, g2): the local degree-preserving switch  (a,b),(c,d) <-> (a,d),(c,b)  of grains g1, g2,
    allowed only if a and c share a neighbour (locality) and no double links appear; it is its own inverse, so
    U = exp(-i [[eps E(G), theta], [theta, eps E(G')]]) on the pair {G, G'} is unitary.
    E = geometry energy U4 * (#4-cycles) - K6 * (#6-rings) through g1, g2 (local; equals the change of the total).
    Gauge-invariant version: allowed only if the two grains carry the same electric flux (sigma^z(g1) = sigma^z(g2)).
LIGHT EVENT L(ring): ring flip of six grains IF they currently form a 6-ring with alternating flux.

Tests (diamond universe, 216 junctions, 432 grains, ice-rule light state from an Euler circuit):
 1. junction rule, bipartiteness, unitarity, Gauss law on every branch; the naive (flux-blind) switch breaks Gauss
 2. how far a geometry event reaches (its footprint)
 3. commutation vs. footprint overlap; causal relations that DIFFER between branches of the superposition
 4. slicing independence: causal order from labels / from the classical background / self-consistent from the state
"""

import itertools
import time
from collections import defaultdict, deque

import numpy as np
from scipy.linalg import expm

from ccef_grain_lattice import build

T0 = time.time()
N, EDGES, _, HEXES = build(3)
NA, M = N // 2, len(EDGES)
AEND = tuple(a for a, b in EDGES)
END0 = tuple(b for a, b in EDGES)
U4, K6, EPS, THETA, PHI = 1.0, 1.0, 0.1, 0.6, 0.5
BASE_ADJ = [set() for _ in range(N)]
for a, b in EDGES:
    BASE_ADJ[a].add(b)
    BASE_ADJ[b].add(a)

_adj = {}


def graph(ends):
    g = _adj.get(ends)
    if g is None:
        if len(_adj) > 20000:
            _adj.clear()
        g = [s.copy() for s in BASE_ADJ]
        for k in range(M):
            if ends[k] != END0[k]:
                g[AEND[k]].discard(END0[k])
                g[END0[k]].discard(AEND[k])
        for k in range(M):
            if ends[k] != END0[k]:
                g[AEND[k]].add(ends[k])
                g[ends[k]].add(AEND[k])
        _adj[ends] = g
    return g


def ball(adj, anchors, r):
    seen = set(anchors)
    front = list(anchors)
    for _ in range(r):
        nxt = []
        for x in front:
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    nxt.append(y)
        front = nxt
    return seen


def cycles_through(adj, u, v):
    out = set()
    stack = [(v, (v,))]
    while stack:
        x, path = stack.pop()
        for y in adj[x]:
            if y == u:
                if len(path) in (3, 5):
                    vs = (u,) + path
                    out.add(frozenset((min(vs[i], vs[(i + 1) % len(vs)]), max(vs[i], vs[(i + 1) % len(vs)]))
                                      for i in range(len(vs))))
            elif y not in path and len(path) < 5:
                stack.append((y, path + (y,)))
    return out


_eloc = {}


def eloc(ends, g1, g2):
    key = (ends, g1, g2)
    e = _eloc.get(key)
    if e is None:
        adj = graph(ends)
        cs = cycles_through(adj, AEND[g1], ends[g1]) | cycles_through(adj, AEND[g2], ends[g2])
        e = U4 * sum(len(c) == 4 for c in cs) - K6 * sum(len(c) == 6 for c in cs)
        if len(_eloc) > 200000:
            _eloc.clear()
        _eloc[key] = e
    return e


def r_partner(ends, spins, g1, g2, gauge=True):
    adj = graph(ends)
    a, b, c, d = AEND[g1], ends[g1], AEND[g2], ends[g2]
    if a == c or b == d or d in adj[a] or b in adj[c] or not (adj[a] & adj[c]):
        return None
    if gauge and spins[g1] != spins[g2]:
        return None
    e2 = list(ends)
    e2[g1], e2[g2] = d, b
    return tuple(e2)


def l_partner(ends, spins, ring):
    inc = defaultdict(list)
    for g in ring:
        inc[AEND[g]].append(g)
        inc[ends[g]].append(g)
    if len(inc) != 6 or any(len(x) != 2 for x in inc.values()):
        return None                                      # the six grains are not a ring in this branch
    order, cur, x = [ring[0]], ring[0], ends[ring[0]]
    while len(order) < 6:
        nxt = inc[x][0] if inc[x][1] == cur else inc[x][1]
        order.append(nxt)
        x = ends[nxt] if AEND[nxt] == x else AEND[nxt]
        cur = nxt
    if any(spins[order[i]] == spins[order[(i + 1) % 6]] for i in range(6)):
        return None                                      # not flippable
    s2 = list(spins)
    for g in ring:
        s2[g] = -s2[g]
    return tuple(s2)


def apply(state, ev, gauge=True):
    new = defaultdict(complex)
    cL, sL = np.cos(PHI), np.sin(PHI)
    for key, amp in state.items():
        ends, spins = key
        if ev[0] == 'R':
            _, g1, g2 = ev
            p = r_partner(ends, spins, g1, g2, gauge)
            E0 = eloc(ends, g1, g2)
            if p is None:
                new[key] += np.exp(-1j * EPS * E0) * amp
                continue
            U = expm(-1j * np.array([[EPS * E0, THETA], [THETA, EPS * eloc(p, g1, g2)]]))
            new[key] += U[0, 0] * amp
            new[(p, spins)] += U[1, 0] * amp
        else:
            p = l_partner(ends, spins, ev[1])
            if p is None:
                new[key] += amp
                continue
            new[key] += cL * amp
            new[(ends, p)] += -1j * sL * amp
    return {k: v for k, v in new.items() if abs(v) > 1e-15}


_fp = {}


def footprint(ev, key):
    ck = (ev, key)
    f = _fp.get(ck)
    if f is not None:
        return f
    ends, spins = key
    if ev[0] == 'L':
        ring = ev[1]
        reads = {('e', g) for g in ring} | {('s', g) for g in ring}
        writes = {('s', g) for g in ring} if l_partner(ends, spins, ring) else set()
        nj = 6
    else:
        _, g1, g2 = ev
        p = r_partner(ends, spins, g1, g2)
        anchors = {AEND[g1], ends[g1], AEND[g2], ends[g2]}
        bl = ball(graph(ends), anchors, 2)
        if p:
            bl |= ball(graph(p), anchors, 2)
        reads = {('e', k) for k in range(M) if AEND[k] in bl or ends[k] in bl}
        reads |= {('s', g1), ('s', g2), ('e', g1), ('e', g2)}
        writes = {('e', g1), ('e', g2)} if p else set()
        nj = len(bl)
    if len(_fp) > 200000:
        _fp.clear()
    f = (reads, writes, nj)
    _fp[ck] = f
    return f


def conflict(e1, e2, key):
    r1, w1, _ = footprint(e1, key)
    r2, w2, _ = footprint(e2, key)
    return bool(w1 & (r2 | w2)) or bool(w2 & (r1 | w1))


def diffnorm(s1, s2):
    keys = set(s1) | set(s2)
    return np.sqrt(sum(abs(s1.get(k, 0) - s2.get(k, 0)) ** 2 for k in keys))


def norm(s):
    return np.sqrt(sum(abs(v) ** 2 for v in s.values()))


def charges(key):
    ends, spins = key
    Q = [0] * N
    for k in range(M):
        Q[AEND[k]] += spins[k]
        Q[ends[k]] -= spins[k]
    return Q


# ---------------------------------------------------------------- ice-rule light state (Euler circuit orientation)
inc0 = [[] for _ in range(N)]
for k, (a, b) in enumerate(EDGES):
    inc0[a].append(k)
    inc0[b].append(k)
used, spins0 = [False] * M, [0] * M
for start in range(N):
    while any(not used[k] for k in inc0[start]):
        v = start
        while True:
            ks = [k for k in inc0[v] if not used[k]]
            if not ks:
                break
            k = ks[0]
            used[k] = True
            spins0[k] = 1 if v < NA else -1
            v = EDGES[k][1] if v == EDGES[k][0] else EDGES[k][0]
# randomise within the ice manifold: reverse random directed loops (keeps 2-in / 2-out everywhere)
_lr = np.random.default_rng(11)
for _ in range(3000):
    v, path, seen = int(_lr.integers(N)), [], {}
    while v not in seen:
        seen[v] = len(path)
        outs = [k for k in inc0[v] if spins0[k] == (1 if v < NA else -1)]
        k = outs[_lr.integers(len(outs))]
        path.append(k)
        v = EDGES[k][1] if v == EDGES[k][0] else EDGES[k][0]
    for k in path[seen[v]:]:
        spins0[k] = -spins0[k]
SPINS0 = tuple(spins0)
KEY0 = (END0, SPINS0)
assert all(q == 0 for q in charges(KEY0))

# ---------------------------------------------------------------- event pools
eid0 = {}
for k, (a, b) in enumerate(EDGES):
    eid0[(a, b)] = eid0[(b, a)] = k
cand = set()
for a in range(NA):
    for e in BASE_ADJ[a]:
        for c in BASE_ADJ[e]:
            if c == a:
                continue
            for b in BASE_ADJ[a] - {e}:
                for d in BASE_ADJ[c] - {e}:
                    if b != d and d not in BASE_ADJ[a] and b not in BASE_ADJ[c]:
                        cand.add(tuple(sorted((eid0[(a, b)], eid0[(c, d)]))))
cand = sorted(cand)
matched = [c for c in cand if SPINS0[c[0]] == SPINS0[c[1]]]
R_EVENTS = [('R',) + c for c in matched]
L_EVENTS = [('L', tuple(h)) for h in HEXES if l_partner(END0, SPINS0, tuple(h))]
dist0 = {}


def bfs_from(v):
    if v not in dist0:
        d = {v: 0}
        q = deque([v])
        while q:
            x = q.popleft()
            for y in BASE_ADJ[x]:
                if y not in d:
                    d[y] = d[x] + 1
                    q.append(y)
        dist0[v] = d
    return dist0[v]


def anchors0(ev):
    gs = ev[1:] if ev[0] == 'R' else ev[1]
    return {AEND[g] for g in gs} | {END0[g] for g in gs}


def ev_dist(e1, e2):
    return min(bfs_from(x)[y] for x in anchors0(e1) for y in anchors0(e2))


def labels(ev):
    return set(ev[1:]) if ev[0] == 'R' else set(ev[1])


print(f"diamond universe: {N} junctions, {M} grains; ice-rule light state (2 in / 2 out at every junction)")
print(f"   local switch moves available in diamond: {len(cand)};  allowed by the electric flux (equal flux on both "
      f"grains): {len(matched)} ({100 * len(matched) / len(cand):.0f}%)")
print(f"   flippable light rings in this state: {len(L_EVENTS)} of {len(HEXES)}")
dE = [eloc(r_partner(END0, SPINS0, e[1], e[2]), e[1], e[2]) - eloc(END0, e[1], e[2]) for e in R_EVENTS[:50]]
print(f"   energy cost of one switch in perfect diamond (rings lost): Delta E = {min(dE):+.0f} .. {max(dE):+.0f} "
      f"(U4 = K6 = 1)\n")

rng = np.random.default_rng(7)

# ================================================================ 1. constraints, unitarity, Gauss law
center = max(range(N), key=lambda v: sum(all(bfs_from(v)[x] <= 3 for x in anchors0(e)) for e in L_EVENTS))
near = lambda ev, r: all(bfs_from(center)[x] <= r for x in anchors0(ev))
R_near = [e for e in R_EVENTS if near(e, 3)]
L_near = [e for e in L_EVENTS if near(e, 3)]
seq = [R_near[i] for i in rng.choice(len(R_near), 10, replace=False)] + \
      [L_near[i] for i in rng.choice(len(L_near), 4, replace=False)]
rng.shuffle(seq)
state = {KEY0: 1.0 + 0j}
for ev in seq:
    state = apply(state, ev)
bad_struct = 0
for (ends, spins) in state:
    deg = np.bincount(ends, minlength=N)[NA:]
    simple = len({(AEND[k], ends[k]) for k in range(M)}) == M
    bad_struct += int(not (np.all(deg == 4) and simple))
gauss = max(max(abs(q) for q in charges(k)) for k in state)
geo = len({k[0] for k in state})
print("1. GEOMETRY EVENTS keep the rules (14 events: 10 switches + 4 light rings, near one junction)")
print(f"   branches of the superposition: {len(state)} ({geo} distinct geometries); norm = {norm(state):.12f}")
print(f"   branches violating 4-grains-per-junction / bipartite / no double links: {bad_struct}")
print(f"   largest Gauss-law violation (electric charge created) in any branch: {gauss}")
# flux-blind switching
R_all_near = [('R',) + c for c in cand if all(bfs_from(center)[x] <= 3 for x in anchors0(('R',) + c))]
seqn = [R_all_near[i] for i in rng.choice(len(R_all_near), 10, replace=False)]
state_n = {KEY0: 1.0 + 0j}
for ev in seqn:
    state_n = apply(state_n, ev, gauge=False)
wbad = sum(abs(v) ** 2 for k, v in state_n.items() if any(q != 0 for q in charges(k)))
print(f"   FLUX-BLIND switches (10 events): weight of branches with created charges = {wbad:.2f}  "
      f"-> geometry may only rewire grains carrying equal electric flux\n")

# ================================================================ 2. reach
nj_R = [footprint(e, KEY0)[2] for e in R_EVENTS[:200]]
print("2. REACH of one geometry event: it reads every junction within 2 steps of its 4 anchor junctions")
print(f"   footprint {np.mean(nj_R):.1f} junctions on average (a light event: 6); it writes only 2 grain ends\n")

# ================================================================ 3. commutation vs footprint overlap
def comm_branch(e1, e2, key):
    s = {key: 1.0 + 0j}
    return diffnorm(apply(apply(s, e1), e2), apply(apply(s, e2), e1))


def sharp_rel(evs, st):
    """ordered pairs (i<j) whose order matters in at least one branch of st"""
    return {(i, j) for i, j in itertools.combinations(range(len(evs)), 2)
            if any(comm_branch(evs[i], evs[j], k) > 1e-12 for k in st)}


print("3. CAUSAL RELATIONS in a superposition of geometries")
stats = defaultdict(list)
sharp = {'order matters in no branch': 0, 'in every branch': 0, 'in SOME branches only': 0}
t3 = time.time()
trials = 0
while trials < 240:
    e1 = R_EVENTS[rng.integers(len(R_EVENTS))]
    pool2 = [e for e in R_EVENTS + L_EVENTS if 1 <= ev_dist(e1, e) <= 4 and not (labels(e) & labels(e1))]
    e2 = pool2[rng.integers(len(pool2))]
    prep = [e for e in R_EVENTS if ev_dist(e, e1) <= 3 or ev_dist(e, e2) <= 3]
    prep = [e for e in prep if not (labels(e) & (labels(e1) | labels(e2)))]
    st = {KEY0: 1.0 + 0j}
    for i in rng.choice(len(prep), min(3, len(prep)), replace=False):
        st = apply(st, prep[i])
    cf = [conflict(e1, e2, k) for k in st]
    cls = 'never' if not any(cf) else ('always' if all(cf) else 'in some branches')
    d = diffnorm(apply(apply(st, e1), e2), apply(apply(st, e2), e1))
    stats[cls].append(d)
    if len(st) > 1:
        db = [comm_branch(e1, e2, k) > 1e-12 for k in st]
        sharp[('order matters in no branch', 'in every branch', 'in SOME branches only')[
            0 if not any(db) else (1 if all(db) else 2)]] += 1
    trials += 1
print("   (a) footprint = everything an event reads or writes (a conservative light cone):")
for cls in ('never', 'always', 'in some branches'):
    v = np.array(stats[cls])
    if len(v):
        print(f"       footprints overlap {cls:17s}: {len(v):4d} pairs; order matters in {np.sum(v > 1e-12):4d}; "
              f"max |E1E2 - E2E1|psi = {v.max():.1e}")
print("   (b) branch by branch (pairs acting on a superposition of >1 geometry):")
for k_, v_ in sharp.items():
    print(f"       {k_:28s}: {v_:4d} pairs")
print(f"   ({time.time() - t3:.0f} s)\n")

# ================================================================ 4. slicing independence
print("4. SLICING INDEPENDENCE with geometry changing under the events")
t4 = time.time()
def closure(rel):
    c = set(rel)
    while True:
        add = {(i, l) for (i, j) in c for (k, l) in c if j == k} - c
        if not add:
            return c
        c |= add


best, fallback, tried = None, None, 0
for attempt in range(400):
    c0 = R_EVENTS[rng.integers(len(R_EVENTS))]
    clus = [e for e in R_EVENTS + L_EVENTS if ev_dist(e, c0) <= 3]
    rng.shuffle(clus)
    chosen, labs = [], set()
    for e in clus:
        if not (labels(e) & labs):
            chosen.append(e)
            labs |= labels(e)
        if len(chosen) == 8:
            break
    if len(chosen) < 8:
        continue
    prep = [e for e in R_EVENTS if ev_dist(e, c0) <= 3 and not (labels(e) & labs)]
    if len(prep) < 2:
        continue
    psi0 = {KEY0: 1.0 + 0j}
    for i in rng.choice(len(prep), 2, replace=False):
        psi0 = apply(psi0, prep[i])
    if len({k[0] for k in psi0}) < 2:
        continue
    tried += 1
    bg_sharp = sharp_rel(chosen, {KEY0: 1})               # where order matters in the classical diamond
    q_sharp = sharp_rel(chosen, psi0)                     # ... in some branch of the actual quantum geometry
    if fallback is None and 4 <= len(bg_sharp) <= 16:
        fallback = (chosen, psi0, bg_sharp, q_sharp)
    if q_sharp - closure(bg_sharp) and len(bg_sharp) <= 16:
        best = (chosen, psi0, bg_sharp, q_sharp)
        break
found = best is not None
chosen, psi0, bg_sharp, q_sharp = best if found else fallback
print(f"   causal links present only in the quantum geometry (not implied by the diamond's): "
      f"{sorted(q_sharp - closure(bg_sharp))}")
lab_rel = set()                                           # never related by grain labels (all distinct)
light_rel = {(i, j) for i, j in itertools.combinations(range(8), 2) if any(conflict(chosen[i], chosen[j], k)
                                                                            for k in psi0)}
K = len(chosen)
print(f"   searched {tried} neighbourhoods; one where the quantum geometry adds a causal link the classical diamond "
      f"does not imply: {'FOUND' if found else 'none found (using a typical one)'}")


def run(order):
    s = psi0
    for i in order:
        s = apply(s, chosen[i])
    return s


def random_order(rel, r):
    done, out = set(), []
    while len(out) < K:
        ready = [i for i in range(K) if i not in done and all(j in done for j in range(i) if (j, i) in rel)]
        i = ready[r.integers(len(ready))]
        done.add(i)
        out.append(i)
    return out


def run_collect(order, rel):
    """run an order; add every pending pair whose order matters on any intermediate state"""
    s = psi0
    pending = set(range(K))
    new = set()
    for i in order:
        for a, b in itertools.combinations(sorted(pending), 2):
            if (a, b) not in rel and (a, b) not in new and \
                    diffnorm(apply(apply(s, chosen[a]), chosen[b]), apply(apply(s, chosen[b]), chosen[a])) > 1e-12:
                new.add((a, b))
        s = apply(s, chosen[i])
        pending.discard(i)
    return s, new


ref = run(list(range(K)))
sc_rel = set(q_sharp)
quiet = 0
while quiet < 12:
    _, new = run_collect(random_order(sc_rel, rng), sc_rel)
    if new:
        sc_rel |= new
        quiet = 0
    else:
        quiet += 1
print(f"   8 events (switches and light rings, all different grains) in one neighbourhood, acting on a superposition "
      f"of {len({k[0] for k in psi0})} geometries")
for name, rel in (("grain labels only (old rule)", lab_rel),
                  ("footprints (conservative light cone)", light_rel),
                  ("classical diamond: where order matters", bg_sharp),
                  ("self-consistent: where order matters in the state", sc_rel)):
    orders = {tuple(random_order(rel, rng)) for _ in range(150)}
    d = max(diffnorm(run(list(o)), ref) for o in orders)
    print(f"   causal order from {name:42s}: {len(rel):2d} ordered pairs, {len(orders):3d} distinct orders -> "
          f"max state difference {d:.1e}")
print(f"   ({time.time() - t4:.0f} s)")
print(f"\ntotal {time.time() - T0:.0f} s")
