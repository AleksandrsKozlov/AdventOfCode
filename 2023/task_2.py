import re
from functools import reduce
from read_lines import read_lines
from mesaure_time import run_with_measurment

def get_color_number_pairs(line: str) -> tuple[str, str]:
    line.strip("\n")
    only_values = line.split(":")[1]
    pattern = re.compile(r'(\d+)\s*([a-zA-Z]+)')
    return re.findall(pattern, only_values)

def part_one(lines: list[str]):
    color_limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    game_nr_sum = 0
    for idx, line in enumerate(lines):
        color_map = get_color_number_pairs(line)
        is_game_valid = True
        for number, color in color_map:
            if int(number) > color_limits[color]:
                is_game_valid = False
                break
        if is_game_valid:
            game_nr_sum += (idx + 1)
    return game_nr_sum

def part_two(lines: list[str]):
    game_nr_sum = 0
    for line in lines:
        least_needed_colors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        color_map = get_color_number_pairs(line)
        for number, color in color_map:
            if int(number) > least_needed_colors[color]:
                least_needed_colors[color] = int(number)
        all_min_values = list(least_needed_colors.values())
        multiply_result = reduce(lambda x, y: x*y, all_min_values)
        game_nr_sum += multiply_result
    return game_nr_sum

lines = run_with_measurment(read_lines, task_number=2)
result = run_with_measurment(part_one, print_result=True, lines=lines)
result = run_with_measurment(part_two, print_result=True, lines=lines)