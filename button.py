import pygame.font


class Button:
    """Representation of a button"""

    def __init__(self, settings, screen, msg):
        """Initializing button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # dimensions and properties of button
        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        # None argument tells Python to use default font
        # the number determines the size of the font
        self.font = pygame.font.SysFont(None, 48)

        # Build the button rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button message
        self.apply_msg(msg)

    def apply_msg(self, msg):
        """Renders msg as a image and center it on the button"""
        # font.render() turns text into a image
        # boolean value is for antialiasing(smooth edges)
        # arguments for font color and background color
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button and the msg"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
