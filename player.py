import pygame
import sys
import os
from loadings import BACKGROUND

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.images = []
        self.direction_of_movement = 'Right'
        self.velocity = 0
        for i in range(3):
            img = pygame.image.load(os.path.join('png', 'Player', 'WALK_' + str(i) + '.png')).convert(BACKGROUND)
            self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def move(self):
        self.velocity = 5

    def turn_left(self):
        if self.direction_of_movement == 'Right':
            self.direction_of_movement = 'Left'

    def turn_right(self):
        if self.direction_of_movement == 'Left':
            self.direction_of_movement = 'Right'


    def update(self):
        pass
