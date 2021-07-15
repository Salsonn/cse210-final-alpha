import arcade
import time
from game import constants
from game.point import Point
from game.math import *
from game.entity.weapon import Weapon
from game.entity.player import Player
from game.entity.enemy import Enemy

class Director(arcade.Window):
    def __init__(self, entities, tasks, input_service, reticle):
        super().__init__(constants.windowX, constants.windowY, "Dino Destroyer")
        self._script = tasks
        self._entities = entities
        self._input_service = input_service
        self._reticle = reticle
        self._actionTime = {}
        self.enemy = Enemy((150, 450), constants.enemyImages[0], 4)
        self.music = None

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.play_song()

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
        if constants.debug:
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
        startTime = time.time()
        if len(self._actionTime) >= 4:
            self._actionTime = {}
        for action in self._script[tag]:
            action.execute(self._entities, self._reticle)
            self._actionTime[tag] = f"Completed {tag} in {round((time.time() - startTime) * 1000, 2)} ms"
        if len(self._actionTime) >= 3 and constants.debug == True:
            print("\n\n\n")
            for action in self._actionTime:
                print(f"{self._actionTime[action]}")

    def play_song(self):
        if self.music:
            self.music.stop()

        # Play the next song
        self.music = arcade.Sound(constants.menuMusic, streaming=True)
        self.current_player = self.music.play(1)
        # This is a quick delay. If we don't do this, our elapsed time is 0.0
        # and on_update will think the music is over and advance us to the next
        # song before starting this one.
        time.sleep(0.03)