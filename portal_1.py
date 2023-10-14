import pygame, random
from constants import *
import player
import random

class Portal1(pygame.sprite.Sprite):
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
            player_group = player_group.main_group
            portal2 = portal2.main_group
            portal1 = portal1.main_group

            for i in portal2:
                if pygame.sprite.groupcollide(player_group, portal1, False, False):
                    player_group.add(player.Player(i.x, i.y, BLOCK_SIZE, BLOCK_SIZE))
