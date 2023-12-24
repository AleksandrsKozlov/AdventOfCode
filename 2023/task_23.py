from measure_time import run_with_measurment
import networkx as nx
from networkx.classes.function import path_weight


def get_input():
    labyrinth = open("2023/inputs/task23.txt").read().split("\n")
    return labyrinth


def part_one(labyrinth: list[str]):
    graph = nx.DiGraph()
    length = len(labyrinth)
    width = len(labyrinth[0])
    start_position = (0,0)
    end_position = (0,0)
    for x, line in enumerate(labyrinth):
        for y, tile in enumerate(line):
            if tile == "#":
                continue
            if x == 0:
                start_position = (x,y)
            if x == length - 1:
                end_position = (x,y)
            if x + 1 < length and labyrinth[x][y] in [".", "v"]:
                new_x = x + 1
                new_y = y
                if labyrinth[new_x][new_y] != "#":
                    graph.add_edge(f"{x}_{y}", f"{new_x}_{new_y}", weight=1)
            if x - 1 >= 0 and labyrinth[x][y] in [".", "^"]:
                new_x = x - 1
                new_y = y
                if labyrinth[new_x][new_y] != "#":
                    graph.add_edge(f"{x}_{y}", f"{new_x}_{new_y}", weight=1)
            if y - 1 >= 0 and labyrinth[x][y] in [".", "<"]:
                new_x = x
                new_y = y - 1
                if labyrinth[new_x][new_y] != "#":
                    graph.add_edge(f"{x}_{y}", f"{new_x}_{new_y}", weight=1)
            if y + 1 < width and labyrinth[x][y] in [".", ">"]:
                new_x = x
                new_y = y + 1
                if labyrinth[new_x][new_y] != "#":
                    graph.add_edge(f"{x}_{y}", f"{new_x}_{new_y}", weight=1)

    all_paths = nx.all_simple_edge_paths(graph, f"{start_position[0]}_{start_position[1]}", f"{end_position[0]}_{end_position[1]}")
    return max(len(path) for path in all_paths)

def part_two(labyrinth: list[str]):
    length = len(labyrinth)
    width = len(labyrinth[0])
    graph = nx.grid_2d_graph(length, width)
    for x, line in enumerate(labyrinth):
        for y, tile in enumerate(line):
            node = (x, y)
            if tile == "#":
                graph.remove_node(node)

    nodes_two_neighbors = [node for node in graph.nodes if len(graph.edges(node)) == 2]

    for node in nodes_two_neighbors:
        left_node, right_node = list(graph.neighbors(node))
        weight = sum(graph.edges[node, node_dir].get("weight", 1) for node_dir in (left_node, right_node))
        graph.add_edge(left_node, right_node, weight=weight)
        graph.remove_node(node)
    
    return max(path_weight(graph, path, "weight") for path in nx.all_simple_paths(graph, (0,1), (length-1, width-2)))


if __name__ == '__main__':
    labyrinth = run_with_measurment(get_input)
    run_with_measurment(part_one, labyrinth=labyrinth, print_result=True)
    run_with_measurment(part_two, labyrinth=labyrinth, print_result=True)