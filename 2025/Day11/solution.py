import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util
from utils.timer import timer



class Graph:

    def __init__(self, special_nodes=[]):
        self.nodes = {'out': Node('out', [])}
        self.special_nodes = special_nodes

    def add_node(self, node):
        self.nodes[node.value] = node

    def link_nodes(self):
        for node in self.nodes.values():
            for neighbor in node.neighbors:
                self.nodes[neighbor].rev_neighbors.append(node.value)

    def delete_node(self, value):
        node = self.nodes[value]
        for neighbor_node in node.neighbors:
            self.nodes[neighbor_node].rev_neighbors.remove(value)
        for neighbor_node in node.rev_neighbors:
            self.nodes[neighbor_node].neighbors.remove(value)

        if value in self.special_nodes:
            self.special_nodes.remove(value)

        del self.nodes[value]

    def get_orphaned_nodes(self):
        orphaned_nodes = [node for node in self.nodes.values() if len(node.rev_neighbors) == 0]
        if any(self.nodes[special_node] in orphaned_nodes for special_node in self.special_nodes):
            nodes_to_prune = [node for node in self.nodes.values() if len(node.rev_neighbors) == 0 and node.value not in self.special_nodes]
            while len(nodes_to_prune) > 0:
                [self.delete_node(node.value) for node in nodes_to_prune]
                nodes_to_prune = [node for node in self.nodes.values() if len(node.rev_neighbors) == 0 and node.value not in self.special_nodes]
            return [node for node in self.nodes.values() if len(node.rev_neighbors) == 0]
        else:
            return orphaned_nodes



class Node:

    def __init__(self, value, neighbors, score=0):
        self.value = value
        self.neighbors = neighbors
        self.rev_neighbors = []
        self.score = score



def find_paths(start, dest, cable_map, nodes_hit=[], paths=[]):
    nodes_hit = nodes_hit[:]
    nodes_hit.append(start)

    for connection in cable_map[start]:
        if connection == dest:
            paths.append(nodes_hit)
        elif connection not in nodes_hit:
            find_paths(connection, dest, cable_map, nodes_hit, paths)
    
    return paths

def count_paths(input, start_node, special_nodes=[]):
    cable_map = {line.split(':')[0]: line.split(' ')[1:] for line in input}
    graph = Graph(special_nodes)

    for key in cable_map.keys():
        node = Node(key, cable_map[key], 1 if key == start_node else 0)
        graph.add_node(node)

    graph.link_nodes()
    
    while True:
        nodes_to_process = graph.get_orphaned_nodes()
        for node in nodes_to_process:
            if node.value == 'out':
                return node.score
            
            for neighbor in node.neighbors:
                graph.nodes[neighbor].score += node.score
            graph.delete_node(node.value)

def solve_part_1(input):
    return count_paths(input, 'you')

def solve_part_2(input):
    return count_paths(input, 'svr', ['dac', 'fft'])

if __name__ == '__main__':
    test_mode = False
    
    timer(solve_part_1, 'Part 1', 10, file_util.read(file_path, 'test_input_p1.txt' if test_mode else 'input.txt').split('\n'))
    timer(solve_part_2, 'Part 2', 10, file_util.read(file_path, 'test_input_p3.txt' if test_mode else 'input.txt').split('\n'))