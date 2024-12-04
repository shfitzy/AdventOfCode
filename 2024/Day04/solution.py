import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

if __name__ == '__main__':
    data = file_util.read_file(file_path, 'input.txt')
    array = [[c for c in line] for line in data]

    count_1 = 0
    count_2 = 0
    
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 'X':
                if i >= 3:
                    if array[i-1][j] == 'M' and array[i-2][j] == 'A' and array[i-3][j] == 'S':
                        count_1 += 1
                if i >= 3 and j >= 3:
                    if array[i-1][j-1] == 'M' and array[i-2][j-2] == 'A' and array[i-3][j-3] == 'S':
                        count_1 += 1
                if j >= 3:
                    if array[i][j-1] == 'M' and array[i][j-2] == 'A' and array[i][j-3] == 'S':
                        count_1 += 1
                if i <= len(array) - 4 and j >= 3:
                    if array[i+1][j-1] == 'M' and array[i+2][j-2] == 'A' and array[i+3][j-3] == 'S':
                        count_1 += 1
                if i <= len(array) - 4:
                    if array[i+1][j] == 'M' and array[i+2][j] == 'A' and array[i+3][j] == 'S':
                        count_1 += 1
                if i <= len(array) - 4 and j <= len(array[i]) - 4:
                    if array[i+1][j+1] == 'M' and array[i+2][j+2] == 'A' and array[i+3][j+3] == 'S':
                        count_1 += 1
                if j <= len(array[i]) - 4:
                    if array[i][j+1] == 'M' and array[i][j+2] == 'A' and array[i][j+3] == 'S':
                        count_1 += 1
                if i >= 3 and j <= len(array[i]) - 4:
                    if array[i-1][j+1] == 'M' and array[i-2][j+2] == 'A' and array[i-3][j+3] == 'S':
                        count_1 += 1

    for i in range(len(array) - 2):
        for j in range(len(array[i]) - 2):
            if array[i+1][j+1] == 'A':
                x_1 = array[i][j] + array[i+2][j+2]
                x_2 = array[i+2][j] + array[i][j+2]
                if x_1 in {'MS', 'SM'} and x_2 in {'MS', 'SM'}:
                    count_2 += 1

    print(count_1)
    print(count_2)