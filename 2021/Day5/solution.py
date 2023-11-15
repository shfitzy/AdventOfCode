import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def find_danger_zones(data):
    danger_zones = {}

    for line in data:
        x_coord_1, y_coord_1 = [int(x) for x in line[0].split(',')]
        x_coord_2, y_coord_2 = [int(x) for x in line[1].split(',')]

        x_step = 0 if x_coord_1 == x_coord_2 else 1 if x_coord_1 < x_coord_2 else -1
        y_step = 0 if y_coord_1 == y_coord_2 else 1 if y_coord_1 < y_coord_2 else -1

        for i in range(max(abs(x_coord_1 - x_coord_2) + 1, abs(y_coord_1 - y_coord_2) + 1)):
            point = str(x_coord_1 + i * x_step) + ", " + str(y_coord_1 + i * y_step)
            danger_zones[point] = danger_zones.get(point, 0) + 1

    return [(k, v) for k, v in danger_zones.items() if int(v) > 1]

if __name__ == '__main__':
    data = file_util.read_file(file_path, split=True, split_str=' -> ')
    print(len(find_danger_zones(data)))
    