import random
from game import constants
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService
from game.reticle import Reticle

from game.entity.player import Player

from game.director import Director
import arcade

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    player = Player()
    cast["player"] = [player]

    # create empty list of projectiles, will be filled automatically later
    cast["projectile"] = []

    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()

    reticle = Reticle()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [handle_collisions_action, move_actors_action]
    script["output"] = [draw_actors_action]

    # start the game
    batter = Director(cast, script, input_service, reticle)
    batter.setup()
    arcade.run()


if __name__ == "__main__":
    main()