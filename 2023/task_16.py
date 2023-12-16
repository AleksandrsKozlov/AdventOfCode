from measure_time import run_with_measurment
import numpy as np

def get_input():
    lines = open("2023/inputs/task16.txt").read().split("\n")
    lines = list(map(list, lines))
    tiles = np.array(lines)
    return tiles


def move_light(from_coords: tuple, coords: tuple, tiles: np.ndarray, energy_tiles: np.ndarray, movement_map: list[tuple]):
    from_x, from_y = from_coords
    x,y = coords
    length, width = tiles.shape

    if from_coords + coords in movement_map:
        return []
    if x < 0 or x >= length or y < 0 or y >= width:
        return []
    
    energy_tiles[x,y] = 1
    next_straight_coords = (x + x - from_x, y + y - from_y)

    movement_map.append(from_coords + coords)

    if tiles[x,y] == ".":
        return [(coords, next_straight_coords)]
    if tiles[x,y] == "-":
        if y == from_y:
            return [(coords, (x, y - 1)), (coords, (x, y + 1))]
        else:
            return [(coords, next_straight_coords)]
    if tiles[x,y] == "|":
        if x == from_x:
            return [(coords, (x - 1, y)), (coords, (x + 1, y))]
        else:
            return [(coords, next_straight_coords)]
    if tiles[x,y] == "\\":
        if x < from_x:
            return [(coords, (x, y - 1))]
        if x > from_x:
            return [(coords, (x, y + 1))]
        if y > from_y:
            return [(coords, (x + 1, y))]
        if y < from_y:
            return [(coords, (x - 1, y))]
    if tiles[x,y] == "/":
        if x < from_x:
            return [(coords, (x, y + 1))]
        if x > from_x:
            return [(coords, (x, y - 1))]
        if y > from_y:
            return [(coords, (x - 1, y))]
        if y < from_y:
            return [(coords, (x + 1, y))]


def energize_field(first_move: tuple[tuple], tiles: np.ndarray):
    movement_map = []
    energy_tiles = np.zeros(tiles.shape)
    from_coords, coords = first_move
    current_inputs = move_light(from_coords, coords, tiles, energy_tiles, movement_map)
    while len(current_inputs) > 0:
        next_inputs = []
        for from_coords, coords in current_inputs:
            next_inputs.extend(move_light(from_coords, coords, tiles, energy_tiles, movement_map))
        current_inputs = next_inputs
    
    return sum(sum(energy_tiles))


def part_one(tiles: np.ndarray):
    first_move = ((0,-1), (0,0))
    return energize_field(first_move, tiles)


def part_two(tiles: np.ndarray):
    length, width = tiles.shape
    energy_results = []
    for i in range(length):
        first_move_left = ((i,-1), (i,0))
        first_move_right = ((i,width), (i,width-1))
        energy_results.append(energize_field(first_move_left, tiles))
        energy_results.append(energize_field(first_move_right, tiles))
    for i in range(width):
        first_move_up = ((-1,i), (0,i))
        first_move_down = ((width,i), (width-1,i))
        energy_results.append(energize_field(first_move_up, tiles))
        energy_results.append(energize_field(first_move_down, tiles))
    return max(energy_results)


if __name__ == '__main__':
    tiles = run_with_measurment(get_input)
    run_with_measurment(part_one, tiles=tiles, print_result=True)
    run_with_measurment(part_two, tiles=tiles, print_result=True)