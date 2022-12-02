# https://adventofcode.com/2022/day/2


def process_stragety_guide(file):
    strategy_guide = []
    with open(file, 'r') as f:
        for line in f:
            l = line.strip().split(' ')
            strategy_guide.append((l[0], l[1]))
    return strategy_guide
        

def get_score(file):
    games = process_stragety_guide(file)
    win = dict(zip(['A', 'B', 'C'], ['Y', 'Z', 'X']))
    draw = dict(zip(['A', 'B', 'C'], ['X', 'Y', 'Z']))
    scores =  dict(zip(['X', 'Y', 'Z'], [1, 2, 3]))
    score = 0
    for opponent, you in games:
        if draw[opponent] == you:
            score += 3
            score += scores[you]
        elif win[opponent] == you:
            score += 6
            score += scores[you]
        else:
            score += scores[you]
    return score

    
if __name__ == '__main__':
    test_inputs = 'puzzle_test_inputs.txt'
    actual_inpus = 'puzzle_inputs.txt'
    print(get_score(test_inputs)) # 15
    print(get_score(actual_inpus)) # 12586