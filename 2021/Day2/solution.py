import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util
from utils.data_structs.point import Point3D



class Sub:

    def __init__(self, alt_func):
        self.x = 0
        self.y = 0
        self.aim = 0
        self.alt_func = alt_func

    def forward(self, val):
        self.x += val
        if self.alt_func:
            self.y += self.aim * val

    def up(self, val):
        if not self.alt_func:
            self.y -= val
        else:
            self.aim -= val

    def down(self, val):
        if not self.alt_func:
            self.y += val
        else:
            self.aim += val

    def execute_command(self, command, val):
        if(command == 'forward'):
            self.forward(val)
        elif(command == 'up'):
            self.up(val)
        elif(command == 'down'):
            self.down(val)

    def get_value(self):
        return self.x * self.y



def execute_commands(commands, alt_func=False):
    sub = Sub(alt_func)
    for command, val in commands:
        sub.execute_command(command, int(val))

    print(sub.get_value())
    

if __name__ == '__main__':
    execute_commands(file_util.read_file(file_path, split=True))
    execute_commands(file_util.read_file(file_path, split=True), True)