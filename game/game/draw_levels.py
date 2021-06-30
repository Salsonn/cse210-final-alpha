import arcade
from game import constants

class Level:
    def level_one(self):

        arcade.start_render()

        # Draw the Walls
        arcade.draw_rectangle_filled(constants.LEFT_WALL_X, constants.LEFT_WALL_Y, 20, constants.windowY, constants.WALL_COLOR_2)
        arcade.draw_rectangle_filled(constants.windowX, constants.LEFT_WALL_Y, 20, constants.windowY, constants.WALL_COLOR_2)
        arcade.draw_rectangle_filled(constants.windowX / 2, constants.windowY, constants.windowX, 20, constants.WALL_COLOR_2)
        arcade.draw_rectangle_filled(constants.windowX / 2, 0, constants.windowX, 20, constants.WALL_COLOR_2)

        # Welcome Message
        arcade.draw_text(constants.INFO, constants.windowX / len(constants.TITLE) + 100, constants.windowY - 40, constants.FONT_COLOR, 25, 340, 'center', 'calibri', True)

        arcade.finish_render()