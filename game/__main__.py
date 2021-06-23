import random
import arcade

from game import constants

from game.director import Director
from game.entity import Entity
from game.point import Point
from game.controls import controls
from game.draw_actors_action import DrawActorsAction
#from game.handle_collisions_action import HandleCollisionsAction
#from game.move_actors_action import MoveActorsAction
from game.physics import Physics
from game.input_service import InputService
from game.output_service import OutputService

def main(screen):

    # create the entities {key: tag, value: list}
    entities = {}

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 1)
    position = Point(x, y)
    paddle = Entity()
    paddle.set_text("===========")
    paddle.set_position(position)
    entities["paddle"] = [paddle]

    entities["brick"] = []
    for x in range(5, 75):
        for y in range(2, 6):
            position = Point(x, y)
            brick = Entity()
            brick.set_text("*")
            brick.set_position(position)
            entities["brick"].append(brick)

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    velocity = Point(1, -1)
    ball = Entity()
    ball.set_text("@")
    ball.set_position(position)
    ball.set_velocity(velocity)
    entities["ball"] = [ball]
    
    # create the script {key: tag, value: list}
    script = {}

    physics = Physics

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()
    
    playerControls = controls(input_service)
    moveTick = physics.moveTick()
    physicsTick = physics.physicsTick()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [playerControls]
    script["update"] = [moveTick, physicsTick]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(entities, script)
    director.setup()
    arcade.run()

if __name__ == "__main__":
    main()