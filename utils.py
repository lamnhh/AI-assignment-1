import math
import sys
from shapely.geometry import LineString


def read_input(file_path):
    f = sys.stdin if file_path is None else open(file_path, "r")

    def read():
        return list(map(float, f.readline().split(",")))

    bound_x, bound_y = read()
    _ = read()
    s_point = [_[0], _[1]]
    t_point = [_[2], _[3]]

    polygon_count = int(f.readline())
    polygon_list = []
    for z in range(polygon_count):
        arr = read()
        polygon = []
        for i in range(0, len(arr), 2):
            polygon.append([arr[i], arr[i + 1]])
        polygon_list.append(polygon)

    extra_point_count = int(f.readline())
    extra_point_list = []
    for i in range(extra_point_count):
        point = read()
        extra_point_list.append(point)

    f.close()
    return bound_x, bound_y, s_point, t_point, polygon_list, extra_point_list


def does_intersect_with_polygon(u, v, polygon):
    """
    Check whether segment (u, v) intersects with a given polygon.

    :param u: 1st endpoint of segment.
    :param v: 2nd endpoint of segment.
    :param polygon: polygon to be checked for intersection.
    :return: True/False <=> intersect/not intersect.
    """
    index_u = -2
    index_v = -2

    for i in range(len(polygon)):
        if u == polygon[i]:
            index_u = i
        if v == polygon[i]:
            index_v = i

    # Ignore case when (u, v) form an edge of given polygon.
    if index_u != -2 and index_v != -2:
        return abs(index_u - index_v) != 1 and (min(index_u, index_v) + len(polygon) - max(index_u, index_v)) != 1

    a = LineString([u, v])
    for i in range(len(polygon)):
        b = LineString([polygon[i - 1], polygon[i]])
        if u != polygon[i - 1] and v != polygon[i - 1] and u != polygon[i] and v != polygon[i] and a.intersects(b):
            return True

    return False


def heuristic(point_list, end):
    """
    Compute Heuristic Function h(x) = Euclidean distance between node x and goal point.

    :param point_list: list of points to compute.
    :param end: goal point.
    :return: list of heuristic values.
    """
    h_list = []
    for point in point_list:
        h_value = math.sqrt((end[0] - point[0]) ** 2 + (end[1] - point[1]) ** 2)
        h_list.append(h_value)
    return h_list
