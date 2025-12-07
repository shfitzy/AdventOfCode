import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util
from utils.timer import timer

def solve_part_1(input):
    beams = set([str(input[0]).index('S')])
    result = 0

    for line in input[1:]:
        splitters = set([idx for idx, c in enumerate(line) if c == '^'])
        collisions = beams.intersection(splitters)
        beams = beams.difference(splitters)
        for c in collisions:
            beams.add(c-1)
            beams.add(c+1)

        result += len(collisions)

    return result

def solve_part_2(input):
    beams = [0 if c == '.' else 1 for c in input[0]]

    for line in input[1:]:
        splitters = set([idx for idx, c in enumerate(line) if c == '^'])
        collisions = set([idx for idx, value in enumerate(beams) if value > 0]).intersection(splitters)
        for c in collisions:
            beams[c-1] += beams[c]
            beams[c+1] += beams[c]
            beams[c] = 0

    return sum(beams)

if __name__ == '__main__':
    input = file_util.read(file_path, 'input.txt').split('\n')[::2]

    timer(solve_part_1, 'Part 1', 10, input)
    timer(solve_part_2, 'Part 2', 10, input)