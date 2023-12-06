import math
from measure_time import run_with_measurment

def calculate_valid_attempts(time: int, distance: int):
    discriminant = math.sqrt((time*time) - 4*distance)
    x1 = (-time + discriminant)/2
    x2 = (-time - discriminant)/2
    return abs(math.ceil(x2) - math.ceil(x1))


def get_inputs():
    lines = open("2023/inputs/task6.txt").read().split("\n")
    time_list = [int(element) for element in lines[0].split() if element.isdigit()]
    distance_list = [int(element) for element in lines[1].split() if element.isdigit()]
    first_input = list(zip(time_list, distance_list))
    second_input = (int(''.join(map(str, time_list))), int(''.join(map(str, distance_list))))
    return first_input, second_input


def part_one(time_distance_pairs: list[tuple[int, int]]):
    return math.prod(calculate_valid_attempts(time, distance) for (time, distance) in time_distance_pairs)


def part_two(time_distance_pair: tuple[int, int]):
    return calculate_valid_attempts(time_distance_pair[0], time_distance_pair[1])


if __name__ == '__main__':
    first_input, second_input = run_with_measurment(get_inputs)
    run_with_measurment(part_one, time_distance_pairs=first_input, use_nanoseconds=True, print_result=True)
    run_with_measurment(part_two, time_distance_pair=second_input, use_nanoseconds=True, print_result=True)
