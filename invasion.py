import pygame
from config import Config
from ship import Ship
import funciones_juego as fj

def run_game():
    # Inicializar el juego, las configuraciones y crear un objeto llamado pantalla.
    pygame.init()
    ai_config = Config()
    screen = pygame.display.set_mode(
        (ai_config.screen_width, ai_config.screen_height))
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)

    # Crea una nave.
    ship = Ship(ai_config, screen)

    # Permite cargar la imagen de fondo.
    background = pygame.image.load("images/theme.jpg")

    # Iniciar el bucle principal del juego.
    while True:
        # Responder a la entrada del teclado o del ratón.
        fj.verificar_eventos(ship)
        ship.update()
        fj.update_screen(ai_config, screen, ship)

        screen.blit(background, (0,0))

run_game()        


