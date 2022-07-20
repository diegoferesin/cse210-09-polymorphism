from game.scripting.action import Action
from game.casting.badfood import badFood


class TimedActions(Action):
    """
    An update action that moves all the actors.

    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """
    def __init__(self):
        self._level = 1


    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._level +=1
        badfood_counter = len(cast.get_actors("badfoods"))
        if badfood_counter < self._level:
            cast.add_actor("badfoods", badFood())

    def get_level(self):
        
        return self._level
        
            