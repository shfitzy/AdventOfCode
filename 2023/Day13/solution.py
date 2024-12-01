import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def check_symmetry(arrays):
    for i in range(1, len(arrays)):
        first = list(reversed(arrays[:i]))
        second = arrays[i:]

        for j in range(min(len(first), len(second))):
            if not first[j] == second[j]:
                break
            if j == min(len(first), len(second)) - 1:
                return len(first)
            
    return 0

def get_score(rows, columns):
    score = 100 * check_symmetry(rows)
    score += check_symmetry(columns)

    print(score)
    return score

def solution_1(patterns):
    sum = 0

    for pattern in patterns:
        rows = pattern.split();
        columns = [''.join(chars) for chars in list(zip(*rows))]

        sum += get_score(rows, columns)

    return sum

def solution_2(data):
    return data

if __name__ == '__main__':
    patterns = file_util.read(file_path, 'input.txt', split=True, split_str='\n\n')

    print(solution_1(patterns))
    # print(solution_2(data))