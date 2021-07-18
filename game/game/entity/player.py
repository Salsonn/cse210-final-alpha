from game.point import Point
from game import constants

import arcade

class Player(arcade.Sprite):
    def __init__(self, position, check_flip=None):
        super().__init__(constants.playerImagePath,  flipped_horizontally=check_flip, center_x=position[0], center_y=position[1], scale = 1.25)

        self.center_x = position[0]
        self.center_y = position[1]
        self.__score = constants.playerScore
        self.__health = constants.playerHealth

    def changeScore(self, delta):
        self.__score += delta

    def getScore(self):
        return self.__score

    def loseHealth(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            return True
        return False
            
    def heal(self):
        self.__health = 100

    def getHealth(self):
        return self.__health
    
    def flipH(self, flipped):
        self.texture = constants.playerImage[flipped]