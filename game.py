

import pygame
from pygame.sprite import Sprite
from bullet import Bullet
from alien import Alien


class Alien(Sprite):
    def __init__(self, ai_game):
        """
        Initialize the Alien class.

        Args:
            ai_game: The main game instance.

        Attributes:
            screen: The game screen.
            image: The image of the alien.
            rect: The rectangle representing the alien's position and size.
            x: The x-coordinate of the alien's position.
        """
        super().__init__()
        self.screen = ai_game.screen
        
        # Load the image of the alien
        self.image = pygame.image.load('/images/alien.png')
        self.rect = self.image.get_rect()
        
        # Set the initial position of the alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        

def __init__ (self):
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
    self.aliens = pygame.sprite.Group()
    
    self._create_fleet()
    
def _create_fleet(self):
    alien = Alien(self)
    self.aliens.add(alien)

def _update_screen(self):
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()
    for bullet in self.bullets.sprites():
        bullet.draw_bullet()
    self.aliens.draw(self.screen)
    
    pygame.display.flip() 

available_space_x = settings.screen_width - (2* alien_width)
