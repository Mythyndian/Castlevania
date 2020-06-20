import pygame,os,random,sys
#import game_module as gm


os.environ['SDL_VIDEO_CENTERED'] = '1' #window center
pygame.init()

pygame.display.set_caption('Castlevania Game')

#game window settings
SIZESCREEN = WIDTH, HEIGHT = 1109, 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZESCREEN)

# Player class

class Belmont(pygame.sprite.Sprite):
	def __init__(self,file_image):
		super().__init__()
		self.image = file_image
		self.rect = self.image.get_rect()
		self.movement_x = 0
		self.movement_y = 0
		self.lifes = 3
		self.level = None
		self.direction_of_movement = 'right'

	def draw(self,surface):
		surface.blit(self.image, self.rect)

belmont = Belmont()


# Main game loop
window_open = True
while window_open:
	screen.fill(pygame.Color('#ffebee'))

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			window_open = False
		elif event.type == pygame.QUIT:
			window_open = False

	pygame.display.flip()
	clock.tick(60)
pygame.quit()