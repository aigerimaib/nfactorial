import sys
import pygame
from pygame.locals import *


class Board:
    def __init__(self, path):

        self.CHUNK_SIZE = 16
        self.load_map(path)
        self.load_images()
        self.make_solid_blocks()
        self.make_water_pools()
        self.make_lava_pools()
        self.make_goo_pools()

    def load_map(self, path):

        self._game_map = []

        with open(path) as f:
            for line in f:
                line = line.strip().split(',')  # convert string to list of str
                self._game_map.append(line)

    def get_game_map(self):

        return self._game_map

    def load_images(self):

        self._background = pygame.image.load('data/board_textures/background.png')
        # create dictionary that maps a string to a board texture
        self._board_textures = {

            "111": pygame.image.load('data/board_textures/grass.png'),
            "113": pygame.image.load('data/board_textures/brick.png'),

            "2": pygame.image.load('data/board_textures/lava.png'),
            "3": pygame.image.load('data/board_textures/water.png'),
        }
        for texture in self._board_textures.keys():
            self._board_textures[texture].set_colorkey((255, 0, 255))

    def get_background(self):

        return self._background

    def get_board_textures(self):

        return self._board_textures

    def make_solid_blocks(self):

        CHUNKS_SIZE = 16
        self._solid_blocks = []
        for y, row in enumerate(self._game_map):
            for x, tile in enumerate(row):
                # if block is not air or a liquid
                if tile not in ['0', '2', '3', '4']:
                    # create a 16 x 16 rect and add it to the list
                    self._solid_blocks.append(
                        pygame.Rect(x * self.CHUNK_SIZE, y * self.CHUNK_SIZE,
                                    self.CHUNK_SIZE, self.CHUNK_SIZE))

    def get_solid_blocks(self):

        return self._solid_blocks

    def make_lava_pools(self):

        # create an empty list to store lava pool rects
        self._lava_pools = []
        for y, row in enumerate(self._game_map):
            for x, tile in enumerate(row):
                # if number in game map represents lava
                if tile == "2":
                    # add a 16x8 rect to the list
                    self._lava_pools.append(
                        pygame.Rect(x * self.CHUNK_SIZE, y * self.CHUNK_SIZE
                                    + self.CHUNK_SIZE / 2, self.CHUNK_SIZE,
                                    self.CHUNK_SIZE / 2))

    def get_lava_pools(self):

        return self._lava_pools

    def make_water_pools(self):

        # Create empty list to store water pool rects
        self._water_pools = []
        for y, row in enumerate(self._game_map):
            for x, tile in enumerate(row):
                # if number in game map represents water
                if tile == "3":
                    # add a 16x8 rect to the list
                    self._water_pools.append(
                        pygame.Rect(x * self.CHUNK_SIZE, y * self.CHUNK_SIZE
                                    + self.CHUNK_SIZE / 2, self.CHUNK_SIZE,
                                    self.CHUNK_SIZE / 2))

    def get_water_pools(self):

        return self._water_pools

    def make_goo_pools(self):

        # create an empty list to store goo rects
        self._goo_pools = []
        for y, row in enumerate(self._game_map):
            for x, tile in enumerate(row):
                # if number in game map represents goo
                if tile == "4":
                    # add a 16x8 rect to the list
                    self._goo_pools.append(
                        pygame.Rect(x * self.CHUNK_SIZE, y * self.CHUNK_SIZE
                                    + self.CHUNK_SIZE / 2, self.CHUNK_SIZE,
                                    self.CHUNK_SIZE / 2))

    def get_goo_pools(self):

        return self._goo_pools
