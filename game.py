import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

run = True
intro = True
while run:
    while intro:
        # Render intro screen
        SCREEN.fill((0, 0, 0))
        for event in pygame.event.get():
            # When user click exit button
            if event.type == pygame.QUIT:
                raise SystemExit
            # When user press Enter game start working
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ENTER:
                    intro = False

        # KEY DOWN EVENTS
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    raise SystemExit

pygame.quit()
