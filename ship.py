import pygame.base


class Ship:
    def __init__(self, screen):
        """Init the ship and set its start position."""
        self.screen = screen
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.image_rect)
