# https://adventofcode.com/2022/day/3#part2


def process_puzzle_inputs(file):
    inputs = []
    tup_list = []
    with open(file, 'r') as f:
        for line in f:
            inputs.append(line.strip('\n'))
        for i in range(0, len(inputs)-2, 3):
            tup_list.append((inputs[i], inputs[i+1], inputs[i+2]))
    return tup_list

def solve_puzzle(file):
    inputs = process_puzzle_inputs(file)
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    scores = dict(zip(alpha, list(range(1, 53))))   
    sum = 0
    for input in inputs:
        ruck_sack_1_items_count = dict(zip(alpha, ([0] * 52).copy()))
        ruck_sack_2_items_count = dict(zip(alpha, ([0] * 52).copy()))
        ruck_sack_3_items_count = dict(zip(alpha, ([0] * 52).copy()))
        badge = ''
        for item in input[0]:
            ruck_sack_1_items_count[item] += 1
            if ruck_sack_1_items_count[item] > 0 and ruck_sack_2_items_count[item] > 0 and ruck_sack_3_items_count[item] > 0:
                badge = item
                break
        for item in input[1]:
            ruck_sack_2_items_count[item] += 1
            if ruck_sack_1_items_count[item] > 0 and ruck_sack_2_items_count[item] > 0 and ruck_sack_3_items_count[item] > 0:
                badge = item
                break
        for item in input[2]:
            ruck_sack_3_items_count[item] += 1
            if ruck_sack_1_items_count[item] > 0 and ruck_sack_2_items_count[item] > 0 and ruck_sack_3_items_count[item] > 0:
                badge = item
                break
        sum += scores[badge]
    return sum


def alt_process_puzzle_inputs(file):
    inputs = []
    with open(file, 'r') as f:
        for line in f:
            inputs.append(line.strip('\n'))
    return inputs


def alt_solve_puzzle(file):
    sacks = alt_process_puzzle_inputs(file)
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    scores = dict(zip(alpha, list(range(1, 53)))) 
    score = 0
    num = len(sacks)
    for i in range(0, num, 3):
        sack_1 = set(sacks[i])
        sack_2 = set(sacks[i+1])
        sack_3 = set(sacks[i+2])
        badge = list((sack_1 & sack_2 & sack_3))[0] # intersection of sets
        score += scores[badge]
    return score


if __name__ == '__main__':
    test_inputs = 'puzzle_test_inputs.txt'
    actual_inpus = 'puzzle_inputs.txt'

    print(solve_puzzle(test_inputs)) # 70
    print(solve_puzzle(actual_inpus)) # 2499

    print(alt_solve_puzzle(test_inputs)) # 157
    print(alt_solve_puzzle(actual_inpus)) # 7793