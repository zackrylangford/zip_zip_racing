from random import randint, randrange
import pygame

from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star in sky."""

    def __init__(self, zz_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = zz_game.screen
        self.settings = zz_game.settings

        # Load the star image and set its rect attribute
        self.image = pygame.image.load('images/yellowstar.bmp')
        self.rect = self.image.get_rect()



    def update(self):
        self.rect.x -= float(self.settings.star_speed)

        # If it goes off the left, move it back to the right.
        if self.rect.x < -500:
            self.rect.x = randint(2550,5000)

    def draw_stars(self):
        """Draw the stars to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
