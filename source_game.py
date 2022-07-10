import pygame, controls
import sys
from gun import Gun

def run():
    pygame.init()
    screen = pygame.display.set_mode ((800, 600))
    pygame.display.set_caption("Джеки")
    bg_color = (0, 0, 0)
    gun = Gun(screen)

    while True:
        controls.events(gun)
        gun.update_gun()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()

run()