from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.badfood import badFood
from game.casting.score import Score
from game.casting.snake import Snake
from game.casting.timer import Timer
from game.directing.director import Director
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.TimedActions import TimedActions
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.timeManager import TimeManager
from game.scripting.script import Script
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService



def main():
    

    # create de services
    keyboard_service = KeyboardService()
    video_service = VideoService()

    # create the cast
    cast = Cast()
    cast.add_actor("foods", Food())
    cast.add_actor("badfoods", badFood())
    

    cast.add_actor("snakes", Snake(1))
    cast.add_actor("scores", Score(1))
    cast.add_actor("timer", Timer())

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", TimeManager(video_service))
    script.add_action("timed_update", TimedActions())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()