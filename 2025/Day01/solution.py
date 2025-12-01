import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def process_input(input):
    p1, p2, dial_value = 0, 0, 50
    
    dir = 'R'
    for i in input:
        new_dir, rotation = i[0], int(i[1:])
        if new_dir != dir:
            dial_value = 100 - dial_value
            dir = new_dir
        
        dial_value = (dial_value % 100) + rotation
        if dial_value % 100 == 0: p1 += 1
        p2 += dial_value // 100

    return p1, p2

if __name__ == '__main__':
    [print(f'Part {i+1}: {x}') for i, x in enumerate(process_input(file_util.read(file_path, 'input.txt').split('\n')))]