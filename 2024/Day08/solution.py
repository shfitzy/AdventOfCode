import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

if __name__ == '__main__':
    input = file_util.read_file(file_path, 'input.txt')

    width, height = len(input[0]), len(input)
    node_map = {}
    antinodes = set()

    for x in range(width):
        for y in range(height):
            value = input[x][y]
            if not value == '.':
                new_node = (y, x)
                if value not in node_map.keys():
                    node_map[value] = [new_node]
                else:
                    for node in node_map[value]:
                        dx, dy = new_node[0] - node[0], new_node[1] - node[1]
                        
                        # diff = (new_node[0] + dx, new_node[1] + dy)
                        diff = (dx, dy)
                        inc = 0
                        while True:
                            if (0 <= new_node[0] + diff[0] * inc < width) and (0 <= new_node[1] + diff[1] * inc < height):
                                antinodes.add((new_node[0] + diff[0] * inc, new_node[1] + diff[1] * inc))
                                inc += 1
                            else:
                                break
                        
                        inc = 1
                        while True:
                            if (0 <= new_node[0] - diff[0] * inc < width) and (0 <= new_node[1] - diff[1] * inc < height):
                                antinodes.add((new_node[0] - diff[0] * inc, new_node[1] - diff[1] * inc))
                                inc += 1
                            else:
                                break

                        # if (0 <= new_node[0] + dx < width) and (0 <= new_node[1] + dy < height):
                        #     antinodes.add((new_node[0] + dx, new_node[1] + dy))
                        # if (0 <= node[0] - dx < width) and (0 <= node[1] - dy < height):
                        #     antinodes.add((node[0] - dx, node[1] - dy))

                    node_map[value].append(new_node)

    for y in range(height):
        for x in range(width):
            if (x, y) in antinodes: print('#', end='')
            else: print('.', end='')
        print('')

    print(len(antinodes))