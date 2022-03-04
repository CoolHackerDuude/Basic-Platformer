import pgzrun
import pygame
from settings import *

brick = pygame.image.load(BRICK)

def update():
    pass
def draw():
    screen.fill(LIGHT_BLUE)
    screen.blit(brick, (WIDTH - 18, 0))
pgzrun.go()
