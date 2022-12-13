# https://adventofcode.com/2022/day/13


def process_puzzle_inputs(file):
    with open(file, 'r') as f:
        inputs = f.read()
        inputs = inputs.replace('10', 'k')
        inputs = inputs.replace('0', 'a')
        inputs = inputs.replace('1', 'b')
        inputs = inputs.replace('2', 'c')
        inputs = inputs.replace('3', 'd')
        inputs = inputs.replace('4', 'e')
        inputs = inputs.replace('5', 'f')
        inputs = inputs.replace('6', 'g')
        inputs = inputs.replace('7', 'h')
        inputs = inputs.replace('8', 'i')
        inputs = inputs.replace('9', 'j')
        inputs = inputs.replace(',', '')
        inputs = [x.split('\n') for x in inputs.split('\n\n')]
    return inputs


def solve_puzzle(file):
    inputs = process_puzzle_inputs(file)
    indices = []
    for idx, input in enumerate(inputs):
        left = input[0]
        right = input[1]
        left_len = len(left)
        right_len = len(right)
        left_list_count = 0
        right_list_count = 0
        num = min(left_len, right_len)
        left_flag = 0
        right_flag = 0
        i = 0
        j = 0
        in_order = False
        while i < num and j < num:
            cl = left[i]
            cr = right[j]
            if cl == '[':
                left_list_count += 1
            if cl == ']':
                left_list_count -= 1
            if cr == '[':
                right_list_count += 1
            if cr == ']':
                right_list_count -= 1
            if cl == '[' and cr.isalpha():
                right_list_count += 1
                right_flag += 1
                i += 1
                continue
            if cl.isalpha() and cr == '[':
                left_list_count += 1
                left_flag += 1
                j += 1
                continue
            if left_list_count > right_list_count:
                break
            if left_list_count < right_list_count:
                in_order = True
                break
            if cl.isalpha() and cr.isalpha():
                if ord(cl) < ord(cr):
                    in_order = True
                    break
                elif ord(cl) > ord(cr):
                    break
            if left_flag > 0:
                left_list_count -= 1
                left_flag -= 1
                i -= 1
            if right_flag > 0:
                right_list_count -= 1
                right_flag -= 1
                j -= 1
            i += 1
            j += 1
        if in_order:
            indices.append(idx + 1)
        elif i == left_len and left_len <= right_len:
            indices.append(idx + 1)
        elif j == right_len and left_len >= right_len:
            indices.append(idx + 1)
    return sum(indices)
    
    
if __name__ == '__main__':
    test_inputs = 'puzzle_test_inputs.txt'
    print(solve_puzzle(test_inputs)) # 13

    actual_inputs = 'puzzle_inputs.txt' 
    print(solve_puzzle(actual_inputs)) # 5675