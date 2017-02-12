import pygame
from config import *


class Racket():
    def __init__(self, screen, color, pos_x = 30, pos_y= 30, width = 100, height = 20):
        self.screen = screen
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.pos_x - self.width / 2, self.pos_y - self.height / 2,
                                                              self.width, self.height))

    def set_x(self, x):
        self.pos_x = x

    def set_y(self, y):
        if y < PLAY_ZONE_CALC + SQUARE_HEIGHT / 2 + LINE_HEIGHT + 1:
            self.pos_y = PLAY_ZONE_CALC + SQUARE_HEIGHT / 2 + LINE_HEIGHT + 1
        else:
            self.pos_y = y