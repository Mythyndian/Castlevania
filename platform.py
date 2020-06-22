import pygame

pygame.init()


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = img
        if img is not None:
            self.image.convert_alpha()
            self.rect = self.image.get_rect()