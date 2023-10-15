from constants import *
from pygame import mixer
import pygame
import csv
import platform
import player
import load_level
import group_manager
import lava

class States_manager():
    def __init__(self):
        self.group_manager = group_manager.Group_manager()
        self.states = ["start", "intro", "running", "paused", "dead", "game_over"]
        self.state = self.states[2]

        self.surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

        self.map = []

        self.ml = load_level.Load_level()

        self.ml.load_level(self.ml.level_num, self.group_manager)



    def events(self):


        events = pygame.event.get()

        for event in events:


            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                #used to kill outside loop
                if event.key == pygame.K_q:
                    return True

                if event.key == pygame.K_p:

                    if self.state == "paused" and event.key == pygame.K_p:
                        self.state = "running"
                    else:
                        self.state = "paused"

            if event.type == pygame.KEYUP:
                if event.key == 32:#SPACE
                    if self.state == "start":
                        self.state = "running"




    def draw(self):
        self.surface.fill((100, 100, 100))#background


        if self.state == "intro":
            pass

        if self.state == "start":
            pass

        if self.state == "running":

            self.group_manager.get_drawing_group().draw(self.surface)
            self.ml.door(self.group_manager)



        if self.state == "paused":
            pass

        if self.state == "dead":
            pass

        if self.state == "end":
            pass



        pygame.display.flip()




    def update(self):


        if self.state == "intro":
            pass

        if self.state == "start":
            pass

        if self.state == "running":
            self.group_manager.update()


        if self.state == "paused":
            pass

        if self.state == "dead":
            pass

        if self.state == "end":
            pass
