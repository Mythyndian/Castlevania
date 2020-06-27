import pygame

pygame.init()


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, rect_x, rect_y):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)
