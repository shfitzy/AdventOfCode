import os
import re
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def calculate_possible_arrangements(springs, records, start_index=0, count=0):
    last_index = get_last_index_to_check(springs, records)

    for i in range(start_index, last_index):
        if is_match(springs, i, records[0]):
            if len(records) == 1:
                if no_more_confirmed_breaks(springs, i, records[0]):
                    count += 1
            else:
                # next_springs = springs[:i] + '#'*records[0] + '.' + springs[i + records[0] + 1:]
                count += calculate_possible_arrangements(springs, records[1:], i + records[0] + 1)

        if springs[i] == '#':
            return count
        # else:
        #     springs = springs[:i] + '.' + springs[i + 1:]
        
    return count

def get_last_index_to_check(springs, records):
    last_index = len(springs) - (sum(records) + len(records) - 2)
    for match in re.split('[\#\?]+', springs[last_index:]):
        last_index -= max(0, len(match) - 1)

    while springs[last_index - 1] == '.':
        last_index -= 1

    return last_index

def is_match(springs, index, record):
    if all(c == '#' or c == '?' for c in springs[index:index + record]):
        if not (index + record < len(springs) and springs[index + record] == '#'):
            return True
        
    return False

def no_more_confirmed_breaks(springs, index, record):
    return (index + record >= len(springs) or not any(c == '#' for c in springs[index + record:]))

def solution_1(data):
    return sum([calculate_possible_arrangements(row[0], [int(i) for i in row[1].split(',')]) for row in data])

def solution_2(data):
    sum = 0

    for row in data:
        springs = '?'.join([row[0]]*5).strip('.')
        records = [int(i) for i in ','.join([row[1]]*5).split(',')]
        value = calculate_possible_arrangements(springs, records)
        print(value)
        sum += value

    return sum

if __name__ == '__main__':
    data = file_util.read_file(file_path, 'input.txt', split=True)

    # print(solution_1(data))
    print(solution_2(data))