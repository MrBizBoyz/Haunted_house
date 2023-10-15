import pygame, random
from constants import *
import player
pygame.init()
from main_entity import Main_entity
import test_enemy

class Player(Main_entity):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.speed = 5
        self.x_speed = 0
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.lift = -1.5
        self.grav = 0.3
        self.vel = 0
        self.max_vel = -7
        self.direction = pygame.math.Vector2(0, 0)
        self.can_jump = True
        self.jump_counter = 0
        self.clock = pygame.time.Clock()
        self.time_passed = 0
        self.facing_direction = pygame.math.Vector2(0, 0)
        self.direction  = pygame.math.Vector2(0, 0)
        self.health = 3


    def update(self, main_group):
        solid_objects_group = main_group.solid_objects_group
        player_group = main_group.player_group
        floor_group = main_group.floor_group
        enemy = main_group.test_enemy_group
        self.gravity()
        self.collide(main_group)
        self.key_input(solid_objects_group, main_group)
        self.move(solid_objects_group, self.speed)
        if self.health <= 0:
            self.kill()

        for f in floor_group:
            if self.rect.x >= GAME_WIDTH // 2 and f.rect.right > 0:
                f.move_left()
            else:

                f.move_right()


    def key_input(self, solid_objects_group, main_group):

        keys = pygame.key.get_pressed()
        player_group = main_group.player_group


        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.facing_direction = pygame.math.Vector2(-1, 0)

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1

            self.facing_direction = pygame.math.Vector2(1, 0)


        else:
            self.direction = pygame.math.Vector2(0, 0)




        self.x_speed *= 0.95 ** (100 * self.time_passed)

        self.rect.x += self.x_speed * self.time_passed

        self.time_passed = self.clock.tick() / 1000

        if keys[pygame.K_SPACE]:
            self.jump()
            self.jump_counter += 1



    def jump(self):
        if self.can_jump == True:
            self.vel += self.lift





    def gravity(self):


        self.vel += self.grav
        self.rect.y += self.vel

        if self.vel < self.max_vel:
            self.vel = self.max_vel
            self.can_jump = False



    def collide(self, main_group):
        floor_group = main_group.floor_group
        enemy = main_group.test_enemy_group
        self_group = main_group.player_group
        platforms = pygame.sprite.spritecollide(self, floor_group, False)
        test_enemy = pygame.sprite.spritecollide(self, enemy, False)

        for f in platforms:
            if self.rect.bottom <= f.rect.top + abs(self.vel):
                self.rect.bottom = f.rect.top
                self.vel = 0
                self.can_jump = True
                self.jump_counter = 0
                self.vel = 0
            elif self.rect.top >= f.rect.bottom - abs(self.vel):
                self.rect.top = f.rect.bottom
                self.vel = 0

        for e in test_enemy:
            if self.rect.bottom < e.rect.bottom:
                e.kill()

        if self.vel > 0:
            self.can_jump = True
