# coding: utf8
import pygame
from config import *


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
            Gère la sens de la balle vers la haut ou le bas
        """
        if Config.DOWN:
            self.pos_y += SPEED
            if self.pos_y > BALL_MAX:
                Config.DOWN = False
        else:
            self.pos_y -= SPEED
            if self.pos_y < 0:
                Config.DOWN = True

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
