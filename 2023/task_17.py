from measure_time import run_with_measurment
import numpy as np
import networkx as nx
from networkx.algorithms.shortest_paths.weighted import single_source_dijkstra_path_length


def get_input():
    lines = open("2023/inputs/task17.txt").read().split("\n")
    lines = list(map(list, lines))
    blocks = np.array(lines).astype(np.int8)
    return blocks


def add_vertices_to_graph(coords: tuple, blocks: np.ndarray, graph: nx.Graph, min_steps: int, max_steps: int):
    x, y = coords
    length, width = blocks.shape
    weight_reduction = blocks[x,y]
    for i in range(1, max_steps + 1):
        if y + i < width:
            new_x = x
            new_y = y + i
            weight = sum(blocks[x, y:new_y + 1]) - weight_reduction
            for j in range(min_steps, max_steps + 1):
                graph.add_edge(f"{x}_{y}_U_{j}", f"{new_x}_{new_y}_R_{i}", weight=weight)
                graph.add_edge(f"{x}_{y}_D_{j}", f"{new_x}_{new_y}_R_{i}", weight=weight)
            for j in range(max_steps - i, 0, -1):
                graph.add_edge(f"{x}_{y}_R_{j}", f"{new_x}_{new_y}_R_{i + j}", weight=weight)
        if y - i >= 0:
            new_x = x
            new_y = y - i
            weight = sum(blocks[x, new_y:y+1]) - weight_reduction
            for j in range(min_steps, max_steps + 1):
                graph.add_edge(f"{x}_{y}_U_{j}", f"{new_x}_{new_y}_L_{i}", weight=weight)
                graph.add_edge(f"{x}_{y}_D_{j}", f"{new_x}_{new_y}_L_{i}", weight=weight)
            for j in range(max_steps - i, 0, -1):
                graph.add_edge(f"{x}_{y}_L_{j}", f"{new_x}_{new_y}_L_{i + j}", weight=weight)
        if x - i >= 0:
            new_x = x - i
            new_y = y
            weight = sum(blocks[new_x:x+1, y]) - weight_reduction
            for j in range(min_steps, max_steps + 1):
                graph.add_edge(f"{x}_{y}_L_{j}", f"{new_x}_{new_y}_U_{i}", weight=weight)
                graph.add_edge(f"{x}_{y}_R_{j}", f"{new_x}_{new_y}_U_{i}", weight=weight)
            for j in range(max_steps - i, 0, -1):
                graph.add_edge(f"{x}_{y}_U_{j}", f"{new_x}_{new_y}_U_{i + j}", weight=weight)
        if x + i < length:
            new_x = x + i
            new_y = y
            weight = sum(blocks[x:new_x+1, y]) - weight_reduction
            for j in range(min_steps, max_steps + 1):
                graph.add_edge(f"{x}_{y}_L_{j}", f"{new_x}_{new_y}_D_{i}", weight=weight)
                graph.add_edge(f"{x}_{y}_R_{j}", f"{new_x}_{new_y}_D_{i}", weight=weight)
            for j in range(max_steps - i, 0, -1):
                graph.add_edge(f"{x}_{y}_D_{j}", f"{new_x}_{new_y}_D_{i + j}", weight=weight)


def count_heap_loss(blocks: np.ndarray, min_steps: int, max_steps: int):
    length, width = blocks.shape
    graph = nx.DiGraph()
    for x in range(length):
        for y in range(width):
            add_vertices_to_graph((x,y), blocks, graph, min_steps=min_steps, max_steps=max_steps)

    path = single_source_dijkstra_path_length(graph, "0_0_R_1")
    
    heap_losses_at_destination = []
    for destination, heap_loss in path.items():
        x, y, _, steps = tuple(destination.split("_"))
        if int(x) == length - 1 and int(y) == width - 1 and int(steps) >= min_steps:
            heap_losses_at_destination.append(heap_loss)
    min_heap_loss = min(heap_losses_at_destination)
    return min_heap_loss


def part_one(blocks: np.ndarray):
    return count_heap_loss(blocks, min_steps=1, max_steps=3)


def part_two(blocks: np.ndarray):
    return count_heap_loss(blocks, min_steps=4, max_steps=10)


if __name__ == '__main__':
    blocks = run_with_measurment(get_input)
    run_with_measurment(part_one, blocks=blocks, print_result=True)
    run_with_measurment(part_two, blocks=blocks, print_result=True)