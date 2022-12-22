# https://adventofcode.com/2022/day/20


import time

def parse(file):
    inputs = []
    with open(file, 'r') as f:
        for line in f:
            inputs.append(int(line.strip('\n')))
    return inputs


def solve(file):
    inputs = parse(file)
    d = {}
    mod = len(inputs) - 1

    for idx, n in enumerate(inputs):
        d[idx] = [idx, n]

    for idx, n in enumerate(inputs):
        curr_idx = d[idx][0]
        if (curr_idx + n) == 0:
            new_idx = mod
        elif (curr_idx + n) == mod:
            new_idx = 0
        elif (curr_idx + n) > 0 and (curr_idx + n) < mod:
            new_idx = (curr_idx + n)
        else:
            new_idx = (curr_idx + n) % mod
        if new_idx > curr_idx:
            d = {k if True else k: [v[0] - 1, v[1]] if v[0] <= new_idx and v[0] > curr_idx and v[0] - 1 >= 0 else [v[0], v[1]]  for k, v in d.items()}
            d[idx] = [new_idx, n]
        elif new_idx < curr_idx:
            d = {k if True else k: [v[0] + 1, v[1]] if v[0] >= new_idx and v[0] < curr_idx and v[0] + 1 <= mod else [v[0], v[1]]  for k, v in d.items()}
            d[idx] = [new_idx, n]

    s = {v[0]: v[1] for _, v in d.items()}
    s = dict(sorted(s.items()))
    key = 0
    for k, v in s.items():
        if v == 0:
            key = k

    idx1 = (key + 1000) % len(inputs)
    idx2 = (key + 2000) % len(inputs)
    idx3 = (key + 3000) % len(inputs)
    val1 = s[idx1]
    val2 = s[idx2]
    val3 = s[idx3]
    answer = val1 + val2 + val3

    return answer
    
    
if __name__ == '__main__':
    start_time = time.time()

    file = 'puzzle_test_inputs.txt'
    file = 'puzzle_inputs.txt' 
    print(solve(file)) # test: 3, puzzle: 6640

    print(f"--- {time.time() - start_time} seconds ---")