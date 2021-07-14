from game.math import *
import arcade
from game import constants
from game.entity.player import Player

class Enemy(arcade.Sprite):
    def __init__(self, position):
        super().__init__(random.choice(constants.enemyImages), center_x=position[0], center_y=position[1])
        self.player = Player((640, 360), False)
        self.center_x = position[0]
        self.center_y = position[1]
        self._check_pos = 0
        self._speed = 3

    def move_enemy(self, position_player, position_enemy):
        eX, eY = position_enemy[0], position_enemy[1]
        pX, pY = position_player[0], position_player[1]

        h = hypotenuse(abs(eX - pX), abs(eY - pY))
        a = angle(h, (abs(eY - pY)))
        coordinate_plane = cartesian(eX, eY, pX, pY)
        direc = direction(coordinate_plane, a)

        # Testing Enemy Location

        if coordinate_plane == 1 and self._check_pos != 1:
            self._check_pos = 1
            print(f"{h, a, coordinate_plane, direc}")
        elif coordinate_plane == 2 and self._check_pos != 2:
            self._check_pos = 2
            print(f"{h, a, coordinate_plane, direc}")
        elif coordinate_plane == 3 and self._check_pos != 3:
            self._check_pos = 3
            print(f"{h, a, coordinate_plane, direc}")
        elif coordinate_plane == 4 and self._check_pos != 4:
            self._check_pos = 4
            print(f"{h, a, coordinate_plane, direc}")
        else:
            pass

        if eX != pX:
            if eX <= pX:
                self.change_x += self._speed
            else:
                self.change_x -= self._speed
        if eY != pY:
            if eY <= pY:
                self.change_y += self._speed
            else:
                self.change_y -= self._speed