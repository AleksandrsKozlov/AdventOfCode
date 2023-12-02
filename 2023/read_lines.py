def read_lines(task_number: int):
    with open(f"2023/inputs/task{task_number}.txt") as f:
        return f.readlines()