import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Represent the alien that are targeted in game"""

    def __init__(self, screen, settings):
        """Initialize all the alien attributes"""
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        # Load the image and set it to a starting position
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()

        # Position the alien at the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's new position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Moving the spaceship"""
        self.x += (self.settings.aliens_speed_factor *
                    self.settings.aliens_speed_direction)
        self.rect.x = self.x

    def reached_edges(self):
        """Return true if the alien has reached the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
