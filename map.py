import pygame
from settings import *
brick = pygame.image.load(BRICK)

class Level:
    def __init__(self):
        self.tiles = []
        with open('level1.txt') as f:
            for line in f:
                self.tiles.append(line.strip())
        self.width = len(self.tiles[0]) * TILE_SIZE
        self.height = len(self.tiles) * TILE_SIZE
   
    """
    x and y are pixel locations in level
    returns True if in a wall
    """
    def get_in_wall(self, x, y):
        tile_x = int(x) // TILE_SIZE
        tile_y = int(y) // TILE_SIZE
        return self.tiles[tile_y][tile_x] == 'X'
        
    def draw_background(self):
        bg = pygame.Surface((self.width, self.height))
        bg.fill(LIGHT_BLUE)
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[y])):
                if self.tiles[y][x] == 'X':
                    bg.blit(brick, (x * TILE_SIZE, y * TILE_SIZE))
        return bg
class Pencil:
    def __init__(self, length, color, has_eraser, is_sharp):
        self.length = length
        self.color = color
        self.has_eraser = has_eraser
        self.is_sharp = is_sharp
        
    def write(self, text):
        print(text)