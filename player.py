import pygame
import sys
import os
from itertools import cycle
from loadings import ATTACK_L, ATTACK_R, CROUCH_R, CROUCH_L, WALK_L, WALK_R, BACKGROUND

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
        self._attack_count = 0
        self.level = None
        self.direction_of_movement = 'right'
        self.rect.x = x
        self.rect.y = y
        self.strike = False

    def turn_right(self):
        if self.direction_of_movement == 'left':
            self.direction_of_movement = 'right'
        self.movement_x = 6

    def turn_left(self):
        if self.direction_of_movement == 'right':
            self.direction_of_movement = 'left'
        self.movement_x = -6

    def stop(self):
        self.movement_x = 0

    def update(self):
        self._gravitation()

        self.rect.x += self.movement_x

        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms, False)

        for p in colliding_platforms:
            if self.movement_x > 0:
                self.rect.right = p.rect.left
            if self.movement_x < 0:
                self.rect.left = p.rect.right

        if self.movement_x > 0:
            self._move(WALK_R)

        if self.movement_x < 0:
            self._move(WALK_L)

        self.rect.y += self.movement_y
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms, False)

        for p in colliding_platforms:
            if self.movement_y > 0:
                self.rect.bottom = p.rect.top
                if self.direction_of_movement == 'left' and self.movement_x == 0:
                    self.image = WALK_L[0]
                if self.direction_of_movement == 'right' and self.movement_x == 0:
                    self.image = WALK_R[0]
            if self.movement_y < 0:
                self.rect.top = p.rect.bottom

            self.movement_y = 0

        if self.movement_y > 0:
            if self.direction_of_movement == 'left':
                self.image = WALK_L[0]
            else:
                self.image = WALK_R[0]
        if self.movement_y < 0:
            if self.direction_of_movement == 'left':
                self.image = CROUCH_L
            else:
                self.image = CROUCH_R
        elif self.direction_of_movement == 'right' and self.strike:
            self._attack(ATTACK_R)
        elif self.direction_of_movement == 'left' and self.strike:
            self._attack(ATTACK_L)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.turn_right()
            if event.key == pygame.K_a:
                self.turn_left()
            if event.key == pygame.K_w:
                self.jump()
            if event.key == pygame.K_f:
                self.stop()
                self.strike = True
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

    def _gravitation(self):
        if self.movement_y == 0:
            self.movement_y = 2
        else:
            self.movement_y += 0.9

    def _attack(self, image_list):
        if self._attack_count < 4:
            self.image = image_list[0]
        elif self._attack_count < 8:
            self.image = image_list[1]
        elif self._attack_count < 12:
            self.image = image_list[2]
        if self._attack_count >= 12:
            self._attack_count = 0
            self.strike = False
        else:
            self._attack_count += 1

    def jump(self):
        self.rect.y += 2
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms, False)
        self.rect.y -= 2
        if colliding_platforms:
            self.movement_y = -14
