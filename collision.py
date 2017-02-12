# coding: utf8
from config import *


class Collision:
    """
        self.ball_pos_x    position de la balle en x
        self.ball_pos_y    position de la balle en y
        self.ball_radius   rayon de la balle
        self.racket_pos_x  position x de la raquette
        self.racket_pos_y  position y de la raquette
        self.racket_width  largeur de la raquette
        self.racket_heigth hauteur de la raquette
    """
    def __init__(self, ball_pos_x, ball_pos_y, ball_radius, racket_pos_x, racket_pos_y, racket_width, racket_heigth):
        self.ball_pos_x    = ball_pos_x
        self.ball_pos_y    = ball_pos_y
        self.ball_radius   = ball_radius
        self.racket_pos_x  = racket_pos_x
        self.racket_pos_y  = racket_pos_y
        self.racket_width  = racket_width
        self.racket_heigth = racket_heigth

    """
        Test si la balle et la raquette sont au même endroit à 10 px près
    """
    def collision_racket_ball(self):
        if self.racket_pos_x - self.racket_width / 2 < self.ball_pos_x < self.racket_pos_x + self.racket_width / 2 and \
           self.racket_pos_y - self.racket_heigth / 2 - SPEED - SPEED / 2 < self.ball_pos_y < \
           self.racket_pos_y - self.racket_heigth / 2 + SPEED - SPEED / 2:

            Config.DOWN = False

    """
        Récupère les valeurs actuelles avant de tester si il y a une collision ou non
    """
    def up_date(self, ball_pos_x, ball_pos_y, racket_pos_x, racket_pos_y):
        self.ball_pos_x   = ball_pos_x
        self.ball_pos_y   = ball_pos_y
        self.racket_pos_x = racket_pos_x
        self.racket_pos_y = racket_pos_y

        self.collision_racket_ball()
