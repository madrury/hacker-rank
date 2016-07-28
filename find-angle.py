# Note: python 2.7
import sys
from math import atan

PI = 3.1415927

def to_degree(angle):
    return angle * (360 / (2 * PI))

def make_pretty_degree_output(angle):
    number_string = str(int(round(to_degree(angle), 0)))
    degree_string = number_string + u"\u00b0"
    return degree_string

def parse_input():
    AB = float(sys.stdin.readline().strip())
    BC = float(sys.stdin.readline().strip())
    return AB, BC

def calc_angle(AB, BC):
    angle = atan(AB / BC)
    return angle


if __name__ == '__main__':
    AB, BC = parse_input()
    angle = calc_angle(AB, BC)
    print make_pretty_degree_output(angle) 
