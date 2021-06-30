from game.point import Point
from game import constants

import arcade

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.playerImage)

        self.center_x = int(constants.windowX / 2)
        self.center_y = int(constants.windowY / 2)
