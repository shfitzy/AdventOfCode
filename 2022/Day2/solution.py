import os

file_path = os.path.dirname(os.path.realpath(__file__))

def read_input_and_transform(filename):
    with open(filename) as f:
        return f.read().splitlines()

def get_result_score(my_move, opponent_move):
    if my_move == opponent_move: return 3
    elif my_move == (opponent_move + 1) % 3: return 6
    else: return 0

def get_game_score(my_move, opponent_move):
    return (my_move + 1) + get_result_score(my_move, opponent_move)

def part_1(line):
    return ord(line.split()[1]) - ord('X')

def part_2(line):
    return (['A', 'B', 'C'].index(line.split()[0]) + (['X', 'Y', 'Z'].index(line.split()[1]) - 1)) % 3

def play_games(input, algo=part_1):
    return sum([get_game_score(algo(line), ord(line.split()[0]) - ord('A')) for line in input])

if __name__ == '__main__':
    input = read_input_and_transform(file_path + os.path.sep + 'input.txt')
    
    print(play_games(input))
    print(play_games(input, algo=part_2))