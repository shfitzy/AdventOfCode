import math
import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def get_winning_permutations_brute_force(duration, target):
    for i in range(duration):
        if i * (duration - i) > target:
            return (duration + 1) - (2 * i)

def get_winning_permutations_bisect(duration, target):
    start, end = 0, duration / 2
    while not start == end:
        check = int((start + end) / 2)
        if check * (duration - check) > target:
            end = check if not end == check else end - 1
        else:
            start = check if not start == check else start + 1

    return (duration + 1) - (2 * start)

def get_winning_permutations_quadratic_formula(duration, target):
    a, b, c = -1, duration, (-1) * target
    quadratic_formula_result =  math.floor(((-1)*b + math.sqrt(b**2 - 4*a*c)) / (2*a))
    
    return (duration - 1) - (2 * quadratic_formula_result)

def solution_1(data):
    return math.prod([get_winning_permutations_quadratic_formula(int(data[0][1:][i]), int(data[1][1:][i])) for i in range(len(data[0][1:]))])

def solution_2(data):
    return get_winning_permutations_quadratic_formula(int(''.join(data[0][1:])), int(''.join(data[1][1:])))

if __name__ == '__main__':
    data = file_util.read_file(file_path, 'test_input.txt', split=True, regex_split=True, split_str='\s+')

    print(solution_1(data))
    print(solution_2(data))