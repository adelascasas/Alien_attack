import sys
import pygame
from bullet import Bullet
from alien import Alien
# for pausing effect
from time import sleep


def check_events(settings, ship, bullets, screen, stats, play_button, aliens, sb):
    """Check for events when the game is played"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            handle_keydown_event(event, ship, settings, bullets, screen)
        elif event.type == pygame.KEYUP:
            handle_keyup_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = pygame.mouse.get_pos()
            check_button(stats, play_button, click_x, click_y, aliens, bullets, ship,
                         settings, screen, sb)


def check_button(stats, play_button, click_x, click_y, aliens, bullets, ship, settings, screen,
                 sb):
    """Check if start button has been pressed and start new game"""
    if play_button.rect.collidepoint(click_x, click_y) and not stats.game_active:
        # Make the mouse cursor invisible
        pygame.mouse.set_visible(False)

        # Reset the game stats
        stats.game_active = True
        stats.reset()

        # Display current scores
        sb.prep_score()
        sb.prep_current_level()
        sb.prep_high_score()
        sb.prep_ships()

        # Empty the aliens and bullets groups
        aliens.empty()
        bullets.empty()

        # Reinitialize dynamic settings
        settings.initialize_dynamic_settings()

        # center ship and create new fleet
        create_fleet(settings, screen, aliens, ship)
        ship.center_ship()


def update_screen(game_screen, spaceship, settings, bullets, aliens, play_button, stats,
                  scoreboard):
    """Screen updated with rgb color and ship position"""
    # Screen will be redrawn with rgb color
    game_screen.fill(settings.background_color)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Set the spaceship at its updated position
    spaceship.blitme()
    # Make a aliens appear with group method draw
    aliens.draw(game_screen)

    # Update the scoreboard
    scoreboard.display_score()

    # show play button if game is not active
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible
    pygame.display.flip()


def handle_keydown_event(event, ship, settings, bullets, screen):
    """Deal with KEYDOWN events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < settings.max_bullets:
            # Create a new bullet and add to Group
            fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def handle_keyup_event(event, ship):
    """Deal with KEYUP events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_bullets(settings, screen, ship, bullets, aliens, stats, sb):
    """Get rid of the bullets outside the screen"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_collisions(settings, screen, ship, aliens, bullets, stats, sb)


def check_collisions(settings, screen, ship, aliens, bullets, stats, sb):
    # adds key-value pairs of Bullet and Alien instances after collision
    # collision - overlap of rects
    # Boolean values tell if objects should be destroyed
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(settings, screen, aliens, ship)
        settings.increase_game_speed()
        stats.current_level += 1
        sb.prep_current_level()
    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alien_score * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)


def check_high_score(stats, sb):
    """Check to see if the current score is greater than the high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()



def fire_bullet(settings, screen, ship, bullets):
    """Create a Bullet and add it to group"""
    new_bullet = Bullet(settings, screen, ship)
    bullets.add(new_bullet)


def get_number_aliens_x(screen, settings):
    """Obtain the max amount of aliens in a row"""
    alien = Alien(screen, settings)
    alien_width = alien.rect.width
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(screen, settings, aliens, alien_number, row_number):
    """Create a alien and add it to group"""
    alien = Alien(screen, settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(settings, screen, aliens, ship):
    """Create a fleet of aliens by adding to group"""
    number_aliens_x = get_number_aliens_x(screen, settings)
    number_rows = get_number_rows(settings, screen, ship)
    # Create a fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Creating and then adding to a row
            create_alien(screen, settings, aliens, alien_number, row_number)


def get_number_rows(settings, screen, ship):
    """Obtain the number of rows for fleet"""
    alien = Alien(screen, settings)
    available_space_y = settings.screen_height - 3 * alien.rect.height - ship.rect.height
    number_rows = int(available_space_y/(2*alien.rect.height))
    return number_rows


def update_aliens(aliens, settings, ship, bullets, stats, screen, sb):
    """Update the aliens into their new position"""
    check_fleet_edges(aliens, settings)
    aliens.update()
    # returns the alien instance after collision
    # else returns None
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_collision(settings, screen, aliens, bullets, ship, stats, sb)
    aliens_reach_bottom(settings, screen, aliens, bullets, ship, stats, sb)


def aliens_reach_bottom(settings, screen, aliens, bullets, ship, stats, sb):
    """When aliens reach end of screen a game life is lost"""
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen.get_rect().bottom:
            ship_collision(settings, screen, aliens, bullets, ship, stats, sb)
            break


def check_fleet_edges(aliens, settings):
    """Check to see it any of the aliens have reached the edge"""
    for alien in aliens.sprites():
        if alien.reached_edges():
            change_fleet_direction(aliens, settings)
            break


def change_fleet_direction(aliens, settings):
    """Change the direction of the fleet after dropping"""
    for alien in aliens.sprites():
        alien.rect.y += settings.aliens_drop_speed
    settings.aliens_speed_direction *= -1


def ship_collision(settings, screen, aliens, bullets, ship, stats, sb):
    """What happens when a alien hits the ship"""
    if stats.num_lives > 0:
        # destroy all existing aliens and bullets
        bullets.empty()
        aliens.empty()

        # decrease the lives of the player by one
        stats.num_lives -= 1

        # Display the remaining amount of lives
        sb.prep_ships()

        # create a new fleet
        create_fleet(settings, screen, aliens, ship)

        # reposition the ship to the center
        ship.center_ship()

        # A pause
        sleep(0.5)
    else:
        pygame.mouse.set_visible(True)
        stats.game_active = False

