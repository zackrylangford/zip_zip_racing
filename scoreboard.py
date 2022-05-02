import pygame.font

from pygame.sprite import Group

from scooter import Scooter


class Scoreboard: 
    """A class to report scoring information."""

    def __init__(self, zz_game):
        """Initialize scorekeeping attributes."""
        self.zz_game = zz_game
        self.screen = zz_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = zz_game.settings
        self.stats = zz_game.stats

    # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

    # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_scooters()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = self.stats.score
        score_str = "{:,}".format(rounded_score)
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.settings.bg_color)
    # Display the score at the top right of the screen. 
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 200
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.settings.bg_color)

    # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw score and level and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.scooters.draw(self.screen)


    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, 
            self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_scooters(self):
        """Show how many scooters are left."""
        self.scooters = Group()
        for scooter_number in range(self.stats.scooters_left):
            scooter = Scooter(self.zz_game)
            scooter.rect.x = 10 + scooter_number * scooter.rect.width
            scooter.rect.y = 10
            self.scooters.add(scooter)


