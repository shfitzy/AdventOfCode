import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def unpack_input(line):
    return int(line.split(":")[0]), [int(i) for i in line.split(":")[1].split()]

def check_validity(working_target, nums, operators):
    """
    Recursive function used to determine whether or not it is possible to generate the given number (target) given a list of numbers
    used in the equation, and the available operands. In order to prevent the complexity from reaching 2^n (or 3^n for the second part),
    some shortcuts are taken - since the operands are processed in left-to-right order, the data can be solved from right to left with the
    following shortcuts:
    * If the last number in the list does not match the end of the target value, we do not need to consider the concat ('||') operator.
    * If the last number in the list does not evenly divide the target value, we do not need to consider the multiplcation ('*') operator.
    * If the last number in the list is greater than or equal to the target value, we do not need to consider the addition ('+') operator.
    
    If any of the above do apply, we recursively call this fuction by reducing the target value (by de-concatenating, dividing, or
    subtracting it depending on the operand) and passing in the list of numbers, excluding the last number. If we reach the last number
    and it equals the target number, we have a valid answer. If we've exhausted all possibilities, there is no valid answer.

    :param working_target: The target number we are trying to achieve with the given input
    :param nums: The list of ordered numbers to be used in the equation to generate the target number
    :param operators: A list of available operators to be used with the numbers to generate the target
    """
    if(len(nums) == 1): return True if (nums[0] == working_target) else False

    result = 0
    if(('||' in operators) and str(working_target).endswith(str(nums[-1])) and (not working_target == nums[-1])):
        result = check_validity(int(str(working_target)[:(-1)*len(str(nums[-1]))]), nums[:-1], operators)

    if(('*' in operators) and (working_target % nums[-1] == 0) and not result):
        result = check_validity(int(working_target / nums[-1]), nums[:-1], operators)

    if(('+' in operators) and (working_target >= nums[-1]) and not result):
        result = check_validity(int(working_target - nums[-1]), nums[:-1], operators)

    return result

if __name__ == '__main__':
    input = file_util.read_file(file_path, 'input.txt')

    print(sum([unpack_input(line)[0] for line in input if(check_validity(*unpack_input(line), {'+', '*'}))]))
    print(sum([unpack_input(line)[0] for line in input if(check_validity(*unpack_input(line), {'+', '*', '||'}))]))