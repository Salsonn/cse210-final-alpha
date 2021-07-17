import arcade

from game import constants


class Welcome():

    def __init__(self, levelController, entities):
        self._triggers = entities["trigger"]
        self._collidableWalls = entities["wall"]
        self._levelController = levelController
        self.font_size = 40
        self._LOGO = 'game\\images\\dinoSplash.png'

    def load(self):
        self._triggers.clear()
        self._collidableWalls.clear()
        # self._LOGO = './images/dinoSplash.png'
        # self.font_size = 40

    def drawMap(self, check_font = None):
        # Welcome Message
        if check_font == None:
            splash = arcade.Sprite(self._LOGO , 1)
            splash.center_x = constants.windowX // 2
            splash.center_y = constants.windowY // 2
            splash.draw()
        
        arcade.draw_text('START', 240, 350, arcade.color.CADMIUM_ORANGE, self.font_size, 200, 'center', 'helvetica', True)
