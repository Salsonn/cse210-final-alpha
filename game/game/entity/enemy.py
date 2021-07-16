from game.math import *
import arcade
import random
from game import constants
from game.entity.player import Player

class Enemy(arcade.Sprite):
    def __init__(self, position, enemy, speed, points):
        super().__init__(enemy, center_x=position[0], center_y=position[1])
        self.player = Player((640, 360), False)
        self._center_x = position[0]
        self._center_y = position[1]
        self.speed = speed
        self.pointValue = points
    
    def chooseEnemy(self):
        random_position = [constants.enemyTopRandom, constants.enemyBottomRandom, constants.enemyLeftRandom, constants.enemyRightRandom]
        
        blue_position = random.choice(random_position)
        yellow_position = random.choice(random_position)
        red_position = random.choice(random_position)

        blue_enemy = Enemy((random.randrange(blue_position["min_x"], blue_position["max_x"]), random.randrange(blue_position["min_y"], blue_position["max_y"])), constants.enemyImages[2], constants.blueEnemySpeed, constants.blueEnemyPoints)
        yellow_enemy = Enemy((random.randrange(yellow_position["min_x"], yellow_position["max_x"]), random.randrange(yellow_position["min_y"], yellow_position["max_y"])), constants.enemyImages[1], constants.yellowEnemySpeed, constants.yellowEnemyPoints)
        red_enemy = Enemy((random.randrange(red_position["min_x"], red_position["max_x"]), random.randrange(red_position["min_y"], red_position["max_y"])), constants.enemyImages[0], constants.redEnemySpeed, constants.redEnemyPoints)
 
        enemyTypes = [blue_enemy, yellow_enemy, red_enemy]
        chosen_enemy = random.choice(enemyTypes)

        return chosen_enemy

    def damage(self, damage, enemies, player):
        player.changeScore(self.pointValue)
        enemies.remove(self)
