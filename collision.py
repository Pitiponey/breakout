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

    @staticmethod
    def calcul_rebound_angle(ball_impact):
        if ball_impact < 0:
            ball_impact *= -1

        inp = int(ball_impact / 9)

        if inp == 0:
            Config.ANGLE = 0
        elif inp == 1:
            Config.ANGLE = 50
        elif inp == 2:
            Config.ANGLE = 60
        elif inp == 3:
            Config.ANGLE = 70
        elif inp == 4:
            Config.ANGLE = 90
        else:
            Config.ANGLE = 80

    """
        Test si la balle et la raquette sont au même endroit à 10 px près
    """
    def collision_racket_ball(self):
        if self.racket_pos_x - self.racket_width / 2 < self.ball_pos_x + RADIUS / 2 < self.racket_pos_x + self.racket_width / 2 + RADIUS and \
           self.racket_pos_y - self.racket_heigth / 2 - SPEED * 2 < self.ball_pos_y < \
           self.racket_pos_y - self.racket_heigth / 2 + SPEED * 2:

            self.calcul_rebound_angle(self.racket_pos_x - self.ball_pos_x)

            if Config.UP:
                Config.UP = False
                Config.DOWN = True


    def collision_brick_ball(self, list_brick):
        for pos_x, pos_y, number in list_brick:
            #if self.ball_pos_x > pos_x and self.ball_pos_x < pos_x + BRICK_WIDTH and self.ball_pos_y > pos_y and self.ball_pos_y < pos_y + BRICK_HEIGHT:
            if pos_x < self.ball_pos_x - (RADIUS * 2) < pos_x + BRICK_WIDTH and pos_y < self.ball_pos_y - \
                    (RADIUS * 2) < pos_y + BRICK_HEIGHT:

                del list_brick[int(number) - 1]

                if Config.UP:
                    Config.UP = False
                    Config.DOWN = True

                if Config.DOWN:
                    Config.UP = True
                    Config.DOWN = False

                if Config.LEFT:
                    Config.RIGHT = True
                    Config.LEFT = False

                if Config.RIGHT:
                    Config.RIGHT = False
                    Config.LEFT = True

    """
        Récupère les valeurs actuelles avant de tester si il y a une collision ou non
    """
    def update(self, ball_pos_x, ball_pos_y, racket_pos_x, racket_pos_y, list_brick):
        self.ball_pos_x   = ball_pos_x
        self.ball_pos_y   = ball_pos_y
        self.racket_pos_x = racket_pos_x
        self.racket_pos_y = racket_pos_y

        self.collision_brick_ball(list_brick)
        self.collision_racket_ball()

    """
        Récupère les valeurs de la balle et calcul si on tape dans un mur
    """
    @staticmethod
    def collision_ball_wall(ball_pos_x, ball_pos_y):
        if Config.UP:
            if ball_pos_y > SCREEN_HEIGHT - RADIUS:
                Config.UP   = False
                Config.DOWN = True

        if Config.DOWN:
            if ball_pos_y < 0 + RADIUS:
                Config.UP   = True
                Config.DOWN = False

        if Config.LEFT:
            if ball_pos_x < 0 + RADIUS:
                Config.RIGHT = True
                Config.LEFT  = False

        if Config.RIGHT:
            if ball_pos_x > SCREEN_WIDTH - RADIUS:
                Config.RIGHT = False
                Config.LEFT  = True
