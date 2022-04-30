from random import randint, randrange
import pygame

from pygame.sprite import Sprite

class Asteroid(Sprite):
    """A class to represent a single asteroid in sky."""

    def __init__(self, zz_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = zz_game.screen
        self.settings = zz_game.settings

        # Load the star image and set its rect attribute
        self.image = pygame.image.load('images/asteroid.bmp')
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.x -= 2


    def draw_stars(self):
        """Draw the asteroids to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)



