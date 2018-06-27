import pygame as pyg
from random import randint

class Player():

    def __init__(self, window):
        self.window = window
        self.image = pyg.image.load('PewPewGame/Images/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(800, 1000)
        self.rect.y = randint(100, 200)

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
