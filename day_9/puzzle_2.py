# https://adventofcode.com/2022/day/9#part2


head = [(0, 0)]
node1 = [(0, 0)]
node2 = [(0, 0)]
node3 = [(0, 0)]
node4 = [(0, 0)]
node5 = [(0, 0)]
node6 = [(0, 0)]
node7 = [(0, 0)]
node8 = [(0, 0)]
node9 = [(0, 0)]


def process_puzzle_inputs(file):
    moves = []
    with open(file, 'r') as f:
        for line in f:
            moves.append(line.strip('\n'))         
    return moves


def move_head(direction):
    head_x = head[-1][0]
    head_y = head[-1][1]
    if direction == 'R':
        head.append((head_x + 1, head_y))
    elif direction == 'L':
        head.append((head_x - 1, head_y))
    elif direction == 'U':
        head.append((head_x, head_y + 1))
    elif direction == 'D':
        head.append((head_x, head_y - 1))
        

def move_tail(first_node, second_node):
    head_x = first_node[-1][0]
    head_y = first_node[-1][1]
    tail_x = second_node[-1][0]
    tail_y = second_node[-1][1]
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
        second_node.append((tail_x + 1, tail_y))
    elif head_x == tail_x - 2 and head_y == tail_y:
        second_node.append((tail_x - 1, tail_y))
    elif head_y == tail_y + 2 and head_x == tail_x:
        second_node.append((tail_x, tail_y + 1))
    elif head_y == tail_y - 2 and head_x == tail_x:
        second_node.append((tail_x, tail_y - 1))
    # if behind diagonally 1, move diagonally 1
    elif head_x == tail_x + 1 and head_y == tail_y + 2:
        second_node.append((tail_x + 1, tail_y + 1))
    elif head_x == tail_x - 1 and head_y == tail_y + 2:
        second_node.append((tail_x - 1, tail_y + 1))
    elif head_x == tail_x + 1 and head_y == tail_y - 2:
        second_node.append((tail_x + 1, tail_y - 1))
    elif head_x == tail_x - 1 and head_y == tail_y - 2:
        second_node.append((tail_x - 1, tail_y - 1))
    elif head_x == tail_x + 2 and head_y == tail_y + 1:
        second_node.append((tail_x + 1, tail_y + 1))
    elif head_x == tail_x - 2 and head_y == tail_y + 1:
        second_node.append((tail_x - 1, tail_y + 1))
    elif head_x == tail_x + 2 and head_y == tail_y - 1:
        second_node.append((tail_x + 1, tail_y - 1))
    elif head_x == tail_x - 2 and head_y == tail_y - 1:
        second_node.append((tail_x - 1, tail_y - 1))
    # if behind diagonally 2, move diagonally 2
    elif head_x == tail_x + 2 and head_y == tail_y + 2:
        second_node.append((tail_x + 1, tail_y + 1))
    elif head_x == tail_x - 2 and head_y == tail_y + 2:
        second_node.append((tail_x - 1, tail_y + 1))
    elif head_x == tail_x + 2 and head_y == tail_y - 2:
        second_node.append((tail_x + 1, tail_y - 1))
    elif head_x == tail_x - 2 and head_y == tail_y - 2:
        second_node.append((tail_x - 1, tail_y - 1))


def solve_puzzle(file):
    moves = process_puzzle_inputs(file)
    for move in moves:
        move = move.strip()
        direction = move[0]
        distance = int(move[2:])
        while distance > 0:
            move_head(direction)
            move_tail(head, node1)
            move_tail(node1, node2)
            move_tail(node2, node3)
            move_tail(node3, node4)
            move_tail(node4, node5)
            move_tail(node5, node6)
            move_tail(node6, node7)
            move_tail(node7, node8)
            move_tail(node8, node9)
            distance -= 1
    return len(set(node9))

    
if __name__ == '__main__':
    # test_inputs = 'puzzle_test_inputs.txt'
    # print(solve_puzzle(test_inputs)) # 13

    actual_inputs = 'puzzle_inputs.txt' 
    print(solve_puzzle(actual_inputs)) # 2562