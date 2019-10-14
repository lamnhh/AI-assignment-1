import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.pyplot import figure


def visualize(polygon_list, s_point, t_point, waiting_point_list, bound_x, bound_y):
    """
    Visualize results

    :param polygon_list: list of polygons, each of which is represented as a Nx2 array, where N is the number of
    vertices in that polygon
    :param s_point: starting point
    :param t_point: ending point
    :param waiting_point_list: list of waiting points
    :param bound_x: x-limit of all points
    :param bound_y: y-limit of all points
    :return: None
    """
    figure(num=None, figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')
    plt.rcParams["figure.figsize"] = (10, 10)
    ax = plt.axes(xlim=(0, bound_x), ylim=(0, bound_y))

    patches = []
    for polygon in polygon_list:
        polygon = Polygon(np.array(polygon), True)
        patches.append(polygon)

    plt.scatter(s_point[0], s_point[1], s=250, label="Starting point")
    plt.scatter(t_point[0], t_point[1], s=250, label="Goal")
    plt.scatter(np.array(waiting_point_list)[:, 0], np.array(waiting_point_list)[:, 1], s=125, label="Waiting points")

    # Display input polygons
    p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)
    colors = 100 * np.random.rand(len(patches))
    p.set_array(np.array(colors))
    ax.add_collection(p)

    plt.legend()
    plt.show()
