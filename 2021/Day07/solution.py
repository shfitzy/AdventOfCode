import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util



class PositionData:

    def __init__(self, position, count):
        self.position = position
        self.count = count
        self.penalty = 0
        self.fuel_spent = 0

    def __gt__(self, other):
        return self.position > other.position
    
    def move(self, direction, add_penalty):
        self.fuel_spent += self.penalty + self.count
        if(add_penalty):
            self.penalty += self.count
        self.position += direction

    def add(self, other):
        self.count += other.count
        self.penalty += other.penalty
        self.fuel_spent += other.fuel_spent

    def get_next_movement_cost(self):
        return self.penalty + self.count



def set_up_crab_data(data):
    crab_data = {}
    for v in data:
        crab_data[int(v)] = crab_data.get(int(v), 0) + 1
    return sorted(list(map(lambda k: PositionData(k, crab_data[k]), crab_data)))

def move_crabs(crab_data, use_penalty):
    while len(crab_data) > 1:
        if crab_data[0].get_next_movement_cost() < crab_data[len(crab_data) - 1].get_next_movement_cost():
            crab_data[0].move(1, use_penalty)
            if crab_data[0].position == crab_data[1].position:
                crab_data[1].add(crab_data[0])
                crab_data.pop(0)
        else:
            crab_data[len(crab_data) - 1].move(-1, use_penalty)
            if crab_data[len(crab_data) - 1].position == crab_data[len(crab_data) - 2].position:
                crab_data[len(crab_data) - 2].add(crab_data[len(crab_data) - 1])
                crab_data.pop()

    print(crab_data[0].fuel_spent)
        
if __name__ == '__main__':
    crab_data = set_up_crab_data(file_util.read_file(file_path, filename='input.txt', split=True, split_str=',')[0])
    move_crabs(crab_data, False)

    crab_data = set_up_crab_data(file_util.read_file(file_path, filename='input.txt', split=True, split_str=',')[0])
    move_crabs(crab_data, True)