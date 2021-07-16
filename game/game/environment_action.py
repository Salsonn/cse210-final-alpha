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
        self.enemy = Enemy((150, 450), constants.enemyImages[0], 4, 50, 5, True)
        self.tick = 0

    def execute(self, entities, reticle):
        # List of specific actions to take every tick
        self.enemyAItick(self.enemies, entities["player"][0])
        self.reticleUpdate(entities, reticle)

    def enemyAItick(self, enemies, player):
        for enemy in enemies:
            self.check_player_side(enemy, player)
            tragectory = theta(Point(enemy.center_x, enemy.center_y), Point(player.center_x, player.center_y))
            enemy.change_x = round(math.cos(tragectory) * enemy.speed)
            enemy.change_y = round(math.sin(tragectory) * enemy.speed)

        if self.enemy_adder % constants.tickSpeed == 0:
            if len(enemies) <= 30:
                enemy = self.enemy.chooseEnemy()
                enemies.append(enemy)
                
        self.enemy_adder += 1
        self.tick += 1
        self.change_tick()
        # position_player = player.position
        # position_enemy = enemies[0].position
        # self.enemies[0].move_enemy(position_player, position_enemy)

    def check_player_side(self, enemy, player):
        eX, eY = enemy.position
        pX, pY = player.position
        side = cartesian(eX, eY, pX, pY)

        if side == 1 or side == 4 and not enemy.check_flip:
            enemy.check_flip = True
            enemy.__init__(enemy.position, enemy.enemyType, enemy.speed, enemy.pointValue, enemy.scale, enemy.check_flip)

        elif side == 2 or side == 3 and enemy.check_flip:
            enemy.check_flip = False
            enemy.__init__(enemy.position, enemy.enemyType, enemy.speed, enemy.pointValue, enemy.scale, enemy.check_flip)

    def change_tick(self):
        if self.tick == (60 * 10):
            constants.tickSpeed = 60
        elif self.tick == (60 * 30):
            constants.tickSpeed = 45
        elif self.tick == (60 * 45):
            constants.tickSpeed = 30
        elif self.tick == (60 * 75):
            constants.tickSpeed = 15
        elif self.tick == (60 * 100):
            constants.tickSpeed = 10
        elif self.tick == (60 * 120):
            constants.tickSpeed = 5

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
            