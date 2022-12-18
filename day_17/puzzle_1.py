# https://adventofcode.com/2022/day/17


import numpy as np
import time


floor = set([(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)])


def parse(file):
    with open(file, 'r') as f:
        wind = f.read().strip('\n')
    return wind


def init_rock(type):
    max_floor = max(floor, key=lambda x: x[1])[1]
    if type == 0:
        rock = set([(3, max_floor + 4), (4, max_floor + 4), (5, max_floor + 4), (6, max_floor + 4)])
    if type == 1:
        rock = set([(3, max_floor + 5), (4, max_floor + 4), (4, max_floor + 5), (4, max_floor + 6), (5, max_floor + 5)])
    if type == 2:
        rock = set([(3, max_floor + 4), (4, max_floor + 4), (5, max_floor + 4), (5, max_floor + 5), (5  , max_floor + 6)])
    if type == 3:
        rock = set([(3, max_floor + 4), (3, max_floor + 5), (3, max_floor + 6), (3, max_floor + 7)])
    if type == 4:
        rock = set([(3, max_floor + 4), (3, max_floor + 5), (4, max_floor + 4), (4, max_floor + 5)])
    return rock


def move_rock(rock):
    global floor
    global wind
    global wind_idx
  
    while True:
        wind_dir = wind[wind_idx % len(wind)]
        rock = list(rock)
        if wind_dir == '<':
            temp = set([(x[0] - 1, x[1]) for x in rock])
            if min(temp, key=lambda x: x[0])[0] > 0 and len(temp.intersection(floor)) == 0:
                rock = temp
            else:
                rock = set(rock)
        if wind_dir == '>':
            temp = set([(x[0] + 1, x[1]) for x in rock])
            if max(temp, key=lambda x: x[0])[0] < 8 and len(temp.intersection(floor)) == 0:
                rock = temp
            else:
                rock = set(rock)
        wind_idx += 1
        rock = list(rock)
        temp = set([(x[0], x[1] - 1) for x in rock])
        if len(temp.intersection(floor)) == 0:
            rock = temp
        else:
            rock = set(rock)
            break
    floor = floor.union(rock)
    
   
if __name__ == '__main__':
    start_time = time.time()

    #file = 'puzzle_test_inputs.txt'
    file = 'puzzle_inputs.txt' 
    wind = parse(file)
    max_rock_count = 2022
    rock_count = 0
    wind_idx = 0
    while rock_count < max_rock_count:
        rock_type = rock_count  % 5
        rock = init_rock(rock_type)
        move_rock(rock)
        rock_type += 1
        rock_count += 1
    print(max(floor, key=lambda x: x[1])[1]) # test: 3068, puzzle: 3200

    print(f"--- {time.time() - start_time} seconds ---")