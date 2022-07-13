from game.scripting.action import Action
from game.scripting.handle_collisions_action import HandleCollisionsAction


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
        handle = HandleCollisionsAction()
        snakes = cast.get_actors("snakes")
        scores = cast.get_actors("scores")
        if not handle._is_game_over:
            for snake in snakes:
                snake.grow_tail(1)
                print(handle._is_game_over)
            for score in scores:
                score.add_points(1)
        elif handle._is_game_over:
            for snake in snakes:
                snake.grow_tail2(1)
                print(handle._is_game_over)
            for score in scores:
                score.add_points(1)
        
            