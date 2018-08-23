import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Represent the bullet in the game"""

    def __init__(self, settings, screen, ship):
        """Create a bullet at the position of the ship"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Setting the position of the Bullet by creating rect
        # Not based on image need to create  a rect from scratch
        self.rect = pygame.Rect(0, 0, settings.bullet_width,
                                settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Storing bullet position (decimal value)
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Display a bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

