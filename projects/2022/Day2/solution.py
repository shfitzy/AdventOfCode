import os

file_path = os.path.dirname(os.path.realpath(__file__))

MOVES = {'A': {'beats': 'C', 'score': 1}, 'B': {'beats': 'A', 'score': 2}, 'C': {'beats': 'B', 'score': 3}}

def read_input_and_transform(filename):
    with open(filename) as f:
        return f.read().splitlines()

def get_result_score(my_move, opponent_move):
    if MOVES[my_move] == MOVES[opponent_move]: return 3
    elif MOVES[my_move]['beats'] == opponent_move: return 6
    else: return 0

def get_game_score(my_move, opponent_move):
    return MOVES[my_move]['score'] + get_result_score(my_move, opponent_move)

def part_1(line):
    return chr(ord(line.split()[1]) - ord('X') + ord('A'))

def part_2(line):
    return chr((ord(line.split()[0]) - ord('A') + ['X', 'Y', 'Z'].index(line.split()[1]) - 1) % 3 + ord('A'))

def play_games(input, algo=part_1):
    return sum([get_game_score(algo(line), line.split()[0]) for line in input])

if __name__ == '__main__':
    input = read_input_and_transform(file_path + os.path.sep + 'input.txt')
    
    print(play_games(input))
    print(play_games(input, algo=part_2))