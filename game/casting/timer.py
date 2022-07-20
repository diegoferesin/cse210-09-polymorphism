from game.casting.actor import Actor
from game.shared.point import Point



class Timer(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self.position = Point(400,0)
        self._time = 0

    def add_time(self, time):
            """Adds the given points to the score's total points.
            
            Args:
                points (int): The points to add.
            """
            self._time += time
            self.set_text(f"Timer: {self._time}")

    def set_time(self, time):
        """Set time for the timer."""

        self._timer = time
        self.set_text(f"Timer {self._timer:.0f}")


    def get_time(self):
        '''Returns the current number of points of said player'''
        return self._timer


    def get_position(self):
        return self.position

