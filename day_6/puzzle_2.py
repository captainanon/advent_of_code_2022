# https://adventofcode.com/2022/day/6#part2


def process_puzzle_inputs(file):
    inputs = ''
    with open(file, 'r') as f:
        input = f.read().strip()
    return input


def solve_puzzle(file):
    signal = process_puzzle_inputs(file)
    message_len = 14
    i = 0
    while i < len(signal) - message_len:
        group = set(signal[i:i+message_len])
        if len(group) == message_len:
            return i + message_len
        i += 1

    
if __name__ == '__main__':
    test_inputs = 'puzzle_test_inputs.txt'
    print(solve_puzzle(test_inputs)) 

    actual_inputs = 'puzzle_inputs.txt' 
    print(solve_puzzle(actual_inputs)) # 2145