import pygame, random
from constants import *
import player
import random

class Portal2(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.x = x
        self.y = y + 45
        self.width = 20
        self.height = 50
        self.speed = 2
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((0, 255 ,0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        def update(self, main_group):
            pass
