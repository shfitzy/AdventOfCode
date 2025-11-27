import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util, pathing

class Node:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reset()

    def add_neighbor(self, other_node, up=True):
        if up:
            self.up = other_node
            other_node.down = self
        else:
            self.left = other_node
            other_node.right = self

    def get_neighbors(self, within_range=True, only_traversable=True):
        neighbors = []

        for direction in ['up', 'down', 'left', 'right']:
            if hasattr(self, direction):
                neighbor = getattr(self, direction)
                if only_traversable and neighbor.value == '#': continue
                if within_range and neighbor.dist and self.dist >= neighbor.dist - 1: continue
                neighbors.append(neighbor)

        return neighbors

    def reset(self):
        self.value = '.'
        self.dist = None


def generate_graph(grid_size):
    graph = dict()
    for y in range(grid_size):
        for x in range(grid_size):
            pos = (x, y)
            node = Node(x, y)
            graph[pos] = node

            if x > 0: node.add_neighbor(graph[(x - 1, y)], up=False)
            if y > 0: node.add_neighbor(graph[(x, y - 1)])

    return graph

def run_input(input, graph, grid_size, len_to_process):
    for line in input[:len_to_process]:
        x, y = line.split(',')
        graph[int(x), int(y)].value = '#'

    return traverse_graph(graph, grid_size)

def find_blocking_byte(input, graph, grid_size):
    first, last = 0, len(input) - 1
    while True:
        [node.reset() for node in graph.values()]

        midpoint = (first + last) // 2
        # print(midpoint)
        run_input(input, graph, grid_size, midpoint)
        if graph[(grid_size - 1, grid_size - 1)].dist: first = midpoint
        else: last = midpoint

        if first + 1 == last: return input[last-1]
            
def traverse_graph(graph, grid_size):
    start = graph[(0, 0)]

    start.dist = 0
    queue = [start]
    while len(queue) > 0:
        cur_node = queue.pop(0)
        for neighbor_node in cur_node.get_neighbors():
            neighbor_node.dist = cur_node.dist + 1
            queue.insert(0, neighbor_node)

    return graph[(grid_size - 1, grid_size - 1)].dist

def print_graph(graph, grid_size):
    for y in range(grid_size):
        row = ''
        for x in range(grid_size):
            row += ' ' if graph[(x, y)].dist else graph[(x, y)].value
        print(row)

if __name__ == '__main__':
    test_mode = False
    input = file_util.read(file_path, 'test_input.txt' if test_mode else 'input.txt').split('\n')
    grid_size = 7 if test_mode else 71
    len_to_process = 12 if test_mode else 1024

    graph = generate_graph(grid_size)
    print(run_input(input, graph, grid_size, len_to_process))
    print(find_blocking_byte(input, graph, grid_size))
