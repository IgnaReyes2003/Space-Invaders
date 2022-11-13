import pygame

class Ship():
    """Sirve para gestionar el comportamiento de la nave."""
    def __init__(self, screen):
        """Inicializa la nave y establece su posición de partida."""

        self.screen = screen

        # Carga la imagen de la nave y obtiene su rect.
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Cada nave comenzará en la parte inferior central de la pantalla.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Dibuja la nave en su ubicación actual."""
        self.screen.blit(self.image, self.rect)
