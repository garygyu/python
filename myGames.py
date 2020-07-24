import pygame, sys
from pygame.locals import *
##import turtle

##import numpy as np
##import csv

RED = (255, 0, 0)
BLACK = (0, 0, 0)

def main():
    pygame.init()

    toLeft = 400
    toTop = 400

    x_init = 10
    y_init = 10
    radius = 10
    displacement = 8
    double = 2

    screen = pygame.display.set_mode((toLeft, toTop))

    screen.fill(BLACK)
    x = x_init
    y = y_init
    pygame.draw.circle(screen, RED, (x, y), radius)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    if event.mod == pygame.KMOD_NONE:
##                    print('No modifier keys were in a pressed state when this '
##                          'event occurred.')
                        x -= displacement
                    elif event.mod & pygame.KMOD_CTRL:
                        x -= double * displacement
                elif event.key == K_RIGHT:
                    if event.mod == pygame.KMOD_NONE:
                        x += displacement
                    elif event.mod & pygame.KMOD_CTRL:
                        x += double * displacement
                elif event.key == K_UP:
                    if event.mod == pygame.KMOD_NONE:
                        y -= displacement
                    elif event.mod & pygame.KMOD_CTRL:
                        y -= double * displacement            
                elif event.key == K_DOWN:
                    if event.mod == pygame.KMOD_NONE:
                        y += displacement
                    elif event.mod & pygame.KMOD_CTRL:
                        y += double * displacement
                    
        pygame.draw.rect(screen, BLACK, (0, 0, toLeft, toTop))
        pygame.draw.circle(screen, RED, (x, y), radius)
        pygame.display.update()
if __name__ == '__main__':
    main()
    
