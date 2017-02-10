import cv2
import numpy as np
from Config import *
from Ball import Ball
from Racket import Racket


def handle_event(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        if y > HAUTEUR_PIXEL:
            print "move"

if __name__ == "__main__":
    img = np.zeros((WINDOW_WIDTH, WINDOW_HEIGTH, 3), np.uint8)
    cv2.rectangle(img, (0, 0), (WINDOW_WIDTH, WINDOW_HEIGTH), (0, 0, 0), -1)
    cv2.rectangle(img, (0, HAUTEUR_PIXEL), (WINDOW_WIDTH, WINDOW_HEIGTH), (50, 50, 50), -1)
    cv2.namedWindow("mouse")

    white_ball = Ball(150, 0, 10, img)
    racket     = Racket(50, 10, img)

    cv2.setMouseCallback("mouse", handle_event)
    while 1:
        cv2.rectangle(img, (0, 0), (WINDOW_HEIGTH, HAUTEUR_PIXEL), (0, 0, 0), -1)
        img = white_ball.draw_ball()
        # Lancement de la balle
        # Gestion des rebonds
        cv2.imshow("mouse", img)
        if cv2.waitKey(1) == 27:
            break
