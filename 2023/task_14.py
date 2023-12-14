from copy import deepcopy
import numpy as np
from measure_time import run_with_measurment


def get_input():
    lines = open("2023/inputs/task14.txt").read().split("\n")
    lines = list(map(list, lines))
    stone_field = np.array(lines)
    return stone_field


def tilt(stone_field: np.ndarray, direction: str):
    length = len(stone_field[:,0]) if direction == "N" or direction == "S" else len(stone_field[0,:])
    for x in range(length):
        line = stone_field[:,x] if direction == "N" or direction == "S" else stone_field[x,:]
        line = line[::-1] if direction == "S" or direction == "E" else line
        new_position = 0
        for y, field in enumerate(line):
            if field == "#":
                new_position = y + 1
            if field == "O":
                line[new_position] = "O"
                if new_position != y:
                    line[y] = "."
                new_position += 1
        if direction == "S":
            stone_field[:,x] = line[::-1]
        if direction == "E":
            stone_field[x,:] = line[::-1]
        if direction == "N":
            stone_field[:,x] = line
        if direction == "W":
            stone_field[x,:] = line

    return stone_field


def count_points(arr: np.ndarray):
    max_points = len(arr[:,0])
    points = 0
    for idx, line in enumerate(arr):
        stones = sum(1 for el in line if el == "O")
        points += stones * (max_points - idx)
    return points


def cycle(stone_field: np.ndarray):
    directions = ["N", "W", "S", "E"]
    cycle_points = []
    for direction in directions:
        stone_field = tilt(stone_field, direction)
        points = count_points(stone_field)
        cycle_points.append(points)
    return stone_field, cycle_points


def part_one(stone_field: np.ndarray):
    tilted_field = tilt(stone_field, direction="N")
    return count_points(tilted_field)


def part_two(stone_field: np.ndarray, cycles: int):
    all_results = []
    for _ in range(cycles):
        stone_field, cycle_points = cycle(stone_field)
        if cycle_points in all_results:
            cycle_start = all_results.index(cycle_points)
            cycle_length = len(all_results) - cycle_start
            answer_index = (1000000000 - cycle_start) % cycle_length
            print(f"Cycle start: {cycle_start}")
            print(f"Cycle length: {cycle_length}")
            return all_results[answer_index + cycle_start - 1][-1]
        else:
            all_results.append(cycle_points)


if __name__ == '__main__':
    stone_field = run_with_measurment(get_input)
    run_with_measurment(part_one, stone_field=deepcopy(stone_field), print_result=True)
    run_with_measurment(part_two, stone_field=stone_field, cycles=1000000000, print_result=True)