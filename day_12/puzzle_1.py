# https://adventofcode.com/2022/day/12


import numpy as np
from queue import PriorityQueue


def process_puzzle_inputs(file):
    input = []
    with open(file, 'r') as f:
        for line in f:
            line = line.replace('S', "`")
            line = line.replace('E', "{")
            row = [ord(x) - 96 for x in line.strip('\n')]
            input.append(row)
    topo_map = np.array(input)
    return topo_map


def find_moves(x, y):
    val = topo_map[x, y]
    #top row
    if x == 0:
        if y == 0:
            return [(x, y+1), (x+1, y)]
        elif y == c - 1:
            return [(x, y-1), (x+1, y)]
        else:
            return [(x, y+1), (x, y-1), (x+1, y)]
    #bottom row
    elif x == r - 1:
        if y == 0:
            return [(x, y+1), (x-1, y)]
        elif y == c - 1:
            return [(x, y-1), (x-1, y)]
        else:
            return [(x, y+1), (x, y-1), (x-1, y)]
    #left column
    elif y == 0: # and x != 0 and x != r - 1:
        return [(x, y+1), (x-1, y), (x+1, y)]
    #right column
    elif y == c - 1: # and x != 0 and x != r - 1
        return [(x, y-1), (x-1, y), (x+1, y)]
    #middle
    else:
        return [(x, y+1), (x, y-1), (x-1, y), (x+1, y)]


def dijkstra(x_start, y_start):
    step_size = 1
    pq = PriorityQueue()
    pq.put((0, (x_start, y_start)))
    while not pq.empty():
        _, curr_coords = pq.get()
        visited.append(curr_coords)
        moves = find_moves(curr_coords[0], curr_coords[1])
        for neighbor in moves:
            distance = topo_map[neighbor[0], neighbor[1]] - topo_map[curr_coords[0], curr_coords[1]]
            if distance > 1:
                pass
            else:
                if neighbor not in visited:
                    old_cost = distances[neighbor[0], neighbor[1]]
                    new_cost = distances[curr_coords[0], curr_coords[1]] + step_size
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        distances[neighbor[0], neighbor[1]] = new_cost
     

if __name__ == '__main__':
    test_inputs = 'puzzle_test_inputs.txt'
    topo_map = process_puzzle_inputs(test_inputs)
    r, c = topo_map.shape
    start_coord = np.where(topo_map == topo_map.min())
    x_start, y_start = start_coord[0][0], start_coord[1][0]
    end_coord = np.where(topo_map == topo_map.max())
    x_end, y_end = end_coord[0][0], end_coord[1][0]
    visited = []
    not_visited = []
    for m in range(0, r):
        for n in range(0, c):
            not_visited.append((m, n))
    not_visited.remove((x_start, y_start))
    distances = np.full((r, c), np.inf)
    distances[x_start, y_start] = 0
    dijkstra(x_start, y_start)
    print(distances[x_end, y_end]) # 31

    actual_inputs = 'puzzle_inputs.txt'
    topo_map = process_puzzle_inputs(actual_inputs)
    r, c = topo_map.shape
    start_coord = np.where(topo_map == topo_map.min())
    x_start, y_start = start_coord[0][0], start_coord[1][0]
    end_coord = np.where(topo_map == topo_map.max())
    x_end, y_end = end_coord[0][0], end_coord[1][0]
    visited = []
    not_visited = []
    for m in range(0, r):
        for n in range(0, c):
            not_visited.append((m, n))
    not_visited.remove((x_start, y_start))
    distances = np.full((r, c), np.inf)
    distances[x_start, y_start] = 0
    dijkstra(x_start, y_start)
    print(distances[x_end, y_end]) # 394