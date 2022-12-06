# https://adventofcode.com/2022/day/6


def process_puzzle_inputs(file):
    inputs = ''
    with open(file, 'r') as f:
        input = f.read().strip()
    return input


def solve_puzzle(file):
    signal = process_puzzle_inputs(file)
    sig_len = 4
    i = 0
    while i < len(signal) - 4:
        group = set(signal[i:i+4])
        if len(group) == 4:
            return i + 4
        i += 1

    
if __name__ == '__main__':
    test_inputs = 'puzzle_test_inputs.txt'
    print(solve_puzzle(test_inputs))

    actual_inputs = 'puzzle_inputs.txt' 
    print(solve_puzzle(actual_inputs)) # 1544