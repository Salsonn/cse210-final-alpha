import arcade

from game import constants

class Level1():

    def __init__(self, levelController, entities):
        self._triggers = entities["trigger"]
        self._collidableWalls = entities["wall"]
        self._levelController = levelController

        self._BACKGROUND_COLOR = arcade.color.BLACK
        self._FLOOR = 'game\images\catacombs\cata_v1.0\mainlevbuild.png'
        self._FLOOR_W = 32
        self._FLOOR_H = 32
        # self._WALL = './images/wall_tile_sprite.png'
        self._WALL = 'game\images\catacombs\cata_v1.0\mainlevbuild.png'
        self._WALL_W = 32
        self._WALL_H = 32
        self._FONT_COLOR = arcade.color.PALE_BLUE
        self._WALL_COLOR = arcade.color.RED
        self._WALL_COLOR_2 = arcade.color.CYBER_YELLOW
        self._LEFT_WALL_X = 0
        self._LEFT_WALL_Y = constants.windowY / 2
        self._TITLE = 'WELCOME TO THE GAME'
        self._LEVEL1 = 'LEVEL 1'
        self._RADIUS = 150
        #SOUND = arcadeload_sound('/sounds/Tada-soundmp3')
        self._INFO = 'CHOOSE WHAT TO DO'
        self._TEMP = arcade.color.GREEN
        self._COLUMN_SPACING = 20
        self._ROW_SPACING = 20
        self._LEFT_MARGIN = 110
        self._BOTTOM_MARGIN = 110
        self._TILE_SPACING = 1.6

    def load(self):
        self._triggers.clear()
        self._collidableWalls.clear()
        self.prepare_floor()

    def draw_edges(self):
        # Draw the Edges
        arcade.draw_rectangle_filled(self._LEFT_WALL_X, self._LEFT_WALL_Y, 20, constants.windowY, self._WALL_COLOR_2)
        arcade.draw_rectangle_filled(constants.windowX, self._LEFT_WALL_Y, 20, constants.windowY, self._WALL_COLOR_2)
        arcade.draw_rectangle_filled(constants.windowX / 2, constants.windowY, constants.windowX, 20, self._WALL_COLOR_2)
        arcade.draw_rectangle_filled(constants.windowX / 2, 0, constants.windowX, 20, self._WALL_COLOR_2)

    def draw_messages(self):
        self._health = 100
        self._weapons = ['knife', 'sword', 'pistol', 'laser']

        # Welcome Message
        arcade.draw_text(self._LEVEL1, constants.windowX / len(self._LEVEL1) + 250, constants.windowY - 40, self._FONT_COLOR, 25, 340, 'center', 'calibri', True)

        # Health
        arcade.draw_text(f'HEALTH:{self._health}', 15, 15, self._FONT_COLOR, 25, 200, 'left', 'calibri', True)

        # Weapons
        arcade.draw_text(f'WEAPON:{self._weapons[3]}', constants.windowX - 215, 15, self._FONT_COLOR, 25, 200, 'left', 'calibri', True)

    def prepare_floor(self):
        self.floor_list = arcade.SpriteList()
        for i in range(constants.windowY // self._FLOOR_H - 5):
            for j in range(constants.windowX // self._FLOOR_W -1):

                # Create the floor instance
                floor = arcade.Sprite(self._WALL, 1,384.0,400.0,self._FLOOR_W, self._FLOOR_H)

                # Position the floor sprites
                floor.center_x = j * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 145
                floor.center_y = i * (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) - 73

                # Add the floor to the lists
                self.floor_list.append(floor)

        # self.floor_list = arcade.SpriteList()
        # # Create the floor instance
        # floor = arcade.Sprite(self._FLOOR, 1)


        # # Position the floor sprites

        # # for i, j in range((constants.windowX // self._FLOOR_H - 1),(constants.windowY // self._FLOOR_H - 1)):
        # for i in range(constants.windowX // self._FLOOR_H - 1):
            
        #     # Position the floor sprites
        #     floor.center_x = i * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 145
        #     floor.center_y = (self._ROW_SPACING) + (self._BOTTOM_MARGIN)

        # # Add the floor to the lists
        #     self.floor_list.append(floor)
        #     # self.floor_list[i].draw()
        #     self.floor_list.draw()

        # for j in range(constants.windowY // self._FLOOR_H - 8):
            
        #     # Position the floor sprites
        #     floor.center_x = (self._COLUMN_SPACING) + (self._LEFT_MARGIN) - 100
        #     floor.center_y = j*  (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) - 15
            
        #     self.floor_list.append(floor)
        #     self.floor_list.draw()
    def draw_floor(self):
        self.floor_list.draw()

    def drawMap(self):
        Level1.draw_edges(self)
        Level1.draw_messages(self)
        Level1.draw_floor(self)

    def handleTrigger(self, actionIndex):
        pass