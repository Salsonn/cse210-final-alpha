class Weapon():

    '''
    A class that allows the weapon to follow the mouse cursor
    '''

    def __init__(self):
        self.weapon_sprite = './wall_tile_sprite.png'
    
    def draw_weapon(self):
        '''
        Draws the weapon for every frame that the game us running
        so that the weapon's angle is matching the cursor's position
        '''

        pass
    
    def attack_weapon(self, weapon):
        '''
        Definition runs when the user clicks with the mouse

        It then checks the weapon that the user is currently holding
        and attacks with the given weapon attack
        '''

        pass

    def weapon_pickup(self, weapon):
        '''
        Runs when the user picks up a dropped weapon.

        It then switches their weapon out for the picked up weapon
        '''

        pass
    
    def update_weapon_pos(self, x_pos_player, y_pos_player):
        '''
        Checks the current coordinates of the player and moves the weapon to
        stay in its standard position so that it's not stationary

        > Moves according to Character Position <
        '''

        pass