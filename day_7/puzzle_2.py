# https://adventofcode.com/2022/day/7#part2  


def process_puzzle_inputs(file):
    with open(file, 'r') as f:
        commands = f.read().split('\n')
        file_system = {}
        dir_size = {}
        cwd = []
        for line in commands:
            if line[0] == '$':
                if line[2:4] == 'cd' and line[5:] != '..':
                    cwd.append(line[5:])
                    file_system[''.join(cwd)] = []
                    dir_size[''.join(cwd)] = 0
                elif line[2:4] == 'cd' and line[5:] == '..':
                    cwd.pop()
            elif line[0] in '0123456789':
                lst = line.split(' ')
                dir_size[''.join(cwd)] += int(lst[0])
            elif line[:3] == 'dir':
                file_system[''.join(cwd)].append(''.join(cwd) + line[4:])
    return file_system, dir_size


def solve_puzzle(current_dir):
    for dir in file_system[current_dir]:
        solve_puzzle(dir)
        dir_size[current_dir] += dir_size[dir]
        
    
if __name__ == '__main__':
    # test_inputs = 'puzzle_test_inputs.txt'
    # file_system, dir_size = process_puzzle_inputs(test_inputs)
    # root = list(file_system.keys())[0]
    # solve_puzzle(root)
    # system = 70000000
    # needed = 30000000
    # current = dir_size['/']
    # free = system - current
    # to_delete = needed - free
    # lst = list(filter(lambda x: x >= free, list(dir_size.values())))
    # dir_to_delete = min(lst)
    # print(dir_to_delete) # 24933642

    actual_inputs = 'puzzle_inputs.txt' 
    file_system, dir_size = process_puzzle_inputs(actual_inputs)
    root = list(file_system.keys())[0]
    solve_puzzle(root)
    system = 70000000
    needed = 30000000
    current = dir_size['/']
    free = system - current
    to_delete = needed - free
    lst = list(filter(lambda x: x >= to_delete, list(dir_size.values())))
    dir_to_delete = min(lst)
    print(dir_to_delete) # 8998590