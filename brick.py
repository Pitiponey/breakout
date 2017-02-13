# coding: utf8
from racket import *
from collision import *


class Brick:
    def __init__(self, screen, color, width = BRICK_WIDTH, height = BRICK_HEIGHT):
        self.screen      = screen
        self.color       = color
        self.width       = width
        self.height      = height
        self.list_bricks = []

    def add_brick(self, pos_x, pos_y, number):
        self.list_bricks.append([pos_x, pos_y, number])

    def create_bricks(self, number_of_bricks_in_line, number_of_lines):
        horizontal_space = (SCREEN_WIDTH - (number_of_bricks_in_line * BRICK_WIDTH)) / (number_of_bricks_in_line + 1)
        space_handler = 0
        vertical_space = SPACE_BETWEEN
        brick_number = 0
        for ligne in range(number_of_lines):
            for brick in range(number_of_bricks_in_line):
                brick_number += 1
                space_handler += horizontal_space
                self.add_brick(space_handler, vertical_space, brick_number)
                space_handler += BRICK_WIDTH

            space_handler = 0
            vertical_space += SPACE_BETWEEN

    def draw(self):
        for pos_x, pos_y, number in self.list_bricks:
            pygame.draw.rect(self.screen, self.color, pygame.Rect(pos_x, pos_y, self.width, self.height))

    def get_brick_list(self):
        return self.list_bricks

