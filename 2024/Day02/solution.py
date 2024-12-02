import itertools
import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util
    
def is_safe_report(report, dampener_level=0, min_diff=1, max_diff=3):
    """
    Checks whether or not the given input list of integers increases or decreases within the given bounds.

    :param report: The list of integers that is checked
    :param dampener_level: The maximum number of errors (levels that can be removed) that can be removed from the report to determine if it is safe
    :param min_diff: The minimum (inclusive) difference each consecutive integer must maintain
    :param max_diff: The maximum (inclusive) difference each consecutive integer must maintain
    :return: Returns True if each integer in the list increases or decreases within the range specified, False otherwise
    """

    # If the number of errors allowed could allow for the list of levels within the report to reduce to one value, return True, since
    # the conditions that would make the report unsafe can not occur.
    if dampener_level >= len(report) - 1:
        return True
    
    # Generate a list of all possible sets of indices within the report list that can be excluded, based on the dampener_level.
    # Ex: If we allow for 1 error in a report of length 5, we'll generate the list [{0], {1}, {2}, {3}, {4}]
    exclusions = [set(v) for v in itertools.combinations(range(len(report)), dampener_level)]

    # For each set of exclusions, we want to create a sublist that excludes the indices in the set, and then check the sublist to see if it is safe.
    for exclusion_set in exclusions:
        sublist = [value for idx, value in enumerate(report) if idx not in exclusion_set]

        if all((sublist[i] + min_diff) <= sublist[i + 1] <= (sublist[i] + max_diff) for i in range(len(sublist) - 1)):
            # All values in the sublist increase within an acceptable range. Return True since the report is safe when excluding the values in the exclusion_set.
            return True
        elif all((sublist[i] - min_diff) >= sublist[i + 1] >= (sublist[i] - max_diff) for i in range(len(sublist) - 1)):
            # All values in the sublist decrease within an acceptable range. Return True since the report is safe when excluding the values in the exclusion_set.
            return True

    # No set of exclusions allows for the report to be safe, so we return False.
    return False

if __name__ == '__main__':
    """
    Generalized solution for the Advent of Code 2024, Day 2 challenges. [https://adventofcode.com/2024/day/2]

    This solution allows for the modification of both the number of errors allowed in the input (dampener_level), as well as the acceptable range required
    for values in the report to increase/decrease to be considered safe (min_diff and max_diff). The only change required to find the solution for the first
    and second parts of the problem are to change the value of the dampener_level from 0 to 1, which determines how many values can be removed from the report
    and have it still be considered safe.
    """
    reports = file_util.get_2d_int_array(file_path, 'input.txt')
    
    for dampener_level in range(2):
        print(sum([is_safe_report(report, dampener_level) for report in reports]))