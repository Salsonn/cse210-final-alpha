import arcade
from game import constants

class Level:

    def welcome_screen(self):
        
        arcade.start_render()
        
        # Draw the Edges
        arcade.draw_rectangle_filled(constants.LEFT_WALL_X, constants.LEFT_WALL_Y, 20, constants.windowY, constants.WALL_COLOR)
        arcade.draw_rectangle_filled(constants.windowX, constants.LEFT_WALL_Y, 20, constants.windowY, constants.WALL_COLOR)
        arcade.draw_rectangle_filled(constants.windowX / 2, constants.windowY, constants.windowX, 20, constants.WALL_COLOR)
        arcade.draw_rectangle_filled(constants.windowX / 2, 0, constants.windowX, 20, constants.WALL_COLOR)

        # Welcome Message
        arcade.draw_text('WELCOME', constants.windowX / 2, constants.windowY / 2, constants.FONT_COLOR, 50, 300, 'center', 'calibri', True)

        # Play sound
        # arcade.play_sound(constants.SOUND)
        # arcade.stop_sound(constants.SOUND)

        arcade.finish_render()


    def instruction_screen(self):
        arcade.start_render()

        # Draw the Walls
        arcade.draw_rectangle_filled(constants.LEFT_WALL_X, constants.LEFT_WALL_Y, 20, constants.windowY, constants.WALL_COLOR)
        arcade.draw_rectangle_filled(constants.windowX, constants.LEFT_WALL_Y, 20, constants.windowY, constants.WALL_COLOR)
        arcade.draw_rectangle_filled(constants.windowX / 2, constants.windowY, constants.windowX, 20, constants.WALL_COLOR)
        arcade.draw_rectangle_filled(constants.windowX / 2, 0, constants.windowX, 20, constants.WALL_COLOR)

        # Welcome Message
        arcade.draw_text(constants.INFO, constants.windowX / len(constants.TITLE) + 100, constants.windowY - 40, constants.FONT_COLOR, 25, 340, 'center', 'calibri', True)

        # Draw Walls to choose what to do next
        self.wall_list_h = arcade.SpriteList()

        for i in range(constants.windowY // constants.WALL_H - 8):

            # Create the floor instance
            wall = arcade.Sprite(constants.WALL, 1)

            # Position the floor sprites
            wall.center_x = i * constants.COLUMN_SPACING + constants.LEFT_MARGIN
            wall.center_y = constants.ROW_SPACING + constants.BOTTOM_MARGIN + 400

            # Add the floor to the lists
            self.wall_list_h.append(wall)
            self.wall_list_h.draw()

        arcade.draw_text('Level 1', wall.center_x, constants.windowY - 150, constants.FONT_COLOR, 20, 340, 'center', 'calibri', True)

             # Draw Walls to choose what to do next
        self.wall_list_v = arcade.SpriteList()

        for j in range(constants.windowY // constants.WALL_H - 8):

            # Create the floor instance
            wall = arcade.Sprite(constants.WALL, 1)

            # Position the floor sprites
            wall.center_x = constants.COLUMN_SPACING + constants.LEFT_MARGIN + 1000
            wall.center_y = j * constants.ROW_SPACING + constants.BOTTOM_MARGIN 

            # Add the floor to the lists
            self.wall_list_v.append(wall)
            self.wall_list_v.draw()

        
        arcade.draw_text('Instructions', constants.windowX -300, constants.windowY - 250, constants.FONT_COLOR, 20, 340, 'center', 'calibri', True)

        arcade.finish_render()

    def level_one(self):

        arcade.start_render()

        # Draw the Walls
        arcade.draw_rectangle_filled(constants.LEFT_WALL_X, constants.LEFT_WALL_Y, 20, constants.windowY, constants.WALL_COLOR_2)
        arcade.draw_rectangle_filled(constants.windowX, constants.LEFT_WALL_Y, 20, constants.windowY, constants.WALL_COLOR_2)
        arcade.draw_rectangle_filled(constants.windowX / 2, constants.windowY, constants.windowX, 20, constants.WALL_COLOR_2)
        arcade.draw_rectangle_filled(constants.windowX / 2, 0, constants.windowX, 20, constants.WALL_COLOR_2)

        # Level Message
        arcade.draw_text(constants.LEVEL_1, constants.windowX / 2 - 200, constants.windowY - 40, constants.FONT_COLOR, 25, 340, 'center', 'calibri', True)


        self.floor_list = arcade.SpriteList()

        for i in range(constants.windowY // constants.FLOOR_H - 5):
            for j in range(constants.windowX // constants.FLOOR_W -1):

                # Create the floor instance
                floor = arcade.Sprite(constants.FLOOR, 1)

                # Position the floor sprites
                floor.center_x = j * constants.COLUMN_SPACING + constants.LEFT_MARGIN
                floor.center_y = i * constants.ROW_SPACING + constants.BOTTOM_MARGIN

                # Add the floor to the lists
                self.floor_list.append(floor)
                self.floor_list.draw()

        arcade.finish_render()