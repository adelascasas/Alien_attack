class GameStats:
    """Represent player history in game"""

    def __init__(self, settings):
        """Initialize the stats"""
        self.settings = settings
        self.reset()
        # state of the game in the beginning is inactive
        self.game_active = False
        # reinitialize the high score
        self.high_score = 0
        # initialize current level
        self.current_level = 1

    def reset(self):
        """Initialize the limited number of lives"""
        self.num_lives = self.settings.max_lives
        self.score = 0
        self.current_level = 0

