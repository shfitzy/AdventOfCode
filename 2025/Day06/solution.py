import math
import os
import re
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util
from utils.timer import timer

def get_part_1_answer(problem):
    if problem[-1] == '+': return sum(map(int, problem[:len(problem)-1]))
    else: return math.prod(map(int, problem[:len(problem)-1]))

def solve_part_1(input):
    input = list(zip(*map(lambda line: re.split(r'\s+', line.strip()), input)))
    return sum([get_part_1_answer(problem) for problem in input])

def solve_part_2(input):
    input = [line[::-1] for line in input]
    
    value, start_idx = 0, 0
    for i in range(len(input[0])):
        operator = input[-1][i]
        if operator != ' ':
            str_matrix = [data[start_idx:i+1] for data in input[:len(input)-1]]
            operands = [int("".join(num).strip()) for num in list(zip(*str_matrix))]
            
            start_idx = i + 2

            if operator == '+': value += sum(operands)
            else: value += math.prod(operands)

    return value

if __name__ == '__main__':
    input = file_util.read(file_path, 'input.txt').split('\n')

    timer(solve_part_1, 'Part 1', 10, input)
    timer(solve_part_2, 'Part 2', 10, input)