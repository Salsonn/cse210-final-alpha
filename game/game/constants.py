import os
import arcade
import random

windowX = 1280
windowY = 720

movementSpeed = 5 # Pixels per frame
projectileSpeed = 30

blueEnemySpeed = random.randrange(5, 6)
yellowEnemySpeed = random.randrange(3, 5)
redEnemySpeed = random.randrange(2, 3)

blueEnemyDamage = 2
yellowEnemyDamage = 4
redEnemyDamage = 6

blueEnemyPoints = 60
yellowEnemyPoints = 40
redEnemyPoints = 30

playerScore = 0
playerHealth = 100

tickSpeed = 60

firstWave = 500
secondWave = 1500
thirdWave = 4000
fourthWave = 7750
fifthWave = 12750
sixthWave = 20750

enemyTopRandom = {'min_x': 100, 'max_x': 1000, 'min_y': windowY-1, 'max_y': windowY}
enemyBottomRandom = {'min_x': 100, 'max_x': 1000, 'min_y': 0, 'max_y': 1}
enemyLeftRandom = {'min_x': 0, 'max_x': 1, 'min_y': 75, 'max_y': 575}
enemyRightRandom = {'min_x': windowX-1, 'max_x': windowX, 'min_y': 75, 'max_y': 575}

acceleration = 2 # Pixels per frame per frame

dropsImage = "game\\images\\medkit_sprite.png"
playerImagePath = "game\\images\\characters\\Player.gif"
playerImage = [arcade.load_texture(playerImagePath), arcade.load_texture(playerImagePath, flipped_horizontally=True)]
projectile1Image = "game\\images\\bullet.png"
enemyImages = ["game\\images\\characters\\Enemy.gif", "game\\images\\characters\\Enemy2.gif", "game\\images\\characters\\Enemy3.gif"]

weaponImages = ["game\\images\\weapons\\ak.png", "game\\images\\weapons\\machinegun.png"]
weaponImagePath1 = weaponImages[0]
weapon1Image = [arcade.load_texture(weaponImagePath1, flipped_horizontally=True), arcade.load_texture(weaponImagePath1, flipped_horizontally=True, flipped_vertically=True)]
weaponImagePath2 = weaponImages[1]
weapon2Image = [arcade.load_texture(weaponImagePath2, flipped_horizontally=True), arcade.load_texture(weaponImagePath2, flipped_horizontally=True, flipped_vertically=True)]

weaponDamages = [1, 2]

weaponRates = [10, 5]

menuMusic = "game\\sounds\\Warhammer.mp3" #"game\\sounds\\CoconutMall.mp3"
levelMusic = "game\\sounds\\background.mp3" # "game\\sounds\\ангел.mp3"



currentLevel = 0

mute = True
# Music length in seconds
menuMusicLength = 127

debug = False
collisionDebug = False