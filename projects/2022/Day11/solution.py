import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

file_path = os.path.dirname(os.path.realpath(__file__))

from utils import file_util



class Monkey:

    def __init__(self, items, operator, value, test_num, success, failure):
        self.items = items
        self.test_num = test_num
        self.success = success
        self.failure = failure
        self.inspections = 0

        if operator == '+':
            self.operation = lambda x: x + int(value)
        elif operator == '*':
            if value == 'old':
                self.operation = lambda x: x * x
            else:
                self.operation = lambda x: x * int(value)



def initialize_monkeys(input):
    monkeys = []

    for monkey_data in input.split('\n\n'):
        lines = monkey_data.split('\n')
        items = [int(i) for i in lines[1].strip('Starting items:').split(',')]
        test_num = int(lines[3].split()[-1])
        success = int(lines[4].split()[-1])
        failure = int(lines[5].split()[-1])
        operator, value = lines[2].split()[-2:]

        monkeys.append(Monkey(items, operator, value, test_num, success, failure))

    return monkeys

def play_game(monkeys, num_rounds=20, worry_reduction=3):
    lcm = np.lcm.reduce([monkey.test_num for monkey in monkeys])
    for round in range(num_rounds):
        for monkey in monkeys:
            monkey.inspections += len(monkey.items)
            monkey.items = [i % lcm for i in monkey.items]
            for item in monkey.items:
                item = monkey.operation(item)
                item //= worry_reduction
                # item = item % lcm
                if item % monkey.test_num == 0:
                    monkeys[monkey.success].items.append(item)
                else:
                    monkeys[monkey.failure].items.append(item)
            monkey.items = []
    
    sorted_values = sorted([m.inspections for m in monkeys], reverse=True)
    print(sorted_values)
    return sorted_values[0] * sorted_values[1]

if __name__ == '__main__':
    input = file_util.read(file_path + os.path.sep + 'input.txt')
    monkeys = initialize_monkeys(input)
    print(play_game(monkeys))
    # monkeys = initialize_monkeys(input)
    # print(play_game(monkeys, 10000, 1))