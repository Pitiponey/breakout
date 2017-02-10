import cv2

class Racket():
    def __init__(self, pos_x, pos_y, width, height, img):
        self.pos_x  = pos_x
        self.pos_y  = pos_y
        self.width  = width
        self.height = height
        self.img    = img

    def changePositions(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def draw(self):
        cv2.rectangle(self.img, (self.pos_x - self.width, self.pos_y - self.height), (self.pos_x + self.width, self.pos_y + self.height),
                      (0, 0, 255), -1)
        return self.img


