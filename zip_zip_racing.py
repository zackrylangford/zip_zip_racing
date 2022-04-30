import sys
from time import sleep

import pygame

from settings import Settings

from game_stats import GameStats

from scooter import Scooter

from bullet import Bullet

from star import Star

from asteroid import Asteroid

from random import randint

class ZipZipRacing:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Zip Zip Racing")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        self.star = Star(self)

        self.scooter = Scooter(self)
        self.bullets = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self._create_belt()
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.scooter.update()
            self.star.update()
            self._update_bullets()
            self._update_asteroids()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.scooter.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.scooter.moving_left = True
        elif event.key == pygame.K_UP:
            self.scooter.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.scooter.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self,event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.scooter.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.scooter.moving_left = False
        elif event.key == pygame.K_UP:
            self.scooter.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.scooter.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:    
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared. 
        for bullet in self.bullets.copy():
            if bullet.rect.x >= self.settings.screen_width:
                self.bullets.remove(bullet)

        # Check for bullets that have hit asteroids
        # If so, get rid of the bullet and the asteroid.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.asteroids, True, True) 

    def _update_asteroids(self):
        """Update the positions of the asteroids in the belt."""
        self.asteroids.update()
        # Get rid of asteroids that go off the screen 
        for asteroid in self.asteroids.copy():
            if asteroid.rect.x <= -5:
                self.asteroids.remove(asteroid)
        if not self.asteroids:
        # Create a new asteroid and send it
            self._create_belt()

        # Decrement amount of asteroids left in level
        self.stats.asteroids_left -= 1

        if pygame.sprite.spritecollideany(self.scooter, self.asteroids):
            self._scooter_hit()

    def _create_belt(self):
        """Create a belt of asteroids."""
        # Make an asteroid.
        asteroid = Asteroid(self)
        asteroid.x = 2550
        asteroid.rect.x = asteroid.x
        asteroid.rect.y = randint (25,1200)
        self.asteroids.add(asteroid)
        self.asteroids.update()

    def _scooter_hit(self):
        """Respond to the ship being hit by an alien."""

        # Decrement scooters_left.
        self.stats.scooters_left -= 1

        # Get rid of any remaining aliens and bullets.
        self.asteroids.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship.
        self._create_belt()
        self.scooter.center_scooter()

        # Pause
        sleep(0.5)

     



 


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.scooter.blitme()
        self.star.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullets()
        self.asteroids.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    zz = ZipZipRacing()
    zz.run_game()
