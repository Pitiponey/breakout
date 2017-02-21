# coding: utf8
import pygame
from config import *
from math import sin, cos


class Ball:
    """
        self.screen = Écran d'affichage
        self.color  = Couleur de la balle
        self.pos_x  = Position x de la balle
        self.pos_y  = Position y de la balle
        self.radius = Rayon de la balle
        self.width  = Renplissage de la balle
    """
    def __init__(self, screen, color, pos_x, pos_y, radius, width):
        self.screen = screen
        self.color  = color
        self.pos_x  = pos_x
        self.pos_y  = pos_y
        self.radius = radius
        self.width  = width

    def increment(self):
        """
            Gère le sens de la balle, et inverse la direction
            Améliorations à faire : Gérer avec des angles et non 90°
        """
        Config.SPEED_Y = int(SPEED * cos(Config.ANGLE))
        Config.SPEED_X = int(SPEED * sin(Config.ANGLE))

        if Config.SPEED_Y < 0:
            Config.SPEED_Y *= -1

        if Config.SPEED_X > 0:
            Config.SPEED_X *= -1

        if Config.UP:
            self.pos_y += Config.SPEED_Y

        if Config.DOWN:
            self.pos_y -= Config.SPEED_Y

        if Config.LEFT:
            self.pos_x += Config.SPEED_X

        if Config.RIGHT:
            self.pos_x -= Config.SPEED_X

    def draw(self):
        """
            Récupère la nouvelle valeur de la balle et l'affiche
        """
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
