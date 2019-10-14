from utils import heuristic
from heapq import heappush, heappop


def a_star(graph):
    n = graph.get_total_vertex_count()
    s = graph.s
    t = graph.t
    cost = graph.cost

    pq = []
    f = [1e9] * n
    g = [1e9] * n
    h = heuristic(graph.point_list, graph.point_list[t])
    p = [-1] * n
    closed = [False] * n

    g[s] = 0
    f[s] = g[s] + h[s]
    p[s] = -2
    heappush(pq, (f[s], s))

    while len(pq) > 0 and f[t] >= pq[0][0]:
        f_u, u = heappop(pq)
        if f_u > f[u]:
            continue
        closed[u] = True
        for v in range(n):
            if closed[v]:
                continue
            g[v] = min(g[v], g[u] + cost[u][v])
            if f[v] > g[v] + h[v]:
                f[v] = g[v] + h[v]
                p[v] = u
                heappush(pq, (f[v], v))

    if p[t] == -1:
        return False, []

    path = []
    v = t
    while v != -2:
        path.append(v)
        v = p[v]

    path.reverse()
    return True, path
