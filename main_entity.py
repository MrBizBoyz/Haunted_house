import pygame

class Main_entity(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height):
		super().__init__()

		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.health = 10

		self.image = pygame.Surface([self.width, self.height])
		self.image.fill((255, 0, 0))
		self.rect = pygame.Rect(self.image.get_rect())
		self.direction  = pygame.math.Vector2(0, 0)



	def collison(self, block_group, dir):

		if dir == "h": #horizontal
			for sprite in block_group:
				if sprite != self:
						if sprite.rect.colliderect(self.rect):
							if self.direction.x > 0:#right
								self.rect.right = sprite.rect.left
								return True
							if self.direction.x < 0:#left
								self.rect.left = sprite.rect.right
								return True

		if dir == "v": #vertical
			for sprite in block_group:
				if sprite != self:
					if sprite.rect.colliderect(self.rect):
						if self.direction.y > 0:#up
							self.rect.bottom = sprite.rect.top
							return True
						if self.direction.y < 0:#down
							self.rect.top = sprite.rect.bottom
							return True

		return False



	def move(self, solid_objects_group, speed):
	# diagonal speed is to fast withoust this
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.rect.x += self.direction.x * speed
		self.collison(solid_objects_group, "h")

		self.rect.y += self.direction.y * speed
		self.collison(solid_objects_group, "v")
