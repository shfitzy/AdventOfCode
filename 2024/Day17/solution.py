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

def get_next_output(registers, program, ptr):
    while ptr < len(program) - 1:
        instr = program[ptr]
        operand = program[ptr + 1]

        if instr != 3 or registers[0] == 0:
            ptr += 2

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
            return [get_combo_operand(operand, registers) % 8, registers, ptr]
        elif instr == 6:
            registers[1] = registers[0] // (2 ** get_combo_operand(operand, registers))
        elif instr == 7:
            registers[2] = registers[0] // (2 ** get_combo_operand(operand, registers))

    return [None, None, None]

def fix_program(registers, program):
    reverse_output = program[::-1]
    
    ptr = 0
    a_reg = 0
    for output in reverse_output:
        a_reg *= 8

        for i in range(0, 8):
            print('Testing: ' + str(i))
            result = get_next_output([a_reg, registers[1], registers[2]], program, ptr)

            if not result: continue
            elif result[0] == output:
                print('Found output: ' + str(result[0]))
                registers = result[1]
                ptr = result[2]

    return a_reg

if __name__ == '__main__':
    registers, program = file_util.read(file_path, 'test_input.txt').split('\n\n')
    registers = [int(line.split(': ')[1]) for line in registers.split('\n')]
    program = [int(i) for i in program.split(': ')[1].split(',')]

    print(get_program_result(registers, program))
    print(fix_program(registers, program))