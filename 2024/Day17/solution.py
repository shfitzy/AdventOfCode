import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

def get_combo_operand(operand, registers):
    if 0 <= operand < 4: return operand
    elif operand == 4: return registers[0]
    elif operand == 5: return registers[1]
    elif operand == 6: return registers[2]

def get_program_result(registers, program):
    ptr = 0
    output = []

    while ptr < len(program) - 1:
        instr = program[ptr]
        operand = program[ptr + 1]

        if instr == 0:
            registers[0] = registers[0] // (2 ** get_combo_operand(operand, registers))
        elif instr == 1:
            registers[1] = registers[1] ^ operand
        elif instr == 2:
            registers[1] = get_combo_operand(operand, registers) % 8
        elif instr == 3:
            if registers[0] != 0:
                ptr = operand
                continue
        elif instr == 4:
            registers[1] = registers[1] ^ registers[2]
        elif instr == 5:
            output.append(get_combo_operand(operand, registers) % 8)
        elif instr == 6:
            registers[1] = registers[0] // (2 ** get_combo_operand(operand, registers))
        elif instr == 7:
            registers[2] = registers[0] // (2 ** get_combo_operand(operand, registers))

        ptr += 2

    return ','.join([str(i) for i in output])

def fix_program(program):
    test_values = [[i] for i in range(8)]
    mappings = {}

    while len(test_values) > 0:
        test_value = test_values.pop(0)
        a_reg = sum([i * pow(8, idx) for idx, i in enumerate(reversed(test_value))])

        partial_solution_candidate = [int(i) for i in get_program_result([a_reg, 0, 0], program).split(',')]
        mappings[tuple(test_value)] = partial_solution_candidate

        if program == partial_solution_candidate:
            return a_reg
        elif program[len(program)-len(partial_solution_candidate):] == partial_solution_candidate:
            if len(test_value) <= 1 or mappings[tuple(test_value[:len(test_value)-1])] != partial_solution_candidate:
                [test_values.insert(0, test_value + [i]) for i in reversed(range(8))]

if __name__ == '__main__':
    registers, program = file_util.read(file_path, 'input.txt').split('\n\n')
    registers = [int(line.split(': ')[1]) for line in registers.split('\n')]
    program = [int(i) for i in program.split(': ')[1].split(',')]

    print(get_program_result(registers, program))
    print(fix_program(program))