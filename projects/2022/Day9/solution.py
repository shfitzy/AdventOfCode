from math import ceil
import operator
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

file_path = os.path.dirname(os.path.realpath(__file__))

from utils import file_util
from utils import pathing

def read_input_and_transform(filename):
    return file_util.read_lines(filename)

def move_tail(head, tail):
    if abs(head[0] - tail[0]) > 1 or  abs(head[1] - tail[1]) > 1:
        if head[0] > tail[0]: tail = (tail[0] + 1, tail[1])
        elif head[0] < tail[0]: tail = (tail[0] - 1, tail[1])
        if head[1] > tail[1]: tail = (tail[0], tail[1] + 1)
        elif head[1] < tail[1]: tail = (tail[0], tail[1] - 1)
    
    return tail

def move_head(head, dir):
    return tuple(map(operator.add, head, pathing.DIRECTIONS_DICT[dir]))

def get_tail_locations(input, length=2):
    knot_chain = [(0, 0) for _ in range(length)]
    positions = set()

    for line in input:
        dir, num_moves = line.split()
        for i in range(int(num_moves)):
            knot_chain[0] = move_head(knot_chain[0], dir)
            for j in range(len(knot_chain) - 1):
                new_position = move_tail(knot_chain[j], knot_chain[j + 1])
                if new_position == knot_chain[j + 1]: break
                knot_chain[j + 1] = move_tail(knot_chain[j], knot_chain[j + 1])
            positions.add(knot_chain[-1])
    
    return positions
            
if __name__ == '__main__':
    input = read_input_and_transform(file_path + os.path.sep + 'input.txt')
    print(len(get_tail_locations(input)))
    print(len(get_tail_locations(input, 10)))