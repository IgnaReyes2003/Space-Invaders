import sys
import pygame

def verificar_eventos_keydown(event, ship):
    """Responde a las pulsaciones de teclas."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def verificar_eventos_keyup(event, ship):
    """Responde a las pulsaciones de teclas."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def verificar_eventos(ship):
    """Responde a las pulsaciones del teclado y a los eventos del ratón."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event, ship)

        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event, ship)

def update_screen(ai_config, screen, ship):
    """Actualiza las imágenes de la pantalla y pasa a la nueva pantalla."""

    # Volver a dibujar la pantalla durante cada pasada por el bucle.
    ship.blitme()  


    # Hacer visible la pantalla dibujada más reciente.
    pygame.display.flip()
