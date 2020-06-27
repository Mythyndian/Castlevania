import pygame
from platform import Platform
import random
from loadings import (ENEMY_DEATH, GHOUL_WALK_L, GHOUL_WALK_R)
from enemies import Ghoul

pygame.init()


class Level:
    def __init__(self, player):
        self.set_of_platforms = set()
        self.set_of_enemies = pygame.sprite.Group()
        self.player = player

    def update(self):
        for p in self.set_of_platforms:
            p.update()
        self.set_of_enemies.update()

    def draw(self, surface):
        for p in self.set_of_platforms:
            p.draw(surface)
        self.set_of_enemies.draw(surface)


class Level1(Level):
    def __init__(self, player=None):
        super().__init__(player)
        #self.crete_platforms()
        self.create_ghouls()

    def crete_platforms(self):
        ws_platform_static = [[80, 35, 0, 175], [40, 30, 80, 200], [40, 30, 120, 220], [220, 15, 120, 220],
                              [275, 75, 370, 175], [115, 250, 640, 0], [50, 40, 0, 500], [380, 40, 50, 540],
                              [350, 50, 430, 500], [180, 100, 750, 395], [150, 50, 930, 430], [50, 50, 1080, 395]]

        for ws in ws_platform_static:
            platform_object = Platform(*ws)
            self.set_of_platforms.add(platform_object)

    def create_ghouls(self):
        ws_platform_static = [[80, 35, 0, 175], [40, 30, 80, 200], [40, 30, 120, 220], [220, 15, 120, 220],
                              [250, 40, 370, 175], [115, 150, 640, 100], [50, 40, 0, 500], [380, 40, 50, 540],
                              [300, 50, 430, 500], [180, 100, 750, 395], [150, 50, 930, 430], [50, 50, 1080, 395]]
        for ws in ws_platform_static:
            platform = Platform(*ws)
            self.set_of_platforms.add(platform)
            ghoul = Ghoul(GHOUL_WALK_R[0], GHOUL_WALK_R,
                          GHOUL_WALK_L, ENEMY_DEATH,
                          platform, 2)
            self.set_of_enemies.add(ghoul)
