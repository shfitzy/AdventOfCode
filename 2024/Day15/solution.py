import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util
from utils import pathing

UP = lambda pos: (pos[0], pos[1] - 1)
DOWN = lambda pos: (pos[0], pos[1] + 1)
LEFT = lambda pos: (pos[0] - 1, pos[1])
RIGHT = lambda pos: (pos[0] + 1, pos[1])

DIRS = [UP, RIGHT, DOWN, LEFT]

class Node:

    up = down = left = right = None

    def __init__(self, pos, value):
        self.pos = pos
        self.value = value

    def add_neighbor(self, other_node, up=True):
        if up:
            self.up = other_node
            other_node.down = self
        else:
            self.left = other_node
            other_node.right = self

    def move(self, move):
        nodes_to_check = [self.get_neighbor(move)]
        nodes_to_move = [self]
        processed_nodes = set()

        while len(nodes_to_check) > 0:
            checked_node = nodes_to_check.pop()
            if checked_node in processed_nodes: continue
            else: processed_nodes.add(checked_node)

            neighbor_node = checked_node.get_neighbor(move)
            if checked_node.value == '#': return self
            elif checked_node.value not in {'.'}:
                nodes_to_move.append(checked_node)
                nodes_to_check.append(neighbor_node)
                if checked_node.value == '[' and move in {'^', 'v'}: nodes_to_check.append(checked_node.get_neighbor('>'))
                if checked_node.value == ']' and move in {'^', 'v'}: nodes_to_check.append(checked_node.get_neighbor('<'))
            
        while len(nodes_to_move) > 0:
            for node in nodes_to_move:
                if node.get_neighbor(move).value == '.':
                    nodes_to_move.remove(node)
                    node.get_neighbor(move).value = node.value
                    node.value = '.'

        return self.get_neighbor(move)

        
    def get_neighbor(self, move):
        if move == '>': return self.right
        elif move == '<': return self.left
        elif move == '^': return self.up
        elif move == 'v': return self.down

    def get_gps_coord_value(self):
        return 100 * self.pos[1] + self.pos[0] if self.value in {'O', '['} else 0



def generate_grid(warehouse_map, wide=False):
    graph = dict()
    robot = None

    if wide:
        warehouse_map = warehouse_map.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')

    lines = warehouse_map.split('\n')
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            pos = (x, y)
            val = lines[y][x]
            
            node = Node(pos, val)
            if x > 0: node.add_neighbor(graph[pathing.move_in_dir(pos, '<')], up=False)
            if y > 0: node.add_neighbor(graph[pathing.move_in_dir(pos, '^', y_pos_up=False)])
            
            graph[pos] = node
            if val == '@': robot = node

    return graph, robot


def move_robot(warehouse_map, moves, wide=False):
    nodes, robot = generate_grid(warehouse_map, wide)
    for move in moves.replace('\n', ''):
        robot = robot.move(move)
        
    print(sum([node.get_gps_coord_value() for node in nodes.values()]))
        

if __name__ == '__main__':
    warehouse_map, moves = file_util.read(file_path, 'input.txt').split('\n\n')
    
    move_robot(warehouse_map, moves)
    move_robot(warehouse_map, moves, True)