import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

if __name__ == '__main__':
    rules, updates = file_util.read(file_path, 'input.txt').split("\n\n")

    correct_sum = 0
    incorrect_sum = 0

    for update in updates.split():
        update = [int(i) for i in update.split(",")]
        update_set = set(update)
        valid = True
        is_error = True

        while is_error:
            is_error = False
            for rule in rules.split():
                num_1, num_2 = [int(i) for i in rule.split("|")]
                if {num_1, num_2}.issubset(update_set):
                    index_1, index_2 = update.index(num_1), update.index(num_2)
                    if index_1 > index_2:
                        update[index_1] = num_2
                        update[index_2] = num_1
                        valid = False
                        is_error = True


        if(valid): correct_sum += update[int((len(update) - 1) / 2)]
        else: incorrect_sum += update[int((len(update) - 1) / 2)]

    print(correct_sum)
    print(incorrect_sum)