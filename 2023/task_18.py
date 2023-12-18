from measure_time import run_with_measurment


def get_input() -> tuple[list[tuple[str, int]], list[tuple[str, str]]]:
    lines = open("2023/inputs/task18.txt").read().split("\n")
    instructions = [tuple(line.split()) for line in lines]
    directions = "RDLU"
    part_one_instructions = [
        (direction, int(length))
        for direction, length, _ in instructions
    ]
    part_two_instructions = [
        (directions[int(hex_code[-2])], int(hex_code[2:7], 16))
        for _, _, hex_code in instructions
    ]
    return part_one_instructions, part_two_instructions


def get_next_point(direction: str, length: int, prev_point: tuple[int, int]):
    prev_x, prev_y = prev_point
    
    if direction == "U":
        return (prev_x - length, prev_y)
    if direction == "D":
        return (prev_x + length, prev_y)
    if direction == "L":
        return (prev_x, prev_y - length)
    if direction == "R":
        return (prev_x, prev_y + length)


def get_area_input(instructions: list[tuple[str, int]]):
    points = [(0,0)]
    perimeter = 1
    for instruction in instructions:
        direction, length = instruction
        perimeter += length
        points.append(get_next_point(direction, length, points[-1]))
    return points, perimeter


def calculate_area(points: list[tuple[int, int]], perimeter: int):
    area = 0
    for idx in range(len(points)-1):
        area += points[idx][0]*points[idx+1][1] - points[idx][1]*points[idx+1][0]
    return abs(area)//2 + perimeter//2 + 1


def part_one(instructions: list[tuple[str, int]]):
    return calculate_area(*get_area_input(instructions))


def part_two(instructions: list[tuple[str, int]]):
    return calculate_area(*get_area_input(instructions))


if __name__ == '__main__':
    part_one_instructions, part_two_instructions = run_with_measurment(get_input)
    run_with_measurment(part_one, instructions=part_one_instructions, print_result=True)
    run_with_measurment(part_two, instructions=part_two_instructions, print_result=True)