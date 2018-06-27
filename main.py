import pygame as pyg
from pygame.sprite import Group

from player import Player
from enemy import Enemy
import game_functions as gf


def main():

    pyg.init() # Init pygame and make a window, the player, and the tiles
    pyg.display.set_caption("Pew Pew Game")
    window = pyg.display.set_mode((1200, 800)) # Tile Dimensions: 60x40
    player = Player(window)
    enemies = Group()
    enemy = Enemy(window)
    enemies.add(enemy)
    walls = Group()
    lavas = Group()
    gf.init_tiles(window, walls, lavas)

    while True:
        gf.fade_to_black(window)
        gf.check_events(player)
        player.move()
        gf.check_collisions(player, walls, lavas, enemies, window)
        gf.update_screen(window, player, walls, lavas, enemies)

if __name__ == '__main__':
    main()
