import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.pyplot import figure

from visualize.helper import add_z_down, add_z_up, add_z_mid, create_arrow


def visualize_3d_polygon(polygon, axe):
    face_list = [list(map(add_z_down, polygon)), list(map(add_z_up, polygon))]
    for i in range(len(polygon)):
        face_list.append(
            [add_z_down(polygon[i]), add_z_up(polygon[i]), add_z_up(polygon[i - 1]), add_z_down(polygon[i - 1])])
    faces = Poly3DCollection(face_list, linewidths=1, edgecolors='k')
    faces.set_facecolor((0, 0, 1, 0.1))
    axe.add_collection3d(faces)

    point_list = []
    point_list += list(map(add_z_down, polygon))
    point_list += list(map(add_z_up, polygon))

    def get_list(k):
        return [point[k] for point in point_list]

    axe.scatter(get_list(0), get_list(1), get_list(2), s=0)


def visualize(polygon_list, point_list, waiting_point_list):
    """
    Visualize results

    :param polygon_list: list of polygons, each of which is represented as a Nx2 array, where N is the number of
    vertices in that polygon
    :param point_list: list of points in the found path, with point_list[0] being the starting point, point_list[-1]
    being the goal
    :param waiting_point_list: list of waiting points
    :return: None
    """
    figure(num=None, figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')
    plt.rcParams["figure.figsize"] = (10, 10)

    fig = plt.figure()
    axe = fig.add_subplot(111, projection="3d")

    for polygon in polygon_list:
        visualize_3d_polygon(polygon, axe)

    # Display the path's 2 endpoints
    axe.scatter(point_list[0][0], point_list[0][1], 0, s=250, label="Starting point")
    axe.scatter(point_list[-1][0], point_list[-1][1], 0, s=250, label="Goal")
    axe.scatter(
        np.array(waiting_point_list)[:, 0],
        np.array(waiting_point_list)[:, 1],
        [0] * len(waiting_point_list),
        s=150, label="Waiting point"
    )

    # Display arrows depicting the found path
    for i in range(1, len(point_list)):
        a = add_z_mid(point_list[i - 1])
        b = add_z_mid(point_list[i])
        axe.add_artist(create_arrow(a, b, mutation_scale=20, lw=3, arrowstyle="-|>", color="r"))

    plt.legend()
    plt.show()
