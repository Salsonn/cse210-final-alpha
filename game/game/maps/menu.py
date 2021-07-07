import arcade
from arcade import sprite_list

from game import constants

class MainMenu():

    def __init__(self, entities):
        self._collidableWalls = entities["wall"]
        self._BACKGROUND_COLOR = arcade.color.BLACK
        self._FLOOR = './images/floor_tile_sprite.png'
        self._FLOOR_W = 32
        self._FLOOR_H = 32
        self._WALL = './images/wall_tile_sprite.png'
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

    def drawMap(self):
        
        # Draw the Walls
        arcade.draw_rectangle_filled(self._LEFT_WALL_X, self._LEFT_WALL_Y, 20, constants.windowY, self._WALL_COLOR)
        arcade.draw_rectangle_filled(constants.windowX, self._LEFT_WALL_Y, 20, constants.windowY, self._WALL_COLOR)
        arcade.draw_rectangle_filled(constants.windowX / 2, constants.windowY, constants.windowX, 20, self._WALL_COLOR)
        arcade.draw_rectangle_filled(constants.windowX / 2, 0, constants.windowX, 20, self._WALL_COLOR)

        # Welcome Message
        arcade.draw_text(self._INFO, constants.windowX / len(self._TITLE) + 100, constants.windowY - 40, self._FONT_COLOR, 25, 340, 'center', 'calibri', True)

        # Draw Walls to choose what to do next
        self.wall_list_h = arcade.SpriteList()

        for i in range(constants.windowY // self._WALL_H - 8):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1)

            # Position the floor sprites
            wall.center_x = i * self._COLUMN_SPACING + self._LEFT_MARGIN
            wall.center_y = self._ROW_SPACING + self._BOTTOM_MARGIN + 400

            # Add the floor to the lists
            self.wall_list_h.append(wall)
        self.wall_list_h.draw()
        for wall in self.wall_list_h:
            self._collidableWalls.append(wall)

        arcade.draw_text('Level 1', wall.center_x, constants.windowY - 150, self._FONT_COLOR, 20, 340, 'center', 'calibri', True)

             # Draw Walls to choose what to do next
        self.wall_list_v = arcade.SpriteList()

        for j in range(constants.windowY // self._WALL_H - 8):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1)

            # Position the floor sprites
            wall.center_x = self._COLUMN_SPACING + self._LEFT_MARGIN + 1000
            wall.center_y = j * self._ROW_SPACING + self._BOTTOM_MARGIN 

            # Add the floor to the lists
            self.wall_list_v.append(wall)
        self.wall_list_v.draw()

        
        arcade.draw_text('Instructions', constants.windowX -300, constants.windowY - 250, self._FONT_COLOR, 20, 340, 'center', 'calibri', True)