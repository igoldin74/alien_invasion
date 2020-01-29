import sys
import pygame.base
from bullet import Bullet


def check_for_events(ai_settings, screen, ship, bullets):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        # Watch for KB and mouse events.
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def check_key_down_events(event, ai_settings, screen, ship, bullets):
    """Respond to key press event."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_key_up_events(event, ship):
    """Respond to key release event."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    # Redraw screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # It is important to call ship blitme() after we fill the background, so it appears on top of it.
    ship.blitme()
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    bullets.update()
    # get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
