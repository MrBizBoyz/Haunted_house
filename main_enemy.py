from constants import *
import pygame
import random as rand
from main_entity import Main_entity
import math
from pygame.locals import *

class Main_enemy(Main_entity):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)


        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((48, 0, 0))
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
        self.direction  = pygame.math.Vector2(1, 1)
        self.speed = 2
        self.can_move_timer = 2 #SECONDS
        self.timer_start_time = 0
        self.can_move_timer_ticks = 0
        self.can_move = True
        self.move_timer = pygame.time.get_ticks()
        self.delay = 2000


    def reverse_direction_move(self, solid_objects_group, speed):

    # diagonal speed is to fast withoust this
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()



        # move
        if self.can_move:
            self.rect.x += self.direction.x * speed
        # check for collision
            if self.collison(solid_objects_group, "h"):

                # self.can_move_timer_ticks
                self.direction.x  = -self.direction.x
