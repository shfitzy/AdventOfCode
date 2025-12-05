import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util
from utils.timer import timer

class Graph:

    def __init__(self, input):
        self.width = len(input[0])
        self.height = len(input)

        self.nodes = dict()
        self.tp_nodes = []

        for y in range(self.height):
            for x in range(self.width):
                value = input[y][x]
                node = Node(x, y, value)
                
                self.nodes[(x, y)] = node
                if value == '@':
                    self.tp_nodes.append(node)

                for potential_neighbor in [(x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]:
                    if self.nodes.get(potential_neighbor):
                        node.add_neighbor(self.nodes[potential_neighbor], value == '@')

    def __str__(self):
        output = ''
        for y in range(self.height):
            for x in range(self.width):
                output += self.nodes[(x, y)].value
            output += '\n'
        return output
    
    def remove_tp(self, node):
        if node in self.tp_nodes and node.value == '@':
            self.tp_nodes.remove(node)
            node.value = '.'
            for neighbor in node.neighbors:
                neighbor.tp_neighbors -= 1

class Node:

    def __init__(self, x, y, value):
        self.pos = (x, y)
        self.value = value
        self.neighbors = []
        self.tp_neighbors = 0

    def add_neighbor(self, other_node, is_tp):
        self.neighbors.append(other_node)
        other_node.neighbors.append(self)
        if other_node.value == '@':
            self.tp_neighbors += 1
        if is_tp:
            other_node.tp_neighbors += 1

def solve_part_1(input):
    return len([node for node in Graph(input).tp_nodes if node.tp_neighbors < 4])

def solve_part_2(input):
    graph = Graph(input)
    result = 0

    while True:
        accessible_nodes = [node for node in graph.tp_nodes if node.tp_neighbors < 4]
        if len(accessible_nodes) == 0:
            return result
        else:
            result += len(accessible_nodes)
            [graph.remove_tp(node) for node in accessible_nodes]

def solve_with_sets(input, recurse=False):
    tp_coords, width, height = set(), len(input[0]), len(input)

    for y in range(height):
        for x in range(width):
            if input[y][x] == '@': tp_coords.add((x, y))

    accessible_tp_coords = set()
    accessible_tp = 0

    while True:
        for tp in tp_coords:
            tp_neighbors = 0
            for n in [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]:
                new_x, new_y = tp[0] + n[0], tp[1] + n[1]
                if new_x >= 0 and new_x < width and new_y >= 0 and new_y < height and (new_x, new_y) in tp_coords:
                    tp_neighbors += 1

            if tp_neighbors < 4:
                accessible_tp_coords.add(tp)

        accessible_tp += len(accessible_tp_coords)
        if not recurse or len(accessible_tp_coords) == 0:
            return accessible_tp
        else:
            tp_coords = tp_coords - accessible_tp_coords
            accessible_tp_coords.clear()
        

        

if __name__ == '__main__':
    input = file_util.read(file_path, 'input.txt').split('\n')

    timer(solve_part_1, 'Part 1 (with graph)', 10, input)
    timer(solve_part_2, 'Part 2 (with graph)', 10, input)
    timer(solve_with_sets, 'Part 1 (with sets)', 10, input)
    timer(solve_with_sets, 'Part 2 (with sets)', 10, input, True)