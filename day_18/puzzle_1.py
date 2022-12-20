# https://adventofcode.com/2022/day/18


import time


def parse(file):
    inputs = []
    with open(file, 'r') as f:
        for line in f:
            inputs.append(tuple([int(x) for x in line.strip('\n').split(',')]))
    return set(inputs)


def solve(file):
    inputs = parse(file)
    points = list(inputs) 
    surface_area = 0
    for point in points:
        pocket = 0
        x = point[0]
        y = point[1]
        z = point[2]
        if (x + 1, y, z) not in inputs:
            surface_area += 1
        if (x - 1, y, z) not in inputs:
            surface_area += 1
        if (x, y + 1, z) not in inputs:
            surface_area += 1
        if (x, y - 1, z) not in inputs:
            surface_area += 1
        if (x, y, z + 1) not in inputs:
            surface_area += 1
        if (x, y, z - 1) not in inputs:
            surface_area += 1
    return surface_area


if __name__ == '__main__':
    start_time = time.time()

    file = 'puzzle_test_inputs.txt'
    file = 'puzzle_inputs.txt' 
    print(solve(file)) # test: 64, puzzle: 3374

    print(f"--- {time.time() - start_time} seconds ---")