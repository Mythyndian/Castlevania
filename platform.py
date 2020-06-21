import pygame

pygame.init()


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        super().__init__(self)
        self.image = img
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
