import pygame.base


class Ship:
    def __init__(self, screen):
        """Init the ship and set its start position."""
        self.screen = screen
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp').convert()
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.image.set_colorkey((230, 230, 230))

        # Start each new ship at the bottom center of the screen.
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.image_rect.centerx += 1
        if self.moving_left:
            self.image_rect.centerx -= 1


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.image_rect)
