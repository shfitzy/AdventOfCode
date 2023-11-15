import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def get_num_incrementing_windows(input, offset=1):
    return len([i for i, x in enumerate(input) if i > offset-1 and x > input[i-offset]])

if __name__ == '__main__':
    print(get_num_incrementing_windows(file_util.get_int_array(file_path)))