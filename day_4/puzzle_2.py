# https://adventofcode.com/2022/day/4#part2


def process_puzzle_inputs(file):
    inputs = []
    with open(file, 'r') as f:
        for line in f:
            inputs.append(line.strip('\n'))
    return inputs
    

def solve_puzzle(file):
    pass

    
if __name__ == '__main__':
    test_inputs = 'puzzle_test_inputs.txt'
    print(solve_puzzle(test_inputs)) # 

    # actual_inpus = 'puzzle_inputs.txt'
    # print(solve_puzzle(actual_inpus)) # 