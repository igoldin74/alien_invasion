import game_functions as gf
import pygame.base
from settings import Settings
from ship import Ship
from unicorn_ship import UnicornShip


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    # Start the main loop for the game.
    while True:
        gf.check_for_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()


