import os
import itertools

file_path = os.path.dirname(os.path.realpath(__file__))



class Board:

    def __init__(self, rows):
        self.combos = self.calc_winning_combos(rows)
        self.all_numbers = self.get_all_numbers(rows)
    
    def calc_winning_combos(self, rows):
        rows = list(map(lambda x: list(map(lambda x: int(x), x.split())), rows))
        winning_combos = []
        for i in range(5):
            winning_combos.append({rows[0][i], rows[1][i], rows[2][i], rows[3][i], rows[4][i]})
            winning_combos.append({rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4]})
        return winning_combos

    def get_all_numbers(self, rows):
        all_numbers = set()
        for row in rows:
            for num in row.split():
                all_numbers.add(int(num))
        return all_numbers

    def has_won(self, numbers_called):
        if any(list(map(lambda x: x.issubset(numbers_called), self.combos))):
            return self

    def calc_score(self, numbers_called, last_num):
        uncalled_numbers = list(map(lambda x: int(x), self.all_numbers - numbers_called))
        return sum(uncalled_numbers) * int(last_num)

    def __str__(self):
        return str(self.combos)



def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()

def generate_board_metadata(data):
    board_data = [list(g) for m, g in itertools.groupby(data, key=lambda x: x != '') if m]
    board_data = list(map(lambda b: Board(b), board_data))
    return board_data

def transform_input(input):
    numbers = list(map(lambda x: int(x), input[0].split(',')))
    boards = generate_board_metadata(input[2:])

    return (numbers, boards)

def check_for_winning_boards(called_numbers, boards):
    # return next((x for x in boards if x.has_won(called_numbers)), None)
    return filter(lambda board: board.has_won(called_numbers), boards)

def play_game(numbers, boards):
    called_numbers = set(numbers[0:4])
    for num in numbers[4:]:
        called_numbers.add(num)
        for board in check_for_winning_boards(called_numbers, boards):
            print(str(board.calc_score(called_numbers, num)) + ' (' + str(num) + ')')
            boards.remove(board)


if __name__ == '__main__':
    input = read_lines(file_path + os.path.sep + 'input.txt')
    numbers, boards = transform_input(input)
    play_game(*transform_input(input))
