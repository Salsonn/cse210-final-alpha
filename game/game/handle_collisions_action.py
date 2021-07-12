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

    def execute(self, entities, reticle):
        """Executes the action using the given actors.

        Args:
            entities (dict): The game actors {key: tag, value: list}.
        """
        self._screenEdgeDetection(entities["player"][0], entities["projectile"])
        if entities["player"][0].change_x or entities["player"][0].change_y: 
            self._wallPlayerDetection(entities["player"][0], entities["projectile"], entities["wall"])
        self._wallProjectileDetection(entities["projectile"], entities["wall"])

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
            if not False in {l, r, t, b}:
                player.center_x += player.change_x * -1
                player.center_y += player.change_y * -1
            if l:
                player.change_x = max(player.change_x, 0) # Stop leftward movement
                if constants.collisionDebug:
                    print("Player cannot move left")
            if r:
                player.change_x = min(player.change_x, 0) # Stop rightward movement
                if constants.collisionDebug:
                    print("Player cannot move right")
            if b:
                player.change_y = max(player.change_y, 0) # Stop downward movement
                if constants.collisionDebug:
                    print("Player cannot move down")
            if t:
                player.change_y = min(player.change_y, 0) # Stop updward movement
                if constants.collisionDebug:
                    print("Player cannot move up")

    def _wallProjectileDetection(self, projectiles, walls):
        for wall in walls:
            for projectile in projectiles:
                # Skip precise collision math if objects are far apart. Didn't seem to help much though.
                if not abs(projectile.center_x + projectile.change_x - wall.center_x + wall.change_x) >= wall._get_width() or not abs(projectile.center_y + projectile.change_y - wall.center_y + wall.change_y) >= wall._get_width():
                    l, r, t, b = self._detectCollision(projectile, wall)
                    if True in {l, r, t, b}:
                        projectile.reflect(projectiles, l, r, t, b)
                    
            
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


    def rightBound(self, entity, factorChange=0):
        return entity.center_x + (entity.change_x * factorChange) + (entity._get_width() / 2) 
    def leftBound(self, entity, factorChange=0):
        return entity.center_x + (entity.change_x * factorChange) - (entity._get_width() / 2) 
    def topBound(self, entity, factorChange=0):
        return entity.center_y + (entity.change_y * factorChange) + (entity._get_height() / 2) 
    def bottomBound(self, entity, factorChange=0):
        return entity.center_y + (entity.change_y * factorChange) - (entity._get_height() / 2) 