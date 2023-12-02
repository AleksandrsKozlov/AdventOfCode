import re
from functools import reduce
from read_lines import read_lines

def part_one(lines: list[str]):
    color_limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    game_nr_sum = 0
    for idx in range(len(lines)):
        line = lines[idx].strip("\n")
        only_cubes = line.split(":")[1]
        bag_grabs = only_cubes.split(";")
        is_game_valid = True
        for bag_grab in bag_grabs:
            pattern = re.compile(r'(\d+)\s*([a-zA-Z]+)')
            matches = re.findall(pattern, bag_grab)
            for number, color in matches:
                if int(number) > color_limits[color]:
                    is_game_valid = False
                    break
            if not is_game_valid:
                break
        if is_game_valid:
            game_nr_sum += (idx + 1)
    print(game_nr_sum)

def part_one_another(lines: list[str]):
    color_limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    game_nr_sum = 0
    for idx in range(len(lines)):
        line = lines[idx].strip("\n")
        only_cubes = line.split(":")[1]
        pattern = re.compile(r'(\d+)\s*([a-zA-Z]+)')
        matches = re.findall(pattern, only_cubes)
        is_game_valid = True
        for number, color in matches:
            if int(number) > color_limits[color]:
                is_game_valid = False
                break
        if is_game_valid:
            game_nr_sum += (idx + 1)
    print(game_nr_sum)

def part_two(lines: list[str]):
    game_nr_sum = 0
    for idx in range(len(lines)):
        least_needed_colors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        line = lines[idx].strip("\n")
        only_cubes = line.split(":")[1]
        pattern = re.compile(r'(\d+)\s*([a-zA-Z]+)')
        matches = re.findall(pattern, only_cubes)
        for number, color in matches:
            if int(number) > least_needed_colors[color]:
                least_needed_colors[color] = int(number)
        all_min_values = list(least_needed_colors.values())
        multiply_result = reduce(lambda x, y: x*y, all_min_values)
        game_nr_sum += multiply_result
    print(game_nr_sum)

lines = read_lines(task_number=2)
part_one(lines)
part_one_another(lines)
part_two(lines)