import pygame, sys

def events(gun):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.moveright = True
            elif event.key == pygame.K_LEFT:
                gun.moveleft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.moveright = False
            elif event.key == pygame.K_LEFT:
                gun.moveleft = False
