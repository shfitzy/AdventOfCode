from collections import defaultdict
import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

class Graph:

    def __init__(self, input):
        self.width = len(input[0])
        self.height = len(input)

        self.nodes = dict()
        for y in range(self.height):
            for x in range(self.width):
                value = input[y][x]
                node = Node(x, y, value)
                self.nodes[(x, y)] = node

                if x > 0: node.add_neighbor(self.nodes[(x - 1, y)], up=False)
                if y > 0: node.add_neighbor(self.nodes[(x, y - 1)])

                if value == 'S':
                    node.dist = 0
                    self.start = node
                if value == 'E': self.end = node

        self.traverse()

    def __str__(self):
        output = ''
        for y in range(self.height):
            for x in range(self.width):
                output += self.nodes[(x, y)].value
            output += '\n'
        return output
    
    def traverse(self):
        nodes = [self.start]
        while len(nodes) > 0:
            cur_node = nodes.pop(0)
            for neighbor in [node for node in cur_node.get_neighbors() if node.is_traversable()]:
                if neighbor.dist is None:
                    neighbor.dist = cur_node.dist + 1
                    nodes.append(neighbor)

class Node:

    def __init__(self, x, y, value, dist=None):
        self.pos = (x, y)
        self.value = value
        self.dist = None

    def add_neighbor(self, other_node, up=True):
        if up:
            self.up = other_node
            other_node.down = self
        else:
            self.left = other_node
            other_node.right = self

    def get_neighbors(self):
        return [getattr(self, direction) for direction in ['up', 'down', 'left', 'right'] if hasattr(self, direction)]
    
    def is_traversable(self):
        return self.value != '#'
    
def calc_shortcuts(graph, cheat_duration, time_save_limit):
    # shortcut_mappings = defaultdict(int)

    # for node in [node for _, node in graph.nodes.items() if node.dist is not None]:
    #     for neighbor in [neighbor for neighbor in node.get_neighbors() if not neighbor.is_traversable()]:
    #         target_node_pos = (2 * (neighbor.pos[0] - node.pos[0]) + node.pos[0], 2 * (neighbor.pos[1] - node.pos[1]) + node.pos[1])
    #         target_node = graph.nodes.get(target_node_pos)
    #         if target_node and target_node.dist is not None and target_node.dist > node.dist + 2:
    #             shortcut_mappings[target_node.dist - (node.dist + 2)] += 1

    num_valid_shortcuts = 0
    keys = sorted([node for _, node in graph.nodes.items() if node.dist is not None], key=lambda n: n.dist)
    for start_node in keys[:-time_save_limit]:
        for end_node in keys[start_node.dist + time_save_limit:]:
            manhattan_distance = abs(start_node.pos[0] - end_node.pos[0]) + abs(start_node.pos[1] - end_node.pos[1])
            if manhattan_distance <= cheat_duration and end_node.dist - start_node.dist - manhattan_distance >= time_save_limit:
                num_valid_shortcuts += 1
    return num_valid_shortcuts
    # for node in [node for _, node in graph.nodes.items() if node.dist is not None]:
    #     for neighbor in [neighbor for neighbor in node.get_neighbors() if not neighbor.is_traversable()]:
    #         target_node_pos = (2 * (neighbor.pos[0] - node.pos[0]) + node.pos[0], 2 * (neighbor.pos[1] - node.pos[1]) + node.pos[1])
    #         target_node = graph.nodes.get(target_node_pos)
    #         if target_node and target_node.dist is not None and target_node.dist > node.dist + 2:
    #             shortcut_mappings[target_node.dist - (node.dist + 2)] += 1

    # return sum([v for k, v in shortcut_mappings.items() if k >= time_save_limit])

if __name__ == '__main__':
    test_mode = False
    graph = Graph(file_util.read(file_path, 'input.txt' if not test_mode else 'test_input.txt').split('\n'))
    time_save_limit = 100 if not test_mode else 50

    print('Part 1: ', calc_shortcuts(graph, 2, time_save_limit))
    print('Part 2: ', calc_shortcuts(graph, 20, time_save_limit))