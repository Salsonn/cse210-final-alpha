from game.point import Point
from game import constants

import arcade

class Drops(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.dropsImage)
        
        self.center_x = int(25)
        self.center_y = int(50)
