import pygame as pyg
from pygame.sprite import Sprite

from random import randint

class Enemy(Sprite):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.image = pyg.image.load('PewPewGame/Images/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(100, 1100)
        self.rect.y = randint(100, 600)

        self.speed = 3

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def move(self):
        if self.moving_right: self.rect.x += self.speed
        if self.moving_left: self.rect.x -= self.speed
        if self.moving_up: self.rect.y -= self.speed
        if self.moving_down: self.rect.y += self.speed

    def render(self):
        self.window.blit(self.image, self.rect)
