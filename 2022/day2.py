move_map = {
  'A': 'rock', 
  'B': 'paper',
  'C': 'scissors',
  'X': 'rock',
  'Y': 'paper',
  'Z': 'scissors'
}
strategy_map = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
shape_score_map = {'rock': 1, 'paper': 2, 'scissors': 3}
outcome_score_map ={ 'lose': 0, 'draw': 3, 'win': 6}
x_beats_y = [('rock','scissors'), ('scissors', 'paper'), ('paper', 'rock')]

def outcome_calculator(your_move, their_move):
    if your_move == their_move:
        return 'draw'
    elif (your_move,their_move) in x_beats_y:
        return 'win'
    else:
        return 'lose'

def score_calc(your_move, their_move):
    outcome = outcome_calculator(your_move, their_move)
    outcome_score = outcome_score_map[outcome]

    shape_score = shape_score_map[your_move]
    return shape_score + outcome_score

def achieve_outcome(result, their_move):
    if result == 'draw':
        return their_move
    elif result == 'win':
        for x, y in x_beats_y:
            if y == their_move:
                return x 
    elif result == 'lose':
        for x, y in x_beats_y:
            if x == their_move:
                return y

def part1():
    your_total = 0
    with open('day2_input.txt', 'r') as rfile:
        for line in rfile:
            their_letter, your_letter = line.strip().split()
            your_move, their_move = move_map[your_letter], move_map[their_letter]
            your_total += score_calc(your_move, their_move)

    print(your_total)

def part2():
    your_total = 0
    with open('day2_input.txt', 'r') as rfile:
        for line in rfile:
            their_letter, your_letter = line.strip().split()
            their_move = move_map[their_letter]

            desired_outcome = strategy_map[your_letter]
            your_move = achieve_outcome(desired_outcome, their_move)
            your_total += score_calc(your_move, their_move)

    print(your_total)

if __name__ == '__main__':
    part1()
    part2()