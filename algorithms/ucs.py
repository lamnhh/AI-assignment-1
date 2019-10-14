from heapq import heappush, heappop


def ucs(graph):
    n = graph.get_total_vertex_count()
    s = graph.s
    t = graph.t
    cost = graph.cost

    pq = []
    dist = [1e9] * n
    prev = [-1] * n
    closed = [False] * n

    dist[s] = 0
    prev[s] = -2
    heappush(pq, (0, s))

    while len(pq) > 0:
        d_u, u = heappop(pq)
        if d_u > dist[u]:
            continue
        if u == t:
            break
        closed[u] = True
        for v in range(n):
            if not closed[v] and dist[v] > dist[u] + cost[u][v]:
                dist[v] = dist[u] + cost[u][v]
                prev[v] = u
                heappush(pq, (dist[v], v))

    if prev[t] == -1:
        return False, []

    path = []
    v = t
    while v != -2:
        path.append(v)
        v = prev[v]

    path.reverse()
    return True, path
