import random
import math

from game.point import Point
from game import constants


def limit(inputValue, minVal, maxVal):
    return max(min(inputValue, maxVal), minVal)

def vector(p1, p2):
    return (p2.get_y() - p1.get_x()) / (p2.get_x() - p1.get_x())

def theta(p1, p2):
    return math.atan2(p2.get_y() - p1.get_y(), p2.get_x() - p1.get_x())