from game.math import *
import arcade
import random
from game import constants
from game.entity.player import Player

class Enemy(arcade.Sprite):
    def __init__(self, position, enemyType, speed, points, damage, check_flip):
        super().__init__(enemyType, center_x=position[0], center_y=position[1], scale = 1.5, flipped_horizontally=check_flip)
        self.player = Player((640, 360), False)
        self._center_x = position[0]
        self._center_y = position[1]
        self.enemyType = enemyType
        self.speed = speed
        self.pointValue = points
        self.power = damage
        self.check_flip = check_flip
        self.scale = 1.5
    
    def drawEnemy(self, position, enemyType, check_flip):
        self._center_x = position[0]
        self._center_y = position[1]
        super().__init__(enemyType, center_x=self._center_x, center_y=self._center_y, scale = self.scale, flipped_horizontally=check_flip)

    def chooseEnemy(self):
        random_position = [constants.enemyTopRandom, constants.enemyBottomRandom, constants.enemyLeftRandom, constants.enemyRightRandom]
        
        blue_position = random.choice(random_position)
        yellow_position = random.choice(random_position)
        red_position = random.choice(random_position)

        blue_enemy = Enemy((random.randrange(blue_position["min_x"], blue_position["max_x"]), random.randrange(blue_position["min_y"], blue_position["max_y"])), constants.enemyImages[2], constants.blueEnemySpeed, constants.blueEnemyPoints, constants.blueEnemyDamage, True)
        yellow_enemy = Enemy((random.randrange(yellow_position["min_x"], yellow_position["max_x"]), random.randrange(yellow_position["min_y"], yellow_position["max_y"])), constants.enemyImages[1], constants.yellowEnemySpeed, constants.yellowEnemyPoints, constants.yellowEnemyDamage, True)
        red_enemy = Enemy((random.randrange(red_position["min_x"], red_position["max_x"]), random.randrange(red_position["min_y"], red_position["max_y"])), constants.enemyImages[0], constants.redEnemySpeed, constants.redEnemyPoints, constants.redEnemyDamage, True)
 
        enemyTypes = [blue_enemy, blue_enemy, blue_enemy, yellow_enemy, yellow_enemy, red_enemy]
        chosen_enemy = random.choice(enemyTypes)

        return chosen_enemy

    def damage(self, damage, enemies, player):
        player.changeScore(self.pointValue)
        enemies.remove(self)
        # print()