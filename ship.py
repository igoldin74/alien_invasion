import pygame.base


class Ship:
    def __init__(self, screen, ai_settings):
        """Init the ship and set its start position."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp').convert()
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.image.set_colorkey((230, 230, 230))

        # Start each new ship at the bottom center of the screen.
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom
        self.ship_center = float(self.image_rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.ship_center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.image_rect.left > 0:
            self.ship_center -= self.ai_settings.ship_speed_factor
        self.image_rect.centerx = self.ship_center


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.image_rect)
