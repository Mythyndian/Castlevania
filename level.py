import pygame
from platform import Platform

pygame.init()


class Level:
    def __init__(self, player):
        self.set_of_platforms = set()
        self.player = player
        self.world_shift = 0

    def update(self):
        for p in self.set_of_platforms:
            p.update()

        if self.player.rect.right >= 1050:
            diff = self.player.rect.right - 1050
            self.player.rect.right = 1050
            self._shift_world(-diff)

        if self.player.rect.left <=150:
            diff = 150 - self.player.rect.left
            self.player.rect.left = 150
            self._shift_world(diff)

    def draw(self, surface):
        for p in self.set_of_platforms:
            p.draw(surface)

    def _shift_world(self, shift_x):
        self.world_shift += shift_x

        for p in self.set_of_platforms:
            p.rect.x += shift_x

class Level1(Level):
    def __init__(self, player=None):
        super().__init__(player)
        self.create_platforms()

    def create_platforms(self):
        ws_platform_static = [[80, 30, 0, 175], [40, 30, 80, 200], [40, 30, 120, 220], [220, 15, 120, 220],
                              [250, 40, 370, 175], [115, 150, 640, 100],[50, 40, 0, 500], [380, 40, 50, 540],
                              [300, 50, 430, 500], [180, 100, 750, 400]]

        for ws in ws_platform_static:
            platform_object = Platform(*ws)
            self.set_of_platforms.add(platform_object)
