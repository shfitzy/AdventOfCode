from collections import Counter
import os
import sys

if __name__ == '__main__':
    input = file_util.read(file_path, 'test_input.txt').split("\n\n")

    page_order = [page for page, _ in Counter([item for sublist in [[r.split("|")[0], r.split("|")[0], r.split("|")[1]] for r in input[0].split()] for item in sublist]).most_common()]
    print(*[sum(int([i for i in page_order if i in update][int((len([i for i in page_order if i in update]) - 1) / 2)]) for update in [[_ for _ in update.split(",")] for update in input[1].split()] if ([i for i in page_order if i in update] == update) == b) for b in [True, False]], sep='\n')