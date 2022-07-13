from game.casting.actor import Actor
from game.shared.point import Point


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self,num):
        super().__init__()
        self.player_num = num
        self.position = Point(15,0)
        self._points = 0
        self.add_points(0)
        if num == 2:
            self.position = Point(760,0)

    def set_player_num(self,num):
        '''Sets the player's number
        
        Args:
            num: the number of the player (one or two)
        '''
        self.player_num = num

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Player {self.player_num} score: {self._points}")

    def subtract_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points -= points
        self.set_text(f"Player {self.player_num} score: {self._points}")

    def get_points(self):
        '''Returns the current number of points of said player'''
        return self._points

    def get_position(self):
        return self.position