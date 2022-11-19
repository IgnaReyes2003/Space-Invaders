import sys
import pygame

def verificar_eventos(ship):
    """Responde a las pulsaciones del teclado y a los eventos del ratón."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx +=1


def update_screen(ai_config, screen, ship):
    """Actualiza las imágenes de la pantalla y pasa a la nueva pantalla."""

    # Volver a dibujar la pantalla durante cada pasada por el bucle.
    screen.fill(ai_config.bg_color)
    ship.blitme()  


    # Hacer visible la pantalla dibujada más reciente.
    pygame.display.flip()
