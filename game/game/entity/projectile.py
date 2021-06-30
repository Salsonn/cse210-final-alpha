from game.point import Point
from game import constants

import arcade

class Projectile(arcade.Sprite):
    def __init__(self, startingX, startingY, dX, dY):
        super().__init__(constants.projectile1Image)

        self.center_x = startingX
        self.center_y = startingY
        self.change_x = dX
        self.change_y = dY