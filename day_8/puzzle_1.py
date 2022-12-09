# https://adventofcode.com/2022/day/8

import numpy as np


def process_puzzle_inputs(file):
    inputs = []
    with open(file, 'r') as f:
        for line in f:
            row = [int(x) for x in line.strip('\n')]
            inputs.append(row)
    arr = np.array(inputs)
    return arr


def solve_puzzle(file):
    arr = process_puzzle_inputs(file)
    rows = arr.shape[0]
    cols = arr.shape[1]
    i = 1
    count = 0
    while i < rows - 1:
        j = 1
        while j < cols - 1:
            row = arr[i]
            row_eval = row - row[j]
            left = row_eval[:j+1]
            right = np.flip(row_eval[j:])
            if np.argmax(left) == j or np.argmax(right) == len(right) - 1:
                count += 1
                j += 1
                continue
            col = arr[:,j]
            col_eval = col - col[i]
            up = col_eval[:i+1]
            down = np.flip(col_eval[i:])
            if np.argmax(up) == i or np.argmax(down) == len(down) - 1:
                count +=1 
            j += 1
        i += 1    
    count += 2 * rows + 2 * (cols - 2)
    return count
 
    
if __name__ == '__main__':
    test_inputs = 'puzzle_test_inputs.txt'
    print(solve_puzzle(test_inputs)) # 21

    actual_inputs = 'puzzle_inputs.txt' 
    print(solve_puzzle(actual_inputs)) #  1794