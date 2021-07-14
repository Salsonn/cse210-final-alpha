import arcade
from game import constants
from game.entity.player import Player

class Enemy(arcade.Sprite):
    def __init__(self, position):
        super().__init__(constants.enemyImage, center_x=position[0], center_y=position[1])
        self.player = Player((640, 360), False)
        self.center_x = position[0]
        self.center_y = position[1]

    def move_enemy(self, entities, position_player, position_enemy):
        eX, eY = position_enemy[0], position_enemy[1]
        pX, pY = position_player[0], position_player[1]

        speed = 4

        if eX != pX:
            if eX < pX:
                entities["enemy"][0].center_x += speed
            else:
                entities["enemy"][0].center_x -= speed
        if eY != pY:
            if eY < pY:
                entities["enemy"][0].center_y += speed
            else:
                entities["enemy"][0].center_y -= speed