# https://adventofcode.com/2022/day/13#part2


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
        inputs = inputs.replace('\n\n', '\n')
        inputs = inputs.replace(',', '')
        inputs = inputs.split('\n')
    return inputs


def sorted  (left, right):
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
        return True
    elif i == left_len and left_len <= right_len:
        return True
    elif j == right_len and left_len >= right_len:
        return True
    else:
        return False

def swap(left, right):
    temp = inputs[j-1]
    inputs[j-1] = inputs[j]
    inputs[j] = temp
    
    
if __name__ == '__main__':
    test_inputs = 'puzzle_test_inputs.txt'
    inputs = process_puzzle_inputs(test_inputs)
    inputs.append('[[c]]')
    inputs.append('[[g]]')
    i = 1
    answer = 1  
    while i < len(inputs):
        left = inputs[i-1]
        right = inputs[i]
        j = i
        while not sorted(left, right) and j > 0:
            swap(left, right)
            j -= 1
            left = inputs[j-1]
            right = inputs[j]
        i += 1
    for idx, row in enumerate(inputs):
        if row == '[[c]]':
            answer *= idx + 1
        if row == '[[g]]':
            answer *= idx + 1
    print(answer) # 140
    # for row in inputs:
    #     print(row) # 

    actual_inputs = 'puzzle_inputs.txt' 
    inputs = process_puzzle_inputs(actual_inputs)
    inputs.append('[[c]]')
    inputs.append('[[g]]')
    i = 1
    answer = 1  
    while i < len(inputs):
        left = inputs[i-1]
        right = inputs[i]
        j = i
        while not sorted(left, right) and j > 0:
            swap(left, right)
            j -= 1
            left = inputs[j-1]
            right = inputs[j]
        i += 1
    for idx, row in enumerate(inputs):
        if row == '[[c]]':
            answer *= idx + 1
        if row == '[[g]]':
            answer *= idx + 1
    print(answer) # 20383