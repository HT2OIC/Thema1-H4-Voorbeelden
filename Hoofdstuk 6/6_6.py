import pygame


fullscreen = True

def draw():
    global fullscreen

    if fullscreen:
        pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        fullscreen = False 