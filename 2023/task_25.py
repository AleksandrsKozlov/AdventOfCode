from measure_time import run_with_measurment
from networkx import Graph, minimum_edge_cut, connected_components
from math import prod

def get_input():
    lines = open("2023/inputs/task25.txt").read().split("\n")
    graph = Graph()
    for line in lines:
        name, connections = line.split(": ")
        for connection in connections.split():
            graph.add_edge(name, connection)
    return graph


def part_one(graph: Graph):
    edges_to_remove = minimum_edge_cut(graph)
    graph.remove_edges_from(edges_to_remove)
    component_groups = connected_components(graph)
    return prod(len(group) for group in component_groups)


if __name__ == '__main__':
    graph = run_with_measurment(get_input)
    run_with_measurment(part_one, graph=graph, print_result=True)