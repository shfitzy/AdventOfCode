import os

file_path = os.path.dirname(os.path.realpath(__file__))

def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()

def play_games_1(input):
    score = 0
    tmp = ord('A') - 1

    for game in input:
        opponent_move, my_move = (list(map(lambda x: ord(x[1]) - 23 - tmp if (x[0] == 1) else ord(x[1]) - tmp, enumerate(game.split()))))
        score += my_move
        if opponent_move == my_move:
            score += 3
        elif (my_move == 1 and opponent_move == 3) or (my_move == 2 and opponent_move == 1) or (my_move == 3 and opponent_move == 2):
            score += 6

    print(score)

def play_games_2(input):
    score = 0
    tmp = ord('A')

    for game in input:
        move_score, result = (list(map(lambda x: x[1] if (x[0] == 1) else ord(x[1]) - tmp, enumerate(game.split()))))
        if result == 'X':
            move_score = (move_score - 1) % 3 + 1
            score += move_score
            score += 0
        elif result == 'Y':
            move_score = move_score % 3 + 1
            score += move_score
            score += 3
        else:
            move_score = (move_score + 1) % 3 + 1
            score += move_score
            score += 6

    print(score)

if __name__ == '__main__':
    input = read_lines(file_path + os.path.sep + 'input.txt')
    play_games_1(input)
    play_games_2(input)