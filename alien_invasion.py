import game_functions as gf
import pygame.base
from settings import Settings
from ship import Ship
from unicorn_ship import UnicornShip
from pygame.sprite import Group


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_settings)
    # Make a group to store bullets in
    bullets = Group()
    # Start the main loop for the game.
    while True:
        gf.check_for_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
