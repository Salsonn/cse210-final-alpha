import random
import arcade

from game import constants
from game.math import *
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, draw_actors_action):
        self.levelControl = draw_actors_action

    def execute(self, entities, reticle):
        """Executes the action using the given actors.

        Args:
            entities (dict): The game actors {key: tag, value: list}.
        """
        # Prevent the player from moving off-screen
        self._screenEdgeDetection(entities["player"][0], entities["projectile"])

        # Prevent the player from smashing through walls
        if entities["player"][0].change_x or entities["player"][0].change_y: 
            self._wallPlayerDetection(entities["player"][0], entities["projectile"], entities["wall"])

        # Bounce projectiles off the walls
        self._wallProjectileDetection(entities["projectile"], entities["wall"])

        # Keeps the enemies from making inappropriate advances on the player.
        self._enemyPlayerDetection(entities["player"][0], entities["enemy"])

        # Detects when the player hits a level trigger
        self._levelChangeDetection(entities["player"][0], entities["trigger"])

        # Keep the enemies from trampling each other and hitting walls.
        self._enemySocialDistancing(entities["enemy"])
        self._wallEnemyDetection(entities["enemy"], entities["wall"])

    def _enemySocialDistancing(self, enemies):
        for enemy in enemies:
            for enemy2 in enemies:
                if self.proxCheck(enemy, enemy2):
                    if enemy != enemy2:
                        l, r, t, b = self._detectCollision(enemy, enemy2, 0)
                        if True in {l, r, t, b}:
                            self._handleCollision(enemy, l, r, t, b)

    def _wallEnemyDetection(self, enemies, walls):
        for enemy in enemies:
            for wall in walls:
                if self.proxCheck(enemy, wall):
                    l, r, t, b = self._detectCollision(enemy, wall, 1)
                    if True in {l, r, t, b}:
                        self._handleCollision(enemy, l, r, t, b)


    def _levelChangeDetection(self, player, triggers):
        if self.levelControl.getLevel() != 0:
            self.levelControl.changeLevel(0)

    def _screenEdgeDetection(self, player, projectiles):
        # Prevent player from leaving sides of window
        if (player.center_x - (player._get_width() / 2)) <= 0 and player.change_x < 0:
            player.change_x = max(player.change_x, 0)
        if (player.center_x + (player._get_width() / 2)) >= constants.windowX and player.change_x > 0:
            player.change_x = min(player.change_x, 0)
        if (player.center_y - (player._get_height() / 2)) <= 0 and player.change_y < 0:
            player.change_y = max(player.change_y, 0)
        if (player.center_y + (player._get_height() / 2)) >= constants.windowY and player.change_y > 0:
            player.change_y = min(player.change_y, 0)

        for projectile in projectiles:
            if (projectile.center_x + (projectile._get_width() / 2) <= 0 or projectile.center_x + (projectile._get_width() / 2) >= constants.windowX) or (projectile.center_y + (projectile._get_height() / 2) <= 0 or projectile.center_y + (projectile._get_height() / 2) >= constants.windowY):
                projectiles.remove(projectile)
                print("Removed a projectile")
    
    def _wallPlayerDetection(self, player, projectiles, walls):
        for entity in walls:
            l, r, t, b = self._detectCollision(player, entity, 1)
            if True in {l, r, t, b}:
                self._handleCollision(player, l, r, t, b)

    def _wallProjectileDetection(self, projectiles, walls):
        for wall in walls:
            for projectile in projectiles:
                # Skip precise collision math if objects are far apart. Didn't seem to help much though.
                #if not abs(projectile.center_x + projectile.change_x - wall.center_x + wall.change_x) >= wall._get_width() or not abs(projectile.center_y + projectile.change_y - wall.center_y + wall.change_y) >= wall._get_width():
                if self.proxCheck(projectile, wall):
                    l, r, t, b = self._detectCollision(projectile, wall)
                    if True in {l, r, t, b}:
                        projectile.reflect(projectiles, l, r, t, b)

    def _enemyPlayerDetection(self, player, enemies):
        for enemy in enemies:
            l, r, t, b = self._detectCollision(enemy, player)
            if True in {l, r, t, b}:
                self._handleCollision(enemy, l, r, t, b)

    def _handleCollision(self, entity, l, r, t, b):
        if not False in {l, r, t, b}:
                entity.center_x += entity.change_x * -1
                entity.center_y += entity.change_y * -1
        if l:
            entity.change_x = max(entity.change_x, 0) # Stop leftward movement
        if r:
            entity.change_x = min(entity.change_x, 0) # Stop rightward movement
        if b:
            entity.change_y = max(entity.change_y, 0) # Stop downward movement
        if t:
            entity.change_y = min(entity.change_y, 0) # Stop updward movement
        return
            
    def _detectCollision(self, entity1, entity2, factorChange=0):
        __left = __right = __top = __bottom = False
        if self.bottomBound(entity2) - self.bottomBound(entity1) > entity1._get_height() + entity2._get_height():
            return __left, __right, __top, __bottom
        if ((self.bottomBound(entity2) <= self.topBound(entity1) and self.topBound(entity1) <= self.topBound(entity2)) or (self.bottomBound(entity2) <= self.bottomBound(entity1) and self.bottomBound(entity1) <= self.topBound(entity2))) and ((self.leftBound(entity1, 1) <= self.rightBound(entity2, 1) and self.rightBound(entity1, factorChange) >= self.leftBound(entity2, factorChange))):
            __left = True
        if ((self.bottomBound(entity2) <= self.topBound(entity1) and self.topBound(entity1) <= self.topBound(entity2)) or (self.bottomBound(entity2) <= self.bottomBound(entity1) and self.bottomBound(entity1) <= self.topBound(entity2))) and ((self.leftBound(entity2, 1) <= self.rightBound(entity1, 1) and self.rightBound(entity2, factorChange) >= self.leftBound(entity1, factorChange))):
            __right = True
        if ((self.leftBound(entity2) <= self.rightBound(entity1) and self.rightBound(entity1) <= self.rightBound(entity2)) or (self.leftBound(entity2) <= self.leftBound(entity1) and self.leftBound(entity1) <= self.rightBound(entity2))) and ((self.bottomBound(entity1, 1) <= self.topBound(entity2, 1) and self.topBound(entity1, factorChange) >= self.bottomBound(entity2, factorChange))):
            __bottom = True
        if ((self.leftBound(entity2) <= self.rightBound(entity1) and self.rightBound(entity1) <= self.rightBound(entity2)) or (self.leftBound(entity2) <= self.leftBound(entity1) and self.leftBound(entity1) <= self.rightBound(entity2))) and ((self.bottomBound(entity2, 1) <= self.topBound(entity1, 1) and self.topBound(entity2, factorChange) >= self.bottomBound(entity1, factorChange))):
            __top = True
        return __left, __right, __top, __bottom

    def proxCheck(self, entity1, entity2):
        return not abs(entity1.center_x + entity1.change_x - entity2.center_x + entity2.change_x) >= entity2._get_width() or not abs(entity1.center_y + entity1.change_y - entity2.center_y + entity2.change_y) >= entity2._get_width()

    def rightBound(self, entity, factorChange=0):
        return entity.center_x + (entity.change_x * factorChange) + (entity._get_width() / 2) 
    def leftBound(self, entity, factorChange=0):
        return entity.center_x + (entity.change_x * factorChange) - (entity._get_width() / 2) 
    def topBound(self, entity, factorChange=0):
        return entity.center_y + (entity.change_y * factorChange) + (entity._get_height() / 2) 
    def bottomBound(self, entity, factorChange=0):
        return entity.center_y + (entity.change_y * factorChange) - (entity._get_height() / 2) 