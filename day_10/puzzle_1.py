# https://adventofcode.com/2022/day/10


def process_puzzle_inputs(file):
    inputs = []
    with open(file, 'r') as f:
        for line in f:
            inputs.append(line.strip('\n').split())
    return inputs


def generate_output(file):
    cycles = process_puzzle_inputs(file)
    addx = 1
    clock = 1
    cycle_list = {}
    for cycle in cycles:
        if cycle[0] == 'addx':
                cycle_list[clock] = addx
                clock += 1
                cycle_list[clock] = addx
                clock += 1
                addx += int(cycle[1])
        else:
            cycle_list[clock] = addx
            clock +=1
    return cycle_list


def find_answer(start, stop, step, cycle_list):
    answer = 0 
    for i in range(start, stop, step):
        answer += i * cycle_list[i]
    return answer

    
if __name__ == '__main__':
    start = 20
    stop = 220 + 1
    step = 40
    test_inputs = 'puzzle_test_inputs.txt'
    cycle_list = generate_output(test_inputs)
    print(find_answer(start, stop, step, cycle_list)) # 1340

    start = 20
    stop = 220 + 1
    step = 40
    actual_inputs = 'puzzle_inputs.txt'
    cycle_list = generate_output(actual_inputs)
    print(find_answer(start, stop, step, cycle_list)) # 14420