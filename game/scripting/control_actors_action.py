from attr import s
import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._player1_direction = Point(0,-constants.CELL_SIZE)
        self._player2_direction = Point(0,-constants.CELL_SIZE)
        self.direction1 = "up"
        self.direction2 = "up"

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """


        snake = cast.get_first_actor("snakes")
        score = cast.get_first_actor("scores")
        # left
        if self._keyboard_service.is_key_down('a'):
            if self.direction1 != "right":
                self._player1_direction = Point(-constants.CELL_SIZE, 0)
                self.direction1 = "left"

        
        # right
        if self._keyboard_service.is_key_down('d'):
            if self.direction1 != "left":
                self._player1_direction = Point(constants.CELL_SIZE, 0)
                self.direction1 = "right"


        # up
        if self._keyboard_service.is_key_down('w'):
            if self.direction1 != "down":
                self._player1_direction = Point(0, -constants.CELL_SIZE)
                self.direction1 = "up"

        # down
        if self._keyboard_service.is_key_down('s'):
            if self.direction1 != "up":
                self._player1_direction = Point(0, constants.CELL_SIZE)
                self.direction1 = "down"


        snake2 = cast.get_second_actor("snakes")
        snake.turn_head(self._player1_direction)
        score2 = cast.get_second_actor("scores")

        # left
        if self._keyboard_service.is_key_down('j'):
            if self.direction2 != "right":
                self._player2_direction = Point(-constants.CELL_SIZE, 0)
                self.direction2 = "left"


        
        # right
        if self._keyboard_service.is_key_down('l'):
            if self.direction2 != "left":
                self._player2_direction = Point(constants.CELL_SIZE, 0)
                self.direction2 = "right"
                
        # up
        if self._keyboard_service.is_key_down('i'):
            if self.direction2 != "down":
                self._player2_direction = Point(0, -constants.CELL_SIZE)
                self.direction2 = "up"
        
        # down
        if self._keyboard_service.is_key_down('k'):
            if self.direction2 != "up":
                self._player2_direction = Point(0, constants.CELL_SIZE)
                self.direction2 = "down"
        

        snake2.turn_head(self._player2_direction)