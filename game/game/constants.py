import os
import arcade

windowX = 1280
windowY = 720

movementSpeed = 5 # Pixels per frame
projectileSpeed = 30
blueEnemySpeed = 4
yellowEnemySpeed = 5
redEnemySpeed = 6
acceleration = 2 # Pixels per frame per frame

dropsImage = "game\\images\\medkit_sprite.png"
playerImage = "game\\images\\characters\\Player.gif"
projectile1Image = "game\\images\\bullet.png"
enemyImages = ["game\\images\\characters\\Enemy.gif", "game\\images\\characters\\Enemy2.gif", "game\\images\\characters\\Enemy3.gif"]
weaponImage = "game\\images\\weapons\\ak.png"
menuMusic = "game\\sounds\\background.mp3"
# menuMusic = "game\\sounds\\CoconutMall.mp3"
levelMusic = "game\\sounds\\ангел.mp3"

debug = False
collisionDebug = False