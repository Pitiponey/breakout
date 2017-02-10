

class Colision():
    def __init__(self, ball_pos_x, ball_pos_y, ball_radius, racket_pos_x, racket_pos_y, racket_width, racket_heigt):
        self.ball_pos_x   = ball_pos_x
        self.ball_pos_y   = ball_pos_y
        self.ball_radius  = ball_radius
        self.racket_pos_x = racket_pos_x
        self.racket_pos_y = racket_pos_y
        self.racket_width = racket_width
        self.racket_heigt = racket_heigt

    def Comparator(self):
        return False
