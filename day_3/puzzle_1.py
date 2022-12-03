# https://adventofcode.com/2022/day/3


def process_puzzle_inputs(file):
    inputs = []
    with open(file, 'r') as f:
        for line in f:
            inputs.append(line.strip('\n'))
    return inputs

def solve_puzzle(file):
    inputs = process_puzzle_inputs(file)
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    scores = dict(zip(alpha, list(range(1, 53))))   
    sum = 0
    for input in inputs:
        ruck_sack_1_items_count = dict(zip(alpha, ([0] * 52).copy()))
        ruck_sack_2_items_count = dict(zip(alpha, ([0] * 52).copy()))
        num_ruck_sack_items = int(len(input) / 2)
        ruck_sack_1 = input[:num_ruck_sack_items]
        ruck_sack_2 = input[num_ruck_sack_items:]
        item = ''
        i = 0
        while i < num_ruck_sack_items:
            ruck_sack_1_item = ruck_sack_1[i]
            ruck_sack_1_items_count[ruck_sack_1_item] += 1
            if ruck_sack_1_items_count[ruck_sack_1_item] > 0 and ruck_sack_2_items_count[ruck_sack_1[i]] > 0:
                item = ruck_sack_1_item
                break

            ruck_sack_2_item = ruck_sack_2[i]
            ruck_sack_2_items_count[ruck_sack_2_item] += 1
            if ruck_sack_2_items_count[ruck_sack_2_item] > 0 and ruck_sack_1_items_count[ruck_sack_2[i]] > 0:
                item = ruck_sack_2_item
                break
            i += 1
        sum += scores[item]
    return sum

    
if __name__ == '__main__':
    test_inputs = 'puzzle_test_inputs.txt'
    actual_inpus = 'puzzle_inputs.txt'
    print(solve_puzzle(test_inputs)) # 157
    print(solve_puzzle(actual_inpus)) # 7793