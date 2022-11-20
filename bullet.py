import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Sirve para controlar las balas disparadas desde la nave."""
    def __init__(self, ai_config, screen, ship):
        super (Bullet, self).__init__()
        self.screen = screen

        # Crea un bala rect en (0, 0) y después establece la posición correcta.
        self.rect = pygame.Rect(0, 0, ai_config.bullet_width, ai_config.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Almacena la posición de la bala como un valor decimal.
        self.y = float(self.rect.y)
        
