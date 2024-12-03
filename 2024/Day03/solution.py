import os
import re
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

if __name__ == '__main__':
    data = file_util.read(file_path, 'input.txt')
    x = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", data)
    print(sum([int(y[4:-1].split(",")[0]) * int(y[4:-1].split(",")[1]) for y in x]))

    value = 0

    while True:
        i = data.find("don't()")
        if i == -1:
            tmp = data
        else:
            tmp = data[:i]

        x = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", tmp)
        value += sum([int(y[4:-1].split(",")[0]) * int(y[4:-1].split(",")[1]) for y in x])
        data = data[i:]

        nextIndex = data.find("do()")
        if nextIndex == -1:
            break
        else:
            data = data[nextIndex:]

    print(value)