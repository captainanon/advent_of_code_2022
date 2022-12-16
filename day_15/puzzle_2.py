# https://adventofcode.com/2022/day/15#part2

 
import re
import time


#file = 'puzzle_test_inputs.txt'
file = 'puzzle_inputs.txt'
d = {}
beacons = set()
sensors = set()


def l_1_norm(pt1, pt2):
     return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

 
def calc_x(k, v):
    return v - abs(k[1] - row)

 
def parse(file):
    with open(file) as f:
        input = f.read().strip().split('\n')
    for line in input:
        pair = [int(s) for s in re.findall('[-+]?\d+', line)]
        d[(pair[0], pair[1])] = l_1_norm((pair[0], pair[1]), (pair[2], pair[3]))
        sensors.add((pair[0], pair[1]))
        beacons.add((pair[2], pair[3]))


if __name__ == '__main__':
    start_time = time.time()
    parse(file)
    m = 4000000 # test: 20
    for row in range(0, m + 1):
        sensor_count = set([(x[0], x[0]) for x in sensors if x[1] == row and x[0] >= 0 and x[0] <= m])
        beacon_count = set([(x[0], x[0]) for x in beacons if x[1] == row and x[0] >= 0 and x[0] <= m])
        tot_range = sensor_count.union(beacon_count)
        curr_range = set()
        for k, v in d.items():
            x = calc_x(k, v)
            if x >= 0:
                curr_range.add((max(k[0] - x, 0), min(k[0] + x, m)))
        curr_range = list(curr_range) + list(sensor_count) + list(beacon_count)
        curr_range = sorted(curr_range, key=lambda x: x[0])
        i = 0
        start = curr_range[0][0]
        end = curr_range[0][1]
        while i < len(curr_range) - 1:
            next_start = curr_range[i + 1][0]
            next_end = curr_range[i + 1][1]
            if end + 1 >= next_start and end + 1 <= next_end:
                end = next_end
            i += 1
        if not (start == 0 and end == m):
            break
    col = end + 1
    answer = col * 4000000 + row
    print(answer) # test: 56000011, puzzle: 13340867187704
    print('time: ', time.time() - start_time)