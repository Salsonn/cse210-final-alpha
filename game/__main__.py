from game.director import Director
import random
from game import constants
from game.director import Director
from game.point import Point
from game.controls import PlayerControls
from game.draw_actors_action import DrawActorsAction
from game.physics import CollisionPhysics
from game.physics import MovementPhysics
# from game.move_actors_action import MoveActorsAction
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService
from game.entity.entity import Entity
from game.entity.player import Player
import arcade

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    player = Player()
    cast["player"] = [player]

    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()
    
    control_actors_action = PlayerControls(input_service)
    move_actors_action = MovementPhysics()
    handle_collisions_action = CollisionPhysics()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script, input_service)
    director.setup()
    arcade.run()


if __name__ == "__main__":
    main()