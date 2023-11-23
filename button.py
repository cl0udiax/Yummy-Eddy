import pygame

class button():
	def __init__(self, screen, x, y, image, scale = 1):
		self.screen = screen
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False

	def draw(self):
		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				pygame.time.delay(200)
				return True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		
		self.screen.blit(self.image, self.rect.topleft)