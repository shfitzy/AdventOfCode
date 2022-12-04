import os

file_path = os.path.dirname(os.path.realpath(__file__))

def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()

def map_char_to_value(char):
    char_value = ord(char)
    if char_value >= ord('a') and char_value <= ord('z'):
        return char_value - (ord('a') - 1)
    elif char_value >= ord('A') and char_value <= ord('Z'):
        return char_value - (ord('A') - 1) + 26

def transform_input(input):
    return list(map(lambda line: list(map(lambda x: map_char_to_value(x), list(line))), input))

def calc_overlapping_values(input):
    print(sum([sum(set.intersection(set(line[:int(len(line) / 2)]), set(line[int(len(line) / 2):]))) for line in input]))

def calc_badge_values(input):
    print(sum([sum(set.intersection(set(input[i]), set(input[i + 1]), set(input[i + 2]))) for i in range(0, len(input), 3)]))

if __name__ == '__main__':
    input = transform_input(read_lines(file_path + os.path.sep + 'input.txt'))
    calc_overlapping_values(input)
    calc_badge_values(input)