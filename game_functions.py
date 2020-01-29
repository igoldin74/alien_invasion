import sys
import pygame.base


def check_for_events(ship):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        # Watch for KB and mouse events.
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def check_key_down_events(event, ship):
    """Respond to key press event."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_key_up_events(event, ship):
    """Respond to key release evnt."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    # Redraw screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # It is important to call ship blitme() after we fill the background, so it appears on top of it.
    ship.blitme()
    # Make the most recently drawn screen visible.
    pygame.display.flip()
