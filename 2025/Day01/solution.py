import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

if __name__ == '__main__':
    input = file_util.read(file_path, 'input.txt').split('\n')

    value = 50
    password = 0
    for i in input:
        dir = 1 if i[0] == 'R' else -1
        num = int(i[1:])
        value = (value + dir * num) % 100
        if value == 0: password += 1

    print('Part 1: ', password)

    value = 50
    password = 0
    for i in input:
        dir = 1 if i[0] == 'R' else -1
        num = int(i[1:])
        prev_value = value
        value += + dir * num
        if value == 0 or value == 100: password += 1
        if value < 0:
            password += value * -1 // 100 + 1
            if prev_value % 100 == 0: password -= 1
        if value > 100: password += value // 100
        value = value % 100
        print(value)

    print('Part 2: ', password)