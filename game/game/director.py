import arcade
from game import constants

class Director(arcade.Window):
    def __init__(self, entities, tasks, input_service):
        super().__init__(constants.windowX, constants.windowY, "Name this Game")
        self._script = tasks
        self._entities = entities
        self._input_service = input_service

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_update(self, delta_time):
        self._cue_action("update")

    def on_draw(self):
        self._cue_action("output")

    def on_key_press(self, symbol, modifiers):
        self._input_service.set_key(symbol, modifiers)
        self._cue_action("input")

    def on_key_release(self, symbol, modifiers):
        self._input_service.remove_key(symbol, modifiers)
        self._cue_action("input")

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._entities)