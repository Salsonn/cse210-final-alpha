from game.point import Point
from game.math import *
import arcade
from game import constants

class Weapon(arcade.Sprite):

    '''
    A class that allows the weapon to follow the mouse cursor
    '''

    # NOTE FOR LATER
    # CHECK SPECIFIC WEAPON AND DETERMINE THE SPRITE LOCATION ON THE SPRITE SHEET

    def __init__(self, check_flip, position):
        super().__init__(constants.weaponImage, center_x = 0, center_y = 0, flipped_horizontally=True, flipped_vertically=check_flip)
        self.center_x = position[0]
        self.center_y = position[1]
        self.angle = 0

        # image, scale, image_x, image_y, image_width, image_height, center_x,center_y

    def flip(self):
        if self.cartesian == 1:
            vertical_flip = False
        elif self.cartesian == 2:
            vertical_flip = True
        elif self.cartesian == 3:
            vertical_flip = True
        else:
            vertical_flip = False

        return vertical_flip

    # WEAPON PICKUP NOT IMPLEMENTED UNTIL FURTHER NOTICE

    # def weapon_pickup(self, fallen_weapon_x, fallen_weapon_y, player_x, player_y):
    #     '''
    #     Runs when the user picks up a dropped weapon.

    #     It then switches their weapon out for the picked up weapon
    #     '''
    #     distance_x = abs(player_x - fallen_weapon_x)
        
    #     distance_y = abs(player_y - fallen_weapon_y)
        
    #     if distance_x <= 5 and distance_y <= 5:
            
    #         # If returned True, then the weapon is within 
    #         # reasonable range to be picked up
    #         return True

    #     # If returned false, the weapon is too far away to be picked up
    #     return False
    
    def update_weapon_angle(self, playerX, playerY, mouseX, mouseY):
        '''
        Checks the current coordinates of the player and moves the weapon to
        stay in its standard position so that it's not stationary

        > Moves according to Character Position <
        '''
        if mouseY < playerY:
            if mouseX < playerX:
                self.cartesian = 3
            else:
                self.cartesian = 4
        elif mouseY > playerY:
            if mouseX > playerX:
                self.cartesian = 1
            else:
                self.cartesian = 2

        finalX = abs(playerX - mouseX)
        finalY = abs(playerY - mouseY)
        h = hypotenuse(finalX, finalY)
        av = angle(h, finalY)

        if self.cartesian == 1:
            self.angle = av * 100

        elif self.cartesian == 2:
            self.angle = 180 - (av * 100)

        elif self.cartesian == 3:
            self.angle = 180 + (av * 100)

        elif self.cartesian == 4:
            self.angle = 360 - (av * 100)

        return self.angle

        