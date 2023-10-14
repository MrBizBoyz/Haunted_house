from constants import *
import pygame
import random as rand
from main_enemy import Main_enemy

class Test_enemy(Main_enemy):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.speed = 2
        self.health_height = 20
        self.health_width = 64
        self.change_direction_timer = 2 #SECONDS
        self.x = x
        self.y = y + 22
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.is_dead = False

        self.random_move = rand.randint(0, 1)
        self.show_timer = pygame.time.get_ticks()
        self.delay = 1000



        # self.direction = self.random_vector2()



    def update(self, main_group):
        solid_objects_group = main_group.solid_objects_group
        player_group = main_group.player_group
        self.reverse_direction_move(solid_objects_group, self.speed)
