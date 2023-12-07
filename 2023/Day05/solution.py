import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util



class Mapping:

    def __init__(self, dest, src, rng):
        self.src = src
        self.dest = dest
        self.rng = rng

    def __gt__(self, other):
        return self.dest > other.dest
    
    def __str__(self):
        return '(' + str(self.src) + ', ' + str(self.src + self.rng - 1) + ') -> (' + str(self.dest) + ', ' + str(self.dest + self.rng - 1) + ')'
    
    def overlaps(self, other):
        overlap = len(range(max(self.dest, other.src), min(self.dest + self.rng, other.src + other.rng)))
        # if(overlap > 0):
        #     print('<OVERLAP>')
        #     print(self)
        #     print(other)
        #     print('<-------->')
        return overlap > 0
    


def get_map_data(data):
    all_mappings = []
    for line in data:
        layer_mappings = []
        for mapping in line.split('\n'):
            layer_mappings.append(list(map(lambda i: int(i), mapping.split())))
        all_mappings.append(layer_mappings)
    return all_mappings

def get_mapping_layer_data(mapping_layer):
    new_mappings = []

    for mapping in mapping_layer.split('\n'):
        dest, src, rng = map(lambda i: int(i), mapping.split())
        m = Mapping(dest, src, rng)
        new_mappings.append(m)

    return sorted(new_mappings)

def add_mapping(mapping, all_mappings):
    new_mappings = []
    collisions = []

    for m in all_mappings:
        if m.overlaps(mapping):
            new_mappings.append(m)
        else:
            collisions.append(m)

    if(len(collisions) == 0):
        new_mappings.append(mapping)

    # [print(m) for m in new_mappings]
    return new_mappings

def get_map_data_2(data):
    all_mappings = []

    for mapping_layer in data:
        new_mappings = []
        layer_mappings = get_mapping_layer_data(mapping_layer)
        for m in layer_mappings:
            new_mappings.extend(add_mapping(m, all_mappings))

        all_mappings = sorted(new_mappings)
        print('----------')
        [print(m) for m in all_mappings]
        print('----------')

    return all_mappings

def get_lowest_seed_pos(seeds, map_data):
    positions = []

    for id in seeds:
        for layer_map in map_data:
            for mapping in layer_map:
                if id >= mapping[1] and id < mapping[1] + mapping[2]:
                    id = id - mapping[1] + mapping[0]
                    break
        positions.append(id)

    return min(positions)

def solution_1(data):
    seeds = list(map(lambda i: int(i), data[0].split(': ')[1].split(' ')))
    map_data = get_map_data(data[1:])

    return get_lowest_seed_pos(seeds, map_data)

def solution_2(data):
    seeds = list(map(lambda i: int(i), data[0].split(': ')[1].split(' ')))
    map_data = get_map_data(data[1:])
    min_value = 1000000000

    for i in range(int(len(seeds) / 2)):
        for j in range(seeds[i * 2 + 1]):
            id = seeds[i * 2] + j
            for layer_map in map_data:
                for mapping in layer_map:
                    if id >= mapping[1] and id < mapping[1] + mapping[2]:
                        id = id - mapping[1] + mapping[0]
                        break

            if id < min_value: min_value = id

    return min_value
    # get_map_data_2(data[1:])
    # return 'hi'

if __name__ == '__main__':
    data = file_util.read(file_path, 'input.txt', split=True, regex_split=True, split_str='\n\n.*:\n')

    # print(solution_1(data))
    print(solution_2(data))