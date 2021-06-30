import arcade
from game import constants
from game.point import Point
from game.math import *

class Director(arcade.Window):
    def __init__(self, entities, tasks, input_service, reticle):
        super().__init__(constants.windowX, constants.windowY, "Name this Game")
        self._script = tasks
        self._entities = entities
        self._input_service = input_service
        self._reticle = reticle

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_update(self, delta_time):
        self._cue_action("update")
        self._cue_action("input")

    def on_draw(self):
        self._cue_action("output")

    def on_key_press(self, symbol, modifiers):
        self._input_service.set_key(symbol, modifiers)
        #self._cue_action("input")

    def on_key_release(self, symbol, modifiers):
        self._input_service.remove_key(symbol, modifiers)
        #self._cue_action("input")

    def on_mouse_press(self, mouseX, mouseY, button, modifiers):
        self._input_service.add_mousebtn(button, modifiers)
        print(f"Click detected at {mouseX}, {mouseY}")
    
    def on_mouse_release(self, mouseX, mouseY, button, modifiers):
        self._input_service.remove_mousebtn(button, modifiers)

    def on_mouse_motion(self, mouseX, mouseY, mouse_dx, mouse_dy):
        self._reticle.set_reticle(Point(mouseX, mouseY), mouse_dx, mouse_dy)

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._entities, self._reticle)