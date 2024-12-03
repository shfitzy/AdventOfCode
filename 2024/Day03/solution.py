import os
import re
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

# This regex searches for the literal string "mul(" followed by 1 to 3 digits, followed by the literal ",", followed by another 1 to 3
# digits, followed by the literal ")".
MUL_COMMAND_REGEX = r"mul\(\d{1,3},\d{1,3}\)"

# This regex searches for all text blocks within the input that exists between "do()" and "don't()" blocks. The "^" near the beginning is
# there to ensure it also includes text at the beginning of the input (before any "do()" or "don't()" block. The regex for the text in
# between the "do()" and "don't()" blocks includes whitespace characters, and uses a lazy quantifier to make sure it escapes as soon as
# it finds a "don't()" block. This also includes a "$" at the end of the regex to allow for a trailing "do()" block to run through to the
# end of the input, since there's potentially no "don't()" block to escape it.
INPUT_INCLUSION_FILTER_REGEX = r"(?:^|do\(\))(?:\s|.)*?(?:$|don't\(\))"

def calc_mul_commands_in_string(data):
    """
    Returns the cumulative sum of the product of the two numbers in each mul command.

    :param data: The input string to calculate the sum of the mul commands from
    """
    return sum([int(cmd[4:-1].split(",")[0]) * int(cmd[4:-1].split(",")[1]) for cmd in re.findall(MUL_COMMAND_REGEX, data)])

def calc_mul_commands_within_conditionals(data):
    """
    Returns the cumulative sum of the product of the two numbers in each mul command that exists within each block of text that does
    not exist within a "don't()" section of the input.

    :param data: The input string to calculate the sum of the mul commands from
    """
    return sum([calc_mul_commands_in_string(block) for block in re.findall(INPUT_INCLUSION_FILTER_REGEX, data)])

if __name__ == '__main__':
    """
    Solution for the Advent of Code 2024, Day 3 challenges. [https://adventofcode.com/2024/day/3]

    The solution uses regex to parse out the multiplication commands ("mul(###,###)") from the input string. For each instance it 
    finds, it will add the product of the two numbers in the command to a running total. For part 2 of the solution, an additional
    regex is used, which limits which parts of the input string checked, so that no commands are processed that occur after a "don't()"
    block before the next "do()".
    """
    data = file_util.read(file_path, 'input.txt')
    
    print(calc_mul_commands_in_string(data))
    print(calc_mul_commands_within_conditionals(data))