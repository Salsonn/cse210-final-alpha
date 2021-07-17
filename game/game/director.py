import arcade
import time
import subprocess

from game import constants
from game.point import Point
from game.math import *
from game.maps.welcome import Welcome

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
        self.welcome = Welcome(self, entities)
        self.enemy = Enemy((150, 450), constants.enemyImages[0], 4, 50, 5, True)
        self.menuMusic = None
        self.startHover = False

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.music_list = [constants.menuMusic, constants.levelMusic]
        self.current_song_index = 0
        self.play_song()

    def on_update(self, delta_time):
        self.current_level = constants.currentLevel
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
        
        if (260 <= mouseX <= 420) and (360 <= mouseY <= 400) and constants.currentLevel == -1:
            # CHANGES LEVEL FROM -1 TO 0
            self._script["output"][0].changeLevel(0)
    
    def on_mouse_release(self, mouseX, mouseY, button, modifiers):
        self._input_service.remove_mousebtn(button, modifiers)

    def on_mouse_motion(self, mouseX, mouseY, mouse_dx, mouse_dy):
        self._reticle.set_reticle(Point(mouseX, mouseY), mouse_dx, mouse_dy)
       
        '''WORK ON THIS BIT LATER
           CHANGES FONT SIZE WHEN HOVERING OVER THE START BUTTON'''

        if (260 <= mouseX <= 420) and (360 <= mouseY <= 400) and not self.startHover:
            self.startHover = True
            self.welcome.font_size += 10
            self.welcome.redrawMap()

        elif self.startHover and (((mouseX < 260) or (420 < mouseX)) or ((mouseY < 360) or (400 < mouseY))):
            self.startHover = False
            self.welcome.font_size -= 10
            self.welcome.redrawMap()
        
    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        startTime = time.time()
        if len(self._actionTime) >= 4:
            self._actionTime = {}
        for action in self._script[tag]:
            action.execute(self._entities, self._reticle, self.current_level)
            self._actionTime[tag] = f"Completed {tag} in {round((time.time() - startTime) * 1000, 2)} ms"
        if len(self._actionTime) >= 3 and constants.debug == True:
            print("\n\n\n")
            for action in self._actionTime:
                print(f"{self._actionTime[action]}")

    def play_song(self):
        # subprocess.call(f'.\game\sounds\sounder.exe {constants.menuMusic}', shell=True)
        # return
        if self.menuMusic:
            self.menuMusic.stop()

        self.menuMusic = arcade.Sound(constants.menuMusic, streaming=True)
        if not constants.mute: self.current_player = self.menuMusic.play(1)
        time.sleep(0.03)