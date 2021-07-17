from game.point import Point
from game import constants
from game.entity.player import Player

import arcade

class Drops(arcade.Sprite):
    def __init__(self, position):
        super().__init__(constants.dropsImage)
        
        self.center_x = position[0]
        self.center_y = position[1]

    def heal(self, heal, drops, player):
        player.changeScore(100)
        drops.remove(self)