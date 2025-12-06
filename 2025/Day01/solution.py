import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util
from utils.timer import timer

def execute_commands(input, value_function):
    value, dial_value = 0, 50
    
    dir = 'R'
    for i in input:
        new_dir, rotation = i[0], int(i[1:])
        if new_dir != dir:
            dial_value = 100 - dial_value
            dir = new_dir
        
        dial_value = (dial_value % 100) + rotation
        value += value_function(dial_value)

    return value

def solve_part_1(input):
    return execute_commands(input, lambda i: 1 if (i % 100 == 0) else 0)

def solve_part_2(input):
    return execute_commands(input, lambda i: i // 100)

if __name__ == '__main__':
    input = file_util.read(file_path, 'input.txt').split('\n')

    timer(solve_part_1, 'Part 1', 10, input)
    timer(solve_part_2, 'Part 2', 10, input)