import arcade

from game import constants

class Level1():

    def __init__(self):
        self._BACKGROUND_COLOR = arcade.color.BLACK
        self._FONT_COLOR = arcade.color.PALE_BLUE
        
        self._TITLE = 'LEVEL 1'
        self._INFO = 'CHOOSE WHAT TO DO'

        self._FLOOR = './images/catacombs/cata_v1.0/mainlevbuild.png'
        self._FLOOR_W = 32
        self._FLOOR_H = 48
        
        self._WALL = './images/catacombs/cata_v1.0/mainlevbuild.png'
        self._WALL_W = 32
        self._WALL_H = 32
        self._LEFT_WALL_X = 0
        self._LEFT_WALL_Y = constants.windowY / 2

        self._COLUMN_SPACING = 20
        self._ROW_SPACING = 20
        self._LEFT_MARGIN = 110
        self._BOTTOM_MARGIN = 110
        self._TILE_SPACING = 1.6


    def draw_messages(self):
        self._health = 100
        self._weapons = ['knife', 'sword', 'pistol', 'laser']

        # Welcome Message
        arcade.draw_text(self._TITLE, constants.windowX / len(self._TITLE) + 250, constants.windowY - 40, self._FONT_COLOR, 25, 340, 'center', 'calibri', True)

        # Health
        arcade.draw_text(f'HEALTH:{self._health}', 15, 15, self._FONT_COLOR, 25, 200, 'left', 'calibri', True)

        # Weapons
        arcade.draw_text(f'WEAPON:{self._weapons[3]}', constants.windowX - 215, 15, self._FONT_COLOR, 25, 200, 'left', 'calibri', True)

    def draw_floor(self):
        self.floor_list = arcade.SpriteList()
        for i in range(constants.windowY // self._FLOOR_H + 1):
            for j in range(constants.windowX // self._FLOOR_W - 2):

                # Create the floor instance
                floor = arcade.Sprite(self._WALL, 1,736.0,208.0,self._FLOOR_W, self._FLOOR_H)

                # Position the floor sprites
                floor.center_x = j * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 127
                floor.center_y = i * (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) - 65

                # Add the floor to the lists
                self.floor_list.append(floor)
        self.floor_list.draw()
    def draw_walls(self):
        
        # Draw Walls to choose what to do next
        self.wall_list_h = arcade.SpriteList()
        # Top wall
        for i in range(constants.windowY // self._WALL_W + 17):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1,736.0,320.0,self._WALL_W, self._WALL_H)

            # Position the floor sprites
            wall.center_x = i * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 158
            wall.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 423

            # Add the floor to the lists
            self.wall_list_h.append(wall)
        self.wall_list_h.draw()

     


        # Draw Walls to choose what to do next
        self.wall_list_v = arcade.SpriteList()

        # Right Vertical Wall
        for j in range(constants.windowY // self._WALL_H - 4):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1,736.0,320.0,self._WALL_W, self._WALL_H)

            # Position the floor sprites
            wall.center_x = (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) + 1052
            wall.center_y = j * (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) - 89

            # Add the floor to the lists
            self.wall_list_v.append(wall)
        self.wall_list_v.draw()

        # Left Vertical Wall
        self.wall_list_v_r = arcade.SpriteList()
        for k in range(constants.windowY // self._WALL_H - 4):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1,736.0,320.0,self._WALL_W, self._WALL_H)

            # Position the floor sprites
            wall.center_x = (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 190
            wall.center_y = k * (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) - 103

            # Add the floor to the lists
            self.wall_list_v_r.append(wall)
        self.wall_list_v_r.draw()

        # Bottom Wall
        self.wall_list_b = arcade.SpriteList()
        for m in range(constants.windowX // self._WALL_H - 1):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1,736.0,320.0,self._WALL_W, self._WALL_H)

            # Position the floor sprites
            wall.center_x = m * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 132
            wall.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) - 135

            # Add the floor to the lists
            self.wall_list_b.append(wall)
        self.wall_list_b.draw()


    def drawMap(self):
        Level1.draw_messages(self)
        Level1.draw_walls(self)
        Level1.draw_floor(self)