
import pygame, random
from constants import *
import player
import random

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.x = x
        self.y = y
        self.width = 100
        self.height = 20
        self.speed = 1
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 0 ,0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.scroll = False


    def update(self, main_group):
        pass

    def move_right(self):
        self.rect = self.rect.move(self.speed, 0)

    def move_left(self):
        self.rect = self.rect.move(-self.speed, 0)
