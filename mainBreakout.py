import cv2
import numpy as np
from Ball import *
from Racket import *
from Controller import *


def handle_event(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        if y < HAUTEUR_PIXEL + RACKET_HEIGTH / 2 + 5:
            y = HAUTEUR_PIXEL + RACKET_HEIGTH / 2 + 5

        racket.changePositions(x, y)

if __name__ == "__main__":
    img = np.zeros((WINDOW_WIDTH, WINDOW_HEIGTH, 3), np.uint8)
    cv2.rectangle(img, (0, 0), (WINDOW_WIDTH, 500), (0, 0, 0), -1)
    cv2.rectangle(img, (0, HAUTEUR_PIXEL), (WINDOW_WIDTH, WINDOW_HEIGTH), (50, 50, 50), -1)
    cv2.namedWindow("mouse")

    white_ball = Ball(150, 0, 10, img)
    racket = Racket(230, 460, RACKET_WIDTH, RACKET_HEIGTH, img)

    comparator = Colision(white_ball.get_pos_x, white_ball.get_pos_y, white_ball.get_radius(),
                          racket.get_pos_x(), racket.get_pos_y(), racket.get_width(), racket.get_height())

    cv2.setMouseCallback("mouse", handle_event)
    while 1:
        cv2.rectangle(img, (0, 0), (WINDOW_HEIGTH, HAUTEUR_PIXEL), (0, 0, 0), -1)
        img = white_ball.draw_ball()
        img = racket.draw()

        print comparator.Comparator()


        # Gestion des rebonds
        cv2.imshow("mouse", img)
        if cv2.waitKey(1) == 27:
            break
