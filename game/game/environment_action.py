import random
import arcade

from game import constants
from game.math import *
from game.action import Action
from game.entity.player import Player
from game.entity.weapon import Weapon
from game.entity.enemy import Enemy

class EnvironmentAction:

    def __init__(self, entities):
        self._entities = entities
        self.enemies = entities["enemy"]
        self.player = Player((640, 360), False)
        self.enemy_adder = 0
        self.enemy = Enemy((150, 450), constants.enemyImages[0], 4, 50, 5, True)
        self.tick_speed = constants.tickSpeed
        self.change = True

    def execute(self, entities, reticle, current_level):
        # List of specific actions to take every tick
        self.enemyAItick(self.enemies, entities["player"][0], current_level)
        self.change_tick(entities["player"][0], entities["weapon"])
        self.reticleUpdate(entities["player"][0], entities["weapon"][0], reticle)

    def enemyAItick(self, enemies, player, current_level):
        if current_level == 1:
            for enemy in enemies:
                self.check_player_side(enemy, player)
                tragectory = theta(Point(enemy.center_x, enemy.center_y), Point(player.center_x, player.center_y))
                enemy.change_x = round(math.cos(tragectory) * enemy.speed)
                enemy.change_y = round(math.sin(tragectory) * enemy.speed)

            if self.enemy_adder % self.tick_speed == 0:
                if len(enemies) <= 30:
                    enemy = self.enemy.chooseEnemy()
                    enemies.append(enemy)
                    
            self.enemy_adder += 1
        # position_player = player.position
        # position_enemy = enemies[0].position
        # self.enemies[0].move_enemy(position_player, position_enemy)

    def check_player_side(self, enemy, player):
        eX, eY = enemy.position
        pX, pY = player.position
        side = cartesian(eX, eY, pX, pY)

        if side == 1 or side == 4:
            enemy.drawEnemy(enemy.position, enemy.enemyType, True)
        else: 
            enemy.drawEnemy(enemy.position, enemy.enemyType, False)

    def change_tick(self, player, weapon):
        self.score = player.getScore()
        if 1 <= self.score < constants.firstWave:pass

        elif constants.firstWave <= self.score < constants.secondWave:
            self.tick_speed = constants.tickSpeed / 2
        elif constants.secondWave <= self.score < constants.thirdWave:
            self.tick_speed = constants.tickSpeed / 3
            if self.change:
                self.change = False
                old_weapon, new_weapon = weapon[0], weapon[1]
                weapon[0], weapon[1] = new_weapon, old_weapon
                self.weapon = weapon[0]

        elif constants.thirdWave <= self.score < constants.fourthWave:
            self.tick_speed = constants.tickSpeed / 4
        elif constants.fourthWave <= self.score < constants.fifthWave:
            self.tick_speed = constants.tickSpeed / 8
        elif constants.fifthWave <= self.score < constants.sixthWave:
            self.tick_speed = constants.tickSpeed / 12
        elif constants.sixthWave <= self.score:
            self.tick_speed = constants.tickSpeed / 24
        else: 
            self.tick_speed = constants.tickSpeed
            if not self.change:
                self.change = True
                old_weapon, new_weapon = weapon[0], weapon[1]
                weapon[0], weapon[1] = new_weapon, old_weapon
                self.weapon = weapon[0]


    def reticleUpdate(self, player, weapon, reticle):
        weapon_angle = weapon.update_weapon_angle(player.center_x, player.center_y, reticle.get_reticleX(), reticle.get_reticleY())
        weapon.angle = weapon_angle
        flip = weapon.flip()
        position = player.position
        weapon.flipH(flip)
        player.flipH(flip)
            