from itertools import groupby

import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def generate_file_system(input):
    return [i for sub in [[i] * int(input[i*2]) + ([None] * int(input[i*2+1]) if i*2+1 < len(input) else []) for i in range(int((len(input) + 1) / 2))] for i in sub]

def generate_file_system_metadata(file_system):
    return [sum(1 for _ in group) for _, group in groupby(file_system, lambda x: 0 if x == None else 1)]

def move_file_blocks_left(file_system, from_pos, to_pos, num_blocks=1):
    if to_pos < from_pos:
        for i in range(num_blocks):
            file_system[to_pos + i] = file_system[from_pos + i]
            file_system[from_pos + i] = None

def solution_1(input):
    file_system = generate_file_system(input)

    next_idx = 0
    last_idx = len(file_system) - 1
    while next_idx < last_idx:
        if file_system[next_idx] == None:
            while not file_system[last_idx]:
                last_idx -= 1
            move_file_blocks_left(file_system, last_idx, next_idx)
        next_idx += 1
            
    return sum([idx * id for idx, id in enumerate(file_system) if id])

# This runs slow - I'd like to store more metadata around the files/disk space to speed up the process
# TODO: Keep track of file metadata (ID, Starting Position, Size)
# TODO: Keep track of the free space in the file system, maybe a map that goes from number of contiguous
# blocks of free space to an ordered list of indices where blocks of that size exist?
def solution_2(input):
    file_system = generate_file_system(input)
    file_system_metadata = [int(c) for c in input]
    file_metadata = {int(idx / 2): int(val) for idx, val in enumerate(input) if idx % 2 == 0}

    for idx in reversed(range(len(file_system))):
        if file_system[idx]:
            file_size = file_metadata[file_system[idx]]
            starting_pos = (idx - file_size + 1)

            # for to_pos in range(starting_pos):
            #     if file_system[to_pos:to_pos+file_size] == [None] * file_size:
            #         move_file_blocks_left(file_system, starting_pos, to_pos, file_size)
            #         file_system_metadata = generate_file_system_metadata(file_system)
            #         break

            for i, free_blocks in enumerate(file_system_metadata[1::2]):
                if free_blocks >= file_size:
                    move_file_blocks_left(file_system, starting_pos, sum(file_system_metadata[:(i*2)+1]), file_size)
                    file_system_metadata = generate_file_system_metadata(file_system)
                    break
            
    return sum([idx * id for idx, id in enumerate(file_system) if id])

if __name__ == '__main__':
    input = file_util.read(file_path, 'input.txt')

    print(solution_1(input))
    print(solution_2(input))
    