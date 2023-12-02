digit_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
all_digits = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

def get_first_digit(line: str):
    map_digit = {}
    for digit in all_digits:
        if digit in line:
            index_of_digit = line.index(digit)
            map_digit[digit] = index_of_digit
    min_digit = min(map_digit, key=map_digit.get)
    min_parsed = str(digit_map.get(min_digit, min_digit))
    return min_parsed

def get_last_digit(line: str):
    map_digit = {}
    for digit in all_digits:
        if digit in line:
            index_of_digit = line.rindex(digit)
            map_digit[digit] = index_of_digit
    max_digit = max(map_digit, key=map_digit.get)
    max_parsed = str(digit_map.get(max_digit, max_digit))
    return max_parsed

with open("2023/inputs/task1.txt") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        first = get_first_digit(line)
        last = get_last_digit(line)
        digit_from_line = int(first + last)
        sum += digit_from_line
    print(sum)