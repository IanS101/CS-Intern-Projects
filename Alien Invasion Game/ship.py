import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.imager = pygame.image.load('images/ship_images/ship_right.png').convert_alpha()
        self.imagel = pygame.image.load('images/ship_images/ship_left.png').convert_alpha()
        self.images = pygame.image.load('images/ship_images/ship.png').convert_alpha()
        self.image = self.images

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        #movement flag
        self.moving_right = 0
        self.moving_left = 0
        self.speed = self.ai_settings.ship_speed_factor
        self.speed_increase_factor = self.ai_settings.ship_speed_increase_factor
        self.speed_increase = 0

    def update(self):
        """Update the ship's position based on the movement flag."""
        #update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.speed_increase += self.speed_increase_factor
            self.image = self.imager
            self.center += (self.speed + self.speed_increase)
        elif self.moving_left and self.rect.left > 0:
            self.speed_increase += self.speed_increase_factor
            self.image = self.imagel
            self.center -= (self.speed + self.speed_increase)
        else:
            self.image = self.images
        # Update rect object from self.center.
        self.rect.centerx = self.center


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)