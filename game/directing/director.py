class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self.timer = 0
        
    def start_game(self, cast, script):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            if self._video_service.get_time() - self.timer > 1:
                self.timer = self._video_service.get_time()
                self._execute_actions("timed_update", cast, script)
            self._execute_actions("output", cast, script)
            if self._video_service.get_time() > 10:
                self._video_service.close_window()
                self.second_level(cast,script)
        self._video_service.close_window()

    def second_level(self,cast,script):
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            if self._video_service.get_time() - self.timer > 1:
                self.timer = self._video_service.get_time()
                self._execute_actions("timed_update", cast, script)
            self._execute_actions("output", cast, script)
        self._video_service.close_window()
        if self._video_service.get_time() > 10:
                self._video_service.close_window()
                self.third_level(cast,script)
        self._video_service.close_window()

    def third_level(self,cast,script):
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            if self._video_service.get_time() - self.timer > 1:
                self.timer = self._video_service.get_time()
                self._execute_actions("timed_update", cast, script)
            self._execute_actions("output", cast, script)
        if self._video_service.get_time() > 10:
                self._video_service.close_window()
        self._video_service.close_window()

    def _execute_actions(self, group, cast, script):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = script.get_actions(group)    
        for action in actions:
            action.execute(cast, script)          