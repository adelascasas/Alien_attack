class Settings:
    """Used to store all the settings of the game"""

    def __init__(self, ship_speed_rate):
        """All the settings are initialized"""
        self.screen_width = 1200
        self.screen_height = 600
        self.background_color = (255, 255, 255)

        # All the ship non-dynamic attributes
        self.max_lives = 3

        # All the attributes of the bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.max_bullets = 3

        # settings for aliens
        self.aliens_drop_speed = 10

        # Speed of the game
        self.speedup_game = 1.1

        # Increase the points per alien
        self.score_increase = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the settings that can be changed midgame"""
        # ship dynamic speed
        self.ship_speed_rate = 1.5
        # Bullet dynamic speed
        self.bullet_speed_factor = 3
        # Alien dynamic speed and direction
        self.aliens_speed_factor = 1
        self.aliens_speed_direction = 1
        # scoring of aliens
        self.alien_score = 50

    def increase_game_speed(self):
        """Increase the speed of all the factors of the game and points"""
        self.ship_speed_rate *= self.speedup_game
        self.aliens_speed_factor *= self.speedup_game
        self.bullet_speed_factor *= self.speedup_game

        # Increase the points given per alien
        self.alien_score = int(self.score_increase * self.alien_score)
