import pygame
import sys
import os
from itertools import cycle
from loadings import WALK_L, WALK_R, BACKGROUND

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(Player, self).__init__()
        self.image = WALK_R[0]
        self.rect = self.image.get_rect()
        self.jumping = False
        self.walk_count = 0
        self.movement_x = 0
        self.movement_y = 0
        self._count = 0
        self.direction_of_movement = 'right'

    def turn_right(self):
        self.movement_x = 6

    def turn_left(self):
        self.movement_x = -6

    def stop(self):
        self.movement_x = 0

    def update(self):
        self.rect.x += self.movement_x

        if self.movement_x > 0:
            self._move(WALK_R)

        if self.movement_x < 0:
            self._move(WALK_L)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.turn_right()
            if event.key == pygame.K_a:
                self.turn_left()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d and self.movement_x > 0:
                self.stop()
                self.image = WALK_R[0]
            if event.key == pygame.K_a and self.movement_x < 0:
                self.stop()
                self.image = WALK_L[0]

    def _move(self, image_list):
        if self._count < 4:
            self.image = image_list[0]
        elif self._count < 8:
            self.image = image_list[1]
        elif self._count < 12:
            self.image = image_list[2]

        if self._count >= 12:
            self._count = 0
        else:
            self._count += 1
