import pgzrun
import pygame
from settings import *
from map import *

level = Level()
background = level.draw_background()
WIDTH = level.width
HEIGHT = level.height
player = Actor('gameboy_idle')

def update():
    pass
def draw():
    screen.blit(background, (0, 0))
    player.draw()
    #show_tiles()
    
def show_tiles():
    for x in range(0, WIDTH, TILE_SIZE):
        screen.draw.line( (x, 0), (x, HEIGHT), GREY)
    for y in range(0, HEIGHT, TILE_SIZE):
        screen.draw.line( (0, y), (WIDTH, y), GREY)
    
pgzrun.go()