# https://adventofcode.com/2022/day/8#part2

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
    i = 0
    count = []
    while i < rows:
        j = 0
        while j < cols:
            row = arr[i]
            left = np.flip(row[:j])
            left_count = 0
            if left.size != 0:
                if (left >= row[j]).sum() == 0:
                    left_count = left.size
                else:
                    left_count = np.argmax(left >= row[j]) + 1
            else:
                left_count = 0
            right = row[j:]
            right_count = 0
            right = np.delete(right, 0)
            if right.size != 0:
                if (right >= row[j]).sum() == 0:
                    right_count = right.size
                else:
                    right_count = np.argmax(right >= row[j]) + 1
            else:
                right_count = 0
            col = arr[:,j]
            up = np.flip(col[:i])
            up_count = 0 
            if up.size != 0:
                if (up >= col[i]).sum() == 0:
                    up_count = up.size
                else:
                    up_count = np.argmax(up >= col[i]) + 1
            else:
                up_count = 0
            down = col[i:]
            down_count = 0
            down = np.delete(down, 0)
            if down.size != 0:
                if (down >= col[i]).sum() == 0:
                    down_count = down.size
                else:
                    down_count = np.argmax(down >= col[i]) + 1
            else:
                down_count = 0
            count.append(left_count * right_count * up_count * down_count)
            j += 1
        i += 1    
    return max(count)
 
    
if __name__ == '__main__':
    test_inputs = 'puzzle_test_inputs.txt'
    print(solve_puzzle(test_inputs)) # 8

    actual_inputs = 'puzzle_inputs.txt' 
    print(solve_puzzle(actual_inputs)) # 199272  