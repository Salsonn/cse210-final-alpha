import os
import arcade

windowX = 1280
windowY = 720

movementSpeed = 5 # Pixels per frame
projectileSpeed = 30
acceleration = 2 # Pixels per frame per frame

dropsImage = "./images/wall_tile_sprite.png"
playerImage = "./images/characters/Player.gif"
projectile1Image = "./images/bullet.png"
enemyImage = "./images/characters/Enemy.gif"
weaponImage = "./images/weapons/ak.png"

debug = False
collisionDebug = False