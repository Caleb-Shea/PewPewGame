import pygame as pyg
from pygame.sprite import Sprite


class Tile(Sprite):

    def __init__(self, window, tile_placement):
        super().__init__()
        self.window = window

        self.rect = pyg.Rect(0, 0, 20, 20)
        self.rect.x = tile_placement[0]
        self.rect.y = tile_placement[1]

    def render(self):
        pyg.draw.rect(self.window, self.color, self.rect)

class Wall(Tile):

    def __init__(self, window, tile_placement):
        super().__init__(window, tile_placement)

        self.color = (60, 60, 60)

class Lava(Tile):

    def __init__(self, window, tile_placement):
        super().__init__(window, tile_placement)

        self.color = (200, 0, 0)
