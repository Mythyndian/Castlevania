import pygame
from loadings import FONT
from loadings import BACKGROUND

pygame.init()
WIDTH, HEIGHT = 1109, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

run = True
intro = True
while run:
    while intro:
        # Render intro screen
        SCREEN.fill((0, 0, 0))
        textSurfaceObj = FONT.render('PRESS   ENTER   TO   START   PLAYING', True, (240, 240, 240), (0, 0, 0))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (650, 500)
        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(textSurfaceObj, textRectObj)
        pygame.display.update()
        for event in pygame.event.get():
            # When user click exit button
            if event.type == pygame.QUIT:
                raise SystemExit
            # When user press Enter game start working
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False

        # KEY DOWN EVENTS
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    raise SystemExit

pygame.quit()
