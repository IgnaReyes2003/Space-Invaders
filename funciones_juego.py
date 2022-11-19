import sys
import pygame

def verificar_eventos():
    """Responde a las pulsaciones del teclado y a los eventos del ratón."""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
