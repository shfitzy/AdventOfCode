import os

file_path = os.path.dirname(os.path.realpath(__file__))

def read_input_and_transform(filename):
    with open(filename) as f:
        return sorted([sum(list(map(lambda i: int(i), group.split('\n')))) for group in f.read().split('\n\n')], reverse=True)

def calcTotalCalories(elf_calorie_totals, top=1):
    return sum(elf_calorie_totals[:top])

if __name__ == '__main__':
    input = read_input_and_transform(file_path + os.path.sep + 'input.txt')

    print(calcTotalCalories(input))
    print(calcTotalCalories(input, 3))