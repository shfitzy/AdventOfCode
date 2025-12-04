import os
import re
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util
from utils.timer import timer

def repeated_id_regex_check(id_ranges, regex):
    # for i, regex in enumerate([r'^(.+)\1{1}$', r'^(.+)\1{1,}$']):
    value = 0
    
    for id_range in id_ranges:
        start, end = map(int, id_range.split('-'))
        for id in range(start, end + 1):
            if re.match(regex, str(id)):
                value += id

    return value

def get_factor_mapping(mapping, len):
    if not mapping.get(len):
        factors = []
        for i in range(2, len+1):
            if len % i == 0: factors.append(i)
        mapping[len] = factors

    return mapping.get(len)

def get_invalid_sum_in_range(start, end, invalid_values=set(), allowed_factors=None, factor_mappings={}):
    if len(str(start)) != len(str(end)):
        get_invalid_sum_in_range(int('1' + '0' * len(str(start))), end, invalid_values, allowed_factors, factor_mappings)
        end = int('9' * len(str(start)))
    
    str_length = len(str(start))
    for factor in get_factor_mapping(factor_mappings, str_length):
        if (not allowed_factors or factor in allowed_factors) and len(str(start)) % (str_length // factor) == 0:
            substr_id_start, substr_id_end = int(str(start)[:str_length // factor]), int(str(end)[:str_length // factor]) + 1
            for i in range(substr_id_start, substr_id_end + 1):
                full_num = int(str(i) * factor)
                if full_num >= start and full_num <= end:
                    invalid_values.add(full_num)

    return invalid_values

def repeated_id_algorithmic_check(id_ranges, allowed_factors):
    invalid_values = set()

    for id_range in id_ranges:
        start, end = map(int, id_range.split('-'))
        get_invalid_sum_in_range(start, end, invalid_values, allowed_factors)

    return sum(invalid_values)
        
if __name__ == '__main__':
    id_ranges = file_util.read(file_path, 'input.txt').split(',')

    timer(repeated_id_regex_check, 'Part 1 - Regex Check', id_ranges, r'^(.+)\1{1}$')
    timer(repeated_id_regex_check, 'Part 2 - Regex Check', id_ranges, r'^(.+)\1{1,}$')
    timer(repeated_id_algorithmic_check, 'Part 1 - Algorithmic Check', id_ranges, {2})
    timer(repeated_id_algorithmic_check, 'Part 2 - Algorithmic Check', id_ranges, None)