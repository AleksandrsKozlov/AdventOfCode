from read_lines import read_lines
from measure_time import run_with_measurment
from functools import reduce

def remove_empty_values(input_list: list[str]):
    return [x for x in input_list if x]

def get_winning_numbers_legth(line: str):
    numbers = line.strip("\n").split(":")[1].split("|")
    winning_numbers = remove_empty_values(numbers[0].split(" "))
    user_numbers = remove_empty_values(numbers[1].split(" "))
    intersection = set(winning_numbers).intersection(user_numbers)
    return len(intersection)

def update_cards_range(list_to_update: list, value: int,  idx: int, length: int, limit: int):
    if idx >= limit:
        return
    range_end = idx + length
    range_end = limit if range_end > limit else range_end
    for i in range(idx, range_end):
        list_to_update[i] = list_to_update[i] + value


def part_one(lines: list[str]):
    sum_value = 0
    for line in lines:
        number_of_winning = get_winning_numbers_legth(line)
        if number_of_winning > 0:
            sum_value += pow(2, number_of_winning - 1)
    return sum_value

def part_two(lines: list[str]):
    number_of_cards = len(lines)
    populated_cards = [0] * number_of_cards
    for idx, line in enumerate(lines):
        populated_cards[idx] = populated_cards[idx] + 1
        number_of_winning = get_winning_numbers_legth(line)
        update_cards_range(populated_cards, populated_cards[idx], idx + 1, number_of_winning, number_of_cards)
    return reduce(lambda x, y: x+y, populated_cards)

lines = run_with_measurment(read_lines, task_number=4)
result = run_with_measurment(part_one, print_result=True, lines=lines)
result = run_with_measurment(part_two, print_result=True, lines=lines)