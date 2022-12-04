import os
import itertools

file_path = os.path.dirname(os.path.realpath(__file__))

def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()

def transform_input(input):
    input = list(map(lambda i: int(i) if i != '' else '', input))
    elf_calorie_totals = [sum(list(g)) for m, g in itertools.groupby(input, key=lambda x: x != '') if m]
    elf_calorie_totals.sort(reverse=True)

    return elf_calorie_totals

def calcTotalCalories(elf_calorie_totals, top=1):
    return sum(elf_calorie_totals[:top])

if __name__ == '__main__':
    input = read_lines(file_path + os.path.sep + 'input.txt')
    input = transform_input(input)

    print(calcTotalCalories(input))
    print(calcTotalCalories(input, 3))