from measure_time import run_with_measurment
import math
from multiprocessing import Pool

def get_input():
    lines = open("2023/inputs/task8.txt").read().split("\n")
    path = lines[0]
    path = [int(char == "R") for char in path]
    path_map = {}
    start_nodes = []
    for line in lines[2:]:
        split_line = line.split("=")
        key = split_line[0].rstrip()
        coordinates = split_line[1].strip(" ").split(",")
        path_map[key] = (coordinates[0][1:], coordinates[1][-4:-1])
        if key[-1] == "A":
            start_nodes.append(key)
    return path, path_map, start_nodes

def go_path(path: list[int], path_map: dict[str, tuple[str, str]], start_node: str, end_condition = None):
    idx = 0
    steps = 0
    path_length = len(path)
    if end_condition is None:
        end_condition = lambda node: node[-1] == "Z"
    while not end_condition(start_node):
        path_turn = path[idx]
        start_node = path_map[start_node][path_turn]
        idx += 1
        steps += 1
        if idx == path_length:
            idx = 0
    return steps

def part_one(path: list[int], path_map: dict[str, tuple[str, str]]):
    start_node = "AAA"
    end_condition = lambda node: node == "ZZZ"
    return go_path(path, path_map, start_node, end_condition)


def part_two(path: list[int], path_map: dict[str, tuple[str, str]], start_nodes: list[str]):
    end_condition = lambda node: node[-1] == "Z"
    all_steps = [go_path(path, path_map, start_node, end_condition) for start_node in start_nodes]
    return math.lcm(*all_steps)

def part_two_parallel(path: list[int], path_map: dict[str, tuple[str, str]], start_nodes: list[str]):
    pool_args = [(path, path_map, start_node) for start_node in start_nodes]
    all_steps = []
    with Pool() as pool:
        for result in pool.starmap(go_path, pool_args):
            all_steps.append(result)
    return math.lcm(*all_steps)

if __name__ == '__main__':
    path, path_map, start_nodes = run_with_measurment(get_input)
    run_with_measurment(part_one, print_result=True, path=path, path_map=path_map)
    run_with_measurment(part_two, print_result=True, path=path, path_map=path_map, start_nodes=start_nodes)
    run_with_measurment(part_two_parallel, print_result=True, path=path, path_map=path_map, start_nodes=start_nodes)