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
        self.scooter_limit = 3
        self.scooter_speed = 2


        # Bullet settings
        self.bullet_width = 20
        self.bullet_height = 20
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 2

        # Asteroid settings
        self.amount_asteroids_level = 4

        # Star settings
        self.amount_stars_level = 30


        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # How quickly the point values increase
        self.score_scale = 1.5
        

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.bullet_speed = 3
        self.asteroid_speed = 1.1
        self.star_speed = 1

        # Scoring
        self.star_points = 50 
        self.asteroid_points = 200

    def increase_speed(self):
        """Increase speed settings and point values."""
        self.bullet_speed *= self.speedup_scale
        self.asteroid_speed *= self.speedup_scale
        self.star_speed *= self.speedup_scale
        self.star_points = int(self.star_points * self.score_scale)
        self.asteroid_points = int(self.asteroid_points * self.score_scale)

        








