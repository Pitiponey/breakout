from config import *

class Collision():
    def __init__(self, ball_pos_x, ball_pos_y, ball_radius, racket_pos_x, racket_pos_y, racket_width, racket_heigth):
        self.ball_pos_x    = ball_pos_x
        self.ball_pos_y    = ball_pos_y
        self.ball_radius   = ball_radius
        self.racket_pos_x  = racket_pos_x
        self.racket_pos_y  = racket_pos_y
        self.racket_width  = racket_width
        self.racket_heigth = racket_heigth

    def up_date(self, ball_pos_x, ball_pos_y, racket_pos_x, racket_pos_y):
        self.ball_pos_x   = ball_pos_x
        self.ball_pos_y   = ball_pos_y
        self.racket_pos_x = racket_pos_x
        self.racket_pos_y = racket_pos_y

    def collision_racket_ball(self):
        if self.racket_pos_x - self.racket_width / 2 < self.ball_pos_x < self.racket_pos_x + self.racket_width / 2 and \
           self.racket_pos_y - self.racket_heigth / 2 - SPEED - SPEED / 2 < self.ball_pos_y < \
           self.racket_pos_y - self.racket_heigth / 2 + SPEED - SPEED / 2:
            
            config.DOWN = False
