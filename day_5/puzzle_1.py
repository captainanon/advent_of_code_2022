# https://adventofcode.com/2022/day/5
import string


def process_puzzle_inputs(file):
    alpha = string.ascii_uppercase
    with open(file, 'r') as f:
        #split pic from moves
        step_1 = f.read()
        step_2 = step_1.split('\n\n')
        pic = step_2[0].split('\n')
        moves = step_2[1].split('\n')
        # create stacks
        num = int(pic.pop()[-2])
        stacks = [[] for x in range(0, num)]
        for stack in pic:
            for i in range(1, len(stack), 4):
                if stack[i] in alpha:
                    idx = i // 4
                    stacks[idx].append(stack[i])
        # create moves
        moves_final = []
        for move in moves:
            lst1 = move.split(' ')
            lst2 = []
            for i in range(1, len(lst1), 2):
                lst2.append(int(lst1[i]))
            moves_final.append(lst2)
    return stacks, moves_final


def solve_puzzle(file):
    stacks, moves = process_puzzle_inputs(file)
    for move in moves:
        num = move[0]
        for i in range(0, num):
            box = stacks[move[1]-1].pop(0)
            stacks[move[2]-1] = [box] + stacks[move[2]-1]
    answer = ''
    for stack in stacks:
        answer += stack[0]
    return answer

    
if __name__ == '__main__':
    test_inputs = 'puzzle_test_inputs.txt'
    print(solve_puzzle(test_inputs)) # 'CMZ'

    actual_inputs = 'puzzle_inputs.txt' 
    print(solve_puzzle(actual_inputs)) # 'TWSGQHNHL'