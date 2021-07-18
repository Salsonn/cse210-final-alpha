import sys
from game.point import Point
from game.entity.player import Player
from game import constants

import arcade

class ArcadeInputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _keys (list): up, dn, lt, rt.
    """

    def __init__(self):
        """The class constructor."""
        self._keys = []
        self._mousebtn = []
        self.player = Player((640, 360), False)
        self.pressed = False
    
    def set_key(self, key, modifiers):
        #Ignoring modifies ar this point...
        self._keys.append(key)

    def remove_key(self, key, modifiers):
        self._keys.remove(key)

    def add_mousebtn(self, button, modifiers):
        self._mousebtn.append(button)

    def remove_mousebtn(self, button, modifiers):
        self._mousebtn.remove(button)

    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        x = 0
        y = 0

        if arcade.key.LEFT in self._keys or arcade.key.A in self._keys:
            x = -1
        elif arcade.key.RIGHT in self._keys or arcade.key.D in self._keys:
            x = 1
        if arcade.key.UP in self._keys or arcade.key.W in self._keys:
            y = 1
        elif arcade.key.DOWN in self._keys or arcade.key.S in self._keys:
            y = -1
        elif arcade.key.E in self._keys:
            


        velocity = Point(x, y)
        return velocity
            
    def check_click(self):
        return arcade.MOUSE_BUTTON_LEFT in self._mousebtn