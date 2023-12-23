from measure_time import run_with_measurment


def get_input():
    lines = open("2023/inputs/task21.txt").read().split("\n")
    start_position = (0,0)
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == "S":
                start_position = (x,y)
                break
    x, y = start_position
    replaced_start_line = list(lines[x])
    replaced_start_line[y] = "."
    lines[x] = "".join(replaced_start_line)
    return lines, start_position


def get_next_moves(positions: list[tuple[int,int]], lines: list[str], processed_moves: list[tuple[int,int]]):
    length = len(lines)
    width = len(lines[0])
    possible_moves = []
    for position in positions:
        x, y = position
        if x - 1 >= 0:
            possible_moves.append((x - 1, y))
        if x + 1 < length:
            possible_moves.append((x + 1, y))
        if y - 1 >= 0:
            possible_moves.append((x, y - 1))
        if y + 1 < width:
            possible_moves.append((x, y + 1))
    
    return set((x,y) for x, y in possible_moves if lines[x][y] == "." and (x,y) not in processed_moves)


def part_one(lines: list[str], start_position: tuple[int,int]):
    processed_moves = set([])
    next_moves = get_next_moves([start_position], lines, processed_moves)
    step_count = 0
    garden_plots = 0
    while step_count < 64 and len(next_moves) > 0:
        processed_moves.update(next_moves)
        if (step_count + 1) % 2 == 0:
            garden_plots += len(next_moves)
        step_count += 1
        next_moves = get_next_moves(next_moves, lines, processed_moves)
    return garden_plots


def part_two(lines: list[str], start_position: tuple[int,int], target_steps: int):
    processed_moves = set([])
    width = len(lines[0])
    distance_from_center = width // 2

    next_moves = get_next_moves([start_position], lines, processed_moves)

    step_count = 0
    garden_plots_odd = 0
    garden_plots_even = 0
    corner_garden_plots_odd = 0
    corner_garden_plots_even = 0

    while len(next_moves) > 0:
        processed_moves.update(next_moves)
        if (step_count + 1) % 2 != 0:
            garden_plots_odd += len(next_moves)
            if step_count + 1 > distance_from_center:
                corner_garden_plots_odd += len(next_moves)
        else:
            garden_plots_even += len(next_moves)
            if step_count + 1 > distance_from_center:
                corner_garden_plots_even += len(next_moves)
        step_count += 1
        next_moves = get_next_moves(next_moves, lines, processed_moves)

    max_length_fields = (target_steps - distance_from_center) // width
    garden_plots_full = (
        (max_length_fields + 1) ** 2 * garden_plots_odd +
        (max_length_fields) ** 2 * garden_plots_even -
        (max_length_fields + 1) * corner_garden_plots_odd +
        (max_length_fields) * corner_garden_plots_even
    )
    return garden_plots_full

if __name__ == '__main__':
    lines, start_position = run_with_measurment(get_input)
    run_with_measurment(part_one, lines=lines, start_position=start_position, print_result=True)
    run_with_measurment(part_two, lines=lines, start_position=start_position, target_steps=26501365, print_result=True)