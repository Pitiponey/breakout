import cv2
from Config import *


class Ball():
    def __init__(self, pos_x, pos_y, radius, img):
        self.pos_x  = pos_x
        self.pos_y  = pos_y
        self.radius = radius
        self.img    = img

    def move_ball(self):
        self.pos_y += 2
        if self.pos_y > WINDOW_HEIGTH:
            self.pos_y = 0

    def draw_ball(self):
        self.move_ball()
        cv2.rectangle(self.img, (0, HAUTEUR_PIXEL), (WINDOW_WIDTH, WINDOW_HEIGTH), (50, 50, 50), -1)
        cv2.circle(self.img, (self.pos_x, int(self.pos_y)), self.radius, (255, 255, 255), -1)

        return self.img
