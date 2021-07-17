import arcade

from game import constants


class Welcome():

    def __init__(self, levelController, entities):
        self._triggers = entities["trigger"]
        self._collidableWalls = entities["wall"]
        self._levelController = levelController
        self.font_size = 40
        self.startBtn_adjust = 350
        self._LOGO = 'game\\images\\dinoSplash.png'

    def load(self):
        self._triggers.clear()
        self._collidableWalls.clear()
        # self._LOGO = './images/dinoSplash.png'
        # self.font_size = 40

    def drawMap(self, reticle, check_font = None):
               
        '''WORK ON THIS BIT LATER
           CHANGES FONT SIZE WHEN HOVERING OVER THE START BUTTON'''

        if (260 <= reticle.get_reticleX() <= 420) and (360 <= reticle.get_reticleY() <= 400):
            self.startHover = True
            self.font_size = 50
            self.startBtn_adjust = -5


        elif (((reticle.get_reticleX() < 260) or (420 < reticle.get_reticleX())) or ((reticle.get_reticleY() < 360) or (400 < reticle.get_reticleY()))):
            self.startHover = False
            self.font_size = 40
            self.startBtn_adjust = 0

        
        # Welcome Message
        if check_font == None:
            splash = arcade.Sprite(self._LOGO, 1.25)
            splash.center_x = constants.windowX // 2
            splash.center_y = constants.windowY // 2
            splash.draw()
        self.textDraw()
        
    def textDraw(self):
        arcade.draw_text('START', 240, 350 + self.startBtn_adjust, arcade.color.CADMIUM_ORANGE, self.font_size, 200, 'center', 'helvetica', True)
