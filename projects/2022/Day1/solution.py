import os
import itertools

file_path = os.path.dirname(os.path.realpath(__file__))

def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()

def transform_input(input):
    return sorted([sum(list(map(lambda i: int(i), g))) for m, g in itertools.groupby(input, key=lambda x: x != '') if m], reverse=True)

def calcTotalCalories(elf_calorie_totals, top=1):
    return sum(elf_calorie_totals[:top])

if __name__ == '__main__':
    input = read_lines(file_path + os.path.sep + 'input.txt')
    input = transform_input(input)

    print(calcTotalCalories(input))
    print(calcTotalCalories(input, 3))