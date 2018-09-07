from settings import Settings
from ship import Ship
import game_functions as gf

import pygame
from pygame.sprite import Group


def run_game():

    pygame.init
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Aliens")

    ship = Ship(ai_settings, screen)
    # makes a group to store bullets in
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # clean up bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
