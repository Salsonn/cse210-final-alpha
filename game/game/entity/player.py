from game.point import Point
from game import constants

import arcade

class Player(arcade.Sprite):
    def __init__(self, position, check_flip=None):
        super().__init__(constants.playerImage, flipped_horizontally=check_flip, center_x=position[0], center_y=position[1])

        self.center_x = position[0]
        self.center_y = position[1]
        self.__score = 0

    def changeScore(self, delta):
        self.__score += delta

    def getScore(self):
        return self.__score
