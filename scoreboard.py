import pygame.font
from spaceship import Spaceship
from pygame.sprite import Group
class Scoreboard:
    """Represent the score of the player"""

    def __init__(self, settings, screen, stats):
        """Initialize the attributes of the scoreboard"""
        self.settings = settings
        self.screen = screen
        self.stats = stats

        # Font settings for scoreboard
        self.text_color =(30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the image as initial score
        self.prep_score()
        # Prepare the image as high score
        self.prep_high_score()
        # Prepare the image as a level
        self.prep_current_level()
        # Prepare the group of ships as omages
        self.prep_ships()

    def prep_ships(self):
        """Turn the lives left into ships"""
        self.ships = Group()
        for ship_number in range(self.stats.num_lives):
            life = Spaceship(self.screen, self.settings)
            life.rect.y = self.level_rect.y + 50
            life.rect.x = self.level_rect.x + ship_number * life.rect.width
            self.ships.add(life)

    def prep_score(self):
        """Turn the score into a image"""
        # round score to the nearest ten
        rounded_score = int(round(self.stats.score, -1))
        score = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score, True, self.text_color,
                                            self.settings.background_color)

        # Show the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen.get_rect().right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Render the high score as a image"""
        high_score = "{:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(high_score, True, self.text_color,
                                                 self.settings.background_color)
        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.top = self.score_rect.top
        self.high_score_rect.centerx = self.screen.get_rect().centerx

    def prep_current_level(self):
        """Display the current level as a image"""
        level_string = str(self.stats.current_level)
        self.level_image = self.font.render(level_string, True, self.text_color,
                                            self.settings.background_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen.get_rect().left + 20
        self.level_rect.top = self.score_rect.top

    def display_score(self):
        """Display the score on screen"""
        # loads score to the
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)