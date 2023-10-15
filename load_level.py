from constants import *
import pygame
import csv
import player
import floor
import door
import test_enemy
import lava



class Load_level():
    def __init__(self):

        self.level = LEVELS

        self.level_num = 0
        self.scroll = False







    def get_list(self, level):
        map_list = ""

        with open(level) as file:
            map_list = file.read().split("\n")
        # filter out all "#" and empty strings
        map_list = list(filter(self.is_comment, map_list))

        #finally split by csv
        for m in range(len(map_list)):
            map_list[m] = map_list[m].split(",")

        return map_list


    def is_comment(self, string):
        if not string:
            return False
        if string[0] == "#":
            return False
        return True

    def load_level(self, level, main_group):
        player_group = main_group.player_group
        floor_group = main_group.floor_group
        door_group = main_group.door_group
        test_enemy_group = main_group.test_enemy_group
        solid_objects_group = main_group.solid_objects_group
        lava_group = main_group.lava_group

        test_enemy_group.empty()
        player_group.empty()
        floor_group.empty()
        door_group.empty()
        lava_group.empty()
        solid_objects_group.empty()


        map_tiles = self.get_list(self.level[level])
        for row in range(len(map_tiles)):
            for col in range(len(map_tiles[row])):
                item = map_tiles[row][col]



                if item == "p":


                    player_group.add(player.Player(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "pf":


                    floor_group.add(floor.Floor(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "d":


                    door_group.add(door.Door(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "e":


                    test_enemy_group.add(test_enemy.Test_enemy(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                if item == "e":
                    lava_group.add(lava.Lava(col * BLOCK_SIZE, row * BLOCK_SIZE, GAME_WIDTH, 0))



    def clear_level(self, main_group):

        player_group = main_group.player_group
        floor_group = main_group.floor_group
        door_group = main_group.door_group
        test_enemy_group = main_group.test_enemy_group
        solid_objects_group = main_group.solid_objects_group
        lava_group = main_group.lava_group

        test_enemy_group.empty()
        player_group.empty()
        floor_group.empty()
        lava_group.empty()
        door_group.empty()
        solid_objects_group.empty()

        self.load_level(self.level_num, main_group)

    def door(self, main_group):
        player_group = main_group.player_group
        door_group = main_group.door_group
        if pygame.sprite.groupcollide(player_group, door_group, False, False):

            self.level_num = self.level_num + 1
            self.clear_level(main_group)
