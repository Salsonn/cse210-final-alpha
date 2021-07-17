from game.point import Point
from game import constants

import arcade

class Trigger(arcade.Sprite):
    def __init__(self, x, y, w, h, parentMap, actionIndex=0):
        super().__init__(None, center_x=x, center_y=y)

        self._set_height(h)
        self._set_width(w)

        self.parentMap = parentMap
        self.actionIndex = actionIndex

    def activate(self):
        self.parentMap.handleTrigger(self.actionIndex)
