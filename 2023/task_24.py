from measure_time import run_with_measurment
from z3 import Solver, Reals, sat

def get_input():
    lines = open("2023/inputs/task24.txt").read().split("\n")
    positions = []
    velocities = []
    for line in lines:
        position, velocity = line.split(" @ ")
        x, y, z = position.split(",")
        dx, dy, dz = velocity.split(",")
        positions.append((int(x),int(y),int(z)))
        velocities.append((int(dx),int(dy),int(dz)))
    return positions, velocities


def part_one(positions: list[tuple[int,int,int]], velocities: list[tuple[int,int,int]]):
    valid_intersections = 0
    min_range, max_range = (200000000000000, 400000000000000)
    for idx in range(len(positions) - 1):
        x1, y1, _ = positions[idx]
        dx1, dy1, _ = velocities[idx]
        for j in range(idx + 1, len(positions)):
            x2, y2, _ = positions[j]
            dx2, dy2, _ = velocities[j]
            if ((dy1/dx1) - (dy2/dx2)) == 0:
                continue
            x = ((x1 * dy1 / dx1) - (x2 * dy2 / dx2) - y1 + y2) / ((dy1/dx1) - (dy2/dx2))
            y = ((x - x1) * dy1 / dx1) + y1
            if (dx1 < 0 and x > x1) or (dx2 < 0 and x > x2) or (dy1 < 0 and y > y1) or (dy2 < 0 and y > y2):
                continue
            if (dx1 > 0 and x < x1) or (dx2 > 0 and x < x2) or (dy1 > 0 and y < y1) or (dy2 > 0 and y < y2):
                continue
            if x >= min_range and x <= max_range and y >= min_range and y <= max_range:
                valid_intersections += 1
    return valid_intersections


def part_two(positions: list[tuple[int,int,int]], velocities: list[tuple[int,int,int]]):
    x1, y1, z1 = positions[0]
    x2, y2, z2 = positions[1]
    x3, y3, z3 = positions[2]
    dx1, dy1, dz1 = velocities[0]
    dx2, dy2, dz2 = velocities[1]
    dx3, dy3, dz3 = velocities[2]

    x, y, z = Reals("x y z")
    dx, dy, dz = Reals("dx dy dz")
    t1, t2, t3 = Reals("t1 t2 t3")

    solver = Solver()

    equation1 = x + t1*dx == x1 + t1*dx1
    equation2 = y + t1*dy == y1 + t1*dy1
    equation3 = z + t1*dz == z1 + t1*dz1
    equation4 = x + t2*dx == x2 + t2*dx2
    equation5 = y + t2*dy == y2 + t2*dy2
    equation6 = z + t2*dz == z2 + t2*dz2
    equation7 = x + t3*dx == x3 + t3*dx3
    equation8 = y + t3*dy == y3 + t3*dy3
    equation9 = z + t3*dz == z3 + t3*dz3
    
    solver.add(
        equation1, equation2, equation3,
        equation4, equation5, equation6,
        equation7, equation8, equation9
    )
    if solver.check() == sat:
        model = solver.model()
        result_sum = 0
        for result in [x, y, z]:
            result_sum += model[result].as_long()
        return result_sum


if __name__ == '__main__':
    positions, velocities = run_with_measurment(get_input)
    run_with_measurment(part_one, positions=positions, velocities=velocities, print_result=True)
    run_with_measurment(part_two, positions=positions, velocities=velocities, print_result=True)