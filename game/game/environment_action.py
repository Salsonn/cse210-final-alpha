import random
import arcade

from game import constants
from game.math import *
from game.action import Action
from game.entity.player import Player
from game.entity.weapon import Weapon
from game.entity.enemy import Enemy

class EnvironmentAction:

    def __init__(self, enemies):
        self.enemies = enemies
        self.weapon = Weapon(False, (640, 360))
        self.playerFlipped = False
        self.player = Player((640, 360), False)
        self.enemy_adder = 0
        self.enemy = Enemy((150, 450), constants.enemyImages[0], 4, 50, 5)

    def execute(self, entities, reticle):
        # List of specific actions to take every tick
        self.enemyAItick(self.enemies, entities["player"][0])
        self.reticleUpdate(entities, reticle)

    def enemyAItick(self, enemies, player):
        for enemy in enemies:
            tragectory = theta(Point(enemy.center_x, enemy.center_y), Point(player.center_x, player.center_y))
            enemy.change_x = round(math.cos(tragectory) * enemy.speed)
            enemy.change_y = round(math.sin(tragectory) * enemy.speed)

        if self.enemy_adder % 15 == 0:
            if len(enemies) <= 30:
                enemy = self.enemy.chooseEnemy()
                enemies.append(enemy)
        self.enemy_adder += 1

        # position_player = player.position
        # position_enemy = enemies[0].position
        # self.enemies[0].move_enemy(position_player, position_enemy)

    def reticleUpdate(self, entities, reticle):
        weapon_angle = self.weapon.update_weapon_angle(entities["player"][0].center_x, entities["player"][0].center_y, reticle.get_reticleX(), reticle.get_reticleY())
        entities["weapon"][0].angle = weapon_angle
        flip = self.weapon.flip()
        if not flip and self.playerFlipped:
            self.playerFlipped = flip
            position = entities["player"][0].position
            entities["weapon"] = [Weapon(flip, position)]
            entities["player"] = [Player(position, flip)]

        if flip and not self.playerFlipped:
            self.playerFlipped = flip
            position = entities["player"][0].position
            entities["weapon"] = [Weapon(flip, position)]
            entities["player"] = [Player(position, flip)]
            