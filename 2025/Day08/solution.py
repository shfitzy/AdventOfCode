import math
import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util
from utils.timer import timer

def get_tuple(line):
    return tuple(map(int, line.split(',')))

def solve_part_1(input, pairs_to_process):
    input = [get_tuple(line) for line in input]
    id_to_junction_list = dict()
    junction_id_mapping = dict()
    mappings = []

    for idx, coord_1 in enumerate(input):
        id_to_junction_list[idx] = [coord_1]
        junction_id_mapping[coord_1] = idx
        for coord_2 in input[idx+1:]:
            mappings.append([coord_1, coord_2, math.dist(coord_1, coord_2)])

    mappings.sort(key=lambda r: r[2])

    for i in range(pairs_to_process):
        id_1 = junction_id_mapping[mappings[i][0]]
        id_2 = junction_id_mapping[mappings[i][1]]
        if id_1 != id_2:
            for coord in id_to_junction_list[id_2]:
                junction_id_mapping[coord] = id_1
                id_to_junction_list[id_1].append(coord)
            id_to_junction_list.pop(id_2)

    return math.prod(sorted([len(v) for v in id_to_junction_list.values()], reverse=True)[:3])

def solve_part_2(input):
    input = [get_tuple(line) for line in input]
    id_to_junction_list = dict()
    junction_id_mapping = dict()
    mappings = []

    for idx, coord_1 in enumerate(input):
        id_to_junction_list[idx] = [coord_1]
        junction_id_mapping[coord_1] = idx
        for coord_2 in input[idx+1:]:
            mappings.append([coord_1, coord_2, math.dist(coord_1, coord_2)])

    mappings.sort(key=lambda r: r[2])

    for i in range(len(mappings)):
        id_1 = junction_id_mapping[mappings[i][0]]
        id_2 = junction_id_mapping[mappings[i][1]]
        if id_1 != id_2:
            for coord in id_to_junction_list[id_2]:
                junction_id_mapping[coord] = id_1
                id_to_junction_list[id_1].append(coord)
            id_to_junction_list.pop(id_2)

            if len(id_to_junction_list) == 1:
                return mappings[i][0][0] * mappings[i][1][0]

if __name__ == '__main__':
    test_mode = False
    input = file_util.read(file_path, 'test_input' if test_mode else 'input.txt').split('\n')

    timer(solve_part_1, 'Part 1', 10, input, 10 if test_mode else 1000)
    timer(solve_part_2, 'Part 2', 10, input)