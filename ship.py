import pygame

class Ship():
    """Sirve para gestionar el comportamiento de la nave."""
    def __init__(self, ai_config, screen):
        """Inicializa la nave y establece su posición de partida."""

        self.screen = screen
        self.ai_config = ai_config

        # Carga la imagen de la nave y obtiene su rect.
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Cada nave comenzará en la parte inferior central de la pantalla.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Almacena un valor decimal para el centro de la nave.
        self.center = float(self.rect.centerx)

        # Banderas de movimiento.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualiza la posición de la nave, según las banderas de movimiento."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_config.speed_factor_ship

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_config.speed_factor_ship

        # Actualiza el objeto rect desde self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Dibuja la nave en su ubicación actual."""
        self.screen.blit(self.image, self.rect)
