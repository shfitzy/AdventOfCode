import math
import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def get_min_cubes_for_game(game):
    red, green, blue = 0, 0, 0
    for game in game[1].split(";"):
        for cubes in game.split(","):
            count, color = cubes.strip().split(" ")
            count = int(count)
            if(color == "red" and count > red):
                red = count
            if(color == "green" and count > green):
                green = count
            if(color == "blue" and count > blue):
                blue = count

    return red, green, blue

def passes_check(line):
    red, green, blue = get_min_cubes_for_game(line)
    return red <= 12 and green <= 13 and blue <= 14

def solution_1(data):
    print(sum([int(line[0].split(" ")[1]) for line in data if passes_check(line)]))

def solution_2(data):
    print(sum([math.prod(get_min_cubes_for_game(line)) for line in data]))

if __name__ == '__main__':
    data = file_util.read_file(file_path, 'input.txt', split=True, split_str=":")

    solution_1(data)
    solution_2(data)