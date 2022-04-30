from random import randint


class Settings:
    """A class to store settings for Zack's game."""

    def __init__(self):
        """Initialize the games static settings."""
           
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (38, 58, 71)

        # Scooter settings
        self.scooter_speed = 3
        self.scooter_limit = 3


        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 20
        self.bullet_height = 8
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 2

        # Asteroid settings
        self.asteroid_speed = 1.1
        self.amount_asteroids_level = 10 



