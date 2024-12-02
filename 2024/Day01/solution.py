from collections import Counter
import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def calc_distance(list_1, list_2):
    list_1 = sorted(list_1)
    list_2 = sorted(list_2)

    print(sum([abs(list_1[i] - list_2[i]) for i in range(len(list_1))]))

def calc_similarity_score(list_1, list_2):
    map_1 = Counter(list_1)
    map_2 = Counter(list_2)

    print(sum([k * v * map_2.get(k) if map_2.get(k) else 0 for k, v in map_1.items()]))

if __name__ == '__main__':
    list_1, list_2 = [], []
    for line in file_util.read_file(file_path, 'input.txt'):
        list_1.append(int(line.split()[0]))
        list_2.append(int(line.split()[1]))
    
    calc_distance(list_1, list_2)
    calc_similarity_score(list_1, list_2)