from measure_time import run_with_measurment
import numpy as np

def get_input():
    lines = open("2023/inputs/task9.txt").read().split("\n")
    return [list(map(int, line.split())) for line in lines]

def part_one(lines: list[list[int]]):
    result = 0
    for line in lines:
        result += line[-1]
        while sum(line) != 0:
            line = np.diff(line)
            result += line[-1]
    return result

def part_two(lines: list[list[int]]):
    result = 0
    for line in lines:
        result += line[0]
        i = 0
        while len(set(line)) != 1:
            line = np.diff(line)
            result -= line[0] if i%2 == 0 else -line[0]
            i += 1
    return result

def part_two_reverse(lines: list[list[int]]):
    result = 0
    for line in lines:
        line.reverse()
        result += line[-1]
        while len(set(line)) != 1:
            line = np.diff(line)
            result += line[-1]
    return result

def both_parts(lines: list[list[int]]):
    part_1_result = 0
    part_2_result = 0
    for line in lines:
        part_1_result += line[-1]
        part_2_result += line[0]
        i = 0
        while len(set(line)) != 1:
            line = np.diff(line)
            part_1_result += line[-1]
            part_2_result -= line[0] if i%2 == 0 else -line[0]
            i += 1
    return part_1_result, part_2_result

if __name__ == '__main__':
    lines = run_with_measurment(get_input)
    run_with_measurment(part_one, lines=lines, print_result=True)
    run_with_measurment(part_two, lines=lines, print_result=True)
    run_with_measurment(part_two_reverse, lines=lines, print_result=True)
    run_with_measurment(both_parts, lines=lines, print_result=True)