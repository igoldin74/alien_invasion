import sys
import pygame.base


def check_for_events():
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        # Watch for KB and mouse events.
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    # Redraw screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # It is important to call ship blitme() after we fill the background, so it appears on top of it.
    ship.blitme()
    # Make the most recently drawn screen visible.
    pygame.display.flip()
