from game.point import Point
from game import constants

import arcade

class Trigger(arcade.Sprite):
    def __init__(self, position, parentMap, actionIndex=0):
        super().__init__(constants.dropsImage)
        
        self.center_x = position[0]
        self.center_y = position[1]

        self.parentMap = parentMap
        self.actionIndex = actionIndex

    def activate(self):
        self.parentMap.handleTrigger(self.actionIndex)
