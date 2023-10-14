from constants import *
import pygame
import random

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.width = 32
        self.height = 32
        self.x = x
        self.y = y
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((50, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.health = 10
