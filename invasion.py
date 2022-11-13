import sys
import pygame

def run_game():
    # Inicializar el juego y crear un objeto llamado pantalla.
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Invaders")

    bg_color = (230, 230, 230)

    # Iniciar el bucle principal del juego.
    while True:

        # Responder a la entrada del teclado o del ratón.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Hacer visible la pantalla dibujada más reciente.
        pygame.display.flip()

run_game()        


