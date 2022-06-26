from game.scripting.action import Action



class TimedActions(Action):
    """
    An update action that moves all the actors.

    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        snakes = cast.get_actors("snakes")
        scores = cast.get_actors("scores")
        for snake in snakes:
            snake.grow_tail(1)
        for score in scores:
            score.add_points(1)
        