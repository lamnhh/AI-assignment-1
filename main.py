import argparse

from algorithms.a_star import a_star
from algorithms.ucs import ucs
from algorithms.task3 import t3_dp, t3_greedy
from algorithms.greedy import greedy
from visualize import visualize_input
from graph import Graph
from utils import read_input

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=None, help="Path to input file, ignore for standard input")
    parser.add_argument("--algorithm", help="Algorithm to run (ucs, greedy, a_star, t3_greedy: greedy algorithm "
                                            "for task 3, t3_dp: dynamic programming algorithm for task 3)")
    parser.add_argument("--visualize", default="2d", help="2d/3d")
    args = parser.parse_args()

    if args.algorithm == "ucs":
        algorithm = ucs
    elif args.algorithm == "greedy":
        algorithm = greedy
    elif args.algorithm == "a_star":
        algorithm = a_star
    elif args.algorithm == "t3_greedy":
        algorithm = t3_greedy
    elif args.algorithm == "t3_dp":
        algorithm = t3_dp
    else:
        raise ValueError(args.algorithm + " is not an acceptable algorithm")

    if args.visualize == "2d":
        visualize = "2d"
    elif args.visualize == "3d":
        visualize = "3d"
    else:
        raise ValueError(args.visualize + " is not an acceptable visualisation option")

    bound_x, bound_y, s_point, t_point, polygon_list, extra_point_list = read_input(args.input)
    visualize_input(polygon_list, s_point, t_point, extra_point_list, bound_x, bound_y)
    graph = Graph(polygon_list, s_point, t_point, extra_point_list)
    graph.visualize_with(algorithm, visualize, bound_x, bound_y)
