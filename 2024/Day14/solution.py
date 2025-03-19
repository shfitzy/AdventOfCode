import os
import re
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.join(file_path, os.path.pardir, os.path.pardir))

from utils import file_util

class Robot:

    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel



def init_robots(input):
    robots = []

    for line in input:
        pos = tuple(map(int, re.search('p=([\\-0-9]*),([\\-0-9]*)', line).groups()))
        vel = tuple(map(int, re.search('v=([\\-0-9]*),([\\-0-9]*)', line).groups()))
        robots.append(Robot(pos, vel))

    return robots

def calc_future_state(robots, time_interval, grid_width, grid_height):
    q1 = q2 = q3 = q4 = 0

    for robot in robots:
        final_pos = (((robot.pos[0] + time_interval * robot.vel[0]) % grid_width), ((robot.pos[1] + time_interval * robot.vel[1]) % grid_height))
        if final_pos[0] < int(grid_width / 2) and final_pos[1] < int(grid_height / 2): q1 += 1
        elif final_pos[0] < int(grid_width / 2) and final_pos[1] > int(grid_height / 2): q2 += 1
        elif final_pos[0] > int(grid_width / 2) and final_pos[1] < int(grid_height / 2): q3 += 1
        elif final_pos[0] > int(grid_width / 2) and final_pos[1] > int(grid_height / 2): q4 += 1

    return q1 * q2 * q3 * q4

def print_timelapse(robots, time_interval, grid_width, grid_height):
    f = open("demofile2.txt", "a")

    for i in range(time_interval + 1):
        robot_positions = set()
        for robot in robots:
            robot_positions.add((((robot.pos[0] + i * robot.vel[0]) % grid_width), ((robot.pos[1] + i * robot.vel[1]) % grid_height)))

        f.write(str(i))
        for y in range(grid_height):
            for x in range(grid_width):
                f.write(' ' if (x, y) not in robot_positions else '*')
            f.write('\n')
        f.write('\n\n')
    f.close()

if __name__ == '__main__':
    robots = init_robots(file_util.read(file_path, 'input.txt').split('\n'))

    print(calc_future_state(robots, 100, 101, 103))
    print_timelapse(robots, 10000, 101, 103)