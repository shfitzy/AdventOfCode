import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def extrapolate_data(line):
    data = [line]

    while not all(x == 0 for x in line):
        line = [line[i+1] - line[i] for i, x in enumerate(line) if i < len(line) - 1]
        data.append(line)

    return data

def solution_1(data):
    return sum([sum([data[-1] for data in extrapolate_data(line)]) for line in data])

def solution_2(data):
    return sum([sum([data[0] * ((-1)**i) for i, data in enumerate(extrapolate_data(line))]) for line in data])

if __name__ == '__main__':
    data = file_util.read_file(file_path, 'input.txt', split=True, map=lambda x: int(x))

    print(solution_1(data))
    print(solution_2(data))