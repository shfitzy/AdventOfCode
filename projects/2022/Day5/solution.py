from functools import reduce
import os
import re

file_path = os.path.dirname(os.path.realpath(__file__))

# Transforms the input into two objects - an initial state of the stacks of boxes (2D-array containing characters) and a list of the commands (strings) to be taken upon them
def read_input_and_transform(filename):
    with open(filename) as f:
        start_pos, commands = f.read().split('\n\n')
        
        stacks = [[line[1 + 4 * i] for line in reversed(start_pos.split('\n')[:-1]) if line[1 + 4 * i] != ' '] for i in range(int(re.findall('\d+', start_pos.split('\n')[-1])[-1]))]
        # stacks = [[] for _ in range(9)]
        # for line in [line for line in start_pos.split('\n')[:-1]]:
        #     for i in range(len(stacks)):
        #         char = line[1 + 4 * i]
        #         if char != ' ':
        #             stacks[i].insert(0, char)

        return stacks, commands.split('\n')


def calc_result(stacks, commands, pop_individually=True):
    for command in commands:
        num, frm, to = [int(x) if i == 0 else int(x) - 1 for i, x in enumerate(re.findall(r'\d+', command))]
        [stacks[to].append(stacks[frm].pop(-1 if pop_individually else -1 * (num - i))) for i in range(num)]

    return reduce(lambda a, b: a + b, [stack.pop() for stack in stacks])

if __name__ == '__main__':
    print(calc_result(*read_input_and_transform(file_path + os.path.sep + 'input.txt')))
    print(calc_result(*read_input_and_transform(file_path + os.path.sep + 'input.txt'), pop_individually=False))