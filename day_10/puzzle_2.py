# https://adventofcode.com/2022/day/10#part2


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


def draw(cycle_list):
    vert_pos = 0
    hor_pos = 0
    picture = ''
    for sprite in cycle_list.values():
        if (sprite - 1) == hor_pos or sprite == hor_pos or (sprite + 1) == hor_pos:
            picture += '#'
        else:
            picture += '.'
        hor_pos += 1
        if hor_pos > 39:
            picture += '\n'
            vert_pos += 1
            hor_pos = 0
    return picture

    
if __name__ == '__main__':
    # test_inputs = 'puzzle_test_inputs.txt'
    # cycle_list = generate_output(test_inputs)
    # print(draw(cycle_list))

    actual_inputs = 'puzzle_inputs.txt'
    cycle_list = generate_output(actual_inputs)
    print(draw(cycle_list)) #RGLRBZAU