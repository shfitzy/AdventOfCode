import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def calc_tree_collisions(trees):
    for row in trees:
        print(row)

if __name__ == '__main__':
    trees = file_util.read_file(file_path, 'test_input.txt')
    
    calc_tree_collisions(trees)