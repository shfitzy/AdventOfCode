import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def find_matches(towels, pattern, matches=0, match_map={}):
    if pattern in match_map:
        return match_map[pattern]
        
    for towel in towels:
        if pattern.startswith(towel):
            if len(towel) == len(pattern): return matches + 1
            else: matches += find_matches(towels, pattern[len(towel):])

    match_map[pattern] = matches
    return matches

if __name__ == '__main__':
    test_mode = False
    input = file_util.read(file_path, 'test_input.txt' if test_mode else 'input.txt').split('\n\n')
    towels, patterns = sorted(input[0].split(', '), key=len), input[1].split('\n')

    results = [find_matches(towels, pattern) for pattern in patterns]

    print(f'Part 1: {sum(1 for r in results if r > 0)}')
    print(f'Part 2: {sum(r for r in results)}')