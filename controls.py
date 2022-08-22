import pygame, sys
from bullet import Bullet

def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.moveright = True
            elif event.key == pygame.K_LEFT:
                gun.moveleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.moveright = False
            elif event.key == pygame.K_LEFT:
                gun.moveleft = False

def update(bg_color, screen, gun, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    pygame.display.flip()

def update_bullets (bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom  <= 0:
            bullets.remove(bullet)



