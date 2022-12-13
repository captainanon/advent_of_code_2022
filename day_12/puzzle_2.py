# https://adventofcode.com/2022/day/12#part2


import numpy as np
from queue import PriorityQueue
import time


def process_puzzle_inputs(file):
    input = []
    with open(file, 'r') as f:
        for line in f:
            line = line.replace('S', "a")
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
    return distances[x_end, y_end]
     

if __name__ == '__main__':
    start_time = time.time()

    test_inputs = 'puzzle_test_inputs.txt'
    topo_map = process_puzzle_inputs(test_inputs)
    r, c = topo_map.shape
    start = np.where(topo_map == 1)
    start = list(zip(list(start[0]), list(start[1])))
    end_coord = np.where(topo_map == topo_map.max())
    x_end, y_end = end_coord[0][0], end_coord[1][0]
    last_path = np.inf
    for x, y in start:
        x_start, y_start = x, y
        visited = []
        distances = np.full((r, c), np.inf)
        distances[x_start, y_start] = 0
        curr_path = dijkstra(x_start, y_start)
        if curr_path < last_path:
            last_path = curr_path
    print(last_path) # 29

    actual_inputs = 'puzzle_inputs.txt'
    topo_map = process_puzzle_inputs(actual_inputs)
    r, c = topo_map.shape
    start = np.where(topo_map == 1)
    start = list(zip(list(start[0]), list(start[1])))
    end_coord = np.where(topo_map == topo_map.max())
    x_end, y_end = end_coord[0][0], end_coord[1][0]
    last_path = np.inf
    for x, y in start:
        x_start, y_start = x, y
        visited = []
        distances = np.full((r, c), np.inf)
        distances[x_start, y_start] = 0
        curr_path = dijkstra(x_start, y_start)
        if curr_path < last_path:
            last_path = curr_path
    print(last_path) # 388

    print(f"--- {time.time() - start_time} seconds ---")