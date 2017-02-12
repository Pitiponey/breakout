# coding: utf8
import pygame
from config import *


class Racket:
    """
        self.screen = Écran d'affichage
        self.color = Couleur de la raquette
        self.pos_x = Position x de la raquette
        self.pos_y = Position y de la raquette
        self.width = Largeur de la raquette
        self.height = Hauteur de la raquette
    """
    def __init__(self, screen, color, pos_x = 30, pos_y= 300, width = 100, height = 20):
        self.screen = screen
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

    def draw(self):
        """
            Dessine le rectangle
        """
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.pos_x - self.width / 2, self.pos_y - self.height / 2,
                                                              self.width, self.height))

    def set_x(self, x):
        self.pos_x = x

    def set_y(self, y):
        """
            Test si la raquette est dans la zone de jeu, sinon l'affiche le plus haut possible
        """
        if y < PLAY_ZONE_CALC + SQUARE_HEIGHT / 2 + LINE_HEIGHT + 1:
            self.pos_y = PLAY_ZONE_CALC + SQUARE_HEIGHT / 2 + LINE_HEIGHT + 1
        else:
            self.pos_y = y

    def get_y(self):
        return self.pos_y

    def get_x(self):
        return self.pos_x

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
