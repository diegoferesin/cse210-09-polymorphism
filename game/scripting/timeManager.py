from game.scripting.action import Action


class TimeManager(Action):
    """
    An update action that moves all the actors.

    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """
    def __init__(self, video_service):
        self.video_service = video_service




    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        time = self.video_service.get_time()
        timer = cast.get_first_actor("timer")
        timer.set_time(time)
        

        
