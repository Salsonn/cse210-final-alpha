import arcade

from game import constants

class MainMenu():

    def __init__(self):
        self._BACKGROUND_COLOR = arcade.color.BLACK
        self._FONT_COLOR = arcade.color.PALE_BLUE
        
        self._TITLE = 'WELCOME TO THE GAME'
        self._INFO = 'CHOOSE WHAT TO DO'

        self._FLOOR = './images/catacombs/cata_v1.0/mainlevbuild.png'
        self._FLOOR_W = 32
        self._FLOOR_H = 48
        
        self._WALL = './images/catacombs/cata_v1.0/mainlevbuild.png'
        self._WALL_W = 32
        self._WALL_H = 32
        self._WALL_COLOR = arcade.color.RED
        self._WALL_COLOR_2 = arcade.color.CYBER_YELLOW
        self._LEFT_WALL_X = 0
        self._LEFT_WALL_Y = constants.windowY / 2

        self._POT = './images/TX_Props.png'
        self._POT_W = 24
        self._POT_H = 36

        self._ALTAR = './images/TX_Props.png'
        self._ALTAR_W = 98
        self._ALTAR_H = 76

        self._STONE = './images/TX_Props.png'
        self._STONE_W = 28
        self._STONE_H = 66
        
        #SOUND = arcadeload_sound('/sounds/Tada-soundmp3')
        
        self._COLUMN_SPACING = 20
        self._ROW_SPACING = 20
        self._LEFT_MARGIN = 110
        self._BOTTOM_MARGIN = 110
        self._TILE_SPACING = 1.6

    def drawMap(self):
    
        MainMenu.draw_walls(self)
        MainMenu.draw_messages(self)
        MainMenu.draw_floor(self)
        MainMenu.draw_decor(self)

    def draw_walls(self):
        
        # Draw Walls to choose what to do next
        self.wall_list_h = arcade.SpriteList()
        # Top left wall
        for i in range(constants.windowY // self._WALL_H - 4):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1,736.0,320.0,self._WALL_W, self._WALL_H)

            # Position the floor sprites
            wall.center_x = i * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 157
            wall.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 373

            # Add the floor to the lists
            self.wall_list_h.append(wall)
        self.wall_list_h.draw()

        # Top middle wall
        self.wall_list_h_l = arcade.SpriteList()
        for l in range(constants.windowY // self._WALL_H - 14):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1,736.0,320.0,self._WALL_W, self._WALL_H)

            # Position the floor sprites
            wall.center_x = l * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) + 500
            wall.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 373

            # Add the floor to the lists
            self.wall_list_h_l.append(wall)
        self.wall_list_h_l.draw()
        
        # Top right wall
        self.wall_list_h_a = arcade.SpriteList()
        for a in range(constants.windowY // self._WALL_H - 13):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1,736.0,320.0,self._WALL_W, self._WALL_H)

            # Position the floor sprites
            wall.center_x = a * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) + 828
            wall.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 373

            # Add the floor to the lists
            self.wall_list_h_a.append(wall)
        self.wall_list_h_a.draw()


        # Draw Walls to choose what to do next
        self.wall_list_v = arcade.SpriteList()

        # Right Vertical Wall
        for j in range(constants.windowY // self._WALL_H - 4):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1,736.0,320.0,self._WALL_W, self._WALL_H)

            # Position the floor sprites
            wall.center_x = (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) + 1052
            wall.center_y = j * (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) - 155

            # Add the floor to the lists
            self.wall_list_v.append(wall)
        self.wall_list_v.draw()

        # Left Vertical Wall
        for k in range(constants.windowY // self._WALL_H - 4):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1,736.0,320.0,self._WALL_W, self._WALL_H)

            # Position the floor sprites
            wall.center_x = (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 190
            wall.center_y = k * (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) - 155

            # Add the floor to the lists
            self.wall_list_v.append(wall)
        self.wall_list_v.draw()

        # Bottom Wall
        for m in range(constants.windowX // self._WALL_H - 2):

            # Create the floor instance
            wall = arcade.Sprite(self._WALL, 1,736.0,320.0,self._WALL_W, self._WALL_H)

            # Position the floor sprites
            wall.center_x = m * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 130
            wall.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) - 187

            # Add the floor to the lists
            self.wall_list_h.append(wall)
        self.wall_list_h.draw()

        

    def draw_floor(self):
        self.floor_list = arcade.SpriteList()
        for i in range(constants.windowY // self._FLOOR_H + 1):
            for j in range(constants.windowX // self._FLOOR_W - 2):

                # Create the floor instance
                floor = arcade.Sprite(self._WALL, 1,736.0,208.0,self._FLOOR_W, self._FLOOR_H)

                # Position the floor sprites
                floor.center_x = j * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 127
                floor.center_y = i * (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) - 115

                # Add the floor to the lists
                self.floor_list.append(floor)
        self.floor_list.draw()

    def draw_messages(self):
        
        # Welcome Message
        arcade.draw_text(self._INFO, constants.windowX / len(self._TITLE) + 100, constants.windowY - 40, self._FONT_COLOR, 25, 340, 'center', 'calibri', True)

        # Level Message
        arcade.draw_text('Level 1', 450, constants.windowY - 60, self._FONT_COLOR, 20, 340, 'center', 'calibri', True)
        
        # Instruction Message
        arcade.draw_text('Instructions', constants.windowX - 485, constants.windowY - 60, self._FONT_COLOR, 20, 340, 'center', 'calibri', True)

    def draw_decor(self):

        # Draw Arch for Instructions
        arch1 = arcade.Sprite(self._WALL, 1, 640.0, 0.0,80,96)
        arch1.center_x = 27 * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 80
        arch1.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 405
        arch1.draw()

        # Draw Arch for Level1
        arch2 = arcade.Sprite(self._WALL, 1, 640.0, 0.0,80,96)
        arch2.center_x = 16.5 * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 84
        arch2.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 405
        arch2.draw()

        # Draw Pottery
        pot = arcade.Sprite(self._POT, 1, 164, 216, self._POT_W, self._POT_H)
        for p in range(3):
            pot.center_x = p * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 65
            pot.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 300
            pot.draw()

        # Draw Altar
        altar = arcade.Sprite(self._ALTAR, 1, 351, 267, self._ALTAR_W, self._ALTAR_H)
        altar.center_x = 6 * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 65
        altar.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 100
        altar.draw()

        altar2 = arcade.Sprite(self._ALTAR, 1, 351, 267, self._ALTAR_W, self._ALTAR_H)
        altar2.center_x = 28 * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 65
        altar2.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 100
        altar2.draw()

        stone = arcade.Sprite(self._ALTAR, 1, 226, 91, self._STONE_W, self._STONE_H)
        stone.center_x = 6 * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 65
        stone.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 125
        stone.draw()

        stone2 = arcade.Sprite(self._ALTAR, 1, 226, 91, self._STONE_W, self._STONE_H)
        stone2.center_x = 28 * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 65
        stone2.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 125
        stone2.draw()
 
