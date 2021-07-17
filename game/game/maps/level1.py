import arcade

from game import constants

from game.entity.trigger import Trigger

class Level1():

    def __init__(self, levelController, entities):
        self._levelController = levelController
        self._collidableWalls = entities["wall"]
        self._triggers = entities["trigger"]

        self._BACKGROUND_COLOR = arcade.color.BLACK
        self._FONT_COLOR = arcade.color.PALE_BLUE
        
        self._INFO = 'CHOOSE WHAT TO DO'

        # self._FLOOR = '.\images\catacombs\cata_v1.0\mainlevbuild.png'
        self._FLOOR = 'game\\images\\catacombs\\cata_v1.0\\mainlevbuild.png'
        self._FLOOR_W = 32
        self._FLOOR_H = 48
        
        # self._WALL = '.\images\catacombs\cata_v1.0\mainlevbuild.png'
        self._WALL = 'game\\images\\catacombs\\cata_v1.0\\mainlevbuild.png'
        self._WALL_W = 32
        self._WALL_H = 32
        self._LEFT_WALL_X = 0
        self._LEFT_WALL_Y = constants.windowY / 2

        # self._POT = '.\images\TX_Props.png'
        self._POT = 'game\\images\\TX_Props.png'
        self._POT_W = 24
        self._POT_H = 36
        
        self._COLUMN_SPACING = 20
        self._ROW_SPACING = 20
        self._LEFT_MARGIN = 110
        self._BOTTOM_MARGIN = 110
        self._TILE_SPACING = 1.6

    def load(self):
        self._triggers.clear()
        self._collidableWalls.clear()
        self.prepare_walls()
        self.prepare_floor()

    def drawMap(self):
        self.wall_list_v.draw()
        self.wall_list_h.draw()
        self.draw_messages()
        self.floor_list.draw()



    def prepare_walls(self):
        # Draw Walls to choose what to do next
        self.wall_list_h = arcade.SpriteList()
        # Top left wall
        for i in range(constants.windowY // self._WALL_H - 4):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1,736.0,320.0,self._WALL_W, self._WALL_H)

            # Position the floor sprites
            wall.center_x = i * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 140
            wall.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 400

            # Add the floor to the lists
            self.wall_list_h.append(wall)

        # Top right wall
        for l in range(constants.windowY // self._WALL_H - 4):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1,736.0,320.0,self._WALL_W, self._WALL_H)

            # Position the floor sprites
            wall.center_x = l * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) + 520
            wall.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 400

            # Add the floor to the lists
            self.wall_list_h.append(wall)

        # Draw Walls to choose what to do next
        self.wall_list_v = arcade.SpriteList()

        # Right Vertical Wall
        for j in range(constants.windowY // self._WALL_H - 4):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1,736.0,320.0,self._WALL_W, self._WALL_H)

            # Position the floor sprites
            wall.center_x = (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) + 1032
            wall.center_y = j * (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) - 140

            # Add the floor to the lists
            self.wall_list_v.append(wall)

        # Left Vertical Wall
        for k in range(constants.windowY // self._WALL_H - 4):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1,736.0,320.0,self._WALL_W, self._WALL_H)

            # Position the floor sprites
            wall.center_x = (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 172
            wall.center_y = k * (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) - 140

            # Add the floor to the lists
            self.wall_list_v.append(wall)

        # Bottom Wall
        for m in range(constants.windowX // self._WALL_H - 3):

            # Create sprite
            wall = arcade.Sprite(self._WALL, 1,736.0,320.0,self._WALL_W, self._WALL_H)

            # Position position sprite
            wall.center_x = m * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 110
            wall.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) - 172

            # Add sprite to necessary lists
            self.wall_list_h.append(wall)

        for wall in self.wall_list_h:
            self._collidableWalls.append(wall)
        for wall in self.wall_list_v:
            self._collidableWalls.append(wall)    

    def prepare_floor(self):
        self.floor_list = arcade.SpriteList()
        for i in range(constants.windowY // self._FLOOR_H + 1):
            for j in range(constants.windowX // self._FLOOR_W + 16):

                # Create the floor instance
                floor = arcade.Sprite(self._WALL, 1,928.0,208.0,self._FLOOR_W, self._FLOOR_H)

                # Position the floor sprites
                floor.center_x = j * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 92
                floor.center_y = i * (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) - 101

                # Add the floor to the lists
                self.floor_list.append(floor)

    def draw_messages(self):
        
        # Welcome Message
        arcade.draw_text(self._INFO, constants.windowX / len(self._TITLE) + 100, constants.windowY - 40, self._FONT_COLOR, 25, 340, 'center', 'calibri', True)

        # Level Message
        arcade.draw_text('Level 1', 470, constants.windowY - 40, self._FONT_COLOR, 20, 340, 'center', 'calibri', True)
        
        # Instruction message
        arcade.draw_text('Instructions', constants.windowX - 470, constants.windowY - 40, self._FONT_COLOR, 20, 340, 'center', 'calibri', True)


    def handleTrigger(self, actionIndex):
        if actionIndex == 1:
            self._levelController.changeLevel(1)
