import sys
import pygame
from config import Config

def run_game():
    # Inicializar el juego, las configuraciones y crear un objeto llamado pantalla.
    pygame.init()
    ai_config = Config()
    screen = pygame.display.set_mode(
        (ai_config.screen_width, ai_config.screen_height))
    pygame.display.set_caption("Space Invaders")

    # Establecer el color del fondo.
    bg_color = (230, 230, 230)


    # Iniciar el bucle principal del juego.
    while True:

        # Responder a la entrada del teclado o del ratón.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Volver a dibujar la pantalla durante cada pasada por el bucle.
        screen.fill(ai_config.bg_color)  


        # Hacer visible la pantalla dibujada más reciente.
        pygame.display.flip()

run_game()        


