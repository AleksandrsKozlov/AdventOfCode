from measure_time import run_with_measurment
import numpy as np

def get_input():
    lines = open("2023/inputs/task11.txt").read().split("\n")
    image = np.array([[char for char in line] for line in lines])
    return image

def get_line_positions_to_add(image: np.ndarray):
    added_lines_pos = []
    for x, line in enumerate(image):
        if "#" not in line:
            added_lines_pos.append(x)
    return added_lines_pos

def get_galaxies_positions(image: np.ndarray, added_lines_pos: list[int], expansion_rate: int):
    added_columns_pos = []
    galaxies = []
    expanded_galaxies = []
    length, width = image.shape
    for y in range(width):
        should_add_column = True
        for x in range(length):
            if image[x,y] == "#":
                should_add_column = False
                added_lines = sum(line < x for line in added_lines_pos)
                galaxies.append((x + added_lines, y + len(added_columns_pos)))
                expanded_galaxies.append((x + added_lines*(expansion_rate-1), y + len(added_columns_pos)*(expansion_rate-1)))
        if should_add_column:
            added_columns_pos.append(y)
    return galaxies, expanded_galaxies

def both_parts(image: np.ndarray):
    added_lines_pos = []
    expansion_rate = 1000000
    added_lines_pos = get_line_positions_to_add(image)
    galaxies, expanded_galaxies = get_galaxies_positions(image, added_lines_pos, expansion_rate)

    distances = 0
    expanded_distances = 0
    for i in range(0, len(galaxies) - 1):
        for j in range(i, len(galaxies)):
            distances += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
            expanded_distances += abs(expanded_galaxies[i][0] - expanded_galaxies[j][0]) + abs(expanded_galaxies[i][1] - expanded_galaxies[j][1])
    return distances, expanded_distances

if __name__ == '__main__':
    image = run_with_measurment(get_input)
    run_with_measurment(both_parts, image=image, print_result=True)