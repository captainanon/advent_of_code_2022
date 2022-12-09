# https://adventofcode.com/2022/day/9


head_pos = [(0, 0)]
tail_pos = [(0, 0)]


def process_puzzle_inputs(file):
    moves = []
    with open(file, 'r') as f:
        for line in f:
            moves.append(line.strip('\n'))         
    return moves


def move_head(direction):
    head_x = head_pos[-1][0]
    head_y = head_pos[-1][1]
    if direction == 'R':
        head_pos.append((head_x + 1, head_y))
    elif direction == 'L':
        head_pos.append((head_x - 1, head_y))
    elif direction == 'U':
        head_pos.append((head_x, head_y + 1))
    elif direction == 'D':
        head_pos.append((head_x, head_y - 1))
        

def move_tail():
    head_x = head_pos[-1][0]
    head_y = head_pos[-1][1]
    tail_x = tail_pos[-1][0]
    tail_y = tail_pos[-1][1]
    # if next to or on top of one another, pass
    if head_x == tail_x + 1 and head_y == tail_y:
        pass
    elif head_x == tail_x and head_y == tail_y + 1:
        pass
    elif head_x == tail_x - 1 and head_y == tail_y:
        pass
    elif head_x == tail_x and head_y == tail_y - 1:
        pass
    elif head_x == tail_x + 1 and head_y == tail_y - 1:
        pass
    elif head_x == tail_x + 1 and head_y == tail_y + 1:
        pass
    elif head_x == tail_x - 1 and head_y == tail_y - 1:
        pass
    elif head_x == tail_x - 1 and head_y == tail_y + 1:
        pass
    elif head_x == tail_x and head_y == tail_y:
        pass
    # if directly behind horizontally or vertically, move horizontally or vertically
    elif head_x == tail_x + 2 and head_y == tail_y:
        tail_pos.append((tail_x + 1, tail_y))
    elif head_x == tail_x - 2 and head_y == tail_y:
        tail_pos.append((tail_x - 1, tail_y))
    elif head_y == tail_y + 2 and head_x == tail_x:
        tail_pos.append((tail_x, tail_y + 1))
    elif head_y == tail_y - 2 and head_x == tail_x:
        tail_pos.append((tail_x, tail_y - 1))
    # if behind diagonally, move diagonally
    elif head_x == tail_x + 1 and head_y == tail_y + 2:
        tail_pos.append((tail_x + 1, tail_y + 1))
    elif head_x == tail_x - 1 and head_y == tail_y + 2:
        tail_pos.append((tail_x - 1, tail_y + 1))
    elif head_x == tail_x + 1 and head_y == tail_y - 2:
        tail_pos.append((tail_x + 1, tail_y - 1))
    elif head_x == tail_x - 1 and head_y == tail_y - 2:
        tail_pos.append((tail_x - 1, tail_y - 1))
    elif head_x == tail_x + 2 and head_y == tail_y + 1:
        tail_pos.append((tail_x + 1, tail_y + 1))
    elif head_x == tail_x - 2 and head_y == tail_y + 1:
        tail_pos.append((tail_x - 1, tail_y + 1))
    elif head_x == tail_x + 2 and head_y == tail_y - 1:
        tail_pos.append((tail_x + 1, tail_y - 1))
    elif head_x == tail_x - 2 and head_y == tail_y - 1:
        tail_pos.append((tail_x - 1, tail_y - 1))


def solve_puzzle(file):
    moves = process_puzzle_inputs(file)
    for move in moves:
        move = move.strip()
        direction = move[0]
        distance = int(move[2:])
        while distance > 0:
            move_head(direction)
            move_tail()
            distance -= 1
    return len(set(tail_pos))

    
if __name__ == '__main__':
    # test_inputs = 'puzzle_test_inputs.txt'
    # print(solve_puzzle(test_inputs)) # 13

    actual_inputs = 'puzzle_inputs.txt' 
    print(solve_puzzle(actual_inputs)) # 6197