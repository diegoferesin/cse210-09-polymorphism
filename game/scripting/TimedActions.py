from asyncio import constants
import constants
from game.scripting.action import Action
from game.casting.badfood import badFood
from game.services.audio_service import AudioService


class TimedActions(Action):
    """
    An update action that moves all the actors.

    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """
    def __init__(self):
        self._level = 1
        self._audio_service = AudioService()


    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._audio_service.playsound(constants.LEVEL_UP)    
        self._level +=1
        badfood_counter = len(cast.get_actors("badfoods"))
        if badfood_counter < self._level:
            cast.add_actor("badfoods", badFood())
        
        if self._level == 10 or self._level == 20 or self._level == 30:
            self._audio_service.playsound(constants.WARNING)    


    def get_level(self):
        
        return self._level

        
            