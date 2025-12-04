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
                # output += self.nodes[(x, y)].value
                output += str(len(self.nodes[(x, y)].tp_neighbors))
            output += '\n'
        return output
    
    def remove_tp(self, node):
        if node in self.tp_nodes and node.value == '@':
            self.tp_nodes.remove(node)
            node.remove_tp()

class Node:

    def __init__(self, x, y, value):
        self.pos = (x, y)
        self.value = value
        self.neighbors = []
        self.tp_neighbors = []

    def add_neighbor(self, other_node, is_tp):
        self.neighbors.append(other_node)
        other_node.neighbors.append(self)
        if other_node.value == '@':
            self.tp_neighbors.append(other_node)
        if is_tp:
            other_node.tp_neighbors.append(self)

    def remove_tp(self):
        self.value = '.'
        for tp_neighbor in self.tp_neighbors:
            tp_neighbor.tp_neighbors.remove(self)
        self.tp_neighbors = []

def get_num_accessible_tp(graph, recurse, tp_accessible=0):
    accessible_nodes = [node for node in graph.tp_nodes if len(node.tp_neighbors) < 4]
    tp_accessible += len(accessible_nodes)

    for node in accessible_nodes: graph.remove_tp(node)

    if len(accessible_nodes) != 0 and recurse:
        return get_num_accessible_tp(graph, recurse, tp_accessible)
    else:
        return tp_accessible

def solve(input, recurse=False):
    return get_num_accessible_tp(Graph(input), recurse)

if __name__ == '__main__':
    input = file_util.read(file_path, 'input.txt').split('\n')

    timer(solve, 'Part 1', 10, input)
    timer(solve, 'Part 2', 10, input, True)