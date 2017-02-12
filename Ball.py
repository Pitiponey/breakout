import pygame
from config import *


class Ball:
    def __init__(self, screen, color, pos_x, pos_y, radius, width):
        self.screen = screen
        self.color  = color
        self.pos_x  = pos_x
        self.pos_y  = pos_y
        self.radius = radius
        self.width  = width

    def increment(self):
        if config.DOWN:
            self.pos_y += SPEED
            if self.pos_y > BALL_MAX:
                config.DOWN = False
        else:
            self.pos_y -= SPEED
            if self.pos_y < 0:
                config.DOWN = True

    def draw(self):
        self.increment()
        pygame.draw.circle(self.screen, self.color, (self.pos_x, self.pos_y), self.radius, self.width)

    def set_x(self, x):
        self.pos_x = x

    def set_y(self, y):
        self.pos_y = y

    def get_y(self):
        return self.pos_y

    def get_x(self):
        return self.pos_x

    def get_radius(self):
        return self.radius
