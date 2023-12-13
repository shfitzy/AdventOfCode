import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

TOP_LEFT = 1
TOP_RIGHT = 2
BOTTOM_LEFT = 3
BOTTOM_RIGHT = 4

size = (0, 0)



class Node:

    def __init__(self, coords, val):
        self.coords = coords
        self.val = val
        self.main_loop_node = False
        self.find_pipe_exits(coords, val)
        self.filled_quads = []

    def find_pipe_exits(self, coords, val):
        if val == '|': self.exits = {(coords[0], coords[1] - 1), (coords[0], coords[1] + 1)}
        elif val == '-': self.exits = {(coords[0] - 1, coords[1]), (coords[0] + 1, coords[1])}
        elif val == 'L': self.exits = {(coords[0], coords[1] - 1), (coords[0] + 1, coords[1])}
        elif val == 'J': self.exits = {(coords[0], coords[1] - 1), (coords[0] - 1, coords[1])}
        elif val == '7': self.exits = {(coords[0] - 1, coords[1]), (coords[0], coords[1] + 1)}
        elif val == 'F': self.exits = {(coords[0] + 1, coords[1]), (coords[0], coords[1] + 1)}
        else: self.exits = set()

    def set_main_loop_node(self):
        self.main_loop_node = True



def generate_graph(data):
    graph = {}

    for y in range(len(data)):
        for x in range(len(data[0])):
            node = Node((x, y), data[y][x])
            if data[y][x] == 'S':
                start = node
                start.set_main_loop_node()
            graph[(x, y)] = node

    if start.coords[0] > 0 and start.coords in graph[(start.coords[0] - 1, start.coords[1])].exits:
        start.exits.add((start.coords[0] - 1, start.coords[1]))
    if start.coords[0] < len(data[0]) - 1 and start.coords in graph[(start.coords[0] + 1, start.coords[1])].exits:
        start.exits.add((start.coords[0] + 1, start.coords[1]))
    if start.coords[1] > 0 and start.coords in graph[(start.coords[0]), start.coords[1] - 1].exits:
        start.exits.add((start.coords[0], start.coords[1] - 1))
    if start.coords[1] < len(data) - 1 and start.coords in graph[(start.coords[0]), start.coords[1] + 1].exits:
        start.exits.add((start.coords[0], start.coords[1] + 1))


    replace_starting_value(start, graph)

    traverse_graph(start, graph)

    replace_non_main_loop_nodes(graph)

    fill_node(graph, (0, 0), set(), TOP_LEFT)

    return graph

def replace_starting_value(start, graph):
    if start.coords[0] > 0 and graph[(start.coords[0] - 1, start.coords[1])].val in ['-', 'L', 'F']:
        if start.coords[1] > 0 and graph[(start.coords[0], start.coords[1] - 1)].val in ['|', '7', 'F']: start.val = "J"
        elif start.coords[1] < size[1] - 1 and graph[(start.coords[0], start.coords[1] + 1)].val in ['|', 'J', 'L']: start.val = "7"
        else: start.val = "-"
    elif start.coords[0] < size[0] - 1 and graph[(start.coords[0] + 1, start.coords[1])].val in ['-', '7', 'J']:
        if start.coords[1] > 0 and graph[(start.coords[0], start.coords[1] - 1)].val in ['|', '7', 'F']: start.val = "L"
        else: start.val = "F"
    else:
        start.val = "|"
        

def traverse_graph(start, graph):
    prev_position = start.coords
    current_node = graph[next(iter(start.exits))]
    steps = 1

    while not current_node.coords == start.coords:
        current_node.set_main_loop_node()
        steps += 1
        tmp = current_node.coords
        current_node = graph[next(iter(current_node.exits - {prev_position}))]
        prev_position = tmp

def replace_non_main_loop_nodes(graph):
    for k, v in graph.items():
        if not v.main_loop_node:
            v.val = " "

def print_graph(graph):
    for y in range(size[1]):
        for x in range(size[0]):
            print(graph[(x, y)].val, end="")
        print()

def fill_node(graph, coord, checked_nodes, fill_from):
    if coord[0] >= 0 and coord[0] < size[0] and coord[1] >= 0 and coord[1] < size[1]:
        if coord not in checked_nodes:
            checked_nodes.add(coord)
            node = graph[coord]

            if node.val == " ":
                node.filled_quads = [TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT]
                fill_node(graph, (coord[0] - 1, coord[1]), checked_nodes, TOP_RIGHT)
                fill_node(graph, (coord[0] + 1, coord[1]), checked_nodes, TOP_LEFT)
                fill_node(graph, (coord[0], coord[1] - 1), checked_nodes, BOTTOM_RIGHT)
                fill_node(graph, (coord[0], coord[1] + 1), checked_nodes, TOP_LEFT)
            elif node.val == "|":
                if fill_from in [TOP_LEFT, BOTTOM_LEFT]:
                    node.filled_quads = [TOP_LEFT, BOTTOM_LEFT]
                    fill_node(graph, (coord[0] - 1, coord[1]), checked_nodes, TOP_RIGHT)
                    fill_node(graph, (coord[0], coord[1] - 1), checked_nodes, BOTTOM_LEFT)
                    fill_node(graph, (coord[0], coord[1] + 1), checked_nodes, TOP_LEFT)
                else:
                    node.filled_quads = [TOP_RIGHT, BOTTOM_RIGHT]
                    fill_node(graph, (coord[0] + 1, coord[1]), checked_nodes, TOP_LEFT)
                    fill_node(graph, (coord[0], coord[1] - 1), checked_nodes, BOTTOM_RIGHT)
                    fill_node(graph, (coord[0], coord[1] + 1), checked_nodes, TOP_RIGHT)
            elif node.val == "-":
                if fill_from in [TOP_LEFT, TOP_RIGHT]:
                    node.filled_quads = [TOP_LEFT, TOP_RIGHT]
                    fill_node(graph, (coord[0] - 1, coord[1]), checked_nodes, TOP_RIGHT)
                    fill_node(graph, (coord[0] + 1, coord[1]), checked_nodes, TOP_LEFT)
                    fill_node(graph, (coord[0], coord[1] - 1), checked_nodes, BOTTOM_LEFT)
                else:
                    node.filled_quads = [BOTTOM_LEFT, BOTTOM_RIGHT]
                    fill_node(graph, (coord[0] - 1, coord[1]), checked_nodes, BOTTOM_RIGHT)
                    fill_node(graph, (coord[0] + 1, coord[1]), checked_nodes, BOTTOM_LEFT)
                    fill_node(graph, (coord[0], coord[1] + 1), checked_nodes, TOP_LEFT)
            elif node.val == "L":
                if fill_from in [TOP_RIGHT]:
                    node.filled_quads = [TOP_RIGHT]
                    fill_node(graph, (coord[0] + 1, coord[1]), checked_nodes, TOP_LEFT)
                    fill_node(graph, (coord[0], coord[1] - 1), checked_nodes, BOTTOM_RIGHT)
                else:
                    node.filled_quads = [TOP_LEFT, BOTTOM_LEFT, BOTTOM_RIGHT]
                    fill_node(graph, (coord[0] - 1, coord[1]), checked_nodes, TOP_RIGHT)
                    fill_node(graph, (coord[0] + 1, coord[1]), checked_nodes, BOTTOM_LEFT)
                    fill_node(graph, (coord[0], coord[1] - 1), checked_nodes, BOTTOM_LEFT)
                    fill_node(graph, (coord[0], coord[1] + 1), checked_nodes, TOP_LEFT)
            elif node.val == "J":
                if fill_from in [TOP_LEFT]:
                    node.filled_quads = [TOP_LEFT]
                    fill_node(graph, (coord[0] - 1, coord[1]), checked_nodes, TOP_RIGHT)
                    fill_node(graph, (coord[0], coord[1] - 1), checked_nodes, BOTTOM_LEFT)
                else:
                    node.filled_quads = [TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT]
                    fill_node(graph, (coord[0] - 1, coord[1]), checked_nodes, BOTTOM_RIGHT)
                    fill_node(graph, (coord[0] + 1, coord[1]), checked_nodes, BOTTOM_LEFT)
                    fill_node(graph, (coord[0], coord[1] - 1), checked_nodes, BOTTOM_RIGHT)
                    fill_node(graph, (coord[0], coord[1] + 1), checked_nodes, TOP_LEFT)
            elif node.val == "7":
                if fill_from in [BOTTOM_LEFT]:
                    node.filled_quads = [BOTTOM_LEFT]
                    fill_node(graph, (coord[0] - 1, coord[1]), checked_nodes, BOTTOM_RIGHT)
                    fill_node(graph, (coord[0], coord[1] + 1), checked_nodes, TOP_LEFT)
                else:
                    node.filled_quads = [TOP_LEFT, TOP_RIGHT, BOTTOM_RIGHT]
                    fill_node(graph, (coord[0] - 1, coord[1]), checked_nodes, TOP_RIGHT)
                    fill_node(graph, (coord[0] + 1, coord[1]), checked_nodes, BOTTOM_LEFT)
                    fill_node(graph, (coord[0], coord[1] - 1), checked_nodes, BOTTOM_RIGHT)
                    fill_node(graph, (coord[0], coord[1] + 1), checked_nodes, TOP_RIGHT)
            elif node.val == "F":
                if fill_from in [BOTTOM_RIGHT]:
                    node.filled_quads = [BOTTOM_RIGHT]
                    fill_node(graph, (coord[0] + 1, coord[1]), checked_nodes, BOTTOM_LEFT)
                    fill_node(graph, (coord[0], coord[1] + 1), checked_nodes, TOP_RIGHT)
                else:
                    node.filled_quads = [TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT]
                    fill_node(graph, (coord[0] - 1, coord[1]), checked_nodes, TOP_RIGHT)
                    fill_node(graph, (coord[0] + 1, coord[1]), checked_nodes, TOP_LEFT)
                    fill_node(graph, (coord[0], coord[1] - 1), checked_nodes, BOTTOM_RIGHT)
                    fill_node(graph, (coord[0], coord[1] + 1), checked_nodes, TOP_LEFT)

def solution_1(graph):
    return int(sum([1 for _, v in graph.items() if v.main_loop_node]) / 2)

def solution_2(data):
    return sum([1 for _, v in graph.items() if len(v.filled_quads) == 0])

if __name__ == '__main__':
    data = file_util.read_file(file_path, 'input.txt')
    sys.setrecursionlimit(25000)
    size = (len(data[0]), len(data))
    graph = generate_graph(data)

    print_graph(graph)
    print(solution_1(graph))
    print(solution_2(data))