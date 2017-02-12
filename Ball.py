import pygame
from config import *

class Ball():
    def __init__(self, screen, color, pos_x, pos_y, radius, width):
        self.screen = screen
        self.color  = color
        self.pos_x  = pos_x
        self.pos_y  = pos_y
        self.radius = radius
        self.width  = width

    def increment(self):
        self.pos_y += SPEED

        if self.pos_y > BALL_MAX:
            self.pos_y = 0

    def draw(self):
        self.increment()
        pygame.draw.circle(self.screen, self.color, (self.pos_x, self.pos_y), self.radius, self.width)

    def set_x(self, x):
        self.pos_x = x

    def set_y(self, y):
        self.pos_y = y