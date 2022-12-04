import os

file_path = os.path.dirname(os.path.realpath(__file__))

# Transforms each row of data into an array containing the bounds of each range [first_start, first_end, second_start, second_end]
def read_input_and_transform(filename):
    with open(filename) as f:
        return [[int(i) for i in line.replace('-', ',').split(',')] for line in f.read().splitlines()]

def calculate_overlapping_pairs(input):
    complete_overlap_count, partial_overlap_count = 0, 0
    
    for line in input:
        first_start, first_end, second_start, second_end = line
        if (first_start <= second_start <= second_end <= first_end) or (second_start <= first_start <= first_end <= second_end):
            complete_overlap_count += 1
        elif not (first_start > second_end or first_end < second_start):
            partial_overlap_count += 1
    
    return[complete_overlap_count, complete_overlap_count + partial_overlap_count]

if __name__ == '__main__':
    input = read_input_and_transform(file_path + os.path.sep + 'input.txt')
    for i in calculate_overlapping_pairs(input): print(i)