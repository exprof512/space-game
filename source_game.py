import pygame, controls
import sys
from gun import Gun
from pygame.sprite import Group

def run():
    pygame.init()
    screen = pygame.display.set_mode ((800, 600))
    pygame.display.set_caption("Джеки")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, bullets)
        controls.update_bullets(bullets)

run()