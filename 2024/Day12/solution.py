import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

UP = lambda pos: (pos[0], pos[1] - 1)
DOWN = lambda pos: (pos[0], pos[1] + 1)
LEFT = lambda pos: (pos[0] - 1, pos[1])
RIGHT = lambda pos: (pos[0] + 1, pos[1])

DIRS = [UP, RIGHT, DOWN, LEFT]

class Node:

    def __init__(self, value, pos):
        self.value = value
        self.pos = pos
        self.neighbors = []
        self.traversed = False

    def link_nodes(self, other_node):
        if(self.value == other_node.value):
            self.neighbors.append(other_node)
            other_node.neighbors.append(self)

    def get_neighbor(self, pos_fnct):
        return next((node for node in self.neighbors if node.pos == pos_fnct(self.pos)), None)

def generate_graph(input):
    """
    This function generates a graph of the input data, returning a dict mapping 2-D tuples to each node in the graph that is
    generated. As each Node in the graph is created, the Node will associate itself to its same-valued neighbor Nodes.

    :param input: The input of the problem, in string format, to be converted into a graph.
    """
    graph = dict()

    for y in range(len(input)):
        for x in range(len(input[y])):
            pos = (x, y)
            node = Node(input[y][x], pos)
            graph[pos] = node

            if x > 0: node.link_nodes(graph[LEFT(pos)])
            if y > 0: node.link_nodes(graph[UP(pos)])

    return graph

def calc_pricing(graph, bulk=False):
    """
    This function calculates the pricing of the input graph, based on whether or not it uses bulk pricing (part A vs part B of the problem).
    It iterates over each Node, keeping a tally of which positions it has already processed. Each time it finds a new Node, it will iterate
    over the region that shares that Node's value, by looping over the Node's neighbors. For each region, it will tally up the total area,
    as well as the perimeter cost of that region.

    The perimeter cost is different between the two parts of the problem, and is toggled by the "bulk" flag. If this flag is False, the loop
    will simply calculate the total perimeter and use that as the value. It does this by checking each Node's neighbors and subtracting them
    by 4, since for each neighbor a Node has, it will occupy the space where the perimeter would have been. If the flag is True, we call into
    another method to calculate how many of the sides of the Node are part of an edge that has not yet been processed.

    :param graph: The input of the puzzle, represented as a dict mapping 2-D tuples (positions) to their respective Nodes.
    :param bulk: Optional parameter (defaulted to False) that determines which pricing model to use.
    """
    total_price = 0

    processed_nodes = set()
    for node in graph:
        if not node in processed_nodes:
            nodes = [graph[node]]
            area_price = perimeter_price = 0

            while not len(nodes) == 0:
                working_node = nodes.pop()
                if not working_node.pos in processed_nodes:
                    [nodes.append(neighbor) for neighbor in working_node.neighbors if neighbor.pos not in processed_nodes]
                    perimeter_price += sum([check_if_unprocessed_edge(graph, working_node, processed_nodes, dir) for dir in DIRS]) if bulk else (4 - len(working_node.neighbors))
                    area_price += 1

                    processed_nodes.add(working_node.pos)

            total_price += area_price * perimeter_price

    return total_price

def check_if_unprocessed_edge(graph, node, processed_nodes, dir):
    """
    This function takes in a Node and a direction, and determines whether or not that side of the Node representes an unprocessed edge within
    the region. If the Node in that direction shares a value with it, it is not an edge of the region and we return False. Otherwise, we
    iterate over the perpendicular directions of the graph, inspecting the edge. If any of the neighbors along the edge have already been
    processed, we know we can return False, since the edge has already been accounted for, otherwise we return True.

    :param graph: The input of the puzzle, represented as a dict mapping 2-D tuples (positions) to their respective Nodes.
    :param node: The Node we are calculating the number of unprocessed edges for.
    :param processed_nodes: A set of processed Node positions (2-D tuples), used by this function and the calling function to keep
    track of which Nodes still need to be processed.
    :param dir: A lambda function representing a mapping of an orthogonal direction to determine which edge we are checking.
    """
    if graph.get(dir(node.pos)) and graph[dir(node.pos)].value == node.value: return False

    for perpendicular_dir in [d for i, d in enumerate(DIRS) if (i % 2) != (DIRS.index(dir) % 2)]:
        while graph.get(perpendicular_dir(node.pos)) and graph[perpendicular_dir(node.pos)].value == node.value:
            node = node.get_neighbor(perpendicular_dir)
            if node.get_neighbor(dir) and node.get_neighbor(dir).value == node.value: break
            elif node.pos in processed_nodes: return False

    return True

if __name__ == '__main__':
    graph = generate_graph(file_util.read(file_path, 'input.txt').split())

    print(calc_pricing(graph))
    print(calc_pricing(graph, bulk=True))