from game import constants
from game.entity.entity import Entity
import arcade

class Player(Entity):
    def __init__(self):
        super().__init__(constants.playerImage, constants.windowX / 2, constants.windowY / 2, 50, 50, True)

        self.center_x = int(constants.windowX / 2)
        self.center_y = int(constants.windowY / 2)