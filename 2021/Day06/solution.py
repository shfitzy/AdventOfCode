import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def set_up_fish_data(data):
    fish_data = {}
    for v in data:
        fish_data[int(v)] = fish_data.get(int(v), 0) + 1
    return fish_data

def simulate(fish_data, days):
    for i in range(max(days)):
        tmp_data = {}
        for k, v in fish_data.items():
            if k > 0:
                tmp_data[k - 1] = tmp_data.get(k - 1, 0) + v
            else:
                tmp_data[6] = tmp_data.get(6, 0) + v
                tmp_data[8] = v
        fish_data = tmp_data

        if (i+1) in days:
            print('Day ' + str(i+1) + ': ' + str(sum([v for k, v in fish_data.items()])))

if __name__ == '__main__':
    fish_data = set_up_fish_data(file_util.read_file(file_path, split=True, split_str=',')[0])
    simulate(fish_data, {80, 256})