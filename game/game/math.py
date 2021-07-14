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

def hypotenuse(x, y):
    return math.sqrt((x**2) + (y**2))

def angle(h, y):
    # Finds the sin to use for a 
    try:
        return math.sin(y / h)
    except:
        return math.sin(y/ (h + 1))

def cartesian(X1, Y1, X2, Y2):
    # Finds which place a x1 and x2 is relative to x2 and y2 via cartesian plane
    if Y1 < Y2:
        if X1 < X2:
            cartesian = 3
        else:
            cartesian = 4
    elif Y1 > Y2:
        if X1 > X2:
            cartesian = 1
        else:
            cartesian = 2
    else:
        return 1
    return cartesian

def direction(cartesian, angle):
    # Determines the absolute angle of one source to another
    if cartesian == 1:
        direction = angle * 100
    elif cartesian == 2:
        direction = 180 - (angle * 100)
    elif cartesian == 3:
        direction = 180 + (angle * 100)
    elif cartesian == 4:
        direction = 360 - (angle * 100)
    return direction