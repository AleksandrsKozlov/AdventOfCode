from read_lines import read_lines
from measure_time import run_with_measurment
from multiprocessing import Pool

def remove_empty_values(input_list: list[str]):
    return [x for x in input_list if x]

def part_one(lines: list[str]):
    seeds: list[int] = None
    should_update_seeds: list[bool] = None
    is_new_map = False
    for line in lines:
        if line.startswith("\n"):
            is_new_map = True
            should_update_seeds = [True for state in should_update_seeds]
            continue
        if is_new_map and line[0].isdigit():
            seed_map = line.strip("\n").split(" ")
            seed_map = [int(seed) for seed in seed_map]
            for idx, seed in enumerate(seeds):
                if seed >= seed_map[1] and seed < seed_map[1] + seed_map[2] and should_update_seeds[idx]:
                    diff = seed - seed_map[1]
                    new_state = seed_map[0] + diff
                    seeds[idx] = new_state
                    should_update_seeds[idx] = False
        if line.startswith("seeds"):
            splited_line = line.split(":")
            seeds = splited_line[1].strip("\n").split(" ")
            seeds = remove_empty_values(seeds)
            seeds = [int(seed) for seed in seeds]
            should_update_seeds = len(seeds) * [True]
    return min(seeds)

def process_pair(seed, seed_maps):
    print(seed)
    min_result = None
    for i in range(seed[1]):
        current_seed = seed[0] + i
        if ((current_seed - seed[0]) % 1000000) == 0:
            print((current_seed - seed[0]) / 1000000)
        for seed_map_section in seed_maps:
            for seed_map in seed_map_section:
                if current_seed >= seed_map[1] and current_seed < seed_map[1] + seed_map[2]:
                    diff = current_seed - seed_map[1]
                    new_state = seed_map[0] + diff
                    current_seed = new_state
                    break
        if min_result is None:
            min_result = current_seed
            continue
        min_result = min(current_seed, min_result)
    return min_result

def part_two(lines: list[str]):
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
            seed_map_step.append(seed_map)
        if line.startswith("seeds"):
            splited_line = line.split(":")
            seeds_single = splited_line[1].strip("\n").split(" ")
            seeds_single = remove_empty_values(seeds_single)
            seeds_single = [int(seed) for seed in seeds_single]
            for idx in range(0, len(seeds_single), 2):
                seeds.append([seeds_single[idx], seeds_single[idx+1]])
    seed_maps.append(seed_map_step)

    pool_args = [(seed, seed_maps) for seed in seeds]
    min_results = []

    with Pool() as pool:
        for result in pool.starmap(process_pair, pool_args):
            print(result)
            min_results.append(result)
    return min(min_results)

if __name__ == '__main__':
    lines = run_with_measurment(read_lines, task_number=5)
    result = run_with_measurment(part_one, print_result=True, lines=lines)
    result = run_with_measurment(part_two, print_result=True, lines=lines)