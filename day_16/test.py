# https://adventofcode.com/2022/day/16#part2


import time


def parse(file):
    valves = {}
    with open(file, 'r') as f:
        for line in f:
            step1 = line.strip('\n').split(';')
            first_half = step1[0].strip().split()
            valve = first_half[1].strip()
            flow = first_half[-1].strip().split('=')[-1].strip()
            second_half = step1[1].strip().split(',')
            next = [second_half[0].strip().split()[-1].strip()] + [x.strip() for x in second_half[1:]]
            valves[valve] = {'flow': int(flow), 'next': next}
    return valves


def solve(valve):
    global timer
    global valves
    global open
    global order
    global answer
    global max_time
    global prev

    next = valves[valve]['next']
    for n in next:        
        skip = valves[n]['next']
        for i, v in enumerate(next + skip):
            if len(order) >= 3 and v == order[-2] and order[-1] == order[-3]:
                continue
            elif i > len(next) - 1:
                if timer + 2 <= max_time:
                    for k in list(open.keys()):
                        open[k] += valves[k]['flow']
                    timer += 2
                    order.append(v)
                    solve(v)
                    prev = order
                    timer -= 2
                    total = sum(list(open.values()))
                    answer = total if total > answer else answer
                    order.pop()
                    for k in list(open.keys()):
                        open[k] -= valves[k]['flow']
                else:
                    return
            else:
                if timer + 2 <= max_time and v not in list(open.keys()) and valves[v]['flow'] != 0:
                    for k in list(open.keys()):
                        open[k] += valves[k]['flow'] * 2
                    open[v] = valves[v]['flow']
                    timer += 2
                    order.append(v)
                    solve(v)
                    timer -= 2
                    total = sum(list(open.values()))
                    answer = total if total > answer else answer
                    order.pop()
                    open.pop(v)
                    for k in list(open.keys()):
                        open[k] -= valves[k]['flow'] * 2
                elif timer + 1 <= max_time:
                    for k in list(open.keys()):
                        open[k] += valves[k]['flow']
                    timer += 1
                    order.append(v)
                    solve(v)
                    timer -= 1
                    total = sum(list(open.values()))
                    answer = total if total > answer else answer
                    order.pop()
                    for k in list(open.keys()):
                        open[k] -= valves[k]['flow']
                else:
                    return


if __name__ == '__main__':
    start_time = time.time()

    file = 'puzzle_test_inputs.txt'
    #file = 'puzzle_inputs.txt' 
    valves = parse(file)
    start_valve = list(valves.keys())[0]
    timer = 1
    open = {}
    order = [start_valve]
    answer = 0
    max_time = 30
    prev = []
    solve(start_valve) # test: puzzle:
    print(answer)

    print(f"--- {time.time() - start_time} seconds ---")