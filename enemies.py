import pygame
import sys
import os
from loadings import BACKGROUND

class enemy(object):
    GHOUL_WALK_L1 = pygame.image.load(os.path.join('png','Enemies','Ghoul_L1.png')).convert_alpha(BACKGROUND)
    GHOUL_WALK_L2 = pygame.image.load(os.path.join('png','Enemies','Ghoul_L2.png')).convert_alpha(BACKGROUND)

    GHOUL_WALK_R1 = pygame.image.load(os.path.join('png','Enemies','Ghoul_R1.png')).convert_alpha(BACKGROUND)
    GHOUL_WALK_R2 = pygame.image.load(os.path.join('png','Enemies','Ghoul_R2.png')).convert_alpha(BACKGROUND)

    GHOUL_L = [GHOUL_WALK_L1,GHOUL_WALK_L2]
    GHOUL_R = [GHOUL_WALK_R1,GHOUL_WALK_R2]
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]  
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x, self.y, 31, 57)

    def draw(self,win):
        self.move()
        if self.walkCount + 1 >= 6:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.GHOUL_R[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.GHOUL_L[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1

        self.hitbox = (self.x, self.y, 31, 57)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel

            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

    def hit(self):
        print('hit')


class Bat(object):
    