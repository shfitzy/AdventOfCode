import os

file_path = os.path.dirname(os.path.realpath(__file__))

def read_lines(filename):
    with open(filename) as f:
        return f.read().splitlines()

def calculate_overlapping_pairs(input):
    complete_overlap_count = 0
    partial_overlap_count = 0
    for line in input:
        first, second = line.split(',')
        first_start, first_end = list(map(lambda x: int(x), first.split('-')))
        second_start, second_end = list(map(lambda x: int(x), second.split('-')))
        if (first_start <= second_start and first_end >= second_end) or (first_start >= second_start and first_end <= second_end):
            complete_overlap_count += 1
        if not (first_start > second_end or first_end < second_start):
            partial_overlap_count += 1
    
    print(complete_overlap_count)
    print(partial_overlap_count)

if __name__ == '__main__':
    input = read_lines(file_path + os.path.sep + 'input.txt')
    calculate_overlapping_pairs(input)