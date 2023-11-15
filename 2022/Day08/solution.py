# from itertools import reduce
import os

file_path = os.path.dirname(os.path.realpath(__file__))

def read_input_and_transform():
    with open(file_path + os.path.sep + 'input.txt') as f:
        return [[int(c) for c in line] for line in f.read().split()]

def calculate_los_map(input):
    los_map = [[0 for j in range(len(line))] for line in input]

    for i in range(len(input)):
        height_check = -1
        for j in range(len(input[i])):
            if j == 0 or input[i][j] > height_check:
                height_check = input[i][j]
                los_map[i][j] = 1
        
        height_check = -1
        for j in reversed(range(len(input[i]))):
            if j == len(input[i]) - 1 or input[i][j] > height_check:
                height_check = input[i][j]
                los_map[i][j] = 1

    for i in range(len(input[0])):
        height_check = -1
        for j in range(len(input)):
            if j == 0 or input[j][i] > height_check:
                height_check = input[j][i]
                los_map[j][i] = 1
        
        height_check = -1
        for j in reversed(range(len(input))):
            if j == len(input[i]) - 1 or input[j][i] > height_check:
                height_check = input[j][i]
                los_map[j][i] = 1

    return los_map

def calculate_scenic_scores(input):
    max_score = 0
    for i in range(len(input[0])):
        for j in range(len(input)):
            s1 = s2 = s3 = s4 = 0
            height = input[j][i]
            for x in reversed(range(i)):
                if x == 0 or height <= input[j][x]:
                    s1 = (i - x)
                    break
            for x in range(i + 1, len(input[0])):
                if x == len(input[0]) - 1 or height <= input[j][x]:
                    s2 = (x - i)
                    break
            for y in reversed(range(j)):
                if y == 0 or height <= input[y][i]:
                    s3 = (j - y)
                    break
            for y in range(j + 1, len(input[0])):
                if y == len(input) - 1 or height <= input[y][i]:
                    s4 = (y - j)
                    break
            
            if max_score < (s1 * s2 * s3 * s4): max_score = (s1 * s2 * s3 * s4)
    return max_score

def calculate_num_visible_trees(input):
    return sum([sum(line) for line in calculate_los_map(input)])

            
if __name__ == '__main__':
    input = read_input_and_transform()

    # los_map = calculate_los_map(input)
    # print(sum([sum(line) for line in los_map]))
    # [print(''.join(map(str, line))) for line in los_map]
    print(calculate_num_visible_trees(input))
    print(calculate_scenic_scores(input))