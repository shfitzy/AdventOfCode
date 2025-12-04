import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util
from utils.timer import timer

def find_first_idx_of_max_in_range(bank, start_idx, end_idx):
    max_value = 0
    idx = start_idx

    for i in range(start_idx, end_idx):
        value = int(bank[i])
        if value > max_value:
            max_value = value
            idx = i
            if value == 9: break

    return idx

def get_battery_bank_output(bank, num_batteries):
    battery_indices = []
    for i in range(num_batteries):
        start_idx = 0 if len(battery_indices) == 0 else battery_indices[-1] + 1
        end_idx = len(bank) - num_batteries + i + 1
        battery_indices.append(find_first_idx_of_max_in_range(bank, start_idx, end_idx))

    return sum([int(bank[value]) * pow(10, idx) for idx, value in enumerate(reversed(battery_indices))])

def calc_max_voltage(battery_banks, num_batteries):
    return sum([get_battery_bank_output(bank, num_batteries) for bank in battery_banks])

if __name__ == '__main__':
    input = file_util.read(file_path, 'input.txt').split('\n')

    timer(calc_max_voltage, 'Part 1', 10, input, 2)
    timer(calc_max_voltage, 'Part 2', 10, input, 12)