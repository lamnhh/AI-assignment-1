from operator import itemgetter
from utils import heuristic


def greedy(graph):
    n = graph.get_total_vertex_count()
    s = graph.s
    t = graph.t
    cost = graph.cost
    h_list = heuristic(graph.point_list, graph.point_list[t])

    path = [s]
    p_remain = list(range(1, n))

    while path[-1] != t:
        u = path[-1]
        next_vertices = []

        check = False
        for v in range(n):
            if cost[u][v] < 1e9 and v in p_remain:
                next_vertices.append(h_list[v])
                check = True
            else:
                next_vertices.append(1e9)

        if not check:
            return False, []

        u = min(enumerate(next_vertices), key=itemgetter(1))[0]
        p_remain.remove(u)
        path.append(u)

    return True, path
