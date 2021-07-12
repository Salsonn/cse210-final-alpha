import arcade
from game import constants
from game.entity.player import Player

class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.enemyImage)

        self.player = Player((640, 360), False)
        self.center_x = 150
        self.center_y = 450

    def move_enemy(self):
        
        if abs(self.center_x - self.player.center_x) < 10:
            self.center_x += 1
            if self.center_x < self.player.center_x:
                self.center_x += 1
            else:
                self.center_x -= 1

        if abs(self.center_y - self.player.center_y) < 10:
            if self.center_y < self.player.center_y:
                self.center_y += 1
            else:
                self.center_y -= 1
        
        

