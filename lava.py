from constants import *
import pygame
import random

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.width = width
        self.h = 0
        self.x = 0
        self.y = 0
        self.height = self.h

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)


    def update(self, main_group):
        # self.image = pygame.Surface([self.width, self.height])
        # self.image.fill((255, 0, 0))
        # self.rect = self.image.get_rect()
        # self.rect.topleft = (self.x, self.y)
        pass
