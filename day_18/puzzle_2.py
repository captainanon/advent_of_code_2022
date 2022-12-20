# https://adventofcode.com/2022/day/18#part2


import time
import collections


def parse(file):
    inputs = []
    with open(file, 'r') as f:
        for line in f:
            inputs.append(tuple([int(x) for x in line.strip('\n').split(',')]))
    return set(inputs)


def find_surface_area(inputs):
    points = list(inputs) 
    air = set()
    surface_area = 0
    for point in points:
        x = point[0]
        y = point[1]
        z = point[2]
        if (x + 1, y, z) not in inputs:
            surface_area += 1
            air.add((x + 1, y, z))
        if (x - 1, y, z) not in inputs:
            surface_area += 1
            air.add((x - 1, y, z))
        if (x, y + 1, z) not in inputs:
            surface_area += 1
            air.add((x, y + 1, z))
        if (x, y - 1, z) not in inputs:
            surface_area += 1
            air.add((x, y - 1, z))
        if (x, y, z + 1) not in inputs:
            surface_area += 1
            air.add((x, y, z + 1))
        if (x, y, z - 1) not in inputs:
            surface_area += 1
            air.add((x, y, z - 1))
    return surface_area, air


def get_surface_area_reduction(point, inputs):
    x = point[0]
    y = point[1]
    z = point[2]
    surface_area_reduction = 0
    if (x + 1, y, z) in inputs:
        surface_area_reduction += 1
    if (x - 1, y, z) in inputs:
        surface_area_reduction += 1
    if (x, y + 1, z) in inputs:
        surface_area_reduction += 1
    if (x, y - 1, z) in inputs:
        surface_area_reduction += 1
    if (x, y, z + 1) in inputs:
        surface_area_reduction += 1
    if (x, y, z - 1) in inputs:
        surface_area_reduction += 1
    return surface_area_reduction


def remove_ext_surface_air(air, inputs):
    air = list(air)
    to_remove = set()
    for point in air:
        x = point[0]
        y = point[1]
        z = point[2]
        x_max = max(max(inputs, key=lambda i: i[0] if i[1] == y and i[2] == z else x)[0], x)
        x_min = min(min(inputs, key=lambda i: i[0] if i[1] == y and i[2] == z else x)[0], x)
        y_max = max(max(inputs, key=lambda i: i[1] if i[0] == x and i[2] == z else y)[1], y)
        y_min = min(min(inputs, key=lambda i: i[1] if i[0] == x and i[2] == z else y)[1], y)
        z_max = max(max(inputs, key=lambda i: i[2] if i[0] == x and i[1] == y else z)[2], z)
        z_min = min(min(inputs, key=lambda i: i[2] if i[0] == x and i[1] == y else z)[2], z)
        if x == x_max or x == x_min or y == y_max or y == y_min or z == z_max or z == z_min:
            to_remove.add(point)
    air = set(air).difference(to_remove)
    return air


def neighbors(point, inputs):
    neighbors = []
    escaped = False
    x = point[0]
    y = point[1]
    z = point[2]
    x_max = max(max(inputs, key=lambda i: i[0] if i[1] == y and i[2] == z else x)[0], x)
    x_min = min(min(inputs, key=lambda i: i[0] if i[1] == y and i[2] == z else x)[0], x)
    y_max = max(max(inputs, key=lambda i: i[1] if i[0] == x and i[2] == z else y)[1], y)
    y_min = min(min(inputs, key=lambda i: i[1] if i[0] == x and i[2] == z else y)[1], y)
    z_max = max(max(inputs, key=lambda i: i[2] if i[0] == x and i[1] == y else z)[2], z)
    z_min = min(min(inputs, key=lambda i: i[2] if i[0] == x and i[1] == y else z)[2], z)
    if x == x_max or x == x_min or y == y_max or y == y_min or z == z_max or z == z_min:
        escaped = True #return [-999]
    if (x + 1, y, z) not in inputs: 
        neighbors.append((x + 1, y, z))
    if (x - 1, y, z) not in inputs: 
        neighbors.append((x - 1, y, z))
    if (x, y + 1, z) not in inputs:
        neighbors.append((x, y + 1, z)) 
    if (x, y - 1, z) not in inputs:
        neighbors.append((x, y - 1, z)) 
    if (x, y, z + 1) not in inputs:
        neighbors.append((x, y, z + 1)) 
    if (x, y, z - 1) not in inputs:
        neighbors.append((x, y, z - 1)) 
    return neighbors, escaped


def bfs(inputs, root):
    global g_cannot_escape
    global g_escaped

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        point = queue.popleft()
        n, escaped = neighbors(point, inputs)
        if escaped: #n == [-999]:
            g_escaped.add(root)
            return 0
        for neighbour in n:
            if neighbour in g_cannot_escape:
                g_cannot_escape.add(root)
                return get_surface_area_reduction(root, inputs)
            if neighbour in g_escaped:
                g_escaped.add(root)
                return 0
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    g_cannot_escape.add(root)
    return get_surface_area_reduction(root, inputs)


if __name__ == '__main__':
    start_time = time.time()

    file = 'puzzle_test_inputs.txt'
    file = 'puzzle_inputs.txt' 
    inputs = parse(file)
    surface_area, air = find_surface_area(inputs)
    air = remove_ext_surface_air(air, inputs)
    air = list(air)
    g_escaped = set()
    g_cannot_escape = set()
    while len(air) > 0:
        root = air.pop()
        surface_area -= bfs(inputs, root)
    print(surface_area) # test: 58, puzzle: 2010

    print(f"--- {time.time() - start_time} seconds ---")