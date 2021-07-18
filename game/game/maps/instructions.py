from game.maps.level1 import Level1
from game.entity.trigger import Trigger
import arcade
from game import constants

class Instructions:

    def __init__(self, levelController, entities):
        
        self._triggers = entities["trigger"]
        self._collidableWalls = entities["wall"]
        self._levelController = levelController

        self._BACKGROUND_COLOR = arcade.color.BLACK
        self._FONT_COLOR = arcade.color.PALE_BLUE

        self._TITLE = 'Instructions'
        self._LINE1 = 'USE THE WASD OR ARROW KEYS TO MOVE'
        self._LINE2 = 'CLICK AND HOLD TO SHOOT THE ENEMIES'
        self._LINE3 = 'TRY NOT TO DIE!'
        self._LINE4 = 'GOODLUCK!'

        self._MAIN = 'MAIN MENU'
        self._LEVEL1 = 'Dungeon'

        # self._ARCH = './images/catacombs/cata_v1.0/mainlevbuild.png'
        self._ARCH = 'game\images\catacombs\cata_v1.0\mainlevbuild.png'
        self._COLUMN_SPACING = 20
        self._ROW_SPACING = 20
        self._LEFT_MARGIN = 110
        self._BOTTOM_MARGIN = 110
        self._TILE_SPACING = 1.6

    def load(self):
        self._triggers.clear()
        self._collidableWalls.clear()
        # self.prepare_floor()

    def drawMap(self):
        Instructions.draw_instructions(self)
        Instructions.draw_doors(self)
        Instructions.draw_messages(self)
    
    def draw_instructions(self):
        arcade.draw_text(self._TITLE, constants.windowX / len(self._TITLE) + 350, constants.windowY - 40, self._FONT_COLOR, 25, 340, 'center', 'calibri', True)
        arcade.draw_text(self._LINE1, constants.windowX / len(self._LINE1) + 350, constants.windowY - 120, self._FONT_COLOR, 25, 560, 'center', 'calibri', True)
        arcade.draw_text(self._LINE2, constants.windowX / len(self._LINE2) + 350, constants.windowY - 160, self._FONT_COLOR, 25, 560, 'center', 'calibri', True)
        arcade.draw_text(self._LINE3, constants.windowX / len(self._LINE3) + 350, constants.windowY - 200, self._FONT_COLOR, 25, 400, 'center', 'calibri', True)
        arcade.draw_text(self._LINE4, constants.windowX / len(self._LINE4) + 300, constants.windowY - 240, self._FONT_COLOR, 25, 400, 'center', 'calibri', True)

    def draw_doors(self):

        # Draw Arch for Level 1
        level1arch = arcade.Sprite(self._ARCH, 1, 398.0, 14.0,84,93)
        level1arch.center_x = 4 * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 80
        level1arch.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 405
        level1arch.draw()
        menuArch = arcade.Sprite(self._ARCH, 1, 398.0, 14.0,84,93)
        menuArch.center_x = 31 * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 84
        menuArch.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 405
        menuArch.draw()

        # Draw Arch for Main MENU
        level1Loader = Trigger(level1arch.center_x, level1arch.center_y + 20, 80, 76, self, 1)
        self._triggers.append(level1Loader)

        menuLoader = Trigger(menuArch.center_x, menuArch.center_y + 20, 80, 76, self, 2)
        self._triggers.append(menuLoader)

    def draw_messages(self):
        # Draw Level 1  text for Arch
        arcade.draw_text(self._LEVEL1, 55, constants.windowY - 60, self._FONT_COLOR, 20, 340, 'center', 'calibri', True)
        
        # Draw Main Menu  text for Arch
        arcade.draw_text(self._MAIN, constants.windowX - 370, constants.windowY - 60, self._FONT_COLOR, 20, 340, 'center', 'calibri', True)
        
    def handleTrigger(self, actionIndex):
        if actionIndex == 1:
            self._levelController.changeLevel(1)
        elif actionIndex == 2:
            self._levelController.changeLevel(0)