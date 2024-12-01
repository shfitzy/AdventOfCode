from functools import reduce
import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def calc_expense_report(entries, n = 2, target = 2020):
    possible_solutions = []

    for entry in entries:
        new_solutions = [[entry]]
        for solution in possible_solutions:
            if sum(solution) + entry == target and (len(solution) == (n - 1)):
                return reduce(lambda x, y: x * y, solution) * entry
            elif sum(solution) + entry < target and (len(solution) < (n - 1)):
                new_solution = solution[:]
                new_solution.append(entry)
                new_solutions.append(new_solution)
        
        possible_solutions.extend(new_solutions)


if __name__ == '__main__':
    entries = file_util.get_int_array(file_path, 'input.txt')

    print(calc_expense_report(entries))
    print(calc_expense_report(entries, 3))