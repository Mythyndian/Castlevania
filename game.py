import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
run = True
intro = True
while run:
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit


        # KEY DOWN EVENTS
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    raise SystemExit

pygame.quit()
