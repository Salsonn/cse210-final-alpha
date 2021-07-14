import random
import arcade

from game import constants
from game.math import *
from game.action import Action

class EnvironmentAction:

    def __init__(self, enemies):
        self.enemies = enemies

    def execute(self, entities, reticle):
        # List of specific actions to take every tick
        self.enemyAItick(self.enemies, entities["player"][0])

    def enemyAItick(self, enemies, player):
        for enemy in enemies:
            tragectory = theta(Point(enemy.center_x, enemy.center_y), Point(player.center_x, player.center_y))
            enemy.change_x = round(math.cos(tragectory) * constants.enemySpeed)
            enemy.change_y = round(math.sin(tragectory) * constants.enemySpeed)

        # position_player = player.position
        # position_enemy = enemies[0].position
        # self.enemies[0].move_enemy(position_player, position_enemy)
