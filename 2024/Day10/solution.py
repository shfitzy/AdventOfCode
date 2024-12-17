from itertools import groupby

import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

class Node:

    def __init__(self, value, pos):
        self.value = value
        self.pos = pos
        self.neighbors = []

    def add_neighbor(self, node):
        if abs(self.value - node.value) == 1:
            self.neighbors.append(node)
            node.neighbors.append(self)

    def get_value(self):
        return self.value

    def get_neighbors(self, value):
        return [neighbor for neighbor in self.neighbors if neighbor.value == value]

def generate_graph(input):
    nodes = {}
    trailheads = set()

    for y, line in enumerate(input):
        for x, c in enumerate(line):
            value = int(c)
            pos = (x, y)
            node = Node(value, pos)
            
            if x > 0: node.add_neighbor(nodes[(x - 1, y)])
            if y > 0: node.add_neighbor(nodes[(x, y - 1)])

            nodes[pos] = node
            if(value == 0): trailheads.add(node)

    return nodes, trailheads

def get_score(trailhead):
    nodes = set([trailhead])

    for i in range(9):
        nodes = set([item for sublist in [node.get_neighbors(i + 1) for node in nodes] for item in sublist])

    return len(nodes)

def get_rating(trailhead):
    nodes = {trailhead: 1}

    for i in range(9):
        new_nodes = {}
        for node in nodes:
            for neighbor in node.get_neighbors(i + 1):
                if neighbor in new_nodes.keys():
                    new_nodes[neighbor] += nodes[node]
                else:
                    new_nodes[neighbor] = nodes[node]
        nodes = new_nodes

    return sum(nodes.values())

if __name__ == '__main__':
    nodes, trailheads = generate_graph(file_util.read(file_path, 'input.txt').split())

    print(sum([get_score(trailhead) for trailhead in trailheads]))
    print(sum([get_rating(trailhead) for trailhead in trailheads]))