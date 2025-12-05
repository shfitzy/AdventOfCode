import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util
from utils.timer import timer

def preprocess_input(input):
    ranges, ids = input.split('\n\n')

    ranges = [list(map(int, r.split('-'))) for r in ranges.split('\n')]
    ranges = sorted(ranges, key = lambda item: item[0])
    
    ids = list(map(int, ids.split('\n')))

    fresh_ingredient_ranges = [ranges[0]]
    for r in ranges[1:]:
        if r[0] <= fresh_ingredient_ranges[-1][1] + 1:
            if r[1] > fresh_ingredient_ranges[-1][1]:
                fresh_ingredient_ranges[-1][1] = r[1]
        else:
            fresh_ingredient_ranges.append(r)

    return fresh_ingredient_ranges, ids

def solve_part_1(input):
    ranges, ids = preprocess_input(input)
    return sum([len([1 for r in ranges if id >= r[0] and id <= r[1]]) for id in ids])

def solve_part_2(input):
    return sum([(r[1] - r[0] + 1) for r in preprocess_input(input)[0]])

if __name__ == '__main__':
    input = file_util.read(file_path, 'input.txt')

    timer(solve_part_1, 'Part 1', 10, input)
    timer(solve_part_2, 'Part 2', 10, input)