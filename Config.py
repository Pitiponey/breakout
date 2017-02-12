# coding: utf8

# Game screen
SCREEN_WIDTH   = 700
SCREEN_HEIGHT  = 500

# Racket config
SQUARE_WIDTH   = 100
SQUARE_HEIGHT  =  20
RACKET_COLOR   = (50, 228, 255)

# Play zone
PLAY_ZONE      = 100
LINE_HEIGHT    =   3
PLAY_ZONE_CALC = SCREEN_HEIGHT - PLAY_ZONE

# speed of the ball and max before hit the ground
SPEED          =  10
BALL_MAX       = 500
RADIUS         =  10


# Color
WHITE          = (255, 255, 255)


class Config:
    def __init__(self):
        pass
    DOWN  = False
    UP    = True
    RIGHT = True
    LEFT  = False

    SPEED_X =  5
    SPEED_Y =  5
    ANGLE   = 60

