import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def filter_data(data, i=0, majority=True):
    count = sum([int(row[i]) for row in data])

    bit = '1' if majority and count >= (len(data) / 2) or not majority and count < (len(data) / 2) else '0'

    filtered_data = [row for row in data if row[i] == bit]
    return int(filtered_data[0], 2) if len(filtered_data) == 1 else filter_data(filtered_data, i+1, majority)

def part_1(data):
    sum = [0] * len(data[0])
    for row in data:
        for i, c in enumerate(row):
            sum[i] += int(c)

    gamma = int(''.join(['1' if sum[i] > len(data) / 2 else '0' for i in range(len(sum))]), 2)
    epsilon = int(''.join(['0' if sum[i] > len(data) / 2 else '1' for i in range(len(sum))]), 2)

    print(gamma * epsilon)

def part_2(data):
    oxygen_rating = filter_data(data)
    co2_rating = filter_data(data, majority=False)

    print(oxygen_rating * co2_rating)

if __name__ == '__main__':
    data = file_util.read_file(file_path)
    part_1(data)
    part_2(data)

