import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

file_path = os.path.dirname(os.path.realpath(__file__))

from utils import file_util

def generate_signal_data(commands):
    signal_strenghts = [1]
    for line in commands:
        signal_strenghts.append(signal_strenghts[-1])
        if line.split()[0] == "addx":
            signal_strenghts.append(int(line.split()[1]) + signal_strenghts[-1])

    return signal_strenghts

def calc_signal_strength(signal_data, indices=[20, 60, 100, 140, 180, 220]):
    return sum([i * signal_data[i-1] for i in indices])

def print_pixels(signal_data):
    signal_data = signal_data[:240]
    pixels = ['#' if abs(signal_data[i] - (i % 40)) <= 1 else ' ' for i in range(len(signal_data))]
    
    for i in range(len(pixels)):
        end_char = '\n' if i % 40 == 39 else ''
        print(pixels[i], end=end_char)
            
if __name__ == '__main__':
    commands = file_util.read_lines(file_path + os.path.sep + 'input.txt')
    signal_data = generate_signal_data(commands)
    print(calc_signal_strength(signal_data))
    print_pixels(signal_data)