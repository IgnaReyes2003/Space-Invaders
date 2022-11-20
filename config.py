import pygame
class Config():
    """Sirve para almacenar las configuraciones de Space Invaders."""
    def __init__(self):
        """Inicializa las configuraciones del juego."""
        self.screen_width = 800
        self.screen_height = 600
        #self.bg_color = (230, 230, 230)

        # Configuraciones de la nave.

        self.speed_factor_ship = 1.5

        # Configuraciones de las balas.

        self.speed_factor_bullet = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60