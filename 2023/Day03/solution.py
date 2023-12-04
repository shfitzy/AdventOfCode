import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def get_numbers_around_point(data, tar_x, tar_y, replace=False):
    x_start = max(0, tar_x-1)
    x_end = min(len(data[tar_y]), tar_x+1)
    y_start = max(0, tar_y-1)
    y_end = min(len(data), tar_y+1)

    numbers = []

    for y in range(y_start, y_end + 1):
        substring = ''
        for x in range(x_start, x_end + 1):
            substring += data[y][x] if data[y][x].isdigit() else ','
            if replace: data[y] = data[y][0:x] + '.' + data[y][x+1:]
        
        if substring[0].isdigit():
            tmp_x = x_start - 1
            while tmp_x >= 0 and data[y][tmp_x].isdigit():
                substring = data[y][tmp_x] + substring
                if replace: data[y] = data[y][0:tmp_x] + '.' + data[y][tmp_x+1:]
                tmp_x -= 1
        
        if substring[len(substring) - 1].isdigit():
            tmp_x = x_end + 1
            while tmp_x < len(data[y]) and data[y][tmp_x].isdigit():
                substring += data[y][tmp_x]
                if replace: data[y] = data[y][0:tmp_x] + '.' + data[y][tmp_x+1:]
                tmp_x += 1

        substring = substring.strip(',')
        if len(substring) > 0:
            numbers.extend(substring.split(','))

    return numbers

def solution_1(data):
    part_numbers = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if(not data[i][j].isdigit() and not data[i][j] == '.'):
                part_numbers.extend(get_numbers_around_point(data, j, i, True))

    print(sum([int(num) for num in part_numbers]))

def solution_2(data):
    total_gear_ratio = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if(data[i][j] == '*'):
                nearby_numbers = get_numbers_around_point(data, j, i)
                if(len(nearby_numbers) == 2):
                    total_gear_ratio += int(nearby_numbers[0]) * int(nearby_numbers[1])

    print(total_gear_ratio)

if __name__ == '__main__':
    solution_1(file_util.read_file(file_path, 'input.txt'))
    solution_2(file_util.read_file(file_path, 'input.txt'))