import os, string

file_path = os.path.dirname(os.path.realpath(__file__))

ALPHABET = string.ascii_lowercase + string.ascii_uppercase

# Transforms each row of data into an array containing the "value" for each character within the string
def read_input_and_transform(filename):
    with open(filename) as f:
        return [[(ALPHABET.index(c) + 1) for c in list(line)] for line in f.read().splitlines()]

def calc_overlapping_values(input):
    return sum([sum(set.intersection(set(line[:(len(line) // 2)]), set(line[(len(line) // 2):]))) for line in input])

def calc_badge_values(input):
    return sum([sum(set.intersection(set(input[i]), set(input[i + 1]), set(input[i + 2]))) for i in range(0, len(input), 3)])

if __name__ == '__main__':
    input = read_input_and_transform(file_path + os.path.sep + 'input.txt')
    
    print(calc_overlapping_values(input))
    print(calc_badge_values(input))