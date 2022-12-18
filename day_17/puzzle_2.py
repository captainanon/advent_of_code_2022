# https://adventofcode.com/2022/day/17#part2


import time


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

def find_rep():
    global floor
    global wind
    global wind_idx

    floor = set([(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)])
    rock_count = 0
   
    cache_floor = []
    cache_y_max = []
    cache_wind_idx = []
    cache_rock_type = []
    match = False

    while not match:
        rock_type = rock_count  % 5
        rock = init_rock(rock_type)
        move_rock(rock)
        rock_type += 1
        rock_count += 1
        y_max = max(floor, key=lambda x: x[1])[1]
        y_1 = max(floor, key=lambda x: x[1] if x[0] == 1 else 0)[1] - y_max
        y_2 = max(floor, key=lambda x: x[1] if x[0] == 2 else 0)[1] - y_max
        y_3 = max(floor, key=lambda x: x[1] if x[0] == 3 else 0)[1] - y_max
        y_4 = max(floor, key=lambda x: x[1] if x[0] == 4 else 0)[1] - y_max
        y_5 = max(floor, key=lambda x: x[1] if x[0] == 5 else 0)[1] - y_max
        y_6 = max(floor, key=lambda x: x[1] if x[0] == 6 else 0)[1] - y_max
        y_7 = max(floor, key=lambda x: x[1] if x[0] == 7 else 0)[1] - y_max
        current_floor = (set([(1, y_1), 
                              (2, y_2), 
                              (3, y_3), 
                              (4, y_4), 
                              (5, y_5), 
                              (6, y_6), 
                              (7, y_7)]))
        if current_floor in cache_floor:
            for f in cache_floor:
                if f == current_floor:
                    idx = cache_floor.index(f)
                    if wind_idx % len(wind) == cache_wind_idx[idx] and rock_type - 1 == cache_rock_type[idx]:
                        rock_rep = rock_count - (idx + 1)
                        prev_y_max = cache_y_max[idx]
                        match = True
                        break
        cache_floor.append(current_floor)
        cache_y_max.append(y_max)
        cache_wind_idx.append(wind_idx % len(wind))
        cache_rock_type.append(rock_type - 1)

    quotient = (max_rock_count - idx) // rock_rep
    rock_count = (idx + 1) + quotient * rock_rep
    floor = (set([(1, (y_1 + prev_y_max) + (y_max - prev_y_max ) * quotient), 
                (2, (y_2 + prev_y_max) + (y_max - prev_y_max ) * quotient), 
                (3, (y_3 + prev_y_max) + (y_max - prev_y_max ) * quotient), 
                (4, (y_4 + prev_y_max) + (y_max - prev_y_max ) * quotient), 
                (5, (y_5 + prev_y_max) + (y_max - prev_y_max ) * quotient), 
                (6, (y_6 + prev_y_max) + (y_max - prev_y_max ) * quotient), 
                (7, (y_7 + prev_y_max) + (y_max - prev_y_max ) * quotient)]))
    return floor, rock_count


if __name__ == '__main__':
    start_time = time.time()

    file = 'puzzle_test_inputs.txt'
    file = 'puzzle_inputs.txt' 

    wind = parse(file)
    max_rock_count = 1000000000000 
    wind_idx = 0
    floor, rock_count = find_rep()

    while rock_count < max_rock_count:
        rock_type = rock_count % 5
        rock = init_rock(rock_type)
        move_rock(rock)
        rock_type += 1
        rock_count += 1

    print(max(floor, key=lambda x: x[1])[1]) # test: 1514285714288, puzzle: 1584927536247

    print(f"--- {time.time() - start_time} seconds ---")