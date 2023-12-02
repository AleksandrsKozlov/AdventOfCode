def read_lines(task_number: int):
    with open(f"inputs/task{task_number}.txt") as f:
        return f.readlines()