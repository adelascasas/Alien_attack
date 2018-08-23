import pygame
from pygame.sprite import Sprite


class Spaceship(Sprite):
    """Specifications of the ship used in the game"""

    def __init__(self, screen, settings):
        """Initialize the ship and set staring position"""
        super(Spaceship, self).__init__()
        self.screen = screen
        self.settings = settings

        # determine if the ship is moving right or left
        self.moving_right = False
        self.moving_left = False

        # load the image and set the starting position
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set the spaceship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # ship's center that will be able to take decimals
        self.center = float(self.rect.centerx)

    def blitme(self):
        """Draw the ship at the specified position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the position of the spaceship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_rate
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_rate
        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx
