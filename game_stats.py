class GameStats:
    """Track statistics for zip zip racing."""

    def __init__(self, zz_game):
        """Initialize statistics."""
        self.settings = zz_game.settings
        self.reset_stats()

        # Start game in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.scooters_left = self.settings.scooter_limit
        self.asteroids_left = self.settings.amount_asteroids_level
        self.score = 0 

        