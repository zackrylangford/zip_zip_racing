import sys
from time import sleep

import pygame

from settings import Settings

from game_stats import GameStats

from scoreboard import Scoreboard

from button import Button

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

        # Create an instance to store game statistics,
        # and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.scooter = Scooter(self)
        self.stars = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self._create_belt()
        self._create_sky()

        # Make the play button
        self.play_button = Button(self, "Click to Play")
    
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.scooter.update()
                self._update_stars()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings. 
            self.settings.initialize_dynamic_settings()
            self._start_game()


    def _start_game(self):
            # Reset the game statistics
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_scooters()

            # Get rid of remaining asteroids, stars, and bullets.
            self.asteroids.empty()
            self.bullets.empty()
            self.stars.empty()

            # Create a new fleet and center the scooter.
            self._create_sky()
            self._create_belt()
            self.scooter.center_scooter()

            # Hide mouse cursor
            pygame.mouse.set_visible(False)
        
      

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
        elif event.key == pygame.K_p:
            self.settings.initialize_dynamic_settings()
            self._start_game()
      


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

        self._check_bullet_star_collisions()
        self._check_bullet_asteroid_collisions()

    def _check_bullet_star_collisions(self):
        """Respond to bullet-alien collisions."""

        # Check for bullets that have hit stars
        # if so, get rid of bullet and star

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.stars, True, True
        )
        if collisions:
            for stars in collisions.values():
                self.stats.score += self.settings.star_points *len(stars)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.stars:
            # Destroy existing bullets and create new sky
            self.bullets.empty()
            self._create_sky()
            self._create_belt()
            self.settings.increase_speed()

            # Increase level. 
            self.stats.level += 1
            self.sb.prep_level()
    
    def _check_bullet_asteroid_collisions(self):

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.asteroids, True, True
        )
        if collisions:
            for asteroids in collisions.values():
                self.stats.score += self.settings.asteroid_points *len(asteroids)
            self.sb.prep_score()
            self.sb.check_high_score()



    def _update_stars(self):
        self.stars.update()

        # Look for scooter and star collisions.

        if pygame.sprite.spritecollideany(self.scooter, self.stars):
            self._scooter_hit()



    def _create_sky(self):
        """Create 10 stars and store them in a group"""
        number_stars = self.settings.amount_stars_level

        # Create stars at random intervals off the right of the screen and then send them back
        for star_number in range(number_stars):
            # Create the star
                star = Star(self)
                star.x = randint(2550,15000)
                star.rect.x = star.x
                star.y = randint (200,1250)
                star.rect.y = star.y
                self.stars.add(star)

    def _update_asteroids(self):
        self.asteroids.update()

        # If asteroid goes off the left, remove it
        for asteroid in self.asteroids.copy(): 
            if asteroid.rect.x < -500:
                self.asteroids.remove(asteroid)

        # Check for asteroid and scooter collisions
        
        if pygame.sprite.spritecollideany(self.scooter, self.asteroids):
            self._scooter_hit()

    
    def _create_belt(self):
        """Create 2 asteroids and store them in a group"""
        number_asteroids = self.settings.amount_asteroids_level

        # Create asteroids at random intervals off the right of the screen
        # and then send them back if they go off the left of screen
        for asteroid_number in range(number_asteroids):
            # Create the asteroid
                asteroid = Asteroid(self)
                asteroid.x = randint(2550,20000)
                asteroid.rect.x = asteroid.x
                asteroid.y = randint (200,1300)
                asteroid.rect.y = asteroid.y
                self.asteroids.add(asteroid)
 


  


    def _scooter_hit(self):
        """Respond to the ship being hit by an asteroid or star."""

        if self.stats.scooters_left > 0:

            # Decrement scooters_left and update scoreboard.
            self.stats.scooters_left -= 1
            self.sb.prep_scooters()

            # Get rid of any remaining asteroids and bullets.
            self.asteroids.empty()
            self.stars.empty()
            self.bullets.empty()

            # Create a new sky and center the ship.
            self.scooter.center_scooter()
            self._create_sky()

            # Pause
            sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)    


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.scooter.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullets()
        self.asteroids.draw(self.screen)
        self.stars.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    zz = ZipZipRacing()
    zz.run_game()
