import arcade
import random
import time

from arcade import texture



class Game_textures:
    

    def __init__(self):
        
        self.SCREEN_WIDTH = 600
        self.SCREEN_HEIGHT = 600
        self.BACKGROUND_COLOR = arcade.color.BLACK
        self.FLOOR = './floor_tile_sprite.png'
        self.FLOOR_W = 32
        self.FLOOR_H = 32
        self.WALL = './wall_tile_sprite.png'
        self.WALL_W = 32
        self.WALL_H = 32
        self.FONT_COLOR = arcade.color.PALE_BLUE
        self.WALL_COLOR = arcade.color.RED
        self.WALL_COLOR_2 = arcade.color.CYBER_YELLOW
        self.LEFT_WALL_X = 0
        self.LEFT_WALL_Y = self.SCREEN_HEIGHT / 2
        self.TITLE = 'WELCOME TO THE GAME'
        self.RADIUS = 150
        self.SOUND = arcade.load_sound('./sounds/Tada-sound.mp3')
        self.INFO = 'CHOOSE WHAT TO DO'
        self.TEMP = arcade.color.GREEN
        

        # arcade.load_texture(FLOOR)
        arcade.set_background_color(self.BACKGROUND_COLOR)

    def welcome_screen(self):
        arcade.open_window(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.TITLE)
        arcade.start_render()
        
        # Trying to import the sprites
        # texture.Texture.draw_sized(FLOOR,SPRITE_W /2,SPRITE_H/2,SCREEN_WIDTH,SCREEN_HEIGHT)
        # arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SPRITE_W //2, SPRITE_H//2, FLOOR)

        # Draw the Edges
        arcade.draw_rectangle_filled(self.LEFT_WALL_X, self.LEFT_WALL_Y, 20, self.SCREEN_HEIGHT, self.WALL_COLOR)
        arcade.draw_rectangle_filled(self.SCREEN_WIDTH, self.LEFT_WALL_Y, 20, self.SCREEN_HEIGHT, self.WALL_COLOR)
        arcade.draw_rectangle_filled(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT, self.SCREEN_WIDTH, 20, self.WALL_COLOR)
        arcade.draw_rectangle_filled(self.SCREEN_WIDTH / 2, 0, self.SCREEN_WIDTH, 20, self.WALL_COLOR)

        # Welcome Message
        arcade.draw_text('WELCOME', self.SCREEN_WIDTH / 4, self.SCREEN_HEIGHT / 2, self.FONT_COLOR, 50, 300, 'center', 'calibri', True)

        # Play sound
        # arcade.play_sound(SOUND)
        # arcade.stop_sound(SOUND)

        arcade.finish_render()

    def second_screen(self):
        arcade.start_render()

        # Draw the Edges
        arcade.draw_rectangle_filled(self.LEFT_WALL_X, self.LEFT_WALL_Y, 20, self.SCREEN_HEIGHT, self.WALL_COLOR_2)
        arcade.draw_rectangle_filled(self.SCREEN_WIDTH, self.LEFT_WALL_Y, 20, self.SCREEN_HEIGHT, self.WALL_COLOR_2)
        arcade.draw_rectangle_filled(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT, self.SCREEN_WIDTH, 20, self.WALL_COLOR_2)
        arcade.draw_rectangle_filled(self.SCREEN_WIDTH / 2, 0, self.SCREEN_WIDTH, 20, self.WALL_COLOR_2)

        # Welcome Message
        arcade.draw_text(self.INFO, self.SCREEN_WIDTH / len(self.INFO) + 100, self.SCREEN_HEIGHT - 40, self.FONT_COLOR, 25, 340, 'center', 'calibri', True)

        # Draw Walls to choose what to do next
        arcade.draw_rectangle_filled(120,self.SCREEN_HEIGHT/1.5,self.SCREEN_WIDTH/4,20,self.TEMP)
        arcade.draw_rectangle_filled(self.SCREEN_WIDTH - 120, self.SCREEN_HEIGHT/1.5,self.SCREEN_WIDTH/4,20,self.TEMP)

        arcade.finish_render()

    def instruction_screen(self):
        arcade.start_render()

        # Draw the Walls
        arcade.draw_rectangle_filled(self.LEFT_WALL_X, self.LEFT_WALL_Y, 20, self.SCREEN_HEIGHT, self.WALL_COLOR)
        arcade.draw_rectangle_filled(self.SCREEN_WIDTH, self.LEFT_WALL_Y, 20, self.SCREEN_HEIGHT, self.WALL_COLOR)
        arcade.draw_rectangle_filled(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT, self.SCREEN_WIDTH, 20, self.WALL_COLOR)
        arcade.draw_rectangle_filled(self.SCREEN_WIDTH / 2, 0, self.SCREEN_WIDTH, 20, self.WALL_COLOR)

        # Welcome Message
        arcade.draw_text(self.INFO, self.SCREEN_WIDTH / len(self.TITLE2) + 100, self.SCREEN_HEIGHT - 40, self.FONT_COLOR, 25, 340, 'center', 'calibri', True)

        # Draw Walls to choose what to do next
        top_left = arcade.draw_rectangle_filled(120,self.SCREEN_HEIGHT/1.5,self.SCREEN_WIDTH/4,20,self.TEMP)
        top_right = arcade.draw_rectangle_filled(self.SCREEN_WIDTH - 120, self.SCREEN_HEIGHT/1.5,self.SCREEN_WIDTH/4,20,self.TEMP)
        right = arcade.draw_rectangle_filled(self.SCREEN_WIDTH - 50, self.SCREEN_HEIGHT/1.5-200,self.SCREEN_WIDTH/4,20,self.TEMP,90)

        arcade.draw_text(self.INFO, self.SCREEN_WIDTH - 470, self.SCREEN_HEIGHT - 200, self.FONT_COLOR, 20, 340, 'center', 'calibri', True)
        arcade.draw_text(self.START, self.SCREEN_WIDTH -300, self.SCREEN_HEIGHT - 250, self.FONT_COLOR, 20, 340, 'center', 'calibri', True)

        arcade.finish_render()

    def level_one(self):

        arcade.start_render()

        # Draw the Walls
        arcade.draw_rectangle_filled(self.LEFT_WALL_X, self.LEFT_WALL_Y, 20, self.SCREEN_HEIGHT, self.WALL_COLOR_2)
        arcade.draw_rectangle_filled(self.SCREEN_WIDTH, self.LEFT_WALL_Y, 20, self.SCREEN_HEIGHT, self.WALL_COLOR_2)
        arcade.draw_rectangle_filled(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT, self.SCREEN_WIDTH, 20, self.WALL_COLOR_2)
        arcade.draw_rectangle_filled(self.SCREEN_WIDTH / 2, 0, self.SCREEN_WIDTH, 20, self.WALL_COLOR_2)

        # Welcome Message
        arcade.draw_text(self.START, self.SCREEN_WIDTH / len(self.TITLE2) + 100, self.SCREEN_HEIGHT - 40, self.FONT_COLOR, 25, 340, 'center', 'calibri', True)

        arcade.finish_render()



