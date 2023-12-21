from measure_time import run_with_measurment
from copy import deepcopy
import math


def get_input() -> tuple[list[tuple[str, int]], list[tuple[str, str]]]:
    lines = open("2023/inputs/task20.txt").read().split("\n")
    configuration = {}
    module_states = {}
    for line in lines:
        splited = line.split(" -> ")
        module = splited[0]
        module_type = module[0]
        destinations = splited[1].split(", ")
        if module == "broadcaster":
            configuration["broadcaster"] = {"type": "broadcaster", "destination": destinations}
        else:
            configuration[module[1:]] = {"type": module_type, "destination": destinations}
        if module_type == "%":
            module_states[module[1:]] = False
        if module_type == "&":
            configuration[module[1:]]["inputs"] = []
            module_states[module[1:]] = True
    for line in lines:
        splited = line.split(" -> ")
        module = splited[0]
        module_type = module[0]
        destinations = splited[1].split(", ")
        for destination in destinations:
            if destination in configuration and configuration[destination]["type"] == "&":
                configuration[destination]["inputs"].append(module[1:])
    return configuration, module_states


def push_button_part_one(configuration: dict, module_states: dict):
    low_pulse = 1
    high_pulse = 0
    current_inputs = []
    for destination in configuration["broadcaster"]["destination"]:
        current_inputs.append({
            "impulse": "low",
            "module": destination
        })
    while len(current_inputs) > 0:
        current_states = deepcopy(module_states)
        next_inputs = []
        for input in current_inputs:
            impulse = input["impulse"]
            if impulse == "low":
                low_pulse += 1
            else:
                high_pulse += 1
            
            if input["module"] not in configuration:
                continue
            module_config = configuration[input["module"]]
            
            if module_config["type"] == "%":
                if impulse == "low":
                    module_states[input["module"]] = not module_states[input["module"]]
                    for destination in module_config["destination"]:
                        next_inputs.append({
                                "impulse": "high" if module_states[input["module"]] else "low",
                                "module": destination
                            })
            if module_config["type"] == "&":
                all_high = True
                for module_input in module_config["inputs"]:
                    if current_states[module_input] == False:
                        all_high = False
                        break
                module_states[input["module"]] = False if all_high else True
                impulse = "low" if all_high else "high"
                for destination in module_config["destination"]:
                    next_inputs.append({
                            "impulse": "low" if all_high else "high",
                            "module": destination
                        })
        current_inputs = next_inputs
    return low_pulse, high_pulse



def push_button_part_two(configuration: dict, module_states: dict, module_ends: list[str]):
    low_pulse = 1
    high_pulse = 0
    current_inputs = []
    check = False
    for destination in configuration["broadcaster"]["destination"]:
        current_inputs.append({
            "impulse": "low",
            "module": destination
        })
    while len(current_inputs) > 0:
        current_states = deepcopy(module_states)
        next_inputs = []
        for input in current_inputs:
            impulse = input["impulse"]
            if impulse == "low":
                low_pulse += 1
            else:
                high_pulse += 1
            
            if input["module"] not in configuration:
                continue
            module_config = configuration[input["module"]]
            
            if module_config["type"] == "%":
                if impulse == "low":
                    module_states[input["module"]] = not module_states[input["module"]]
                    for destination in module_config["destination"]:
                        next_inputs.append({
                                "impulse": "high" if module_states[input["module"]] else "low",
                                "module": destination
                            })
            if module_config["type"] == "&":
                all_high = True
                for module_input in module_config["inputs"]:
                    if current_states[module_input] == False:
                        all_high = False
                        break
                module_states[input["module"]] = False if all_high else True
                impulse = "low" if all_high else "high"
                for destination in module_config["destination"]:
                    if destination in module_ends and impulse == "low":
                        check=True
                    next_inputs.append({
                            "impulse": "low" if all_high else "high",
                            "module": destination
                        })
        current_inputs = next_inputs
    return check



def part_one(configuration: dict, module_states: dict):
    result_low_pulse = 0
    result_high_pulse = 0
    for _ in range(1000):
        low_pulse, high_pulse = push_button_part_one(configuration, module_states)
        result_low_pulse += low_pulse
        result_high_pulse += high_pulse
    return result_low_pulse * result_high_pulse


def part_two(configuration: dict, module_states: dict):
    main_module = "rx"
    output_module = None
    for module, config in configuration.items():
        if main_module in config["destination"]:
            output_module = module
            break
    cycle_main_modules = []
    for module, config in configuration.items():
        if output_module in config["destination"]:
            cycle_main_modules.append(module)
    
    button_pressed_count_all = []
    button_pressed_count = 0
    while len(button_pressed_count_all) < len(cycle_main_modules):
        found = push_button_part_two(configuration, module_states, cycle_main_modules)
        button_pressed_count += 1
        if found:
            button_pressed_count_all.append(button_pressed_count)
    return math.prod(button_pressed_count_all)

if __name__ == '__main__':
    configuration, module_states = run_with_measurment(get_input)
    run_with_measurment(part_one, configuration=configuration, module_states=deepcopy(module_states), print_result=True)
    run_with_measurment(part_two, configuration=configuration, module_states=module_states, print_result=True)