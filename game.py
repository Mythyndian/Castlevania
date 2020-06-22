import pygame
from loadings import (FONT, BACKGROUND, L1_1)
from itertools import cycle
from player import Player
from platform import Platform

pygame.init()
BLINK_EVENT = pygame.USEREVENT + 0
WIDTH, HEIGHT = 1109, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
run = True
intro = True
# BLINKING TEXT CODE
# ---------------------------------------------------------------------------------
on_text_surface = FONT.render('PRESS   ENTER   TO   START   PLAYING', True, (240, 240, 240), (0, 0, 0))
blink_rect = on_text_surface.get_rect()
blink_rect.center = (650, 500)
off_text_surface = pygame.Surface(blink_rect.size)
blink_surfaces = cycle([on_text_surface, off_text_surface])
blink_surface = next(blink_surfaces)
pygame.time.set_timer(BLINK_EVENT, 1000)
# ---------------------------------------------------------------------------------
while run:
    # INTRO
    # ---------------------------------------------------------------------------------
    while intro:
        # Render intro screen
        SCREEN.blit(BACKGROUND, (0, 0))
        for event in pygame.event.get():
            # When user click exit button
            if event.type == pygame.QUIT:
                raise SystemExit
            # When user press Enter game start working
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
            # CUSTOM BLINK EVENT
            if event.type == BLINK_EVENT:
                blink_surface = next(blink_surfaces)
        SCREEN.blit(blink_surface, blink_rect)
        pygame.display.update()
        # ---------------------------------------------------------------------------------
        # KEY DOWN EVENTS
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(L1_1, (0, 0))
    # Creating objects
    # ---------------------------------------------------------------------------------
    # platform_1 = Platform(0, 120, 50, 20)
    player = Player()
    player.rect.x = 0
    player.rect.y = 120
    player_list = pygame.sprite.Group()
    player_list.add(player)
    # ---------------------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                raise SystemExit
            player.get_event(event)
    player_list.draw(SCREEN)
    pygame.display.update()
    CLOCK.tick(60)
pygame.quit()
