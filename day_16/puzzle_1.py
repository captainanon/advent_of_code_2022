# https://adventofcode.com/2022/day/16


import numpy as np
from queue import PriorityQueue
import time


def parse(file):
    valves = {}
    with open(file, 'r') as f:
        for line in f:
            step1 = line.strip('\n').split(';')
            first_half = step1[0].strip().split()
            node = first_half[1].strip()
            weight = first_half[-1].strip().split('=')[-1].strip()
            second_half = step1[1].strip().split(',')
            edges = [second_half[0].strip().split()[-1].strip()] + [x.strip() for x in second_half[1:]]
            valves[node] = {'weight': int(weight), 'edges': edges}
    return valves


def dijkstra(valve):
    ttv = {k: np.inf for k, _ in valves.items()}
    ttv[valve] = 0
    visited = []
    t = 1
    pq = PriorityQueue()
    pq.put((0, valve))
    while not pq.empty():
        _, node = pq.get()
        visited.append(node)
        moves = valves[node]['edges']
        for neighbor in moves:
            if neighbor not in visited:
                    old_cost = ttv[neighbor]
                    new_cost = ttv[node] + t
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        ttv[neighbor] = new_cost
    return ttv


def permutations(valve, delta_t):
    global global_time
    global global_visited
    global answer
    global max_time
    global mappings
    local_visited = global_visited.copy()
    local_time = global_time

    if global_time >= max_time:
        global_time -= delta_t
        t_remaining = max_time - global_time
        global_visited.pop(valve)
        global_visited = {k: v - valves[k]['weight'] * (delta_t) for k, v in global_visited.items()}
        global_visited = {k: v + valves[k]['weight'] * t_remaining for k, v in global_visited.items()}
        p = sum(list(global_visited.values()))
        answer = p if p > answer else answer
        return

    ttv = mappings[valve]
    ttv = {k: v for k, v in ttv.items() if valves[k]['weight'] != 0 and k not in list(global_visited.keys())}

    if ttv == {}:
        t_remaining = max_time - global_time
        global_visited = {k: v + valves[k]['weight'] * t_remaining for k, v in global_visited.items()}
        p = sum(list(global_visited.values()))
        answer = p if p > answer else answer
        return

    for i in list(ttv.keys()):
        global_visited = local_visited.copy()
        global_time = local_time
        global_time += ttv[i] + 1
        global_visited = {k: v + valves[k]['weight'] * (ttv[i] + 1) for k, v in global_visited.items()}
        global_visited[i] = 0 
        permutations(i, ttv[i] + 1)


if __name__ == '__main__':
    start_time = time.time()

    #file = 'puzzle_test_inputs.txt'
    file = 'puzzle_inputs.txt' 
    valves = parse(file)
    mappings = {}
    for valve in list(valves.keys()):
        mappings[valve] = dijkstra(valve)
        #mappings[valve].pop(valve)
    start_valve = 'AA'
    global_visited = {} 
    global_time = 0
    answer = 0
    max_time = 30
    permutations(start_valve, 0)
    print(answer) # test: 1651, puzzle: 2330

    print(f"--- {time.time() - start_time} seconds ---")