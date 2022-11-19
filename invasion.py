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

    # Crea una nave.
    ship = Ship(screen)

    # Establecer el color del fondo.
    bg_color = (230, 230, 230)


    # Iniciar el bucle principal del juego.
    while True:

        # Responder a la entrada del teclado o del ratón.
        fj.verificar_eventos()

        # Volver a dibujar la pantalla durante cada pasada por el bucle.
        screen.fill(ai_config.bg_color)
        ship.blitme()  


        # Hacer visible la pantalla dibujada más reciente.
        pygame.display.flip()

run_game()        


