# https://adventofcode.com/2022/day/4


def process_puzzle_inputs(file):
    inputs = []
    with open(file, 'r') as f:
        for line in f:
            step1 = line.strip('\n')
            step2 = step1.split(',')
            step3 = [x.split('-') for x in step2]
            step4a = (int(step3[0][0]), int(step3[0][1]))
            step4b = (int(step3[1][0]), int(step3[1][1]))
            inputs.append((step4a, step4b))
    return inputs


def solve_puzzle(file):
    elves = process_puzzle_inputs(file)
    count = 0
    for pair in elves:
        set1 = set(range(pair[0][0], pair[0][1] + 1))
        set2 = set(range(pair[1][0], pair[1][1] + 1))
        intersection = set1.intersection(set2)
        if  intersection == set1 or intersection == set2:
            count +=1
    return count  

    
if __name__ == '__main__':
    test_inputs = 'puzzle_test_inputs.txt'
    print(solve_puzzle(test_inputs)) 

    actual_inpus = 'puzzle_inputs.txt' # 2
    print(solve_puzzle(actual_inpus)) # 500