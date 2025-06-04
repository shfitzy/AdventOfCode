import numpy
import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util
from utils import pathing

class Node:

    up = down = left = right = None
    up_score = down_score = left_score = right_score = None

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

    def get_neighbor(self, dir):
        if dir == (1, 0): return self.right
        elif dir == (-1, 0): return self.left
        elif dir == (0, 1): return self.down
        elif dir == (0, -1): return self.up

    def get_traversable_neighbors(self):
        return filter(lambda x: x.value != '#', [self.up, self.down, self.left, self.right])
    
    def set_new_directional_score(self, score, dir):
        if dir == (1, 0) and (not self.right_score or self.right_score > score):
            self.right_score = score
        elif dir == (-1, 0) and (not self.left_score or self.left_score > score):
            self.left_score = score
        elif dir == (0, 1) and (not self.down_score or self.down_score > score):
            self.down_score = score
        elif dir == (0, -1) and (not self.up_score or self.up_score > score):
            self.up_score = score
        else: return False

        return True
    
    def get_directional_score(self, dir):
        if dir == (1, 0): return self.right_score or 0
        if dir == (-1, 0): return self.left_score or 0
        if dir == (0, 1): return self.down_score or 0
        if dir == (0, -1): return self.up_score or 0
    
    def get_low_score(self):
        return min(filter(lambda x: x is not None, [self.up_score, self.down_score, self.left_score, self.right_score]))


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

def calc_min_score(start, end):
    paths_to_process = [(start, (1, 0))]

    while len(paths_to_process) > 0:
        node, dir = paths_to_process.pop(0)

        for neighbor in node.get_traversable_neighbors():
            new_dir = tuple(numpy.subtract(neighbor.pos, node.pos))
            new_score = node.get_directional_score(dir) + 1 if new_dir == dir else node.get_directional_score(dir) + 1001
            
            if new_dir != dir * -1 and neighbor.set_new_directional_score(new_score, new_dir):
                paths_to_process.append((neighbor, new_dir))

    print(end.get_low_score())


def calc_num_optimal_tiles(end):
    nodes_to_process = [(end, n) for n in end.get_traversable_neighbors() if end.get_directional_score(tuple(numpy.subtract(end.pos, n.pos))) == end.get_low_score()]
    optimal_nodes = set()

    while len(nodes_to_process) > 0:
        node, next_node = nodes_to_process.pop()
        optimal_nodes.add(node)
        
        dir = tuple(numpy.subtract(node.pos, next_node.pos))
        node_score = node.get_directional_score(dir)

        if next_node.get_directional_score(dir) == node_score - 1:
            nodes_to_process.append((next_node, next_node.get_neighbor((dir[0] * -1, dir[1] * -1))))
        if next_node.get_directional_score((dir[1], dir[0])) == node_score - 1001:
            nodes_to_process.append((next_node, next_node.get_neighbor((dir[1] * -1, dir[0] * -1))))
        if next_node.get_directional_score((dir[1] * -1, dir[0] * -1)) == node_score - 1001:
            nodes_to_process.append((next_node, next_node.get_neighbor((dir[1], dir[0]))))

    print(len(optimal_nodes))


if __name__ == '__main__':
    start, end = generate_map(file_util.read(file_path, 'input.txt'))
    
    calc_min_score(start, end)
    calc_num_optimal_tiles(end)