from settings import Settings
from spaceship import Spaceship
import game_functions as gf
import pygame
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
# contains the functionality needed to make a game


def run_game():
    """Initialize game and create a screen object"""
    pygame.init()

    # Initialize the settings
    settings = Settings(1.5)

    # Initialize the game statistics
    stats = GameStats(settings)

    game_screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Attack")

    # Make the Play button
    play_button = Button(settings, game_screen, "Play")

    # Initialize the spaceship
    spaceship = Spaceship(game_screen, settings)

    # Play the background music
    pygame.mixer.music.load("background_music.mp3")
    # Set volume from zero to one
    pygame.mixer.music.set_volume(0.5)
    # endless loop
    pygame.mixer.music.play(-1)

    # Make a group to store bullets in
    # list but with extra functionality
    bullets = Group()

    # Initialize alien fleet then update it
    aliens = Group()
    gf.create_fleet(settings, game_screen, aliens, spaceship)

    # Initialize the scoreboard
    scoreboard = Scoreboard(settings, game_screen, stats)

    # Beginning of the main loop that starts the game
    while True:
        # Handling of keyboard and mouse events
        gf.check_events(settings, spaceship, bullets, game_screen, stats, play_button,
                        aliens, scoreboard)
        if stats.game_active:
            # Updating ship position after checking key events
            spaceship.update()
            # Update bullet positions(update() call on elements)
            bullets.update()
            # Getting rid of bullets outside of game screen
            gf.update_bullets(settings, game_screen, spaceship, bullets, aliens, stats,
                              scoreboard)
            # Update the positions of the aliens
            gf.update_aliens(aliens, settings, spaceship, bullets, stats, game_screen, scoreboard)

        # Updating screen
        gf.update_screen(game_screen, spaceship, settings, bullets,
                         aliens, play_button, stats, scoreboard)


run_game()
