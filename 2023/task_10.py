from measure_time import run_with_measurment
import numpy as np
from matplotlib.path import Path
from shapely.geometry import Point, Polygon

def get_input():
    lines = open("2023/inputs/task10.txt").read().split("\n")
    return lines

def get_first_connection(start: tuple[int, int], labyrinth: np.ndarray):
    x, y = start

    if labyrinth[x-1][y] in ["|", "7", "F"]:
        return (labyrinth[x-1][y], x-1, y, x, y)
    if labyrinth[x+1][y] in ["|", "J", "L"]:
        return (labyrinth[x+1][y], x+1, y, x, y)
    
    if labyrinth[x][y-1] in ["-", "L", "F"]:
        return (labyrinth[x][y-1], x, y-1, x, y)
    if labyrinth[x][y+1] in ["-", "7", "J"]:
        return (labyrinth[x][y+1], x, y+1, x, y)

def get_next_connection(start: tuple[str, int, int], labyrinth: np.ndarray):
    shape, x, y, prev_x, prev_y = start
    up = (x-1, y)
    down = (x+1, y)
    left = (x, y-1)
    right = (x, y+1)
    if shape == "|":
        coords_to_check = [up, down]
    if shape == "-":
        coords_to_check = [left, right]
    if shape == "7":
        coords_to_check = [left, down]
    if shape == "F":
        coords_to_check = [right, down]
    if shape == "L":
        coords_to_check = [right, up]
    if shape == "J":
        coords_to_check = [left, up]
    coords_to_check = [coord for coord in coords_to_check if coord != (prev_x, prev_y)][0]
    return (labyrinth[coords_to_check], coords_to_check[0], coords_to_check[1], x, y)

def part_one(lines: list[str]):
    labyrinth = np.array([[char for char in line] for line in lines])
    labyrinth = np.pad(labyrinth, pad_width=1, constant_values=".")
    start = np.where(labyrinth == "S")[0].base[0]
    current = get_first_connection(start, labyrinth)
    steps = 1
    contour_points = [(start[0], start[1])]
    while current[0] != "S":
        contour_points.append((current[1], current[2]))
        current = get_next_connection(current, labyrinth)
        steps += 1
    contour_points.append((start[0], start[1]))
    print(f"Part 1, Steps: {steps//2}")
    return contour_points, labyrinth

def part_two(contour_points: list[tuple[int,int]], labyrinth: np.ndarray):
    polygon = Polygon(contour_points)
    tiles = 0
    for x, line in enumerate(labyrinth):
        for y in range(len(line)):
            point = Point(x,y)
            if polygon.contains(point):
                tiles += 1
    return tiles


if __name__ == '__main__':
    lines = run_with_measurment(get_input)
    contour_points, labyrinth = run_with_measurment(part_one, lines=lines)
    contour_points = run_with_measurment(part_two, contour_points=contour_points, labyrinth=labyrinth, print_result=True)