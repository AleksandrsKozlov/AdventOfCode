from measure_time import run_with_measurment


def get_input() -> tuple[list[tuple[str, int]], list[tuple[str, str]]]:
    lines = open("2023/inputs/task19.txt").read().split("\n\n")
    workflows_unparsed = lines[0].split("\n")
    parts_unparsed = lines[1].split("\n")
    workflows = {}
    for workflow_unparsed in workflows_unparsed:
        splited = workflow_unparsed.split("{")
        workflow_name = splited[0]
        instructions = splited[1].split("}")[0].split(",")
        workflow_instructions = []
        for instruction in instructions:
            if ":" not in instruction:
                workflow_instructions.append({"next_workflow":  instruction})
                continue
            instruction_split = instruction.split(":")
            workflow_instructions.append({
                "part": instruction_split[0][0],
                "operator": instruction_split[0][1],
                "value": int(instruction_split[0][2:]),
                "next_workflow": instruction_split[1]
            })
        workflows[workflow_name] = workflow_instructions

    parts = []
    for part_unparsed in parts_unparsed:
        split_part = part_unparsed.split("{")[1].split("}")[0].split(",")
        part = {}
        for category in split_part:
            part[category[0]] = int(category[2:])
        parts.append(part)
    return workflows, parts


def part_one(workflows: dict[str,list[dict[str, any]]], parts: list[dict[str, int]]):
    result = 0
    for part in parts:
        next_workflow = "in"
        while next_workflow != "A" and next_workflow != "R":
            workflow = workflows[next_workflow]
            for instruction in workflow:
                if "operator" not in instruction.keys():
                    next_workflow = instruction["next_workflow"]
                    break
                if instruction["operator"] == ">":
                    if part[instruction["part"]] > instruction["value"]:
                        next_workflow = instruction["next_workflow"]
                        break
                if instruction["operator"] == "<":
                    if part[instruction["part"]] < instruction["value"]:
                        next_workflow = instruction["next_workflow"]
                        break

            if next_workflow == "A":
                for value in part.values():
                    result += value
    return result


def find_workflow_by_result(workflows: dict[str,list[dict[str, any]]], result: str):
    for key, instructions in workflows.items():
        for idx, instruction in enumerate(instructions):
            if instruction["next_workflow"] == result:
                return {"workflow": workflows[key], "idx": idx, "name": key}


def get_categories_stats(start_wokflow: dict, workflows: dict[str,list[dict[str, any]]]):
    stats = {
        "x": {"min": 0, "max": 4000},
        "m": {"min": 0, "max": 4000},
        "a": {"min": 0, "max": 4000},
        "s": {"min": 0, "max": 4000},
    }
    current_workflow = start_wokflow
    while current_workflow is not None:
        current_instructions: list[dict] = current_workflow["workflow"]
        for i in range(current_workflow["idx"], -1, -1):
            instruction = current_instructions[i]
            if "operator" not in instruction.keys():
                continue
            current_value = instruction["value"]
            if current_workflow["idx"] == i:
                if instruction["operator"] == ">":
                    if stats[instruction["part"]]["min"] < current_value:
                        stats[instruction["part"]]["min"] = current_value
                if instruction["operator"] == "<":
                    if stats[instruction["part"]]["max"] > current_value:
                        stats[instruction["part"]]["max"] = current_value - 1
            else:
                if instruction["operator"] == "<":
                    if stats[instruction["part"]]["min"] < current_value:
                        stats[instruction["part"]]["min"] = current_value - 1
                if instruction["operator"] == ">":
                    if stats[instruction["part"]]["max"] > current_value:
                        stats[instruction["part"]]["max"] = current_value
        
        if current_workflow["name"] == "in":
            current_workflow = None
        else :
            current_workflow = find_workflow_by_result(workflows, current_workflow["name"])

    return stats


def part_two(workflows: dict[str,list[dict[str, any]]]):
    accepted_workflows: list[dict] = []
    for key, instructions in workflows.items():
        for idx, instruction in enumerate(instructions):
            if instruction["next_workflow"] == "A":
                accepted_workflows.append({"workflow": workflows[key], "idx": idx, "name": key})

    distinct_combinations = 0
    for accepted_workflow in accepted_workflows:
        stats = get_categories_stats(accepted_workflow, workflows)
        current_combinations = 1
        for key, min_max_values in stats.items():
            current_combinations *= (min_max_values["max"] - min_max_values["min"])
        distinct_combinations += current_combinations
    return distinct_combinations


if __name__ == '__main__':
    workflows, parts = run_with_measurment(get_input)
    run_with_measurment(part_one, workflows=workflows, parts=parts, print_result=True)
    run_with_measurment(part_two, workflows=workflows, print_result=True)