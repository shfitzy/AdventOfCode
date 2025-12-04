import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util
from utils.timer import timer

def solve(input):
    pass

if __name__ == '__main__':
    input = file_util.read(file_path, 'input.txt').split('\n')

    timer(solve, 'Part 1', 10, input)
    timer(solve, 'Part 2', 10, input)