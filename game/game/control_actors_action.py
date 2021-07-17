from game.add_entity import add_entity
from game.reticle import Reticle
from game import constants
from game.action import Action
from game.math import *

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service
        self._coolDown = 0

    def execute(self, cast, reticle, current_level, script):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        impulse = self._input_service.get_direction().scale(constants.acceleration)
        player = cast["player"][0] # there's only one in the cast
        weapon = cast["weapon"][0]
        
        # x axis player movement (with acceleration and decelleration)
        if impulse.get_x() != 0:
            player.change_x = limit(player.change_x + impulse.get_x(), -1 * constants.movementSpeed, constants.movementSpeed)
        elif player.change_x > 0:
            player.change_x = min(player.change_x - 1, 0)
        elif player.change_x < 0:
            player.change_x = max(player.change_x + 1, 0)
        
        # y axis player movement (with acceleration and decelleration)
        if impulse.get_y() != 0:
            player.change_y = limit(player.change_y + impulse.get_y(), -1 * constants.movementSpeed, constants.movementSpeed)
        elif player.change_y > 0:
            player.change_y = min(player.change_y - 1, 0)
        elif player.change_y < 0:
            player.change_y = max(player.change_y + 1, 0)

        weapon.center_x = player.center_x
        weapon.center_y = player.center_y

        if self._input_service.check_click():
            # placeholder code for firing rate. Will need to be expanded upon late
            if self._coolDown % 10 == 0:
                add_entity(cast, "projectile", Point(player.center_x, player.center_y), theta(Point(player.center_x, player.center_y), reticle.get_reticle()))
            self._coolDown += 1


