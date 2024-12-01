import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def is_valid_password(password):
    min, max = map(lambda i: int(i), password[0].split('-'))
    letter = password[1][0]
    return min <= sum([letter == c for c in password[2]]) <= max

if __name__ == '__main__':
    passwords = file_util.read_file(file_path, 'test_input.txt', split=True)

    print(sum([is_valid_password(password) for password in passwords]))
