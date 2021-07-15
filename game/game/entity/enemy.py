from game.math import *
import arcade
from game import constants
from game.entity.player import Player

class Enemy(arcade.Sprite):
    def __init__(self, position, enemy, speed):
        super().__init__(enemy, center_x=position[0], center_y=position[1])
        self.player = Player((640, 360), False)
        self._center_x = position[0]
        self._center_y = position[1]
        self.speed = speed