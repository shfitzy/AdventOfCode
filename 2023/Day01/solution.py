import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

lookup_values_1 = {
    '1': ['1'],
    '2': ['2'],
    '3': ['3'],
    '4': ['4'],
    '5': ['5'],
    '6': ['6'],
    '7': ['7'],
    '8': ['8'],
    '9': ['9']
}

lookup_values_2 = {
    '1': ['1', 'one'],
    '2': ['2', 'two'],
    '3': ['3', 'three'],
    '4': ['4', 'four'],
    '5': ['5', 'five'],
    '6': ['6', 'six'],
    '7': ['7', 'seven'],
    '8': ['8', 'eight'],
    '9': ['9', 'nine']
}

def calc_calibration_level(line, lookup_values):
    first_index, last_index = len(line), -1
    tens_digit, ones_digit = '', ''

    for key in lookup_values.keys():
        for token in lookup_values.get(key):
            
            left_find = line.find(token)
            right_find = line.rfind(token)

            if left_find > -1 and left_find < first_index:
                first_index = left_find
                tens_digit = key

            if right_find > -1 and right_find + len(token) - 1 > last_index:
                last_index = right_find + len(token) - 1
                ones_digit = key

    return int(tens_digit + ones_digit)

if __name__ == '__main__':
    data = file_util.read_file(file_path, 'input.txt')

    print(sum([calc_calibration_level(line, lookup_values_1) for line in data]))
    print(sum([calc_calibration_level(line, lookup_values_2) for line in data]))