from game.point import Point
from game import constants

import arcade

class Trigger(arcade.Sprite):
    def __init__(self, x, y, w, h, parentMap, actionIndex=0):
        super().__init__()

        self.center_x = x
        self.center_y = y
        self.__width = w
        self.__height = h

        self.parentMap = parentMap
        self.actionIndex = actionIndex

    def activate(self):
        self.parentMap.handleTrigger(self.actionIndex)

    def _get_width(self):
        return self.__width

    def _get_height(self):
        return self.__height
