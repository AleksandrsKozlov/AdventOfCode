from measure_time import run_with_measurment
from functools import cache

def get_input():
    lines = open("2023/inputs/task12.txt").read().split("\n")
    springs = []
    helpers = []
    for line in lines:
        parsed = line.split()
        springs.append(parsed[0])
        helpers.append(
            tuple(
                [int(helper) for helper in parsed[1].split(",")]
            ))
    return springs, helpers

def update_input(springs: list[str], helpers: list[tuple]):
    helpers = [helper*5 for helper in helpers]
    springs = ["?".join([spring] * 5) for spring in springs]
    return springs, helpers


def part_one(springs, helpers):
    result = 0
    for idx, spring in enumerate(springs):
        result += get_line_combinations(spring, tuple(helpers[idx]), 0)
    print(get_line_combinations.cache_info())
    return result

def part_two(springs, helpers):
    springs, helpers = update_input(springs, helpers)
    result = 0
    for idx, spring in enumerate(springs):
        result += get_line_combinations(spring, tuple(helpers[idx]), 0)
    print(get_line_combinations.cache_info())
    return result

@cache
def get_line_combinations(springs: str, helpers: list[int], current_size: int):
    if len(helpers) == 0:
        if "#" in springs:
            return 0
        return 1
    if not springs:
        if len(helpers) == 1 and current_size == helpers[0]:
            return 1
        return 0
    
    if springs[0] == "?":
        return (
            get_line_combinations("#" + springs[1:], helpers, current_size)
            + get_line_combinations("." + springs[1:], helpers, current_size)
        )
    if springs[0] == ".":
        if current_size == 0:
            return get_line_combinations(springs[1:], helpers, current_size=0)
        if helpers[0] <= current_size:
            return get_line_combinations(springs[1:], helpers[1:], current_size=0)
        return 0
    if springs[0] == "#":
        if current_size + 1 > helpers[0]:
            return 0
        return get_line_combinations(springs[1:], helpers, current_size+1)


if __name__ == '__main__':
    springs, helpers = run_with_measurment(get_input)
    run_with_measurment(part_one, springs=springs, helpers=helpers, print_result=True)
    run_with_measurment(part_two, springs=springs, helpers=helpers, print_result=True)