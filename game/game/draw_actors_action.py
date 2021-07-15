from game.maps.menu import MainMenu
from game.maps.welcome import Welcome
from game.maps.level1 import Level1

from game.action import Action
from game import constants

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service, entities):
        """The class constructor.
        
        Args:
            _output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service
        self.activeLevel = 0
        self._mainMenu = MainMenu(entities)
        self._welcome = Welcome(entities)
        self._level1 = Level1(entities)

    def execute(self, cast, reticle):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()

        #for ball in cast["balls"]:
        #    self._output_service.draw_actor(ball)

        if self.activeLevel == 0:
            self._mainMenu.drawMap()
        elif self.activeLevel == 1:
            self._welcome.drawMap()
        elif self.activeLevel == 2:
            self._level1.drawMap()

        player = cast["player"][0] # there's only one
        self._output_service.draw_actor(player)
        
        weapon = cast["weapon"][0]
        self._output_service.draw_actor(weapon)

        enemy = cast["enemy"][0]
        self._output_service.draw_actor(enemy)

        for projectile in cast["projectile"]:
            self._output_service.draw_actor(projectile)

        self._output_service.flush_buffer()

    def changeLevel(self, newLevel):
        if newLevel == 0:
            self._mainMenu.load()
        elif newLevel == 1:
            self._welcome.load()
        elif newLevel == 2:
            self._level1.load()

    def getLevel(self):
        return self.activeLevel