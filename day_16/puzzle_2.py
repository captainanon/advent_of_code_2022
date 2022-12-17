# https://adventofcode.com/2022/day/16#part2


import time


def parse(file):
    inputs = []
    with open(file, 'r') as f:
        for line in f:
            pass
    return inputs


def solve(file):
    inputs = parse(file)
    pass 

    
if __name__ == '__main__':
    start_time = time.time()

    file = 'puzzle_test_inputs.txt'
    #file = 'puzzle_inputs.txt' 
    print(solve(file)) # test: puzzle:

    print(f"--- {time.time() - start_time} seconds ---")