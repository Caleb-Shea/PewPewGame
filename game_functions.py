import pygame as pyg
import sys
import os

from time import sleep

from tile import *
from map import MAP
from player import Player

def terminate():
    pyg.quit()
    sys.exit()

def fade_to_black(window):
    for shade in range(256):
        shade = 255 - shade
        color = (shade,shade,shade)
        window.fill(color)
        pyg.display.flip()
        sleep(0.00001)

def player_died(player, window):
    window.fill((0,0,0))

    print("You Died")
    sleep(0.666)
    player.__init__(window)

def init_tiles(window, walls, lavas): # Init the map tiles
    x = 0
    y = 0
    for line in MAP:
        for tile in line:
            tileX = 20*x # Get tile coords
            tileY = 20*y

            if tile == "W": # Create the tiles
                curtile = Wall(window, (tileX, tileY))
                walls.add(curtile)
            elif tile == "L":
                curtile = Lava(window, (tileX, tileY))
                lavas.add(curtile)

            x += 1 # Update the position of the insertion tile
        x = 0
        y += 1

def check_events(player): # Handle keypresses
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            terminate()

        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_SPACE:
                player.speed = 6
            if event.key == pyg.K_RIGHT:
                player.moving_right = True
            if event.key == pyg.K_LEFT:
                player.moving_left = True
            if event.key == pyg.K_UP:
                player.moving_up = True
            if event.key == pyg.K_DOWN:
                player.moving_down = True

            if event.key == pyg.K_r: # Restart program
                os.execl(sys.executable, sys.executable, *sys.argv)

        elif event.type == pyg.KEYUP:
            if event.key == pyg.K_SPACE:
                player.speed = 3
            if event.key == pyg.K_RIGHT:
                player.moving_right = False
            if event.key == pyg.K_LEFT:
                player.moving_left = False
            if event.key == pyg.K_UP:
                player.moving_up = False
            if event.key == pyg.K_DOWN:
                player.moving_down = False

def check_collisions(player, walls, lavas, enemies, window):
    for lava in lavas.sprites():
        if pyg.sprite.collide_rect(player, lava):
            player_died(player, window)
            return
    for wall in walls.sprites():
        if pyg.sprite.collide_rect(player, wall):
            if player.moving_up:
                player.rect.top = wall.rect.bottom
                #player.moving_up = False
            elif player.moving_down:
                player.rect.bottom = wall.rect.top
                #player.moving_down = False
            elif player.moving_right:
                player.rect.right = wall.rect.left
                #player.moving_right = False
            elif player.moving_left:
                player.rect.left = wall.rect.right
                #player.moving_left = False
    for enemy in enemies.sprites():
        if pyg.sprite.collide_rect(player, enemy):
            player_died(player, window)
            return

def update_screen(window, player, walls, lavas, enemies):
    window.fill((230, 230, 230))

    for i in range(61): # Draw a grid
        pyg.draw.line(window, (150, 150, 150), (20*i, 0), (20*i, 800))
    for i in range(41):
        pyg.draw.line(window, (150, 150, 150), (0, 20*i), (1200, 20*i))

    for wall in walls.sprites(): # Draw tiles
        wall.render()
    for lava in lavas.sprites():
        lava.render()

    for enemy in enemies.sprites():
        enemy.render()

    player.render()
    pyg.display.flip()
