from measure_time import run_with_measurment


def get_input():
    input = open("2023/inputs/task15.txt").read().split("\n")[0]
    codes = input.split(",")
    return codes


def hash_algorithm(label: str):
    current_value = 0
    for char in label:
        ascii_value = ord(char)
        current_value = ((current_value + ascii_value) * 17) % 256
    return current_value


def get_lens_by_label(lenses: list[dict], label: str):
    for idx, lens in enumerate(lenses):
        if lens["label"] == label:
            return idx
    return -1


def calculate_focusing_power(boxes: dict[str, list[dict]]):
    box_result = 0
    for box_value, lenses in enumerate(boxes.values()):
        for lens_order, lens in enumerate(lenses):
            box_result += ((box_value + 1) * (lens_order + 1) * lens["value"])
    return box_result


def part_one(codes: list[str]):
    return sum(hash_algorithm(code) for code in codes)


def part_two(codes: list[str]):
    boxes: dict[str, list] = {}
    for i in range(256):
        boxes[str(i)] = []
    for code in codes:
        remove = "-" in code
        parsed = code.split("-") if remove else code.split("=")
        label = parsed[0]
        value = parsed[1]
        box_nr = hash_algorithm(label)
        lenses = boxes[str(box_nr)]
        lens_idx = get_lens_by_label(lenses, label)
        if remove and lens_idx != -1:
            del lenses[lens_idx]
        if not remove:
            if lens_idx == -1:
                lenses.append({"label": label, "value": int(value)})
            else:
                lenses[lens_idx]["value"] = int(value)
    
    return calculate_focusing_power(boxes)


if __name__ == '__main__':
    codes = run_with_measurment(get_input)
    run_with_measurment(part_one, codes=codes, print_result=True)
    run_with_measurment(part_two, codes=codes, print_result=True)