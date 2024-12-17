import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def calc_stone_count(rocks, iterations):
    stone_map = {value: 1 for value in rocks}

    for i in range(iterations):
        new_map = dict()

        for rock, count in stone_map.items():
            if rock == 0:
                add_rocks_to_map(1, count, new_map)
            elif len(str(rock)) % 2 == 0:
                add_rocks_to_map(int(str(rock)[:int(len(str(rock)) / 2)]), count, new_map)
                add_rocks_to_map(int(str(rock)[int(len(str(rock)) / 2):]), count, new_map)
            else:
                add_rocks_to_map(rock * 2024, count, new_map)
        
        stone_map = new_map

        print(f"After {i+1} blinks, there are {sum([count for count in stone_map.values()])} stones.")

def add_rocks_to_map(value, count, map):
    map[value] = map.get(value, 0) + count

if __name__ == '__main__':
    rocks = list(map(lambda i: int(i), file_util.read(file_path, 'input.txt').split()))

    calc_stone_count(rocks, 75)