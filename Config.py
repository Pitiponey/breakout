# coding: utf8

# Game screen
SCREEN_WIDTH   = 700
SCREEN_HEIGHT  = 500

# Racket config
SQUARE_WIDTH   = 100
SQUARE_HEIGHT  =  20

# Play zone
PLAY_ZONE      = 100
LINE_HEIGHT    =   3
PLAY_ZONE_CALC = SCREEN_HEIGHT - PLAY_ZONE

# Ball configuration
SPEED          =  10
RADIUS         =  10
FILL           = 0

# Brick configuration
BRICK_WIDTH    = 50
BRICK_HEIGHT   = 25
NUMBER_BRICKS  = 10
NUMBER_LINE    =  5

# Color
WHITE          = (255, 255, 255)
BLACK          = (0, 0, 0)
BRICK_COLOR    = (0, 0, 255)
RACKET_COLOR   = (50, 228, 255)

# Config general
NUMBER_FPS     = 60

class Config:
    def __init__(self):
        pass
    DOWN  = True
    UP    = False
    RIGHT = False
    LEFT  = True

    SPEED_X = SPEED
    SPEED_Y = SPEED
    ANGLE   = 0

