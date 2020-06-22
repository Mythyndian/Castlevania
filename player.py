import pygame
import sys
import os
from itertools import cycle
from loadings import WALK_L, WALK_R, BACKGROUND

pygame.init()
ani = 3


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.movement_x = 0
        self.movement_y = 0
        self.moving = False
        self.move_right = cycle([WALK_R[0], WALK_R[1], WALK_R[2]])
        self.move_left = cycle([WALK_L[0], WALK_L[1], WALK_L[2]])
        self.frame = 0
        self.direction_of_movement = 'Right'
        self.image = WALK_R[0]
        self.rect = self.image.get_rect()

    def turn_right(self):
        if self.direction_of_movement == 'Left':
            self.direction_of_movement = 'Right'
            self.image = WALK_R[0]

    def turn_left(self):
        if self.direction_of_movement == 'Right':
            self.direction_of_movement = 'Left'
            self.image = WALK_L[0]

    def move(self, x, y):
        self.movement_x += x
        self.movement_y += y

    def stop(self):
        self.movement_x = 0
        if self.direction_of_movement == 'Right':
            self.image = WALK_R[0]

    def update(self):
        # UPDATE PLAYER POSITION
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y
        # UPDATE IMAGES
        # MOVING LEFT
        if self.movement_x < 0:
            self.image = next(self.move_left)

        # MOVING RIGHT
        if self.movement_x > 0:
            self.image = next(self.move_right)

    def get_event(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.stop()
                self.turn_right()
                self.move(5, 0)

            if event.key == pygame.K_a:
                self.stop()
                self.turn_left()
                self.move(-5, 0)


