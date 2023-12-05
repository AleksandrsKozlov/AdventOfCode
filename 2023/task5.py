from read_lines import read_lines
from measure_time import run_with_measurment

def remove_empty_values(input_list: list[str]):
    return [x for x in input_list if x]

def parse_input(lines: list[str], part_nr: int):
    seeds: list[int] = []
    seed_map_step = []
    seed_maps: list[list[list]] = []
    for line in lines:
        if line.startswith("\n"):
            if len(seed_map_step) > 0:
                seed_maps.append(seed_map_step)
            seed_map_step = []
            continue
        if line[0].isdigit():
            seed_map = line.strip("\n").split(" ")
            seed_map = [int(seed) for seed in seed_map]
            seed_map_step.append(tuple(seed_map))
        if line.startswith("seeds"):
            splited_line = line.split(":")
            seeds_single = splited_line[1].strip("\n").split(" ")
            seeds_single = remove_empty_values(seeds_single)
            seeds_single = [int(seed) for seed in seeds_single]
            if part_nr == 1:
                for seed in seeds_single:
                    seeds.append((seed, 1))
            elif part_nr == 2:
                for idx in range(0, len(seeds_single), 2):
                    seeds.append((seeds_single[idx], seeds_single[idx+1]))
    seed_maps.append(seed_map_step)
    return seeds, seed_maps

def grow_seeds(seeds: list[int], seed_maps: list[list[list[int]]]):
    seeds_for_next_section = []
    for idx, seed_map_section in enumerate(seed_maps):
        if idx == 0:
            seeds_for_next_section = seeds
        seeds_for_next_map = seeds_for_next_section
        seeds_for_next_section = []

        for destination, source, length in seed_map_section:
            seeds_for_map = seeds_for_next_map
            seeds_for_next_map = []
            
            for seed, seed_range in seeds_for_map:
                overlap = (max(seed, source), min(seed + seed_range, source + length))
                if overlap[0] <= overlap[1]:
                    if seed < source:
                        lesser_seed = (seed, source - seed)
                        seeds_for_next_map.append(lesser_seed)
                    if (seed + seed_range) > (source + length):
                        greater_seed = (source + length, seed + seed_range - source - length)
                        seeds_for_next_map.append(greater_seed)
                    seed = overlap[0] + destination - source
                    seed_range = overlap[1] - overlap[0]
                    seeds_for_next_section.append((seed, seed_range))
                else:
                    seeds_for_next_map.append((seed, seed_range))

        seeds_for_next_section.extend(seeds_for_next_map)

    return min([seed[0] for seed in seeds_for_next_section])


def part_one(lines: list[str]):
    seeds, seed_maps = parse_input(lines=lines, part_nr=1)
    return grow_seeds(seeds, seed_maps)

def part_two(lines: list[str]):
    seeds, seed_maps = parse_input(lines=lines, part_nr=2)
    return grow_seeds(seeds, seed_maps)

if __name__ == '__main__':
    lines = run_with_measurment(read_lines, task_number=5)
    result = run_with_measurment(part_one, print_result=True, lines=lines)
    result = run_with_measurment(part_two, print_result=True, lines=lines)