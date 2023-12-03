import re
from read_lines import read_lines
from mesaure_time import run_with_measurment

def get_line_numbers(line: str):
    return [
        {"start": m.start(), "end": m.end(), "value": int(m.group())}
        for m in re.finditer(r'\d+', line)
    ]

def get_symbol_stats(line: list[str]):
    return [
        m.start()
        for m in re.finditer(r'[^\d^.]', line)
    ]

def get_gear_coordinates(line: str):
    return [
        m.start()
        for m in re.finditer(r'[*]', line)
    ]

def get_adjacent_number_stats(lines: list[str], idx: int, data_length: int):
    previous_line = get_line_numbers(lines[idx-1].strip("\n")) if idx > 0 else []
    current_line = get_line_numbers(lines[idx].strip("\n"))
    next_line = get_line_numbers(lines[idx+1].strip("\n")) if idx < data_length - 1 else []
    return [previous_line, current_line, next_line]

def get_adjacent_symbol_stats(lines: list[str], idx: int, data_length: int):
    previous_line = get_symbol_stats(lines[idx-1].strip("\n")) if idx > 0 else []
    current_line = get_symbol_stats(lines[idx].strip("\n"))
    next_line = get_symbol_stats(lines[idx+1].strip("\n")) if idx < data_length - 1 else []
    return [previous_line, current_line, next_line]

def check_intersection(range_to_check: list[int], values_to_check: list[int]):
    a = set(range_to_check)
    b = set(values_to_check)
    c = a.intersection(b)
    return len(c) > 0

def check_numbers(
        number_stats: list[dict],
        symbol_stats: list[list[int]],
        data_width: int
    ):
    line_sum = 0
    for number_data in number_stats:
        check_range_start = number_data["start"] - 1 if number_data["start"] > 0 else number_data["start"]
        check_range_end = number_data["end"] + 1 if number_data["end"] < data_width - 1 else number_data["end"]
        check_range_list = list(range(check_range_start, check_range_end))
        for symbol_stat in symbol_stats:
            if len(symbol_stat) > 0:
                is_valid_number = check_intersection(check_range_list, symbol_stat)
                if is_valid_number:
                    line_sum += number_data["value"]
                    break
    return line_sum

def get_gear_line_numbers(numbers_line: list[dict], check_range_list: list[int]):
    valid_numbers = []
    for number in numbers_line:
        number_range = list(range(number["start"], number["end"]))
        is_valid_number = check_intersection(check_range_list, number_range)
        if is_valid_number:
            valid_numbers.append(number["value"])
    return valid_numbers

def get_gear_numbers(gear_stat: int, numbers_lines: list[list[dict]], data_width: int):
    valid_numbers = []
    check_range_start = gear_stat - 1 if gear_stat > 0 else gear_stat
    check_range_end = gear_stat + 2 if gear_stat < data_width - 1 else gear_stat
    check_range_list = list(range(check_range_start, check_range_end))
    for numbers_line in numbers_lines:
        valid_line_numbers = get_gear_line_numbers(numbers_line, check_range_list)
        valid_numbers.extend(valid_line_numbers)
    return valid_numbers

def check_gears(gear_stats: list[int], numbers_lines: list[list[dict]], data_width: int):
    line_sum = 0
    for gear_stat in gear_stats:
        valid_numbers = get_gear_numbers(gear_stat, numbers_lines, data_width)
        if len(valid_numbers) == 2:
            line_sum += (valid_numbers[0] * valid_numbers[1])
    return line_sum

def part_one(lines: list[str]):
    data_width = len(lines[0]) - 1
    data_length = len(lines)
    sum_of_valid_numbers = 0
    for idx, line in enumerate(lines):
        line = lines[idx].strip("\n")
        numbers_stats = get_line_numbers(line)
        adjacent_stats = get_adjacent_symbol_stats(lines, idx, data_length)
        valid_line_sum = check_numbers(numbers_stats, adjacent_stats, data_width)
        sum_of_valid_numbers += valid_line_sum
    return sum_of_valid_numbers

def part_two(lines: list[str]):
    data_width = len(lines[0]) - 1
    data_length = len(lines)
    sum_of_valid_numbers = 0
    for idx, line in enumerate(lines):
        line = lines[idx].strip("\n")
        gers_stats = get_gear_coordinates(line)
        adjacent_stats = get_adjacent_number_stats(lines, idx, data_length)
        valid_line_sum = check_gears(gers_stats, adjacent_stats, data_width)
        sum_of_valid_numbers += valid_line_sum
    return sum_of_valid_numbers

lines = run_with_measurment(read_lines, task_number=3)
result = run_with_measurment(part_one, print_result=True, lines=lines)
result = run_with_measurment(part_two, print_result=True, lines=lines)