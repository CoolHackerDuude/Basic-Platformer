import pgzrun
import pygame
from settings import *
from map import *

level = Level()
background = level.draw_background()
WIDTH = level.width
HEIGHT = level.height
""" PLAYER """
player = Actor('gameboy_idle', anchor = ('center', 'center'))
player.x = WIDTH // 2
player.y = HEIGHT // 2
player.vel_y = 0
player.vel_x = 0
player.on_ground = False

""" ENEMY """
enemies = []
for y in range(len(level.tiles)):
    for x in range(len(level.tiles[y])):
        if level.tiles[y][x] == 'E':
            enemy = Actor('evil_gameboy', ancor = ('center', 'center'))
            enemy.x = x * TILE_SIZE
            enemy.y = y * TILE_SIZE
            enemy.vel_x, enemy.vel_y = 0, 0
            enemy.direction = -1
            enemies.append(enemy)

def update():
    update_keys()
    update_player()
    update_enemies()
    
def update_enemies():
    for enemy in enemies:
        enemy.vel_y += GRAVITY
        if enemy.direction == -1:
            turn = look_ahead(enemy, 'left')
        else:
            turn = look_ahead(enemy, 'right')
        if turn:
            enemy.direction *= -1
        enemy.vel_x = enemy.direction * ENEMY_SPEED
        if move(enemy, 0, int(enemy.vel_y)):
            if enemy.vel_y > 0:
                enemy.on_ground = True
            enemy.vel_y = 0
        if move(enemy, int(enemy.vel_x), 0):
            enemy.vel_x = 0
            enemy.direction *= -1
        
def look_ahead(actor, direction):
    y = actor.bottom + TILE_SIZE // 2
    if direction == 'left':
        x = actor.left - TILE_SIZE // 2
    else:
        x = actor.right + TILE_SIZE // 2
    return not level.get_in_wall(x, y)
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
    for enemy in enemies:
        if player.colliderect(enemy):
            player.x = TILE_SIZE * 2
            player.y = HEIGHT - TILE_SIZE * 2
        
    
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
            if level.get_in_wall(int(actor.left), int(actor.bottom)) or level.get_in_wall(int(actor.left), int(actor.top)) :
                actor.x += 1
                return True
    if dy > 0:
        for i in range(dy):
            actor.y += 1
            left_foot = actor.left + 1/4 * actor.width
            right_foot = actor.right - 1/4 * actor.width 
            if level.get_in_wall(int(left_foot), int(actor.bottom)) or level.get_in_wall(int(right_foot), int(actor.bottom)) :
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
    for enemy in enemies:
        enemy.draw()
    #show_tiles()
    
def show_tiles():
    for x in range(0, WIDTH, TILE_SIZE):
        screen.draw.line( (x, 0), (x, HEIGHT), GREY)
    for y in range(0, HEIGHT, TILE_SIZE):
        screen.draw.line( (0, y), (WIDTH, y), GREY)
    
pgzrun.go()