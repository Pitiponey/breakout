# coding: utf8
from ball import *
from racket import *
from collision import *


class Brick():
    def __init__(self, screen, color, width = BRICK_WIDTH, height = BRICK_HEIGHT):
        self.screen      = screen
        self.color       = color
        self.width       = width
        self.height      = height
        self.list_bricks = []

    def add_brick(self, pos_x, pos_y):
        self.list_bricks.append([pos_x, pos_y])

    def create_bricks(self, number_of_bricks_in_line, number_of_lines):
        pass

    def draw(self):
        for pos_x, pos_y in self.list_bricks:
            pygame.draw.rect(self.screen, self.color, pygame.Rect(pos_x, pos_y, self.width, self.height))
