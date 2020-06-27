import pygame
import os
import sys

pygame.init()
SCREEN = pygame.display.set_mode((1109, 600))
BACKGROUND = pygame.image.load('png/Castlevania_logo.png')
FONT = pygame.font.Font('font/pixelated.ttf', 40)
L1_1 = pygame.image.load('png/L1.png')

# PLAYER ASSETS

WALK_L_1 = pygame.image.load(os.path.join('png', 'Player', 'WALK_L_1.png')).convert_alpha(BACKGROUND)
WALK_L_2 = pygame.image.load(os.path.join('png', 'Player', 'WALK_L_2.png')).convert_alpha(BACKGROUND)
WALK_L_3 = pygame.image.load(os.path.join('png', 'Player', 'WALK_L_3.png')).convert_alpha(BACKGROUND)

WALK_R_1 = pygame.image.load(os.path.join('png', 'Player', 'WALK_R_1.png')).convert_alpha(BACKGROUND)
WALK_R_2 = pygame.image.load(os.path.join('png', 'Player', 'WALK_R_2.png')).convert_alpha(BACKGROUND)
WALK_R_3 = pygame.image.load(os.path.join('png', 'Player', 'WALK_R_3.png')).convert_alpha(BACKGROUND)

CROUCH_R = pygame.image.load(os.path.join('png', 'Player', 'CROUCH_R.png')).convert_alpha(BACKGROUND)
CROUCH_L = pygame.image.load(os.path.join('png', 'Player', 'CROUCH_L.png')).convert_alpha(BACKGROUND)

ATTACK_R_1 = pygame.image.load(os.path.join('png', 'Player', 'ATTACK_R_1.png')).convert_alpha(BACKGROUND)
ATTACK_R_2 = pygame.image.load(os.path.join('png', 'Player', 'ATTACK_R_2.png')).convert_alpha(BACKGROUND)
ATTACK_R_3 = pygame.image.load(os.path.join('png', 'Player', 'ATTACK_R_3.png')).convert_alpha(BACKGROUND)

ATTACK_L_1 = pygame.image.load(os.path.join('png', 'Player', 'ATTACK_L_1.png')).convert_alpha(BACKGROUND)
ATTACK_L_2 = pygame.image.load(os.path.join('png', 'Player', 'ATTACK_L_2.png')).convert_alpha(BACKGROUND)
ATTACK_L_3 = pygame.image.load(os.path.join('png', 'Player', 'ATTACK_L_3.png')).convert_alpha(BACKGROUND)

WALK_L = [WALK_L_1, WALK_L_2, WALK_L_3]
WALK_R = [WALK_R_1, WALK_R_2, WALK_R_3]

ATTACK_R = [ATTACK_R_1, ATTACK_R_2, ATTACK_R_3]
ATTACK_L = [ATTACK_L_1, ATTACK_L_2, ATTACK_L_3]
# ENEMIES ASSETS

GHOUL_WALK_L1 = pygame.image.load(os.path.join('png', 'Enemies', 'Ghoul_L1.png')).convert_alpha(BACKGROUND)
GHOUL_WALK_L2 = pygame.image.load(os.path.join('png', 'Enemies', 'Ghoul_L2.png')).convert_alpha(BACKGROUND)

GHOUL_WALK_R1 = pygame.image.load(os.path.join('png', 'Enemies', 'Ghoul_R1.png')).convert_alpha(BACKGROUND)
GHOUL_WALK_R2 = pygame.image.load(os.path.join('png', 'Enemies', 'Ghoul_R2.png')).convert_alpha(BACKGROUND)

GHOUL_WALK_L = [GHOUL_WALK_L1, GHOUL_WALK_L2]
GHOUL_WALK_R = [GHOUL_WALK_R1, GHOUL_WALK_R2]

ENEMY_DEATH_1 = pygame.image.load(os.path.join('png', 'Enemies', 'DEATH_1.png')).convert_alpha(BACKGROUND)
ENEMY_DEATH_2 = pygame.image.load(os.path.join('png', 'Enemies', 'DEATH_2.png')).convert_alpha(BACKGROUND)
ENEMY_DEATH_3 = pygame.image.load(os.path.join('png', 'Enemies', 'DEATH_3.png')).convert_alpha(BACKGROUND)

ENEMY_DEATH = [ENEMY_DEATH_1, ENEMY_DEATH_2, ENEMY_DEATH_3]
