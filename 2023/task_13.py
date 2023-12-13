from measure_time import run_with_measurment

def get_input():
    lines = open("2023/inputs/task13.txt").read().split("\n")
    pattern = []
    horizontal_patterns = []
    for line in lines:
        if not line:
            horizontal_patterns.append(pattern)
            pattern = []
            continue
        pattern.append(line)
    horizontal_patterns.append(pattern)

    vertical_patterns = []
    for horizontal_pattern in horizontal_patterns:
        length = len(horizontal_pattern[0])
        vertical_pattern = []
        for idx in range(length):
            vertical_pattern.append(''.join(pattern[idx] for pattern in horizontal_pattern))
        vertical_patterns.append(vertical_pattern)
    return horizontal_patterns, vertical_patterns

def part_one(horizontal_patterns: list[list[str]], vertical_patterns: list[list[str]]):
    processed_horizontal = process_patterns(horizontal_patterns)
    processed_vertical = process_patterns(vertical_patterns)
    return sum(processed_horizontal) * 100 + sum(processed_vertical)

def part_two(horizontal_patterns: list[list[str]], vertical_patterns: list[list[str]]):
    processed_horizontal = process_patterns(horizontal_patterns, fix_number=1)
    processed_vertical = process_patterns(vertical_patterns, fix_number=1)
    return sum(processed_horizontal) * 100 + sum(processed_vertical)
        
def process_patterns(patterns: list[list[str]], fix_number: int = 0):
    processed_patterns = []
    for pattern in patterns:
        processed_pattern = 0
        for idx in range(len(pattern) - 1):
            back_pattern = pattern[idx]
            front_patter = pattern[idx + 1]
            diff_count = sum(1 for a, b in zip(back_pattern, front_patter) if a != b)
            distance_to_wall = min(len(pattern) - idx - 1, idx + 1)
            for distance in range(1, distance_to_wall):
                if diff_count > fix_number:
                    break
                back_pattern = pattern[idx - distance]
                front_patter = pattern[idx + 1 + distance]
                diff_count += sum(1 for a, b in zip(back_pattern, front_patter) if a != b)
            if diff_count == fix_number:
                processed_pattern = idx + 1
                break
        processed_patterns.append(processed_pattern)
    return processed_patterns

if __name__ == '__main__':
    horizontal_patterns, vertical_patterns = run_with_measurment(get_input)
    run_with_measurment(part_one, horizontal_patterns=horizontal_patterns, vertical_patterns=vertical_patterns, print_result=True)
    run_with_measurment(part_two, horizontal_patterns=horizontal_patterns, vertical_patterns=vertical_patterns, print_result=True)