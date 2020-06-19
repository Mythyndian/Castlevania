import pygame
from loadings import FONT
from loadings import BACKGROUND

pygame.init()
WIDTH, HEIGHT = 1109, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
run = True
intro = True
while run:
    while intro:
        # Render intro screen
        on_text_surface = FONT.render('PRESS   ENTER   TO   START   PLAYING', True, (240, 240, 240), (0, 0, 0))
        textRectObj = on_text_surface.get_rect()
        off_text_surface = pygame.Surface(textRectObj.size)
        textRectObj.center = (625, 500)
        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(on_text_surface, textRectObj)
        pygame.display.update()
        on_text_surface.fill((0, 0, 0))

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
    CLOCK.tick(60)
pygame.quit()
