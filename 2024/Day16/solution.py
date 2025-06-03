import numpy
import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util
from utils import pathing

class Node:

    up = down = left = right = None
    score = None

    def __init__(self, pos, value):
        self.pos = pos
        self.value = value

    def add_neighbor(self, other_node, up=True):
            if up:
                self.up = other_node
                other_node.down = self
            else:
                self.left = other_node
                other_node.right = self

    def get_traversable_neighbors(self):
        return [n for n in [self.up, self.down, self.left, self.right] if n.value == '.']


def generate_map(input):
    graph = dict()
    start = end = None

    lines = input.split('\n')
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            pos = (x, y)
            val = lines[y][x]
            
            node = Node(pos, val)
            if x > 0: node.add_neighbor(graph[pathing.move_in_dir(pos, '<')], up=False)
            if y > 0: node.add_neighbor(graph[pathing.move_in_dir(pos, '^', y_pos_up=False)])
            
            graph[pos] = node
            if val == 'S':
                start = node
                node.score = 0
            if val == 'E':
                node.value = '.'
                end = node

    return start, end


def calc_traversal(start):
    paths_to_process = [(start, (1, 0))]
    while len(paths_to_process) > 0:
        node, dir = paths_to_process.pop()
        for neighbor in node.get_traversable_neighbors():
            new_dir = tuple(numpy.subtract(neighbor.pos, node.pos))
            new_score = node.score + 1 if new_dir == dir else node.score + 1001
            if new_dir != dir * -1:
                if not neighbor.score or neighbor.score > new_score:
                    neighbor.score = new_score
                    paths_to_process.append((neighbor, new_dir))


def calc_score(start, end):
    calc_traversal(start)
    print(end.score)


if __name__ == '__main__':
    start, end = generate_map(file_util.read(file_path, 'input.txt'))
    
    calc_score(start, end)