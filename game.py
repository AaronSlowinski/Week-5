

import pygame
from pygame.sprite import Sprite


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
        