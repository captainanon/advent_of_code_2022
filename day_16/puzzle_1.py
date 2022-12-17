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


def permutations(v):
    global global_time
    global global_visited
    global answer
    global max_time

    ttv = dijkstra(v)    
    ttv = {k: v for k, v in ttv.items() if valves[k]['weight'] != 0 and k not in global_visited}
    for i in list(ttv.keys()):
        if global_time + ttv[i] + 1 >= max_time:
            return
        global_time += ttv[i] + 1
        global_visited = {k: v + valves[k]['weight'] * (ttv[i] + 1) for k, v in global_visited.items()}
        global_visited[i] = 0
        #global_visited[i] = valves[i]['weight']
        permutations(i)
        t_remaining = max_time - global_time
        global_visited = {k: v + valves[k]['weight'] * t_remaining for k, v in global_visited.items()}
        p = sum(list(global_visited.values()))
        answer = p if p > answer else answer
        global_time -= (ttv[i] + 1)
        global_visited = {k: v - valves[k]['weight'] * (ttv[i] + 1 + t_remaining) for k, v in global_visited.items()}
        global_visited.pop(i)

    
if __name__ == '__main__':
    start_time = time.time()

    file = 'puzzle_test_inputs.txt'
    #file = 'puzzle_inputs.txt' 
    valves = parse(file)
    v = list(valves.keys())[0]
    global_visited = {} 
    global_time = 0
    answer = 0
    max_time = 30
    permutations(v)
    print(answer) # test: 1651, puzzle: 2252 too low

    print(f"--- {time.time() - start_time} seconds ---")