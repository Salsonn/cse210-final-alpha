import random
import arcade

from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, reticle):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._edgeDetection(cast["player"][0], cast["projectile"])
        self._wallDetection(cast["player"][0], cast["projectile"], cast["wall"])

        """paddle = cast["paddle"][0]

        balls_to_remove = []

        for ball in cast["balls"]:
            self._handle_wall_bounce(ball)
            self._handle_paddle_bounce(ball, paddle)

            bricks = cast["bricks"]
            self._handle_brick_collision(ball, bricks)

            if constants.BALLS_CAN_DIE and self._is_off_screen(ball):
                balls_to_remove.append(ball)

        for ball in balls_to_remove:
            cast["balls"].remove(ball)"""

    def _edgeDetection(self, player, projectiles):
        # Prevent player from leaving sides of window
        if (player.center_x - (player._get_width() / 2)) <= 0 and player.change_x < 0:
            player.change_x = max(player.change_x, 0)
        if (player.center_x + (player._get_width() / 2)) >= constants.windowX and player.change_x > 0:
            player.change_x = min(player.change_x, 0)
        if (player.center_y - (player._get_height() / 2)) <= 0 and player.change_y < 0:
            player.change_y = max(player.change_y, 0)
        if (player.center_y + (player._get_height() / 2)) >= constants.windowY and player.change_y > 0:
            player.change_y = min(player.change_y, 0)

        for entity in projectiles:
            if (entity.center_x + (entity._get_width() / 2) <= 0 or entity.center_x + (entity._get_width() / 2) >= constants.windowX) or (entity.center_y + (entity._get_height() / 2) <= 0 or entity.center_y + (entity._get_height() / 2) >= constants.windowY):
                #projectiles[entity].remove_from_sprite_lists()
                projectiles.remove(entity)
                print("Removed a projectile")

    def _badwallDetection(self, player, projectiles, walls):
        collisionList = []
        for wall in walls:
            #if player.center_x - (player._get_width() / 2) == wall.center_x + (wall._get_width() / 2) or player.center_x + (player._get_width() / 2) == wall.center_x - (wall._get_width() / 2) or player.center_y - (player._get_height() / 2) == wall.center_y + (wall._get_height() / 2) or player.center_y + (player._get_height() / 2) == wall.center_y - (wall._get_height() / 2):
            if (player.center_x - (player._get_width() / 2) == wall.center_x + (wall._get_width() / 2) and player.center_y + (player._get_height() / 2) == wall.center_y - (wall._get_height() / 2)) or (player.center_y - (player._get_height() / 2) == wall.center_y + (wall._get_height() / 2) and player.center_x + (player._get_width() / 2) == wall.center_x - (wall._get_width() / 2)):
                collisionList.append(wall)
            if arcade.check_for_collision(player, wall):
                collisionList.append(wall)
        print(len(collisionList))
        for entity in collisionList:
            if entity.center_x < player.center_x:
                player.change_x = max(player.change_x, 0)
                print("collision detected from the left")
            if entity.center_x > player.center_x:
                player.change_x = min(player.change_x, 0)
                print("collision detected from the right")
            if entity.center_y < player.center_y:
                player.change_y = max(player.change_y, 0)
                print("collision detected from the top")
            if entity.center_y > player.center_y:
                player.change_y = min(player.change_y, 0)
                print("collision detected from the bottom")
        collisionList.clear()
    
    def _wallDetection(self, player, projectiles, walls):
        for entity in walls:
            if ((self.bottomBound(entity) <= self.topBound(player) and self.topBound(player) <= self.topBound(entity)) or (self.bottomBound(entity) <= self.bottomBound(player) and self.bottomBound(player) <= self.topBound(entity))) and (self.leftBound(player, 1) <= self.rightBound(entity, 1) and self.rightBound(player, 1) >= self.leftBound(entity, 1)):
                player.change_x = max(player.change_x, 0) # Stop leftward movement
            if ((self.bottomBound(entity) <= self.topBound(player) and self.topBound(player) <= self.topBound(entity)) or (self.bottomBound(entity) <= self.bottomBound(player) and self.bottomBound(player) <= self.topBound(entity))) and (self.leftBound(entity, 1) <= self.rightBound(player, 1) and self.rightBound(entity, 1) >= self.leftBound(player, 1)):
                player.change_x = min(player.change_x, 0) #, 1 Stop rightward movement
            if ((self.leftBound(entity) <= self.rightBound(player) and self.rightBound(player) <= self.rightBound(entity)) or (self.leftBound(entity) <= self.leftBound(player) and self.leftBound(player) <= self.rightBound(entity))) and (self.bottomBound(player, 1) <= self.topBound(entity, 1) and self.topBound(player, 1) >= self.bottomBound(entity, 1)):
                player.change_y = max(player.change_y, 0) # Stop downward movement
            if ((self.leftBound(entity) <= self.rightBound(player) and self.rightBound(player) <= self.rightBound(entity)) or (self.leftBound(entity) <= self.leftBound(player) and self.leftBound(player) <= self.rightBound(entity))) and (self.bottomBound(entity, 1) <= self.topBound(player, 1) and self.topBound(entity, 1) >= self.bottomBound(player, 1)):
                player.change_y = min(player.change_y, 0) # Stop updward movement
            


    def rightBound(self, entity, factorChange=0):
        return entity.center_x + (entity.change_x * factorChange) + (entity._get_width() / 2) 
    def leftBound(self, entity, factorChange=0):
        return entity.center_x + (entity.change_x * factorChange) - (entity._get_width() / 2) 
    def topBound(self, entity, factorChange=0):
        return entity.center_y + (entity.change_y * factorChange) + (entity._get_height() / 2) 
    def bottomBound(self, entity, factorChange=0):
        return entity.center_y + (entity.change_y * factorChange) - (entity._get_height() / 2) 


    def _handle_wall_bounce(self, ball):
        ball_x = ball.center_x
        ball_y = ball.center_y

        # Check for bounce on walls
        if ball_x <= 0 or ball_x >= constants.MAX_X:
            ball.bounce_vertical()

        if ball_y >= constants.MAX_Y:
            ball.bounce_horizontal()
        
        if not constants.BALLS_CAN_DIE and ball_y <= 0:
            ball.bounce_horizontal()
    
    def _handle_paddle_bounce(self, ball, paddle):
        # This makes use of the `Sprite` functionality
        if paddle.collides_with_sprite(ball):
            # Ball and paddle collide!
            ball.bounce_horizontal()

    def _handle_brick_collision(self, ball, bricks):
        brick_to_remove = None

        for brick in bricks:
            # This makes use of the `Sprite` functionality
            if ball.collides_with_sprite(brick):
                ball.bounce_horizontal()
                brick_to_remove = brick
        
        if brick_to_remove != None:
            bricks.remove(brick_to_remove)

    def _is_off_screen(self, ball):
        return ball.center_y < 0