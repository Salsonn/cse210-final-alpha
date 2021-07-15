from game.point import Point
from game import constants

import arcade

class Drops(arcade.Sprite):
    def __init__(self, position):
        super().__init__(constants.dropsImage)
        
        self.center_x = position[0]
        self.center_y = position[1]