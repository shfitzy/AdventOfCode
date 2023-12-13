import os
import sys
from itertools import combinations

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def get_galaxy_coords(data, universe_expansion_factor):
    expansion_rows = [i for i in range(len(data)) if not any(c == '#' for c in data[i])]
    expansion_columns = [i for i in range(len(data)) if not any(c == '#' for c in [''.join(s) for s in [*zip(*data)]][i])]

    galaxy_data = set()
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '#':
                x_coord = x + sum([universe_expansion_factor - 1 for expansion_column in expansion_columns if expansion_column < x])
                y_coord = y + sum([universe_expansion_factor - 1 for expansion_row in expansion_rows if expansion_row < y])
                galaxy_data.add((x_coord, y_coord))

    return galaxy_data

def calc_distances(galaxy_pairings):
    return sum([abs(pair[0][1] - pair[1][1]) + abs(pair[0][0] - pair [1][0]) for pair in galaxy_pairings])

def solution_1(data):
    galaxy_pairings = {combination for combination in combinations(get_galaxy_coords(data, 2), r=2)}
    return calc_distances(galaxy_pairings)

def solution_2(data):
    galaxy_pairings = {combination for combination in combinations(get_galaxy_coords(data, 1000000), r=2)}
    return calc_distances(galaxy_pairings)

if __name__ == '__main__':
    data = file_util.read_file(file_path, 'input.txt')

    print(solution_1(data))
    print(solution_2(data))