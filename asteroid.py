import pygame
from pygame.sprite import Sprite

class Asteroid(Sprite):
    """A class to represent a single asteroid in belt."""

    def __init__(self, zz_game):
        """Initialize the asteroid and set its starting position."""
        super().__init__()
        self.screen = zz_game.screen
       

        # Load the asteroid image and set its rect attribute
        self.image = pygame.image.load('images/asteroid.bmp')
        self.rect = self.image.get_rect()

        # Start each new asteroid near the top left of the screen, slightly off screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the asteroid's exact horizontal position
        self.x = float(self.rect.x)

