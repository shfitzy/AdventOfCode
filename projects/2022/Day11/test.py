import os
import sys
import unittest

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir))
sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir, os.path.pardir))

import solution

from utils import file_util

# class TestSolution(unittest.TestCase):

#     def test_part_one(self):
#         input = solution.read_input_and_transform(file_path + os.path.sep + 'input.txt')
#         result = solution.get_tail_locations(input)
#         self.assertEqual(len(result), 6745)

#     def test_part_two(self):
#         input = solution.read_input_and_transform(file_path + os.path.sep + 'input.txt')
#         result = solution.get_tail_locations(input, 10)
#         self.assertEqual(len(result), 2793)

class TestProvidedExample(unittest.TestCase):

    def test_puzzle_one_with_example(self):
        input = file_util.read(file_path + os.path.sep + 'test_input_1.txt')
        monkeys = solution.initialize_monkeys(input)
        self.assertEqual(solution.play_game(monkeys), 10605)
    
    # def test_puzzle_two_with_example(self):
    #     input = file_util.read_lines(file_path + os.path.sep + 'test_input_1.txt')
    #     signal_data = solution.generate_signal_data(input)
    #     solution.print_pixels(signal_data)

if __name__ == '__main__':
    unittest.main()