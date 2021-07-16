import arcade

from game import constants

class Welcome():

    def __init__(self, levelController, entities):
        self._collidableWalls = entities["wall"]
        self._levelController = levelController

        self._BACKGROUND_COLOR = arcade.color.BLACK
        self._FLOOR = '../images/floor_tile_sprite.png'
        self._FLOOR_W = 32
        self._FLOOR_H = 32
        self._WALL = '../images/wall_tile_sprite.png'
        self._WALL_W = 32
        self._WALL_H = 32
        self._FONT_COLOR = arcade.color.PALE_BLUE
        self._WALL_COLOR = arcade.color.RED
        self._WALL_COLOR_2 = arcade.color.CYBER_YELLOW
        self._LEFT_WALL_X = 0
        self._LEFT_WALL_Y = constants.windowY / 2
        self._TITLE = 'WELCOME TO THE GAME'
        self._RADIUS = 150
        #SOUND = arcadeload_sound('/sounds/Tada-soundmp3')
        self._INFO = 'CHOOSE WHAT TO DO'
        self._TEMP = arcade.color.GREEN
        self._COLUMN_SPACING = 20
        self._ROW_SPACING = 20
        self._LEFT_MARGIN = 110
        self._BOTTOM_MARGIN = 110

    def load(self):
        self._collidableWalls.clear()
    
    def drawMap(self):
        # Draw the Edges
        arcade.draw_rectangle_filled(self._LEFT_WALL_X, self._LEFT_WALL_Y, 20, constants.windowY, self._WALL_COLOR)
        arcade.draw_rectangle_filled(constants.windowX, self._LEFT_WALL_Y, 20, constants.windowY, self._WALL_COLOR)
        arcade.draw_rectangle_filled(constants.windowX / 2, constants.windowY, constants.windowX, 20, self._WALL_COLOR)
        arcade.draw_rectangle_filled(constants.windowX / 2, 0, constants.windowX, 20, self._WALL_COLOR)

        # Welcome Message
        arcade.draw_text('WELCOME', constants.windowX / 2, constants.windowY / 2, self._FONT_COLOR, 50, 300, 'center', 'calibri', True)

    def handleTrigger(self, actionIndex):
        pass