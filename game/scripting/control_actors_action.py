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
        self._player1_direction = Point(constants.CELL_SIZE, 0)
        self._player2_direction = Point(constants.CELL_SIZE, 0)
        self.direction1 = "right"
        self.direction2 = "right"

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """


        snake = cast.get_first_actor("snakes")
        # left
        if self._keyboard_service.is_key_down('a'):
            self._player1_direction = Point(-constants.CELL_SIZE, 0)
            if self.direction1 != "left":
                self.direction1 = "left"
                snake.grow_tail(1)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._player1_direction = Point(constants.CELL_SIZE, 0)
            if self.direction1 != "right":
                self.direction1 = "right"
                snake.grow_tail(1)

        # up
        if self._keyboard_service.is_key_down('w'):
            self._player1_direction = Point(0, -constants.CELL_SIZE)
            if self.direction1 != "up":
                self.direction1 = "up"
                snake.grow_tail(1)

        # down
        if self._keyboard_service.is_key_down('s'):
            self._player1_direction = Point(0, constants.CELL_SIZE)
            if self.direction1 != "down":
                self.direction1 = "down"
                snake.grow_tail(1)


        snake2 = cast.get_second_actor("snakes")
        snake.turn_head(self._player1_direction)

        # left
        if self._keyboard_service.is_key_down('j'):
            self._player2_direction = Point(-constants.CELL_SIZE, 0)
            if self.direction2 != "left":
                self.direction2 = "left"            
                snake2.grow_tail(1)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._player2_direction = Point(constants.CELL_SIZE, 0)
            if self.direction2 != "right":
                self.direction2 = "right"            
                snake2.grow_tail(1)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._player2_direction = Point(0, -constants.CELL_SIZE)
            if self.direction2 != "up":
                self.direction2 = "up"            
                snake2.grow_tail(1)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._player2_direction = Point(0, constants.CELL_SIZE)
            if self.direction2 != "down":
                self.direction2 = "down"            
                snake2.grow_tail(1)
        

        snake2.turn_head(self._player2_direction)