import os
import re
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def get_num_matches(line):
    nums, matching_nums = re.split('\s+\|\s+', line[1])
    matching_nums = {_ for _ in re.split('\s+', matching_nums)}
    return len([num for num in re.split('\s+', nums) if num in matching_nums])

def solution_1(data):
    return sum([(2**(matches - 1)) for line in data if (matches := get_num_matches(line)) > 0])

def solution_2(data):
    card_count = [1] * len(data)

    for i in range(len(data)):
        for j in range(get_num_matches(data[i])):
            card_count[i + j + 1] += card_count[i]
        
    return sum(card_count)

if __name__ == '__main__':
    data = file_util.read_file(file_path, 'input.txt', split=True, regex_split=True, split_str=':\s+')

    print(solution_1(data))
    print(solution_2(data))