import pgzrun
import pygame
from settings import *
from map import *

level = Level()
background = level.draw_background()
WIDTH = level.width
HEIGHT = level.height
player = Actor('gameboy_idle', anchor = ('center', 'center'))
player.x = WIDTH // 2
player.y = HEIGHT // 2
player.vel_y = 0
player.vel_x = 0
player.on_ground = False 

def update():
    update_keys()
    update_player()

def update_keys():
    player.vel_x = 0
    if keyboard.left:
        player.vel_x -= SPEED
    if keyboard.right:
        player.vel_x += SPEED
    if keyboard.up and player.on_ground:
        player.vel_y -= JUMP
def update_player():
    player.vel_y += GRAVITY
    player.on_ground = False
    if move(player, 0, int(player.vel_y)):
        if player.vel_y >0:
            player.on_ground = True
        player.vel_y = 0
    if move(player, int(player.vel_x), 0):
        player.vel_x = 0
        
    
def move(actor, dx, dy):
    if dx > 0:
        for i in range(dx):
            actor.x += 1
            if level.get_in_wall(int(actor.right), int(actor.y)) or level.get_in_wall(int(actor.right), int(actor.top)):
                actor.x -= 1
                return True
    if dx < 0:
        for i in range(abs(dx)):
            actor.x -= 1
            if level.get_in_wall(int(actor.left), int(actor.y)) or level.get_in_wall(int(actor.left), int(actor.top)) :
                actor.x += 1
                return True
    if dy > 0:
        for i in range(dy):
            actor.y += 1
            if level.get_in_wall(int(actor.x), int(actor.bottom)):
                actor.y -= 1
                return True
    if dy < 0:
        for i in range(abs(dy)):
            actor.y -= 1
            if level.get_in_wall(int(actor.x), int(actor.top)):
                actor.y += 1
                return True
    
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