import math

from utils import does_intersect_with_polygon
from visualize import visualize2d, visualize3d


class Graph:
    def __init__(self, polygon_list, start, end, extra_point_list):
        self.polygon_list = polygon_list

        # Extract all polygons vertices.
        self.point_list = []
        self.point_list += extra_point_list
        self.point_list += [start, end]
        self.s = len(self.point_list) - 2
        self.t = len(self.point_list) - 1
        self.point_list += sum(polygon_list, [])

        self.extra_point_count = len(extra_point_list)

        n = len(self.point_list)
        self.cost = [[0] * n for i in range(n)]
        self.compute_graph_cost()

    def compute_graph_cost(self):
        n = len(self.point_list)
        for u in range(n):
            for v in range(n):
                self.cost[u][v] = self.get_weight(self.point_list[u], self.point_list[v])

    def get_total_vertex_count(self):
        return len(self.point_list)

    def get_weight(self, u, v):
        """
        Compute weight for a single edge (u, v)

        :param u: 1st endpoint of edge.
        :param v: 2nd endpoint of edge.
        :return: weight of this edge or 1e9 if this edge does not exist.
        """
        for polygon in self.polygon_list:
            if does_intersect_with_polygon(u, v, polygon):
                return 1e9

        return math.sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2)

    def visualize_with(self, algorithm, visualize, bound_x, bound_y):
        reachable, path = algorithm(self)
        if reachable:
            path = list(map(lambda i: self.point_list[i], path))
            print(path)
            if visualize == "2d":
                visualize2d(self.polygon_list, path, self.point_list[0:self.extra_point_count], bound_x, bound_y)
            else:
                visualize3d(self.polygon_list, path, self.point_list[0:self.extra_point_count])
