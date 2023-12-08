import math
import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util



class Node:

    def __init__(self, value, left, right, goal):
        self.value = value
        self.left = left
        self.right = right
        self.goal = goal
    
    def generate_traversal_data(self, instructions):
        node = self
        traversal_set = set()
        count = 0

        goal_indices = []

        while True:
            inst_index = count % len(instructions)
            key = str(inst_index) + '-' + node.value

            if not key in traversal_set: traversal_set.add(key)
            else:
                start = int(key.split('-')[0])
                cycle_length = count - start
                goal_indices = [i for i in goal_indices if i >= start]

                return TraversalData(start, cycle_length, goal_indices)

            if node.goal:
                goal_indices.append(count)
            node = node.left if instructions[inst_index] == 'L' else node.right
            count += 1
    


class TraversalData:

    def __init__(self, start, cycle_length, goal_indices):
        self.start = start
        self.cycle_length = cycle_length
        self.goal_indices = goal_indices



def set_up_map(mappings, start_criteria, goal_criteria):
    node_map = {}
    starting_nodes = []

    for mapping in mappings:
        value = mapping.split(' = ')[0]
        left, right = mapping.split(' = ')[1].lstrip("(").rstrip(")").split(", ")
        is_goal = goal_criteria(value)

        node = Node(value, left, right, is_goal)
        node_map[value] = node

        if start_criteria(value):
            starting_nodes.append(node)

    for k, _ in node_map.items():
        node_map[k].left = node_map[node_map[k].left]
        node_map[k].right = node_map[node_map[k].right]

    return starting_nodes

def calc_total_steps(instructions, mappings, start_criteria, goal_criteria):
    nodes = set_up_map(mappings, start_criteria, goal_criteria)
    data = [node.generate_traversal_data(instructions) for node in nodes]

    return math.lcm(*[datum.goal_indices[0] for datum in data])

def solution_1(instructions, mappings):
    return calc_total_steps(instructions, mappings, lambda s: s == 'AAA', lambda s: s == 'ZZZ')

def solution_2(instructions, mappings):
    return calc_total_steps(instructions, mappings, lambda s: s[-1] == 'A', lambda s: s[-1] == 'Z')

if __name__ == '__main__':
    data = file_util.read_file(file_path, 'input.txt')

    instructions = data[0]
    mappings = data[2:]

    print(solution_1(instructions, mappings))
    print(solution_2(instructions, mappings))