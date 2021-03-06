import pygame
import sys
import os
import random
from loadings import BACKGROUND
from loadings import GHOUL_WALK_L, GHOUL_WALK_R

pygame.init()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, star_image, image_list_right,
                 image_list_left, image_list_dead,
                 movement_x=0, movement_y=0):
        super().__init__()
        self.image = star_image
        self.rect = self.image.get_rect()
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.image_list_right = image_list_right
        self.image_list_left = image_list_left
        self.image_list_dead = image_list_dead
        self.direction_of_movement = 'right'
        self.lifes = 1
        self._count = 0

    def update(self):
        if not self.lifes and self._count > 7:
            self.kill()

        self.rect.x += self.movement_x

        # ANIMATION
        if self.lifes:
            if self.movement_x > 0:
                self._move(self.image_list_right)
            if self.movement_x < 0:
                self._move(self.image_list_left)
        else:
            if self.direction_of_movement == 'right':
                self._move(self.image_list_dead)
            else:
                self._move(self.image_list_dead)
        if self.movement_x > 0 and self.direction_of_movement == 'left':
            self.direction_of_movement = 'right'

        if self.movement_x < 0 and self.direction_of_movement == 'right':
            self.direction_of_movement = 'left'

    def _move(self, image_list):
        if self._count < 4:
            self.image = image_list[0]
        elif self._count < 8:
            self.image = image_list[1]

        if self._count >= 8:
            self._count = 0
        else:
            self._count += 1


class Ghoul(Enemy):
    def __init__(self, star_image, image_list_right,
                 image_list_left, image_list_dead, platform,
                 movement_x=0, movement_y=0):
        super().__init__(star_image, image_list_right,
                         image_list_left, image_list_dead,
                         movement_x, movement_y)

        self.platform = platform
        self.rect.bottom = self.platform.rect.top
        # self.rect.centerx = random.randint(self.rect.left + self.rect.width // 2,
        #                                  self.rect.right - self.rect.width // 2)
        self.rect.x = self.platform.rect.x

    def update(self):
        super(Ghoul, self).update()

        if (self.rect.right > self.platform.rect.right
                or self.rect.left < self.platform.rect.left):
            self.movement_x *= -1
