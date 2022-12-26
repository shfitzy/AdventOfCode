import os
import sys
import unittest
import random

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir))
sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir, os.path.pardir))

import solution
from utils import file_util

class TestSolution(unittest.TestCase):

    def test_solution_with_incrementing_values(self):
        input = range(0, random.randint(10, 1000))
        result = solution.get_num_incrementing_windows(input)
        self.assertEqual(result, len(input) - 1)

    def test_solution_is_zero_for_decrementing_values(self):
        input = range(random.randint(10, 1000), 0, -1)
        result = solution.get_num_incrementing_windows(input)
        self.assertEqual(result, 0)

    def test_solution_is_zero_same_values(self):
        input = [0] * random.randint(10, 1000)
        result = solution.get_num_incrementing_windows(input)
        self.assertEqual(result, 0)

class TestProvidedExample(unittest.TestCase):

    def test_solution_with_provided_example(self):
        input = file_util.read_lines(file_path + os.path.sep + 'example_input.txt')
        self.assertEqual(solution.get_num_incrementing_windows(input), 7)

    def test_solution_with_provided_example_with_window_of_3(self):
        input = file_util.read_lines(file_path + os.path.sep + 'example_input.txt')
        self.assertEqual(solution.get_num_incrementing_windows(input, 3), 5)

if __name__ == '__main__':
    unittest.main()