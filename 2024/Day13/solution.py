import os
import re
import sys

file_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def calc_min_tokens_to_win_all(machine, prize_mod_fnct=lambda i: i):
    """
    This function is given a string representing the input for a given machine, and solves the system of equations provided to it.
    If the system of equations has no solution, or if the solution exists, but 'a' and 'b' are not both integers greater than or equal
    to zero, this function returns 0. Otherwise, it will return 3 times the number of a button presses required plus the number of b
    button presses required.

    :param machine: The string representation of an individual machine from the puzzle input.
    :param prize_mod_fnct: An optional parameter you can pass in to modify the prize data given by the input. By default this is
    an identity function.
    """
    btn_a_x, btn_a_y = map(lambda x: int(x), re.search('Button A: X+(.*), Y+(.*)', machine).groups())
    btn_b_x, btn_b_y = map(lambda x: int(x), re.search('Button B: X+(.*), Y+(.*)', machine).groups())
    prize_x, prize_y = map(lambda x: prize_mod_fnct(int(x)), re.search('Prize: X=(.*), Y=(.*)', machine).groups())
    
    tmp1 = btn_a_y * btn_b_x - btn_a_x * btn_b_y
    tmp2 = btn_a_y * prize_x - btn_a_x * prize_y
    
    a_btn_presses = b_btn_presses = 0

    if tmp1 == 0:
        can_get_prize_with_only_a = (prize_x % btn_a_x == 0) and prize_y == (prize_x / btn_a_x) * btn_a_y
        can_get_prize_with_only_b = (prize_x % btn_b_x == 0) and prize_y == (prize_x / btn_b_x) * btn_b_y
        a_to_b_ratio = btn_a_x / btn_b_x

        a_btn_presses = (prize_x / btn_a_x) if can_get_prize_with_only_a and (not can_get_prize_with_only_b or a_to_b_ratio >= 3) else 0
        b_btn_presses = (prize_x / btn_b_x) if can_get_prize_with_only_b and (not can_get_prize_with_only_a or a_to_b_ratio < 3) else 0
    elif tmp1 != 0 and tmp2 % tmp1 == 0:
        b_btn_presses = tmp2 / tmp1
        a_btn_presses = (prize_x - (b_btn_presses * btn_b_x)) / btn_a_x

        if a_btn_presses < 0 or b_btn_presses < 0:
            return 0

    return int(b_btn_presses + 3 * a_btn_presses)

if __name__ == '__main__':
    input = file_util.read(file_path, 'input.txt').split('\n\n')

    print(sum([calc_min_tokens_to_win_all(machine) for machine in input]))
    print(sum([calc_min_tokens_to_win_all(machine, prize_mod_fnct=lambda i: i + 10000000000000) for machine in input]))