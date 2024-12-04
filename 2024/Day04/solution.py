from collections import defaultdict
import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def xmas(data):
    count = 0

    for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 'X':
                    if i >= 3:
                        if data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-3][j] == 'S':
                            count += 1
                    if i >= 3 and j >= 3:
                        if data[i-1][j-1] == 'M' and data[i-2][j-2] == 'A' and data[i-3][j-3] == 'S':
                            count += 1
                    if j >= 3:
                        if data[i][j-1] == 'M' and data[i][j-2] == 'A' and data[i][j-3] == 'S':
                            count += 1
                    if i <= len(data) - 4 and j >= 3:
                        if data[i+1][j-1] == 'M' and data[i+2][j-2] == 'A' and data[i+3][j-3] == 'S':
                            count += 1
                    if i <= len(data) - 4:
                        if data[i+1][j] == 'M' and data[i+2][j] == 'A' and data[i+3][j] == 'S':
                            count += 1
                    if i <= len(data) - 4 and j <= len(data[i]) - 4:
                        if data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S':
                            count += 1
                    if j <= len(data[i]) - 4:
                        if data[i][j+1] == 'M' and data[i][j+2] == 'A' and data[i][j+3] == 'S':
                            count += 1
                    if i >= 3 and j <= len(data[i]) - 4:
                        if data[i-1][j+1] == 'M' and data[i-2][j+2] == 'A' and data[i-3][j+3] == 'S':
                            count += 1

    return count

def x_mas(data):
    return sum((data[i][j] == 'A') and ({data[i-1][j-1], data[i+1][j+1]} == {data[i-1][j+1], data[i+1][j-1]} == {'M', 'S'}) 
        for i in range(1, len(data) - 1)
        for j in range(1, len(data[i]) - 1)
    )

if __name__ == '__main__':
    data = [[c for c in line] for line in file_util.read_file(file_path, 'input.txt')]

    print(xmas(data))
    print(x_mas(data))