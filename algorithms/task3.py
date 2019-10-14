def __dijkstra(graph):
    n = graph.get_total_vertex_count()
    cost = [[1e9] * n for i in range(n)]
    prev = [[-1] * n for i in range(n)]

    for s in range(graph.extra_point_count + 2):
        free = [True] * n
        cost[s][s] = 0
        for z in range(n):
            u = -1
            for i in range(n):
                if free[i] and (u == -1 or cost[s][u] > cost[s][i]):
                    u = i
            if u == -1:
                break
            free[u] = False
            for v in range(n):
                if free[v] and cost[s][v] > cost[s][u] + graph.cost[u][v]:
                    cost[s][v] = cost[s][u] + graph.cost[u][v]
                    prev[s][v] = u
    return cost, prev


def __trace(s, t, prev):
    path = []
    while t != s:
        path.append(t)
        t = prev[s][t]
    return path


def t3_dp(graph):
    n = graph.extra_point_count + 2
    s = graph.s
    t = graph.t

    dp = [[1e9] * n for i in range(1 << n)]
    pr = [[-1] * n for i in range(1 << n)]
    dp[1 << s][s] = 0
    pr[1 << s][s] = -2

    cost, prev = __dijkstra(graph)

    for mask in range(1 << n):
        for u in range(n):
            if (mask >> u & 1) == 0:
                continue
            for v in range(n):
                if (mask >> v & 1) == 1:
                    continue
                next_mask = mask | (1 << v)
                if dp[next_mask][v] > dp[mask][u] + cost[u][v]:
                    dp[next_mask][v] = dp[mask][u] + cost[u][v]
                    pr[next_mask][v] = u

    end_mask = (1 << n) - 1
    if pr[end_mask][t] == -1:
        return False, []

    path = []
    while t != s:
        p = pr[end_mask][t]
        path += __trace(p, t, prev)
        end_mask = end_mask - (1 << t)
        t = p
    path.append(s)
    path = list(reversed(path))
    return True, path


def t3_greedy(graph):
    n = graph.extra_point_count + 2
    s = graph.s
    t = graph.t

    cost, prev = __dijkstra(graph)
    free = [True] * n

    path = [s]
    free[s] = False
    for z in range(n - 2):
        nxt = -1
        u = path[-1]
        for v in range(n - 1):
            if free[v] and (nxt == -1 or cost[u][v] < cost[u][nxt]):
                nxt = v
        free[nxt] = False
        path += list(reversed(__trace(u, nxt, prev)))
    path += list(reversed(__trace(path[-1], t, prev)))
    return True, path
