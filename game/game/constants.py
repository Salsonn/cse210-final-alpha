import os
import arcade

windowX = 1280
windowY = 720

movementSpeed = 5 # Pixels per frame
projectileSpeed = 30
acceleration = 2 # Pixels per frame per frame

dropsImage = "./images/wall_tile_sprite.png"
playerImage = "game\\images\\characters\\Player.gif"
projectile1Image = "game\\images\\bullet.png"
enemyImage = "game\\images\\characters\\Enemy.gif"
weaponImage = "game\\images\\weapons\\ak.png"

debug = False
collisionDebug = False