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
            print("[Instr 0] Updating register A: " + str(registers[0]) + " -> ", end='')
            registers[0] = registers[0] // (2 ** get_combo_operand(operand, registers))
            print(registers[0])
        elif instr == 1:
            print("[Instr 1] Updating register B: " + str(registers[1]) + " -> ", end='')
            registers[1] = registers[1] ^ operand
            print(registers[1])
        elif instr == 2:
            print("[Instr 2] Updating register B: " + str(registers[1]) + " -> ", end='')
            registers[1] = get_combo_operand(operand, registers) % 8
            print(registers[1])
        elif instr == 3:
            if registers[0] != 0:
                ptr = operand
                continue
        elif instr == 4:
            registers[1] = registers[1] ^ registers[2]
        elif instr == 5:
            return [get_combo_operand(operand, registers) % 8, registers, ptr]
        elif instr == 6:
            print("[Instr 6] Updating register B: " + str(registers[1]) + " -> ", end='')
            registers[1] = registers[0] // (2 ** get_combo_operand(operand, registers))
            print(registers[1])
        elif instr == 7:
            print("[Instr 7] Updating register C: " + str(registers[2]) + " -> ", end='')
            registers[2] = registers[0] // (2 ** get_combo_operand(operand, registers))
            print(registers[2])

    return None

def fix_program(program):
    reverse_output = program[::-1]
    
    output_idx = 0
    start_at = 0
    a_reg = 0

    while True:
        found_output = False

        for i in range(start_at, 8):
            tmp_a_reg = a_reg * 8 + i
            b_reg = tmp_a_reg % 8
            b_reg = b_reg ^ 1
            c_reg = tmp_a_reg // pow(2, b_reg)
            b_reg = (b_reg ^ c_reg) % 8
            b_reg = b_reg ^ 4

            if b_reg == reverse_output[output_idx]:
                # print('Found output: ' + str(i))
                a_reg = a_reg * 8 + i

                if output_idx == len(reverse_output) - 1:
                    return a_reg
                else:
                    found_output = True
                    output_idx += 1
                    start_at = 0
                    break

        if not found_output: # If we didn't find a valid output for the current output index, we need to backtrack
            if output_idx == 0: # If we haven't found any output for the first output in the reverse list, then there is no solution
                # print('No solution found')
                return -1
            else: # Backtrack to the previous output and try the next possible value for that output
                # print('No output found for: ' + str(reverse_output[output_idx]))
                start_at = (a_reg % 8) + 1
                a_reg //= 8
                output_idx -= 1

if __name__ == '__main__':
    registers, program = file_util.read(file_path, 'input.txt').split('\n\n')
    registers = [int(line.split(': ')[1]) for line in registers.split('\n')]
    program = [int(i) for i in program.split(': ')[1].split(',')]

    print(get_program_result(registers, program))
    print(fix_program(program))