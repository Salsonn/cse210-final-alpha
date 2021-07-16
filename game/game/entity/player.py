from game.point import Point
from game import constants

import arcade

class Player(arcade.Sprite):
    def __init__(self, position, check_flip=None):
        super().__init__(constants.playerImage, flipped_horizontally=check_flip, center_x=position[0], center_y=position[1], scale = 1.25)

        self.center_x = position[0]
        self.center_y = position[1]
        self.__score = constants.playerScore
        self.__health = constants.playerHealth

    def changeScore(self, delta):
        self.__score += delta
        constants.playerScore = self.__score

    def getScore(self):
        return self.__score

    def loseHealth(self, damage):
        self.__health -= damage
        constants.playerHealth = self.__health
        if self.__health <= 0:
            # This is where the game will stop running and the end screen will display with their final score.
            print(f'YOU DIED, YOUR FINAL SCORE WAS {self.__score}')