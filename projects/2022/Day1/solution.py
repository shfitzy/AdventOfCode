import os

file_path = os.path.dirname(os.path.realpath(__file__))

def read_lines(filename):
    with open(filename) as f:
        return f.read().split('\n\n')

def transform_input(input):
    return sorted([sum(list(map(lambda i: int(i), row.split('\n')))) for row in input], reverse=True)

def calcTotalCalories(elf_calorie_totals, top=1):
    return sum(elf_calorie_totals[:top])

if __name__ == '__main__':
    input = read_lines(file_path + os.path.sep + 'input.txt')
    input = transform_input(input)

    print(calcTotalCalories(input))
    print(calcTotalCalories(input, 3))