import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

dir_alg = ['U', 'R', 'D', 'L']

class Node:

    def __init__(self, value, pos):
        self.value = ('.' if value == '^' else value)
        self.og_value = ('.' if value == '^' else value)

        self.dirs_traversed = []
        self.pos = pos
        self.up = self.down = self.left = self.right = None

    def reset(self):
        self.value = self.og_value
        self.dirs_traversed = []

    def link_node(self, other_node, other_node_dir):
        if(other_node_dir == 'L'):
            self.left = other_node
            other_node.right = self
        elif(other_node_dir == 'U'):
            self.up = other_node
            other_node.down = self

    def check_next(self, dir):
        if(dir == 'U' and (not self.up or self.up.value == '.')): return True
        elif(dir == 'R' and (not self.right or self.right.value == '.')): return True
        elif(dir == 'D' and (not self.down or self.down.value == '.')): return True
        elif(dir == 'L' and (not self.left or self.left.value == '.')): return True
        else: return False

    def move(self, dir):
        next_node = None
        loop = False

        if(dir == 'U'): next_node = self.up
        elif(dir == 'R'): next_node = self.right
        elif(dir == 'D'): next_node = self.down
        elif(dir == 'L'): next_node = self.left
        
        if dir in self.dirs_traversed:
            loop = True
        else:
            self.dirs_traversed.append(dir)

        return next_node, loop

    def is_traversed(self):
        return len(self.dirs_traversed) > 0
    
def generate_graph(input):
    nodes = {}
    current_node = None

    for y, row in enumerate(input):
        for x, char in enumerate(list(row)):
            new_node = Node(char, (x, y))
            nodes[(x, y)] = new_node
            if(char == '^'): current_node = new_node
            if(x > 0): new_node.link_node(nodes[(x-1, y)], 'L')
            if(y > 0): new_node.link_node(nodes[x, y-1], 'U')

    return nodes, current_node
    
def solution_1(nodes, starting_node):
    current_node = starting_node
    dir_alg_idx = 0

    while current_node:
        if(current_node.check_next(dir_alg[dir_alg_idx % len(dir_alg)])):
            current_node = current_node.move(dir_alg[dir_alg_idx % len(dir_alg)])[0]
        else:
            dir_alg_idx += 1

    print(sum([node.is_traversed() for node in nodes.values()]))

    return [v for _, v in nodes.items() if v.is_traversed() and not v == starting_node]

def solution_2(nodes, starting_node, path):
    sum = 0

    for node in path:
        node.value = '#'

        current_node = starting_node
        dir_alg_idx = 0
        
        while current_node:
            if(current_node.check_next(dir_alg[dir_alg_idx % len(dir_alg)])):
                current_node, loop = current_node.move(dir_alg[dir_alg_idx % len(dir_alg)])
                if loop:
                    sum += 1
                    break
            else:
                dir_alg_idx += 1

        [node.reset() for node in nodes.values()]

    print(sum)

if __name__ == '__main__':
    nodes, starting_node = generate_graph(file_util.read(file_path, 'input.txt').split())

    path = solution_1(nodes, starting_node)
    solution_2(nodes, starting_node, path)
    


    