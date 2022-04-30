import pygame
 
class Scooter:
    """A class to manage the ship."""
 
    def __init__(self, zz_game):
        """Initialize the scooter and set its starting position."""
        self.screen = zz_game.screen
        self.settings = zz_game.settings
        self.screen_rect = zz_game.screen.get_rect()

        # Load the scooter image and get its rect.
        self.image = pygame.image.load('images/scooterupdate.bmp')
        self.rect = self.image.get_rect()

        # Start each new scooter at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Store a decimal value for the ship's vertical position
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the ships position based on the movement flags."""
        # Update the scooter's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.scooter_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.scooter_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.scooter_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.scooter_speed


        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the scooter at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_scooter(self):
        """Center  the ship on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)



