from measure_time import run_with_measurment
from copy import deepcopy


def get_input():
    lines = open("2023/inputs/task22.txt").read().split("\n")
    bricks = []
    for i, line, in enumerate(lines):
        l = line.strip()
        b1, b2 = l.split('~')
        x1, y1, z1 = map(int, b1.split(','))
        x2, y2, z2 = map(int, b2.split(','))
        if i < len('ABCDEFGHIJKLMNOQPRS'):
            brick_name = 'ABCDEFGHIJKLMNOPQRS'[i]
        else:
            brick_name = i
        bricks.append((x1, y1, z1, x2, y2, z2, brick_name))
    return bricks


def is_supported(brick, supported):
    x1, y1, z1, x2, y2, _, _ = brick
    z = z1 - 1
    if z == 0:
        return True
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if (x, y, z) in supported:
                return True
    return False

def do_fall(bricks):
    did_fall = False
    new_bricks = []
    supported = set()
    for (x1, y1, z1, x2, y2, z2, brick_name) in bricks:
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                supported.add((x, y, z2))

    for brick in bricks:
        x1, y1, z1, x2, y2, z2, brick_name = brick
        if not is_supported(brick, supported):
            did_fall = True
            z1 -= 1
            z2 -= 1
            new_brick = (x1, y1, z1, x2, y2, z2, brick_name)
            new_bricks.append(new_brick)
        else:
            new_bricks.append(brick)
    return did_fall, new_bricks


def fall_all(bricks):
    did_fall = True
    while did_fall:
        bricks = sorted(bricks, key=lambda coord: coord[2])
        did_fall, bricks = do_fall(bricks)
    return bricks


def part_one(bricks):
    bricks = fall_all(bricks)
    disintegrate = 0
    for idx, _ in enumerate(bricks):
        bricks_copy = deepcopy(bricks)
        del bricks_copy[idx]
        did_fall, _ = do_fall(bricks_copy)
        if not did_fall:
            disintegrate += 1
    return disintegrate


def part_two(bricks):
    bricks = fall_all(bricks)
    stacked_bricks = set(bricks)
    block_falls = 0
    for idx, _ in enumerate(bricks):
        bricks_copy = deepcopy(bricks)
        del bricks_copy[idx]
        did_fall = True
        while did_fall:
            did_fall, bricks_copy = do_fall(bricks_copy)
        new_stack = set(bricks_copy)
        block_falls += int((len(stacked_bricks ^ new_stack)-1) / 2)
    return block_falls


if __name__ == '__main__':
    bricks = run_with_measurment(get_input)
    run_with_measurment(part_one, bricks=deepcopy(bricks), print_result=True)
    run_with_measurment(part_two, bricks=deepcopy(bricks), print_result=True)