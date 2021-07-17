from game.point import Point
from game import constants
from game.entity.player import Player

import arcade

class Drop(arcade.Sprite):
    def __init__(self, position):
        super().__init__(constants.dropsImage)
        
        self.center_x = position[0]
        self.center_y = position[1]

    def interact(self, drops, player):
        player.heal()
        drops.remove(self)