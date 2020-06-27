import pygame

class Item(pygame.sprite.Sprite):
	def __init__(self,image,name,rect_center_x,rect_center_y):
		super().__init__()
		self.image = image
		self.rect = self.image.get_rect()
		self.name = name
		self.rect.center = [rect_center_x, rect_center_y]
