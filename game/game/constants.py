import os
import arcade

windowX = 1280
windowY = 720

movementSpeed = 5 # Pixels per frame
projectileSpeed = 30
acceleration = 2 # Pixels per frame per frame

playerImage = "./images/wall_tile_sprite.png"
projectile1Image = "./images/floor_tile_sprite.png"

debug = False
collisionDebug = False