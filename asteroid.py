from random import randint, randrange
import pygame

from pygame.sprite import Sprite

class Asteroid(Sprite):
    """A class to represent a single asteroid in belt."""

    def __init__(self, zz_game):
        """Initialize the asteroid and set its starting position."""
        super().__init__()
        self.screen = zz_game.screen
        self.settings = zz_game.settings


        # Load the asteroid image and set its rect attribute
        self.image = pygame.image.load('images/asteroid.bmp')
        self.rect = self.image.get_rect()

        # Start each new asteroid at a random height, slightly off screen
        self.rect.x = 2550
        self.rect.y = randint (25,1200)

        # Store the asteroid's exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the asteroid to the left"""
        self.x -= self.settings.asteroid_speed
        self.rect.x = self.x



