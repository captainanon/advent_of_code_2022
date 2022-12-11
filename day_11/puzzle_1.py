# https://adventofcode.com/2022/day/11


def process_puzzle_inputs(file):
    monkeys = {}
    monkey  = 0
    with open(file, 'r') as f:
        for line in f:
            line = line.strip('\n')
            if 'Monkey' in line:
                line = line.strip(':')
                monkey = line[7:]
                monkeys[monkey] = {'items': [], 'operation': '', 'value': '', 'test': 0, 'true': 0, 'false': 0, 'inspection_count': 0}
            elif 'Starting' in line:
                line = line.split(':')
                items = [int(x) for x in line[1].split(',')]
                monkeys[monkey]['items'] += items
            elif 'Operation' in line:
                line = line.split(':')
                if '*' in line[1]:
                    monkeys[monkey]['operation'] = '*'
                elif '+' in line[1]:
                    monkeys[monkey]['operation'] = '+'
                line = line[1].split()
                value = line[-1]
                monkeys[monkey]['value'] = value
            elif 'Test' in line:
                test = int(line.split()[-1])
                monkeys[monkey]['test'] = test
            elif 'true' in line:
                true = int(line.split()[-1])
                monkeys[monkey]['true'] = true
            elif 'false' in line:
                false = int(line.split()[-1])
                monkeys[monkey]['false'] = false
    return monkeys


def solve_puzzle(file, rounds):
    monkeys = process_puzzle_inputs(file)
    for round in range(rounds):
        for monkey in monkeys:
            items = monkeys[monkey]['items'].copy()
            operation = monkeys[monkey]['operation']
            value = monkeys[monkey]['value']
            test = monkeys[monkey]['test']
            true = monkeys[monkey]['true']
            false = monkeys[monkey]['false']
            for item in items:
                monkeys[monkey]['inspection_count'] += 1
                monkeys[monkey]['items'].pop(0)
                if operation == '*':
                    if value == 'old':
                        new_value = (item * item) // 3
                    else:
                        new_value = (item * int(value)) // 3
                elif operation == '+':
                    if value == 'old':
                        new_value = (item + item) // 3
                    else:
                        new_value = (item + int(value)) // 3
                pass_to = str(true if new_value % test == 0 else false)
                monkeys[pass_to]['items'].append(new_value)
    inspection_counts = []
    for monkey in monkeys:
        inspection_counts.append(monkeys[monkey]['inspection_count'])
    inspection_counts = sorted(inspection_counts)
    return inspection_counts[-1] * inspection_counts[-2]
    
    
if __name__ == '__main__':
    rounds = 20
    test_inputs = 'puzzle_test_inputs.txt'
    print(solve_puzzle(test_inputs, rounds)) # 10605

    actual_inputs = 'puzzle_inputs.txt' 
    print(solve_puzzle(actual_inputs, rounds)) # 56120