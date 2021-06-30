import os
import arcade

windowX = 1280
windowY = 720

movementSpeed = 5 # Pixels per frame
acceleration = 2 # Pixels per frame per frame

playerImage = "./images/wall_tile_sprite.png"
projectile1Image = "./images/floor_tile_sprite.png"

BACKGROUND_COLOR = arcade.color.BLACK
FLOOR = './images/floor_tile_sprite.png'
FLOOR_W = 32
FLOOR_H = 32
WALL = './images/wall_tile_sprite.png'
WALL_W = 32
WALL_H = 32
FONT_COLOR = arcade.color.PALE_BLUE
WALL_COLOR = arcade.color.RED
WALL_COLOR_2 = arcade.color.CYBER_YELLOW
LEFT_WALL_X = 0
LEFT_WALL_Y = windowY / 2
TITLE = 'WELCOME TO THE GAME'
RADIUS = 150
#SOUND = arcadeload_sound('/sounds/Tada-soundmp3')
INFO = 'CHOOSE WHAT TO DO'
LEVEL_1 = 'LEVEL 1'
COLUMN_SPACING = 32.0
ROW_SPACING = 32.0
LEFT_MARGIN = 32
BOTTOM_MARGIN = 110