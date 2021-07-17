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
        super().__init__(constants.weaponImagePath, center_x = 0, center_y = 0, flipped_horizontally=True, flipped_vertically=check_flip, scale = 1.25)
        self.center_x = position[0]
        self.center_y = position[1]
        self.angle = 0

        # image, scale, image_x, image_y, image_width, image_height, center_x,center_y

    def flip(self):
        if self.cartesian in {2, 3}: return True
        else: return False

    
    def flipH(self, flipped):
        self.texture = constants.weaponImage[flipped]

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
        self.cartesian = cartesian(mouseX, mouseY, playerX, playerY)

        finalX = abs(playerX - mouseX)
        finalY = abs(playerY - mouseY)
        h = hypotenuse(finalX, finalY)
        av = angle(h, finalY)
        self.angle = direction(self.cartesian, av)
        
        return self.angle

        