import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

file_path = os.path.dirname(os.path.realpath(__file__))

from utils import file_util, operator_util



class Monkey:

    def __init__(self, items, operator, value, test_num, success, failure):
        self.items = items
        self.test_num = test_num
        self.success = success
        self.failure = failure
        self.inspections = 0
        self.operation = lambda x: operator_util.OPERATORS[operator](x, value if value.isnumeric() else x)



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

def worry_mod_alg(i, monkey, lcm, worry_reduction):
    i = monkey.operation(i)
    if worry_reduction > 1:
        return i // worry_reduction
    else:
        return i % lcm

def play_game(monkeys, num_rounds=20, worry_reduction=3):
    lcm = np.lcm.reduce([monkey.test_num for monkey in monkeys])
    for round in range(num_rounds):
        for monkey in monkeys:
            monkey.inspections += len(monkey.items)
            monkey.items = [worry_mod_alg(i, monkey, lcm, worry_reduction) for i in monkey.items]
            [monkeys[monkey.success if i % monkey.test_num == 0 else monkey.failure].items.append(i) for i in monkey.items]
            monkey.items = []
    
    sorted_values = sorted([m.inspections for m in monkeys], reverse=True)
    return sorted_values[0] * sorted_values[1]

if __name__ == '__main__':
    input = file_util.read(file_path + os.path.sep + 'input.txt')
    print(play_game(initialize_monkeys(input)))
    print(play_game(initialize_monkeys(input), 10000, 1))