import arcade

from game import constants


class Welcome():

    def __init__(self):
        self._LOGO = './images/dinoSplash.png'
        self.font_size = 40
    
    def drawMap(self):
        # Welcome Message
        splash = arcade.Sprite(self._LOGO , 1)
        splash.center_x = constants.windowX // 2
        splash.center_y = constants.windowY // 2
        splash.draw()

        
        arcade.draw_text('START', 240, 350, arcade.color.CADMIUM_ORANGE, self.font_size, 200, 'center', 'helvetica', True)
