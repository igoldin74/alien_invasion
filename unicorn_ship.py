import pygame.base


class UnicornShip:
    def __init__(self, screen):
        """Init the ship and set its start position."""
        self.screen = screen
        # Load the ship image and get its rect.
        self.image = pygame.transform.rotozoom(pygame.image.load('images/unicorn_ship.bmp').convert(), 0, 0.4)
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.image.set_colorkey((255, 255, 255))  # this is to set hte given color as transparent

        # Start each new ship at the bottom center of the screen.
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.image_rect)
